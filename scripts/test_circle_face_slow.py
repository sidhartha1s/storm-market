"""circle_face.slow_line: a face pass that slows to 10x (the 26 Oct 26 ZBook pass, 24 s per second of face when the
card spilled into shared memory) prints one loud [SLOW] line with the rate and the card's processes, at most once per
50 chunks, and never stops the pass. Run: python3 scripts/test_circle_face_slow.py

circle_face.py imports torch and the FlashHead model at load, which only its own venv has, so the test lifts the
limit and slow_line out of its source and runs them alone."""
import ast
import sys
from pathlib import Path

src = (Path(__file__).parent / "circle_face.py").read_text(encoding="utf-8")
keep = [n for n in ast.parse(src).body
        if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "MAX_S_PER_FACE_S"
        or isinstance(n, ast.FunctionDef) and n.name == "slow_line"]
ns = {"card_holders": lambda: "unused"}
exec(compile(ast.Module(body=keep, type_ignores=[]), "circle_face.py", "exec"), ns)
slow_line = ns["slow_line"]

holders = lambda: "1234, python.exe"  # noqa: E731
fails = []
lines = {}
alarmed_at = None
for i in range(200):  # every chunk at 24 s per second of face
    line = slow_line(i, 24.0, alarmed_at, holders)
    if line:
        lines[i] = line
        alarmed_at = i
if sorted(lines) != [10, 60, 110, 160]:
    fails.append(f"alarm chunks {sorted(lines)}, want [10, 60, 110, 160] (from chunk 10, once per 50)")
first = lines.get(10, "")
if not (first.startswith("[SLOW] 24.0 s per second") and "1234, python.exe" in first):
    fails.append(f"alarm line lacks the rate or the card holders: {first!r}")
if any(slow_line(i, 2.3, None, holders) for i in range(200)):
    fails.append("a normal 2.3 s rate alarmed")
if slow_line(5, 24.0, None, holders):
    fails.append("alarmed before chunk 10 (start-up noise)")
loop = src.split("for i, chunk in enumerate(chunks):")[1].split("# no -shortest")[0]
if any(w in loop for w in ("sys.exit", "break", "return", "raise")):
    fails.append("the chunk loop can stop on a slow rate")
if "alarmed_at = i" not in loop:
    fails.append("the chunk loop never records the alarm, so it would alarm every chunk")

for f in fails:
    print("FAIL", f)
print("test_circle_face_slow:", "FAIL" if fails else "PASS (10x slow pass alarms 4 times in 200 chunks, keeps running)")
sys.exit(1 if fails else 0)
