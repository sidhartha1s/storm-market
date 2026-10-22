#!/usr/bin/env python3
"""Settle-frame snapshots of an episode, through the same RAM and render gate every other browser launch uses.

Why: `npx hyperframes snapshot` opens its own Chromium and was the one launch that skipped `render_busy.py`; on
22 Oct 26 builders took 60 of them on the ASUS beside each other and stalled the box. This is the one entry point:
it runs `render_busy.py` (exit 3 = wait, retry), reads the pin from config.yaml and passes everything else through.

Usage: python3 scripts/snapshot.py episodes/<slug> --at <t1>,<t2>,<t3> -o <dir> [more hyperframes snapshot args]
"""
import shutil
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))
from render_preflight import parse_pin  # noqa: E402


def argv(pin, args):
    return ["npx", f"hyperframes@{pin}", "snapshot", *args, "--no-end", "--describe", "false"]


def main(args):
    if len(args) < 1:
        sys.exit(__doc__.strip().splitlines()[-1])
    gate = subprocess.run([sys.executable, str(SCRIPTS / "render_busy.py")])
    if gate.returncode:
        return gate.returncode
    pin = parse_pin(SCRIPTS.parent)
    if not pin:
        sys.exit("[snapshot] FAIL: config.yaml has no hyperframes_version")
    cmd = argv(pin, args)
    return subprocess.run([shutil.which("npx") or cmd[0], *cmd[1:]]).returncode


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
