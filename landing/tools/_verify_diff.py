#!/usr/bin/env python3
import re, os, sys, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_pages as bp

def clean(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"&mdash;|&middot;|&rarr;|&darr;|&sect;|&#9654;|&larr;", " ", s)
    s = s.replace("&amp;", "&").replace("&rsquo;", "'").replace("&nbsp;", " ").replace("&times;", "x")
    s = re.sub(r"\s+", " ", s).strip()
    return s

def sentences(text):
    text = bp.fix_dashes(text)
    parts = re.split(r'(?<=[.!?])\s+', text)
    return [p.strip() for p in parts if len(p.strip()) > 3]

def words(text):
    text = bp.fix_dashes(text).lower()
    return set(re.findall(r"[a-z0-9']+", text))

total_missing = 0
for spec in bp.PAGES:
    rel = spec["rel"]
    src = bp.read_orig(rel)
    orig_content = bp.get_content_region(src, spec.get("simple", False))
    # drop the print-only button and old nav 'back' link text already handled;
    # also drop nav/footer -- get_content_region already excludes footer/topnav.
    orig_text = clean(orig_content)

    new_path = os.path.join(bp.LANDING, rel)
    new_html = open(new_path, encoding="utf-8").read()
    main_m = re.search(r'<main class="sheet-wrap" id="main">(.*)</main>', new_html, re.S)
    new_text = clean(main_m.group(1)) if main_m else ""

    ow, nw = words(orig_text), words(new_text)
    missing_words = ow - nw
    # ignore trivial function words / numbering artifacts
    missing_words = {w for w in missing_words if len(w) > 2}

    osent = sentences(orig_text)
    nw_join = bp.fix_dashes(new_text).lower()
    missing_sent = []
    for s in osent:
        s_clean = re.sub(r"[^a-z0-9 ]", "", s.lower())
        s_clean = re.sub(r"\s+", " ", s_clean).strip()
        if len(s_clean) < 8:
            continue
        target = re.sub(r"[^a-z0-9 ]", "", nw_join)
        target = re.sub(r"\s+", " ", target)
        if s_clean not in target:
            # fuzzy: ratio check against best window
            missing_sent.append(s)

    print("=== %s ===" % rel)
    print("  missing words (%d):" % len(missing_words), sorted(missing_words)[:40])
    print("  missing sentences (%d):" % len(missing_sent))
    for s in missing_sent[:15]:
        print("    -", s[:160])
    total_missing += len(missing_sent)

print("\nTOTAL missing-sentence flags across all pages:", total_missing)
