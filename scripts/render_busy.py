"""Refuse to start heavy work while a hyperframes render is alive, or while RAM headroom is thin.

Why: 2026-09-11 the Krakatau #4 draft (2 capture workers) ran while the static gate suite
(two headless Chromiums + an ffmpeg batch) was launched on top of it and the owner's
browser — the box went to OOM. render_preflight.py guards the render's own start; this
guards everything that starts DURING a render: blank_scan / graphics_qc (via
playwright_env.mjs), optimize_clips.py, and the slice/draft launchers.

Owner rule (2026-09-11): keep ≥1 GB free for the whole render, no compromise. Two capture
workers take ~3 GB, so a launch needs ≥4 GB free (RENDER_MIN_FREE_GB overrides).

--launch also pins every headless Chrome hyperframes can launch to the dedicated GPU
(HKCU DirectX GpuPreference=2). Owner 2026-09-15: every render before that day captured on the
Intel iGPU (GTX 1650 at 0 %, 100 % CPU, ~6 GB RAM); the registry pin alone moves capture to the
1650 (probe line in render_full.log says NVIDIA). A new hyperframes/Playwright Chrome build is a
new exe path, so the pin is re-asserted on every launch, never once by hand.

--light (freeze_scan.mjs via QC_LIGHT=1): ONE half-resolution Chromium page may run beside a live
render when at least LIGHT_MIN_FREE_GB (default 2) is free, so composers can test a fix without
queueing behind a 15-minute draft (owner 17 Sep 26). The full browser gates stay exclusive.

Exit 0 = clear. Exit 3 = a render is running, or (with --launch) RAM is under the floor.
RENDER_BUSY_OK=1 overrides, for the case where the render itself is the thing being tested.
"""
import ctypes
import glob
import os
import subprocess
import sys
import winreg

MIN_FREE_GB = float(os.environ.get("RENDER_MIN_FREE_GB", "4"))


def ps(cmd):
    return subprocess.run(["powershell", "-NoProfile", "-Command", cmd], capture_output=True, text=True).stdout.strip()


def live_renders():
    out = ps("Get-CimInstance Win32_Process | Where-Object { $_.Name -eq 'node.exe' -and "
             "$_.CommandLine -like '*hyperframes*render*' } | ForEach-Object { $_.ProcessId.ToString() + ' ' + $_.CommandLine }")
    return [l.strip() for l in out.splitlines() if l.strip()]


def pin_chrome_to_dedicated_gpu():
    """Set GpuPreference=2 (high performance) for every headless Chrome hyperframes may launch."""
    home = os.path.expanduser("~")
    exes = glob.glob(os.path.join(home, ".cache", "hyperframes", "chrome", "**", "chrome-headless-shell.exe"), recursive=True)
    exes += glob.glob(os.path.join(home, "AppData", "Local", "ms-playwright", "chromium*", "**", "chrome-headless-shell.exe"), recursive=True)
    key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\DirectX\UserGpuPreferences")
    for exe in exes:
        exe = os.path.normpath(exe)
        try:
            cur = winreg.QueryValueEx(key, exe)[0]
        except FileNotFoundError:
            cur = ""
        if cur != "GpuPreference=2;":
            winreg.SetValueEx(key, exe, 0, winreg.REG_SZ, "GpuPreference=2;")
            print(f"[gpu-pin] pinned to dedicated GPU: {exe}")
    if not exes:
        print("[gpu-pin] WARNING no chrome-headless-shell.exe found to pin")


class _MemStatus(ctypes.Structure):
    _fields_ = [("dwLength", ctypes.c_ulong), ("dwMemoryLoad", ctypes.c_ulong)] + [(n, ctypes.c_ulonglong) for n in (
        "ullTotalPhys", "ullAvailPhys", "ullTotalPageFile", "ullAvailPageFile", "ullTotalVirtual", "ullAvailVirtual",
        "ullAvailExtendedVirtual")]


def free_gb():
    # GlobalMemoryStatusEx, not a second PowerShell CIM query: same figure (3.97 vs 4.01 GB read back
    # to back, 27 Sep 26) without ~2.9 s of PowerShell + WMI start-up on every Chromium gate launch
    m = _MemStatus(dwLength=ctypes.sizeof(_MemStatus))
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
    return m.ullAvailPhys / 2**30


if __name__ == "__main__":
    if os.environ.get("RENDER_BUSY_OK") == "1":
        sys.exit(0)
    live = live_renders()
    if live and "--light" in sys.argv:
        free, floor = free_gb(), float(os.environ.get("LIGHT_MIN_FREE_GB", "2"))
        if free >= floor:
            print(f"[render_busy] OK (light) — render alive, {free:.1f} GB free >= {floor:g} GB: one half-resolution page may run beside it")
            sys.exit(0)
        print(f"[render_busy] REFUSING (light) — render alive and only {free:.1f} GB free, need {floor:g} GB")
        sys.exit(3)
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
    if "--launch" in sys.argv:
        pin_chrome_to_dedicated_gpu()
    print(f"[render_busy] OK — no render alive, {free:.1f} GB free")
