from __future__ import annotations

import argparse
import asyncio
import copy
import json
import re
import subprocess
import tempfile
from pathlib import Path

import build
import gen_tts

ROOT = Path(__file__).resolve().parent.parent
APPROVED_VOICES = {
    "Priya": "en-IN-NeerjaNeural",
    "Raj": "en-IN-PrabhatNeural",
    "Anika": "en-IN-NeerjaNeural",
    "Lukas": "de-DE-FlorianMultilingualNeural",
    "Hannah": "de-DE-SeraphinaMultilingualNeural",
}


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def save_json(path: Path, value: dict) -> None:
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=path.parent, delete=False, suffix=".tmp"
    ) as handle:
        json.dump(value, handle, ensure_ascii=False, indent=1)
        handle.write("\n")
        temporary = Path(handle.name)
    temporary.replace(path)


def spoken_seconds(executable: str, audio: Path, lines: list[dict]) -> dict[str, float]:
    result = subprocess.run(
        [executable, "-hide_banner", "-i", str(audio), "-af",
         "silencedetect=noise=-40dB:d=0.12", "-f", "null", "-"],
        capture_output=True, text=True, check=True,
    )
    silence = []
    beginning = None
    for message in result.stderr.splitlines():
        start = re.search(r"silence_start: ([0-9.]+)", message)
        end = re.search(r"silence_end: ([0-9.]+)", message)
        if start:
            beginning = float(start.group(1))
        if end and beginning is not None:
            silence.append((beginning, float(end.group(1))))
            beginning = None
    if beginning is not None:
        silence.append((beginning, lines[-1]["end"]))
    speakers = {}
    for line in lines:
        start, end = line["start"], line["end"]
        quiet = sum(max(0.0, min(end, stop) - max(start, begin))
                    for begin, stop in silence)
        speakers[line["sp"]] = speakers.get(line["sp"], 0.0) + max(0.0, end - start - quiet)
    return speakers


