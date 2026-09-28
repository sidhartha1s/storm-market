"""Self-check for scripts/pop_scan.py: python3 scripts/test_pop_scan.py
find_pops() is unit-tested against tiny synthetic in-memory frames (no ffmpeg needed) for the
three cases that matter: an isolated spike, smooth motion, and a sustained hard cut. An ffmpeg
integration test then proves the real pipe (fps/scale/format -> rawvideo -> stdin) finds an
injected single-frame flash at its known timestamp, and that verify_render.sh's new pop-scan
section never fails the render (report-only, unlike every other check in that script).
"""
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
from pop_scan import find_pops  # noqa: E402

FAILS = []


def check(name, cond, detail=""):
    if cond:
        print(f"PASS {name}")
    else:
        FAILS.append(name)
        print(f"FAIL {name} {detail}")


def flat(v, n=16):
    return np.full(n, v, dtype=np.int16)


# --- unit: isolated single-frame spike between two identical frames is flagged ---
frames = [flat(20), flat(20), flat(220), flat(20), flat(20)]
pops = find_pops(iter(frames))
check("pop_scan-01 isolated single-frame spike is flagged", [p[0] for p in pops] == [2], pops)

# --- unit: smooth gradual motion (each frame a small, similar step) is not flagged ---
frames = [flat(v) for v in (20, 30, 40, 50, 60, 70)]
pops = find_pops(iter(frames))
check("pop_scan-02 smooth gradual motion is not flagged", pops == [], pops)

# --- unit: a sustained hard cut (level changes and STAYS) is not flagged — only a frame that ---
# --- differs from both neighbours while THEY resemble each other counts as a pop ---
frames = [flat(20), flat(20), flat(200), flat(200), flat(200), flat(200)]
pops = find_pops(iter(frames))
check("pop_scan-03 a sustained hard cut is not flagged (only isolated frames are)", pops == [], pops)

# --- unit: floor rejects a tiny difference even if the ratio would pass ---
frames = [flat(20), flat(20), flat(23), flat(20), flat(20)]
pops = find_pops(iter(frames), floor=8.0)
check("pop_scan-04 absolute floor rejects a sub-threshold wobble", pops == [], pops)


HAVE_FFMPEG = subprocess.run(["ffmpeg", "-version"], capture_output=True).returncode == 0
if HAVE_FFMPEG:
    with tempfile.TemporaryDirectory() as d:
        clip = Path(d) / "flash.mp4"
        fps = 10
        # 2s gray clip at fps=10 (20 frames) with a single white flash frame at frame 10 (t=1.0s),
        # built via a per-frame luma expr (geq) keyed on the frame index N, so the injected
        # frame is exactly one frame wide.
        r = subprocess.run(
            ["ffmpeg", "-y", "-v", "error",
             "-f", "lavfi", "-i", f"color=c=gray:s=64x64:r={fps}:d=2",
             "-vf", "geq=lum='if(eq(N\\,10)\\,255\\,80)'",
             "-c:v", "libx264", "-pix_fmt", "yuv420p", str(clip)],
            capture_output=True, text=True)
        check("pop_scan-05 fixture: synthetic flash clip built", r.returncode == 0 and clip.exists(), r.stderr[-400:])

        pipe = subprocess.run(
            ["ffmpeg", "-hide_banner", "-v", "error", "-i", str(clip),
             "-vf", f"fps={fps},scale=180:180,format=gray", "-f", "rawvideo", "-"],
            capture_output=True)
        scan = subprocess.run([sys.executable, str(S / "pop_scan.py"), "--fps", str(fps)],
                               input=pipe.stdout, capture_output=True)
        scan_out = scan.stdout.decode()
        check("pop_scan-06 the real ffmpeg pipe finds the injected flash near frame 10 (t=1.0s)",
              "frame 10" in scan_out or "frame 9" in scan_out or "frame 11" in scan_out,
              scan_out)

    # --- verify_render.sh integration: pop scan runs and never turns a clean render into a FAIL ---
    with tempfile.TemporaryDirectory() as d2:
        ep = Path(d2)
        (ep / "renders").mkdir()
        (ep / "index.html").write_text(
            '<div id="root" data-composition-id="x" data-start="0" data-width="320" '
            'data-height="240" data-duration="2.00" data-fps="25"></div>', encoding="utf-8")
        (ep / "render_full.log").write_text(
            "browserGpuMode probe worker0 NVIDIA GeForce GTX 1650\n", encoding="utf-8")
        mp4 = ep / "renders" / "clean-final.mp4"
        subprocess.run(["ffmpeg", "-y", "-v", "error",
                        "-f", "lavfi", "-i", "testsrc=size=320x240:rate=25:duration=2",
                        "-f", "lavfi", "-i", "sine=frequency=440:duration=2",
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", str(mp4)],
                       capture_output=True)
        r = subprocess.run(["bash", str(S / "verify_render.sh"), str(ep), "clean-final"],
                            capture_output=True, text=True)
        check("pop_scan-07 verify_render.sh runs the pop-scan section", "pop scan" in r.stdout, r.stdout[-1500:])
        check("pop_scan-08 verify_render.sh still exits 0 on a clean render (pop-scan never FAILs)",
              r.returncode == 0, f"rc={r.returncode}\n{r.stdout[-1500:]}")
else:
    print("SKIP pop_scan-05..08: ffmpeg not on PATH")

print()
if FAILS:
    print(f"{len(FAILS)} FAILED: {FAILS}")
    sys.exit(1)
print("pop_scan self-check: ALL PASS")
