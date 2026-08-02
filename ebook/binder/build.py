#!/usr/bin/env python3
"""Parse P6-the-binder.md's 41 form specifications into real fillable pages.

The manuscript file is a SPECIFICATION, not prose to typeset: it names 41 forms across
seven sections and, for each, the fields the form must carry. This script parses that
markdown directly and renders one fixed 6x9 `.page` per form (repeated where the spec
says to, or where a form's own field count needs a second "(continued)" page). It never
retypes a field name — every label in the output HTML is a substring of P6-the-binder.md
(or, for the two forms whose field list genuinely lives in another chapter -- see
standard_gobag_items() -- of that chapter, parsed the same way appendix/build.py parses
the front matter's region table). A later manuscript edit flows through on the next run.

Where the spec does not dictate a *layout* (table vs. checklist vs. plain lines, or how
many rows/copies a form with no explicit page count gets), that choice is made in code
and commented at the point it's made -- see FORM_LAYOUT and the per-form builders below.
No field is invented to fill space: a form with 6 short fields gets 6 fill-lines, not a
padded 12.

Usage:
    python3 build.py --check     # parse and report form/page counts, write nothing
    python3 build.py --build     # write out/binder.html
"""

import argparse
import html as html_mod
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
MANUSCRIPT = HERE.parent / "manuscript" / "P6-the-binder.md"
GOBAG_SOURCE = HERE.parent / "manuscript" / "P5-C3-evacuation.md"
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

def read_lines(path):
    if not path.exists():
        sys.exit(f"FAIL: {path} does not exist.")
    return path.read_text(encoding="utf-8").splitlines()


def parse_manuscript():
    """Returns (sections, front_sheet_lines) where sections is a list of
    {letter, title, budget, forms: [...]} and each form is
    {number, title, serves_raw, _blocks: [raw_block_lines, ...]}.

    A form's body is every blank-line-separated block between its own "### Form N"
    heading (skipping the italic Serves line, handled separately) and the next
    "### Form" / "## Section" / "## The one-page front sheet" heading."""
    lines = read_lines(MANUSCRIPT)
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
            sm = SERVES_LEAD_RE.match(lines[j].strip()) if j < n else None
            if sm:
                cur_form["serves_raw"] = sm.group(1).strip()
                remainder = sm.group(2).strip()
                if remainder:
                    pending_block.append(remainder)
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
SENT_SPLIT_RE = re.compile(r"(?<=[.:])\s+(?=[A-Z*])")


def join_block(raw_lines):
    return " ".join(raw_lines)


def classify_unit(text):
    """One sentence (or a whole blockquote) -> a typed unit dict. The *shape* of a unit
    (table-per-entity / row-per-item / field-list / bold-label group / plain text) is
    read off markup the spec itself uses consistently: 'Per X:' / 'Rows for:' as an
    explicit repeat instruction, a leading '**Label**' as a labelled sub-section, '·' as
    the field separator used almost everywhere else. Nothing here invents field text; it
    only decides which HTML shape the same field text renders as."""
    m = re.match(r"^Per (\w+):\s*(.+)$", text)
    if m and "·" in m.group(2):
        fields = [f.strip().rstrip(".") for f in m.group(2).split("·")]
        return {"type": "table_per", "entity": m.group(1), "fields": fields}

    m = re.match(r"^Rows for:\s*(.+)$", text)
    if m:
        items = [f.strip().rstrip(".") for f in m.group(1).split("·")]
        return {"type": "rows_for", "items": items}

    m = re.match(r"^\*\*([^*]+?)\*\*:?\s*(.*)$", text)
    if m:
        return {"type": "group", "label": m.group(1).rstrip(":").strip(), "desc": m.group(2).strip()}

    if "·" in text:
        fields = [f.strip().rstrip(".") for f in text.split("·")]
        return {"type": "fields", "fields": fields}

    return {"type": "text", "text": text.strip()}


