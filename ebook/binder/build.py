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
and commented at the point it's made -- see build_form()'s dispatch and the per-form
builders below. No field is invented to fill space: a form with 6 short fields gets 6
fill-lines, not a padded 12.

Usage:
    python3 build.py --check     # parse and report form/page counts, write nothing
    python3 build.py --build     # write out/binder.html
"""

import argparse
import html as html_mod
import re
import sys
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).parent
MANUSCRIPT = HERE.parent / "manuscript" / "P6-the-binder.md"
GOBAG_SOURCE = HERE.parent / "manuscript" / "P5-C3-evacuation.md"
BOOK_CSS = HERE.parent / "build" / "book.css"
BINDER_CSS = HERE / "templates" / "binder.css"
OUT = HERE / "out"
D = "—"  # em dash

PARSED_SECTIONS = None  # set once in main(); build_form30() needs Form 29's own field
                        # list ("Same fields" — see build_form30's docstring)

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
SENT_SPLIT_RE = re.compile(r"(?<=[.:*])\s+(?=[A-Z*])")


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


SPLIT_TOKEN_RE = re.compile(r"\*\*|\*|[(),]")


def split_top(text, sep=","):
    """Split on sep at top level only — not inside parentheses (Form 4's Crisis lines
    field has a parenthetical with its own comma: "988 (Suicide & Crisis Lifeline —
    call or text)") and not inside *italic* or **bold** markup (Form 11's Gas meter
    field has an italic aside with its own commas: "and the rule written out — *only
    if I smell gas, hear it, see damage, or am told to.*" — an earlier draft split
    that aside into four garbled one-word fields and leaked the stray asterisks as
    literal text, because it only guarded parentheses)."""
    parts, cur = [], ""
    paren_depth = 0
    in_bold = in_italic = False
    pos = 0
    for m in SPLIT_TOKEN_RE.finditer(text):
        tok = m.group()
        if tok == sep and paren_depth == 0 and not in_bold and not in_italic:
            cur += text[pos:m.start()]
            parts.append(cur.strip())
            cur = ""
        else:
            cur += text[pos:m.end()]
            if tok == "(":
                paren_depth += 1
            elif tok == ")":
                paren_depth -= 1
            elif tok == "**":
                in_bold = not in_bold
            elif tok == "*":
                in_italic = not in_italic
        pos = m.end()
    cur += text[pos:]
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


def balanced_split(weights, k):
    """Split a sequence of per-item weights into k contiguous, ordered parts (item order
    never changes -- only where the page break falls), choosing whichever split minimizes
    the heaviest part. Splitting a multi-page form at a fixed item-count boundary (e.g.
    "first 3 groups, then the rest") assumes every item costs the same page space, which
    groups/trades plainly don't (Form 11's "Gas meter" group is three fields and an aside;
    its "Water heater" group is one line) -- that produced page 17: two fields on a page,
    three-quarters empty, while page 16 was packed (owner 2026-08-03). n and k are always
    small here (a handful of groups/trades, 2-3 pages), so brute-forcing every split-point
    combination is simplest and exact -- no need for a smarter algorithm at this size.
    Returns a list of k (start, end) index pairs into the original sequence."""
    n = len(weights)
    prefix = [0]
    for w in weights:
        prefix.append(prefix[-1] + w)
    best_cuts, best_max = None, None
    for cuts in combinations(range(1, n), k - 1):
        bounds = (0,) + cuts + (n,)
        sums = [prefix[bounds[i + 1]] - prefix[bounds[i]] for i in range(k)]
        if any(s <= 0 for s in sums):
            continue  # every page must carry at least one item
        worst = max(sums)
        if best_max is None or worst < best_max:
            best_max, best_cuts = worst, bounds
    return [(best_cuts[i], best_cuts[i + 1]) for i in range(k)]


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
    # The sentence wraps across several source lines (it's one prose paragraph in the
    # manuscript, not one physical line) — paragraph-join up to the next blank line
    # before extracting it, or only the first wrapped line was ever captured.
    for i, line in enumerate(lines[start:start + 20]):
        if line.startswith("Contents that earn their weight:"):
            para = [line]
            for cont in lines[start + i + 1:start + i + 10]:
                if not cont.strip():
                    break
                para.append(cont)
            sentence = " ".join(para).split(":", 1)[1].strip().rstrip(".")
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


def group_map(form):
    return {u["label"]: u["desc"] for u in units_of_type(form["units"], "group")}


def all_fields(form):
    out = []
    for u in units_of_type(form["units"], "fields"):
        out.extend(u["fields"])
    return out


# ---------------------------------------------------------------- 6. generic primitives

CHECKLIST_FORMS = {10, 34, 35}      # the spec's own wording: "...checklist"
GROUP_AS_CHECKLIST_FORMS = {24}     # "Five-minute list" / "Thirty-minute list" — items to
                                     # grab, not values to record, so a box reads better
                                     # than a blank line.


def build_groups_generic(form):
    groups = units_of_type(form["units"], "group")
    if form["number"] in GROUP_AS_CHECKLIST_FORMS:
        parts = []
        for g in groups:
            items = split_top(g["desc"].rstrip("."), ",")
            parts.append(f'<div class="bgroup"><h4>{render_inline(g["label"])}</h4>'
                         f'{render_checklist(items)}</div>')
        return "".join(parts)
    return render_groups(groups)


def build_table_per_form(form, rows):
    u = units_of_type(form["units"], "table_per")[0]
    lede = f'<p class="form-sub">One row per {esc(u["entity"])}.</p>'
    return lede + render_table(u["fields"], rows)


def build_form1(form):
    """Household roster. "One page, one row per person" names a table explicitly —
    rendering it as one set of vertical fields (the generic fallback) would only hold
    one person and leave most of the page blank. Eight rows covers most households
    with room to spare; no fixed household size is given anywhere in the binder."""
    return render_table(all_fields(form), 13)


def build_form22(form):
    """Fridge and freezer log. A log is inherently repeated entries (temperature
    checked more than once during an outage), so it's a table, not one-time fields."""
    return render_table(all_fields(form), 9)


