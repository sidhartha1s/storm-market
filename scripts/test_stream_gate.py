"""Self-check for stream_gate.py: python3 scripts/test_stream_gate.py

Camille's full render (25 Oct 26, learnings/render.md on claude/ep-mayfield-2021-a6d084): RENDER_WORKERS=2,
71.5 GB free, gate `enabled:false, reason: multi_worker`, 75.0 GB of disk capture asked. Its failed log was overwritten
by the 1-worker rerun, so the failing gate line is that rerun's real line (fixtures/stream_gate/camille-full-1worker.txt)
with the logged 2-worker values put back. Moore's real 2-worker line (parallel_forced) must pass.
"""
import sys
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
import stream_gate  # noqa: E402

FIX = S / "fixtures" / "stream_gate"
camille_ok = (FIX / "camille-full-1worker.txt").read_text(encoding="utf-8")
camille_bad = (camille_ok.replace('"enabled":true', '"enabled":false').replace('"single_worker"', '"multi_worker"')
               .replace('"workerCount":1', '"workerCount":2'))
moore = (FIX / "moore-full-2workers.txt").read_text(encoding="utf-8")
render_cmd = (S / "render.cmd").read_text(encoding="utf-8")
FAILS = []


def check(name, ok):
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


check("Camille launch (full, 2 workers, 71.5 GB free) is refused", stream_gate.launch_refusal("full", 2, 71.5) is not None)
check("full at 1 worker on the same disk launches", stream_gate.launch_refusal("full", 1, 71.5) is None)
check("a draft at 3 workers launches", stream_gate.launch_refusal("draft", 3, 71.5) is None)
check("Camille's multi_worker gate line stops the render", "multi_worker" in stream_gate.log_verdict(camille_bad, 60))
check("Camille's 1-worker rerun line passes", stream_gate.log_verdict(camille_ok, 60) == "ok")
check("Moore's 2-worker parallel_forced line passes", stream_gate.log_verdict(moore, 60) == "ok")
check("no gate line yet is pending", stream_gate.log_verdict("Checking browser", 60) == "pending")
check("no gate line after the watch window stops the render", stream_gate.log_verdict("Checking browser", 600) != "pending")
launch, watch, npx = (render_cmd.find('stream_gate.py" launch'), render_cmd.find('stream_gate.py" watch'),
                      render_cmd.find("call npx hyperframes"))
check("render.cmd runs launch, then watch, after the worker count is final and before npx",
      render_cmd.find("render_%MODE%.workers\" set /p") < launch < watch < npx)

if FAILS:
    sys.exit(f"{len(FAILS)} check(s) failed")
print("all stream-gate checks passed")
