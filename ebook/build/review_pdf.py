#!/usr/bin/env python3
"""Render the whole manuscript to one continuous review PDF.

This is NOT the book. The book is hand-laid into fixed 6x9 pages (see book.css and
fitcheck.mjs); this is a flowing read-through copy so the manuscript can be reviewed
before anyone spends days on pagination. It is labelled as such on every page.

    python3 review_pdf.py            # writes review/manuscript-review.html + .pdf
    python3 review_pdf.py --html     # HTML only, skip Chrome
"""

import argparse
import html
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
MS = HERE.parent / "manuscript"
OUT = HERE / "review"
CHROME = r"C:/Program Files/Google/Chrome/Application/chrome.exe"

# Reading order. Explicit, because filename sort puts Part 5 before Part 6 but also
# puts P3-01 before P2-C7, and the owner should read it in book order.
ORDER = [
    "P0-front-matter.md",
    "P1-C1-six-mechanisms.md",
    "P1-C2-the-timeline.md",
    "P2-C1-water.md",
    "P2-C2-food.md",
    "P2-C3-temperature-shelter.md",
    "P2-C4-power.md",
    "P2-C5-air-sanitation.md",
    "P2-C6-medical.md",
    "P2-C7-structure-hardening.md",
    "P3-01-tornado.md",
    "P3-02-hurricane-surge.md",
    "P3-03-extreme-rain-flash-flood.md",
    "P3-04-riverine-coastal-flooding.md",
    "P3-05-wildfire.md",
    "P3-06-wildfire-smoke.md",
    "P3-07-hail-derecho.md",
    "P3-08-lightning.md",
    "P3-09-blizzard-ice-storm.md",
    "P3-10-extreme-heat.md",
    "P3-11-extreme-cold.md",
    "P3-12-drought-water-scarcity-dust.md",
    "P3-13-earthquake.md",
    "P3-14-tsunami.md",
    "P3-15-space-weather.md",
    "P3-16-volcanic-ashfall.md",
    "P3-17-grid-failure-long-outage.md",
    "P3-18-systems-dark.md",
    "P3-19-electronics-records.md",
    "P3-20-water-sanitation-failure.md",
    "P3-21-hazmat-released-by-disaster.md",
    "P3-22-radiological-proximity.md",
    "P3-23-medical-care-alone.md",
    "P4-C1-people.md",
    "P4-C2-places.md",
    "P5-C1-warning-literacy.md",
    "P5-C2-documents-money.md",
    "P5-C3-evacuation.md",
    "P5-C4-electronics-radiological.md",
    "P6-the-binder.md",
    "P7-the-60-days.md",
]

CSS = """
@page { size: A4; margin: 18mm 16mm 20mm; }
* { box-sizing: border-box; }
body { font: 10.5pt/1.5 Georgia,'Times New Roman',serif; color:#141414; margin:0; }
.banner { background:#7a1d1d; color:#fff; padding:6px 10px; font:600 8.5pt/1.3 Segoe UI,Arial,sans-serif;
          letter-spacing:.04em; text-transform:uppercase; margin:0 0 18px; }
h1 { font:600 19pt/1.2 Segoe UI,Arial,sans-serif; margin:0 0 4px; page-break-before:always;
     border-bottom:2px solid #141414; padding-bottom:6px; }
h1:first-of-type { page-break-before:avoid; }
h2 { font:600 14pt/1.25 Segoe UI,Arial,sans-serif; margin:22px 0 6px; }
h3 { font:600 11.5pt/1.3 Segoe UI,Arial,sans-serif; margin:18px 0 4px;
     border-left:3px solid #7a1d1d; padding-left:8px; page-break-after:avoid; }
p { margin:0 0 8px; }
strong { color:#000; }
em { color:#333; }
hr { border:0; border-top:1px solid #d4d4d4; margin:16px 0; }
blockquote { margin:8px 0 8px 14px; padding-left:10px; border-left:2px solid #bbb; color:#333; }
table { border-collapse:collapse; width:100%; margin:10px 0; font-size:9pt;
        page-break-inside:avoid; }
th,td { border:1px solid #c9c9c9; padding:4px 6px; text-align:left; vertical-align:top; }
th { background:#f0f0f0; font:600 9pt Segoe UI,Arial,sans-serif; }
ul,ol { margin:0 0 8px 18px; padding:0; }
li { margin:0 0 3px; }
code { font:9.5pt Consolas,monospace; background:#f3f3f3; padding:1px 3px; }
pre { background:#f3f3f3; padding:8px; font:9pt Consolas,monospace; white-space:pre-wrap; }
sup.ref { font-size:7.5pt; color:#7a1d1d; font-weight:600; vertical-align:super; }
sup.pending { color:#a06800; }
.sources li.pending { color:#7a5c00; }
.sources li.pending::after { content:" — SOURCE PENDING"; font:600 7.5pt Segoe UI,Arial,sans-serif; color:#a06800; }
.sources { font-size:9pt; }
.sources li { margin:0 0 5px; }
.sources .src-ch { font:600 10pt Segoe UI,Arial,sans-serif; margin:14px 0 4px; }
.meta { font:9pt Segoe UI,Arial,sans-serif; color:#666; margin:0 0 14px; }
.toc { font:10pt Segoe UI,Arial,sans-serif; }
.toc li { margin:0 0 2px; }
"""

