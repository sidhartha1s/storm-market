#!/usr/bin/env python3
"""Episode identity: what kind of episode a slug is, and its E<nn> number and topic.

Why one owner: four gates each carried their own slug pattern (`ep-`, `ep\\d*-`), so a documentary
named the way CLAUDE.md step 7 asks (`e10-<topic>`) matched none of them and skipped the CTA, end-ask,
close-card, voice and layer checks while run_gates printed PASS.

Slugs:
  e<nn>-<topic>      documentary numbered at kickoff (e10- onward); E number = the slug's number
  ep-<topic>-<year>  documentary E02 to E09; its number is in the tracked E<nn>-<topic>-metadata.md name
  ep<n>-<topic>      documentary from before the current build contract (ep1- to ep8-, El Reno = ep4-)
  ms- / sh- / br-    mini, short, old breaking lane

  python3 scripts/episode.py            # every numbered episode: E<nn>-<topic>  <slug>
"""
import re
import sys
from pathlib import Path

_DOC = re.compile(r"(ep\d*|e\d+)-")
_OLD_DOC = re.compile(r"ep\d+-")
_NUMBERED = re.compile(r"e(\d+)-(.+)")
_METADATA = re.compile(r"E(\d+)-(.+)-metadata\.md")


def is_documentary(slug):
    return bool(_DOC.match(slug))


def is_current_documentary(slug):
    """A documentary built to the current contract (corner circle, bed, Paul's clips, brand close card)."""
    return is_documentary(slug) and not _OLD_DOC.match(slug)


def is_mini(slug):
    return slug.startswith("ms-")


def identity(ep_dir):
    """(number, topic) of an episode folder, or None while it has no E number."""
    ep_dir = Path(ep_dir)
    m = _NUMBERED.fullmatch(ep_dir.name)
    if m:
        return int(m.group(1)), m.group(2)
    found = sorted(mm for f in ep_dir.glob("E*-metadata.md") if (mm := _METADATA.fullmatch(f.name)))
    if len(found) > 1:
        sys.exit(f"[episode] FAIL: {ep_dir.name} has {len(found)} E<nn>-*-metadata.md files; one episode, one number")
    return (int(found[0].group(1)), found[0].group(2)) if found else None


def label(ep_dir):
    """E<nn>-<topic>, the prefix of every deliverable name and of the uploads folder; None without a number."""
    ident = identity(ep_dir)
    return f"E{ident[0]:02d}-{ident[1]}" if ident else None


def numbered(episodes_dir):
    """{number: episode folder} for every numbered episode; two folders on one number is a FAIL."""
    out = {}
    for d in sorted(Path(episodes_dir).iterdir()):
        ident = identity(d) if d.is_dir() else None
        if not ident:
            continue
        if ident[0] in out:
            sys.exit(f"[episode] FAIL: E{ident[0]:02d} is claimed by both {out[ident[0]].name} and {d.name}")
        out[ident[0]] = d
    return out


def next_number(episodes_dir):
    return max(numbered(episodes_dir), default=0) + 1


if __name__ == "__main__":
    episodes = Path(__file__).resolve().parent.parent / "episodes"
    for n, d in sorted(numbered(episodes).items()):
        print(f"{label(d)}  {d.name}")
    print(f"next: e{next_number(episodes)}-<topic>")
