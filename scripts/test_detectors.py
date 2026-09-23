"""Self-check for the d-detectors fix round: python3 scripts/test_detectors.py
Builds throwaway episodes carrying each bug class once; each check must FAIL on the old
code and PASS/catch-correctly on the new one (see individual test comments for the git rev
compared against, ad3c9871 — the commit before this fix round).
Covers: narration_picture_check.py (assets-comps-01 / qc-gates-01), overlap_check.mjs
(qc-gates-04/05/06), graphics_qc.mjs (qc-gates-07/08 / assets-comps-05).
comp_lint.py (qc-gates-03) is covered in test_comp_gates.py per the fixer brief.
"""
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

S = Path(__file__).resolve().parent


def _mk(ep, files):
    for rel, content in files.items():
        p = ep / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding='utf-8')


# ---------------------------------------------------------------- narration_picture_check.py
def npc(files):
    with tempfile.TemporaryDirectory() as d:
        ep = Path(d)
        _mk(ep, files)
        r = subprocess.run([sys.executable, str(S / 'narration_picture_check.py'), str(ep)],
                            capture_output=True, text=True)
        return r.returncode, r.stdout


# a dashed nx id, and archival status that only shows up in a per-file provenance `era` column
# (not a hardcoded ARCHIVAL_DIRS folder name) — the exact ep-1974 defect.
ERA_FILES = {
    'index.html': '<div data-start="0" data-duration="2" data-track-index="1" src="media/act1/old.jpg"></div>\n'
                   '<audio id="nx-a1-s1" data-start="0" data-duration="2"></audio>\n',
    'audio/a1-s1.words.json': json.dumps([{"start": 0.1, "text": "2025"}]),
    'media/act1/provenance.csv': 'file,source_url,license,credit,era,note\n'
                                  'old.jpg,https://example,Public domain,Example Archive,1925,period photo\n',
}
code, out = npc(ERA_FILES)
assert code == 1 and 'says "2025"' in out, out

MISSING_SEG_FILES = {
    'index.html': '<audio id="nx-a1-s1" data-start="0" data-duration="2"></audio>\n'
                   '<audio id="nx-a2-s1"></audio>\n',  # markup/regex gap: no data-start/duration
}
code, out = npc(MISSING_SEG_FILES)
assert code == 1 and 'not parsed' in out, out

# old code (ad3c9871): dashed id truncates at the first dash, and ARCHIVAL_DIRS never matches
# media/act1/ — prove both defects on the ERA_FILES fixture.
OLD_NPC = S / '_old_npc_tmp.py'
OLD_NPC.write_text(subprocess.run(['git', 'show', 'ad3c9871:scripts/narration_picture_check.py'],
                                   cwd=S.parent, capture_output=True, text=True).stdout, encoding='utf-8')
with tempfile.TemporaryDirectory() as d:
    ep = Path(d)
    _mk(ep, ERA_FILES)
    r = subprocess.run([sys.executable, str(OLD_NPC), str(ep)], capture_output=True, text=True)
    assert r.returncode == 0 and 'says "2025"' not in r.stdout, \
        f'old code should have missed this (dashed id + non-standard archival dir) but got: {r.stdout}'
OLD_NPC.unlink()
print('narration_picture_check self-check PASS (dashed ids, provenance-era archival, missed-segment gate)')

GSAP = (S / '..' / 'library' / 'gallery' / 'gsap.min.js').resolve()


def _stage_ep(files):
    d = tempfile.mkdtemp()
    ep = Path(d)
    _mk(ep, files)
    shutil.copy(GSAP, ep / 'gsap.min.js')
    return ep


def old_rev(rel_path, tmp_name):
    out = S / tmp_name
    out.write_text(subprocess.run(['git', 'show', f'ad3c9871:scripts/{rel_path}'],
                                   cwd=S.parent, capture_output=True, text=True).stdout, encoding='utf-8')
    return out


