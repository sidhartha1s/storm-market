#!/usr/bin/env python3
"""Fail a hook whose shape repeats either of the last 2 episodes' hooks (owner 26 Oct 26).

The rule and the shape menu live in references/script-quickref.md "The hook"; the tags are read
from its "### Hook shapes" list, so this file holds no second copy. Each edit_script.md records
`Hook shape: <tag> (<YYYY-MM-DD>)` on its own line. "Last 2 episodes" = the 2 OTHER tagged episodes just before
this one in ship order: numbered episodes by their E number (scripts/episode.py), then episodes not numbered yet
after all of them by tag date (a tag date is when the hook was written, not when the episode shipped: E08 and E09
were tagged a day before E07). Read across every checkout of the repo (main and every worktree), because the
episodes the owner sees side by side are usually still on unmerged branches. Minis count too: the
owner watches them in the same feed. An untagged episode is skipped (it predates the rule).

Usage: python3 scripts/hook_shape.py episodes/<slug>
Exit 0 = tag present, on the menu, and not the shape of the last 2 episodes. Exit 1 = it fails.
"""
import re
import subprocess
import sys
from pathlib import Path

import episode

TAG_LINE = re.compile(r"^Hook shape: `?([a-z-]+)`? \((\d{4}-\d{2}-\d{2})\)", re.M)
MENU_LINE = re.compile(r"^- `([a-z-]+)`:", re.M)


def menu_tags(quickref_text):
    section = quickref_text.split("### Hook shapes", 1)[1].split("\n#", 1)[0]
    return MENU_LINE.findall(section)


def parse_tag(edit_script_text):
    m = TAG_LINE.search(edit_script_text)
    return (m.group(1), m.group(2)) if m else None


def ship_order(tagged):
    """Sort key of a (tag, date, E number or None): numbered episodes by number, then the rest by tag date."""
    _, date, number = tagged
    return (number is None, number or 0, date)


def last_two(others):
    """The 2 latest (slug, (tag, date, number)) in ship order; slug breaks a tie so the order is stable."""
    return sorted(others.items(), key=lambda kv: (ship_order(kv[1]), kv[0]), reverse=True)[:2]


def earlier(others, own):
    """Only episodes before this one in ship order count: a later episode is not one of its last 2."""
    return {s: td for s, td in others.items() if ship_order(td) <= ship_order(own)}


def check(own, others, menu):
    """own = (tag, date, number) or None; others = {slug: (tag, date, number)}; returns a list of failures."""
    if own is None:
        return ["no `Hook shape: <tag> (<YYYY-MM-DD>)` line in edit_script.md"]
    tag = own[0]
    if tag not in menu:
        return [f"hook shape `{tag}` is not on the menu: {', '.join(menu)}"]
    return [f"hook shape `{tag}` repeats {slug} ({date})" for slug, (t, date, _) in last_two(earlier(others, own)) if t == tag]


def checkouts(ep):
    """Every checkout of the repo `git worktree list` names (main first)."""
    out = subprocess.run(["git", "-C", str(ep), "worktree", "list", "--porcelain"],
                         capture_output=True, text=True, check=True).stdout
    return [Path(line[9:]) for line in out.splitlines() if line.startswith("worktree ")]


def number(ep_dir):
    ident = episode.identity(ep_dir)
    return ident[0] if ident else None


def other_tags(roots, slug):
    """(tag, date, E number) per other episode slug over the given checkout roots: the latest-dated tag, and the
    number from whichever checkout has the episode's E<nn>-*-metadata.md (often only main once it shipped)."""
    found, numbers = {}, {}
    for root in roots:
        for es in root.glob("episodes/*/edit_script.md"):
            other = es.parent.name
            tag = parse_tag(es.read_text(encoding="utf-8", errors="replace"))
            if other == slug or not tag:
                continue
            if other not in found or tag[1] > found[other][1]:
                found[other] = tag
            numbers[other] = numbers.get(other) or number(es.parent)
    return {s: tag + (numbers[s],) for s, tag in found.items()}


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python3 scripts/hook_shape.py episodes/<slug>")
    ep = Path(sys.argv[1]).resolve()
    es = ep / "edit_script.md"
    if not es.is_file():
        sys.exit(f"HOOK_SHAPE FAIL - no edit_script.md in {ep}")
    quickref = Path(__file__).resolve().parent.parent / "references" / "script-quickref.md"
    menu = menu_tags(quickref.read_text(encoding="utf-8"))
    tag = parse_tag(es.read_text(encoding="utf-8"))
    own = tag + (number(ep),) if tag else None
    others = other_tags(checkouts(ep), ep.name)
    fails = check(own, others, menu)
    if fails:
        print("HOOK_SHAPE FAIL - " + "; ".join(fails))
        sys.exit(1)
    print(f"HOOK_SHAPE PASS - `{own[0]}`, last 2 episodes: "
          + (", ".join(f"{s} `{t}`" for s, (t, d, n) in last_two(earlier(others, own))) or "none tagged yet"))


if __name__ == "__main__":
    main()
