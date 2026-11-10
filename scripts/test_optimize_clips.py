"""Self-check for optimize_clips.py: python3 scripts/test_optimize_clips.py

1. The md5-pinned skip list. Camille and Mayfield (25 Oct 26, learnings/render.md on claude/ep-mayfield-2021-a6d084):
   `optimize_clips.py --apply` re-encoded the staged end-ask clips, so sweep_episode.py failed their md5 against
   assets/end-ask/. The episode here mounts the two end-ask clips exactly as Mayfield's index.html does, staged from
   the real assets, plus one stock clip. The plan must hold the stock clip and neither end-ask file (dry run).
2. `--apply` on tiny generated clips (audit R1, 11 Nov 26): the `media/_orig/` backup was keyed by file name only, so
   two clips named alike in two folders shared one original, and a re-downloaded clip was put back to its old
   original. Each check reads the first pixel's colour of the real output.
3. `--apply` with nothing to optimize exits 0 (audit R14: it divided by a zero total).
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

S = Path(__file__).resolve().parent
ASK = S.parent / "assets" / "end-ask"
FAILS = []
ENV = {**os.environ, "RENDER_BUSY_OK": "1"}  # tiny test clips: no live render or heavy-lock holder may block --apply


def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


def clip(path, colour, seconds=3):
    path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", f"color=c={colour}:s=64x36:r=15", "-t", str(seconds),
                    "-pix_fmt", "yuv420p", str(path)], check=True)


def pixel(path):
    """(r, g, b) of the first frame's top-left pixel."""
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-frames:v", "1", "-f", "rawvideo", "-pix_fmt", "rgb24",
                          "-"], capture_output=True, check=True).stdout
    return tuple(raw[:3])


def is_colour(path, want):
    r, g, b = pixel(path)
    return {"red": r > 180 and g < 80 and b < 80, "blue": b > 180 and r < 80 and g < 80,
            "lime": g > 180 and r < 80 and b < 80, "yellow": r > 180 and g > 180 and b < 80}[want]


def episode(root, videos):
    ep = Path(root) / "ep-x"
    ep.mkdir(parents=True, exist_ok=True)
    (ep / "index.html").write_text('<div id="root" data-width="1920" data-height="1080" data-duration="60">\n' + "".join(
        f'<video id="v{i}" src="{src}" data-start="{i * 5}" data-duration="1" data-track-index="1" muted></video>\n'
        for i, src in enumerate(videos)) + "</div>\n", encoding="utf-8")
    return ep


def apply(ep):
    return subprocess.run([sys.executable, str(S / "optimize_clips.py"), str(ep), "--apply"], capture_output=True,
                          text=True, env=ENV)


with tempfile.TemporaryDirectory() as tmp:
    ep = Path(tmp) / "ep-mayfield-2021"
    (ep / "media" / "end-ask").mkdir(parents=True)
    for n in ("a", "b"):
        shutil.copy(ASK / f"paul-end-ask-v1-oct19-{n}.mp4", ep / "media" / "end-ask")
    clip(ep / "media" / "stock" / "stock-a.mp4", "red", 4)
    (ep / "index.html").write_text(
        '<div id="root" data-width="1920" data-height="1080" data-duration="1150">\n'
        '<video id="st-a" src="media/stock/stock-a.mp4" data-start="10" data-duration="3" data-track-index="1" muted></video>\n'
        '<video id="ins-endask-a" src="media/end-ask/paul-end-ask-v1-oct19-a.mp4" data-start="1125.697" '
        'data-duration="9.083" data-track-index="1" data-volume="1" data-has-audio="true"></video>\n'
        '<video id="ins-endask-b" src="media/end-ask/paul-end-ask-v1-oct19-b.mp4" data-start="1134.780" '
        'data-duration="6.417" data-track-index="1" data-volume="1" data-has-audio="true"></video>\n</div>\n',
        encoding="utf-8")
    r = subprocess.run([sys.executable, str(S / "optimize_clips.py"), str(ep)], capture_output=True, text=True)
    plan = [l for l in r.stdout.splitlines() if l.split() and l.split()[0].endswith(".mp4")]  # rows over comp end in "<- over comp"

