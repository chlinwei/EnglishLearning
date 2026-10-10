from __future__ import annotations

import asyncio
import html
import json
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "audio" / "voice-samples"
TEXT = (
    "Okay, just to confirm, the disk is filling up, right? "
    "We've paused the noisy job. That should buy us time. "
    "Please keep an eye on the queue. "
    "We'll check the logs before restarting anything."
)
TRANSLATION = "好，我确认一下，磁盘快被占满了，对吧？我们暂停了产生大量日志的任务，这应该能争取时间。请留意队列。我们会先检查日志，不直接重启。"
VOICES = [
    ("en-IN-PrabhatNeural", "印度英语 · 男声", "印度音色试听"),
    ("en-IN-NeerjaNeural", "印度英语 · 女声", "印度音色试听"),
    ("de-DE-FlorianMultilingualNeural", "德国多语言候选 · 男声", "英语口音待试听确认"),
    ("de-DE-SeraphinaMultilingualNeural", "德国多语言候选 · 女声", "英语口音待试听确认"),
]


async def main() -> None:
    available = {voice["ShortName"] for voice in await edge_tts.list_voices()}
    missing = [voice for voice, _, _ in VOICES if voice not in available]
    if missing:
        raise RuntimeError(f"Unavailable voices: {missing}")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    samples = []
    for voice, label, status in VOICES:
        target = OUTPUT / f"{voice}.mp3"
        await edge_tts.Communicate(TEXT, voice, rate="+0%").save(str(target))
        size = target.stat().st_size
        if size == 0:
            raise RuntimeError(f"Empty audio: {voice}")
        samples.append({"voice": voice, "label": label, "status": status,
                        "file": target.name, "bytes": size})
        print(f"{voice}: {size} bytes", flush=True)
    metadata = {"purpose": "voice audition, not a published dialogue",
                "english": TEXT, "chinese": TRANSLATION,
                "germanEnglishAccentApproved": False, "samples": samples}
    (OUTPUT / "samples.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    tracks = "\n".join(
        f'<section><h2>{html.escape(sample["label"])}</h2>'
        f'<p>{html.escape(sample["voice"])} · {html.escape(sample["status"])}</p>'
        f'<audio controls preload="metadata" src="{sample["file"]}"></audio></section>'
        for sample in samples
    )
    page = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>会议英语 · 音色试听</title>
<style>
body{{margin:0;background:#f4f7f7;color:#182b27;font-family:"Microsoft YaHei",sans-serif;line-height:1.7}}
main{{max-width:820px;margin:auto;padding:28px 20px}}
h1{{font-size:26px;margin:0 0 20px}}h2{{font-size:18px;margin:0}}
section{{padding:20px 0;border-top:1px solid #cbd6d2}}
p{{overflow-wrap:anywhere;margin:8px 0 16px}}section p{{font-size:13px;color:#4a605a}}
audio{{display:block;width:100%;max-width:580px;height:54px}}
</style>
</head>
<body><main>
<h1>会议英语 · 音色试听</h1>
<p>{html.escape(TEXT)}</p>
<p>{html.escape(TRANSLATION)}</p>
{tracks}
</main></body></html>
'''
    (OUTPUT / "index.html").write_text(page, encoding="utf-8")
    print(f"Audition page: {OUTPUT / 'index.html'}", flush=True)


if __name__ == "__main__":
    asyncio.run(main())