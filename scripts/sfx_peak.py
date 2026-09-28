#!/usr/bin/env python3
"""Report tool: for one-shot SFX hits (stamp/boom/impact) mounted in an episode's index.html,
measure each sound file's true peak sample time and print the data-start that lands the peak
exactly on the cue.

Why a reporting tool, not a wired-in mount: SFX timing is hand-authored directly in index.html
(`<audio data-start="...">`), and no script may author episode HTML — cuts, holds, timing design
are judgment (CLAUDE.md "HARD RULE: do not write code for what reasoning already does" tripwire).
This script only READS index.html and PRINTS a suggestion; the editor still hand-sets data-start.

Scope: one-shot hits only.
  - Risers are excluded — DESIGN.md rule stands: a riser ends where the LINE ends, not
    peak-aligned (id containing "riser" is skipped).
  - Beds are excluded (any element carrying the `data-bed` attribute) — continuous ambience has
    no single impact to align.
  - Narration (nx-*) and inserts (ins-*) are excluded — their timing is script/transcript driven.

Usage: python3 scripts/sfx_peak.py episodes/<slug> [element-id ...]
  No ids given -> reports every eligible hit element found in index.html.

Prints, per hit: id, src, cue (current data-start), the file's peak offset, and the corrected
data-start (cue - peak) that would land the transient on the cut.
"""
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

SAMPLE_RATE = 22050  # plenty for a peak-location measurement, keeps the decode cheap


def find_peak_time(path: Path, sample_rate: int = SAMPLE_RATE) -> float:
    """argmax(|signal|) over the decoded mono samples, in seconds from file start."""
    r = subprocess.run(
        ["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(sample_rate),
         "-f", "s16le", "-"],
        capture_output=True)
    if r.returncode != 0 or not r.stdout:
        raise ValueError(f"no decodable audio in {path}: {r.stderr[-300:]!r}")
    samples = np.frombuffer(r.stdout, dtype="<i2")
    peak_idx = int(np.argmax(np.abs(samples)))
    return peak_idx / sample_rate


_TAG_RE = re.compile(r"<(audio|video)\b([^>]*)>")


def eligible_hits(html: str):
    """Yield (id, src, cue) for every one-shot hit element — see module docstring for the
    riser/bed/narration/insert exclusions."""
    for m in _TAG_RE.finditer(html):
        attrs = m.group(2)
        eid = re.search(r'\sid="([^"]+)"', attrs)
        src = re.search(r'\ssrc="([^"]+)"', attrs)
        start = re.search(r'\sdata-start="([\d.]+)"', attrs)
        if not (eid and src and start):
            continue
        eid = eid.group(1)
        if eid.startswith("nx-") or eid.startswith("ins-"):
            continue
        if "riser" in eid:
            continue
        if re.search(r'\sdata-bed(?=[\s>/=]|$)', attrs):
            continue
        yield eid, src.group(1), float(start.group(1))


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    ep = Path(sys.argv[1])
    wanted = set(sys.argv[2:])
    html = (ep / "index.html").read_text(encoding="utf-8", errors="replace")
    rows = [r for r in eligible_hits(html) if not wanted or r[0] in wanted]
    if not rows:
        print("[sfx_peak] no eligible hit elements found (excluded: nx-/ins-/riser/data-bed ids)")
        return
    print(f"[sfx_peak] {len(rows)} hit element(s):")
    for eid, src, cue in rows:
        p = ep / src
        if not p.exists():
            print(f"  {eid}: MISSING {src}")
            continue
        peak = find_peak_time(p)
        corrected = cue - peak
        print(f"  {eid}: {src}  cue={cue:.3f}s  peak={peak:.3f}s  "
              f"-> corrected data-start={corrected:.3f}s")


if __name__ == "__main__":
    main()
