"""Self-check for paul_start_frame.py: python3 scripts/test_paul_start_frame.py

Fixtures are the real Mayfield jobs.json files (episodes/ep-mayfield-2021/media/paul/): ins-paul-1 was made from
paul-sheet-c.png (the wrong face, owner 25 Oct 26), ins-paul-1-retake and ins-paul-2 from paul-start-frame-omni-v2.png.
- Mayfield before 4e606b56 (clip 1 mounted from ins-paul-1/) must fail on differing frames.
- Mayfield after 4e606b56 (clip 1 from ins-paul-1-retake/) must pass.
- A clip with no jobs.json beside it must fail.
- Palm Sunday's layout: clips 2 to 6 batched in one media/paul/acts-2-6/jobs.json (jobs named ins-paul-2..6, the real
  names) with clip 1's own beside it, all from one frame, must pass.
"""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

S = Path(__file__).resolve().parent
FIX = S / "fixtures" / "paul_start_frame"
FAILS = []


def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


def run(clip1_dir, with_jobs=True):
    with tempfile.TemporaryDirectory() as tmp:
        ep = Path(tmp) / "ep-mayfield-2021"
        mounts = []
        for n, d in [(1, clip1_dir)] + [(n, "ins-paul-2") for n in range(2, 7)]:
            # clips 2 to 6 share ins-paul-2's real jobs.json: same start frame as the real 3 to 6
            folder = ep / "media" / "paul" / (d if n == 1 else f"ins-paul-{n}")
            folder.mkdir(parents=True, exist_ok=True)
            if with_jobs or n != 1:
                shutil.copy(FIX / f"{d}.jobs.json", folder / "jobs.json")
            mounts.append(f'<video id="ins-paul-{n}" src="{folder.relative_to(ep).as_posix()}/ins-paul-{n}-vc.mp4" '
                          'data-start="0" data-duration="5" data-track-index="1" data-volume="1"></video>')
        (ep / "index.html").write_text("\n".join(mounts), encoding="utf-8")
        r = subprocess.run([sys.executable, str(S / "paul_start_frame.py"), str(ep)], capture_output=True, text=True)
        return r.returncode, r.stdout


rc, out = run("ins-paul-1")
check("Mayfield before 4e606b56 (clip 1 off the character sheet) fails", rc == 1 and "paul-sheet-c.png" in out)
rc, out = run("ins-paul-1-retake")
check("Mayfield after the retake passes", rc == 0 and "paul-start-frame-omni-v2.png" in out)
rc, out = run("ins-paul-1-retake", with_jobs=False)
check("a clip without jobs.json fails", rc == 1 and "ins-paul-1: no single start frame" in out)

with tempfile.TemporaryDirectory() as tmp:  # Palm Sunday: one batch jobs.json for clips 2 to 6
    ep = Path(tmp) / "ep-palm-sunday-1965"
    paul = ep / "media" / "paul"
    job = lambda n: {"name": f"ins-paul-{n}", "frame": "C:/x/media/paul/inputs/paul-desk-frame.jpg"}  # noqa: E731
    (paul / "acts-2-6").mkdir(parents=True)
    (paul / "acts-2-6" / "jobs.json").write_text(json.dumps({"jobs": [job(n) for n in range(2, 7)]}), encoding="utf-8")
    for n in range(1, 7):
        (paul / f"ins-paul-{n}").mkdir()
    (paul / "ins-paul-1" / "jobs.json").write_text(json.dumps({"jobs": [job(1)]}), encoding="utf-8")
    (ep / "index.html").write_text("\n".join(f'<video id="ins-paul-{n}" src="media/paul/ins-paul-{n}/ins-paul-{n}.mp4"></video>'
                                             for n in range(1, 7)), encoding="utf-8")
    r = subprocess.run([sys.executable, str(S / "paul_start_frame.py"), str(ep)], capture_output=True, text=True)
check("Palm Sunday (clips 2 to 6 in one batch jobs.json) passes", r.returncode == 0 and "6 clip(s)" in r.stdout)

if FAILS:
    sys.exit(f"{len(FAILS)} check(s) failed")
print("all paul-start-frame checks passed")
