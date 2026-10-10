# -*- coding: utf-8 -*-
"""
配音 + 字幕生成：从 sources/dialogues.json 生成音频与 WebVTT 字幕。

输出（每段素材四个文件，同目录同名）：
    <mediaRoot>/<dir>/<name>.mp3        整段对话（逐句拼接）
    <mediaRoot>/<dir>/<name>.vtt        中英双语字幕
    <mediaRoot>/<dir>/<name>.en.vtt     纯英文字幕
    <mediaRoot>/<dir>/<name>.zh.vtt     纯中文字幕

同时把每句的 start / end 与整段的 duration **回写**到 sources/dialogues.json
（时间轴由音频决定，属于脚本维护字段，不要手改）。

用法：
    python tools/gen_tts.py --check              只检查音色是否可用，不合成
    python tools/gen_tts.py --dry-run            列出将要合成的段落与音色分配
    python tools/gen_tts.py --missing            只给还没有 mp3 的段落配音
    python tools/gen_tts.py --only 0003,0007     只重做指定段落
    python tools/gen_tts.py --force              全部重做
    python tools/gen_tts.py --rate -10%          整体降速 10%

前提：pip install edge-tts（可选 imageio-ffmpeg，用于校准时长）
"""
from __future__ import annotations

import argparse
import asyncio
import json
import os
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(REPO, "sources", "dialogues.json")
BYTES_PER_SEC_FALLBACK = 6000.0   # 无 ffmpeg 时的经验值


def load_doc() -> dict:
    with open(SRC, encoding="utf-8") as f:
        return json.load(f)


def save_doc(doc: dict) -> None:
    with open(SRC, "w", encoding="utf-8", newline="\n") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
        f.write("\n")


def assign_voices(doc: dict, item: dict) -> dict:
    """按首次出场顺序在同性音色池里轮转，保证同样的文本永远得到同样的音色。"""
    sets = doc.get("voices", {})
    pool = sets.get(item.get("voiceSet") or "en-IN") or sets.get("en-IN") or {}
    genders = doc.get("speakers", {})
    # 同一角色在整库范围固定音色：doc.voiceOf 优先，item.voiceOf 可覆盖
    fixed = dict(doc.get("voiceOf") or {})
    fixed.update(item.get("voiceOf") or {})
    used = {"F": 0, "M": 0}
    mapping: dict[str, str] = {}
    unknown: list[str] = []
    for ln in item["lines"]:
        sp = ln.get("sp", "")
        if not sp or sp == "旁白" or sp in mapping:
            continue
        if sp in fixed:
            mapping[sp] = fixed[sp]
            continue
        g = genders.get(sp)
        if g not in ("F", "M"):
            g = "M"
            unknown.append(sp)
        lst = pool.get("female" if g == "F" else "male") or []
        if not lst:
            raise SystemExit(f"音色集 {item.get('voiceSet')} 缺少 {'female' if g == 'F' else 'male'} 池")
        mapping[sp] = lst[used[g] % len(lst)]
        used[g] += 1
    if unknown:
        print(f"  ! 未声明性别的说话人，按男声处理：{sorted(set(unknown))}")
    return mapping


async def synth(text: str, voice: str, rate: str) -> bytes:
    import edge_tts
    buf = bytearray()
    async for ch in edge_tts.Communicate(text, voice, rate=rate).stream():
        if ch["type"] == "audio":
            buf += ch["data"]
    return bytes(buf)


