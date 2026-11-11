#!/usr/bin/env python3
"""Run every pre-render gate in order, stop on first failure.

GATES below is the one list of pre-render gates and their order (CLAUDE.md "HARD RULE: the render is
the LAST step" points here); all must be green BEFORE any render starts. Each gate already fails loud on its own (sweep_episode.py,
lint_timeline.py, beat_density.py, audio_levels.py, media_budget.py, blank_scan.mjs and the
rest), but nothing chained them — a FAIL sitting in scrollback reads as success to anything
that only checks the LAST exit code (a wrapper, a subagent, `&&`). This runs the whole suite in
order, stops at the first non-zero exit, and names the gate that failed instead of letting a
later PASS bury it.

Usage: python3 scripts/run_gates.py episodes/<slug> [--all]
Exit 0 = every gate passed, safe to render. Exit 1 = a gate failed (its name is printed).
--all runs every gate even after a failure and ends with one list of every failed gate (exit 1 if any):
one fix cycle for a many-gate episode instead of one per gate. e2e.py runs without it.
"""
import subprocess
import sys
from pathlib import Path

run_all = "--all" in sys.argv[1:]
args = [a for a in sys.argv[1:] if a != "--all"]
if len(args) != 1:
    sys.exit("usage: python3 scripts/run_gates.py episodes/<slug> [--all]")

ep = Path(args[0])
if not ep.is_dir():
    sys.exit(f"not a directory: {ep}")
ep_abs = str(ep.resolve())
scripts = Path(__file__).resolve().parent

# the gate list and its order: this list is the only copy
GATES = [
    ("layer parity",        [sys.executable, str(scripts / "render_preflight.py"), str(ep), "--layers"], None),
    ("paul_start_frame.py", [sys.executable, str(scripts / "paul_start_frame.py"), str(ep)], None),
    ("sweep_episode.py",    [sys.executable, str(scripts / "sweep_episode.py"), str(ep)], None),
    ("lint_timeline.py",    [sys.executable, str(scripts / "lint_timeline.py"), str(ep)], None),
    ("build_srt.py --check", [sys.executable, str(scripts / "build_srt.py"), str(ep), "--check"], None),
    ("narration_picture_check.py", [sys.executable, str(scripts / "narration_picture_check.py"), str(ep)], None),
    ("flag_words.py",       [sys.executable, str(scripts / "flag_words.py"), str(ep)], None),
    ("hook_shape.py",       [sys.executable, str(scripts / "hook_shape.py"), str(ep)], None),
    ("homograph_scan.py",   [sys.executable, str(scripts / "homograph_scan.py"), str(ep)], None),
    ("beat_density.py",     [sys.executable, str(scripts / "beat_density.py"), str(ep)], None),
    ("media_budget.py",     [sys.executable, str(scripts / "media_budget.py"), str(ep)], None),
    ("audio_levels.py",     [sys.executable, str(scripts / "audio_levels.py"), str(ep)], None),
    ("blank_scan.mjs",      ["node", str(scripts / "blank_scan.mjs"), ep_abs], None),
    ("overlap_check.mjs",   ["node", str(scripts / "overlap_check.mjs"), ep_abs], None),
    ("occlusion_check.mjs", ["node", str(scripts / "occlusion_check.mjs"), ep_abs], None),
    ("graphics_qc.mjs",     ["node", str(scripts / "graphics_qc.mjs"), "."], ep.resolve()),
]
if ep.resolve().name.startswith("sh-"):  # a 9:16 short: the runtime text lint for its frame and the Shorts UI safe zone
    GATES.append(("shorts_lint.mjs", ["node", str(scripts / "shorts_lint.mjs"), ep_abs], None))

failed = []
for name, cmd, cwd in GATES:
    print(f"\n=== {name} ===", flush=True)  # header before the gate's own output (e2e.gate_results reads it)
    r = subprocess.run(cmd, cwd=cwd)
    if r.returncode != 0:
        if not run_all:
            print(f"\nRUN_GATES FAIL - {name} exited {r.returncode}. Fix it, do not render.")
            sys.exit(1)
        failed.append(f"{name} exited {r.returncode}")
    print()

if failed:
    print(f"RUN_GATES FAIL - {len(failed)} of {len(GATES)} gates failed. Fix them all, do not render:")
    for f in failed:
        print(f"  - {f}")
    sys.exit(1)

print("RUN_GATES PASS - all gates green, safe to render.")
sys.exit(0)
