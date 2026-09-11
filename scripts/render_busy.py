"""Refuse to start heavy work while a hyperframes render is alive.

Why: 2026-09-11 the Krakatau #4 draft (2 capture workers) ran while the static gate suite
(two headless Chromiums + an ffmpeg batch) was launched on top of it and the owner's
browser — the box went to OOM. render_preflight.py guards the render's own start; this
guards everything that starts DURING a render: blank_scan / graphics_qc (via
playwright_env.mjs), optimize_clips.py, and the slice/draft launchers.

Exit 0 = clear. Exit 3 = a render is running (the command lines are printed).
RENDER_BUSY_OK=1 overrides, for the case where the render itself is the thing being tested.
"""
import os
import subprocess
import sys


def live_renders():
    ps = ("Get-CimInstance Win32_Process | Where-Object { $_.Name -eq 'node.exe' -and "
          "$_.CommandLine -like '*hyperframes*render*' } | ForEach-Object { $_.ProcessId.ToString() + ' ' + $_.CommandLine }")
    out = subprocess.run(["powershell", "-NoProfile", "-Command", ps], capture_output=True, text=True).stdout
    return [l.strip() for l in out.splitlines() if l.strip()]


if __name__ == "__main__":
    if os.environ.get("RENDER_BUSY_OK") == "1":
        sys.exit(0)
    live = live_renders()
    if live:
        print(f"[render_busy] REFUSING — {len(live)} hyperframes render(s) alive; one heavy job at a time (owner 2026-09-11):")
        for l in live:
            print("   ", l[:160])
        sys.exit(3)
