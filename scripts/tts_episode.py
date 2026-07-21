#!/usr/bin/env python3
"""TTS driver: extract narration segments from an episode's edit_script.md and synthesize
each as its own wav via pocket-TTS (external tool, paths in config.yaml), then transcribe
each for word timestamps (faster-whisper, offline).

Segment = a '### <ID> — narration' heading followed by one blockquote. ID like 'A3-S5'.
Outputs per segment: audio/<id>.txt, audio/<id>.wav, audio/<id>.words.json + audio/manifest.json.

Usage: python3 scripts/tts_episode.py episodes/<slug> [--only A3-S5,...]
"""
import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def load_cfg():
    import yaml  # storm venv-less: pyyaml via python312 site or fallback parse
    return yaml.safe_load(open(REPO / "config.yaml", encoding="utf-8"))


def parse_segments(md: str):
    segs = []
    blocks = re.split(r"\n### ", md)
    for b in blocks[1:]:
        header = b.split("\n", 1)[0]
        m = re.match(r"([A-Z]\d+-S\d+)\s+—\s+narration", header)
        if not m:
            continue
        sid = m.group(1).lower()
        quote = "\n".join(l[2:] for l in b.splitlines() if l.startswith("> "))
        text = re.sub(r"\s+", " ", quote).strip()
        if text:
            segs.append((sid, text))
    return segs


def main():
    ep = Path(sys.argv[1])
    only = None
    if "--only" in sys.argv:
        only = set(s.strip().lower() for s in sys.argv[sys.argv.index("--only") + 1].split(","))
    cfg = load_cfg()
    ext = cfg["external"]
    (ep / "audio").mkdir(exist_ok=True)
    segs = parse_segments((ep / "edit_script.md").read_text(encoding="utf-8"))
    print(f"[tts_episode] {len(segs)} narration segments found")
    manifest = {}
    for sid, text in segs:
        if only and sid not in only:
            continue
        txt, wav = ep / "audio" / f"{sid}.txt", ep / "audio" / f"{sid}.wav"
        txt.write_text(text, encoding="utf-8")
        if not wav.exists():
            r = subprocess.run([ext["pocket_venv_python"], ext["tts_clone_py"],
                                "--text-file", str(txt), "--out", str(wav),
                                "--voice", ext["voice_ref"]],
                               env={**__import__("os").environ, "PYTHONUTF8": "1", "PYTHONUNBUFFERED": "1"})
            if r.returncode != 0:
                sys.exit(f"[tts_episode] FAIL on {sid}")
        d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                  "-of", "default=nw=1:nk=1", str(wav)],
                                 capture_output=True, text=True).stdout.strip())
        manifest[sid] = {"wav": f"audio/{sid}.wav", "duration": round(d, 3),
                         "words": len(text.split())}
        print(f"[tts_episode] {sid}: {d:.1f}s ({len(text.split())} words)", flush=True)
    (ep / "audio" / "manifest.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    total = sum(v["duration"] for v in manifest.values())
    print(f"[tts_episode] DONE — {len(manifest)} segments, {total/60:.1f} min narration")


if __name__ == "__main__":
    main()
