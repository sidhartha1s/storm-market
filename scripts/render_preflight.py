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
import re
import subprocess
import sys
from pathlib import Path

# a render itself needs: 3 workers + a capture Chromium + ffmpeg. Anything beyond a
# couple of idle helper processes is competition.
MAX_HEAVY = 2
HEAVY_MB = 120
WATCH = ("chrome.exe", "msedge.exe", "ffmpeg.exe", "ffprobe.exe")


def heavy_processes():
    out = subprocess.run(["tasklist", "/FO", "CSV", "/NH"],
                         capture_output=True, text=True).stdout
    found = []
    for line in out.splitlines():
        parts = [p.strip('"') for p in line.split('","')]
        if len(parts) < 5:
            continue
        name, pid, mem = parts[0], parts[1], parts[4]
        if name.lower() not in WATCH:
            continue
        try:
            mb = int(mem.replace(",", "").replace(" K", "")) / 1024
        except ValueError:
            continue
        if mb >= HEAVY_MB:
            found.append((name, pid, round(mb)))
    return found


def version_check(repo):
    """Pin drift is a hard failure; a newer release upstream is a loud warning.

    Drift is checked offline and is always a real bug: config.yaml and the npx pin in the
    render scripts disagreeing means the render does not run the version anyone reviewed.
    'Is something newer published' needs the network, so it warns rather than blocks — a
    render must not fail because npm is unreachable, but nobody gets to say they forgot.
    """
    cfg = (repo / "config.yaml").read_text(encoding="utf-8", errors="replace")
    m = re.search(r'hyperframes_version:\s*"([\d.]+)"', cfg)
    if not m:
        print("[version] no hyperframes_version in config.yaml", file=sys.stderr)
        return 4
    pinned = m.group(1)

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

    latest = subprocess.run(["npm", "view", "hyperframes", "version"],
                            capture_output=True, text=True, shell=True, timeout=60)
    newest = latest.stdout.strip()
    if latest.returncode != 0 or not re.fullmatch(r'[\d.]+', newest):
        print(f"[version] pin {pinned}; could not reach npm to check for newer (not fatal)")
        return 0
    if newest != pinned:
        print(f"[VERSION] pinned {pinned}, but hyperframes {newest} is published.")
        print(f"[VERSION] Bump config.yaml + the npx pins together, or decide deliberately")
        print(f"[VERSION] to stay. Read the diff for the extract stage and any timeout:")
        print(f"[VERSION] 0.7.81 shortened the ffprobe deadline from 120s to 30s.")
    else:
        print(f"[version] pin {pinned} is the latest published.")
    return 0


busy = heavy_processes()
if len(busy) > MAX_HEAVY:
    print(f"[preflight] REFUSING TO RENDER — {len(busy)} heavy processes are competing "
          f"for the CPU (limit {MAX_HEAVY}):", file=sys.stderr)
    for name, pid, mb in sorted(busy, key=lambda p: -p[2]):
        print(f"    {name:14} pid {pid:>7}  {mb:>6} MB", file=sys.stderr)
    print("[preflight] Close the QC browsers / stop background agents, then re-launch.",
          file=sys.stderr)
    print("[preflight] A render that starts here fails at video_extract with "
          "'ffprobe deadline with code 0', which reads like a bad asset and is not.",
          file=sys.stderr)
    sys.exit(2)

print(f"[preflight] OK — {len(busy)} heavy process(es), under the limit of {MAX_HEAVY}.")

# An idle box is not enough. Eleven of the twelve failed renders were started with the
# machine quiet and died anyway, because the media itself was too expensive to extract.
# The asset check is part of preflight so it cannot be skipped by launching a render
# directly: the render script calls this file and stops on a non-zero exit.
here = Path(__file__).resolve().parent
episode = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()

rc = version_check(here.parent)
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
