"""Refuse to start heavy work while a hyperframes render is alive, or while RAM headroom is thin.

Why: 2026-09-11 the Krakatau #4 draft (2 capture workers) ran while the static gate suite
(two headless Chromiums + an ffmpeg batch) was launched on top of it and the owner's
browser — the box went to OOM. render_preflight.py guards the render's own start; this
guards everything that starts DURING a render: blank_scan / graphics_qc (via
playwright_env.mjs), optimize_clips.py, and the slice/draft launchers.

Owner rule (2026-09-11): keep ≥1 GB free for the whole render, no compromise. --launch <file>
picks the most capture workers (RENDER_WORKERS down to 1) whose need_gb() fits free RAM and writes
that number to <file> for render.cmd; fewer workers beats waiting (owner 18 Oct 26). It refuses only
when even 1 worker does not fit (MIN_FREE_GB; RENDER_MIN_FREE_GB overrides that 1-worker floor).

--launch also pins every headless Chrome hyperframes can launch to the dedicated GPU
(HKCU DirectX GpuPreference=2). Owner 2026-09-15: every render before that day captured on the
Intel iGPU (GTX 1650 at 0 %, 100 % CPU, ~6 GB RAM); the registry pin alone moves capture to the
1650 (probe line in render_full.log says NVIDIA). A new hyperframes/Playwright Chrome build is a
new exe path, so the pin is re-asserted on every launch, never once by hand.

--light (freeze_scan.mjs via QC_LIGHT=1): ONE half-resolution Chromium page may run beside a live
render when at least LIGHT_MIN_FREE_GB (default 2) is free, so composers can test a fix without
queueing behind a 15-minute draft (owner 17 Sep 26). The full browser gates stay exclusive.

--jobs: print every heavy job alive (render, render_acts, snapshot_queue, run_gates, test_detectors, graphics_qc,
blank_scan), exit 0 idle / 1 busy / 2 process table unreadable. For wait scripts; matches by exe + argv and skips its own parent chain.

Exit 0 = clear. Exit 3 = a render is running, or (with --launch) not even 1 worker fits.
RENDER_BUSY_OK=1 overrides, for the case where the render itself is the thing being tested.

The heavy lock (owner 26 Oct 26; why: learnings/render.md): one heavy job per machine at a time. render.cmd, pin_ritual.py, TTS (tts_episode.py, tts_clone.py), the face
pass (circle_face.py) and e2e.py book ~/.storm-heavy.lock before they start and wait their turn. A job started
from the ASUS over ssh runs as the same user on the ZBook, so it books the same file. The file records holder,
job, machine, pid and start time. A holder whose pid is gone (or reused by a newer process) is dead and its
lock is taken over. A waiting job prints who holds the lock and waits in-process (no window, no shell loop).
  with render_busy.heavy_lock("tts ep-x"): ...   a Python job: held by this process, released when the block ends
  render_busy.py --hold <job>                     a cmd script (render.cmd): held by the calling cmd.exe until
  render_busy.py --release                        it calls --release (or exits); --hold again from it passes
The no-argument gate mode (not --light) also waits while another job holds the lock, without booking it, so the
snapshot worker's call waits its turn. A child of the holder passes: HEAVY_LOCK_TOKEN in its environment matches.
"""
import ctypes
import glob
import json
import os
import platform
import subprocess
import sys
import time
import uuid
import winreg
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path


def need_gb(workers):
    # 1.0 headroom + 0.33 node+ffmpeg + 1.27 Chrome per worker (1-worker draft, 18 Oct 26: Chrome x5 1,273 MB, node 173 MB, ffmpeg 160 MB) = 2.6 GB at 1, 3.87 GB at 2 (the old 4 GB floor)
    return 1.0 + 0.33 + 1.27 * workers


MIN_FREE_GB = float(os.environ.get("RENDER_MIN_FREE_GB", need_gb(1)))


def workers_that_fit(requested, free):
    """Most workers from `requested` down to 1 whose RAM need fits `free` GB; 0 under MIN_FREE_GB."""
    if free < MIN_FREE_GB:
        return 0
    for n in range(requested, 1, -1):
        if free >= need_gb(n):
            return n
    return 1