def classify_form(form):
    """Flattens a form's raw paragraph blocks into a list of typed `units` (see
    classify_unit) at SENTENCE granularity, because several forms mix an intro
    sentence, a labelled field sentence and a trailing instruction sentence inside one
    blank-line-delimited paragraph (Form 36 is the extreme case: one paragraph carries
    nine "**Label:** ... ·-list." sentences back to back). A blockquote block is kept
    as one whole "note" unit rather than sentence-split, since every blockquote in this
    file is already a single short reader-facing note."""
    form["raw_paragraphs"] = [join_block(b) for b in form["_blocks"]]
    units = []
    for raw in form["_blocks"]:
        if raw[0].startswith(">"):
            quote = " ".join(BLOCKQUOTE_RE.match(l).group(1) if BLOCKQUOTE_RE.match(l) else l
                              for l in raw)
            units.append({"type": "note", "text": quote.strip()})
            continue
        text = join_block(raw)
        for sentence in SENT_SPLIT_RE.split(text):
            sentence = sentence.strip()
            if sentence:
                units.append(classify_unit(sentence))
    form["units"] = units
    del form["_blocks"]
    return form


# ---------------------------------------------------------------- 3. small text helpers

NUM_WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
             "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
             "fourteen": 14, "fifteen": 15, "sixteen": 16}


def esc(s):
    return html_mod.escape(s)


def render_inline(text):
    """**bold** -> <strong>, *italic* -> <em>, and a run of 2+ underscores (the spec's
    own inline blank, e.g. Form 7's "power out for more than ___ hours") -> a small
    fillable span, so the reader's pen lands exactly where the spec already put the
    blank rather than on a separately-invented line."""
    text = esc(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\w)\*([^*\n]+)\*(?!\w)", r"<em>\1</em>", text)
    text = re.sub(r"_{2,}", '<span class="b-blank"></span>', text)
    return text


def split_top(text, sep=","):
    """Split on sep at top level only — not inside parentheses (Form 4's Crisis lines
    field has a parenthetical with its own comma: "988 (Suicide & Crisis Lifeline —
    call or text)")."""
    parts, depth, cur = [], 0, ""
    for ch in text:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == sep and depth == 0:
            parts.append(cur.strip())
            cur = ""
        else:
            cur += ch
    if cur.strip():
        parts.append(cur.strip())
    return parts


def field_line_class(label_raw):
    """A field whose label reads like a single word/date/number gets a short rule; one
    that reads like a sentence gets the full width — book.css's own sizing rule."""
    plain = re.sub(r"[*_]", "", label_raw)
    if len(plain) <= 22 and "," not in plain:
        return "short"
    if len(plain) <= 48:
        return "med"
    return ""


def render_field(label_raw, cls_hint=None):
    cls = field_line_class(label_raw) if cls_hint is None else cls_hint
    line_cls = f"line {cls}".strip() if cls else "line"
    return (f'<div class="field"><label>{render_inline(label_raw)}</label>'
            f'<div class="{line_cls}"></div></div>')


def render_fields(labels, cls_hint=None):
    return "".join(render_field(l, cls_hint) for l in labels)


def render_group_desc(desc):
    """A bold-labelled group's description renders as one or more fill-lines. If the
    spec already itemised the description with '·' or a real comma-separated list
    (3+ items — below that, a comma is just a compound sentence, not an enumeration),
    each item gets its own line; otherwise the whole description is one field."""
    desc = desc.strip().rstrip(".")
    if not desc or desc in (",",):
        return ""
    if "·" in desc:
        return render_fields([s.strip().rstrip(".") for s in desc.split("·")])
    subs = split_top(desc, ",")
    if len(subs) >= 3:
        return render_fields(subs)
    return render_field(desc.lstrip(", "))


def render_group(label, desc):
    body = render_group_desc(desc)
    if not body:
        # A bolded statement with nothing left to fill under it (Form 6's "nobody
        # goes back for anybody") — print the statement itself, not an empty field.
        return f'<p class="b-serves"><strong>{render_inline(label)}</strong></p>'
    return f'<div class="bgroup"><h4>{render_inline(label)}</h4>{body}</div>'


