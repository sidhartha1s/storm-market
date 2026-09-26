#!/usr/bin/env python3
"""Run every pre-render gate in the CLAUDE.md order, stop on first failure.

CLAUDE.md "HARD RULE: the render is the LAST step" names nine gates that must all be green
BEFORE any render starts. Each gate already fails loud on its own (sweep_episode.py,
lint_timeline.py, beat_density.py, audio_levels.py, media_budget.py, blank_scan.mjs and the
rest), but nothing chained them — a FAIL sitting in scrollback reads as success to anything
that only checks the LAST exit code (a wrapper, a subagent, `&&`). This runs the whole suite in
order, stops at the first non-zero exit, and names the gate that failed instead of letting a
later PASS bury it.

Usage: python3 scripts/run_gates.py episodes/<slug>
Exit 0 = every gate passed, safe to render. Exit 1 = a gate failed (its name is printed).
"""
import subprocess
import sys
from pathlib import Path

if len(sys.argv) != 2:
    sys.exit("usage: python3 scripts/run_gates.py episodes/<slug>")

ep = Path(sys.argv[1])
if not ep.is_dir():
    sys.exit(f"not a directory: {ep}")
ep_abs = str(ep.resolve())
scripts = Path(__file__).resolve().parent

# order per CLAUDE.md "the render is the LAST step" code block
GATES = [
    ("sweep_episode.py",    [sys.executable, str(scripts / "sweep_episode.py"), str(ep)], None),
    ("lint_timeline.py",    [sys.executable, str(scripts / "lint_timeline.py"), str(ep)], None),
    ("narration_picture_check.py", [sys.executable, str(scripts / "narration_picture_check.py"), str(ep)], None),
    ("flag_words.py",       [sys.executable, str(scripts / "flag_words.py"), str(ep)], None),
    ("beat_density.py",     [sys.executable, str(scripts / "beat_density.py"), str(ep)], None),
    ("media_budget.py",     [sys.executable, str(scripts / "media_budget.py"), str(ep)], None),
    ("audio_levels.py",     [sys.executable, str(scripts / "audio_levels.py"), str(ep)], None),
    ("blank_scan.mjs",      ["node", str(scripts / "blank_scan.mjs"), ep_abs], None),
    ("overlap_check.mjs",   ["node", str(scripts / "overlap_check.mjs"), ep_abs], None),
    ("occlusion_check.mjs", ["node", str(scripts / "occlusion_check.mjs"), ep_abs], None),
    ("graphics_qc.mjs",     ["node", str(scripts / "graphics_qc.mjs"), "."], ep.resolve()),
]

for name, cmd, cwd in GATES:
    print(f"=== {name} ===")
    r = subprocess.run(cmd, cwd=cwd)
    if r.returncode != 0:
        print(f"\nRUN_GATES FAIL - {name} exited {r.returncode}. Fix it, do not render.")
        sys.exit(1)
    print()

print("RUN_GATES PASS - all gates green, safe to render.")
sys.exit(0)
