#!/usr/bin/env python3
"""Parse P6-the-binder.md's 41 form specifications into real fillable pages.

The manuscript file is a SPECIFICATION, not prose to typeset: it names 41 forms across
seven sections and, for each, the fields the form must carry. This script parses that
markdown directly and renders one fixed 6x9 `.page` per form (repeated where the spec
says to). It never retypes a field name — every label in the output HTML is a substring
of P6-the-binder.md, found by parsing, so a later manuscript edit flows through on the
next run. Where the spec does not dictate a *layout* (table vs. checklist vs. plain
lines, or how many rows/copies for a form with no explicit page count), that choice is
made in code and commented at the point it's made — see PAGE_PLAN and SHAPE below.

Usage:
    python3 build.py --check     # parse P6-the-binder.md and report form/page counts
    python3 build.py --build     # write out/binder.html
"""

import argparse
import html as html_mod
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
MANUSCRIPT = HERE.parent / "manuscript" / "P6-the-binder.md"
BOOK_CSS = HERE.parent / "build" / "book.css"
BINDER_CSS = HERE / "templates" / "binder.css"
OUT = HERE / "out"
D = "—"  # em dash

SECTION_RE = re.compile(r"^## Section ([A-Z]) — (.+?)\s*\((\d+) pages?\)\s*$")
FORM_RE = re.compile(r"^### Form (\d+)\s*·\s*(.+)$")
FRONT_SHEET_RE = re.compile(r"^## The one-page front sheet\s*$")
# The italic "Serves ..." run is always the leading run on its line, but two forms
# (29, 30) run field text on the *same* line right after the closing "*" instead of
# starting a new paragraph — captured as `remainder` and fed back into the block
# scanner rather than lost.
SERVES_LEAD_RE = re.compile(r"^\*(.+?)\*\s*(.*)$")


# ---------------------------------------------------------------- 1. parse the manuscript

def read_lines():
    if not MANUSCRIPT.exists():
        sys.exit(f"FAIL: {MANUSCRIPT} does not exist.")
    return MANUSCRIPT.read_text(encoding="utf-8").splitlines()


def split_blocks(lines):
    """Blank-line-separated paragraph blocks, each a list of its raw (stripped) lines.
    Mirrors review_pdf.py's own paragraph consumption (blank line ends a block) so a
    field list that wraps across source lines (e.g. Form 7's "Rows for:" list) is
    rejoined into one block instead of being cut at the wrap."""
    blocks = []
    cur = []
    for line in lines:
        if not line.strip():
            if cur:
                blocks.append(cur)
                cur = []
            continue
        cur.append(line.strip())
    if cur:
        blocks.append(cur)
    return blocks


def parse_manuscript():
    """Returns (sections, front_sheet) where sections is a list of
    {letter, title, budget, forms: [...]} and each form is
    {number, title, serves_raw, blocks: [raw_block_lines, ...]}.

    A form's body is every blank-line-separated block between its own "### Form N"
    heading (skipping the italic Serves line, handled separately) and the next
    "### Form" / "## Section" / "## The one-page front sheet" heading."""
    lines = read_lines()
    sections = []
    front_sheet_lines = []
    cur_section = None
    cur_form = None
    in_front_sheet = False
    pending_block = []

    def flush_block():
        nonlocal pending_block
        if pending_block:
            if cur_form is not None:
                cur_form["_blocks"].append(pending_block)
            pending_block = []

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()

        if FRONT_SHEET_RE.match(stripped):
            flush_block()
            in_front_sheet = True
            cur_form = None
            i += 1
            continue

        if in_front_sheet:
            front_sheet_lines.append(line)
            i += 1
            continue

        m = SECTION_RE.match(stripped)
        if m:
            flush_block()
            cur_section = {"letter": m.group(1), "title": m.group(2).strip(),
                           "budget": int(m.group(3)), "forms": []}
            sections.append(cur_section)
            cur_form = None
            i += 1
            continue

        m = FORM_RE.match(stripped)
        if m:
            flush_block()
            cur_form = {"number": int(m.group(1)), "title": m.group(2).strip(),
                        "serves_raw": "", "_blocks": []}
            cur_section["forms"].append(cur_form)
            # the very next non-blank line is the italic "*Serves ...*" line
            j = i + 1
            while j < n and not lines[j].strip():
                j += 1
            if j < n and lines[j].strip().startswith("*") and lines[j].strip().endswith("*"):
                cur_form["serves_raw"] = lines[j].strip().strip("*")
                i = j + 1
            else:
                i += 1
            continue

        if stripped == "---" or stripped.startswith("#"):
            # a rule or an unrelated heading (e.g. "## The forms") between forms
            flush_block()
            i += 1
            continue

        if not stripped:
            flush_block()
            i += 1
            continue

        pending_block.append(stripped)
        i += 1

    flush_block()
    return sections, front_sheet_lines


