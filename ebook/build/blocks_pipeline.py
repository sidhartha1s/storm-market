#!/usr/bin/env python3
"""Flatten the 41 manuscript files into a stream of block-level HTML elements, in book
reading order, for paginate.mjs to lay out into fixed 6x9 pages.

Reuses review_pdf.py's markdown parser (render_markdown), inline formatting, and citation
handling (SOURCES / _SEEN / CITE_RE) as a library rather than writing a second parser — see
the docstring on render_markdown for why that matters (citation numbering and the Sources
chapter would drift between two implementations). ORDER also comes from review_pdf.py: it
is the one place book reading order is recorded, and it must not be duplicated here.

This script owns exactly one thing review_pdf.py does not do: emitting the Sources chapter
as one block per reference instead of one flowing <ol>. review_pdf.py's Sources chapter is
a single continuous list relying on the browser's <ol> counter (fine for one long review
PDF) — but a fixed-page book chops the Sources chapter across many separate pages, and an
<ol> split across page boundaries loses its shared counter. So each reference here prints
its own number as text.

Usage: python3 blocks_pipeline.py > blocks.json
Output: a JSON array of {html, tag, file, part, chapterTitle, fileStart, heading}.
  - fileStart: true on the first block of each manuscript file (and of the synthetic
    "SOURCES" file) — paginate.mjs forces a new page there (chapter/part opener rule).
  - heading: true for h1-h4 blocks and for the Sources chapter's per-chapter subheads —
    paginate.mjs never leaves one of these as the last element on a page.
"""
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import review_pdf as rp  # noqa: E402

try:
    import figures  # noqa: E402  — provides render_figure(fig_id); may not exist yet
except ImportError:
    figures = None

# Matches every file title in the manuscript: "Part Two, Chapter One — Water",
# "Part Three, Playbook 1 — Tornado", "Part Six — The Binder". Used to split the
# file-opening h1 into a small uppercase kicker ("PART TWO, CHAPTER ONE") plus the large
# title line, the way a real chapter opener is set — book.css has no ready-made component
# for this (sample.html hand-set each one), so paginate.mjs supplies a small generic
# .chapter-open style instead.
TITLE_RE = re.compile(r"^(Part [A-Za-z]+(?:, (?:Chapter|Playbook) [A-Za-z0-9]+)?)\s*—\s*(.+)$")


def short_title(h1_text):
    """'Part Two, Chapter One — Water' -> 'Water'. Used as the folio label."""
    return h1_text.rsplit("—", 1)[-1].strip() if "—" in h1_text else h1_text


def chapter_opener_html(title):
    """Re-render a file's title heading as a kicker + title pair instead of the plain
    <h1> render_markdown produces, so an auto-laid chapter opener carries some of the
    hierarchy sample.html's hand-set openers have. Falls back to a plain <h1> if a title
    ever doesn't match the "Part X [, Chapter Y] — Title" convention."""
    m = TITLE_RE.match(title)
    if not m:
        return f"<h1 class=\"chapter-open\">{rp.inline(title)}</h1>"
    kicker, main = m.group(1).upper(), m.group(2)
    return (f'<h1 class="chapter-open"><span class="kicker">{rp.inline(kicker)}</span>'
            f"{rp.inline(main)}</h1>")


def part_of(filename):
    return filename.split("-", 1)[0]  # 'P0', 'P1', ... 'P7'


def tag_of(block_html):
    """First tag name, ignoring any attributes (chapter-opener h1s carry a class)."""
    if not block_html.startswith("<"):
        return "p"
    return block_html[1:block_html.index(">")].split()[0]


LI_RE = re.compile(r"<li>(.*?)</li>", re.S)


def explode_lists(block_list):
    """Split every <ul>/<ol> block into one block per <li>.

    Tables, figures and the numbered-protection blocks must never split across a page
    (task brief); plain bulleted/numbered lists are not on that list, and several hazard
    playbooks have a "Before" list of ten-plus prioritized protections that is taller than
    a whole page by itself — kept as one opaque block it can never be placed at all. A list
    item is a complete, self-contained unit like a paragraph, so splitting between items
    carries none of the widow/orphan risk a mid-paragraph split would.

    Each <li> becomes its own bare <li> block (no <ul>/<ol> wrapper) — Chrome applies
    `display:list-item` to <li> regardless of its parent, so it still renders as a list
    item; book-auto.css supplies the bullet/number and indent that a real <ul>/<ol> parent
    would otherwise provide. This also sidesteps the alternative (re-opening/closing a
    <ul>...</ul> wrapper on whichever page a split lands on, and re-numbering an <ol> with
    a `start=`) for no real benefit, since a bare <li> needs neither.
    """
    out = []
    for block_html in block_list:
        tag = tag_of(block_html)
        if tag not in ("ul", "ol"):
            out.append(block_html)
            continue
        items = LI_RE.findall(block_html)
        for n, inner in enumerate(items, start=1):
            if tag == "ol":
                out.append(f'<li class="li-bare li-ol"><span class="li-num">{n}.</span> {inner}</li>')
            else:
                out.append(f'<li class="li-bare li-ul">{inner}</li>')
    return out


FIG_RE = re.compile(r"^<p>«FIG:\s*([\w-]+)\s*»</p>$")


