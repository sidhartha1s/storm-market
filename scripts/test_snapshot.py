"""Self-check for snapshot.py: python3 scripts/test_snapshot.py (no browser, no npx: the gate and the launch are stubbed)."""
import subprocess
import sys
from pathlib import Path

S = Path(__file__).resolve().parent
sys.path.insert(0, str(S))
import snapshot  # noqa: E402

FAILS = []


def check(name, cond, detail=""):
    print(("ok   " if cond else "FAIL ") + name + (f"  {detail}" if detail and not cond else ""))
    if not cond:
        FAILS.append(name)


class Fake:
    def __init__(self, code):
        self.returncode = code


calls = []


def fake_run(gate_code):
    def run(cmd, **kw):
        calls.append(cmd)
        return Fake(gate_code if "render_busy.py" in str(cmd[-1]) else 0)
    return run


check("argv carries the pin, --no-end and --describe false",
      snapshot.argv("0.8.185", ["episodes/ep-x", "--at", "1,2", "-o", "d"])
      == ["npx", "hyperframes@0.8.185", "snapshot", "episodes/ep-x", "--at", "1,2", "-o", "d", "--no-end", "--describe", "false"])

snapshot.subprocess.run = fake_run(3)
calls.clear()
check("render_busy exit 3 (thin RAM or live render) stops it with exit 3", snapshot.main(["episodes/ep-x", "--at", "1"]) == 3)
check("no npx launched after a refusal", len(calls) == 1 and "render_busy.py" in str(calls[0][-1]), str(calls))

snapshot.subprocess.run = fake_run(0)
calls.clear()
check("gate clear: npx snapshot launched with the config pin", snapshot.main(["episodes/ep-x", "--at", "1"]) == 0
      and len(calls) == 2 and calls[1][1] == f"hyperframes@{snapshot.parse_pin(S.parent)}", str(calls))
snapshot.subprocess.run = subprocess.run

if FAILS:
    sys.exit(f"[test_snapshot] FAIL: {FAILS}")
print("[test_snapshot] all checks passed")
