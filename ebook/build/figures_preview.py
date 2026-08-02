#!/usr/bin/env python3
"""figures_preview.py — render every figure in figures.py onto its own fixed 6x9 page,
so the whole set can be eyeballed and fitchecked without a full book build.

Usage: python3 figures_preview.py   ->  writes out/figures.html

Each page carries the real <figure> HTML exactly as render_figure() produces it, plus a
review-only header (figure id, protection cross-reference, one-line justification) so a
reviewer can check "does this earn its place" against the actual prose reference without
opening the manuscript file. That review header is preview-harness scaffolding — it is not
part of what ships in the book.
"""
import html
from pathlib import Path

from figures import FIGURES, render_figure

HERE = Path(__file__).parent
OUT = HERE / "out" / "figures.html"

PAGE_TEMPLATE = '''<section class="page">
  <div class="runhead"><span>Figure preview &middot; {fig_id}</span><span>Protection {protection}</span></div>
  <div class="tag">Preview harness &mdash; not book content</div>
  <h3 style="font-size:12pt;margin:5pt 0 9pt">{fig_id}</h3>
  {figure_html}
  <div class="notdo" style="margin-top:10pt">
    <div class="lbl">Why this figure earns its place</div>
    <p>{justification}</p>
  </div>
  <p class="small" style="margin-top:6pt">Anchors in <code>{file}</code>.</p>
  <div class="folio"><span>figures_preview.py</span><span>{number}</span></div>
</section>'''


def build():
    pages = []
    for entry in FIGURES:
        figure_html = render_figure(entry["id"])
        pages.append(PAGE_TEMPLATE.format(
            fig_id=html.escape(entry["id"]),
            protection=html.escape(str(entry["protection"]) if entry["protection"] is not None else "&mdash;"),
            figure_html=figure_html,
            justification=html.escape(entry["justification"]),
            file=html.escape(entry["file"]),
            number=entry["number"],
        ))

    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Figure set preview — The Storm-Ready Home</title>
<link rel="stylesheet" href="book.css">
</head>
<body>
{"".join(pages)}
</body>
</html>
'''
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(doc, encoding="utf-8")
    print(f"wrote {OUT} — {len(FIGURES)} pages")


if __name__ == "__main__":
    build()