# ---------------------------------------------------------------- overlap_check.mjs
# qc-gates-04 (seek suppressEvents) + qc-gates-05 (dup-fact: same-comp AND overlay texts):
# a tl.call sets '#x-fact' text; old seek(rel) with no suppressEvents=false arg never fires it,
# so it reads empty and never collides with the overlay's identical text. A second comp shows
# the same fact twice on two distinct static spans — old addFact only compared cross-source 'who'.
OV_FILES = {
    'index.html':
        '<div id="host-x-fact" data-composition-id="x-fact" data-composition-src="compositions/x-fact.html" '
        'data-start="0" data-duration="3" data-track-index="2" data-width="1920" data-height="1080"></div>\n'
        '<div id="host-x-dup" data-composition-id="x-dup" data-composition-src="compositions/x-dup.html" '
        'data-start="10" data-duration="3" data-track-index="2" data-width="1920" data-height="1080"></div>\n'
        '<div id="ov-fact" data-start="0" data-duration="3" data-track-index="0" '
        'style="position:absolute;left:900px;top:100px;font-size:30px;color:red"><span>80 PERCENT</span></div>\n',
    'compositions/x-fact.html':
        '<!doctype html><html><head><meta charset="UTF-8"></head><body><template>\n'
        '<div id="root" style="position:absolute;inset:0">\n'
        '  <span id="x-fact" style="position:absolute;left:100px;top:100px;font-size:40px;color:#fff"></span>\n'
        '</div>\n<script>\nwindow.__timelines = window.__timelines || {};\n'
        'const tl = gsap.timeline({ paused: true });\n'
        "tl.call(() => { document.getElementById('x-fact').textContent = '80 PERCENT'; }, null, 0.2);\n"
        "tl.to('#root', { duration: 3, opacity: 1 }, 0);\nwindow.__timelines['x-fact'] = tl;\n</script>\n"
        '</template></body></html>\n',
    'compositions/x-dup.html':
        '<!doctype html><html><head><meta charset="UTF-8"></head><body><template>\n'
        '<div id="root" style="position:absolute;inset:0">\n'
        '  <span id="x-dup-a" style="position:absolute;left:100px;top:100px;font-size:40px;color:#fff">42 MILES</span>\n'
        '  <span id="x-dup-b" style="position:absolute;left:1400px;top:900px;font-size:40px;color:#fff">42 MILES</span>\n'
        '</div>\n<script>\nwindow.__timelines = window.__timelines || {};\n'
        'const tl = gsap.timeline({ paused: true });\n'
        "tl.to('#root', { duration: 3, opacity: 1 }, 0);\nwindow.__timelines['x-dup'] = tl;\n</script>\n"
        '</template></body></html>\n',
}
ep = _stage_ep(OV_FILES)
r = subprocess.run(['node', str(S / 'overlap_check.mjs'), str(ep)], capture_output=True, text=True)
assert r.returncode == 1 and 'dup-fact: "80 PERCENT"' in r.stdout and 'dup-fact: "42 MILES"' in r.stdout, r.stdout + r.stderr
old_ov = old_rev('overlap_check.mjs', '_old_overlap_check_tmp.mjs')
r_old = subprocess.run(['node', str(old_ov), str(ep)], capture_output=True, text=True)
old_ov.unlink()
assert r_old.returncode == 0 and 'dup-fact' not in r_old.stdout, \
    f'old code should have missed both (suppressEvents seek + same-comp dup) but got: {r_old.stdout}'
shutil.rmtree(ep, ignore_errors=True)
print('overlap_check self-check PASS (suppressEvents seek, same-comp + overlay dup-fact)')

# PR #88 review: g-scale-hook's TOWNS[] lists "TANNER · AL" twice (Tanner was hit by two
# separate F5s, distinct times) — a bare repeated place-name label is not a duplicate FACT.
# Same town + different time must PASS; an identical row (same town AND same time) must FAIL,
# because its own time — a digit-bearing string — then collides with itself.
def _bar_comp(comp_id, town_a, time_a, town_b, time_b):
    return (
        '<!doctype html><html><head><meta charset="UTF-8"></head><body><template>\n'
        f'<div id="root" style="position:absolute;inset:0">\n'
        f'  <div class="bar" style="position:absolute;left:100px;top:100px">\n'
        f'    <div class="town" style="font-size:20px;color:#fff">{town_a}</div>\n'
        f'    <div class="time" style="font-size:20px;color:#9ab">{time_a}</div>\n'
        f'  </div>\n'
        f'  <div class="bar" style="position:absolute;left:1400px;top:900px">\n'
        f'    <div class="town" style="font-size:20px;color:#fff">{town_b}</div>\n'
        f'    <div class="time" style="font-size:20px;color:#9ab">{time_b}</div>\n'
        f'  </div>\n'
        '</div>\n<script>\nwindow.__timelines = window.__timelines || {};\n'
        'const tl = gsap.timeline({ paused: true });\n'
        f"tl.to('#root', {{ duration: 3, opacity: 1 }}, 0);\nwindow.__timelines['{comp_id}'] = tl;\n</script>\n"
        '</template></body></html>\n'
    )