check("dry run exits 0", r.returncode == 0)
check("the stock clip is in the plan", any(l.startswith("stock-a.mp4") for l in plan))
check("neither end-ask clip is in the plan (Camille/Mayfield md5 break)", not any("end-ask" in l for l in plan))
check("both end-ask clips are named as skipped", r.stdout.count("skip media/end-ask/") == 2)
out = [r]

with tempfile.TemporaryDirectory() as tmp:
    # R1 (a): two clips named alike in two folders each keep their own picture and their own original
    ep = episode(tmp, ["media/news/clip.mp4", "media/stock/clip.mp4"])
    clip(ep / "media" / "news" / "clip.mp4", "red")
    clip(ep / "media" / "stock" / "clip.mp4", "blue")
    r = apply(ep)
    out.append(r)
    check("apply on two same-named clips exits 0", r.returncode == 0)
    check("news/clip.mp4 is still red after --apply", is_colour(ep / "media" / "news" / "clip.mp4", "red"))
    check("stock/clip.mp4 is still blue after --apply (was re-encoded from news's original)",
          is_colour(ep / "media" / "stock" / "clip.mp4", "blue"))
    orig = ep / "media" / "_orig"
    check("each original is kept under its own path in _orig/",
          is_colour(orig / "news" / "clip.mp4", "red") and is_colour(orig / "stock" / "clip.mp4", "blue"))

    # R1 (b): a clip re-downloaded under the same name after a pass is optimized from the NEW file, not put back
    clip(ep / "media" / "news" / "clip.mp4", "lime")
    r = apply(ep)
    out.append(r)
    check("a re-downloaded clip keeps its new picture after a second --apply",
          r.returncode == 0 and is_colour(ep / "media" / "news" / "clip.mp4", "lime"))
    check("its backup is the new download", is_colour(orig / "news" / "clip.mp4", "lime"))
    check("an untouched clip is re-encoded from its backup, not from its own re-encode",
          is_colour(ep / "media" / "stock" / "clip.mp4", "blue"))

with tempfile.TemporaryDirectory() as tmp:
    # a flat backup from before the fix (media/_orig/<name>) is still this clip's original: it moves under its path
    ep = episode(tmp, ["media/stock/solo.mp4"])
    clip(ep / "media" / "_orig" / "solo.mp4", "yellow")
    clip(ep / "media" / "stock" / "solo.mp4", "blue")  # stands in for an earlier pass's output
    r = apply(ep)
    out.append(r)
    check("a flat pre-fix backup is used as the original",
          r.returncode == 0 and is_colour(ep / "media" / "stock" / "solo.mp4", "yellow"))
    check("the flat backup moved to its path under _orig/",
          (ep / "media" / "_orig" / "stock" / "solo.mp4").exists() and not (ep / "media" / "_orig" / "solo.mp4").exists())

with tempfile.TemporaryDirectory() as tmp:
    # a flat pre-fix backup whose name two mounted clips share cannot be assigned: refuse, touch nothing
    ep = episode(tmp, ["media/a/dup.mp4", "media/b/dup.mp4"])
    clip(ep / "media" / "_orig" / "dup.mp4", "yellow")
    clip(ep / "media" / "a" / "dup.mp4", "red")
    clip(ep / "media" / "b" / "dup.mp4", "blue")
    r = apply(ep)
    out.append(r)
    check("an ambiguous flat backup refuses (exit 1) and leaves both clips as they were",
          r.returncode == 1 and is_colour(ep / "media" / "a" / "dup.mp4", "red")
          and is_colour(ep / "media" / "b" / "dup.mp4", "blue") and (ep / "media" / "_orig" / "dup.mp4").exists())

with tempfile.TemporaryDirectory() as tmp:
    # R14: nothing to optimize
    r = apply(episode(tmp, []))
    out.append(r)
    check("--apply with no clips exits 0 (was ZeroDivisionError)", r.returncode == 0)

if FAILS:
    for r in out:
        print(r.stdout, r.stderr)
    sys.exit(f"{len(FAILS)} check(s) failed")
print("all optimize-clips checks passed")
