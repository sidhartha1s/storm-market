"""Per-segment TTS for this episode: audio/<id>.txt -> audio/_raw/<id>.wav (pocket-TTS clone)
-> audio/<id>.wav (atempo 1.10, 48 kHz; documentaries run 1.10 per script-os.md)
-> audio/<id>.words.json (faster-whisper small.en on the SPED wav; tempo before timing) -> audio/manifest.json.
Run with the JP-market pocket venv python. Skips segments whose sped wav already exists (delete the wav
and words.json before re-synthesising a changed segment).
"""
import json, os, subprocess, sys, time, hashlib
from pathlib import Path

ep = Path(__file__).resolve().parent.parent
repo = ep.parent.parent
import yaml
ext = yaml.safe_load((repo / "config.yaml").read_text(encoding="utf-8"))["external"]
voice = ext["voice_ref"]
assert hashlib.md5(open(voice, "rb").read()).hexdigest() == "2d8ea8f14763932f3f76da67d7fd1612", "voice ref md5 mismatch"

audio = ep / "audio"
raw = audio / "_raw"
raw.mkdir(exist_ok=True)
only = set(sys.argv[1].split(",")) if len(sys.argv) > 1 else None
txts = sorted(p for p in audio.glob("*.txt") if not only or p.stem in only)
print(f"[tts_run] {len(txts)} segments", flush=True)

from faster_whisper import WhisperModel
model = WhisperModel("small.en", device="cpu", compute_type="int8")

manifest = json.loads((audio / "manifest.json").read_text(encoding="utf-8")) if (audio / "manifest.json").exists() else {}
for txt in txts:
    sid = txt.stem
    rwav, swav, words = raw / f"{sid}.wav", audio / f"{sid}.wav", audio / f"{sid}.words.json"
    if not swav.exists():
        if not rwav.exists():
            for attempt in (1, 2):
                r = subprocess.run([ext["pocket_venv_python"], ext["tts_clone_py"], "--text-file", str(txt),
                                    "--out", str(rwav), "--voice", voice],
                                   env={**os.environ, "PYTHONUTF8": "1", "PYTHONUNBUFFERED": "1"},
                                   capture_output=True, text=True)
                if r.returncode == 0 and rwav.exists():
                    break
                print(f"[tts_run] [FALLBACK] {sid} attempt {attempt} exit {r.returncode}: {r.stderr[-300:]}", flush=True)
            else:
                sys.exit(f"[tts_run] FAIL {sid} after retry")
        r = subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(rwav), "-filter:a", "atempo=1.10",
                            "-ar", "48000", str(swav)], capture_output=True, text=True)
        if r.returncode != 0:
            sys.exit(f"[tts_run] ffmpeg atempo failed on {sid}: {r.stderr[-300:]}")
    if not words.exists():
        segments, _ = model.transcribe(str(swav), word_timestamps=True, language="en")
        w = [{"text": x.word.strip(), "start": round(x.start, 3), "end": round(x.end, 3)}
             for s in segments for x in (s.words or [])]
        words.write_text(json.dumps(w), encoding="utf-8")
    d = None
    for _ in range(4):
        out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                              "default=nw=1:nk=1", str(swav)], capture_output=True, text=True).stdout.strip()
        if out:
            d = float(out); break
        time.sleep(3)
    n = len(txt.read_text(encoding="utf-8").split())
    manifest[sid] = {"wav": f"audio/{sid}.wav", "duration": round(d, 3), "words": n,
                     "wpm": round(n / d * 60, 1) if d else None}
    (audio / "manifest.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    print(f"[tts_run] {sid}: {d:.1f}s {n}w {manifest[sid]['wpm']} wpm", flush=True)

total = sum(v["duration"] for v in manifest.values())
print(f"[tts_run] DONE {len(manifest)} segments, {total/60:.1f} min narration at 1.10", flush=True)
