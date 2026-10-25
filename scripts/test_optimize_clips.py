"""Self-check for optimize_clips.py's md5-pinned skip list: python3 scripts/test_optimize_clips.py

Camille and Mayfield (25 Oct 26, learnings/render.md on claude/ep-mayfield-2021-a6d084): `optimize_clips.py --apply`
re-encoded the staged end-ask clips, so sweep_episode.py failed their md5 against assets/end-ask/. The episode here
mounts the two end-ask clips exactly as Mayfield's index.html does, staged from the real assets, plus one stock clip.
The plan (the list --apply re-encodes) must hold the stock clip and neither end-ask file. Dry run only: nothing is
re-encoded.
"""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

S = Path(__file__).resolve().parent
ASK = S.parent / "assets" / "end-ask"
FAILS = []


def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


with tempfile.TemporaryDirectory() as tmp:
    ep = Path(tmp) / "ep-mayfield-2021"
    (ep / "media" / "end-ask").mkdir(parents=True)
    (ep / "media" / "stock").mkdir(parents=True)
    for n in ("a", "b"):
        shutil.copy(ASK / f"paul-end-ask-v1-oct19-{n}.mp4", ep / "media" / "end-ask")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "lavfi", "-i", "testsrc2=size=320x180:rate=15", "-t", "4",
                    "-pix_fmt", "yuv420p", str(ep / "media" / "stock" / "stock-a.mp4")], check=True)
    (ep / "index.html").write_text(
        '<div id="root" data-width="1920" data-height="1080" data-duration="1150">\n'
        '<video id="st-a" src="media/stock/stock-a.mp4" data-start="10" data-duration="3" data-track-index="1" muted></video>\n'
        '<video id="ins-endask-a" src="media/end-ask/paul-end-ask-v1-oct19-a.mp4" data-start="1125.697" '
        'data-duration="9.083" data-track-index="1" data-volume="1" data-has-audio="true"></video>\n'
        '<video id="ins-endask-b" src="media/end-ask/paul-end-ask-v1-oct19-b.mp4" data-start="1134.780" '
        'data-duration="6.417" data-track-index="1" data-volume="1" data-has-audio="true"></video>\n</div>\n',
        encoding="utf-8")
    r = subprocess.run([sys.executable, str(S / "optimize_clips.py"), str(ep)], capture_output=True, text=True)
    plan = [l for l in r.stdout.splitlines() if l.endswith("s") and ".mp4" in l and not l.startswith("skip")]

check("dry run exits 0", r.returncode == 0)
check("the stock clip is in the plan", any(l.startswith("stock-a.mp4") for l in plan))
check("neither end-ask clip is in the plan (Camille/Mayfield md5 break)", not any("end-ask" in l for l in plan))
check("both end-ask clips are named as skipped", r.stdout.count("skip media/end-ask/") == 2)

if FAILS:
    print(r.stdout, r.stderr)
    sys.exit(f"{len(FAILS)} check(s) failed")
print("all optimize-clips checks passed")
