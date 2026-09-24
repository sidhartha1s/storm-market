#!/usr/bin/env python3
"""End-to-end check of the pipeline tooling. Read-only: never renders, never calls TTS or any paid API.

1. Every scripts/test_*.py self-check must exit 0 (each one proves a gate FAILs on a seeded defect).
2. For each real episode given, the tooling must run end to end without crashing:
   - tts_episode.parse_segments + word_budget's counter read the script (0 segments is fine only
     for a script word_budget can count another way),
   - scripts/run_gates.py runs the whole pre-render suite and ends in a verdict.
   An episode may legitimately FAIL a gate (a real defect); a crash, a traceback or a missing
   verdict is a tooling bug and fails this suite.

Usage: python3 scripts/e2e.py [episodes/<slug> ...]
Exit 0 = all green. Exit 1 = a self-check failed or a tool crashed (named in the output).
"""
import re
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent

# run_gates' four Node gates exit 1 on an uncaught JS exception same as on a real gate FAIL.
# These markers only ever appear in a Node crash dump (checked against every gate's own FAIL
# print via grep) - never widen this list without re-checking the gate scripts' FAIL text.
NODE_CRASH_MARKERS = ("node:internal", "\n    at ", "Error [ERR_", "TypeError:", "ReferenceError:")

# gate names in run order, scraped from run_gates.py's own GATES list (single source of truth)
GATE_NAMES = re.findall(r'^\s*\("([^"]+)",', (SCRIPTS / "run_gates.py").read_text(encoding="utf-8"), re.M)


def is_tool_crash(out):
    """A crashed gate (Python traceback or uncaught Node exception), not a legitimate gate FAIL."""
    return "Traceback (most recent call last)" in out or any(m in out for m in NODE_CRASH_MARKERS)


def run(cmd, timeout, cwd=None):
    """A hung tool is a failure, never a suite that waits forever: timeout returns exit code None."""
    try:
        r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8",
                           errors="replace", timeout=timeout)
    except subprocess.TimeoutExpired:
        return None, f"(timed out after {timeout}s)"
    return r.returncode, r.stdout + r.stderr


def main():
    sys.stdout.reconfigure(errors="replace")  # a gate printing a non-cp1252 glyph must not crash the suite
    bad = []

    print("== self-checks ==")
    tests = sorted(SCRIPTS.glob("test_*.py"))
    if not tests:
        bad.append("no scripts/test_*.py found")
    for t in tests:
        code, out = run([sys.executable, str(t)], timeout=600)
        print(f"{'PASS' if code == 0 else 'FAIL'} {t.name} (exit {code})")
        if code != 0:
            bad.append(t.name)
            print(out[-1500:])

    sys.path.insert(0, str(SCRIPTS))
    from tts_episode import parse_segments  # noqa: E402

    for arg in sys.argv[1:]:
        ep = Path(arg).resolve()
        print(f"\n== {ep.name} ==")
        script = ep / "edit_script.md"
        if script.exists():
            text = script.read_text(encoding="utf-8")
            try:
                segs = parse_segments(text)
                print(f"parse_segments: {len(segs)} segments")
                if not segs and "## SCRIPT" not in text:
                    bad.append(f"{ep.name}: script parses to 0 segments and has no '## SCRIPT' section")
            except Exception as e:  # a SegmentParseError is a real script defect worth surfacing here
                print(f"parse_segments raised {type(e).__name__}: {e}")
                bad.append(f"{ep.name}: parse_segments {type(e).__name__}")
        code, out = run([sys.executable, str(SCRIPTS / "run_gates.py"), str(ep)], timeout=1800)
        verdict = next((l for l in out.splitlines() if l.startswith("RUN_GATES")), None)
        print(verdict or "(no RUN_GATES verdict line)")
        if is_tool_crash(out) or verdict is None or code not in (0, 1):
            bad.append(f"{ep.name}: run_gates crashed or gave no verdict (exit {code})")
            print(out[-2500:])
        ran = set(re.findall(r'^=== (.+) ===$', out, re.M))
        not_exercised = [g for g in GATE_NAMES if g not in ran]
        if not_exercised:
            print("not exercised: " + ", ".join(not_exercised))

    print()
    if bad:
        print("E2E FAIL - " + "; ".join(bad))
        sys.exit(1)
    print("E2E PASS")


if __name__ == "__main__":
    main()
