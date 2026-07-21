#!/usr/bin/env python3
"""Per-segment word timestamps via faster-whisper (offline, small.en cached).
Run with JP-market .venv python. Usage: python transcribe_episode.py episodes/<slug>
Outputs audio/<id>.words.json: [{"text","start","end"}, ...] per segment.
"""
import json
import sys
from pathlib import Path

ep = Path(sys.argv[1])
from faster_whisper import WhisperModel  # noqa: E402

model = WhisperModel("small.en", device="cpu", compute_type="int8")
for wav in sorted((ep / "audio").glob("*.wav")):
    out = wav.with_suffix(".words.json")
    if out.exists():
        continue
    segments, _ = model.transcribe(str(wav), word_timestamps=True, language="en")
    words = [{"text": w.word.strip(), "start": round(w.start, 3), "end": round(w.end, 3)}
             for s in segments for w in (s.words or [])]
    out.write_text(json.dumps(words), encoding="utf-8")
    print(f"{wav.stem}: {len(words)} words, last end {words[-1]['end'] if words else 0}s", flush=True)
print("DONE")