INLINE = [
    (re.compile(r"\*\*(.+?)\*\*", re.S), lambda m: f"<strong>{m.group(1)}</strong>"),
    (re.compile(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])"), lambda m: f"<em>{m.group(1)}</em>"),
    (re.compile(r"`([^`]+)`"), lambda m: f"<code>{m.group(1)}</code>"),
]

# Two marker kinds share one numbering sequence:
#   «SRC: ...»  a resolved reference — the citation itself
#   «CITE: ...» still pending — a description of the source to obtain
CITE_RE = re.compile(r"«(SRC|CITE):(.+?)»", re.S)

# Sources accumulate across the whole render into one numbered list, the way the
# finished book will carry them: a superscript number in the text, the source itself
# in the Sources chapter at the back.
SOURCES = []          # [(chapter_title, text, resolved)]
_CURRENT_CHAPTER = [""]
_SEEN = {}            # dedup key -> reference number


def _key(text, resolved):
    """Dedup key. Resolved sources are keyed on their URL, because the same document is
    frequently cited from several chapters with a different summary each time — a book
    must not carry two footnote numbers for one page. Pending markers are keyed on their
    full description, since there is no URL yet."""
    if resolved:
        url = re.search(r"https?://\S+", text)
        if url:
            return url.group(0).rstrip(".,;)")
    return text.lower()


def take_citation(match):
    """Replace a marker with a reference number and bank its text, reusing the number if
    this source has already been cited."""
    resolved = match.group(1) == "SRC"
    text = " ".join(match.group(2).split())
    cls = "ref" if resolved else "ref pending"
    key = _key(text, resolved)
    if key in _SEEN:
        return f'<sup class="{cls}">[{_SEEN[key]}]</sup>'
    SOURCES.append((_CURRENT_CHAPTER[0], text, resolved))
    _SEEN[key] = len(SOURCES)
    return f'<sup class="{cls}">[{len(SOURCES)}]</sup>'


def inline(text):
    # Citations are pulled out before escaping so the marker text cannot break the pattern,
    # and the returned <sup> is not re-escaped afterwards.
    text = CITE_RE.sub(lambda m: f"\x00{take_citation(m)}\x00", text)
    parts = text.split("\x00")
    for i, part in enumerate(parts):
        if part.startswith("<sup"):
            continue
        part = html.escape(part)
        for pattern, repl in INLINE:
            part = pattern.sub(repl, part)
        parts[i] = part
    return "".join(parts)


