"""Self-check for the two static comp gates: python3 scripts/test_comp_gates.py
Builds a throwaway episode carrying each bug class once and a clean twin; the gates must fail the
first and pass the second."""
import subprocess
import sys
import tempfile
from pathlib import Path

S = Path(__file__).resolve().parent
BAD = '''<template><div class="chip" id="x-note"><span id="x-rule"></span></div><div id="x-sub">a</div>
<script>tl.set("#x-note", { textContent: "hello" }, 1);
tl.to("#x-sub", { duration: 0.01, onStart: () => { document.getElementById("x-sub").textContent = "b"; } }, 2);</script></template>'''
GOOD = '''<template><div class="x-chip" id="x-note"><span id="x-rule"></span><span id="x-text"></span></div>
<script>tl.set("#x-text", { textContent: "hello" }, 1);
tl.to("#x-text", { duration: 1, onUpdate: () => { document.getElementById("x-text").textContent = "1"; } }, 2);</script></template>'''
HOST = '<html><head><style>.chip{left:110px;bottom:300px}</style></head><body></body></html>'


def run(script, comp):
    with tempfile.TemporaryDirectory() as d:
        ep = Path(d)
        (ep / 'compositions').mkdir()
        (ep / 'index.html').write_text(HOST, encoding='utf-8')
        (ep / 'compositions' / 'x.html').write_text(comp, encoding='utf-8')
        r = subprocess.run([sys.executable, str(S / script), str(ep)], capture_output=True, text=True)
        return r.returncode, r.stdout


code, out = run('comp_lint.py', BAD)
assert code == 1 and ' R1 ' in out and ' R2 ' in out, out
code, out = run('comp_lint.py', GOOD)
assert code == 0, out
code, out = run('css_collision.py', BAD)
assert code != 0 and 'chip' in out, out
code, out = run('css_collision.py', GOOD)
assert code == 0, out
print('comp gates self-check PASS (comp_lint R1+R2, css_collision)')
