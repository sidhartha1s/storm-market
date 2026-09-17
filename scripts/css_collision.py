"""Fail when a composition reuses a class name that index.html also styles.

hyperframes mounts every composition inside index.html's DOM, so a host rule like
`.chip { bottom:300px }` leaks into a comp's own `.chip` (Dujuan U1, 17 Sep 26: agency
tags stretched into 720 px panels). Usage: python3 scripts/css_collision.py episodes/<slug>
"""
import re, sys, pathlib

ep = pathlib.Path(sys.argv[1])
classes = lambda css: set(re.findall(r'\.([A-Za-z_][\w-]*)', re.sub(r'/\*.*?\*/', '', css, flags=re.S)))
styles = lambda html: '\n'.join(re.findall(r'<style[^>]*>(.*?)</style>', html, flags=re.S))
host = classes(styles((ep / 'index.html').read_text(encoding='utf-8')))
bad = 0
for comp in sorted((ep / 'compositions').glob('*.html')):
    src = comp.read_text(encoding='utf-8')
    # styled OR merely used: a comp that writes class="chip" with no rule of its own still inherits the host's
    used = {c for attr in re.findall(r'class="([^"]*)"', src) for c in attr.split()}
    shared = sorted(host & (classes(styles(src)) | used))
    if shared:
        bad += 1
        print(f'FAIL {comp.name}: shares host classes {", ".join(shared)}')
print(f'[css_collision] {"FAIL" if bad else "PASS"} — {bad} comps share class names with index.html ({len(host)} host classes)')
sys.exit(1 if bad else 0)
