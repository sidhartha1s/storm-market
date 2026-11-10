"""Self-check for render_busy --launch picking the worker count that fits free RAM:
python3 scripts/test_render_busy.py

Free RAM is injected (render_busy.free_gb replaced); no render, no registry write (the GPU pin is
stubbed), no process scan (live_renders stubbed). The 3.3 GB case is the 18 Oct 26 Joplin launch
that sat refused for 34 minutes, then stalled on 2 workers."""
import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
import render_busy  # noqa: E402

FAILS = []


def check(name, cond, detail=""):
    if cond:
        print(f"PASS {name}")
    else:
        FAILS.append(name)
        print(f"FAIL {name} {detail}")


REAL_LIVE_RENDERS = render_busy.live_renders
render_busy.live_renders = lambda: []
render_busy.pin_chrome_to_dedicated_gpu = lambda: None


def launch(free, requested, table=(), sleeps=None):
    """Run main() --launch as render.cmd does, against a fake process table of other jobs; return (exit code, stdout,
    workers file text or None). A sleep (a wait for a job) is recorded in `sleeps` and empties the table."""
    render_busy.free_gb = lambda: free
    os.environ["RENDER_WORKERS"] = str(requested)
    os.environ.pop("RENDER_BUSY_OK", None)
    cur, real = list(table), (render_busy.process_table, render_busy.time.sleep)
    render_busy.process_table = lambda: cur
    render_busy.time.sleep = lambda s: ((sleeps if sleeps is not None else []).append(s), cur.clear())
    try:
        with tempfile.TemporaryDirectory() as d:
            out_file = Path(d) / "render_draft.workers"
            sys.argv = ["render_busy.py", "--launch", str(out_file)]
            buf, code = io.StringIO(), 0
            with contextlib.redirect_stdout(buf):
                try:
                    render_busy.main()
                except SystemExit as e:
                    code = e.code
            return code, buf.getvalue(), out_file.read_text() if out_file.exists() else None
    finally:
        render_busy.process_table, render_busy.time.sleep = real


code, out, n = launch(4.2, 2)
check("4.2 GB free, request 2 -> 2 workers", (code, n) == (0, "2"), f"code={code} n={n} out={out!r}")
check("4.2 GB free, request 2 -> no [FALLBACK] line", "[FALLBACK]" not in out, out)

code, out, n = launch(3.3, 2)
check("3.3 GB free, request 2 -> 1 worker", (code, n) == (0, "1"), f"code={code} n={n} out={out!r}")
check("3.3 GB free, request 2 -> [FALLBACK] line",
      "[FALLBACK] fewer workers: 2 -> 1, 3.3 GB free" in out, out)

code, out, n = launch(2.0, 2)
check("2.0 GB free -> exit 3, no workers file", (code, n) == (3, None), f"code={code} n={n} out={out!r}")
check("2.0 GB free -> refusal never says close or quit",
      "close" not in out.lower() and "quit" not in out.lower(), out)
check("2.0 GB free -> refusal states the GB numbers", "2.0 GB free" in out and "2.6 GB" in out, out)

code, out, n = launch(6.0, 3)
check("6.0 GB free, request 3 -> 3 workers (need 5.14 GB)", (code, n) == (0, "3"), f"code={code} n={n} out={out!r}")

code, out, n = launch(4.2, 3)
check("4.2 GB free, request 3 -> 2 workers with [FALLBACK] 3 -> 2",
      (code, n) == (0, "2") and "[FALLBACK] fewer workers: 3 -> 2, 4.2 GB free" in out, f"code={code} n={n} out={out!r}")

render_busy.MIN_FREE_GB = 1.5  # what RENDER_MIN_FREE_GB=1.5 sets
code, out, n = launch(2.0, 1)
check("RENDER_MIN_FREE_GB=1.5 override: 2.0 GB free, request 1 -> 1 worker", (code, n) == (0, "1"), f"code={code} n={n} out={out!r}")
render_busy.MIN_FREE_GB = 4.5
code, out, n = launch(4.0, 2)
check("RENDER_MIN_FREE_GB=4.5 override is the floor for any launch: 4.0 GB, request 2 -> exit 3",
      (code, n) == (3, None), f"code={code} n={n} out={out!r}")
render_busy.MIN_FREE_GB = render_busy.need_gb(1)

