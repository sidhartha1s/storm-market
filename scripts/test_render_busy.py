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


render_busy.live_renders = lambda: []
render_busy.pin_chrome_to_dedicated_gpu = lambda: None


def launch(free, requested):
    """Run main() --launch as render.cmd does; return (exit code, stdout, workers file text or None)."""
    render_busy.free_gb = lambda: free
    os.environ["RENDER_WORKERS"] = str(requested)
    os.environ.pop("RENDER_BUSY_OK", None)
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

render_busy.MIN_FREE_GB = 1.5  # what RENDER_MIN_FREE_GB=1.5 sets (scripts/nepal_full_task.cmd)
code, out, n = launch(2.0, 1)
check("RENDER_MIN_FREE_GB=1.5 override: 2.0 GB free, request 1 -> 1 worker", (code, n) == (0, "1"), f"code={code} n={n} out={out!r}")
render_busy.MIN_FREE_GB = 4.5
code, out, n = launch(4.0, 2)
check("RENDER_MIN_FREE_GB=4.5 override is the floor for any launch: 4.0 GB, request 2 -> exit 3",
      (code, n) == (3, None), f"code={code} n={n} out={out!r}")
render_busy.MIN_FREE_GB = render_busy.need_gb(1)

# render.cmd plumbing: run its own lines from the RENDER_WORKERS default through `set /p`, with
# render_busy.py swapped for a stub that runs the real main() at 3.3 GB free, and echo what npx would get.
render_cmd = (S / "render.cmd").read_text(encoding="utf-8").splitlines()
start = next(i for i, l in enumerate(render_cmd) if l.startswith("if not defined RENDER_WORKERS"))
end = next(i for i, l in enumerate(render_cmd) if "set /p RENDER_WORKERS" in l)
with tempfile.TemporaryDirectory() as d:
    stub = Path(d) / "busy_stub.py"
    stub.write_text(f"import sys\nsys.path.insert(0, {str(S)!r})\nimport render_busy\n"
                    "render_busy.free_gb = lambda: 3.3\nrender_busy.live_renders = lambda: []\n"
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

# Heavy lock (owner 26 Oct 26): a second heavy job waits for the first, then runs. Temp lock file; the
# HEAVY_LOCK_TOKEN e2e.py holds is dropped, or every job here would pass through as e2e's child.
NW = subprocess.CREATE_NO_WINDOW
with tempfile.TemporaryDirectory() as d:
    lock = Path(d) / "heavy.lock"
    os.environ["HEAVY_LOCK_FILE"] = str(lock)
    os.environ.pop("HEAVY_LOCK_TOKEN", None)
    render_busy.POLL_S = 0.2
    py = f"import sys; sys.path.insert(0, {str(S)!r}); import render_busy, time\n"

    holder = subprocess.Popen([sys.executable, "-c", py + "with render_busy.heavy_lock('render ep-test full'):\n time.sleep(4)"],
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
          holder_done and waited > 1.5 and mine["job"] == "tts ep-test", f"waited={waited:.1f}s done={holder_done} out={out!r}")
    check("the waiting job prints who holds the lock",
          "WAITING to start tts ep-test" in out and "render ep-test full" in out and f"pid {holder.pid}" in out, out)
    check("lock released when the block ends", not lock.exists())

    dead = subprocess.Popen([sys.executable, "-c", "pass"], creationflags=NW)
    dead.wait()
    for name, fake in (("dead pid", {"pid": dead.pid, "created": 1}),
                       ("pid reused by a newer process", {"pid": os.getpid(), "created": 1})):
        lock.write_text(json.dumps({**fake, "job": "render old", "holder": "x", "machine": "x", "start": "x", "token": "t"}))
        buf, t0 = io.StringIO(), time.time()
        with contextlib.redirect_stdout(buf):
            with render_busy.heavy_lock("e2e"):
                pass
        check(f"a dead holder's lock is taken over at once ({name})",
              time.time() - t0 < 1 and "took over a dead holder's lock: render old" in buf.getvalue(), buf.getvalue())

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
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        with render_busy.heavy_lock("e2e"):
            pass
    check("render.cmd's lock is free once its cmd.exe exits", "took over a dead holder's lock: render ep-test draft" in buf.getvalue(),
          buf.getvalue())
    os.environ.pop("HEAVY_LOCK_FILE")

if FAILS:
    print(f"\n{len(FAILS)} FAILED")
    sys.exit(1)
print("\nall passed")
