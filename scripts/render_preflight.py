#!/usr/bin/env python3
"""Refuse to start a render while the box is busy.

ep3 v3 lost two renders to `[FFmpeg] ffprobe deadline with code 0` — a deadline miss,
not a corrupt asset. The tell is in the failure summary: between two failures of the
same composition, compileOnlyMs went 95s -> 260s and browserProbeMs 31s -> 99s, on
FEWER videos (23 -> 20). Nothing about the episode got heavier; the machine did. The
Playwright QC gates each run a Chromium over every composition, and a render sharing
8 cores with them starves at the probe stage.

CLAUDE.md already said "don't run other heavy sessions during a final render". This
makes it a gate instead of a sentence, because the failure costs 10 minutes and looks
like an asset problem.

Exits non-zero (and says what to close) if the box is not quiet enough to render.
"""
import subprocess
import sys
from pathlib import Path

# a render itself needs: 3 workers + a capture Chromium + ffmpeg. Anything beyond a
# couple of idle helper processes is competition.
MAX_HEAVY = 2
HEAVY_MB = 120
WATCH = ("chrome.exe", "msedge.exe", "ffmpeg.exe", "ffprobe.exe")


def heavy_processes():
    out = subprocess.run(["tasklist", "/FO", "CSV", "/NH"],
                         capture_output=True, text=True).stdout
    found = []
    for line in out.splitlines():
        parts = [p.strip('"') for p in line.split('","')]
        if len(parts) < 5:
            continue
        name, pid, mem = parts[0], parts[1], parts[4]
        if name.lower() not in WATCH:
            continue
        try:
            mb = int(mem.replace(",", "").replace(" K", "")) / 1024
        except ValueError:
            continue
        if mb >= HEAVY_MB:
            found.append((name, pid, round(mb)))
    return found


busy = heavy_processes()
if len(busy) > MAX_HEAVY:
    print(f"[preflight] REFUSING TO RENDER — {len(busy)} heavy processes are competing "
          f"for the CPU (limit {MAX_HEAVY}):", file=sys.stderr)
    for name, pid, mb in sorted(busy, key=lambda p: -p[2]):
        print(f"    {name:14} pid {pid:>7}  {mb:>6} MB", file=sys.stderr)
    print("[preflight] Close the QC browsers / stop background agents, then re-launch.",
          file=sys.stderr)
    print("[preflight] A render that starts here fails at video_extract with "
          "'ffprobe deadline with code 0', which reads like a bad asset and is not.",
          file=sys.stderr)
    sys.exit(2)

print(f"[preflight] OK — {len(busy)} heavy process(es), under the limit of {MAX_HEAVY}.")