def fmt_ts(t: float) -> str:
    h = int(t // 3600)
    m = int(t % 3600 // 60)
    return f"{h:02d}:{m:02d}:{t % 60:06.3f}"


def ffmpeg_exe() -> str | None:
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return None


def real_duration(path: str) -> float | None:
    """用 ffmpeg 读出真实时长，用于把「按字节估算」校准为准确时间轴。"""
    exe = ffmpeg_exe()
    if not exe:
        return None
    try:
        r = subprocess.run([exe, "-hide_banner", "-i", path], capture_output=True, text=True)
    except OSError:
        return None
    for ln in (r.stderr or "").splitlines():
        if "Duration:" in ln:
            part = ln.split("Duration:")[1].split(",")[0].strip()
            h, m, s = part.split(":")
            return int(h) * 3600 + int(m) * 60 + float(s)
    return None


async def build_one(doc: dict, item: dict, rate: str, dry: bool) -> dict:
    folder = os.path.join(REPO, doc.get("mediaRoot", "audio"), item["dir"])
    base = item["audio"].rsplit(".", 1)[0]
    mp3 = os.path.join(folder, item["audio"])
    vmap = assign_voices(doc, item)
    narrator = (doc.get("voices", {}).get(item.get("voiceSet") or "en-IN") or {}).get("narrator")

    if dry:
        print(f"[{item['id']}] {item['title']}")
        print(f"    输出 {os.path.relpath(mp3, REPO)}")
        for k, v in vmap.items():
            print(f"    说话人 {k:8s} -> {v}")
        print(f"    旁白   -> {narrator}")
        return {}

    os.makedirs(folder, exist_ok=True)
    parts: list[bytes] = []
    sizes: list[int] = []
    for ln in item["lines"]:
        voice = narrator if ln.get("sp") == "旁白" else vmap[ln["sp"]]
        line_rate = item.get("rateOf", {}).get(ln.get("sp"), rate)
        blob = await synth(ln["en"], voice, line_rate)
        parts.append(blob)
        sizes.append(len(blob))

    with open(mp3, "wb") as f:
        f.write(b"".join(parts))

    total_bytes = sum(sizes)
    dur = real_duration(mp3)
    if dur and dur > 0:
        bps = total_bytes / dur
        source = f"ffmpeg 校准 {bps:.0f} B/s"
    else:
        bps = BYTES_PER_SEC_FALLBACK
        dur = total_bytes / bps
        source = f"经验值 {bps:.0f} B/s（无 ffmpeg）"

    t = 0.0
    for ln, n in zip(item["lines"], sizes):
        d = n / bps
        ln["start"] = round(t, 3)
        ln["end"] = round(t + d, 3)
        t += d
    item["duration"] = round(dur, 2)

    def write_vtt(name: str, lang: str) -> None:
        with open(os.path.join(folder, name), "w", encoding="utf-8", newline="\n") as f:
            f.write("WEBVTT\n\n")
            for i, c in enumerate(item["lines"], 1):
                f.write(f"{i}\n{fmt_ts(c['start'])} --> {fmt_ts(c['end'])}\n")
                if lang == "en":
                    f.write(f"{c['sp']}: {c['en']}\n\n")
                elif lang == "zh":
                    f.write(f"{c['zh']}\n\n")
                else:
                    f.write(f"{c['sp']}: {c['en']}\n{c['zh']}\n\n")

    write_vtt(base + ".vtt", "both")
    write_vtt(base + ".en.vtt", "en")
    write_vtt(base + ".zh.vtt", "zh")

    print(f"[{item['id']}] {item['title']}")
    print(f"    {item['audio']}  {dur:6.1f}s  {len(item['lines'])} 句  {total_bytes//1024} KB  ({source})")
    print("    音色 " + " · ".join(f"{k}={v.replace('en-', '')}" for k, v in vmap.items())
          + (f" · 旁白={narrator.replace('en-', '')}" if narrator else ""))
    return item


async def run(args: argparse.Namespace) -> int:
    doc = load_doc()
    items = doc["dialogues"]
    media_root = doc.get("mediaRoot", "audio")

    if args.check:
        import edge_tts
        avail = {v["ShortName"] for v in await edge_tts.list_voices()}
        want: set[str] = set()
        for cfg in doc.get("voices", {}).values():
            for k in ("female", "male"):
                want.update(cfg.get(k) or [])
            if cfg.get("narrator"):
                want.add(cfg["narrator"])
        missing = sorted(want - avail)
        print(f"音色配置 {len(want)} 个，可用 {len(want) - len(missing)} 个")
        if missing:
            print("  不可用：" + ", ".join(missing))
            return 1
        print("  全部可用。样例：" + ", ".join(sorted(want)[:4]))
        return 0

    todo = items
    if args.only:
        want = {s.strip() for s in args.only.split(",") if s.strip()}
        todo = [x for x in items if x["id"] in want]
        if not todo:
            print("--only 没有匹配到任何段落")
            return 1
    elif args.missing:
        todo = [x for x in items
                if not os.path.isfile(os.path.join(REPO, media_root, x["dir"], x["audio"]))]
    elif not args.force:
        print("未指定范围：默认全部重做。加 --missing 只补缺失，加 --only ID 指定段落。")

    if not todo:
        print("没有需要处理的段落。")
        return 0

    print(f"{'[试运行] ' if args.dry_run else ''}待处理 {len(todo)} 段，语速 {args.rate}\n")
    for it in todo:
        await build_one(doc, it, args.rate, args.dry_run)

    if not args.dry_run:
        save_doc(doc)
        print(f"\n已回写时间轴到 {os.path.relpath(SRC, REPO)}")
        print("下一步：python tools/build.py")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="配音并生成字幕（时间轴自动回写）")
    ap.add_argument("--check", action="store_true", help="只校验音色可用性")
    ap.add_argument("--dry-run", action="store_true", help="只列出计划，不合成")
    ap.add_argument("--missing", action="store_true", help="只处理还没有音频的段落")
    ap.add_argument("--only", default="", help="只处理指定 id，逗号分隔")
    ap.add_argument("--force", action="store_true", help="全部重做")
    ap.add_argument("--rate", default="+0%", help="语速，如 -10%% / +15%%")
    return asyncio.run(run(ap.parse_args()))


if __name__ == "__main__":
    sys.exit(main())