def build_form28(form):
    """Alarm inventory. A household has several smoke/CO alarms — "inventory" is
    plural by nature — so each alarm is a table row rather than one shared set of
    fields for all of them."""
    return render_table(all_fields(form), 12)


def build_form37(form):
    """Mitigation credits. "Each qualifying upgrade" names a per-upgrade row; the
    carrier's own credit-table request date happens once, so it stands above the
    table rather than being folded into a column."""
    fields = all_fields(form)
    return render_field(fields[0]) + render_table(fields[1:], 9)


def build_form3(fields):
    """Animals (no pet count given in the spec). Two side-by-side blocks fit one page
    at book.css's field sizing; a household with more pets reuses a second blank copy
    of this page, the same way Form 2's spares work for people."""
    last = fields[-1]  # "the three phone numbers: pet-friendly shelter, boarding
                        # facility, out-of-area contact who would take them"
    label, _, detail = last.partition(":")
    subs = split_top(detail, ",") if detail else []
    tail = (f'<div class="bgroup"><h4>{render_inline(label.strip())}</h4>{render_fields(subs)}</div>'
            if subs else render_field(last))

    def one_animal(n):
        return (f'<div><p class="b-cont">Animal {n}</p>'
                f'{render_fields(fields[:-1], cls_hint="med")}{tail}</div>')

    return f'<div class="grid2">{one_animal(1)}{one_animal(2)}</div>'


def build_form4_pages(form):
    """The contact sheet. Custom rather than the generic groups primitive because two
    of its seven bold-labelled groups are themselves repeated-row tables (two local
    contacts, three neighbours) and one (Crisis lines) mixes a fixed fact (988) with
    a field the reader still has to look up and write in — none of that is expressible
    by the generic single-field-per-group renderer. Measured to overflow the page by
    ~500px as one page (fitcheck), so it splits at the natural boundary between the
    people/utilities groups and the services/crisis-line groups."""
    g = group_map(form)

    def whole(label):
        return f'{label} {g[label]}'.replace("  ", " ").rstrip(". ")

    page1 = ('<div class="bgroup"><h4>Out-of-area contact</h4>' +
             render_fields(split_top(g["Out-of-area contact"].lstrip(", "), ","), cls_hint="med") +
             '</div>' +
             f'<div class="bgroup"><h4>{esc(whole("Two local emergency contacts"))}</h4>' +
             render_table(["Name", "Relationship", "Phone"], 2, numbered=False) + '</div>' +
             f'<div class="bgroup"><h4>{esc(whole("Neighbours"))}</h4>' +
             render_table(["Name", "Phone", "Note — elderly, alone, disabled, medically dependent"],
                          3, numbered=False) + '</div>' +
             '<div class="bgroup"><h4>Utilities</h4>' +
             render_fields(split_top(g["Utilities"].rstrip("."), ","), cls_hint="med") + '</div>')
    # Split at the sentence's own ", and " boundary: the 988 line is a fixed fact to
    # print verbatim, the Disaster Distress Helpline is what the reader looks up and
    # writes in. An earlier draft paraphrased the 988 line instead of quoting it.
    crisis_fixed, _, crisis_fillin = g["Crisis lines"].partition(", and ")
    page2 = ('<div class="bgroup"><h4>Services</h4>' +
             render_fields(split_top(g["Services"].rstrip("."), ","), cls_hint="short") + '</div>' +
             render_field(whole("Your county's ten-digit emergency backup number")) +
             '<div class="bgroup"><h4>Crisis lines</h4>'
             f'<p class="small">{render_inline(crisis_fixed)}.</p>' +
             render_field(crisis_fillin.rstrip(".")) + '</div>')
    return [page1, page2]


