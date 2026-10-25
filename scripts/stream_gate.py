#!/usr/bin/env python3
"""Stop a render that will capture frames to disk instead of streaming them into ffmpeg.

Camille's full render (25 Oct 26, 1205 s, RENDER_WORKERS=2) logged `streaming-encode gate {"enabled":false,
"reason":"multi_worker"}` and asked for 75.0 GB of frame storage with 71.5 GB free. Moore at 2 workers streamed
(`parallel_forced`): whether hyperframes takes the parallel streaming route depends on the composition, so the
worker count alone does not tell. learnings/render.md (25 Oct 26): under 100 GB free, full renders run at 1 worker.

  stream_gate.py launch <draft|full> <workers> <episode dir>   exit 1 = refuse before launch (render.cmd)
  stream_gate.py watch <render log> <done marker> <preflight log>  runs beside the render; kills it when the
      gate line says enabled:false, or is missing WATCH_S after launch
"""
import json
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

MIN_FREE_GB_MULTI = 100  # learnings/render.md 25 Oct 26: Camille needed 75.0 GB at 2 workers
WATCH_S = 480  # the gate line printed within the first 4 min of every measured full render; twice that
GATE = re.compile(r"streaming-encode gate (\{.*?\})")


def launch_refusal(mode, workers, free_gb):
    """Reason to refuse before launch, or None."""
    if mode == "full" and workers > 1 and free_gb < MIN_FREE_GB_MULTI:
        return (f"full render at {workers} workers with {free_gb:.1f} GB free: hyperframes may skip streaming "
                f"(multi_worker) and capture to disk (Camille needed 75.0 GB). Set RENDER_WORKERS=1 or free "
                f"{MIN_FREE_GB_MULTI} GB")


def log_verdict(text, waited_s):
    """'ok', 'pending', or the reason the render must stop."""
    m = GATE.search(text)
    if m:
        gate = json.loads(m.group(1))
        if gate.get("enabled") is True:
            return "ok"
        return f"streaming-encode gate enabled:false, reason {gate.get('reason')} at {gate.get('workerCount')} workers: frames go to disk"
    if waited_s > WATCH_S:
        return f"no streaming-encode gate line {WATCH_S} s after launch"
    return "pending"


def kill_renders():
    import render_busy
    for line in render_busy.live_renders():
        subprocess.run(["taskkill", "/PID", line.split()[0], "/T", "/F"], capture_output=True)


def watch(log, marker, out):
    start = time.time()
    while not marker.exists():
        text = log.read_text(encoding="utf-8", errors="replace") if log.exists() else ""
        verdict = log_verdict(text, time.time() - start)
        if verdict == "ok":
            return 0
        if verdict != "pending":
            with out.open("a", encoding="utf-8") as f:
                f.write(f"[stream_gate] STOPPING THE RENDER: {verdict}. Relaunch with RENDER_WORKERS=1.\n")
            kill_renders()
            return 1
        time.sleep(10)
    return 0


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[:1] == ["launch"] and len(a) == 4:
        why = launch_refusal(a[1], int(a[2]), shutil.disk_usage(a[3]).free / 1e9)
        print(f"[stream_gate] REFUSING TO RENDER: {why}" if why else "[stream_gate] OK before launch")
        sys.exit(1 if why else 0)
    if a[:1] == ["watch"] and len(a) == 4:
        sys.exit(watch(*map(Path, a[1:])))
    sys.exit(__doc__)
