#!/usr/bin/env python3
"""Transcribe every media/broadcast/*.mp4 clip with word timestamps.
Writes research/transcripts/<clipname>.json (raw) and .md (readable, timecoded).

Usage: <JP-market .venv python> transcribe_clips.py
"""
import os, sys, json, glob
from pathlib import Path

EP = Path(__file__).resolve().parent.parent
CLIPS_DIR = EP / "media" / "broadcast"
OUT_DIR = EP / "research" / "transcripts"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Borrow CUDA DLLs from JP-market's pocket venv (same trick as JP-market/engine/transcribe.py) --
# this .venv has no torch/CUDA runtime of its own.
TORCH_LIB = Path("C:/Users/Sidhartha/Automation Projects/JP-market/.venv-pocket/Lib/site-packages/torch/lib")
have_dlls = TORCH_LIB.is_dir()
if have_dlls:
    os.environ["PATH"] = str(TORCH_LIB) + os.pathsep + os.environ.get("PATH", "")

from faster_whisper import WhisperModel
import ctranslate2

try:
    cuda_ok = have_dlls and ctranslate2.get_cuda_device_count() > 0
except Exception:
    cuda_ok = False
device = "cuda" if cuda_ok else "cpu"
compute_type = "int8_float16" if cuda_ok else "int8"
print(f"device={device} compute_type={compute_type}", flush=True)

model = WhisperModel("small.en", device=device, compute_type=compute_type)


def fmt_ts(t):
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return f"{h:02d}:{m:02d}:{s:05.2f}"


clips = sorted(glob.glob(str(CLIPS_DIR / "*.mp4")))
print(f"{len(clips)} clips found", flush=True)

for i, clip_path in enumerate(clips, 1):
    clip = Path(clip_path)
    name = clip.stem
    json_out = OUT_DIR / f"{name}.json"
    md_out = OUT_DIR / f"{name}.md"
    if json_out.exists():
        print(f"[{i}/{len(clips)}] SKIP (exists) {name}", flush=True)
        continue
    print(f"[{i}/{len(clips)}] transcribing {name} ...", flush=True)
    try:
        segments, info = model.transcribe(
            str(clip), word_timestamps=True, beam_size=5,
            condition_on_previous_text=False,
        )
        segments = list(segments)
    except Exception as e:
        print(f"  !! FAILED {name}: {e}", flush=True)
        continue

    seg_list = []
    for seg in segments:
        words = [
            {"word": w.word.strip(), "start": round(w.start, 3), "end": round(w.end, 3)}
            for w in (seg.words or [])
        ]
        seg_list.append({
            "start": round(seg.start, 3), "end": round(seg.end, 3),
            "text": seg.text.strip(), "words": words,
        })

    data = {
        "clip": name, "duration": round(info.duration, 3),
        "language": info.language, "segments": seg_list,
    }
    json_out.write_text(json.dumps(data, indent=2), encoding="utf-8")

    lines = [f"# {name}", "", f"Duration: {info.duration:.2f}s", ""]
    for seg in seg_list:
        lines.append(f"[{fmt_ts(seg['start'])} - {fmt_ts(seg['end'])}] {seg['text']}")
    md_out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  -> {info.duration:.1f}s, {len(seg_list)} segments", flush=True)

print("done", flush=True)