def build_form6(form):
    g = group_map(form)
    body = (render_field(f'Near home: {g["Near home"].rstrip(".")}') +
            render_field(f'Out of area: {g["Out of area"].rstrip(".")}') +
            '<p class="b-serves"><strong>We have agreed: nobody goes back for anybody.</strong></p>' +
            render_signature(1))
    return body


def build_form7(form):
    """The trigger plan. "Rows for:" names the hazards as row LABELS, not column
    headers (see classify_unit) — each row completes "When [hazard] happens, we
    _____", so the hazard name is pre-filled and the reader only fills the response.
    A tight row height (see .btable.tight) is needed to fit all 14 rows plus the
    signature block on one page — this is "the single most important page in the
    binder" per the spec, so it does not get a second page to breathe into."""
    items = units_of_type(form["units"], "rows_for")[0]["items"]
    rows = "".join(
        f'<tr><td>{render_inline(item)}</td><td class="fill"></td></tr>' for item in items)
    table = (f'<table class="btable tight"><tr><th>When this happens</th>'
             f'<th>We will {D} without further discussion</th></tr>{rows}</table>')
    # Rendered from the parsed blockquote unit itself, not retyped -- an earlier draft
    # hand-typed this sentence, which happened to match but would have silently gone
    # stale if the spec's wording ever changed.
    note_text = units_of_type(form["units"], "note")[0]["text"]
    note = f'<p class="b-note">{render_inline(note_text)}</p>'
    # "a signature line for every adult, and a date" — the household size isn't
    # given anywhere in the binder, so three lines are offered (covers most
    # households; a larger one adds a line by hand, which costs nothing on a page
    # that is otherwise full).
    return note + table + render_signature(3)


def build_form8(form):
    """Region priority worksheet. "your ten protections in order" is an explicit
    count (also matches the ten-row table every packet already builds from the same
    front-matter data — see appendix/build.py's region_first_ten()), so the table is
    ten rows, not a guessed default."""
    body = (render_field("Your region or regions", cls_hint="med") +
            render_table(["Protection", "Done on"], 10))
    return body


def build_form9(form):
    """The vulnerability walk. Completed twice — once in heavy rain, once dry — so
    each question gets two answer columns rather than one, per the spec's own
    instruction, not a layout invented past it."""
    texts = units_of_type(form["units"], "text")
    questions = [q.strip() + "?" for q in texts[1]["text"].rstrip("?").split("?") if q.strip()]
    rows = "".join(
        f'<tr><td>{render_inline(q)}</td><td class="fill"></td><td class="fill"></td></tr>'
        for q in questions)
    return (f'<table class="btable tight" style="table-layout:auto">'
            f'<tr><th>{render_inline(texts[0]["text"])}</th><th>Heavy rain</th><th>Dry weather</th></tr>'
            f'{rows}</table>')


def build_form11_pages(form):
    """Shut-offs. Five groups as one page overflowed by ~140px (fitcheck), so it needs
    two pages -- but a fixed "first 3, then the rest" split put Water main + Gas meter +
    Breaker panel (11 fields between them) on page 1 and Water heater + Sprinklers/pool/
    well/septic (2 fields) on page 2, three-quarters empty (roomcheck, owner 2026-08-03).
    balanced_split() weighs each group by its own field count instead, so the split point
    follows the content rather than a fixed count."""
    groups = units_of_type(form["units"], "group")
    weights = [0.35 + (render_group_desc(g["desc"]).count('<div class="field">') or 1)
               for g in groups]
    (a0, a1), (b0, b1) = balanced_split(weights, 2)
    page1 = render_groups(groups[a0:a1])
    page2 = render_groups(groups[b0:b1])
    return [page1, page2]