async def run(args: argparse.Namespace) -> None:
    executable = gen_tts.ffmpeg_exe()
    if not executable:
        raise RuntimeError("imageio-ffmpeg is required for media and spoken-time validation")
    draft_path = ROOT / "sources" / "drafts" / f"{args.scenario}.json"
    draft = read_json(draft_path)
    source_path = ROOT / "sources" / "dialogues.json"
    bank_path = ROOT / "sources" / "phrases.json"
    source = read_json(source_path)
    bank = read_json(bank_path)
    incoming = {item["id"] for item in draft["dialogues"]}
    if args.skip_published and incoming <= {item["id"] for item in source["dialogues"]}:
        print(f"{args.scenario}: already published", flush=True)
        return
    if incoming & {item["id"] for item in source["dialogues"]}:
        raise RuntimeError("Dialogue IDs already published; existing media will not be overwritten")
    if draft["series"]["id"] in {series["id"] for series in source.get("series", [])}:
        raise RuntimeError("Series already published")
    definitions = {phrase["id"]: phrase for phrase in bank["phrases"]}
    for phrase in draft["phraseDefinitions"]:
        existing = definitions.get(phrase["id"])
        if existing is not None and any(existing.get(key) != value for key, value in phrase.items()):
            raise RuntimeError(f"Conflicting phrase definition: {phrase['id']}")
        if existing is None:
            bank["phrases"].append(copy.deepcopy(phrase))
            definitions[phrase["id"]] = phrase
    prepared = copy.deepcopy(source)
    prepared.setdefault("series", []).append(copy.deepcopy(draft["series"]))
    voices = {}
    rates = {}
    for name, speaker in draft["speakers"].items():
        voice = speaker.get("voice") or APPROVED_VOICES.get(name)
        if not voice:
            raise RuntimeError(f"No approved voice for {name}")
        india = speaker["accent"] == "en-IN"
        if india != voice.startswith("en-IN-"):
            raise RuntimeError(f"Accent and voice mismatch for {name}")
        voices[name] = voice
        rates[name] = args.india_rate if india else args.german_rate
        prepared.setdefault("speakers", {})[name] = "M" if name in ("Raj", "Lukas") else "F"
    rendered = []
    spoken = {}
    for raw in draft["dialogues"]:
        item = copy.deepcopy(raw)
        base = f"{item['id']}-{item['title'].split('：')[0]}"
        item.update({"group": draft["series"]["group"], "domain": draft["series"]["domain"],
                     "series": draft["series"]["id"], "parts": 10, "seq": item["part"],
                     "scene": item["premise"], "dir": f"{draft['series']['domain']}/{base}",
                     "audio": f"{base}.mp3", "accent": "印度英语 60% / 德国英语 40%（场景发声时长）",
                     "voiceSet": "en-IN", "voiceOf": voices, "rateOf": rates,
                     "roles": [f"{name}（{speaker['role']}）" for name, speaker in draft["speakers"].items()],
                     "tags": [draft["series"]["domain"], item["stage"]]})
        for line in item["lines"]:
            line["role"] = draft["speakers"][line["sp"]]["role"]
        folder = ROOT / prepared.get("mediaRoot", "audio") / item["dir"]
        checkpoint = folder / "rendered.json"
        if checkpoint.exists():
            cached = read_json(checkpoint)
            if (cached.get("voiceOf") != voices or cached.get("rateOf") != rates
                    or [line["en"] for line in cached["lines"]] != [line["en"] for line in item["lines"]]
                    or [line["zh"] for line in cached["lines"]] != [line["zh"] for line in item["lines"]]):
                raise RuntimeError(f"Checkpoint changed: {item['id']}; review it before resuming")
            item = cached
            print(f"[{item['id']}] Reusing completed synthesis", flush=True)
        else:
            for attempt in range(4):
                try:
                    await gen_tts.build_one(prepared, item, "+0%", False)
                    break
                except Exception:
                    if attempt == 3:
                        raise
                    print(f"[{item['id']}] Retrying synthesis ({attempt + 1}/3)", flush=True)
            save_json(checkpoint, item)
        if item["duration"] > 120:
            raise RuntimeError(f"{item['id']} exceeds 120 seconds")
        times = spoken_seconds(executable, folder / item["audio"], item["lines"])
        for name, duration in times.items():
            spoken[name] = spoken.get(name, 0.0) + duration
        rendered.append(item)
        print(f"[{item['id']}] Decoded and speech measured", flush=True)
    india_seconds = sum(duration for name, duration in spoken.items()
                        if draft["speakers"][name]["accent"] == "en-IN")
    total = sum(spoken.values())
    ratio = india_seconds / total if total else 0
    report = {"scenario": args.scenario, "voices": voices, "rates": rates,
              "speakingSecondsByRole": {name: round(value, 3) for name, value in spoken.items()},
              "indianSpeakingShare": ratio, "totalSpeakingSeconds": total,
              "measurement": "ffmpeg silencedetect -40dB, silence >=0.12s excluded; approximate acoustic speech time",
              "segments": [{"id": item["id"], "duration": item["duration"]} for item in rendered]}
    report_path = ROOT / "audio" / f"{args.scenario}-voice-report.json"
    save_json(report_path, report)
    print(f"Indian spoken share: {ratio:.2%}", flush=True)
    if not 0.55 <= ratio <= 0.65:
        raise RuntimeError("Accent ratio outside 55%-65%; source not published")
    prepared["dialogues"].extend(rendered)
    errors = build.validate(prepared)
    if errors:
        raise RuntimeError("\n".join(errors))
    metrics = build.metrics(prepared)
    for row in metrics["rows"]:
        if row["id"] not in incoming:
            continue
        core = sum(1 for spec in next(item for item in rendered if item["id"] == row["id"])["phrases"]
                   if (spec.split(":")[1] if ":" in spec else definitions[spec]["level"]) == "core")
        if not (5 <= row["wps"] <= 9.5 and row["short"] >= 0.5
                and row["indian"] >= 1 and row["banned"] == 0 and 1 <= core <= 3):
            raise RuntimeError(f"Text acceptance failed: {row['id']}")
    save_json(bank_path, bank)
    save_json(source_path, prepared)
    print(f"Published {len(rendered)} source records. Run tools/build.py --check, then tools/build.py.", flush=True)


async def batch(args: argparse.Namespace) -> None:
    scenarios = [f"S{number:02}" for number in range(4, 51)] if args.scenario == "all" else [args.scenario]
    failures = {}
    for scenario in scenarios:
        current = copy.copy(args)
        current.scenario = scenario
        try:
            await run(current)
        except Exception as error:
            failures[scenario] = str(error)
            print(f"{scenario}: FAILED: {error}", flush=True)
    if args.scenario == "all":
        save_json(ROOT / "audio" / "batch-report.json", {"scenarios": scenarios, "failures": failures})
    if failures:
        raise RuntimeError(f"{len(failures)} scenario(s) failed: {failures}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("scenario", choices=["all"] + [f"S{number:02}" for number in range(3, 51)])
    parser.add_argument("--skip-published", action="store_true")
    parser.add_argument("--india-rate", default="+10%")
    parser.add_argument("--german-rate", default="-15%")
    asyncio.run(batch(parser.parse_args()))