# audit R4 (11 Nov 26): --launch looked only for live renders, so a render started on top of a running gate (the 11 Sep
# OOM case) and render.cmd then deleted that gate's staged _*_tmp.html. A job that is itself waiting for the heavy lock
# render.cmd already holds must not be waited for, or neither ever runs: e2e.py and render_acts.py book the lock, and a
# gate parked in its render_busy.py check (playwright_env.mjs) waits in wait_free().
def row(pid, parent, name, cmd):
    return {"ProcessId": pid, "ParentProcessId": parent, "Name": name, "CommandLine": cmd}


QC = row(501, 1, "node.exe", r'node.exe C:\r\scripts\graphics_qc.mjs episodes\ep-y')
PARKED = row(502, 501, "python.exe", r'python.exe C:\r\scripts\render_busy.py')
GATES = row(503, 1, "python.exe", r'python.exe C:\r\scripts\run_gates.py episodes\ep-y')
GATES_PARKED = [GATES, row(504, 503, "node.exe", r'node.exe C:\r\scripts\blank_scan.mjs episodes\ep-y'),
                row(505, 504, "python.exe", r'python.exe C:\r\scripts\render_busy.py')]
for label, table, want_wait in (
        ("waits for a running graphics_qc.mjs", [QC], True),
        ("waits for a running run_gates.py", [GATES], True),
        ("does not wait for a graphics_qc.mjs parked in its render_busy check", [QC, PARKED], False),
        ("does not wait for a run_gates.py whose gate is parked in its render_busy check", GATES_PARKED, False),
        ("does not wait for an e2e.py (it books the heavy lock: beside this render it waits)",
         [row(506, 1, "python.exe", r'python.exe C:\r\scripts\e2e.py')], False),
        ("does not wait for a render_acts.py (it books the heavy lock)",
         [row(507, 1, "python.exe", r'python.exe C:\r\scripts\render_acts.py ep-y draft v1')], False)):
    sleeps = []
    code, out, n = launch(6.0, 2, table, sleeps)
    check(f"R4: --launch {label}", (code, n, bool(sleeps)) == (0, "2", want_wait), f"code={code} n={n} sleeps={sleeps} out={out!r}")
code, out, n = launch(6.0, 2, [QC])
check("R4: a waiting --launch names the job it waits for", "WAITING" in out and "501 graphics_qc.mjs" in out, out)

# render.cmd plumbing: run its own lines from the RENDER_WORKERS default through `set /p`, with
# render_busy.py swapped for a stub that runs the real main() at 3.3 GB free, and echo what npx would get.
render_cmd = (S / "render.cmd").read_text(encoding="utf-8").splitlines()
start = next(i for i, l in enumerate(render_cmd) if l.startswith("if not defined RENDER_WORKERS"))
end = next(i for i, l in enumerate(render_cmd) if "set /p RENDER_WORKERS" in l)
with tempfile.TemporaryDirectory() as d:
    stub = Path(d) / "busy_stub.py"
    stub.write_text(f"import sys\nsys.path.insert(0, {str(S)!r})\nimport render_busy\n"
                    "render_busy.free_gb = lambda: 3.3\nrender_busy.live_renders = lambda: []\nrender_busy.running_jobs = lambda: []\n"
                    "render_busy.pin_chrome_to_dedicated_gpu = lambda: None\nrender_busy.main()\n", encoding="utf-8")
    block = "\n".join(render_cmd[start:end + 1]).replace('"%~dp0render_busy.py"', f'"{stub}"')
    dry = Path(d) / "dry.cmd"
    dry.write_text("@echo off\nset MODE=draft\nset PREFLIGHT_LOG=pre.log\n" + block
                   + "\necho WORKERS=%RENDER_WORKERS%\n", encoding="utf-8")
    env = {**os.environ, "RENDER_WORKERS": "2"}
    r = subprocess.run(["cmd", "/c", str(dry)], cwd=d, capture_output=True, text=True, env=env)
    log = (Path(d) / "pre.log").read_text(encoding="utf-8", errors="replace")
    print(f"  render.cmd dry run echoed: {r.stdout.strip()!r}; log: {log.strip()!r}")
    check("render.cmd dry run: request 2 at 3.3 GB free -> --workers gets 1", r.stdout.strip() == "WORKERS=1",
          f"rc={r.returncode} out={r.stdout!r} err={r.stderr!r}")

