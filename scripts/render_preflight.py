#!/usr/bin/env python3
"""Refuse to start a render while the box is busy.

ep3 v3 lost two renders to `[FFmpeg] ffprobe deadline with code 0` — a deadline miss,
not a corrupt asset. The tell is in the failure summary: between two failures of the
same composition, compileOnlyMs went 95s -> 260s and browserProbeMs 31s -> 99s, on
FEWER videos (23 -> 20). Nothing about the episode got heavier; the machine did. The
Playwright QC gates each run a Chromium over every composition, and a render sharing
8 cores with them starves at the probe stage.

CLAUDE.md already said "don't run other heavy sessions during a final render". This
makes it a gate instead of a sentence, because the failure costs 10 minutes and looks
like an asset problem.

Exits non-zero (and says what to close) if the box is not quiet enough to render.

It also enforces two things that were written as prose rules and therefore forgotten:
the media budget (media_budget.py) and the version pin. "Remember to run npm view"
is the same class of instruction as "remember to cap your assets" — which survived
twelve failed renders precisely because nothing checked it.
"""
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import render_busy  # the busy check below reuses this, not a second process/name list


# --- version helpers (shared: pin_ritual.py imports these) ---------------------

def parse_pin(repo):
    """The pinned hyperframes version from config.yaml, or None if the key is missing."""
    m = re.search(r'hyperframes_version:\s*"([\d.]+)"',
                  (repo / "config.yaml").read_text(encoding="utf-8", errors="replace"))
    return m.group(1) if m else None


def npm_latest(timeout=30):
    """Latest hyperframes on npm, or None (npm missing/unreachable/garbage output).

    None means currency is UNKNOWN — each caller decides what that implies
    (preflight proceeds, the ritual hard-fails)."""
    npm = shutil.which("npm")
    if not npm:
        return None
    try:
        out = subprocess.run([npm, "view", "hyperframes", "version"],
                             capture_output=True, text=True, timeout=timeout).stdout.strip()
    except (subprocess.TimeoutExpired, OSError):
        return None
    return out if re.fullmatch(r"[\d.]+", out) else None


def semver(v):
    return tuple(int(x) for x in v.split("."))


def version_check(repo, mode):
    """Pin drift (offline) + pin currency (registry).

    Drift: config.yaml and the npx pin in the render scripts disagreeing means the render
    does not run the version anyone reviewed — hard fail, checked offline.

    Currency (owner 2026-08-14, supersedes the 2026-07-29 'planning question' ruling): a
    FULL render refuses to start while npm has a newer hyperframes than the pin, and the
    unblock is `python3 scripts/pin_ritual.py` — the scripted A/B ritual that verifies and
    bumps in ~10-25 min. Upstream ships ~1.6 releases/day; the old non-blocking warning let
    the pin rot 26 versions in 2 weeks. Drafts skip the registry lookup entirely (iteration
    speed — the answer would not block anyway), and npm being unreachable NEVER blocks a
    render — offline means currency unknown, not stale.
    """
    pinned = parse_pin(repo)
    if pinned is None:
        print("[version] no hyperframes_version in config.yaml", file=sys.stderr)
        return 4

    drift = []
    for script in sorted((repo / "scripts").glob("*.cmd")):
        for used in re.findall(r'npx hyperframes@([\d.]+)', script.read_text(
                encoding="utf-8", errors="replace")):
            # ep2 shipped on its own pin; its retired scripts are history, not a run path
            if used != pinned and "ep3v2" not in script.name and "ep2" not in script.name:
                drift.append((script.name, used))
    if drift:
        print(f"[version] PIN DRIFT — config.yaml says {pinned}:", file=sys.stderr)
        for name, used in drift:
            print(f"    {name} runs hyperframes@{used}", file=sys.stderr)
        return 5

    if mode != "full":
        print(f"[version] pin {pinned}; render scripts agree (currency checked on full "
              "renders and by pin_ritual.py, not on drafts)")
        return 0
    latest = npm_latest()
    if latest is None:
        print(f"[version] pin {pinned}; scripts agree. Currency UNKNOWN (npm unreachable) "
              "— proceeding, an offline box must not kill a render.")
        return 0
    if semver(latest) > semver(pinned):
        # Owner per-render override (ep6, 2026-08-23, when 0.8.6–0.8.10 opened a visible
        # Windows Terminal tab per ffprobe/ffmpeg spawn and the ritual could not bump).
        # Kept for the next such block. Never silent — it names itself in the render log.
        if os.environ.get("RENDER_PIN_STALE_OK") == "1":
            print(f"[version] [OVERRIDE] PIN STALE (npm latest {latest}, pin {pinned}) — "
                  "rendering anyway: RENDER_PIN_STALE_OK=1 set by the owner for this run.")
            return 0
        print(f"[version] PIN STALE — npm latest is {latest}, pin is {pinned}. A full "
              f"render must run a verified-current pin.\n[version] Unblock: python3 "
              f"scripts/pin_ritual.py  (A/B-verifies and bumps, ~10-25 min)",
              file=sys.stderr)
        return 6
    print(f"[version] pin {pinned}; render scripts agree; current (npm latest {latest})")
    return 0