def build_form14_pages(form):
    """The contractor list. Each **Trade:** group's "·"-separated items become rows
    under a trade sub-header, and the trailing "Each row: requested · quoted · done ·
    documentation filed." sentence supplies the status columns every row gets. All 21
    items in one table overflowed the page by ~200px (fitcheck), so it needs two pages
    — split at a trade boundary (never mid-trade), chosen by balanced_split() weighing
    each trade by its own item count (Roofer's 7 items are not the same page weight as
    HVAC's 3), rather than a fixed "first 3 trades" cut."""
    trades = units_of_type(form["units"], "group")
    status_fields = form["units"][-1]["fields"]  # ['Each row: requested','quoted','done','documentation filed']
    if status_fields[0].split(":")[0].strip() != "Each row":
        sys.exit("FAIL: Form 14's trailing status-column sentence moved or was reworded.")
    status_cols = [status_fields[0].split(":")[-1].strip()] + status_fields[1:]

    def trade_table(subset):
        ths = "<th>Item</th>" + "".join(f"<th>{esc(c.title())}</th>" for c in status_cols)
        rows = [f"<tr>{ths}</tr>"]
        for t in subset:
            items = t["desc"].rstrip(".").split("·")
            rows.append(f'<tr><td class="trade-head" colspan="{len(status_cols) + 1}">'
                        f'{render_inline(t["label"])}</td></tr>')
            for item in items:
                tds = f"<td>{render_inline(item.strip())}</td>" + "<td></td>" * len(status_cols)
                rows.append(f"<tr>{tds}</tr>")
        return f'<table class="btable tight" style="table-layout:auto">{"".join(rows)}</table>'

    weights = [0.3 + len(t["desc"].rstrip(".").split("·")) for t in trades]
    (a0, a1), (b0, b1) = balanced_split(weights, 2)
    return [trade_table(trades[a0:a1]), trade_table(trades[b0:b1])]


def build_form15(form):
    """Structural protections progress. "Sixteen rows...for: A · B · C" gives both an
    explicit row count and the column list in one sentence; the sixteen protection
    numbers are Serves 69-84 from this same form's byline, not a re-typed list."""
    fields = all_fields(form)
    first = fields[0].split(":")[-1].strip()  # "...columns for: applies to me" -> "applies to me"
    columns = ["Protection", first] + fields[1:]
    return render_table(columns, 16, prefill_col0=list(range(69, 85)), numbered=False)


def build_form16(form):
    """Maintenance calendar. "Monthly, seasonal and annual: A · B · ..." lists the
    ROWS (ten tasks), each checked off under whichever cadence applies — this is the
    "Rows for:" shape (see Form 7) under different wording, so it's handled the same
    way rather than as ten flat fields."""
    fields = all_fields(form)
    first = fields[0].split(":")[-1].strip()
    tasks = [first] + fields[1:]
    rows = "".join(
        f'<tr><td>{render_inline(t)}</td><td class="box-cell"><span class="box"></span></td>'
        f'<td class="box-cell"><span class="box"></span></td><td class="box-cell"><span class="box"></span></td>'
        f'<td class="fill"></td></tr>' for t in tasks)
    return (f'<table class="btable tight" style="table-layout:auto">'
            f'<tr><th>Task</th><th>Monthly</th><th>Seasonal</th><th>Annual</th><th>Last done</th></tr>'
            f'{rows}</table>')


def build_form17(form):
    """Water sizing and store. The formula sentence becomes four short blanks feeding
    one big result blank; "Then a store log: A, B, C, D" names the log's own columns."""
    texts = units_of_type(form["units"], "text")
    formula = ('<div class="field"><label>People &times; gallons per day &times; days, '
               'plus animals</label><div class="line"></div></div>'
               '<div class="field"><label>Your number (total gallons to store)</label>'
               '<div class="line"></div></div>')
    log_cols = texts[1]["text"].split(":", 1)[1].rstrip(".").split(",")
    return formula + render_table([c.strip() for c in log_cols], 6)


def build_form18(form):
    """The pre-fill list. "In order:" makes this a sequence, not a checkbox set — the
    reader still has to write which tub/pot/bottle, so each item gets a numbered
    fill-line rather than a tick-box."""
    text = units_of_type(form["units"], "text")[0]["text"]
    items = split_top(text.split(":", 1)[1].rstrip("."), ",")
    items[-1] = re.sub(r"^and\s+", "", items[-1])
    lis = "".join(
        f'<div class="field"><label><span class="bn">{i}.</span> {render_inline(item)}</label>'
        f'<div class="line"></div></div>'
        for i, item in enumerate(items, start=1))
    return lis


def build_form20(form):
    """The no-cook pantry. "Fourteen-day list" is an explicit row count; "the deep-
    pantry additions" is a second, shorter table for longer-life stock the fourteen-day
    rotation doesn't cover — column names (item/quantity/expiry) are the spec's own
    "quantities and expiry dates," not invented."""
    return (render_table(["Item", "Quantity", "Expiry date"], 14) +
            '<p class="b-cont">Deep-pantry additions</p>' +
            render_table(["Item", "Quantity", "Expiry date"], 5, numbered=False))