# "Is a heavy job alive?" matches exe + argv, never a substring (29 Oct 26: a checker counted its own shell).
# Real sleepers are spawned and looked up by pid, so a render running on this box changes nothing here.
NW = subprocess.CREATE_NO_WINDOW
with tempfile.TemporaryDirectory() as d:
    fake = Path(d) / "render_acts.py"
    fake.write_text("import time; time.sleep(60)\n", encoding="utf-8")
    mention = ("import time; time.sleep(60)  # grep render_acts.py snapshot_queue.py test_detectors hyperframes render", )
    procs = {
        "real": subprocess.Popen([sys.executable, str(fake)], creationflags=NW),
        # a python -c string / node -e string that only MENTIONS the job: the old regex counted these
        "py -c mention": subprocess.Popen([sys.executable, "-c", *mention], creationflags=NW),
        "node -e mention": subprocess.Popen(["node", "-e", "setTimeout(()=>{},60000) // hyperframes render graphics_qc.mjs"], creationflags=NW),
        "cmd mention": subprocess.Popen(["cmd", "/c", f'ping -n 60 127.0.0.1 > nul & rem grep render_acts.py'], creationflags=NW),
    }
    extra = []
    try:
        time.sleep(1.5)
        seen = {pid: kind for pid, kind, _ in render_busy.busy_jobs()}
        check("a real `python <dir>/render_acts.py` sleeper is busy", seen.get(procs["real"].pid) == "render_acts.py", seen)
        for nm in ("test_gates.py", "e2e.py", "run_gates.py", "snapshot_queue.py", "test_detectors.py"):
            f = Path(d) / nm
            f.write_text("import time; time.sleep(60)\n", encoding="utf-8")
            extra.append(subprocess.Popen([sys.executable, str(f)], creationflags=NW))
        time.sleep(1.5)
        seen = {pid: kind for pid, kind, _ in render_busy.busy_jobs()}
        for nm, pr in zip(("test_gates.py", "e2e.py", "run_gates.py", "snapshot_queue.py", "test_detectors.py"), extra):
            check(f"a real `python <dir>/{nm}` sleeper is busy", seen.get(pr.pid) == nm, seen)
        accent = Path(d) / "Jos\u00e9"
        accent.mkdir()
        (accent / "render_acts.py").write_text("import time; time.sleep(60)\n", encoding="utf-8")
        extra.append(subprocess.Popen([sys.executable, str(accent / "render_acts.py")], creationflags=NW))
        time.sleep(1.5)
        seen = {pid: kind for pid, kind, _ in render_busy.busy_jobs()}
        check("a real job whose path has an accent is decoded and found", seen.get(extra[-1].pid) == "render_acts.py", seen)
        for name in ("py -c mention", "node -e mention", "cmd mention"):
            check(f"{name}: a command line that only mentions a job name is idle", procs[name].pid not in seen, seen)
        check("hyperframes render live_renders() ignores a node -e string that mentions it",
              not any(l.split()[0] == str(procs["node -e mention"].pid) for l in REAL_LIVE_RENDERS()))

        # the checker's own parent chain: a render_acts.py that runs the check must not see itself
        probe = Path(d) / "render_acts.py"  # same basename on purpose
        probe.write_text(f"import sys, os; sys.path.insert(0, {str(S)!r}); import render_busy; "
                         "print('SELF', os.getpid() in {p for p, _, _ in render_busy.busy_jobs()})", encoding="utf-8")
        r = subprocess.run([sys.executable, str(probe)], capture_output=True, text=True, creationflags=NW)
        check("a render_acts.py that runs the check does not count itself", "SELF False" in r.stdout, r.stdout + r.stderr)
        table = [{"ProcessId": 10, "ParentProcessId": 1, "Name": "python.exe",
                  "CommandLine": f'python.exe "{fake}" ep-x'},
                 {"ProcessId": 11, "ParentProcessId": 10, "Name": "cmd.exe", "CommandLine": "cmd /c check"},
                 {"ProcessId": 12, "ParentProcessId": 11, "Name": "python.exe", "CommandLine": "python.exe render_busy.py --jobs"},
                 {"ProcessId": 20, "ParentProcessId": 1, "Name": "python.exe", "CommandLine": r'python.exe -u "C:\a b\run_gates.py" ep-y'}]
        got = [(p, k) for p, k, _ in render_busy.busy_jobs(table, self_pid=12)]
        check("the whole parent chain is skipped (render_acts.py ancestor), a sibling job still counts",
              got == [(20, "run_gates.py")], got)
    finally:
        for pr in [*procs.values(), *extra]:
            pr.kill()
    r = subprocess.run([sys.executable, str(S / "render_busy.py"), "--jobs"], capture_output=True, text=True, creationflags=NW)
    check("--jobs CLI: exit 0 idle / 1 busy, last line says which", r.returncode in (0, 1) and
          r.stdout.strip().splitlines()[-1].startswith("[render_busy] " + ("IDLE" if r.returncode == 0 else "BUSY")), r.stdout + r.stderr)

