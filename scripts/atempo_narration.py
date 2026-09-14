"""Speed every narration wav in <episode>/audio by a pitch-preserving atempo, keeping the natives in audio/_native/.

Usage: python3 scripts/atempo_narration.py episodes/<slug> [1.10]
News lane (Format C) runs atempo 1.10: TTS -> THIS -> transcribe_episode.py on the sped wavs -> time graphics from
that words.json (references/script-os.md "tempo before timing"). Idempotent: a wav already in _native/ is not re-sped.
Deletes nothing.
"""
import pathlib, subprocess, sys

ep = pathlib.Path(sys.argv[1])
factor = sys.argv[2] if len(sys.argv) > 2 else "1.10"
audio = ep / "audio"
native = audio / "_native"
native.mkdir(exist_ok=True)
done = 0
for wav in sorted(audio.glob("*.wav")):
    keep = native / wav.name
    if keep.exists():
        continue
    wav.rename(keep)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(keep), "-filter:a", f"atempo={factor}", str(wav)], check=True)
    for stale in (audio / f"{wav.stem}.words.json", audio / "manifest.json"):
        if stale.exists():
            stale.rename(stale.with_suffix(stale.suffix + ".native"))
    done += 1
print(f"[atempo_narration] {done} wav(s) sped x{factor}; natives in {native}; re-run transcribe_episode.py now")
