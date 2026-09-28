"""Self-check for scripts/homograph_scan.py: python3 scripts/test_homograph_scan.py

Runs against the SHIPPED references/homographs.md, not a private fixture wordlist -- this
locks in the real "lives" row (the exact defect this gate exists to catch, LEARNINGS.md
2026-09-28), not just a parser detail that could stay green while the shipped table went
blank or dropped the row.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

S = Path(__file__).resolve().parent
FAILS = []


def check(label, cond, detail=""):
    if cond:
        print(f"PASS {label}")
    else:
        FAILS.append(label)
        print(f"FAIL {label} {detail}")


def run_gate(ep_dir):
    r = subprocess.run([sys.executable, str(S / "homograph_scan.py"), str(ep_dir)],
                        capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


with tempfile.TemporaryDirectory() as d:
    root = Path(d)

    # 1. the required regression: "lives" in "they lost their lives" must be flagged, with the
    #    sentence it sits in and both senses.
    ep = root / "ep-lives"
    ep.mkdir()
    (ep / "edit_script.md").write_text(
        "### A1-S1 — narration\n> Seven tornadoes touched down that day. They lost their lives "
        "before the sirens ever sounded.\n", encoding="utf-8")
    rc, out = run_gate(ep)
    check("lives: exit 0 (WARN, never blocks a render on its own)", rc == 0, f"rc={rc}")
    check('lives: flags "lives" against the sentence it appears in',
          '"lives" in: They lost their lives before the sirens ever sounded.' in out, out)
    check("lives: prints both senses", "sense A:" in out and "sense B:" in out, out)
    check("lives: WARN summary names the count and measurement-not-guess rule",
          "HOMOGRAPH_SCAN WARN - 1 homograph occurrence" in out
          and "measurement, never by guess" in out, out)

    # 2. a sentence with no homograph passes clean, 0 occurrences (sanity check the gate isn't
    #    flagging everything).
    ep_clean = root / "ep-clean"
    ep_clean.mkdir()
    (ep_clean / "edit_script.md").write_text(
        "### A1-S1 — narration\n> The storm moved north overnight.\n", encoding="utf-8")
    rc2, out2 = run_gate(ep_clean)
    check("clean sentence: exit 0", rc2 == 0, f"rc={rc2}")
    check("clean sentence: PASS with 0 occurrences",
          "HOMOGRAPH_SCAN PASS - 0 homograph occurrences." in out2, out2)

print()
if FAILS:
    print(f"test_homograph_scan: {len(FAILS)} FAILED: {FAILS}")
    sys.exit(1)
print("test_homograph_scan: all PASS")