def build_form23(form):
    """Go-bag contents, per person. The spec names "Standard contents checklist" but
    does not itemise it here — the itemised list lives under Protection 107 in Part
    Five (see standard_gobag_items()), parsed from there rather than left blank."""
    items = standard_gobag_items()
    return (render_checklist(items) +
            '<p class="b-cont">Person-specific additions</p>' +
            render_table(["Item"], 5, numbered=False) +
            render_field("Size and season check date", cls_hint="short"))


def build_form25(form):
    """The power priority list. "One row per load, in priority order" names no fixed
    count — eight rows is a working household's typical load list (fridge, well pump,
    furnace fan, medical device, router, a few lights/chargers...) with the total row
    the spec calls for underneath."""
    fields = all_fields(form)
    first = fields[0].split(":")[-1].strip()
    cols = [first] + fields[1:]
    return (render_table(cols, 8) +
            '<div class="btotal"><span>Total watts to size against</span>'
            '<span class="b-blank"></span></div>')


def build_form30(form):
    """Route two. The spec literally says "Same fields" — Form 29's own field list is
    reused rather than retyped a second time, plus the one thing this form adds: the
    no-shared-bottleneck caveat, carried forward as a note since it's the one way
    Route two must differ from Route one."""
    form29 = next(f for s in PARSED_SECTIONS for f in s["forms"] if f["number"] == 29)
    fields = all_fields(form29)
    caveat = next(u["label"] for u in units_of_type(form["units"], "group"))
    return render_fields(fields) + f'<p class="b-note">{render_inline(caveat)}</p>'


def build_form36_pages(form):
    """The insurance audit. Dense enough (five identity fields plus eleven bold-
    labelled money/coverage groups) that one page cannot hold it at a legible size.
    A 2-page split (policy identity + limits/deductibles, then exclusions/sub-limits/
    separate policies) still overflowed both pages by ~115px each (fitcheck), so it
    splits into 3 at group boundaries instead of shrinking type or clipping content."""
    g = group_map(form)
    top_fields = units_of_type(form["units"], "fields")[0]["fields"]
    page1 = (render_fields(top_fields, cls_hint="med") +
            render_group("Dwelling limit", g["Dwelling limit"]) +
            render_group("Contents limit", g["Contents limit"]))
    page2 = (render_group("Deductibles", g["Deductibles"]) +
            render_group("Roof settlement basis", g["Roof settlement basis"]) +
            render_group("Loss of use", g["Loss of use"]) +
            render_group("Exclusions confirmed", g["Exclusions confirmed"]))
    texts = units_of_type(form["units"], "text")
    question = " ".join(t["text"] for t in texts)
    page3 = (render_group("Sub-limits", g["Sub-limits"]) +
            render_group("Separate policies", g["Separate policies"]) +
            f'<p class="b-note">{render_inline(question)}</p>' +
            render_field("Answer", cls_hint=""))
    return [page1, page2, page3]


def build_form38(form):
    """The gap worksheet. Each "difference" sentence is Your number / Policy number /
    Difference — rendered as a three-column row rather than three unrelated blanks, so
    the arithmetic the spec is asking for is visually obvious. "Difference" is itself
    just a column header, not a fourth value to fill in per row — an earlier draft
    printed the word "difference" as a label AND swallowed the contents-value row's
    real fourth field (its actual-cash-value note) into that same slot by assuming
    every triple has exactly 3 fields; the contents row has 4, so it's handled as its
    own extra note line instead of a column every other row would carry empty."""
    triples = units_of_type(form["units"], "fields")
    rows = []
    for t in triples:
        f = t["fields"]
        rows.append(f'<tr><td>{render_inline(f[0])}</td><td class="fill"></td>'
                    f'<td>{render_inline(f[1])}</td><td class="fill"></td>'
                    f'<td class="fill"></td></tr>')
        if len(f) > 3:  # the contents row alone carries an ACV-adjustment note
            rows.append(f'<tr><td colspan="5" class="small">{render_inline(f[2])}'
                        f'<span class="b-blank"></span></td></tr>')
    table = (f'<table class="btable" style="table-layout:auto">'
            f'<tr><th>Your number</th><th></th><th>Policy provides</th><th></th>'
            f'<th>Difference</th></tr>{"".join(rows)}</table>')
    texts = units_of_type(form["units"], "text")
    ded = next(t["text"] for t in texts if t["text"].startswith("Deductibles"))
    fed = next(t["text"] for t in texts if t["text"].startswith("Then: what federal"))
    final_group = units_of_type(form["units"], "group")[0]["label"]
    return (table + render_field(ded.rstrip(".")) + f'<p class="small">{render_inline(fed)}</p>' +
            render_field("Honest total") +
            f'<p class="b-serves"><strong>{render_inline(final_group)}</strong></p>')