# Table-driven job_kind / live_renders on the two REAL render.cmd command lines (live process table, 29 Oct 26) plus the
# cmd.exe in between. Without these, a job_kind that returns None for every render passes every other test and a heavy job
# launches on top of a live render.
NPX = (r'"C:\Program Files\nodejs\node.exe"  "C:\Program Files\nodejs\node_modules\npm\bin\npx-cli.js" '
       "hyperframes@0.8.211 render . -c _act_tmp.html --gpu --workers 2")
MJS = (r'"node"   "C:\Users\u\AppData\Local\npm-cache\_npx\abc123\node_modules\.bin\..\hyperframes\bin\hyperframes.mjs" '
       "render . -c _act_tmp.html --gpu --workers 2")
CMDHF = r'C:\WINDOWS\system32\cmd.exe /d /s /c hyperframes render . -c _act_tmp.html'
RENDER_TABLE = [
    {"ProcessId": 1, "ParentProcessId": 0, "Name": "explorer.exe", "CommandLine": None},
    {"ProcessId": 35000, "ParentProcessId": 1, "Name": "node.exe", "CommandLine": NPX},
    {"ProcessId": 10181, "ParentProcessId": 35000, "Name": "cmd.exe", "CommandLine": CMDHF},
    {"ProcessId": 10180, "ParentProcessId": 10181, "Name": "node.exe", "CommandLine": MJS},
    {"ProcessId": 90, "ParentProcessId": 1, "Name": "node.exe", "CommandLine": 'node -e "x // hyperframes render"'},
    {"ProcessId": 91, "ParentProcessId": 1, "Name": "python.exe", "CommandLine": 'python.exe C:\\Users\\Jos\u00e9\\render_acts.py ep-x'},
]
for nm, row, want in (("npx-cli.js node", 1, "hyperframes render"), ("hyperframes.mjs node", 3, "hyperframes render"),
                      ("cmd /d /s /c hyperframes render", 2, None), ("node -e mention", 4, None),
                      ("accented path python job", 5, "render_acts.py")):
    r = RENDER_TABLE[row]
    got = render_busy.job_kind(r["Name"], r["CommandLine"])
    check(f"job_kind: {nm} -> {want}", got == want, got)
got = sorted(p for p, _, _ in render_busy.busy_jobs(RENDER_TABLE, self_pid=1, kinds={"hyperframes render"}))
check("busy_jobs(kinds=render) finds exactly the 2 render nodes, not the cmd.exe between them", got == [10180, 35000], got)
_real_table = render_busy.process_table
render_busy.process_table = lambda: RENDER_TABLE
live = [l.split()[0] for l in REAL_LIVE_RENDERS()]
render_busy.process_table = _real_table
check("live_renders() lists both render nodes", sorted(live) == ["10180", "35000"], live)

# A failed process query is "could not look", never IDLE (review of PR 245).
real_ps = render_busy.ps
for nm, ret in (("nonzero exit", (1, "", "Get-CimInstance : access denied")), ("empty output", (0, "", ""))):
    render_busy.ps = lambda cmd, ret=ret: ret
    try:
        render_busy.process_table()
        raised = False
    except RuntimeError:
        raised = True
    check(f"process_table raises on {nm}", raised)
    buf, argv0, code = io.StringIO(), sys.argv, None
    sys.argv = ["render_busy.py", "--jobs"]
    try:
        with contextlib.redirect_stdout(buf):
            render_busy.main()
    except SystemExit as e:
        code = e.code
    sys.argv = argv0
    check(f"--jobs on {nm}: exit 2 and an ERROR line, never IDLE",
          code == 2 and "ERROR" in buf.getvalue() and "IDLE" not in buf.getvalue(), (code, buf.getvalue()))
render_busy.ps = real_ps

