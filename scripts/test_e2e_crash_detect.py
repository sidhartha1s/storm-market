"""Self-check for e2e.py's Node-crash detector (Opus review: run_gates exit 1 from an
uncaught Node exception in blank_scan/overlap_check/occlusion_check/graphics_qc read as a
legitimate gate FAIL, so e2e.py reported PASS over a crashed tool).

Feeds real gate FAIL text (should NOT be flagged as a crash) and a fake Node uncaught-exception
dump (SHOULD be flagged) through is_tool_crash(). Fails on the old e2e.py: is_tool_crash did not
exist there (any FAIL text was accepted as a legitimate gate result, no crash detector at all).

python3 scripts/test_e2e_crash_detect.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from e2e import is_tool_crash  # noqa: E402

FAILS = []


def check(label, cond):
    if cond:
        print(f"PASS {label}")
    else:
        FAILS.append(label)
        print(f"FAIL {label}")


# real gate FAIL output (grepped from blank_scan.mjs, overlap_check.mjs, occlusion_check.mjs,
# graphics_qc.mjs's own FAIL prints) — a legitimate gate FAIL, never a crash.
GATE_FAIL_OUTPUT = """=== blank_scan.mjs ===
intro               dur     12s  samples 48

BLANK SCAN FAIL - 1 finding(s)
    intro - blank for 1.20s at 4.30s
"""

# a real uncaught Node exception, as blank_scan.mjs etc. would print if a bug in the tool
# itself threw mid-run (stack trace, error type, node:internal frame, exit 1 same as a FAIL).
NODE_CRASH_OUTPUT = """=== blank_scan.mjs ===
file:///C:/storm-market/scripts/blank_scan.mjs:42
  const dur = comp.duration.toFixed(1);
                            ^

TypeError: Cannot read properties of undefined (reading 'toFixed')
    at Object.<anonymous> (file:///C:/storm-market/scripts/blank_scan.mjs:42:35)
    at Module._compile (node:internal/modules/cjs/loader:1254:14)

Node.js v22.14.0
"""

check("real gate FAIL text is not flagged as a crash", not is_tool_crash(GATE_FAIL_OUTPUT))
check("uncaught Node exception IS flagged as a crash", is_tool_crash(NODE_CRASH_OUTPUT))
check("a Python traceback is flagged as a crash",
      is_tool_crash("Traceback (most recent call last):\n  File x\nValueError: boom"))

if FAILS:
    print(f"\n{len(FAILS)} check(s) failed: {FAILS}")
    sys.exit(1)
print("\nall checks passed")