def build_form39_pages(form):
    """Home inventory log. Six pages, explicit in the spec ("Six pages"). Five carry
    the room-by-room log (nine columns, so a small tight table); the sixth is the
    separate high-value schedule the spec names as "then," a distinct list with its
    own three columns rather than more rows of the main log."""
    main_fields = units_of_type(form["units"], "fields")[0]["fields"]
    log_pages = []
    for _ in range(5):
        log_pages.append(render_table(main_fields, 11, tight=True))
    hv_fields = units_of_type(form["units"], "fields")[1]["fields"]
    hv_fields = [hv_fields[0].split(":")[-1].strip()] + hv_fields[1:]
    log_pages.append('<p class="form-sub">The high-value schedule.</p>' +
                     render_table(hv_fields, 16, tight=True))
    return log_pages


def build_form41_pages(form):
    """The claim log. Four pages, explicit in the spec ("Four pages"), and it already
    names four distinct logs (call / expense / mitigation / discard) plus the claim's
    own identity fields — one log per page is the spec's own structure, not a layout
    invented for it."""
    ident = units_of_type(form["units"], "fields")[0]["fields"]
    texts = units_of_type(form["units"], "text")
    page1 = render_fields(ident, cls_hint="med") + '<p class="b-cont">Call log</p>' + \
        render_table([c.strip() for c in texts[0]["text"].split(":", 1)[1].rstrip(".").split(",")], 9, tight=True)
    page2 = render_table([c.strip() for c in texts[1]["text"].split(":", 1)[1].rstrip(".").split(",")], 12)
    page3 = render_table([c.strip() for c in texts[2]["text"].split(":", 1)[1].rstrip(".").split(",")], 11)
    page4 = render_table([c.strip() for c in texts[3]["text"].split(":", 1)[1].rstrip(".").split(",")], 11)
    return [page1, page2, page3, page4]


# Forms whose page repeats are identical copies of the same blank template — the spec
# says so explicitly for Form 2 ("Four pages -- one per person, plus spares"). Form 23
# has no stated count of its own ("One page per person" -- no number), so it borrows
# Form 2's count for the same household rather than a second hardcoded 4 -- see
# _parse_page_count() below, called once PARSED_SECTIONS exists (main()), and
# build_form23()'s own "photocopy as needed" line, which tells the reader the count is
# borrowed, not sourced for Form 23 itself.
FORM_REPEAT = {2: 4}

_WORD_NUMS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6}


def _parse_page_count(serves_raw):
    """Pulls the page count out of a form's own "Serves ... <Number> pages" byline
    (Form 2: "Four pages -- one per person, plus spares.") so a count another form
    borrows traces to the sentence that actually states it, not a bare integer typed
    twice in code."""
    m = re.search(r"\b(One|Two|Three|Four|Five|Six)\s+pages?\b", serves_raw)
    if not m:
        sys.exit(f"FAIL: expected an explicit '<Number> pages' phrase in: {serves_raw!r}")
    return _WORD_NUMS[m.group(1).lower()]


# Forms with their own multi-page builder (each page's content differs, so the builder
# returns the full list rather than main() repeating one page N times). 4, 11, 14 and 36
# started as single-page builders and were moved here once fitcheck measured them
# overflowing the page box — see each builder's own docstring for the measured amount.
MULTI_PAGE_BUILDERS = {
    4: build_form4_pages, 11: build_form11_pages, 14: build_form14_pages,
    36: build_form36_pages, 39: build_form39_pages, 41: build_form41_pages,
}

# A form with only a handful of fields/rows still gets book.css's normal fixed spacing,
# tuned for a *full* page -- so a short form can leave most of its page blank even
# though nothing about it is wrong. roomcheck.mjs flagged 12 such single pages plus 2
# multi-page forms whose split dumped the remainder onto an under-filled page
# (2026-08-03). The owner's rule, refined after a first pass overshot it: this is a
# CEILING, not a fill target -- grow each write-in row up to roughly 0.55in total
# (label + line + margin, or one table/checklist row) and stop there, even if the page
# still shows white below. A short reference form that hits that ceiling with room to
# spare is finished, not defective -- it is reported below, not chased further.
# ROOMY_FIELD_PT / ROOMY_ROW_PT / ROOMY_CHECK_PT are that ceiling's headroom above each
# component's own book.css/binder.css baseline (~36pt for a plain field, ~33pt inside a
# .bgroup, ~25pt for a table row, ~21pt for a checklist item -- see binder.css's own
# component rules), i.e. the most any page here is allowed to grow a row by:
ROOMY_FIELD_PT = 4      # plain .field (label + line + 10pt margin)
ROOMY_FIELD_GROUP_PT = 7   # .bgroup .field (7pt margin instead of 10pt -- more headroom)
ROOMY_ROW_PT = 15       # .btable td (normal or .tight -- same ceiling, different base)
ROOMY_CHECK_PT = 19     # .bcheck