def ps(cmd):
    """(exit code, stdout, stderr) of a PowerShell command, decoded as UTF-8 so an accented command line cannot crash the scan."""
    r = subprocess.run(["powershell", "-NoProfile", "-Command", "[Console]::OutputEncoding=[Text.Encoding]::UTF8; " + cmd],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, r.stdout.strip(), r.stderr.strip()


# --- "is a heavy job alive?": match the executable and its argv, never a substring of a command line ---
# 2026-10-29: two checkers matched a regex against every process's command line, so they counted themselves, their
# parent shell, or any agent shell whose bash -c / powershell -Command string merely MENTIONED render_acts.py or
# test_detectors, and waited forever or refused. A job is found here only by exact exe name plus the argv shape
# below; the checker's own pid and its whole parent chain are never a job. This is the one owner of the scan:
# wait scripts call `render_busy.py --jobs` (exit 0 idle, 1 busy, 2 unreadable: never idle) instead of their own regex.
PY_JOBS = {"render_acts.py", "snapshot_queue.py", "run_gates.py", "test_detectors.py",
           "test_gates.py", "e2e.py"}  # python.exe, argv[1] script
NODE_JOBS = {"graphics_qc.mjs", "blank_scan.mjs"}  # node.exe, script arg
_CODE_FLAGS = {"-c", "-m", "-e", "-p", "--eval", "--print"}  # the next arg is code, not a script path


def process_table():
    """[{ProcessId, ParentProcessId, Name, CommandLine}] for every process. Raises when the query fails or comes back
    empty: a live machine always has processes, so no table means "could not look", never "idle"."""
    code, out, err = ps("Get-CimInstance Win32_Process | Select-Object ProcessId,ParentProcessId,Name,CommandLine | ConvertTo-Json -Compress")
    if code != 0 or not out:
        raise RuntimeError(f"process query failed (exit {code}): {err[-200:] or 'empty output'}")
    rows = json.loads(out)
    return [rows] if isinstance(rows, dict) else rows


def split_args(cmdline):
    """argv of a Windows command line, the way the C runtime splits it."""
    n = ctypes.c_int()
    shell32 = ctypes.WinDLL("shell32")
    shell32.CommandLineToArgvW.restype = ctypes.POINTER(ctypes.c_wchar_p)
    argv = shell32.CommandLineToArgvW(cmdline, ctypes.byref(n))
    try:
        return [argv[i] for i in range(n.value)]
    finally:
        ctypes.WinDLL("kernel32").LocalFree(argv)


def script_arg(args):
    """The first non-flag arg, or None when the interpreter runs inline code (-c/-m/-e/-p)."""
    for a in args:
        if a in _CODE_FLAGS:
            return None
        if not a.startswith("-"):
            return a
    return None


def job_kind(name, cmdline):
    """Label of the heavy job this process IS (exact exe name + argv), else None."""
    name, args = (name or "").lower(), split_args(cmdline)[1:] if cmdline else []
    base = os.path.basename((script_arg(args) or "").replace("\\", "/"))
    if name in ("python.exe", "pythonw.exe") and base in PY_JOBS:
        return base
    if name == "node.exe":
        if base in NODE_JOBS:
            return base
        code = next((i for i, a in enumerate(args) if a in _CODE_FLAGS), len(args))
        scan = args[:code]  # a hyperframes CLI path (or npx's hyperframes@x) followed by a separate `render` arg
        if any("hyperframes" in a.lower() and not a.startswith("-") and "render" in scan[i + 1:] for i, a in enumerate(scan)):
            return "hyperframes render"
    return None


def ancestors(table, pid):
    """pid and every parent above it, so a checker never counts itself or the shell that launched it."""
    parent, chain = {r["ProcessId"]: r["ParentProcessId"] for r in table}, set()
    while pid and pid not in chain:
        chain.add(pid)
        pid = parent.get(pid)
    return chain


def busy_jobs(table=None, self_pid=None, kinds=None):
    """[(pid, kind, commandline)] of live heavy jobs; `kinds` limits which (default all)."""
    table = process_table() if table is None else table
    skip = ancestors(table, os.getpid() if self_pid is None else self_pid)
    jobs = [(r["ProcessId"], job_kind(r["Name"], r["CommandLine"]), r["CommandLine"]) for r in table if r["ProcessId"] not in skip]
    return [j for j in jobs if j[1] and (kinds is None or j[1] in kinds)]


def live_renders():
    return [f"{pid} {cmd}" for pid, _, cmd in busy_jobs(kinds={"hyperframes render"})]


LOCK_JOBS = {"e2e.py", "render_acts.py"}  # they book the heavy lock: alive beside a render that holds it = waiting for it
_MODES = {"--launch", "--hold", "--release", "--jobs"}


def running_jobs():
    """Heavy jobs a render must not start beside (audit R4: the 11 Sep OOM): every busy_jobs() job outside this
    process's chain, except one that waits for the heavy lock render.cmd holds (a LOCK_JOBS kind, or a job with a
    render_busy.py gate check below it, which waits in wait_free()). Waiting on those would deadlock."""
    table = process_table()
    parked = set()
    for r in table:
        args = split_args(r["CommandLine"])[1:] if r["CommandLine"] else []
        if ((r["Name"] or "").lower() in ("python.exe", "pythonw.exe") and not _MODES & set(args)
                and os.path.basename((script_arg(args) or "").replace("\\", "/")) == "render_busy.py"):
            parked |= ancestors(table, r["ProcessId"])
    return [j for j in busy_jobs(table) if j[1] not in LOCK_JOBS and j[0] not in parked]


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


POLL_S = 5  # seconds between looks at a held lock
_k32 = ctypes.WinDLL("kernel32")
_k32.OpenProcess.restype = ctypes.c_void_p  # a HANDLE, not the default 32-bit int


def lock_path():
    return Path(os.environ.get("HEAVY_LOCK_FILE") or Path.home() / ".storm-heavy.lock")  # tests point it at a temp file


def created(pid):
    """Creation time (FILETIME) of a running pid; None when it is not running."""
    h = _k32.OpenProcess(0x1000, False, pid)  # PROCESS_QUERY_LIMITED_INFORMATION
    if not h:  # gone, or access denied: holders are this user's own processes, so a denied pid is someone else's now
        return None
    h = ctypes.c_void_p(h)
    try:
        code, t = ctypes.c_ulong(), (ctypes.c_ulonglong * 4)()
        if not _k32.GetExitCodeProcess(h, ctypes.byref(code)) or code.value != 259:  # 259 = STILL_ACTIVE
            return None
        _k32.GetProcessTimes(h, *(ctypes.byref(t, 8 * i) for i in range(4)))
        return t[0]
    finally:
        _k32.CloseHandle(h)


def holder_alive(rec):
    return created(rec["pid"]) == rec["created"]  # gone, or the pid reused by a newer process = the holder died


def read_lock(p):
    try:
        rec = json.loads(p.read_text(encoding="utf-8"))
        rec["pid"], rec["created"]  # a record without them is unreadable, like a half-written one
        return rec
    except (OSError, ValueError, KeyError, TypeError):
        return None


def describe(rec):
    return (f"{rec.get('job')} (holder {rec.get('holder')}, machine {rec.get('machine')}, pid {rec['pid']}, "
            f"since {rec.get('start')})")


def take(job, pid):
    """Wait until this machine's heavy lock is free, then book it for pid. Returns the record, or None when the
    caller's own holder already has it (a child of the holder)."""
    p, mine, shown = lock_path(), os.environ.get("HEAVY_LOCK_TOKEN"), None
    ssh = os.environ.get("SSH_CONNECTION", "").split()
    rec = {"holder": os.environ.get("HEAVY_LOCK_HOLDER")
                     or os.environ.get("USERNAME", "?") + (f" via ssh from {ssh[0]}" if ssh else " local"),
           "job": job, "machine": platform.node(), "pid": pid, "created": created(pid),
           "start": datetime.now().isoformat(timespec="seconds"), "token": uuid.uuid4().hex}
    while True:
        try:
            fd = os.open(p, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        except FileExistsError:
            cur = read_lock(p)
            if cur is None:  # being written by its taker this instant, or corrupt: a minute on, it counts as dead
                try:
                    age = time.time() - p.stat().st_mtime
                except OSError:
                    continue
                if age < 60:
                    time.sleep(0.2)
                    continue
                cur = {"pid": 0, "created": 0, "job": "an unreadable lock file"}
            if (mine and cur.get("token") == mine) or (cur["pid"], cur["created"]) == (pid, rec["created"]):
                return None  # a child of the holder, or the holder itself again (a wrapper calling render.cmd twice)
            if not holder_alive(cur):
                stale = p.with_name(f"{p.name}.{rec['token']}.stale")
                try:
                    os.rename(p, stale)  # one taker wins the rename; the loser sees the new file next pass
                except OSError:
                    continue
                moved = read_lock(stale)
                if moved and holder_alive(moved):  # a live lock was booked between our read and the rename: put it back
                    os.rename(stale, p)  # shortcut: fails if a third job books in that gap; never seen, add a mutex if it is
                    continue
                os.remove(stale)
                print(f"[heavy-lock] took over a dead holder's lock: {describe(cur)}", flush=True)
                continue
            if cur != shown:
                print(f"[heavy-lock] WAITING to start {job}: this machine's heavy lock is held by {describe(cur)}", flush=True)
                shown = cur
            time.sleep(POLL_S)
            continue
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(rec, f)
        print(f"[heavy-lock] booked for {job} (pid {pid}, {rec['machine']})", flush=True)
        return rec


@contextmanager
def heavy_lock(job):
    """Hold this machine's heavy lock for the current process while the block runs; its children pass through."""
    rec = take(job, os.getpid())  # None: a child of the holder, which owns neither the lock nor the token
    if rec:
        os.environ["HEAVY_LOCK_TOKEN"] = rec["token"]
    try:
        yield
    finally:
        if rec:
            os.environ.pop("HEAVY_LOCK_TOKEN", None)
            release(lambda cur: cur["token"] == rec["token"])


def release(ours):
    """Delete the lock if ours(record) says it is ours. A waiter reading the file at that instant blocks the delete
    (WinError 32), so it is retried for up to 5 s."""
    p = lock_path()
    for _ in range(50):
        cur = read_lock(p)
        if not cur or not ours(cur):
            return
        try:
            p.unlink()
            return
        except PermissionError:
            time.sleep(0.1)
    print(f"[heavy-lock] could not delete {p}; the next job takes it over once this process exits", flush=True)


def wait_free():
    """Gate mode: wait while another job holds the lock, without booking it."""
    p, mine, shown = lock_path(), os.environ.get("HEAVY_LOCK_TOKEN"), None
    while (cur := read_lock(p)) and cur.get("token") != mine and holder_alive(cur):
        if cur != shown:
            print(f"[heavy-lock] WAITING: this machine's heavy lock is held by {describe(cur)}", flush=True)
            shown = cur
        time.sleep(POLL_S)


def main():
    if "--hold" in sys.argv:  # before RENDER_BUSY_OK: that override skips render.cmd's RAM and live-render checks, not its turn
        take(sys.argv[sys.argv.index("--hold") + 1], os.getppid())
        sys.exit(0)
    if "--release" in sys.argv:  # render.cmd, before each exit: frees what --hold booked for the same cmd.exe
        parent = (os.getppid(), created(os.getppid()))
        release(lambda cur: (cur["pid"], cur["created"]) == parent)
        sys.exit(0)
    if "--jobs" in sys.argv:  # wait scripts: print every heavy job alive, exit 0 idle / 1 busy / 2 unreadable (no RAM check, no lock)
        try:
            jobs = busy_jobs()
        except RuntimeError as e:  # never IDLE on an unread table
            print(f"[render_busy] ERROR - cannot read the process table: {e}")
            sys.exit(2)
        for pid, kind, cmd in jobs:
            print(f"{pid} {kind}: {cmd[:160]}")
        print(f"[render_busy] {'BUSY' if jobs else 'IDLE'} - {len(jobs)} heavy job(s)")
        sys.exit(1 if jobs else 0)
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
    if "--launch" not in sys.argv and "--light" not in sys.argv:  # --light may run beside a heavy job; render.cmd already holds the lock (--hold) when it gets to --launch
        wait_free()
    # the RAM floor protects a RENDER about to start (--launch); a gate's single headless Chromium (~300 MB) only needs 'no render alive'
    free = free_gb()
    if "--launch" in sys.argv:
        requested = int(os.environ["RENDER_WORKERS"])  # render.cmd sets the default
        n = workers_that_fit(requested, free)
        if n == 0:
            print(f"[render_busy] REFUSING — {free:.1f} GB free, 1 worker needs {MIN_FREE_GB:.1f} GB so the render keeps ≥1 GB headroom (owner 2026-09-11)")
            sys.exit(3)
        if n < requested:
            print(f"[FALLBACK] fewer workers: {requested} -> {n}, {free:.1f} GB free")
        pin_chrome_to_dedicated_gpu()
        Path(sys.argv[sys.argv.index("--launch") + 1]).write_text(str(n), encoding="ascii")
        print(f"[render_busy] workers {n} ({need_gb(n):.1f} GB needed)")
    print(f"[render_busy] OK — no render alive, {free:.1f} GB free")


if __name__ == "__main__":
    main()
