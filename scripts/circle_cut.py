"""Cut the presenter-circle clips an episode mounts out of the long face passes.

The windows are the hand-written `<video class="pip" src="media/pip/..." data-start data-duration>` elements of
`episodes/<slug>/index.html`: this script reads them and never writes HTML. Each window is cut from the face pass that
covers it, cropped so Paul's face fills about 70 % of the circle, scaled to the circle's 240 px and given a silent
sound track (every mounted video needs an audio stream, learnings/render.md). A window no pass covers is a FAIL.

Usage: python3 scripts/circle_cut.py episodes/<slug> <face.mp4>@<timeline_start_s> [<face.mp4>@<timeline_start_s> ...]
       (the timeline start of a pass is the second circle_audio.py printed for its wav)
Exit 0 = every pip window cut. Exit 1 = a window is not covered, or no pip window is mounted.
"""
import re
import subprocess
import sys
from pathlib import Path

SIZE = 240  # the circle, references/mg-quickref.md "Presenter circle"
CROP = (0.868, 0.066, 0.0125)  # square side, left, top as fractions of the face clip's width (assets/paul/circle-portrait-560.jpg framing)
PAD = 0.04  # one 25 fps frame, so a clip never ends before its window does


def windows(html):
    """(src, start_s, duration_s) of every mounted circle clip."""
    out = []
    for tag in re.findall(r"<video\b[^>]*>", html):
        a = dict(re.findall(r'([\w-]+)="([^"]*)"', tag))
        if "pip" in a.get("class", "").split():
            out.append((a["src"], float(a["data-start"]), float(a["data-duration"])))
    return out


def plan(wins, passes):
    """Match each window to a pass. passes: (face_path, timeline_start_s, length_s).
    Returns (cuts, uncovered): cuts are (src, face_path, seek_s, duration_s)."""
    cuts, uncovered = [], []
    for src, start, dur in wins:
        hit = next((p for p in passes if p[1] <= start and start + dur <= p[1] + p[2]), None)
        if hit:
            cuts.append((src, hit[0], round(start - hit[1], 3), dur))
        else:
            uncovered.append(src)
    return cuts, uncovered


def probe(path):
    """(width_px, length_s) of the picture stream: the picture's length, not the file's (the sound can run longer)."""
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,duration", "-of", "default=nw=1", path],
                         capture_output=True, text=True, check=True).stdout
    v = dict(line.split("=", 1) for line in out.split())
    return int(v["width"]), float(v["duration"])


def main():
    ep = Path(sys.argv[1])
    passes, widths = [], {}
    for arg in sys.argv[2:]:
        face, start = arg.rsplit("@", 1)
        widths[face], length = probe(face)
        passes.append((face, float(start), length))
    cuts, uncovered = plan(windows((ep / "index.html").read_text(encoding="utf8")), passes)
    if uncovered or not cuts:
        sys.exit(f"FAIL: no face pass covers {uncovered}" if uncovered else "FAIL: index.html mounts no <video class=\"pip\">")
    for src, face, seek, dur in cuts:
        c, x, y = (round(f * widths[face]) for f in CROP)
        (ep / src).parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{seek:.3f}", "-i", face, "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
                        "-t", f"{dur + PAD:.3f}", "-map", "0:v", "-map", "1:a", "-vf", f"crop={c}:{c}:{x}:{y},scale={SIZE}:{SIZE}:flags=lanczos",
                        "-c:v", "libx264", "-crf", "23", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "32k", "-movflags", "+faststart", str(ep / src)], check=True)
        print(f"{src}: {dur:.2f} s from {Path(face).name} at {seek:.2f} s")
    print(f"cut {len(cuts)} circle clips, {sum(c[3] for c in cuts):.1f} s of face")


if __name__ == "__main__":
    main()
