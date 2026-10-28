"""Self-check for references/grader-calibration.md: python3 scripts/test_grader_calibration.py

The doc is the grader's rubric and its calibration set. problems() fails on: a set under 20 rows,
a set row that does not parse (bad verdict, bad check id) or differs from the heading's N, a row
naming a check not in the rubric, no PASS/FAIL mix, an Applies-to list that differs from the
rubric, a missing re-tune note. The seeded bad copies below prove each failure fires.
"""
import re
import sys
from pathlib import Path

DOC = Path(__file__).resolve().parent.parent / "references" / "grader-calibration.md"
CID = r"(?:HK|PAUL|SC|TI|AN|TH)\d+"


def problems(text):
    out = []
    checks = set(re.findall(rf"^\| ({CID}) \| [A-Z0-9-]+ \|", text, re.M))
    lines = re.findall(r"^\| C\d\d \|.*$", text, re.M)
    rows = re.findall(rf"^\| (C\d\d) \| [\w-]+ \|.*\| (PASS|FAIL) \| .*\| ((?:{CID}|-)(?:, {CID})*) \| [^|]*\|\s*$", text, re.M)
    n = re.search(r"Calibration set \((\d+) verdicts\)", text)
    if len(checks) < 15: out.append(f"only {len(checks)} checks")
    if len(rows) < 20: out.append(f"only {len(rows)} well-formed rows")
    if len(lines) != len(rows): out.append(f"{len(lines) - len(rows)} malformed set rows")
    if not n or int(n.group(1)) != len(lines): out.append("heading count differs from rows")
    for cid, _v, named in rows:
        out += [f"{cid} names unknown check {c}" for c in named.split(", ") if c != "-" and c not in checks]
    if {r[1] for r in rows} != {"PASS", "FAIL"}: out.append("set needs both PASS and FAIL rows")
    ap = re.search(r"Applies to: (.*)\.", text)
    used = set(re.findall(CID, ap.group(1))) if ap else set()
    if used != checks: out.append(f"Applies-to differs from rubric: {sorted(used ^ checks)}")
    if "YouTube" not in text: out.append("re-tune-from-YouTube note missing")
    return out


text = DOC.read_text(encoding="utf8")
bad = {
    "bad verdict": text.replace("| FAIL |", "| FAILED |", 1),
    "lowercase check": text.replace("| HK7 | memory", "| hk7 | memory", 1),
    "rows deleted": re.sub(r"^\| C2[1-4] \|.*\n", "", text, flags=re.M),
    "unknown check": text.replace("| HK7 | memory", "| HK77 | memory", 1),
    "rubric row deleted": re.sub(r"^\| HK5 \|.*\n", "", text, flags=re.M),
    "no retune note": text.replace("YouTube", "web"),
}
fails = [f"real doc: {p}" for p in problems(text)]
fails += [f"seeded '{k}' not caught" for k, v in bad.items() if v != text and not problems(v)]
fails += [f"seed '{k}' did not change the doc" for k, v in bad.items() if v == text]
for f in fails: print("FAIL:", f)
print("FAILED" if fails else "OK")
sys.exit(1 if fails else 0)
