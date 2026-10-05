#!/usr/bin/env python3
"""Migration gate: every landing/**/*.html on this branch vs the same path on main.
Checks per page: (1) visible-text sentences of the old page all present in the new page
(after em-dash / punctuation / whitespace normalisation), (2) JSON-LD blocks equal after the
same normalisation, (3) no lorem / em dash / #000 in the new page, (4) buy link present.
Exit 1 on any failure. Run from anywhere: python3 landing/tools/gate_migration.py [--allow "old nav label" ...]
"""
import json, os, re, subprocess, sys, html as htmlmod

HERE = os.path.dirname(os.path.abspath(__file__))
LANDING = os.path.dirname(HERE)
REPO = os.path.dirname(LANDING)
SKIP = {"og-src.html"}
# text that legitimately disappears (old chrome: nav labels, footer rows, hard popup)
ALLOW = set(a.lower() for a in sys.argv[1:])
ALLOW_DEFAULT = {"field notes", "free checklists", "state guides", "youtube", "get the book",
                 "get the book $9.99", "skip to content", "back to top", "look inside", "reviews", "faq",
                 "privacy", "terms", "menu", "close",
                 "before you go further", "your state's storm packet is", "no purchase just pick your state",
                 "get my free state packet", "back to the storm ready home", "or see inside the book",
                 "week one of the plan costs", "it's the week the disaster reports keep citing", "$9 99 refundable for seven days",
                 "or see what's inside", "be ready before the next one", "four pages the three hazards your state actually gets who to call your state's mitigation program and deductible rules and a one page plan"}

def visible(h):
    h = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", " ", h, flags=re.S)
    h = re.sub(r"<[^>]+>", " ", h)
    h = htmlmod.unescape(h)
    return h

def norm(s):
    s = s.replace("—", " ").replace("–", " ").replace("’", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"[^\w$%'\"]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()

def sentences(h):
    """Element-level chunks: text between tag boundaries, so table cells and headings are
    compared on their own rather than fused into run-on sentences."""
    h = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", " ", h, flags=re.S)
    h = re.sub(r"<(nav|footer|header).*?</>", " ", h, flags=re.S)  # old chrome is replaced by design
    chunks = re.split(r"<[^>]+>", h)
    out = []
    for c in chunks:
        for part in re.split(r"(?<=[.!?])\s+", htmlmod.unescape(c)):
            n = norm(part)
            if len(n.split()) >= 4:
                out.append(n)
    return out

def ldjson(h):
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    out = []
    for b in blocks:
        try:
            out.append(json.loads(norm_json(b)))
        except Exception as e:
            out.append({"__parse_error__": str(e)})
    return out

def norm_json(s):
    return s.replace("—", ",").replace("–", "-")

def canon(o):
    if isinstance(o, dict): return {k: canon(v) for k, v in sorted(o.items())}
    if isinstance(o, list): return [canon(x) for x in o]
    if isinstance(o, str): return norm(o)
    return o

# Deliberate copy changes since main: applied to main's page before comparing, so the gate still
# catches every other lost sentence. Owner 5 Oct 26: price $14.99 -> $9.99 everywhere.
OLD_TO_NEW = [("14.99", "9.99")]

def old_file(rel):
    r = subprocess.run(["git", "-C", REPO, "show", f"main:landing/{rel}"], capture_output=True)
    if r.returncode != 0:
        return None
    h = r.stdout.decode("utf-8", "replace")
    for a, b in OLD_TO_NEW:
        h = h.replace(a, b)
    return h

def main():
    fails = 0; pages = 0
    for d, _, fs in os.walk(LANDING):
        if any(x in d for x in (".wrangler", "node_modules", os.sep + "gumroad", os.sep + "tools")): continue
        for f in fs:
            if not f.endswith(".html") or f in SKIP: continue
            path = os.path.join(d, f); rel = os.path.relpath(path, LANDING).replace("\\", "/")
            new = open(path, encoding="utf-8").read(); old = old_file(rel)
            pages += 1; probs = []
            if old is not None and rel != "index.html":  # home = approved Binder concept, owner decision 2026-09-06; old copy not ported
                newtext = norm(visible(new))
                missing = [s for s in sentences(old) if s not in newtext and s not in ALLOW and s not in ALLOW_DEFAULT]
                if missing: probs.append(f"{len(missing)} old sentences missing: " + " | ".join(m[:90] for m in missing[:5]))
                lo, ln = [canon(x) for x in ldjson(old)], [canon(x) for x in ldjson(new)]
                if lo != ln: probs.append(f"JSON-LD differs (old {len(lo)} blocks, new {len(ln)})")
            if re.search(r"lorem", new, re.I): probs.append("lorem present")
            if "—" in new: probs.append(f"em dash x{new.count(chr(0x2014))}")
            if re.search(r"#000\b", new): probs.append("#000 present")
            if "gumroad.com/l/ebook" not in new and "/#offer" not in new and f != "404.html": probs.append("no buy link")
            if probs:
                fails += 1; print(f"FAIL {rel}\n   " + "\n   ".join(probs))
    print(f"\n{pages} pages checked, {fails} failing")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
