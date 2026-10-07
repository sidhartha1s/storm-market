#!/usr/bin/env python3
"""Rebuild the 15 hand-written inner pages through the Binder chrome (chrome.py).

Deterministic, no third-party deps. Reads each page's ORIGINAL bytes from
tools/_orig/<same relative path> (never from the file it is about to overwrite),
keeps title/meta/canonical/robots/OG/Twitter/JSON-LD and every body word verbatim
(only em dashes are rewritten, consistently, in body text AND JSON-LD text), and
re-emits the page through chrome.render().

Run: python3 tools/build_pages.py   (from landing/, or anywhere -- paths are absolute)
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))          # landing/tools
LANDING = os.path.dirname(HERE)                             # landing/
ORIG = os.path.join(HERE, "_orig")

sys.path.insert(0, HERE)
import chrome  # noqa: E402

# ---------------------------------------------------------------------------
# Page manifest: relative path (from landing/), directory depth (0 = landing/
# root, 1 = one dir below, 2 = two dirs below), and whether it is a "simple"
# utility page (privacy/terms/404) that gets a single "Page" tab instead of
# one tab per H2.
# ---------------------------------------------------------------------------
PAGES = [
    {"rel": "about/index.html", "depth": 1},
    {"rel": "privacy.html", "depth": 0, "simple": True},
    {"rel": "terms.html", "depth": 0, "simple": True},
    {"rel": "404.html", "depth": 0, "simple": True},
    {"rel": "yt/index.html", "depth": 1, "simple": True, "tab1_label": "The checklist", "no_final_tab": True},
    {"rel": "field-notes/index.html", "depth": 1, "tab1_label": "Dispatches"},
    {"rel": "field-notes/joplin-tornado-2011/index.html", "depth": 2},
    {"rel": "field-notes/tornado-warning-vs-watch/index.html", "depth": 2},
    {"rel": "resources/index.html", "depth": 1},
    {"rel": "resources/emergency-binder/index.html", "depth": 2},
    {"rel": "resources/family-emergency-plan-template/index.html", "depth": 2},
    {"rel": "resources/go-bag-checklist/index.html", "depth": 2},
    {"rel": "resources/home-inventory-for-insurance/index.html", "depth": 2},
    {"rel": "resources/hurricane-preparedness-checklist/index.html", "depth": 2},
    {"rel": "resources/tornado-preparedness-checklist/index.html", "depth": 2},
    {"rel": "resources/tornado-safe-room/index.html", "depth": 2},
]

BUY = chrome.BUY
PACKET = chrome.PACKET

# ---------------------------------------------------------------------------
# Em dash normalisation -- deterministic, exact-phrase overrides first (the
# handful of repeated boilerplate constructions that make up the bulk of the
# occurrences), then a fixed fallback rule for everything else. Applied
# identically to body text and to JSON-LD text so the two stay consistent.
# ---------------------------------------------------------------------------
DASH_CHARS = ("—", "&mdash;")

LITERAL_DASH_FIXES = [
    ("Get the Book &mdash; $9.99 &rarr;", "Get the Book, $9.99 &rarr;"),
    ("Get the book &mdash; $9.99 &rarr;", "Get the book, $9.99 &rarr;"),
    ("Get the Book — $9.99 →", "Get the Book, $9.99 →"),
    ("Get the book — $9.99 →", "Get the book, $9.99 →"),
    ("Get the Book &mdash; $9.99", "Get the Book, $9.99"),
    (" &mdash; book cover\"", ": book cover\""),
    (" — book cover\"", ": book cover\""),
]


def fix_dashes(s):
    for old, new in LITERAL_DASH_FIXES:
        s = s.replace(old, new)
    # Fallback: any remaining em dash (entity or literal char), used in this
    # corpus as an explanatory/elaborating connector -- a colon reads correctly
    # in that role in every remaining case reviewed while writing this script.
    s = re.sub(r"\s*(?:&mdash;|—)\s*", ": ", s)
    return s


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------

def read_orig(rel):
    path = os.path.join(ORIG, rel)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def find_balanced(html, open_re, tag):
    """Find the first match of open_re (a compiled regex matching an opening
    tag like <div class="x" ...>) and return (start, end, whole, inner) for
    the element through its matching close tag (</tag>), counting nested
    same-tag opens. Returns None if not found."""
    m = open_re.search(html)
    if not m:
        return None
    start = m.start()
    pos = m.end()
    depth = 1
    open_tag_re = re.compile(r"<%s\b" % tag, re.I)
    close_tag_re = re.compile(r"</%s\s*>" % tag, re.I)
    while depth > 0:
        nxt_open = open_tag_re.search(html, pos)
        nxt_close = close_tag_re.search(html, pos)
        if not nxt_close:
            raise ValueError("unbalanced <%s> starting at %d" % (tag, start))
        if nxt_open and nxt_open.start() < nxt_close.start():
            depth += 1
            pos = nxt_open.end()
        else:
            depth -= 1
            pos = nxt_close.end()
    end = pos
    whole = html[start:end]
    return start, end, whole


def inner_of(whole, tag):
    """Strip the outer <tag ...> ... </tag> wrapper off a whole-element string."""
    m = re.match(r"<%s\b[^>]*>" % tag, whole, re.I)
    close = re.search(r"</%s\s*>\s*$" % tag, whole, re.I)
    return whole[m.end():close.start()]


def unwrap_divs(content, class_alt):
    """Properly unwrap every <div class="X"> whose class matches class_alt
    (a regex alternation like "wrap|col|grid"): remove the OPEN tag AND its
    true matching CLOSE tag, keeping the inner content in place.

    Stripping only the opening tag and leaving the closing tag as a "harmless
    orphan" is WRONG: HTML's stack-based parser pops whatever real <div> is
    currently innermost-open when it hits any </div>, so a stray close
    prematurely closes a real ancestor (chrome's .sheet-wrap, .binder, a
    .row, ...) rather than being ignored -- this broke .sheet-wrap's
    overflow:hidden clipping and the .binder grid on several pages before
    this helper replaced the naive open-tag-only strips."""
    open_re = re.compile(r'<div class="(?:%s)"[^>]*>' % class_alt)
    out = []
    pos = 0
    while True:
        m = open_re.search(content, pos)
        if not m:
            out.append(content[pos:])
            break
        out.append(content[pos:m.start()])
        start, end, whole = find_balanced(content[m.start():], open_re, "div")
        out.append(inner_of(whole, "div"))
        pos = m.start() + end
    return "".join(out)


def strip_tags(s):
    return re.sub(r"<[^>]+>", " ", s)


def clean_text(s):
    s = strip_tags(s)
    s = re.sub(r"&mdash;|&middot;|&rarr;|&darr;|&sect;|&#9654;", " ", s)
    s = s.replace("&amp;", "&").replace("&rsquo;", "'").replace("&nbsp;", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s


# Hand-picked tab labels, keyed by the start of the heading text (after clean_text).
# Anything not listed falls back to the first words of the heading.
TAB_LABELS = {
    "The reports get written": "The reports",
    "The method, in four rules": "The method",
    "What the report": "The report",
    "Where the work lives": "The work",
    "Privacy Policy": "Privacy",
    "Terms of Use": "Terms",
    "That page isn't here": "Not found",
    "Field Notes.": "Dispatches",
    "The Joplin tornado had": "Joplin, 2011",
    "Questions people ask about Joplin": "Questions",
    "The part the episode": "Your part",
    "More field notes": "More notes",
    "Watch. Warning. Advisory.": "Watch vs warning",
    "Why sirens make this worse": "Sirens",
    "Questions people ask": "Questions",
    "Seven pages,": "Pick a page",
    "Seven pages are a taste": "The book",
    "Emergency binder checklist": "The binder",
    "What belongs in an emergency binder": "What goes in",
    "Where your state's mitigation credits": "State credits",
    "What the free version doesn't": "Free vs book",
    "Family emergency plan template": "The plan",
    "Two independent alert paths": "Alert paths",
    "Evacuation zone and safe room": "Zone and room",
    "What this plan doesn't do": "Limits",
    "Go bag checklist": "The go bag",
    "The kids' go bag": "Kids' bag",
    "What a go bag doesn't cover": "Limits",
    "Home inventory for insurance": "The inventory",
    "Photograph your mitigation work": "Mitigation",
    "What documentation cannot do": "Limits",
    "Hurricane preparedness checklist": "Before season",
    "When a watch is issued": "Watch issued",
    "Reading the cone correctly": "The cone",
    "Tornado preparedness checklist": "The plan",
    "The kit": "The kit",
    "Reading a radar loop": "Radar",
    "Tornado safe room in house": "Safe room",
    "Storm shelter vs safe room": "Shelter vs room",
    "Tornado safe room cost": "Cost",
    "What should you have in a storm shelter": "What to stock",
}

def short_label(text, maxwords=3):
    t = clean_text(text)
    for k, v in TAB_LABELS.items():
        if t.startswith(k):
            return v
    words = [w for w in t.split(" ") if w]
    return " ".join(words[:maxwords])


# ---------------------------------------------------------------------------
# Head metadata extraction
# ---------------------------------------------------------------------------

def extract_head(html):
    head_match = re.search(r"<head>(.*?)</head>", html, re.S | re.I)
    head = head_match.group(1)

    title = re.search(r"<title>(.*?)</title>", head, re.S | re.I).group(1)
    desc_m = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', head, re.I)
    description = desc_m.group(1) if desc_m else ""
    canon_m = re.search(r'<link\s+rel="canonical"\s+href="([^"]*)"', head, re.I)
    canonical = canon_m.group(1) if canon_m else ""
    robots_m = re.search(r'<meta\s+name="robots"[^>]*>', head, re.I)
    robots_tag = robots_m.group(0) if robots_m else ""

    og_tags = re.findall(r'<meta\s+property="og:[^"]*"[^>]*>', head, re.I)
    tw_tags = re.findall(r'<meta\s+name="twitter:[^"]*"[^>]*>', head, re.I)

    ldjson_blocks = re.findall(
        r'<script type="application/ld\+json">(.*?)</script>', html, re.S | re.I
    )

    return {
        "title": title,
        "description": description,
        "canonical": canonical,
        "robots_tag": robots_tag,
        "og_tags": og_tags,
        "tw_tags": tw_tags,
        "ldjson_blocks": ldjson_blocks,
    }


def build_head_extra(meta):
    parts = []
    if meta["robots_tag"]:
        parts.append(meta["robots_tag"])
    parts.extend(meta["og_tags"])
    parts.extend(meta["tw_tags"])
    for block in meta["ldjson_blocks"]:
        fixed = fix_dashes(block)
        parts.append('<script type="application/ld+json">%s</script>' % fixed)
    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Content-region extraction (between <header ...> / start-of-body and
# <footer) and block-level conversions into chrome's vocabulary.
# ---------------------------------------------------------------------------

def get_content_region(html, simple):
    body_m = re.search(r"<body>(.*)</body>", html, re.S | re.I)
    body = body_m.group(1)
    footer_idx = body.find("<footer")
    content = body[:footer_idx] if footer_idx != -1 else body
    if simple:
        # No topnav/header on these pages -- content is the single <div class="wrap">.
        m = re.search(r'<div class="wrap">', content)
        if m:
            start, end, whole = find_balanced(content[m.start():], re.compile(r'<div class="wrap">'), "div")
            content = inner_of(whole, "div")
        # Drop the "back to home" nav link -- equivalent of an old nav label.
        content = re.sub(r'<a class="back"[^>]*>.*?</a>\s*', "", content, flags=re.S)
        return content
    header_idx = content.find("<header")
    if header_idx == -1:
        raise ValueError("no <header> found")
    return content[header_idx:]


def convert_details_faq(content):
    """<div class="faq|faqbox">...<details><summary>Q</summary><p>A</p></details>...</div>
    -> <dl class="faq"><div><dt>Q</dt><dd>A</dd></div>...</dl>
    Uses balanced-div extraction -- a lookahead-terminated non-greedy match
    can silently swallow real content past the real close (caught in review:
    it ate a whole bookcta block on one page)."""
    open_re = re.compile(r'<div class="(?:faq|faqbox)">')
    out = []
    pos = 0
    while True:
        m = open_re.search(content, pos)
        if not m:
            out.append(content[pos:])
            break
        out.append(content[pos:m.start()])
        start, end, whole = find_balanced(content[m.start():], open_re, "div")
        inner = inner_of(whole, "div")
        items = re.findall(r"<details>\s*<summary>(.*?)</summary>\s*(.*?)</details>", inner, re.S)
        rows = []
        for q, a in items:
            a = re.sub(r"</?p>", "", a).strip()
            rows.append("<div><dt>%s</dt><dd>%s</dd></div>" % (q.strip(), a))
        out.append('<dl class="faq">%s</dl>\n' % "".join(rows))
        pos = m.start() + end
    return "".join(out)


def convert_list_blocks(content):
    """<ul class="checklist">|<ol class="method|protections">
    with <li><b>T</b>...(<span class="sub">D</span>|D)...</li>
    -> <ol class="ruled"><li><b>T</b><p>D</p></li>...</ol>"""

    def conv_li(li_inner):
        # protections/method style: <span class="n">No 04</span><span><b>T.</b> body</span>
        m = re.match(r'<span class="n">([^<]*)</span><span>(.*)</span>\s*$', li_inner, re.S)
        if m:
            num, rest = m.group(1).strip(), m.group(2)
            bm = re.match(r"\s*<b>(.*?)</b>\s*(.*)$", rest, re.S)
            if bm:
                title, body = bm.group(1).strip(), bm.group(2).strip()
                return "<li><b>%s. %s</b><p>%s</p></li>" % (num, title, body)
        # checklist style: <b>T</b><span class="sub">D</span>
        m = re.match(r"<b>(.*?)</b>\s*<span[^>]*>(.*?)</span>\s*$", li_inner, re.S)
        if m:
            return "<li><b>%s</b><p>%s</p></li>" % (m.group(1).strip(), m.group(2).strip())
        return "<li>%s</li>" % li_inner

    def conv_block(m):
        tag, cls, inner = m.group(1), m.group(2), m.group(3)
        lis = re.findall(r"<li>(.*?)</li>", inner, re.S)
        new_lis = "".join(conv_li(li) for li in lis)
        return '<ol class="ruled">%s</ol>\n' % new_lis

    pattern = re.compile(
        r'<(ul|ol) class="(checklist|method|protections)">(.*?)</\1>', re.S
    )
    return pattern.sub(conv_block, content)


def convert_pull(content):
    """<div class="pull">TEXT<span class="src">SRC</span></div>
    -> <blockquote class="quote"><p>TEXT</p><cite>SRC</cite></blockquote>"""

    def conv(m):
        inner = m.group(1)
        sm = re.search(r'<span class="src">(.*?)</span>', inner, re.S)
        src = sm.group(1).strip() if sm else ""
        text = re.sub(r'<span class="src">.*?</span>', "", inner, flags=re.S).strip()
        return '<blockquote class="quote"><p>%s</p><cite>%s</cite></blockquote>\n' % (text, src)

    return re.sub(r'<div class="pull">(.*?)</div>', conv, content, flags=re.S)


def convert_note_callout(content):
    """<div class="note">INNER</div> (single manufactured-home style callout,
    NOT the .note *link cards* which are converted separately before this
    runs) -> <p>INNER</p>"""
    return re.sub(r'<div class="note">(.*?)</div>', lambda m: "<p>%s</p>\n" % m.group(1).strip(), content, flags=re.S)


def convert_defs(content):
    """.defs/.def/.word/.rule glossary -> <ol class="ruled">"""
    m = re.search(r'<div class="defs">', content)
    if not m:
        return content
    start, end, whole = find_balanced(content[m.start():], re.compile(r'<div class="defs">'), "div")
    whole_start = m.start()
    inner = inner_of(whole, "div")
    defs = []
    search_from = 0
    def_open_re = re.compile(r'<div class="def(?: warn)?">')
    while True:
        dm = def_open_re.search(inner, search_from)
        if not dm:
            break
        d_start, d_end, d_whole = find_balanced(inner[dm.start():], re.compile(r'<div class="def(?: warn)?">'), "div")
        defs.append(inner_of(d_whole, "div"))
        search_from = dm.start() + d_end
    lis = []
    for d in defs:
        word_m = re.search(r'<div class="word">(.*?)</div>', d, re.S)
        h3_m = re.search(r"<h3>(.*?)</h3>", d, re.S)
        rule_m = re.search(r'<p class="rule">(.*?)</p>', d, re.S)
        body = re.sub(r'<div class="word">.*?</div>|<h3>.*?</h3>|<p class="rule">.*?</p>', "", d, flags=re.S).strip()
        body = re.sub(r"</?p>", " ", body).strip()
        pieces = [x.strip() for x in [word_m.group(1) if word_m else "", body, rule_m.group(1) if rule_m else ""] if x and x.strip()]
        lis.append("<li><b>%s</b><p>%s</p></li>" % (h3_m.group(1).strip() if h3_m else "", ". ".join(pieces)))
    new_block = '<ol class="ruled">%s</ol>\n' % "".join(lis)
    return content[:whole_start] + new_block + content[whole_start + len(whole):]


def convert_tvframe(content):
    """<figure class="tvframe"><div class="screen"><iframe .../></div><figcaption>...</figcaption></figure>
    -> plain figure with inline-styled 16:9 wrapper, iframe attrs kept verbatim."""

    def conv(m):
        whole = m.group(0)
        iframe_m = re.search(r"<iframe\b.*?</iframe>|<iframe\b[^>]*>", whole, re.S)
        iframe_tag = iframe_m.group(0)
        iframe_tag = re.sub(
            r"^<iframe\b",
            '<iframe style="position:absolute;inset:0;width:100%;height:100%;border:0"',
            iframe_tag,
        )
        cap_m = re.search(r"<figcaption>(.*?)</figcaption>", whole, re.S)
        cap = clean_text(cap_m.group(1)) if cap_m else ""
        cap_html_m = re.search(r"<figcaption>(.*?)</figcaption>", whole, re.S)
        cap_inner = cap_html_m.group(1) if cap_html_m else ""
        return (
            '<figure style="margin:0 0 30px">'
            '<div style="position:relative;aspect-ratio:16/9;background:#000">'
            "%s</div><figcaption>%s</figcaption></figure>\n" % (iframe_tag, cap_inner)
        )

    return re.sub(r'<figure class="tvframe">.*?</figure>', conv, content, flags=re.S)


def extract_and_drop_exhibit_wrapper(content):
    """<div class="exhibit"> is purely a layout wrapper around the tvframe
    figure -- unwrap it (leave the figure in place)."""
    return unwrap_divs(content, "exhibit")


def convert_samplestrip(content):
    def conv(m):
        inner = m.group(1)
        p_m = re.search(r"<p>(.*?)</p>", inner, re.S)
        a_m = re.search(r'<a href="([^"]*)"[^>]*>(.*?)</a>', inner, re.S)
        p_text = p_m.group(1).strip() if p_m else ""
        if a_m:
            return "<p>%s <a href=\"%s\">%s</a></p>\n" % (p_text, a_m.group(1), a_m.group(2).strip())
        return "<p>%s</p>\n" % p_text

    return re.sub(r'<div class="samplestrip">(.*?)</div>', conv, content, flags=re.S)


def extract_printbar(content):
    """Pull the .printbar/.gate free-pack CTA out of the flow entirely; return
    (content_without_it, extracted_html_for_final_tab_or_None)."""
    m = re.search(r'<div class="printbar">', content)
    if not m:
        return content, None
    start, end, whole = find_balanced(content, re.compile(r'<div class="printbar">'), "div")
    inner = inner_of(whole, "div")
    gate_m = re.search(r'<div class="gate">(.*?)</div>\s*<a class="ghost" href="([^"]*)"[^>]*>(.*?)</a>', inner, re.S)
    extracted = ""
    if gate_m:
        gate_inner, href, linktext = gate_m.group(1), gate_m.group(2), gate_m.group(3).strip()
        k_m = re.search(r'<div class="k">(.*?)</div>', gate_inner, re.S)
        h3_m = re.search(r"<h3>(.*?)</h3>", gate_inner, re.S)
        p_m = re.search(r"<p>(.*?)</p>", gate_inner, re.S)
        sub_m = re.search(r'<div class="sub">(.*?)</div>', gate_inner, re.S)
        extracted = (
            '<p class="kick">%s</p>\n<h3>%s</h3>\n<p>%s</p>\n'
            '<p><a class="btn ghost" href="%s">%s</a></p>\n'
            '<p style="font-size:14px;color:var(--faded)">%s</p>\n'
            % (
                clean_text(k_m.group(1)) if k_m else "",
                h3_m.group(1).strip() if h3_m else "",
                p_m.group(1).strip() if p_m else "",
                href,
                linktext,
                sub_m.group(1).strip() if sub_m else "",
            )
        )
    new_content = content[:start] + content[end:]
    return new_content, extracted


def convert_standalone_gate(content):
    """A .gate block NOT wrapped in .printbar (the resources hub's own free-
    pack CTA) -- convert it inline to the same simplified idiom, in place."""
    m = re.search(r'<div class="gate">', content)
    if not m:
        return content
    start, end, whole = find_balanced(content, re.compile(r'<div class="gate">'), "div")
    k_m = re.search(r'<div class="k">(.*?)</div>', whole, re.S)
    h3_m = re.search(r"<h3>(.*?)</h3>", whole, re.S)
    p_m = re.search(r"<p>(.*?)</p>", whole, re.S)
    sub_m = re.search(r'<div class="sub">(.*?)</div>', whole, re.S)
    ghost_m = re.search(r'<a class="ghost" href="([^"]*)"[^>]*>(.*?)</a>', whole, re.S)
    new_block = (
        '<p class="kick">%s</p>\n<h3>%s</h3>\n<p>%s</p>\n'
        '<p><a class="btn ghost" href="%s">%s</a></p>\n'
        '<p style="font-size:14px;color:var(--faded)">%s</p>\n'
        % (
            clean_text(k_m.group(1)) if k_m else "",
            h3_m.group(1).strip() if h3_m else "",
            p_m.group(1).strip() if p_m else "",
            ghost_m.group(1) if ghost_m else BUY,
            ghost_m.group(2).strip() if ghost_m else "",
            sub_m.group(1).strip() if sub_m else "",
        )
    )
    return content[:start] + new_block + content[end:]


def convert_bookcta(content):
    """Keep bookcta inline (it is real page copy), simplified to chrome idiom.
    Uses balanced-div extraction (bookcta nests a .cover div and, on some
    pages, a .ctarow div with a second button) so nothing inside is dropped."""
    out = []
    pos = 0
    open_re = re.compile(r'<div class="bookcta">')
    while True:
        m = open_re.search(content, pos)
        if not m:
            out.append(content[pos:])
            break
        out.append(content[pos:m.start()])
        start, end, whole = find_balanced(content[m.start():], open_re, "div")
        h3_m = re.search(r"<h3>(.*?)</h3>", whole, re.S)
        p_m = re.search(r"<p>(.*?)</p>", whole, re.S)
        btns = re.findall(r'<a class="btn[^"]*"[^>]*href="([^"]*)"[^>]*>(.*?)</a>', whole, re.S)
        sub_m = re.search(r'<div class="btn-sub">(.*?)</div>', whole, re.S)
        h3 = h3_m.group(1).strip() if h3_m else ""
        p = p_m.group(1).strip() if p_m else ""
        sub = sub_m.group(1).strip() if sub_m else ""
        btn_html = "".join('<p><a class="btn" href="%s">%s</a></p>\n' % (href, txt.strip()) for href, txt in btns) or (
            '<p><a class="btn" href="%s">Get the Book</a></p>\n' % BUY
        )
        out.append(
            '<p><strong>%s</strong> %s</p>\n%s'
            '<p style="font-size:14px;color:var(--faded)">%s</p>\n' % (h3, p, btn_html, sub)
        )
        pos = m.start() + end
    return "".join(out)


def convert_sources_and_chapters(content):
    content = re.sub(r'<div class="sources">(.*?)</div>', lambda m: m.group(1).strip() + "\n", content, flags=re.S)
    content = re.sub(r'<div class="chapters">(.*?)</div>', lambda m: m.group(1).strip() + "\n", content, flags=re.S)
    return content


def convert_note_cards(content):
    """.notegrid > a.note (archive cross-link cards, h2 or h3 title)
    -> <ol class="ruled"> list. Runs BEFORE the h2-split, so any h2 used as a
    card title here is safely demoted to <b> and never becomes a split point."""
    m = re.search(r'<div class="notegrid">', content)
    if not m:
        return content
    start, end, whole = find_balanced(content, re.compile(r'<div class="notegrid">'), "div")
    inner = inner_of(whole, "div")
    cards = re.findall(r'<a class="note" href="([^"]*)">(.*?)</a>', inner, re.S)
    lis = []
    for href, body in cards:
        meta_m = re.search(r'<div class="meta">(.*?)</div>', body, re.S)
        title_m = re.search(r"<h[23]>(.*?)</h[23]>", body, re.S)
        p_m = re.search(r"<p>(.*?)</p>", body, re.S)
        meta = clean_text(meta_m.group(1)) if meta_m else ""
        title = title_m.group(1).strip() if title_m else ""
        p = p_m.group(1).strip() if p_m else ""
        lead = ("%s: " % meta) if meta else ""
        lis.append('<li><b>%s<a href="%s">%s</a></b><p>%s</p></li>' % (lead, href, title, p))
    new_block = '<ol class="ruled">%s</ol>\n' % "".join(lis)
    return content[:start] + new_block + content[end:]


def convert_pg_grid(content):
    """resources hub: .grid > .pg cards -> <ol class="ruled">"""
    m = re.search(r'<div class="grid">', content)
    if not m or '<div class="pg' not in content[m.start():]:
        return content  # only the resources-hub card grid uses .pg -- any
        # other <div class="grid"> (e.g. about's portrait/text intro layout)
        # is a plain layout wrapper and must be left for generic_cleanup.
    start, end, whole = find_balanced(content, re.compile(r'<div class="grid">'), "div")
    if '<div class="pg' not in whole:
        return content
    inner = inner_of(whole, "div")
    cards = re.findall(r'<div class="pg(?: book)?">(.*?)</div>\s*(?=<div class="pg|$)', inner, re.S)
    lis = []
    for card in cards:
        from_m = re.search(r'<div class="from">(.*?)</div>', card, re.S)
        h3_m = re.search(r"<h3>(.*?)</h3>", card, re.S)
        p_m = re.search(r"<p>(.*?)</p>", card, re.S)
        acts_m = re.search(r'<div class="acts">(.*?)</div>', card, re.S)
        btn_m = re.search(r'<a class="btn"[^>]*href="([^"]*)"[^>]*>(.*?)</a>', card, re.S)
        title_html = h3_m.group(1).strip() if h3_m else ""
        lead = (clean_text(from_m.group(1)) + ". ") if from_m else ""
        p = p_m.group(1).strip() if p_m else ""
        tail = ""
        if acts_m:
            tail = " (%s)" % clean_text(acts_m.group(1))
        li = "<li><b>%s</b><p>%s%s%s</p>" % (title_html, lead, p, tail)
        if btn_m:
            li += '<p><a class="btn" href="%s">%s</a></p>' % (btn_m.group(1), btn_m.group(2).strip())
        li += "</li>"
        lis.append(li)
    new_block = '<ol class="ruled">%s</ol>\n' % "".join(lis)
    return content[:start] + new_block + content[end:]


def convert_proof_strip(content):
    m = re.search(r'<div class="proof">', content)
    if not m:
        return content
    start, end, whole = find_balanced(content, re.compile(r'<div class="proof">'), "div")
    items = re.findall(r"<div><b>(.*?)</b>(.*?)</div>", whole, re.S)
    line = " &middot; ".join("%s %s" % (a.strip(), b.strip()) for a, b in items)
    return content[:start] + '<p class="kick">%s</p>\n' % line + content[end:]


def convert_mealcard(content):
    m = re.search(r'<div class="mealcard">', content)
    if not m:
        return content
    start, end, whole = find_balanced(content, re.compile(r'<div class="mealcard">'), "div")
    inner = inner_of(whole, "div")
    inner = re.sub(r'<div class="covers"[^>]*>.*?</div>\s*', "", inner, flags=re.S)
    inner = re.sub(r'<div class="kicker">(.*?)</div>', lambda m2: '<p class="kick">%s</p>' % m2.group(1), inner)
    new_block = (
        '<div class="row"><div>%s</div>'
        '<figure style="margin:0"><img class="cover" src="/assets/cover.jpg" width="300" height="420" '
        'alt="The Storm-Ready Home by Paul Raymond: book cover" loading="lazy"></figure></div>\n' % inner
    )
    return content[:start] + new_block + content[end:]


def convert_hero_grid(content, depth):
    """resources hub header: drop the decorative .fan cover stack, keep text."""
    fan_m = re.search(r'<div class="fan"[^>]*>', content)
    if fan_m:
        start, end, whole = find_balanced(content, re.compile(r'<div class="fan"[^>]*>'), "div")
        content = content[:start] + content[end:]
    content = unwrap_divs(content, "hero-grid")
    content = re.sub(r'<div class="kicker">(.*?)</div>', lambda m: '<p class="kick">%s</p>' % m.group(1), content)
    content = re.sub(r'<p class="sub">', '<p class="lead">', content)
    content = re.sub(r'<div class="fine">(.*?)</div>', lambda m: '<p style="font-size:14px;color:var(--faded)">%s</p>' % m.group(1), content)
    content = re.sub(r'<a class="ghostbtn"([^>]*)>(.*?)</a>', r'<a class="btn ghost"\1>\2</a>', content)
    content = re.sub(r'<a class="btn big"', '<a class="btn"', content)
    return content


def generic_cleanup(content):
    """Kickers/leads/bylines/misc wrapper divs with no chrome equivalent:
    map the ones chrome styles, properly unwrap the rest via unwrap_divs()
    (open AND matching close both removed -- see unwrap_divs docstring for
    why a stray close cannot just be left behind)."""
    content = re.sub(r'<div class="kicker">(.*?)</div>', lambda m: '<p class="kick">%s</p>' % m.group(1), content, flags=re.S)
    content = re.sub(r'<div class="dispatch-no">(.*?)</div>\s*<div class="datestamp">(.*?)</div>',
                      lambda m: '<p class="kick">%s &middot; %s</p>' % (m.group(1), m.group(2)), content, flags=re.S)
    content = re.sub(r'<p class="standfirst">', '<p class="lead">', content)
    content = re.sub(r'<p class="directanswer">', '<p class="lead">', content)
    content = re.sub(r'<p class="sub">', '<p class="lead">', content)
    content = re.sub(
        r'<div class="byline">\s*<span class="face"[^>]*></span>\s*<span class="who">(.*?)</span>\s*</div>',
        lambda m: "<p>%s</p>" % m.group(1), content, flags=re.S,
    )
    content = re.sub(r'<p class="secondary">', "<p>", content)
    content = re.sub(r'<p class="internal">', "<p>", content)
    content = re.sub(r'<button class="printbtn"[^>]*>.*?</button>\s*', "", content, flags=re.S)
    content = re.sub(r'<div class="shots">', '<div class="gallery">', content)
    content = re.sub(
        r'<div class="honest">(.*?)</div>',
        lambda m: '<blockquote class="quote"><p>%s</p></blockquote>' % m.group(1).strip(),
        content, flags=re.S,
    )
    content = re.sub(r'<div class="nextup">(.*?)</div>', lambda m: '<p class="kick">%s</p>' % m.group(1).strip(), content, flags=re.S)
    content = re.sub(r'<p class="meta">', '<p class="kick">', content)
    # Pure layout wrappers -- strip the opening tag only; unmatched closing
    # </div> tags are dropped silently by every HTML5 parser.
    content = unwrap_divs(content, "wrap|col|grid|text|topnav")
    return content


def transform_content(content, depth):
    content = convert_note_cards(content)       # before h2-split: demotes card h2/h3 to <b>
    content = convert_pg_grid(content)
    content = convert_proof_strip(content)
    content = convert_hero_grid(content, depth)
    content = convert_mealcard(content)
    content = convert_defs(content)
    content = convert_details_faq(content)
    content = convert_list_blocks(content)
    content = convert_pull(content)
    content = convert_tvframe(content)
    content = extract_and_drop_exhibit_wrapper(content)
    content = convert_samplestrip(content)
    content, extracted_gate = extract_printbar(content)
    content = convert_standalone_gate(content)
    content = convert_bookcta(content)
    content = convert_sources_and_chapters(content)
    content = convert_note_callout(content)
    content = generic_cleanup(content)
    content = fix_dashes(content)
    # Drop the <header .../header>/<article>/<section> wrapper tags themselves
    # (chrome's own .sheet-wrap already supplies the page frame) -- unwrap.
    content = re.sub(r'</?header[^>]*>', "", content)
    content = re.sub(r'</?article[^>]*>', "", content)
    content = re.sub(r'<section class="[^"]*"[^>]*>', "", content)
    content = re.sub(r'</section>', "", content)
    return content, extracted_gate


# ---------------------------------------------------------------------------
# Split transformed content into <section class="sheet"> blocks at each <h2>.
# ---------------------------------------------------------------------------

def balance_divs(chunk):
    """Splitting at <h2> can cut through a wrapper <div>. Drop closers that have no opener
    in this chunk and close any opener left open, so a sheet never pops the page chrome."""
    depth = 0
    out = []
    for tok in re.split(r"(<div[^>]*>|</div>)", chunk):
        if tok.startswith("<div"):
            depth += 1
        elif tok == "</div>":
            if depth == 0:
                continue
            depth -= 1
        out.append(tok)
    return "".join(out) + "</div>" * depth


def split_sections(content, simple, tab1_label_override=None):
    h2_positions = [m.start() for m in re.finditer(r"<h2\b", content)]
    tabs = []
    sheets = []
    if simple or not h2_positions:
        label = tab1_label_override or "Page"
        sheets.append(('<section class="sheet" id="sheet-1">%s</section>' % content))
        tabs.append(("sheet-1", label))
        return tabs, sheets

    boundaries = [0] + h2_positions + [len(content)]
    chunks = []
    pre = content[boundaries[0]:boundaries[1]]
    first = content[boundaries[1]:boundaries[2]]
    chunks.append(pre + first)
    for i in range(2, len(boundaries) - 1):
        chunks.append(content[boundaries[i]:boundaries[i + 1]])

    for i, chunk in enumerate(chunks):
        hm = re.search(r"<h2\b[^>]*>(.*?)</h2>", chunk, re.S)
        label = short_label(hm.group(1)) if hm else (tab1_label_override or "Start")
        if i == 0 and tab1_label_override:
            label = tab1_label_override
        sid = "sheet-%d" % (i + 1)
        chunk = balance_divs(chunk)
        sheets.append('<section class="sheet" id="%s">%s</section>' % (sid, chunk))
        tabs.append((sid, label))
    return tabs, sheets


GET_BOOK_LEAD = (
    "The Storm-Ready Home is a 486-page manual built from post-storm reports: "
    "130 numbered protections, 23 hazard playbooks, the 60-day sequence, and "
    "the 61-page printable binder, every figure cited."
)


def build_final_tab(n, extracted_gate):
    sid = "sheet-%d" % n
    extra = extracted_gate or ""
    html = (
        '<section class="sheet" id="%s"><h2>Get the book</h2>'
        '<div class="row"><div><p class="lead">%s</p>'
        '<p><a class="btn" href="%s">Get the Book, $9.99 &rarr;</a></p>%s</div>'
        '<figure style="margin:0"><img class="cover" src="/assets/cover-mini.webp" width="260" height="347" '
        'alt="The Storm-Ready Home by Paul Raymond: book cover" loading="lazy"></figure></div></section>'
        % (sid, GET_BOOK_LEAD, BUY, extra)
    )
    return sid, "Get the book", html


# ---------------------------------------------------------------------------
# Main per-page build
# ---------------------------------------------------------------------------

def build_page(spec):
    rel = spec["rel"]
    depth = spec["depth"]
    simple = spec.get("simple", False)
    src = read_orig(rel)

    meta = extract_head(src)
    head_extra = build_head_extra(meta)

    content = get_content_region(src, simple)
    content, extracted_gate = transform_content(content, depth)
    tabs, sheets = split_sections(content, simple, spec.get("tab1_label"))

    if not spec.get("no_final_tab"):  # /yt/ is one screen: the buy button is already on it
        sid, label, final_html = build_final_tab(len(tabs) + 1, extracted_gate)
        tabs.append((sid, label))
        sheets.append(final_html)

    out = chrome.render(
        title=fix_dashes(meta["title"]),
        description=fix_dashes(meta["description"]),
        canonical=meta["canonical"],
        tabs=tabs,
        sheets="\n".join(sheets),
        depth=depth,
        head_extra=head_extra,
    )
    return out


def main():
    written = 0
    for spec in PAGES:
        out = build_page(spec)
        dest = os.path.join(LANDING, spec["rel"])
        with open(dest, "w", encoding="utf-8") as f:
            f.write(out.replace(chr(0x2014), ',').replace('&mdash;', ',').replace('background:#000"', 'background:#0b0f14"'))
        written += 1
        print("wrote", spec["rel"])
    print("%d files written" % written)


if __name__ == "__main__":
    main()
