#!/usr/bin/env python3
"""Stop a render that will capture frames to disk instead of streaming them into ffmpeg.

Camille's full render (25 Oct 26, 1205 s, RENDER_WORKERS=2) logged `streaming-encode gate {"enabled":false,
"reason":"multi_worker"}` and asked for 75.0 GB of frame storage with 71.5 GB free. Moore at 2 workers streamed
(`parallel_forced`): whether hyperframes takes the parallel streaming route depends on the composition, so the
worker count alone does not tell. learnings/render.md (25 Oct 26): under 100 GB free, full renders run at 1 worker.

  stream_gate.py launch <draft|full> <workers> <episode dir>   exit 1 = refuse before launch (render.cmd)
  stream_gate.py watch <render log> <done marker> <preflight log>  runs beside the render; kills it when the
      gate line says enabled:false, is missing WATCH_S after launch, or the render already runs on something
      other than what it asked for (used_vs_asked)
  stream_gate.py check <render log> [mp4]   after the render (render.cmd, verify_render.sh): exit 1 and one
      [FALLBACK] line per way the render ran on something other than what it asked for

ZBook renders (driver 595.95, Oct 26): ffmpeg 8.1.2's NVENC needs driver 610+, the nvenc probe failed on every
render and hyperframes encoded on Intel QSV instead without saying so. Six episodes went out that way.
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
ASKED = re.compile(r"GPU: (.+)")  # hyperframes' plan line: "encoder GPU" = --gpu, "browser GPU" = --browser-gpu
BROWSER = re.compile(r"browserGpuMode probe .*")  # one per capture worker, names the WebGL renderer


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


def used_vs_asked(text, video_encoder=None):
    """One [FALLBACK] line per way the render ran on something other than it asked for; [] = ran as asked.

    video_encoder is the output's video-stream encoder tag ('Lavc62.28.102 h264_nvenc'), None when not probed.
    hyperframes picks its encoder silently: a failed probe is printed only under HYPERFRAMES_DEBUG_GPU_PROBE=1
    (render.cmd sets it), so the tag on the finished file is the proof once it exists.
    """
    m = ASKED.search(text)
    if not m:
        return ["[FALLBACK] no 'GPU:' line in the render log: what the render asked for is unknown"]
    asked, out = m.group(1), []
    if "encoder GPU" in asked:
        if "[gpuEncoder] nvenc probe failed" in text:
            out.append("[FALLBACK] encoder: --gpu asked, the nvenc probe failed, hyperframes encoded on another encoder")
        if video_encoder is not None and "nvenc" not in video_encoder:
            out.append(f"[FALLBACK] encoder: --gpu asked, the output was encoded by '{video_encoder}', not nvenc")
    if "browser GPU" in asked:
        probes = BROWSER.findall(text)
        if not probes or any("NVIDIA" not in p for p in probes):
            out.append("[FALLBACK] browser: --browser-gpu asked, a capture worker did not run on the NVIDIA GPU: "
                       + ("; ".join(p[:160] for p in probes if "NVIDIA" not in p) or "no browserGpuMode probe line"))
    gates = [json.loads(g) for g in GATE.findall(text)]
    if not gates or any(g.get("enabled") is not True for g in gates):
        out.append("[FALLBACK] capture: streaming asked, frames went to disk ("
                   + (", ".join(str(g.get("reason")) for g in gates) or "no streaming-encode gate line") + ")")
    return out


def video_encoder(mp4):
    """The video stream's encoder tag, read with the ffprobe render.cmd names (HYPERFRAMES_FFPROBE_PATH)."""
    import os
    r = subprocess.run([os.environ.get("HYPERFRAMES_FFPROBE_PATH", "ffprobe"), "-v", "error", "-select_streams", "v:0",
                        "-show_entries", "stream_tags=encoder", "-of", "default=nw=1:nk=1", str(mp4)],
                       capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"[stream_gate] ffprobe failed on {mp4}: {r.stderr.strip()[-300:]}")
    return r.stdout.strip()


def check(log, mp4=None):
    text = log.read_text(encoding="utf-8", errors="replace") if log.exists() else ""
    fallbacks = used_vs_asked(text, video_encoder(mp4) if mp4 else None)
    for line in fallbacks:
        print(line)
    print(f"[stream_gate] RENDER FAILED: it ran on something other than it asked for ({log})" if fallbacks
          else "[stream_gate] OK: encoder, browser GPU and streaming capture are what the render asked for")
    return 1 if fallbacks else 0


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
            fallbacks = used_vs_asked(text)  # the probes print before the gate line, so this is minute one
            if not fallbacks:
                return 0
            verdict = "; ".join(fallbacks)
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
    if a[:1] == ["check"] and len(a) in (2, 3):
        sys.exit(check(Path(a[1]), Path(a[2]) if len(a) == 3 else None))
    sys.exit(__doc__)
