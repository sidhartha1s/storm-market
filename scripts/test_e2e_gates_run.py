"""Self-check: e2e.py fails when any run_gates gate failed or never ran.

Skeptic finding 27 (owner verdict "do", 26 Oct 26): run_gates stops at the first FAIL and e2e.py accepted
that as a legitimate result, so on real episodes 8 of 9 gates never ran and e2e still printed PASS. Fails on
the old e2e.py: gate_results did not exist and an early stop only printed "not exercised".

python3 scripts/test_e2e_gates_run.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from e2e import FIXTURE, GATE_NAMES, gate_results  # noqa: E402

FAILS = []


def check(label, cond):
    print(("PASS " if cond else "FAIL ") + label)
    if not cond:
        FAILS.append(label)


all_ran = "".join(f"=== {g} ===\n\n" for g in GATE_NAMES) + "RUN_GATES PASS - all gates green, safe to render.\n"
stopped = (f"=== {GATE_NAMES[0]} ===\n\n=== {GATE_NAMES[1]} ===\n"
           f"\nRUN_GATES FAIL - {GATE_NAMES[1]} exited 1. Fix it, do not render.\n")

check("run_gates lists at least the 15 gates of 26 Oct 26", len(GATE_NAMES) >= 15)
check("a full run reads as every gate PASS", set(gate_results(all_ran).values()) == {"PASS"})
r = gate_results(stopped)
check("the gate that failed reads FAIL", r[GATE_NAMES[1]] == "FAIL")
check("the gate before it reads PASS", r[GATE_NAMES[0]] == "PASS")
check("every gate after the stop reads NOT RUN", all(r[g] == "NOT RUN" for g in GATE_NAMES[2:]))
check("the pinned fixture exists with its composition", (FIXTURE / "index.html").is_file())

if FAILS:
    sys.exit(f"{len(FAILS)} check(s) failed")
print("all e2e gate-run checks passed")
