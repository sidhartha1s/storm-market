"""Transcribe reels on CPU with faster-whisper. Usage: python3 transcribe.py <model> <lang|auto> <mp4> [mp4...]
Writes <mp4>.tr.json: [{start, end, text}] per segment, plus detected language."""
import json, sys, os
from faster_whisper import WhisperModel

model = WhisperModel(sys.argv[1], device="cpu", compute_type="int8", cpu_threads=6)
lang = None if sys.argv[2] == "auto" else sys.argv[2]
for p in sys.argv[3:]:
    out = p + ".tr.json"
    if os.path.exists(out):
        continue
    segs, info = model.transcribe(p, language=lang, vad_filter=True)
    rows = [{"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()} for s in segs]
    json.dump({"language": info.language, "segments": rows}, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(os.path.basename(p), info.language, len(rows), "segments", flush=True)