def busy_refusal():
    """None if clear to render, else the exit code preflight should use.

    Reuses render_busy's own live-render detection and free-RAM floor instead of a second,
    narrower process-name list: render_busy.live_renders() matches on command line (catches
    chrome-headless-shell.exe capture workers and any other hyperframes process), not on a
    fixed WATCH tuple that never saw chrome-headless-shell.exe or firefox.exe and refused on
    process COUNT instead of free RAM (an owner's own idle chrome.exe tabs could false-refuse
    while a live render beside them passed)."""
    live = render_busy.live_renders()
    if live:
        print(f"[preflight] REFUSING TO RENDER — {len(live)} hyperframes render(s) already "
              "alive; one heavy job at a time (owner 2026-09-11):", file=sys.stderr)
        for l in live:
            print("   ", l[:160], file=sys.stderr)
        return 2
    free = render_busy.free_gb()
    if free < render_busy.MIN_FREE_GB:
        print(f"[preflight] REFUSING TO RENDER — {free:.1f} GB free, need "
              f"{render_busy.MIN_FREE_GB:g} GB so the render keeps headroom (owner "
              "2026-09-11). Close a browser or wait.", file=sys.stderr)
        return 2
    print(f"[preflight] OK — no render alive, {free:.1f} GB free.")
    return None


def main():
    rc = busy_refusal()
    if rc:
        print("[preflight] A render that starts here fails at video_extract with "
              "'ffprobe deadline with code 0', which reads like a bad asset and is not.",
              file=sys.stderr)
        sys.exit(rc)

    # An idle box is not enough. Eleven of the twelve failed renders were started with the
    # machine quiet and died anyway, because the media itself was too expensive to extract.
    # The asset check is part of preflight so it cannot be skipped by launching a render
    # directly: the render script calls this file and stops on a non-zero exit.
    here = Path(__file__).resolve().parent
    episode = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    mode = sys.argv[2] if len(sys.argv) > 2 else "full"

    rc = version_check(here.parent, mode)
    if rc:
        print("[preflight] REFUSING TO RENDER — version pin is not trustworthy (see above).",
              file=sys.stderr)
        sys.exit(rc)
    budget = subprocess.run([sys.executable, str(here / "media_budget.py"), str(episode)],
                            capture_output=True, text=True)
    print(budget.stdout.rstrip())
    if budget.returncode != 0:
        print(budget.stderr.rstrip(), file=sys.stderr)
        print("[preflight] REFUSING TO RENDER — media budget gate failed (see above).",
              file=sys.stderr)
        sys.exit(3)


if __name__ == "__main__":
    main()
