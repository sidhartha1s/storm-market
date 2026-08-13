"""Trim and cap every mounted clip to what the timeline actually uses.

Why this exists: ep3 v3 failed eleven renders at `video_extract` with
`[FFmpeg] ffprobe deadline with code 0`. The probe itself is not slow — measured with
hyperframes' own arguments, the worst clip is 3.18s serial and 8.18s at six-way
concurrency, against a 120s deadline. What blows the deadline is the extract stage
running underneath it: 549 MB of 1080p24-30 source is decoded to frames by three
workers while a probe waits behind that I/O, and the stage had already run 204s when
it died.

The clips are far larger than the cut needs. `stock-cloudsomen-01.mp4` is 46.5s at
7.2 Mbps feeding a window under 9s; `mvtn-centerpiece-aerial-30s.mp4` is 1920x1440,
which the repo's own rule already forbids ("cap every source asset at the
composition's resolution before wiring it").

So: trim each clip to its longest window plus a safety margin, cap height at 1080,
and re-encode with a short GOP so seeking is cheap. Originals are moved to
media/_orig/ — nothing is destroyed.

Usage: python3 scripts/optimize_clips.py episodes/<slug> [--apply]
Without --apply it prints the plan and changes nothing.
"""
import re
import shutil
import subprocess
import sys
from pathlib import Path

ep = Path(sys.argv[1])
apply = "--apply" in sys.argv
MARGIN = 1.5          # headroom over the longest window, so vdur() never clips a window
GOP = 15              # draft renders at 15fps; a keyframe per second keeps seeks cheap

h = (ep / "index.html").read_text(encoding="utf-8", errors="replace")
used = {}
for m in re.finditer(r'<video\b([^>]*)>', h):
    attrs = m.group(1)
    src = re.search(r'src="([^"]+)"', attrs)
    dur = re.search(r'data-duration="([\d.]+)"', attrs)
    if not (src and dur):
        continue
    used[src.group(1)] = max(used.get(src.group(1), 0.0), float(dur.group(1)))

orig_dir = ep / "media" / "_orig"
plan, total_before = [], 0
for src, want in sorted(used.items()):
    p = ep / src
    if not p.exists():
        print(f"MISSING {src}")
        continue
    info = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                           "-show_entries", "stream=width,height:format=duration",
                           "-of", "csv=p=0", str(p)], capture_output=True, text=True).stdout
    nums = [x for x in re.split(r'[,\n]', info) if x.strip()]
    w, hgt, dur = int(nums[0]), int(nums[1]), float(nums[2])
    mb = p.stat().st_size / 1e6
    total_before += mb
    keep = min(dur, want + MARGIN)
    plan.append((src, mb, w, hgt, dur, keep))

print(f"{'clip':44} {'MB':>7} {'source':>12} {'len':>7} {'keep':>7}")
for src, mb, w, hgt, dur, keep in plan:
    flag = "  <- over 1080" if hgt > 1080 else ""
    print(f"{Path(src).name:44} {mb:7.1f} {w:5}x{hgt:<6} {dur:6.1f}s {keep:6.1f}s{flag}")
print(f"\n{len(plan)} clips, {total_before:.0f} MB before")
if not apply:
    print("dry run — pass --apply to rewrite (originals move to media/_orig/)")
    raise SystemExit(0)

orig_dir.mkdir(parents=True, exist_ok=True)
total_after = 0
for src, mb, w, hgt, dur, keep in plan:
    p = ep / src
    backup = orig_dir / Path(src).name
    if not backup.exists():
        shutil.copy2(p, backup)
    tmp = p.with_suffix(".opt.mp4")
    cmd = ["ffmpeg", "-y", "-v", "error", "-i", str(p), "-t", f"{keep:.2f}",
           "-an", "-vf", "scale=-2:'min(1080,ih)'", "-c:v", "libx264",
           "-preset", "veryfast", "-crf", "23", "-g", str(GOP), "-pix_fmt", "yuv420p",
           "-movflags", "+faststart", str(tmp)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0 or not tmp.exists():
        print(f"FAILED {Path(src).name}: {r.stderr.strip()[:120]}")
        tmp.unlink(missing_ok=True)
        continue
    tmp.replace(p)
    after = p.stat().st_size / 1e6
    total_after += after
    print(f"{Path(src).name:44} {mb:7.1f} -> {after:6.1f} MB")

print(f"\n{total_before:.0f} MB -> {total_after:.0f} MB "
      f"({100 * (1 - total_after / total_before):.0f}% less to decode)")
print("originals in media/_orig/ — rebuild index.html, the window caps come from vdur()")
