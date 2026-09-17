"""Static lint for composition bug classes that passed every gate and failed in the render.

Both were found on 17 Sep 26 (Dujuan batch), each by more than one composer independently:

R1  textContent / innerHTML / innerText written on an element that HAS CHILD ELEMENTS.
    The write deletes the children at runtime. ladder-l5's sweeping rule was a <span> inside the
    caption div; the first caption's `tl.set("#l5-note", {textContent: ...})` removed it, so the
    rule existed for 1.9 s of a 55 s comp while the DOM-at-parse-time gates all passed.
    Fix: write the text on a dedicated leaf span.

R2  text mutated inside onStart / onComplete / onRepeat.
    The browser gates seek the timeline with suppressEvents, so the callback never fires and they
    measure stale markup (ladder.html's three notes, compare-card's grade label). Fix: pre-author
    each text in its own element and toggle autoAlpha. onUpdate count-ups on a leaf are fine.

Usage: python3 scripts/comp_lint.py episodes/<slug>      exit 1 on any finding
"""
import re
import sys
from pathlib import Path

ep = Path(sys.argv[1])
TEXT_PROPS = r'(?:textContent|innerHTML|innerText)'
findings = []


def element_inner(html, el_id):
    """Inner HTML of the element carrying id=el_id, or None."""
    m = re.search(r'<([a-zA-Z][\w-]*)\b[^>]*\bid="' + re.escape(el_id) + r'"[^>]*>', html)
    if not m:
        return None
    tag, i, depth = m.group(1), m.end(), 1
    for t in re.finditer(r'<(/?)' + tag + r'\b[^>]*?(/?)>', html[i:]):
        if t.group(2):            # self-closing
            continue
        depth += -1 if t.group(1) else 1
        if depth == 0:
            return html[i:i + t.start()]
    return None


for comp in sorted((ep / 'compositions').glob('*.html')):
    src = comp.read_text(encoding='utf-8')
    markup = re.sub(r'<script\b.*?</script>', '', src, flags=re.S)
    script = '\n'.join(re.findall(r'<script\b[^>]*>(.*?)</script>', src, flags=re.S))

    # R1: every id that receives a text write, via gsap vars or a direct DOM assignment
    targets = set()
    for m in re.finditer(r'\(\s*["\']#([\w-]+)["\']\s*,\s*\{[^{}]*\b' + TEXT_PROPS + r'\s*:', script):
        targets.add(m.group(1))
    for m in re.finditer(r'(?:getElementById\(\s*["\']([\w-]+)["\']\s*\)|querySelector\(\s*["\']#([\w-]+)["\']\s*\))\s*\.\s*' + TEXT_PROPS + r'\s*=', script):
        targets.add(m.group(1) or m.group(2))
    for var, el_id in re.findall(r'(?:const|let|var)\s+(\w+)\s*=\s*document\.(?:getElementById\(\s*["\']([\w-]+)["\']\s*\))', script):
        if re.search(r'\b' + re.escape(var) + r'\s*\.\s*' + TEXT_PROPS + r'\s*=', script):
            targets.add(el_id)
    for el_id in sorted(targets):
        inner = element_inner(markup, el_id)
        if inner is not None and re.search(r'<[a-zA-Z]', inner):
            findings.append(f'{comp.name}: R1 text write on #{el_id}, which has child elements (they are deleted at runtime) - write on a leaf span')

    # R2: text mutation inside a lifecycle callback other than onUpdate
    for m in re.finditer(r'\b(onStart|onComplete|onRepeat)\s*:', script):
        body = script[m.end():m.end() + 400]
        cut = re.search(r'\bon(?:Start|Complete|Repeat|Update)\s*:|\btl\.(?:to|from|fromTo|set|add|call)\(', body)
        body = body[:cut.start()] if cut else body
        if re.search(TEXT_PROPS, body):
            line = script[:m.start()].count('\n') + 1
            findings.append(f'{comp.name}: R2 text mutated in {m.group(1)} (script line ~{line}); seek-based QC never fires it - pre-author the text, toggle autoAlpha')

for f in findings:
    print('FAIL', f)
print(f'[comp_lint] {"FAIL" if findings else "PASS"} - {len(findings)} finding(s) in {len(list((ep / "compositions").glob("*.html")))} comps')
sys.exit(1 if findings else 0)
