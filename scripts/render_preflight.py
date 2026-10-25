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

Exits non-zero (and says why, in GB) if the box is not quiet enough to render; it never asks the owner to close his apps.

It also enforces two things that were written as prose rules and therefore forgotten:
the media budget (media_budget.py) and the version pin. "Remember to run npm view"
is the same class of instruction as "remember to cap your assets" — which survived
twelve failed renders precisely because nothing checked it.
"""
import re
import subprocess
import sys
from pathlib import Path

import render_busy  # the busy check below reuses this, not a second process/name list


# --- version helpers (shared: pin_ritual.py imports parse_pin) -----------------

def parse_pin(repo):
    """The pinned hyperframes version from config.yaml, or None if the key is missing."""
    m = re.search(r'hyperframes_version:\s*"([\d.]+)"',
                  (repo / "config.yaml").read_text(encoding="utf-8", errors="replace"))
    return m.group(1) if m else None


def version_check(repo):
    """Pin drift (offline): config.yaml and the npx pin in the render scripts disagreeing
    means the render does not run the version anyone reviewed — hard fail.

    Currency is NOT checked here (owner 26 Sep 26, replaces the 2026-08-14 full-render
    block): a newer npm release must never stop a render mid-episode. Episode kickoff runs
    `python3 scripts/pin_ritual.py --check-only` and bumps before the first render instead,
    so one episode renders on one version end to end.
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

    print(f"[version] pin {pinned}; render scripts agree")
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
              "2026-09-11). Wait for memory to free or render on the other box; never ask the owner to close his apps.", file=sys.stderr)
        return 2
    print(f"[preflight] OK — no render alive, {free:.1f} GB free.")
    return None


# --- layer parity: a documentary renders only with every layer the owner already asked for ---
# The Joplin draft (18 Oct 26) went to render with 0 corner-circle mounts and no music bed while
# both shipped documentaries had them. Owner: "it should be fucking checked before you fucking fire render".

DOC_SLUG = "ep-"
TAG = re.compile(r'<(audio|video)\b((?:[^>"]|"[^"]*")*)>', re.I)
ATTR = re.compile(r'([\w-]+)(?:="([^"]*)")?')
BED_COVER_MIN = 0.80
PAUL_CLIPS = 6


def _mounts(html):
    live = re.sub(r"<!--.*?-->", "", html, flags=re.S)  # a commented-out mount is not mounted
    return [(tag.lower(), dict(ATTR.findall(attrs))) for tag, attrs in TAG.findall(live)]


def _window(attrs):
    start = float(attrs["data-start"])
    return start, start + float(attrs["data-duration"])


def _circle_gap(mounts, _episode=None):
    # same window rule as circle_cut.windows (pip class + pip-w id), so the gate and the cutter agree
    if not any(t == "video" and "pip" in a.get("class", "").split() and a.get("id", "").startswith("pip-w")
               for t, a in mounts):
        return '0 <video id="pip-w<n>" class="pip"> mounts'


def _bed_gap(mounts, _episode=None):
    # A bed is how the shipped episodes mount it: data-bed plus "bed" or "mus" in the id (Palm Sunday
    # sx-bed-a1, El Reno sx-mus-bed-a, 1974 sx-mus-a1). Swells and hits also carry data-bed, so the
    # attribute alone is not a bed.
    beds = sorted(_window(a) for t, a in mounts
                  if t == "audio" and "data-bed" in a and {"bed", "mus"} & set(a.get("id", "").split("-")))
    if not beds:
        return "0 bed <audio> mounts (data-bed with 'bed' or 'mus' in the id)"
    narration = [_window(a) for t, a in mounts if t == "audio" and re.match(r"nx-(?!ins)", a.get("id", ""))]  # same narration rule as lint_timeline / circle_audio
    if not narration:
        return "no nx- narration to measure the bed against"
    lo, hi = min(s for s, _ in narration), max(e for _, e in narration)
    covered, edge = 0.0, lo
    for start, end in beds:
        start, end = max(start, edge), min(end, hi)
        if end > start:
            covered, edge = covered + end - start, end
    share = covered / (hi - lo)
    if share < BED_COVER_MIN:
        return f"beds cover {share:.0%} of the narration span {lo:.1f}-{hi:.1f} s, need {BED_COVER_MIN:.0%}"