ROWS_FILES = {
    'index.html':
        '<div id="host-rows-ok" data-composition-id="rows-ok" data-composition-src="compositions/rows-ok.html" '
        'data-start="0" data-duration="3" data-track-index="2" data-width="1920" data-height="1080"></div>\n'
        '<div id="host-rows-bad" data-composition-id="rows-bad" data-composition-src="compositions/rows-bad.html" '
        'data-start="10" data-duration="3" data-track-index="2" data-width="1920" data-height="1080"></div>\n',
    'compositions/rows-ok.html': _bar_comp('rows-ok', 'TANNER · AL', '6:20 PM CDT', 'TANNER · AL', '7:30 PM CDT'),
    'compositions/rows-bad.html': _bar_comp('rows-bad', 'TANNER · AL', '6:20 PM CDT', 'TANNER · AL', '6:20 PM CDT'),
}
ep = _stage_ep(ROWS_FILES)
r = subprocess.run(['node', str(S / 'overlap_check.mjs'), str(ep)], capture_output=True, text=True)
assert 'rows-ok' not in r.stdout or 'TANNER' not in r.stdout.split('rows-bad')[0], \
    f'same town, different time must not dup-fact: {r.stdout}'
assert 'dup-fact' in r.stdout and '6:20 PM' in r.stdout.upper().replace('CDT', 'CDT'), r.stdout
shutil.rmtree(ep, ignore_errors=True)
print('overlap_check self-check PASS (repeated place label vs. genuinely repeated row)')

# ---------------------------------------------------------------- graphics_qc.mjs
# qc-gates-07 (idle-budget HARD) + assets-comps-05 (host duration vs tl duration): a 3s timeline
# mounted in a 6s host window — frozen tail undetected and idle-budget only a warning before.
GQC_FILES = {
    'index.html':
        '<div id="host-y-short" data-composition-id="y-short" data-composition-src="compositions/y-short.html" '
        'data-start="0" data-duration="6" data-track-index="2" data-width="1920" data-height="1080"></div>\n',
    'compositions/y-short.html':
        '<!doctype html><html><head><meta charset="UTF-8"></head><body><template>\n'
        '<div id="root" style="position:absolute;inset:0;background:#000">\n'
        '  <div id="y-box" style="position:absolute;left:200px;top:200px;width:300px;height:100px;background:#c33"></div>\n'
        '</div>\n<script>\nwindow.__timelines = window.__timelines || {};\n'
        'const tl = gsap.timeline({ paused: true });\n'
        "tl.fromTo('#y-box', { x: 0 }, { x: 400, duration: 3, ease: 'power2.out' }, 0);\n"
        "window.__timelines['y-short'] = tl;\n</script>\n</template></body></html>\n",
}
ep = _stage_ep(GQC_FILES)
r = subprocess.run(['node', str(S / 'graphics_qc.mjs'), str(ep)], capture_output=True, text=True)
assert r.returncode == 1 and 'ERROR [short-duration]' in r.stdout and 'ERROR [idle-budget]' in r.stdout, r.stdout + r.stderr
old_gqc = old_rev('graphics_qc.mjs', '_old_graphics_qc_tmp.mjs')
r_old = subprocess.run(['node', str(old_gqc), str(ep)], capture_output=True, text=True)
old_gqc.unlink()
assert 'short-duration' not in r_old.stdout and 'ERROR [idle-budget]' not in r_old.stdout, \
    f'old code should have missed the frozen tail and only warned on idle-budget but got: {r_old.stdout}'
shutil.rmtree(ep, ignore_errors=True)
print('graphics_qc self-check PASS (short-duration vs host window, idle-budget promoted to hard)')
