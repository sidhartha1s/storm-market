"""Time ffprobe against every video the episode mounts.

hyperframes' video_extract stage probes each clip and gives up on a deadline. Three ep3
renders died there with "ffprobe deadline with code 0", and the two theories on the table
(a 4K source asset; CPU contention from QC gates running alongside) were both guesses.
This produces the number that decides it: run it on an idle box, then again under load.

A clip that is slow on an IDLE box is a bad file — fix that file. Clips that are all fast
idle and slow under load make it contention, and the answer is to stop sharing the box
with the render.
"""
import re
import subprocess
import sys
import time
from pathlib import Path

ep = Path(sys.argv[1])
reps = int(sys.argv[2]) if len(sys.argv) > 2 else 3

h = (ep / "index.html").read_text(encoding="utf-8", errors="replace")
srcs = []
for m in re.finditer(r'<video\b[^>]*src="([^"]+)"', h):
    if m.group(1) not in srcs:
        srcs.append(m.group(1))

print(f"{len(srcs)} distinct video sources, {reps} probes each\n")
print(f"{'clip':52} {'MB':>7} {'best':>8} {'worst':>8}")
rows = []
for s in srcs:
    p = ep / s
    if not p.exists():
        print(f"{s:52} MISSING")
        continue
    times = []
    for _ in range(reps):
        t0 = time.perf_counter()
        # The probe that matters is the one hyperframes runs at video_extract, and it is not
        # the cheap format=duration read: -count_packets walks every packet in the file, so
        # cost tracks packet count, not megabytes. Its deadline is hardcoded at 120s.
        r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                            "-count_packets", "-show_entries",
                            "stream=nb_read_packets,r_frame_rate", "-of", "json", str(p)],
                           capture_output=True, text=True)
        times.append(time.perf_counter() - t0)
        if r.returncode != 0:
            print(f"{s:52} ffprobe rc={r.returncode} {r.stderr.strip()[:60]}")
    mb = p.stat().st_size / 1e6
    rows.append((max(times), min(times), mb, s))
    print(f"{Path(s).name:52} {mb:7.1f} {min(times):7.2f}s {max(times):7.2f}s")

rows.sort(reverse=True)
print()
worst, best, mb, s = rows[0]
print(f"slowest clip: {Path(s).name}  {worst:.2f}s worst  ({mb:.1f} MB)")
print(f"total worst-case probe pass: {sum(r[0] for r in rows):.1f}s over {len(rows)} clips")
