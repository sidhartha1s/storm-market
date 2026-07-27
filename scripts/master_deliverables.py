#!/usr/bin/env python3
"""Post-render deliverables: -14 LUFS master + SRT, per repo CLAUDE.md step 7.

Usage: python3 scripts/master_deliverables.py episodes/<slug> <render-basename>
e.g.:  python3 scripts/master_deliverables.py episodes/ep2-2011-super-outbreak ep2-final

Reads  episodes/<slug>/renders/<basename>.mp4 and writes:
  renders/<basename>-master.mp4  (video stream copied, single measured gain,
                                  aac 256k; verified -14 LUFS +/-0.5, TP <= -0.9)
  renders/<basename>.srt         (via scripts/build_srt.py)

Plain gain (not dynamic loudnorm) is deliberate: episode mixes land with tight
LRA (~3.4 measured on ep2), where one measured gain preserves the mix exactly.
Fails loud (exit 1) if the verify pass misses tolerance.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

TARGET_I = -14.0
TARGET_TP = -1.0
TOL_I = 0.5

def measure(path: Path) -> dict:
    r = subprocess.run(
        ["ffmpeg", "-hide_banner", "-i", str(path),
         "-af", f"loudnorm=I={TARGET_I}:TP={TARGET_TP}:print_format=json",
         "-f", "null", "-"],
        capture_output=True, text=True)
    m = re.search(r"\{[^{}]+\}", r.stderr[-2000:], re.S)
    if not m:
        sys.exit(f"loudnorm measure failed on {path}:\n{r.stderr[-800:]}")
    return json.loads(m.group(0))

def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    ep = Path(sys.argv[1])
    base = sys.argv[2]
    src = ep / "renders" / f"{base}.mp4"
    if not src.exists():
        sys.exit(f"no such render: {src}")
    master = ep / "renders" / f"{base}-master.mp4"

    print(f"[1/4] measuring {src.name} ...")
    m = measure(src)
    in_i, in_tp = float(m["input_i"]), float(m["input_tp"])
    # one gain satisfying both the loudness target and the true-peak ceiling
    gain = round(min(TARGET_I - in_i, TARGET_TP - in_tp), 2)
    print(f"      input {in_i} LUFS / TP {in_tp} dBTP -> gain {gain:+.2f} dB")

    print(f"[2/4] writing {master.name} (video copy, aac 256k) ...")
    r = subprocess.run(
        ["ffmpeg", "-hide_banner", "-y", "-i", str(src), "-c:v", "copy",
         "-af", f"volume={gain}dB", "-c:a", "aac", "-b:a", "256k", str(master)],
        capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"master encode failed:\n{r.stderr[-800:]}")

    print("[3/4] verifying master loudness ...")
    v = measure(master)
    out_i, out_tp = float(v["input_i"]), float(v["input_tp"])
    expected_i = in_i + gain
    print(f"      master {out_i} LUFS / TP {out_tp} dBTP (expected ~{expected_i:.2f})")
    if abs(out_i - expected_i) > TOL_I or out_tp > -0.9:
        sys.exit(f"FAIL: master out of tolerance (I {out_i} vs {expected_i:.2f} "
                 f"+/-{TOL_I}, TP {out_tp} must be <= -0.9)")
    if abs(out_i - TARGET_I) > 1.0:
        sys.exit(f"FAIL: master landed {out_i} LUFS, > 1.0 LU from the {TARGET_I} target — "
                 "mix is peak-limited (TP ceiling capped the gain). Fix the mix or add a "
                 "limiter pass upstream; do not ship this master.")

    print("[4/4] building SRT ...")
    r = subprocess.run([sys.executable, str(Path(__file__).parent / "build_srt.py"),
                        str(ep), base], capture_output=True, text=True)
    print("      " + (r.stdout.strip() or r.stderr.strip()))
    if r.returncode != 0:
        sys.exit("build_srt.py failed")

    print(f"OK: {master} + {ep/'renders'/(base + '.srt')}")

if __name__ == "__main__":
    main()