# Which forms get which ceiling(s). A form only appears here if roomcheck.mjs measured
# genuine spare room on that exact page -- this never overrides a form (like Form 7's
# tight 14-row page) that already needs its whole page and was never flagged.
ROOMY_EXTRA = {
    5: {"row": ROOMY_ROW_PT}, 9: {"row": ROOMY_ROW_PT}, 17: {"field": ROOMY_FIELD_PT, "row": ROOMY_ROW_PT},
    18: {"field": ROOMY_FIELD_PT}, 19: {"field": ROOMY_FIELD_PT}, 26: {"field": ROOMY_FIELD_PT},
    29: {"field": ROOMY_FIELD_PT}, 32: {"field": ROOMY_FIELD_PT}, 33: {"row": ROOMY_ROW_PT},
    34: {"check": ROOMY_CHECK_PT}, 38: {"field": ROOMY_FIELD_PT, "row": ROOMY_ROW_PT},
    40: {"field": ROOMY_FIELD_PT},
}
# Multi-page forms: both pages get the same ceiling (it's a per-row cap, not a per-page
# tuned target), EXCEPT where the ceiling itself would overflow the page -- Form 14's
# 13-to-15-row tables have less spare room per page than the 15pt table ceiling needs,
# so it's capped lower (10pt) there; Form 11's field ceiling (group context) is well
# under either page's spare room, so it applies at full value on both.
ROOMY_EXTRA_PAGES = {
    11: [{"field": ROOMY_FIELD_GROUP_PT}] * 2,
    14: [{"row": 10}] * 2,
}


def roomy(body_html, extras):
    style = "; ".join(f"--extra-{k}:{v}pt" for k, v in extras.items())
    return f'<div class="roomy" style="{style}">{body_html}</div>'


def build_form2(form):
    """Medical summary. Thirteen fields plus the "stranger providing care" note (see
    the build_form() dispatch note on why that note was almost dropped) push a one-
    page copy right to the edge -- fitcheck measured +21px once the note was restored.
    Tightened field spacing here only, rather than loosening the shared .field
    component everywhere else in the binder that already fits with headroom to spare."""
    fields = all_fields(form)
    note_text = units_of_type(form["units"], "note")[0]["text"]
    return (f'<div class="tight-fields">{render_fields(fields)}</div>'
            f'<p class="b-note">{render_inline(note_text)}</p>')


def build_form(form):
    """Returns a list of page-body HTML fragments for one form (usually length 1)."""
    n = form["number"]
    if n in MULTI_PAGE_BUILDERS:
        pages = MULTI_PAGE_BUILDERS[n](form)
        extras = ROOMY_EXTRA_PAGES.get(n)
        if extras:
            pages = [roomy(p, e) for p, e in zip(pages, extras)]
        return pages
    single = {
        1: lambda: build_form1(form),
        2: lambda: build_form2(form),
        3: lambda: build_form3(all_fields(form)),
        6: lambda: build_form6(form),
        7: lambda: build_form7(form),
        8: lambda: build_form8(form),
        9: lambda: build_form9(form),
        15: lambda: build_form15(form),
        16: lambda: build_form16(form),
        17: lambda: build_form17(form),
        18: lambda: build_form18(form),
        20: lambda: build_form20(form),
        22: lambda: build_form22(form),
        23: lambda: build_form23(form),
        25: lambda: build_form25(form),
        28: lambda: build_form28(form),
        30: lambda: build_form30(form),
        37: lambda: build_form37(form),
        38: lambda: build_form38(form),
    }.get(n)
    if single:
        body = single()
    else:
        if n == 5:
            body = build_table_per_form(form, rows=6)
        elif n == 33:
            body = build_table_per_form(form, rows=5)
        elif any(u["type"] == "group" for u in form["units"]):
            body = build_groups_generic(form)
        elif n in CHECKLIST_FORMS:
            body = render_checklist(all_fields(form))
        else:
            body = render_fields(all_fields(form))
        # A blockquote in the spec is a note to the reader (per the brief) and must
        # reach the page even on a form that otherwise takes a generic layout path --
        # Form 2's "This is the page a stranger providing care needs..." was silently
        # dropped here until this line existed, because none of the generic branches
        # above ever looked at a form's 'note' units. Bespoke `single` builders own
        # their own notes already (Form 7 inlines its "When ___ happens" line), so
        # this only runs for the generic branch, never twice.
        for note in units_of_type(form["units"], "note"):
            body += f'<p class="b-note">{render_inline(note["text"])}</p>'

    if n in ROOMY_EXTRA:
        body = roomy(body, ROOMY_EXTRA[n])
    repeat = FORM_REPEAT.get(n, 1)
    return [body] * repeat