# Heavy lock (owner 26 Oct 26): a second heavy job waits for the first, then runs. Temp lock file; the
# HEAVY_LOCK_TOKEN e2e.py holds is dropped, or every job here would pass through as e2e's child.
with tempfile.TemporaryDirectory() as d:
    lock = Path(d) / "heavy.lock"
    os.environ["HEAVY_LOCK_FILE"] = str(lock)
    os.environ.pop("HEAVY_LOCK_TOKEN", None)
    render_busy.POLL_S = 0.2
    def book(job):
        """Book and release the lock for job in this process; return what it printed."""
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            with render_busy.heavy_lock(job):
                pass
        return buf.getvalue()

    py = f"import sys; sys.path.insert(0, {str(S)!r}); import render_busy, time\n"

    holder = subprocess.Popen([sys.executable, "-c", py + "with render_busy.heavy_lock('render ep-test full'):\n time.sleep(2.5)"],
                              stdout=subprocess.DEVNULL, creationflags=NW)
    t0 = time.time()
    while not render_busy.read_lock(lock) and time.time() - t0 < 20:
        time.sleep(0.1)
    rec = render_busy.read_lock(lock)
    check("lock records holder, job, machine, pid and start time",
          rec and rec["job"] == "render ep-test full" and rec["pid"] == holder.pid
          and all(rec.get(k) for k in ("holder", "machine", "start")), rec)
    buf, t0 = io.StringIO(), time.time()
    with contextlib.redirect_stdout(buf):
        with render_busy.heavy_lock("tts ep-test"):
            waited, holder_done = time.time() - t0, holder.poll() is not None
            mine = render_busy.read_lock(lock)
    out = buf.getvalue()
    check("second heavy job waits while the first holds the lock, then runs",
          holder_done and waited > 1.0 and mine["job"] == "tts ep-test", f"waited={waited:.1f}s done={holder_done} out={out!r}")
    check("the waiting job prints who holds the lock",
          "WAITING to start tts ep-test" in out and "render ep-test full" in out and f"pid {holder.pid}" in out, out)
    check("lock released when the block ends", not lock.exists())

    dead = subprocess.Popen([sys.executable, "-c", "pass"], creationflags=NW)
    dead.wait()
    for name, fake in (("dead pid", {"pid": dead.pid, "created": 1}),
                       ("pid reused by a newer process", {"pid": os.getpid(), "created": 1})):
        lock.write_text(json.dumps({**fake, "job": "render old", "holder": "x", "machine": "x", "start": "x", "token": "t"}))
        t0 = time.time()
        out = book("e2e")
        check(f"a dead holder's lock is taken over at once ({name})",
              time.time() - t0 < 1 and "took over a dead holder's lock: render old" in out, out)

    with render_busy.heavy_lock("tts ep-test"):
        r = subprocess.run([sys.executable, "-c", py + "with render_busy.heavy_lock('tts_clone'):\n print('INNER RAN')"],
                           capture_output=True, text=True, timeout=30, creationflags=NW)
    check("a child of the holder (tts_episode -> tts_clone) passes through the lock", "INNER RAN" in r.stdout, r.stdout + r.stderr)

    bat = Path(d) / "hold.cmd"
    bat.write_text(f'@echo off\n"{sys.executable}" "{S / "render_busy.py"}" --hold "render ep-test draft"\n'
                   f'"{sys.executable}" -c "import json; print(json.load(open(r\'{lock}\'))[\'pid\'])"\n', encoding="utf-8")
    p = subprocess.Popen(["cmd", "/c", str(bat)], stdout=subprocess.PIPE, text=True, creationflags=NW)
    out = p.communicate(timeout=60)[0]
    check("--hold books the lock for the calling cmd.exe (render.cmd)", out.strip().splitlines()[-1:] == [str(p.pid)], out)
    out = book("e2e")
    check("render.cmd's lock is free once its cmd.exe exits", "took over a dead holder's lock: render ep-test draft" in out, out)

    # A wrapper calling render.cmd twice (draft, then full) in one cmd.exe: the second --hold must pass, and
    # --release must free the lock while that cmd.exe lives on (review blocker: it waited forever on itself).
    busy = f'"{sys.executable}" "{S / "render_busy.py"}"'
    bat.write_text(f'@echo off\n{busy} --hold "render ep-test draft"\n{busy} --hold "render ep-test full"\n'
                   f'echo HELD TWICE\n{busy} --release\n'
                   f'if exist "{lock}" (echo STILL LOCKED) else (echo RELEASED)\n', encoding="utf-8")
    try:
        out = subprocess.run(["cmd", "/c", str(bat)], capture_output=True, text=True, timeout=30, creationflags=NW).stdout
    except subprocess.TimeoutExpired:
        out = "timed out: the second --hold waited on its own cmd.exe"
    check("one cmd.exe books the lock twice, then --release frees it before it exits",
          "HELD TWICE" in out and "RELEASED" in out, out)
    os.environ.pop("HEAVY_LOCK_FILE")

if FAILS:
    print(f"\n{len(FAILS)} FAILED")
    sys.exit(1)
print("\nall passed")
