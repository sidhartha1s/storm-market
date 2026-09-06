#!/usr/bin/env python3
"""Build landing/index.html from the owner-approved Binder concept (tools/binder-home-source.html,
snapshot of storm-redesigns/c2-binder on 2026-09-06). The concept IS the page: this script only
(1) wraps its sheets in the shared chrome, (2) restores the live page's SEO head (title, meta,
JSON-LD from tools/_orig/home-head.html), (3) applies the owner's post-preview edits listed below.
Never port old-page sections in here; the owner rejected that (2026-09-06)."""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import chrome

LANDING = os.path.dirname(HERE)
SRC = os.path.join(HERE, "binder-home-source.html")
src = open(SRC, encoding="utf-8").read()

sheets = re.findall(r'<section class="sheet" id="[^"]+">.*?</section>', src, re.S)
assert len(sheets) == 8, len(sheets)
body = "\n".join(sheets)

# concept assets live one level up; the site keeps them beside index.html
body = body.replace("../assets/", "assets/")

# owner edit: stat strip under the hero button, ONE row
STATS = ('<p class="rated"><span class="stars">★★★★★</span> Rated five stars by early readers. '
         'Built from National Weather Service &amp; FEMA post-storm reports.</p>\n'
         '<ul class="stats"><li><b>486</b><span>pages</span></li><li><b>130</b><span>protections</span></li>'
         '<li><b>23</b><span>hazards</span></li><li><b>60</b><span>day sequence</span></li>'
         '<li><b>7-day</b><span>refund, no questions</span></li></ul>')
# place it AFTER the hero .row (full width) so the nowrap row never squeezes the cover column
start = body.index('<section class="sheet" id="sheet-start">')
end_row = body.index('</section>', start)
body = body[:end_row] + STATS + '\n      ' + body[end_row:]
assert 'class="stats"' in body

# owner edit: three recent-event quotes, the third is the thank-you note (drop the fourth)
recent = re.findall(r'<blockquote class="quote recent">.*?</blockquote>', body, re.S)
assert len(recent) == 4, len(recent)
carol = [q for q in recent if "Carol" in q][0]
body = body.replace(carol + "\n          ", "", 1) if (carol + "\n          ") in body else body.replace(carol, "", 1)
assert len(re.findall(r'<blockquote class="quote recent">', body)) == 3

# inner pages link the order form as /#offer
body = body.replace('<section class="sheet" id="sheet-get">', '<section class="sheet" id="sheet-get"><span id="offer"></span>', 1)

tabs = [("sheet-start", "Start here"), ("sheet-why", "Why this book"), ("sheet-inside", "Inside"),
        ("sheet-saves", "What it saves"), ("sheet-readers", "Testimonials"), ("sheet-paul", "About the author"),
        ("sheet-questions", "FAQs"), ("sheet-get", "Get my copy")]

head_extra = open(os.path.join(HERE, "_orig", "home-head.html"), encoding="utf-8").read()
title = open(os.path.join(HERE, "_orig", "home-title.txt"), encoding="utf-8").read().strip()
extra_css = ('<style>.rated{margin:18px 0 6px;font-size:18px;color:var(--soft)}.rated .stars{color:var(--tab5);letter-spacing:.12em}'
             '.stats{list-style:none;margin:0 0 8px;padding:0;display:flex;flex-wrap:nowrap;gap:28px;overflow-x:auto;scrollbar-width:none}'
             '.stats li{flex:0 0 auto;text-align:left}.stats b{display:block;font-family:var(--display);font-weight:900;font-size:40px;line-height:1;color:var(--tab3);letter-spacing:-.02em}'
             '.stats span{display:block;font-family:var(--mono);font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--faded);margin-top:4px;white-space:nowrap}'
             '.row>*{min-width:0}@media (max-width:600px){.stats{gap:18px}.stats b{font-size:30px}}</style>')

page = chrome.render(title=title, description="", canonical="https://paulraymond.online/", tabs=tabs, sheets=body, depth=0,
                     head_extra=head_extra + "\n" + extra_css)
# description + canonical already come from home-head.html; drop the empty duplicates render() emitted
page = page.replace('<meta name="description" content="">\n', '').replace('<link rel="canonical" href="https://paulraymond.online/">\n', '', 1)
page = page.replace(chr(0x2014), ",")
out = os.path.join(LANDING, "index.html")
open(out, "w", encoding="utf-8", newline="\n").write(page)
print("wrote", out, len(page), "bytes")