# ---------------------------------------------------------------- 2. classify each form's blocks

BLOCKQUOTE_RE = re.compile(r"^>\s*(.*)$")
BOLD_LABEL_RE = re.compile(r"\*\*([^*]+?)\*\*:?")


def join_block(raw_lines):
    return " ".join(raw_lines)


def classify_block(raw_lines):
    """One raw paragraph -> a typed block dict. See module docstring: the *shape* of a
    block (table / checklist / plain fields / groups / note) is inferred from markup the
    spec itself uses consistently (a leading '>' for a note, 'Per X:' / 'Rows for:' as an
    explicit repeat instruction, '·' as the field separator used almost everywhere,
    '**Label:**' groups where a form is written as labelled sub-sections instead).
    Nothing here invents field text; it only decides which HTML shape a field list of
    the same field text renders as."""
    text = join_block(raw_lines)

    if raw_lines[0].startswith(">"):
        quote = " ".join(BLOCKQUOTE_RE.match(l).group(1) if BLOCKQUOTE_RE.match(l) else l
                          for l in raw_lines)
        return {"type": "note", "text": quote.strip()}

    m = re.match(r"^Per (\w+):\s*(.+)$", text)
    if m and "·" in m.group(2):
        fields = [f.strip().rstrip(".") for f in m.group(2).split("·")]
        return {"type": "table_per", "entity": m.group(1), "fields": fields}

    m = re.match(r"^Rows for:\s*(.+)$", text)
    if m:
        # everything up to the first sentence that isn't part of the · list (the
        # list itself always ends the paragraph in the manuscript) is items
        items = [f.strip().rstrip(".") for f in m.group(1).split("·")]
        return {"type": "rows_for", "items": items}

    if "·" in text:
        fields = [f.strip().rstrip(".") for f in text.split("·")]
        return {"type": "fields", "fields": fields}

    if BOLD_LABEL_RE.search(text):
        # split into (label, description) groups at each **Label** boundary
        groups = []
        matches = list(BOLD_LABEL_RE.finditer(text))
        for k, mm in enumerate(matches):
            start = mm.end()
            end = matches[k + 1].start() if k + 1 < len(matches) else len(text)
            desc = text[start:end].strip()
            if desc.startswith(":"):
                desc = desc[1:].strip()
            groups.append({"label": mm.group(1).strip(), "desc": desc})
        return {"type": "groups", "groups": groups}

    return {"type": "text", "text": text}


def classify_form(form):
    form["blocks"] = [classify_block(b) for b in form["_blocks"]]
    del form["_blocks"]
    return form


# ---------------------------------------------------------------- main (parse-only for now)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="parse and report, no HTML written")
    parser.add_argument("--build", action="store_true", help="write out/binder.html")
    args = parser.parse_args()
    if not (args.check or args.build):
        parser.error("nothing to do -- pass --check or --build")

    sections, front_sheet_lines = parse_manuscript()
    for s in sections:
        for f in s["forms"]:
            classify_form(f)

    total_forms = sum(len(s["forms"]) for s in sections)
    print(f"{len(sections)} sections, {total_forms} forms, "
          f"{len(front_sheet_lines)} front-sheet lines")
    for s in sections:
        print(f"\nSection {s['letter']} — {s['title']} (budget {s['budget']} pages)")
        for f in s["forms"]:
            btypes = [b["type"] for b in f["blocks"]]
            print(f"  Form {f['number']} · {f['title']}  [{f['serves_raw'][:60]}]  blocks={btypes}")


if __name__ == "__main__":
    main()