def resolve_figures(block_list, filename):
    """Replace a bare <p>«FIG: fig-id»</p> block — its own paragraph, blank lines around,
    per the figures agent's marker convention (matching how «SRC:»/«CITE:» work) — with
    figures.render_figure(fig_id)'s HTML.

    Fails loud rather than leaving the marker in the rendered book or silently dropping the
    figure: an unresolved marker reaching a reader's page is exactly the «CITE:» leak this
    manuscript has been burned by once already (see manuscript/README.md). Each figure's
    <svg> carries its own fixed height (the figures agent's convention, matching sample.html),
    so it measures deterministically like any other block — no special-casing needed here
    beyond the substitution itself; tag_of() reads it as a plain <figure> block, which is
    atomic by default, matching the brief's "figures ... atomic" rule."""
    out = []
    for block_html in block_list:
        m = FIG_RE.match(block_html)
        if not m:
            out.append(block_html)
            continue
        fig_id = m.group(1)
        if figures is None:
            sys.exit(f"FAIL: {filename} references «FIG: {fig_id}» but build/figures.py does not exist yet.")
        if not hasattr(figures, "render_figure"):
            sys.exit(f"FAIL: build/figures.py has no render_figure() — needed for {filename}'s «FIG: {fig_id}»")
        try:
            out.append(figures.render_figure(fig_id))
        except Exception as e:
            sys.exit(f"FAIL: {filename}'s «FIG: {fig_id}» could not be rendered: {e}")
    return out


def assign_groups(tags):
    """Group index per block: every h3 opens a new group that also covers every block up
    to (not including) the next h1/h2/h3. None outside any h3's span.

    The brief calls out "the numbered-protection blocks" as atomic — never split across
    pages — alongside tables and figures. In this manuscript that is exactly what an h3
    marks: the 130 "### N · Name" protection entries in Part Two and Part Five, the 41
    "### Form N" entries in the Binder, and the six "### phase" subheads in the timeline
    chapter. All of them are a self-contained unit a reader looks up by number/name, so
    the same atomicity is applied uniformly rather than pattern-matching the "### N ·"
    numbering specifically. h1/h2 keep the narrower "heading not last on a page" check in
    paginate.mjs instead of full-group atomicity — grouping a whole h2 section (which can
    contain a 10-item list already taller than a page) would just recreate the oversized-
    block problem explode_lists exists to solve."""
    groups = [None] * len(tags)
    gid = None
    for i, tag in enumerate(tags):
        if tag == "h3":
            gid = i  # group id = the h3's own index; unique and stable
        elif tag in ("h1", "h2"):
            gid = None
        groups[i] = gid
    return groups


def main():
    missing = [name for name in rp.ORDER if not (rp.MS / name).exists()]
    if missing:
        sys.exit("FAIL: missing manuscript files:\n  " + "\n  ".join(missing))

    blocks = []
    for name in rp.ORDER:
        text = (rp.MS / name).read_text(encoding="utf-8")
        title = text.split("\n", 1)[0].lstrip("# ").strip()
        rp._CURRENT_CHAPTER[0] = title
        file_blocks = rp.render_markdown(text)
        file_blocks[0] = chapter_opener_html(title)  # plain <h1> -> kicker + title
        file_blocks = explode_lists(file_blocks)
        tags = [tag_of(bh) for bh in file_blocks]
        groups = assign_groups(tags)
        for i, block_html in enumerate(file_blocks):
            blocks.append({
                "html": block_html,
                "tag": tags[i],
                "file": name,
                "part": part_of(name),
                "chapterTitle": short_title(title),
                "fileStart": i == 0,
                "heading": tags[i] in ("h1", "h2", "h3", "h4"),
                "group": (f"{name}#{groups[i]}" if groups[i] is not None else None),
            })

    # ---- Sources chapter, one block per reference (see module docstring) ----
    blocks.append({
        "html": '<h1 class="chapter-open"><span class="kicker">BACK MATTER</span>Sources</h1>',
        "tag": "h1", "file": "SOURCES", "part": "SOURCES",
        "chapterTitle": "Sources", "fileStart": True, "heading": True,
    })

    resolved = sum(1 for *_, ok in rp.SOURCES if ok)
    pending = len(rp.SOURCES) - resolved
    if pending:
        meta = (f'<p class="meta">{len(rp.SOURCES)} numbered references: <strong>{resolved} carry a full '
                f'citation and a retrieval date</strong>, and <strong>{pending} are still pending</strong> '
                'and marked as such. Every pending entry is either replaced with a primary document or the '
                'claim is cut from the book.</p>')
    else:
        meta = (f'<p class="meta">{len(rp.SOURCES)} numbered references, <strong>every one carrying a full '
                'citation and a retrieval date</strong>. Where a claim could not be traced to a primary '
                'document it was cut rather than softened.</p>')
    blocks.append({"html": meta, "tag": "p", "file": "SOURCES", "part": "SOURCES",
                   "chapterTitle": "Sources", "fileStart": False, "heading": False})

    last_chapter = None
    for number, (chapter, text, ok) in enumerate(rp.SOURCES, start=1):
        if chapter != last_chapter:
            blocks.append({
                "html": f'<p class="src-ch">{html.escape(chapter)}</p>', "tag": "p",
                "file": "SOURCES", "part": "SOURCES", "chapterTitle": "Sources",
                "fileStart": False, "heading": True,
            })
            last_chapter = chapter
        item = html.escape(text)
        for pattern, repl in rp.INLINE:
            item = pattern.sub(repl, item)
        cls = "ref-item" if ok else "ref-item pending"
        blocks.append({
            "html": f'<p class="{cls}"><span class="refnum">{number}.</span> {item}</p>',
            "tag": "p", "file": "SOURCES", "part": "SOURCES", "chapterTitle": "Sources",
            "fileStart": False, "heading": False,
        })

    for b in blocks:
        b.setdefault("group", None)  # Sources-chapter blocks carry no h3 group

    print(json.dumps(blocks))


if __name__ == "__main__":
    main()
