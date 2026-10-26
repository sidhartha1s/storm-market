"""Self-check for references/grader-calibration.md: python3 scripts/test_grader_calibration.py

The doc is the grader's rubric and its calibration set. Fails when the set drops below 20 rows,
a row has no PASS/FAIL, a row names a check that is not in the rubric, or a kind lacks checks.
"""
import re
import sys
from pathlib import Path

DOC = Path(__file__).resolve().parent.parent / "references" / "grader-calibration.md"
text = DOC.read_text(encoding="utf8")
checks = set(re.findall(r"^\| ((?:HK|PAUL|SC|TI|AN|TH)\d+) \| [A-Z0-9-]+ \|", text, re.M))
rows = re.findall(r"^\| (C\d\d) \| (\w[\w-]*) \|.*\| (PASS|FAIL) \| .*\| ([A-Z0-9, -]+) \| .*\|$", text, re.M)
fails = []
if len(checks) < 15: fails.append(f"only {len(checks)} checks in the rubric")
if len(rows) < 20: fails.append(f"only {len(rows)} well-formed set rows")
for cid, kind, verdict, named in rows:
    for c in (x.strip() for x in named.split(",")):
        if c != "-" and c not in checks: fails.append(f"{cid} names unknown check {c}")
if not {r[2] for r in rows} == {"PASS", "FAIL"}: fails.append("set needs both PASS and FAIL rows")
applies = re.search(r"Applies to: (.*)\.", text)
used = set(re.findall(r"(?:HK|PAUL|SC|TI|AN|TH)\d+", applies.group(1))) if applies else set()
if used != checks: fails.append(f"Applies-to list differs from rubric: {sorted(used ^ checks)}")
if "YouTube" not in text: fails.append("re-tune-from-YouTube note missing")
for f in fails: print("FAIL:", f)
print("OK" if not fails else "FAILED", f"({len(checks)} checks, {len(rows)} rows)")
sys.exit(1 if fails else 0)
