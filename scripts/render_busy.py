"""Refuse to start heavy work while a hyperframes render is alive, or while RAM headroom is thin.

Why: 2026-09-11 the Krakatau #4 draft (2 capture workers) ran while the static gate suite
(two headless Chromiums + an ffmpeg batch) was launched on top of it and the owner's
browser — the box went to OOM. render_preflight.py guards the render's own start; this
guards everything that starts DURING a render: blank_scan / graphics_qc (via
playwright_env.mjs), optimize_clips.py, and the slice/draft launchers.

Owner rule (2026-09-11): keep ≥1 GB free for the whole render, no compromise. Two capture
workers take ~3 GB, so a launch needs ≥4 GB free (RENDER_MIN_FREE_GB overrides).

Exit 0 = clear. Exit 3 = a render is running, or (with --launch) RAM is under the floor.
RENDER_BUSY_OK=1 overrides, for the case where the render itself is the thing being tested.
"""
import os
import subprocess
import sys

MIN_FREE_GB = float(os.environ.get("RENDER_MIN_FREE_GB", "4"))


def ps(cmd):
    return subprocess.run(["powershell", "-NoProfile", "-Command", cmd], capture_output=True, text=True).stdout.strip()


def live_renders():
    out = ps("Get-CimInstance Win32_Process | Where-Object { $_.Name -eq 'node.exe' -and "
             "$_.CommandLine -like '*hyperframes*render*' } | ForEach-Object { $_.ProcessId.ToString() + ' ' + $_.CommandLine }")
    return [l.strip() for l in out.splitlines() if l.strip()]


def free_gb():
    return float(ps("(Get-CimInstance Win32_OperatingSystem).FreePhysicalMemory") or 0) / 1048576


if __name__ == "__main__":
    if os.environ.get("RENDER_BUSY_OK") == "1":
        sys.exit(0)
    live = live_renders()
    if live:
        print(f"[render_busy] REFUSING — {len(live)} hyperframes render(s) alive; one heavy job at a time (owner 2026-09-11):")
        for l in live:
            print("   ", l[:160])
        sys.exit(3)
    # the RAM floor protects a RENDER about to start (--launch); a gate's single headless Chromium (~300 MB) only needs 'no render alive'
    free = free_gb()
    if "--launch" in sys.argv and free < MIN_FREE_GB:
        print(f"[render_busy] REFUSING — {free:.1f} GB free, need {MIN_FREE_GB:g} GB so the render keeps ≥1 GB headroom (owner 2026-09-11). Close a browser or wait.")
        sys.exit(3)
    print(f"[render_busy] OK — no render alive, {free:.1f} GB free")
