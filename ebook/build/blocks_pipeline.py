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

# Matches every file title in the manuscript: "Part Two, Chapter One — Water",
# "Part Six — The Binder". Used to split the file-opening h1 into a small uppercase
# kicker ("PART TWO, CHAPTER ONE") plus the large title line, the way a real chapter
# opener is set — book.css has no ready-made component for this (sample.html hand-set
# each one), so paginate.mjs supplies a small generic .chapter-open style instead.
TITLE_RE = re.compile(r"^(Part [A-Za-z]+(?:, Chapter [A-Za-z]+)?)\s*—\s*(.+)$")


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
    return block_html[1:block_html.index(">")] if block_html.startswith("<") else "p"


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
        for i, block_html in enumerate(file_blocks):
            blocks.append({
                "html": block_html,
                "tag": tag_of(block_html),
                "file": name,
                "part": part_of(name),
                "chapterTitle": short_title(title),
                "fileStart": i == 0,
                "heading": tag_of(block_html) in ("h1", "h2", "h3", "h4"),
            })

    # ---- Sources chapter, one block per reference (see module docstring) ----
    blocks.append({"html": "<h1>Sources</h1>", "tag": "h1", "file": "SOURCES", "part": "SOURCES",
                   "chapterTitle": "Sources", "fileStart": True, "heading": True})

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

    print(json.dumps(blocks))


if __name__ == "__main__":
    main()
