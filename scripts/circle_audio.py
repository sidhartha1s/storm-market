"""The narration alone, placed as it sits on the timeline: the sound one presenter-circle face pass is made from.

Reads the `nx-*` narration elements of `episodes/<slug>/index.html` that start between two timeline seconds and writes
one 16 kHz mono wav that begins at the first of them and is silent where Paul does not speak, so the face video lines
up with the episode second for second. Prints the timeline second the wav starts at: `circle_cut.py` takes it after
the `@`. Split passes at the book ad and at full-frame Paul clips, where the circle is hidden anyway.

Usage: python3 scripts/circle_audio.py episodes/<slug> <from_s> <to_s> <out.wav>
"""
import re
import subprocess
import sys
from pathlib import Path


def narration(html, lo, hi):
    """(start_s, duration_s, src) of every nx-* audio element starting in [lo, hi), in timeline order."""
    segs = []
    for tag in re.findall(r"<audio\b[^>]*>", html):
        a = dict(re.findall(r'([\w-]+)="([^"]*)"', tag))
        if a.get("id", "").startswith("nx-") and lo <= float(a["data-start"]) < hi:
            segs.append((float(a["data-start"]), float(a["data-duration"]), a["src"]))
    return sorted(segs)


def mix_graph(segs):
    """ffmpeg filter graph that delays each segment to its place after the first one and sums them."""
    t0 = segs[0][0]
    parts = [f"[{i}:a]aresample=16000,adelay={round((s - t0) * 1000)}:all=1[a{i}]" for i, (s, _, _) in enumerate(segs)]
    return ";".join(parts) + ";" + "".join(f"[a{i}]" for i in range(len(segs))) + f"amix=inputs={len(segs)}:normalize=0:duration=longest,apad[m]"


def main():
    ep, lo, hi, out = Path(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
    segs = narration((ep / "index.html").read_text(encoding="utf8"), lo, hi)
    if not segs:
        sys.exit(f"FAIL: no nx-* narration starts between {lo} and {hi} s in {ep / 'index.html'}")
    t0, end = segs[0][0], max(s + d for s, d, _ in segs)
    cmd = ["ffmpeg", "-v", "error", "-y"]
    for _, _, src in segs:
        cmd += ["-i", str(ep / src)]
    subprocess.run(cmd + ["-filter_complex", mix_graph(segs), "-map", "[m]", "-ac", "1", "-ar", "16000", "-t", f"{end - t0:.3f}", out], check=True)
    print(f"{out}: {len(segs)} segments, starts at timeline {t0:.2f} s, {end - t0:.2f} s long, speech {sum(d for _, d, _ in segs):.1f} s")


if __name__ == "__main__":
    main()
