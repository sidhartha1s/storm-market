"""The narration alone, placed as it sits on the timeline: the sound one presenter-circle face pass is made from.

Reads the `nx-*` narration elements of `episodes/<slug>/index.html` that start between two timeline seconds and writes
one 16 kHz mono wav that begins at the first of them, runs to <to_s> and is silent where Paul does not speak, so the
face video lines up with the episode second for second. Insert audio (`nx-ins*`) is another voice and is left out.
<to_s> is where the pass's last circle window ends: a wav that stopped with the last word would leave that window
without a face (El Reno: two windows ran 0.3 s past their pass). Prints the timeline second the wav starts at:
`circle_cut.py` takes it after the `@`. Split passes at the book ad, where the circle is hidden anyway.

Usage: python3 scripts/circle_audio.py episodes/<slug> <from_s> <to_s> <out.wav>
"""
import re
import subprocess
import sys
from pathlib import Path


def narration(html, lo, hi):
    """(start_s, duration_s, src) of every narration element starting in [lo, hi), in timeline order."""
    segs = []
    for tag in re.findall(r"<audio\b[^>]*>", html):
        a = dict(re.findall(r'([\w-]+)="([^"]*)"', tag))
        if re.match(r"nx-(?!ins)", a.get("id", "")) and lo <= float(a["data-start"]) < hi:
            segs.append((float(a["data-start"]), float(a["data-duration"]), a["src"]))
    return sorted(segs)


def mix_graph(segs):
    """ffmpeg filter graph that delays each segment to its place after the first one, sums them and pads with silence."""
    t0 = segs[0][0]
    parts = [f"[{i}:a]aresample=16000,adelay={round((s - t0) * 1000)}:all=1[a{i}]" for i, (s, _, _) in enumerate(segs)]
    return ";".join(parts) + ";" + "".join(f"[a{i}]" for i in range(len(segs))) + f"amix=inputs={len(segs)}:normalize=0:duration=longest,apad[m]"


def ffmpeg_args(ep, segs, hi, out):
    """The whole ffmpeg call: every segment in, one wav out that runs from the first segment's start to hi."""
    cmd = ["ffmpeg", "-v", "error", "-y"]
    for _, _, src in segs:
        cmd += ["-i", str(Path(ep) / src)]
    return cmd + ["-filter_complex", mix_graph(segs), "-map", "[m]", "-ac", "1", "-ar", "16000", "-t", f"{hi - segs[0][0]:.3f}", out]


def main():
    ep, lo, hi, out = Path(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), sys.argv[4]
    segs = narration((ep / "index.html").read_text(encoding="utf8"), lo, hi)
    if not segs:
        sys.exit(f"FAIL: no nx-* narration starts between {lo} and {hi} s in {ep / 'index.html'}")
    subprocess.run(ffmpeg_args(ep, segs, hi, out), check=True)
    t0 = segs[0][0]
    print(f"{out}: {len(segs)} segments, starts at timeline {t0:.3f} s, {hi - t0:.3f} s long, speech {sum(d for _, d, _ in segs):.1f} s")


if __name__ == "__main__":
    main()
