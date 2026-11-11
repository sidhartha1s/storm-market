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

All green writes the stamp render_preflight.py checks before any render: timeline.digest() of the timeline checked,
in <episode>/gates_passed.marker (gitignored). A failing gate deletes it; a timeline edited mid-run gets none.
Beside a render (it holds the heavy lock: render_busy.render_holder()) only the "file" gates run, each only while
free memory is at or above config.yaml render.gates_beside_render_min_free_gb; the "browser" gates are listed as
waiting for the render. Exit 3 = no verdict because a render is running; no stamp.
"""
import subprocess
import sys
from pathlib import Path

import yaml

import render_busy
import timeline

run_all = "--all" in sys.argv[1:]
args = [a for a in sys.argv[1:] if a != "--all"]
if len(args) != 1:
    sys.exit("usage: python3 scripts/run_gates.py episodes/<slug> [--all]")

ep = Path(args[0])
if not ep.is_dir():
    sys.exit(f"not a directory: {ep}")
ep_abs = str(ep.resolve())
scripts = Path(__file__).resolve().parent

# the gate list and its order: this list is the only copy. kind, read from each gate's source (11 Nov 26):
# "file" = Python, ffmpeg, ffprobe or git on files; "browser" = opens a headless Chromium (playwright_env.mjs)
GATES = [
    ("layer parity",        [sys.executable, str(scripts / "render_preflight.py"), str(ep), "--layers"], None, "file"),
    ("paul_start_frame.py", [sys.executable, str(scripts / "paul_start_frame.py"), str(ep)], None, "file"),
    ("sweep_episode.py",    [sys.executable, str(scripts / "sweep_episode.py"), str(ep)], None, "file"),
    ("lint_timeline.py",    [sys.executable, str(scripts / "lint_timeline.py"), str(ep)], None, "file"),
    ("build_srt.py --check", [sys.executable, str(scripts / "build_srt.py"), str(ep), "--check"], None, "file"),
    ("narration_picture_check.py", [sys.executable, str(scripts / "narration_picture_check.py"), str(ep)], None, "file"),
    ("flag_words.py",       [sys.executable, str(scripts / "flag_words.py"), str(ep)], None, "file"),
    ("hook_shape.py",       [sys.executable, str(scripts / "hook_shape.py"), str(ep)], None, "file"),
    ("homograph_scan.py",   [sys.executable, str(scripts / "homograph_scan.py"), str(ep)], None, "file"),
    ("beat_density.py",     [sys.executable, str(scripts / "beat_density.py"), str(ep)], None, "browser"),  # via beat_probe.mjs
    ("media_budget.py",     [sys.executable, str(scripts / "media_budget.py"), str(ep)], None, "timed"),
    ("audio_levels.py",     [sys.executable, str(scripts / "audio_levels.py"), str(ep)], None, "file"),
    ("blank_scan.mjs",      ["node", str(scripts / "blank_scan.mjs"), ep_abs], None, "browser"),
    ("overlap_check.mjs",   ["node", str(scripts / "overlap_check.mjs"), ep_abs], None, "browser"),
    ("occlusion_check.mjs", ["node", str(scripts / "occlusion_check.mjs"), ep_abs], None, "browser"),
    ("graphics_qc.mjs",     ["node", str(scripts / "graphics_qc.mjs"), "."], ep.resolve(), "browser"),
]

beside = render_busy.render_holder()
if beside:
    floor = float(yaml.safe_load((scripts.parent / "config.yaml").read_text(encoding="utf-8"))["render"]["gates_beside_render_min_free_gb"])
    print(f"[run_gates] a render holds the heavy lock: {render_busy.describe(beside)}. File-only gates run while free "
          f"memory stays >= {floor:g} GB (config.yaml render.gates_beside_render_min_free_gb); browser gates wait.")
stamp, checked = ep / timeline.STAMP, timeline.digest(ep)

failed, waiting = [], []
for name, cmd, cwd, kind in GATES:
    if beside and kind == "browser":
        waiting.append(name)
        continue
    if beside and (free := render_busy.free_gb()) < floor:  # read before every gate: the render's memory moves
        print(f"\nRUN_GATES WAIT - {free:.1f} GB free beside the render, below config.yaml "
              f"render.gates_beside_render_min_free_gb {floor:g} GB: {name} and every gate after it not run.")
        sys.exit(3)
    print(f"\n=== {name} ===", flush=True)  # header before the gate's own output (e2e.gate_results reads it)
    r = subprocess.run(cmd, cwd=cwd)
    if r.returncode != 0:
        stamp.unlink(missing_ok=True)
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

if waiting:
    print(f"RUN_GATES WAIT - file-only gates green; {len(waiting)} browser gates waiting for the render, not run: "
          f"{', '.join(waiting)}. Not a pass: re-run when the render ends.")
    sys.exit(3)

if timeline.digest(ep) != checked:
    print("RUN_GATES FAIL - the timeline changed while the gates ran; no stamp. Re-run the gates.")
    sys.exit(1)
stamp.write_text(checked, encoding="ascii")
print("RUN_GATES PASS - all gates green, safe to render.")
sys.exit(0)
