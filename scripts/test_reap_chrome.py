"""Self-check for scripts/reap_chrome.py: python3 scripts/test_reap_chrome.py

Fake process records only: no test reads or touches a real process. Each case is a Chrome the reaper must kill or
must spare; sparing a live gate's Chrome or the owner's own browser matters as much as reaping the orphans.
"""
import json
import sys
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
import reap_chrome  # noqa: E402
from reap_chrome import select  # noqa: E402

FAILS = []
MIN = 60 * 10**7  # one minute in FILETIME ticks
NOW = 1000 * MIN
TEMP = r"C:\Users\Sidhartha\AppData\Local\Temp"


def check(name, cond):
    if not cond:
        FAILS.append(name)
    print(("ok   " if cond else "FAIL ") + name)


def proc(pid, ppid, created, name="chrome.exe", session=0, profile=None, cmd=None):
    if cmd is None and profile:
        cmd = f'"chrome.exe" --headless --user-data-dir={TEMP}\\{profile} --remote-debugging-pipe'
    return {"pid": pid, "ppid": ppid, "session": session, "name": name, "created": created, "cmd": cmd}


def d(name, minutes_old):
    return {"name": name, "created": NOW - minutes_old * MIN}


P1, P2, P3, P4 = (f"playwright_chromiumdev_profile-{x}" for x in ("aB12cd", "Ef34gh", "Ij56kl", "Mn78op"))
procs = [
    proc(4, 0, 0, name="System"),
    # orphan root: its node (pid 100) is gone; a renderer and a gpu process hang below it
    proc(201, 100, 10 * MIN, profile=P1),
    proc(202, 201, 10 * MIN + 1, cmd="chrome.exe --type=renderer"),
    proc(203, 201, 10 * MIN + 2, cmd="chrome.exe --type=gpu-process"),
    # live gate: node 300 is alive and started before its Chrome
    proc(300, 1, 20 * MIN, name="node.exe"),
    proc(301, 300, 21 * MIN, profile=P2),
    proc(302, 301, 21 * MIN + 1, cmd="chrome.exe --type=renderer"),
    # reused parent pid: pid 400 now belongs to a process that started AFTER this Chrome, so its node is dead
    proc(400, 1, 50 * MIN, name="svchost.exe"),
    proc(401, 400, 30 * MIN, profile=P3),
    # the owner's own Playwright browser in his desktop session, parent dead: never touched
    proc(501, 999, 5 * MIN, session=1, profile=P4),
    # a plain session-0 chrome with a dead parent but no Playwright profile (not ours)
    proc(601, 998, 5 * MIN, cmd="chrome.exe --no-first-run"),
    # a session-0 chrome whose parent is a live non-chrome process: spared even with an orphan above it
    proc(701, 300, 22 * MIN, cmd="chrome.exe --type=utility"),
]
dirs = [d(P1, 2), d(P2, 120), d(P3, 5), d(P4, 120),
        d("playwright_chromiumdev_profile-Qr90st", 120),   # nobody names it, 2 h old: leftover of a killed gate
        d("playwright_chromiumdev_profile-Uv12wx", 3)]     # nobody names it yet, 3 min old: a gate still launching

kill, gone = select(procs, dirs, NOW)
pids = {p for p, _ in kill}
check("an orphan root with the Playwright profile is killed", 201 in pids)
check("its renderer and gpu children go with it", {202, 203} <= pids)
check("a Chrome whose parent pid was reused by a younger process is an orphan", 401 in pids)
check("a live gate's Chrome and its renderer are spared", not pids & {301, 302})
check("the owner's desktop-session Chrome is spared", 501 not in pids)
check("a session-0 Chrome without a Playwright profile is spared", 601 not in pids)
check("a chrome below a live parent is spared", 701 not in pids)
check("only chrome.exe is ever killed", not pids & {4, 300, 400})
check("each kill carries its start time, so a reused pid is checked again at kill time",
      dict(kill)[201] == 10 * MIN and dict(kill)[401] == 30 * MIN)
check("a reaped Chrome's profile is deleted even when young", P1 in gone and P3 in gone)
check("a live gate's profile is kept even when old", P2 not in gone)
check("a profile named by a desktop-session Chrome is kept", P4 not in gone)
check("an unnamed old leftover profile is deleted", "playwright_chromiumdev_profile-Qr90st" in gone)
check("an unnamed young profile is kept (its gate may be launching)", "playwright_chromiumdev_profile-Uv12wx" not in gone)
check("nothing to reap on a clean host", select([proc(4, 0, 0, name="System")], [], NOW) == ([], []))

# reap(): dry run reads only; --apply sends the kills and deletes in chunks and reports the counts
calls = []


def fake_ps(host, script, timeout=90):
    calls.append(script)
    if "ConvertTo-Json" in script:
        return 0, json.dumps({"procs": procs, "dirs": dirs, "now": NOW})
    if "NtResumeProcess" in script:
        return 0, str(script.split("$a = @(")[1].split(")")[0].count(",") // 2 + 1) + "\n"
    return 0, str(script.count("'playwright_chromiumdev_profile-")) + "\n"


reap_chrome.ps = fake_ps
line = reap_chrome.reap("zbook", apply=False)
check("dry run only reads the host", len(calls) == 1 and "would kill 4 orphan chrome, delete 3 profiles" in line)
calls.clear()
line = reap_chrome.reap("zbook", apply=True)
kills = [c for c in calls if "NtResumeProcess" in c]
check("apply resumes before it stops each process", kills and all(c.index("NtResumeProcess($h)") < c.index("Stop-Process") for c in kills))
check("apply reports what it did", "killed 4 of 4 orphan chrome, deleted 3 of 3 profiles" in line)
many = [proc(1000 + i, 99999, MIN, profile=f"playwright_chromiumdev_profile-z{i:05d}") for i in range(60)]
procs = many  # fake_ps serves this reading now
calls.clear()
reap_chrome.reap("zbook", apply=True)
check("60 orphans go in chunks small enough for the ssh line cap", len([c for c in calls if "NtResumeProcess" in c]) == 3
      and max(len(c) for c in calls) < 2500)
reap_chrome.ps = lambda h, s, timeout=90: (255, "Connection reset by peer")
try:
    reap_chrome.reap("zbook", apply=True)
    check("an unreadable host raises, never reports a clean reap", False)
except RuntimeError as e:
    check("an unreadable host raises, never reports a clean reap", "cannot read processes on zbook" in str(e))

if FAILS:
    sys.exit(f"[test_reap_chrome] FAIL: {FAILS}")
print("[test_reap_chrome] all checks passed")