def render_groups(groups):
    return "".join(render_group(g["label"], g["desc"]) for g in groups)


def render_table(columns, rows, prefill_col0=None, numbered=True, tight=False):
    """columns: header labels. rows: row count. prefill_col0: optional list of already-
    known values for the first data column (e.g. Form 15's protection numbers, derived
    from its own "Serves 69-84" line, not invented)."""
    cls = "btable tight" if tight else "btable"
    ths = ("<th class=\"n\">#</th>" if numbered else "") + \
          "".join(f"<th>{render_inline(c)}</th>" for c in columns)
    body = []
    for r in range(rows):
        tds = f'<td class="n">{r + 1}</td>' if numbered else ""
        for ci in range(len(columns)):
            if prefill_col0 is not None and ci == 0:
                tds += f"<td>{esc(str(prefill_col0[r]))}</td>"
            else:
                tds += "<td></td>"
        body.append(f"<tr>{tds}</tr>")
    return f'<table class="{cls}"><tr>{ths}</tr>{"".join(body)}</table>'


def render_checklist(items, numbered=False):
    lis = []
    for i, item in enumerate(items, start=1):
        marker = f'<span class="bn">{i}.</span>' if numbered else '<span class="box"></span>'
        lis.append(f'<li class="bcheck">{marker}<span>{render_inline(item)}</span></li>')
    return f'<ul class="bchecklist">{"".join(lis)}</ul>'


def render_signature(count=1):
    return "".join(
        '<div class="bsign"><span>Signed</span><span class="b-blank"></span>'
        '<span>Date</span><span class="b-blank date"></span></div>'
        for _ in range(count))


def units_of_type(units, *types):
    return [u for u in units if u["type"] in types]


# ---------------------------------------------------------------- 4. one cross-chapter lookup

def standard_gobag_items():
    """Form 23 says "Standard contents checklist" without listing the contents — the
    list lives in Protection 107's own chapter (Serves 107), the same relationship
    appendix/build.py's region_first_ten() has with the front matter's region table.
    Parsed, not retyped: if Protection 107's paragraph is edited, this list changes
    with it on the next build. Fails loudly if the paragraph moves or is reworded,
    rather than silently shipping an empty go-bag page."""
    lines = read_lines(GOBAG_SOURCE)
    start = None
    for i, line in enumerate(lines):
        if line.strip() == "### 107 · The go-bag, per person":
            start = i
            break
    if start is None:
        sys.exit(f"FAIL: Protection 107 not found in {GOBAG_SOURCE} — Form 23 needs it "
                  "for the standard contents list.")
    for line in lines[start:start + 20]:
        if line.startswith("Contents that earn their weight:"):
            sentence = line.split(":", 1)[1].strip().rstrip(".")
            items = split_top(sentence, ",")
            items[-1] = re.sub(r"^and\s+", "", items[-1])
            return items
    sys.exit(f"FAIL: the go-bag contents sentence was not found under Protection 107 in "
              f"{GOBAG_SOURCE} — if it moved or was reworded, update standard_gobag_items().")


# ---------------------------------------------------------------- 5. page assembly

def page_shell(section_letter, section_title, kicker_extra, head_html, body_html, folio):
    kicker = f"Section {section_letter} · {kicker_extra}" if kicker_extra else f"Section {section_letter}"
    return (f'<section class="page">\n'
            f'<p class="runhead"><span>The Binder</span><span>Section {esc(section_letter)} '
            f'{D} {esc(section_title)}</span></p>\n'
            f'<p class="b-kicker">{esc(kicker)}</p>\n{head_html}\n{body_html}\n'
            f'<p class="folio">{folio}</p>\n</section>')


def form_head(form_title, serves_raw, cont_label=None):
    if cont_label:
        return f'<p class="b-cont">{render_inline(form_title)} {D} {esc(cont_label)}</p>'
    head = f'<h2 class="form-title">{render_inline(form_title)}</h2>'
    if serves_raw:
        head += f'<p class="b-serves">{render_inline(serves_raw)}</p>'
    return head