def render_markdown(md):
    """Deliberately minimal: this repo has no markdown dependency and does not need one.
    Handles what the manuscript actually uses — headings, paragraphs, lists, tables,
    blockquotes, rules, fenced code.

    Returns the list of top-level block HTML strings (one per heading/paragraph/table/
    list/blockquote/rule/code-block), not a joined string — paginate.mjs's block-stream
    builder (blocks_pipeline.py) reuses this list directly so the book layout shares the
    exact same parser and citation handling as this review PDF, instead of a second parser
    drifting out of sync. main() below joins the list for its own flowing-HTML output."""
    out = []
    lines = md.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("```"):
            block = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                block.append(html.escape(lines[i]))
                i += 1
            i += 1
            out.append("<pre>" + "\n".join(block) + "</pre>")
            continue

        if re.fullmatch(r"-{3,}", stripped):
            out.append("<hr>")
            i += 1
            continue

        heading = re.match(r"(#{1,6})\s+(.*)", stripped)
        if heading:
            level = len(heading.group(1))
            out.append(f"<h{level}>{inline(heading.group(2))}</h{level}>")
            i += 1
            continue

        # Table: a pipe row followed by a separator row.
        if stripped.startswith("|") and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|?$", lines[i + 1].strip()):
            def cells(row):
                return [c.strip() for c in row.strip().strip("|").split("|")]

            header = cells(stripped)
            i += 2
            body = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                body.append(cells(lines[i].strip()))
                i += 1
            head_html = "".join(f"<th>{inline(c)}</th>" for c in header)
            rows_html = "".join(
                "<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>" for row in body
            )
            out.append(f"<table><thead><tr>{head_html}</tr></thead><tbody>{rows_html}</tbody></table>")
            continue

        if stripped.startswith(">"):
            block = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                block.append(lines[i].strip().lstrip(">").strip())
                i += 1
            out.append(f"<blockquote>{inline(' '.join(block))}</blockquote>")
            continue

        bullet = re.match(r"[-*]\s+(.*)", stripped)
        numbered = re.match(r"\d+\.\s+(.*)", stripped)
        if bullet or numbered:
            tag = "ul" if bullet else "ol"
            pattern = re.compile(r"[-*]\s+(.*)") if bullet else re.compile(r"\d+\.\s+(.*)")
            items = []
            while i < len(lines):
                m = pattern.match(lines[i].strip())
                if m:
                    items.append(m.group(1))
                    i += 1
                elif lines[i].strip() and lines[i].startswith(("  ", "\t")) and items:
                    items[-1] += " " + lines[i].strip()  # continuation of the same bullet
                    i += 1
                else:
                    break
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
            continue

        # Paragraph: consume until a blank line or a block-level start. A leading pipe only
        # ends the paragraph when it actually starts a table (pipe row + separator row) —
        # citation bodies wrap their "| url | retrieved date" tail onto a new line, and
        # breaking there would orphan the closing marker and leak it into the page.
        block = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            table_start = nxt.startswith("|") and i + 1 < len(lines) \
                and re.match(r"^\|[\s:|-]+\|?$", lines[i + 1].strip())
            if not nxt or table_start or nxt.startswith(("#", ">", "```", "- ", "* ")) \
               or re.fullmatch(r"-{3,}", nxt) or re.match(r"\d+\.\s", nxt):
                break
            block.append(nxt)
            i += 1
        out.append(f"<p>{inline(' '.join(block))}</p>")

    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--html", action="store_true", help="write HTML only, skip Chrome")
    args = parser.parse_args()

    missing = [name for name in ORDER if not (MS / name).exists()]
    if missing:
        sys.exit("FAIL: missing manuscript files:\n  " + "\n  ".join(missing))

    words = 0
    body = []
    toc = []
    for name in ORDER:
        text = (MS / name).read_text(encoding="utf-8")
        words += len(text.split())
        title = text.split("\n", 1)[0].lstrip("# ").strip()
        _CURRENT_CHAPTER[0] = title
        toc.append(f"<li>{html.escape(title)}</li>")
        body.append("\n".join(render_markdown(text)))

    # Sources chapter, grouped by chapter, numbered continuously.
    src_html = ['<h1>Sources</h1>']
    resolved = sum(1 for *_, ok in SOURCES if ok)
    pending = len(SOURCES) - resolved
    if pending:
        src_html.append(
            f'<p class="meta">{len(SOURCES)} numbered references: <strong>{resolved} carry a full citation '
            f'and a retrieval date</strong>, and <strong>{pending} are still pending</strong> and marked as '
            'such. Every pending entry is either replaced with a primary document or the claim is cut from '
            'the book.</p>'
        )
    else:
        src_html.append(
            f'<p class="meta">{len(SOURCES)} numbered references, <strong>every one carrying a full '
            'citation and a retrieval date</strong>. Where a claim could not be traced to a primary '
            'document it was cut rather than softened.</p>'
        )
    src_html.append('<ol class="sources">')
    last_chapter = None
    for number, (chapter, text, ok) in enumerate(SOURCES, start=1):
        if chapter != last_chapter:
            src_html.append(f'</ol><p class="src-ch">{html.escape(chapter)}</p>'
                            f'<ol class="sources" start="{number}">')
            last_chapter = chapter
        cls = "" if ok else ' class="pending"'
        # Citation bodies carry the same emphasis markup as the manuscript (italic report
        # titles, bold key figures), so run the inline pass here too rather than printing
        # raw asterisks in the Sources chapter.
        item = html.escape(text)
        for pattern, repl in INLINE:
            item = pattern.sub(repl, item)
        src_html.append(f"<li{cls}>{item}</li>")
    src_html.append("</ol>")
    body.append("".join(src_html))
    cites = pending
    ref_state = f"{cites} still pending" if cites else "none pending"
    source_note = (
        "Those sources are still being obtained &mdash; each is either cited in full or the claim is "
        "cut before launch." if cites else
        "Every reference carries a full citation and a retrieval date; claims that could not be traced "
        "to a primary document were cut."
    )

    OUT.mkdir(parents=True, exist_ok=True)
    page = f"""<!doctype html><html><head><meta charset="utf-8">
<title>The Storm-Ready Home — draft review copy</title><style>{CSS}</style></head><body>
<p class="banner">Draft review copy &mdash; not the laid-out book. {words:,} words &middot;
{len(SOURCES)} references, {ref_state} &middot; see Sources at the back</p>
<h1>The Storm-Ready Home &mdash; draft review copy</h1>
<p class="meta">This renders the manuscript as continuous flowing text so it can be read and marked
up. The finished book is hand-laid into fixed 6&times;9 pages with the cover and design in
<code>sample.html</code>, so nothing about the pagination or the look here reflects the product.
Superscript numbers are references; the Sources chapter at the back lists each one. {source_note}</p>
<ol class="toc">{''.join(toc)}</ol>
{''.join(body)}
</body></html>"""

    html_path = OUT / "manuscript-review.html"
    html_path.write_text(page, encoding="utf-8")
    print(f"wrote {html_path}  ({words:,} words, {cites} open citations)")

    if args.html:
        return

    pdf_path = (OUT / "manuscript-review.pdf").resolve()
    # Chrome refuses a relative --print-to-pdf path with "Access is denied".
    subprocess.run(
        [CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf_path}", html_path.resolve().as_uri()],
        check=True,
    )
    print(f"wrote {pdf_path}  ({pdf_path.stat().st_size / 1_048_576:.1f} MB)")


if __name__ == "__main__":
    main()