def _paul_gap(mounts, _episode=None):
    clips = {a["id"] for t, a in mounts
             if t == "video" and re.fullmatch(r"ins-paul-\d+", a.get("id", ""))}
    if len(clips) < PAUL_CLIPS:
        return f'{len(clips)} <video id="ins-paul-<n>"> mounts, need {PAUL_CLIPS}'


# Camille and Mayfield rough cuts (23 Oct 26) shipped a still of circle-portrait-560.jpg as the circle (Camille
# commit 0ab221e4 swapped them out). Measured over 20 s at 2 fps, 64x64 grey: the stand-in moves 0.01 levels a
# frame on average, a real FlashHead face 3.8 to 6.3 (Joplin's pip clips 3.82 to 5.19). Below this the circle is a
# still, whatever its file name.
FACE_MOTION_MIN = 1.0
FACE_SAMPLE = 64


def face_motion(path):
    """Mean grey-level change between frames 0.5 s apart over the clip's first 20 s (0..255)."""
    n = FACE_SAMPLE * FACE_SAMPLE
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-t", "20", "-vf",
                          f"fps=2,scale={FACE_SAMPLE}:{FACE_SAMPLE},format=gray", "-f", "rawvideo", "-"],
                         capture_output=True, check=True).stdout
    frames = [raw[i:i + n] for i in range(0, len(raw) - n + 1, n)]
    if len(frames) < 2:
        return 0.0
    return sum(sum(abs(a - b) for a, b in zip(x, y)) / n for x, y in zip(frames, frames[1:])) / (len(frames) - 1)


def _frozen_gap(mounts, episode=None):
    if episode is None:
        return None
    # a missing file is sweep_episode.py's finding, not this one
    frozen = [f"{a['id']} ({m:.2f})" for t, a in mounts
              if t == "video" and "pip" in a.get("class", "").split() and (episode / a.get("src", "")).is_file()
              and (m := face_motion(episode / a["src"])) < FACE_MOTION_MIN]
    if frozen:
        return f"{len(frozen)} pip clip(s) barely move, need {FACE_MOTION_MIN:g}: " + ", ".join(frozen)


LAYERS = (
    ("presenter corner circle", _circle_gap,
     "mg-quickref.md 'Corner circle': Paul's face speaking the narration, on through the whole "
     "documentary wherever the corner is free"),
    ("music bed", _bed_gap,
     "CLAUDE.md 'Sound': one bed across the episode plus swells at script peaks (about every "
     "45 to 60 s) is the default"),
    ("Paul full-frame clips", _paul_gap,
     "mg-quickref.md 'Paul on screen': Full frame (Flow/Omni), about 1 min: 6 clips of 10 s"),
    ("moving presenter face", _frozen_gap,
     "mg-quickref.md 'Corner circle': the circle is FlashHead's face speaking, never a still stand-in"),
)


def missing_layers(slug, html, episode=None):
    """(layer, finding, rule) for every owner-asked layer the timeline lacks; [] outside documentaries."""
    if not slug.startswith(DOC_SLUG):
        return []
    mounts = _mounts(html)
    return [(name, gap, rule) for name, check, rule in LAYERS if (gap := check(mounts, episode))]


def layer_refusal(episode):
    """None if every layer is mounted, else the exit code preflight should use."""
    missing = missing_layers(episode.name, (episode / "index.html").read_text(encoding="utf-8"), episode)
    if not missing:
        print("[layers] OK: circle (moving), bed and Paul's clips are mounted.")
        return None
    for name, gap, rule in missing:
        print(f"[layers] MISSING {name}: {gap}. Rule: {rule}", file=sys.stderr)
    return 6


def main():
    episode = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    rc = layer_refusal(episode)
    if "--layers" in sys.argv[2:]:  # run_gates.py runs only this check, so a missing layer shows before render.cmd
        sys.exit(rc or 0)
    if rc:
        print("[preflight] REFUSING TO RENDER: a layer the owner already asked for is missing.",
              file=sys.stderr)
        sys.exit(rc)

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


if __name__ == "__main__":
    main()
