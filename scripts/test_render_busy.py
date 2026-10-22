"""Self-check for render_busy --launch picking the worker count that fits free RAM:
python3 scripts/test_render_busy.py

Free RAM is injected (render_busy.free_gb replaced); no render, no registry write (the GPU pin is
stubbed), no process scan (live_renders stubbed). The 3.3 GB case is the 18 Oct 26 Joplin launch
that sat refused for 34 minutes, then stalled on 2 workers."""
import contextlib
import io
import os
import subprocess
import sys
import tempfile
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


def run_main(free, *argv):
    """Run main() with this much free RAM and these args; return (exit code, stdout)."""
    render_busy.free_gb = lambda: free
    os.environ.pop("RENDER_BUSY_OK", None)
    sys.argv = ["render_busy.py", *argv]
    buf, code = io.StringIO(), 0
    with contextlib.redirect_stdout(buf):
        try:
            render_busy.main()
        except SystemExit as e:
            code = e.code
    return code, buf.getvalue()


def launch(free, requested):
    """Run main() --launch as render.cmd does; return (exit code, stdout, workers file text or None)."""
    os.environ["RENDER_WORKERS"] = str(requested)
    with tempfile.TemporaryDirectory() as d:
        out_file = Path(d) / "render_draft.workers"
        code, out = run_main(free, "--launch", str(out_file))
        return code, out, out_file.read_text() if out_file.exists() else None


def plain(free):
    """Run main() as a gate does (no --launch): return (exit code, stdout)."""
    return run_main(free)


code, out = plain(0.5)
check("gate at 0.5 GB free (the 22 Oct stall) -> exit 3", code == 3, f"code={code} out={out!r}")
check("gate refusal states the GB numbers", "0.5 GB free" in out and "1.5 GB" in out, out)
code, out = plain(3.0)
check("gate at 3.0 GB free -> OK", code == 0 and "OK" in out, f"code={code} out={out!r}")

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

if FAILS:
    print(f"\n{len(FAILS)} FAILED")
    sys.exit(1)
print("\nall passed")
