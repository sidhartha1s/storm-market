"""Self-check for scripts/master_deliverables.py's BT.709 tv-range tagging:
python3 scripts/test_master_deliverables.py
Builds a 3s synthetic source render (ffmpeg lavfi, no color tags — matches a real capture, which
carries no color metadata) in a temp episode dir, runs the real master step end to end, and reads
the master back with ffprobe. Loudness/SRT logic is untouched by this PR and already exercised by
the real pipeline; this test is scoped to the one thing that changed.
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

S = Path(__file__).resolve().parent

FAILS = []


def check(name, cond, detail=""):
    if cond:
        print(f"PASS {name}")
    else:
        FAILS.append(name)
        print(f"FAIL {name} {detail}")


HAVE_FFMPEG = subprocess.run(["ffmpeg", "-version"], capture_output=True).returncode == 0
if not HAVE_FFMPEG:
    print("SKIP master-01/02: ffmpeg not on PATH")
else:
    with tempfile.TemporaryDirectory() as d:
        ep = Path(d)
        (ep / "renders").mkdir()
        (ep / "audio").mkdir()
        # build_srt.py (step [4/4], untouched by this PR) needs one real nx-* narration cue to
        # not hard-exit; minimal fixture, not exercising build_srt's own logic.
        (ep / "index.html").write_text(
            '<audio id="nx-001" src="audio/001.wav" data-start="0"></audio>', encoding="utf-8")
        (ep / "audio" / "001.words.json").write_text(
            json.dumps([{"word": "test", "start": 0.0, "end": 0.5}]), encoding="utf-8")
        (ep / "audio" / "001.txt").write_text("test", encoding="utf-8")
        src = ep / "renders" / "test-final.mp4"
        r = subprocess.run(
            ["ffmpeg", "-y", "-v", "error",
             "-f", "lavfi", "-i", "testsrc=size=320x240:rate=25:duration=3",
             "-f", "lavfi", "-i", "sine=frequency=440:duration=3",
             "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", str(src)],
            capture_output=True, text=True)
        check("master-01 fixture: synthetic 3s source render built", r.returncode == 0 and src.exists(), r.stderr[-400:])

        r = subprocess.run(
            [sys.executable, str(S / "master_deliverables.py"), str(ep), "test-final"],
            capture_output=True, text=True)
        master = ep / "renders" / "test-final-master.mp4"
        check("master-02 master_deliverables.py runs clean on the synthetic source",
              r.returncode == 0 and master.exists(), f"rc={r.returncode}\n{r.stdout}\n{r.stderr}")

        if master.exists():
            probe = subprocess.run(
                ["ffprobe", "-v", "error", "-select_streams", "v:0",
                 "-show_entries", "stream=color_space,color_range",
                 "-of", "json", str(master)],
                capture_output=True, text=True)
            tags = json.loads(probe.stdout)["streams"][0]
            check("master-03 master carries color_space=bt709", tags.get("color_space") == "bt709", tags)
            check("master-04 master carries color_range=tv", tags.get("color_range") == "tv", tags)

print()
if FAILS:
    print(f"{len(FAILS)} FAILED: {FAILS}")
    sys.exit(1)
print("master_deliverables BT.709 self-check: ALL PASS")
