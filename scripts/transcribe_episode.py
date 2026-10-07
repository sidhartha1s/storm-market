#!/usr/bin/env python3
"""Per-segment word timestamps via faster-whisper (offline, small.en cached).
Usage: python3 scripts/transcribe_episode.py episodes/<slug>
Outputs audio/<id>.words.json: [{"text","start","end"}, ...] per segment.

tts_episode.py now does this transcription step itself as part of its TTS -> atempo ->
transcribe pipeline, so a fresh run never needs this script. It stays for existing callers
that invoke it standalone (e.g. after a hand-replaced wav). A words.json is regenerated
whenever it looks stale for that wav: missing, older by mtime, OR — the case mtime alone
misses, measured on ep3-tristate where words.json was NEWER than the wav it no longer
matched — its last word ends past the wav's actual duration.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from tts_episode import ffprobe_duration, load_whisper_model, transcribe_wav  # noqa: E402


def words_are_stale(wav: Path, words_json: Path) -> bool:
    if not words_json.exists():
        return True
    if words_json.stat().st_mtime < wav.stat().st_mtime:
        return True
    try:
        words = json.loads(words_json.read_text(encoding="utf-8"))
        if isinstance(words, dict):
            words = words.get("words", [])
        last_end = words[-1]["end"] if words else 0.0
    except (json.JSONDecodeError, KeyError, IndexError):
        return True
    dur = ffprobe_duration(wav)
    if dur is not None and last_end > dur + 0.5:
        return True
    return False


def main():
    ep = Path(sys.argv[1])
    model = None
    for wav in sorted((ep / "audio").glob("*.wav")):
        out = wav.with_suffix(".words.json")
        if not words_are_stale(wav, out):
            continue
        if model is None:
            model = load_whisper_model()
        words = transcribe_wav(model, wav)
        out.write_text(json.dumps(words), encoding="utf-8")
        print(f"{wav.stem}: {len(words)} words, last end {words[-1]['end'] if words else 0}s",
              flush=True)
    print("DONE")


if __name__ == "__main__":
    main()
