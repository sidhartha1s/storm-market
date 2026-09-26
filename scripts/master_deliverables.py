#!/usr/bin/env python3
"""Post-render deliverables: -14 LUFS master + SRT, per repo CLAUDE.md step 7.

Usage: python3 scripts/master_deliverables.py episodes/<slug> <render-basename> [--hevc]

e.g.:  python3 scripts/master_deliverables.py episodes/ep2-2011-super-outbreak ep2-final
       python3 scripts/master_deliverables.py episodes/ep3-tristate ep3-final --hevc

Reads  episodes/<slug>/renders/<basename>.mp4 and writes:
  renders/<basename>-master.mp4        (video stream copied, single measured gain,
                                         aac 256k; verified -14 LUFS +/-0.5, TP <= -0.9)
  renders/<basename>.srt               (via scripts/build_srt.py)
  renders/<basename>-master-hevc.mp4   (--hevc only: GPU hevc_nvenc, audio bit-copied
                                         from the master; ~2.5x smaller, visually lossless)

Plain gain (not dynamic loudnorm) is deliberate: episode mixes land with tight
LRA (~3.4 measured on ep2), where one measured gain preserves the mix exactly.
Exception (2026-08-13): when the source's true peak would cap the gain >0.5 dB
below the loudness target, the loudness gain is applied WITH a true-peak
alimiter — renders can touch 0 dBFS and a quiet master is the worse trade.
Fails loud (exit 1) if the verify pass misses tolerance.

--hevc uses GPU NVENC (fast: ~6x realtime). It requires an ffmpeg whose hevc_nvenc
matches the box's Nvidia driver — the WinGet PATH ffmpeg (Gyan Essentials 8.1.1) works;
the 8.1.2 shared build's NVENC needs driver 610+ and fails with API-version -40. If NVENC
is unavailable this step fails loud (exit 2) rather than silently dropping to a 4-hour
software x265 encode. See learnings/render.md "Render size + HEVC compression".
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

def encode_hevc(master: Path, out: Path):
    """GPU HEVC transcode of the finished master. Video re-encoded (visually lossless
    cq22), audio bit-copied so the -14 LUFS mix is untouched. Fails loud if NVENC is
    unavailable — never falls back to a multi-hour software encode."""
    print(f"[5/5] GPU HEVC -> {out.name} (hevc_nvenc p7 cq22, audio copied) ...")
    r = subprocess.run(
        ["ffmpeg", "-hide_banner", "-y", "-i", str(master),
         "-c:v", "hevc_nvenc", "-preset", "p7", "-tune", "hq", "-rc", "vbr",
         "-cq", "22", "-pix_fmt", "yuv420p", "-tag:v", "hvc1",
         "-c:a", "copy", str(out)],
        capture_output=True, text=True)
    if r.returncode != 0 or not out.exists() or out.stat().st_size == 0:
        tail = r.stderr[-600:]
        if "nvenc" in tail.lower() or "13.1" in tail:
            sys.exit("HEVC FAILED: GPU NVENC unavailable (driver/ffmpeg mismatch). Use the "
                     "PATH ffmpeg 8.1.1 build or update the Nvidia driver to 610+. Not "
                     f"falling back to slow software x265.\n{tail}")
        sys.exit(f"HEVC encode failed:\n{tail}")
    mb = out.stat().st_size / 1e6
    print(f"      {out.name} — {mb:.0f} MB")

def main():
    argv = [a for a in sys.argv[1:] if a != "--hevc"]
    want_hevc = "--hevc" in sys.argv[1:]
    if len(argv) != 2:
        sys.exit(__doc__)
    ep = Path(argv[0])
    base = argv[1]
    src = ep / "renders" / f"{base}.mp4"
    if not src.exists():
        sys.exit(f"no such render: {src}")
    master = ep / "renders" / f"{base}-master.mp4"

    print(f"[1/4] measuring {src.name} ...")
    m = measure(src)
    in_i, in_tp = float(m["input_i"]), float(m["input_tp"])
    # one gain satisfying both the loudness target and the true-peak ceiling
    loud_gain = TARGET_I - in_i
    gain = round(min(loud_gain, TARGET_TP - in_tp), 2)
    # when hot peaks cap the gain >0.5 dB below the loudness target, take the loudness
    # gain and let a true-peak limiter catch the few hot samples instead of shipping a
    # quiet master (renders can touch 0 dBFS — measured on ep5 v4/v5, 2026-08-13)
    limited = loud_gain - gain > 0.5
    if limited:
        # limit 1 dB under the TP target: alimiter caps SAMPLE peaks, while loudnorm
        # measures inter-sample true peak, which overshoots ~0.9 dB after AAC (measured)
        af = (f"volume={round(loud_gain, 2)}dB,"
              f"alimiter=limit={10 ** ((TARGET_TP - 1.0) / 20):.4f}:attack=5:release=80:level=false")
        print(f"      input {in_i} LUFS / TP {in_tp} dBTP -> gain {loud_gain:+.2f} dB "
              f"+ limiter ceiling {TARGET_TP - 1.0} dBFS for the {TARGET_TP} dBTP target "
              f"(plain gain would land {gain:+.2f})")
    else:
        af = f"volume={gain}dB"
        print(f"      input {in_i} LUFS / TP {in_tp} dBTP -> gain {gain:+.2f} dB")

    print(f"[2/4] writing {master.name} (video copy, aac 256k) ...")
    r = subprocess.run(
        ["ffmpeg", "-hide_banner", "-y", "-i", str(src), "-c:v", "copy",
         "-af", af, "-c:a", "aac", "-b:a", "256k", str(master)],
        capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"master encode failed:\n{r.stderr[-800:]}")

    print("[3/4] verifying master loudness ...")
    v = measure(master)
    out_i, out_tp = float(v["input_i"]), float(v["input_tp"])
    expected_i = in_i + (loud_gain if limited else gain)
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

    outs = f"{master} + {ep/'renders'/(base + '.srt')}"
    if want_hevc:
        hevc = ep / "renders" / f"{base}-master-hevc.mp4"
        encode_hevc(master, hevc)
        outs += f" + {hevc}"
    print(f"OK: {outs}")

if __name__ == "__main__":
    main()
