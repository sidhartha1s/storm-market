#!/usr/bin/env python3
"""Fail a hook whose shape repeats either of the last 2 episodes' hooks (owner 26 Oct 26).

The rule and the shape menu live in references/script-quickref.md "The hook"; the tags are read
from its "### Hook shapes" list, so this file holds no second copy. Each edit_script.md records
`Hook shape: <tag> (<YYYY-MM-DD>)` on its own line. "Last 2 episodes" = the 2 most recently dated
tags of OTHER episodes across every checkout of the repo (main and every worktree), because the
episodes the owner sees side by side are usually still on unmerged branches.

Usage: python3 scripts/hook_shape.py episodes/<slug>
Exit 0 = tag present, on the menu, and not the shape of the last 2 episodes. Exit 1 = it fails.
"""
import re
import subprocess
import sys
from pathlib import Path

TAG_LINE = re.compile(r"^Hook shape: `?([a-z-]+)`? \((\d{4}-\d{2}-\d{2})\)", re.M)
MENU_LINE = re.compile(r"^- `([a-z-]+)`:", re.M)


def menu_tags(quickref_text):
    section = quickref_text.split("### Hook shapes", 1)[1].split("\n#", 1)[0]
    return MENU_LINE.findall(section)


def parse_tag(edit_script_text):
    m = TAG_LINE.search(edit_script_text)
    return (m.group(1), m.group(2)) if m else None


def check(own, others, menu):
    """own = (tag, date) or None; others = {slug: (tag, date)}; returns a list of failures."""
    if own is None:
        return ["no `Hook shape: <tag> (<YYYY-MM-DD>)` line in edit_script.md"]
    tag, _ = own
    if tag not in menu:
        return [f"hook shape `{tag}` is not on the menu: {', '.join(menu)}"]
    last2 = sorted(others.items(), key=lambda kv: kv[1][1], reverse=True)[:2]
    return [f"hook shape `{tag}` repeats {slug} ({date})" for slug, (t, date) in last2 if t == tag]


def other_tags(ep, slug):
    """Latest-dated tag per other episode slug, over every checkout `git worktree list` names."""
    out = subprocess.run(["git", "-C", str(ep), "worktree", "list", "--porcelain"],
                         capture_output=True, text=True, check=True).stdout
    found = {}
    for line in out.splitlines():
        if not line.startswith("worktree "):
            continue
        for es in Path(line[9:]).glob("episodes/*/edit_script.md"):
            other = es.parent.name
            tag = parse_tag(es.read_text(encoding="utf-8", errors="replace"))
            if other != slug and tag and (other not in found or tag[1] > found[other][1]):
                found[other] = tag
    return found


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python3 scripts/hook_shape.py episodes/<slug>")
    ep = Path(sys.argv[1]).resolve()
    es = ep / "edit_script.md"
    if not es.is_file():
        sys.exit(f"HOOK_SHAPE FAIL - no edit_script.md in {ep}")
    quickref = Path(__file__).resolve().parent.parent / "references" / "script-quickref.md"
    menu = menu_tags(quickref.read_text(encoding="utf-8"))
    own = parse_tag(es.read_text(encoding="utf-8"))
    others = other_tags(ep, ep.name)
    fails = check(own, others, menu)
    if fails:
        print("HOOK_SHAPE FAIL - " + "; ".join(fails))
        sys.exit(1)
    print(f"HOOK_SHAPE PASS - `{own[0]}`, last 2 episodes: "
          + ", ".join(f"{s} `{t}`" for s, (t, d) in sorted(others.items(), key=lambda kv: kv[1][1], reverse=True)[:2]))


if __name__ == "__main__":
    main()