# ---------------------------------------------------------------- 7. the front sheet

def parse_front_sheet(lines):
    rows = []
    final_quote = ""
    for line in lines:
        s = line.strip()
        if not s:
            continue
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if all(re.fullmatch(r"-+", c) for c in cells if c) or not any(cells):
                continue
            if len(cells) == 2:
                rows.append(cells)
        elif s.startswith(">"):
            final_quote += (" " if final_quote else "") + s.lstrip(">").strip()
    return rows, final_quote


def render_front_sheet(rows, final_quote):
    trs = []
    for q, a in rows:
        cls = "a blank" if "_" in a else "a"
        trs.append(f'<tr><td class="q">{render_inline(q)}</td><td class="{cls}">{render_inline(a)}</td></tr>')
    body = ('<h2 class="form-title">The binder, at a glance</h2>'
            '<p class="form-sub">Filled in last — every answer here is completed somewhere else in the '
            'binder first.</p>'
            f'<table class="bfs-table">{"".join(trs)}</table>'
            f'<p class="bfs-final">{render_inline(final_quote)}</p>')
    return (f'<section class="page">\n<p class="runhead"><span>The Binder</span>'
            f'<span>The front sheet</span></p>\n{body}\n<p class="folio">1</p>\n</section>')


# ---------------------------------------------------------------- 8. document assembly

def document(body):
    """Self-contained: book.css + binder.css inlined, so out/binder.html can be opened
    or fitchecked on its own, the same way appendix/build.py's document() works."""
    css = []
    for path in (BOOK_CSS, BINDER_CSS):
        if not path.exists():
            sys.exit(f"FAIL: stylesheet {path} is missing.")
        css.append(f"/* {path.name} */\n{path.read_text(encoding='utf-8')}")
    return ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<title>The Storm-Ready Home — The Binder</title>\n<style>\n" + "\n".join(css) +
            f"\n</style>\n</head>\n<body>\n{body}\n</body>\n</html>\n")


def main():
    global PARSED_SECTIONS
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="parse and report, no HTML written")
    parser.add_argument("--build", action="store_true", help="write out/binder.html")
    args = parser.parse_args()
    if not (args.check or args.build):
        parser.error("nothing to do -- pass --check or --build")

    sections, front_sheet_lines = parse_manuscript()
    PARSED_SECTIONS = sections
    for s in sections:
        for f in s["forms"]:
            classify_form(f)

    total_forms = sum(len(s["forms"]) for s in sections)
    if len(sections) != 7:
        sys.exit(f"FAIL: found {len(sections)} sections, expected 7.")
    if total_forms != 41:
        sys.exit(f"FAIL: found {total_forms} forms, expected 41.")

    fs_rows, fs_quote = parse_front_sheet(front_sheet_lines)
    if not fs_rows or not fs_quote:
        sys.exit("FAIL: the one-page front sheet did not parse "
                 f"(rows={len(fs_rows)}, quote={'yes' if fs_quote else 'no'}).")

    pages = [render_front_sheet(fs_rows, fs_quote)]
    total_budget = sum(s["budget"] for s in sections)
    report_lines = [f"1 front sheet page (not counted against the 80-page section budget)"]

    for s in sections:
        section_pages = 0
        for f in s["forms"]:
            bodies = build_form(f)
            n_pages = len(bodies)
            for i, body in enumerate(bodies):
                cont = None
                if n_pages > 1:
                    cont = "continued" if i > 0 else None
                head = form_head(f["title"], f["serves_raw"], cont_label=cont)
                folio = len(pages) + 1  # 1-based, own-page numbering (paginate.mjs
                                        # replaces this with the book sequence, exactly
                                        # like the Appendix B splice)
                pages.append(page_shell(s["letter"], s["title"],
                                        f"Form {f['number']}", head, body, folio))
                section_pages += 1
        gap = section_pages - s["budget"]
        report_lines.append(
            f"Section {s['letter']} — {s['title']}: {section_pages} pages "
            f"(budget {s['budget']}, {'+' if gap >= 0 else ''}{gap})")
        total_budget -= 0  # (kept for clarity: budget already summed above)

    total_pages = len(pages) - 1  # exclude the front sheet from the 80-page comparison
    print(f"{len(sections)} sections, {total_forms} forms")
    for line in report_lines:
        print(f"  {line}")
    print(f"\n{len(pages)} binder pages total ({total_pages} forms pages + 1 front sheet), "
          f"vs. the stated 80-page target ({total_pages - 80:+d})")

    if args.check:
        return

    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / "binder.html"
    target.write_text(document("\n".join(pages)), encoding="utf-8")
    print(f"\nwrote {target}")


if __name__ == "__main__":
    main()
