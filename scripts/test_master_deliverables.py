"""Self-check for scripts/master_deliverables.py: python3 scripts/test_master_deliverables.py
Builds a 3s synthetic source render (ffmpeg lavfi, no color tags — matches a real capture, which
carries no color metadata) in a temp episode dir, runs the real master step end to end, and reads
the master back: BT.709 tv-range tags and the -14 LUFS / TP target. Then the failure path: a master
that misses the loudness verify never lands under the shipping name (audit R9).
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
import master_deliverables as md  # noqa: E402

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
            v = md.measure(master)
            check("master-05 the master measures -14 LUFS +/-0.5 and TP <= -0.9 dBTP",
                  abs(float(v["input_i"]) - md.TARGET_I) <= md.TOL_I and float(v["input_tp"]) <= -0.9, v)
            check("master-06 no temp master is left beside it", not list((ep / "renders").glob("*.tmp.mp4")))

        # audit R9 (11 Nov 26): a master that failed the loudness verify stayed on disk under the shipping name, and a
        # re-run overwrote a good master before verifying. The verify pass is stubbed to miss tolerance (the real
        # encode runs); an earlier good master must survive and no file may be left under either name.
        master.write_bytes(b"an earlier verified master")
        real_measure, calls = md.measure, []

        def bad_verify(path):
            calls.append(path)
            m = real_measure(path)
            return m if len(calls) == 1 else {**m, "input_i": str(float(m["input_i"]) + 3)}
        md.measure, sys.argv = bad_verify, ["master_deliverables.py", str(ep), "test-final"]
        try:
            md.main()
            code = 0
        except SystemExit as e:
            code = e.code
        finally:
            md.measure = real_measure
        check("master-07 a master out of loudness tolerance fails (exit message)", isinstance(code, str) and "FAIL" in code, code)
        check("master-08 the failed master is not left under the shipping name; the earlier master is untouched",
              master.read_bytes() == b"an earlier verified master", master.stat().st_size)
        check("master-09 the failed temp master is removed", not list((ep / "renders").glob("*.tmp.mp4")),
              list((ep / "renders").iterdir()))

print()
if FAILS:
    print(f"{len(FAILS)} FAILED: {FAILS}")
    sys.exit(1)
print("master_deliverables BT.709 self-check: ALL PASS")
