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
                                   cwd=S.parent, capture_output=True, text=True, check=True).stdout, encoding='utf-8')
with tempfile.TemporaryDirectory() as d:
    ep = Path(d)
    _mk(ep, ERA_FILES)
    r = subprocess.run([sys.executable, str(OLD_NPC), str(ep)], capture_output=True, text=True)
    assert r.returncode == 0 and 'says "2025"' not in r.stdout, \
        f'old code should have missed this (dashed id + non-standard archival dir) but got: {r.stdout}'
OLD_NPC.unlink()
print('narration_picture_check self-check PASS (dashed ids, provenance-era archival, missed-segment gate)')

# Opus review: on-screen media that never gets classified archival (no provenance era row, and
# it lives in media/act1/ — not an ARCHIVAL_DIR_NAMES folder) must not silently PASS with nothing
# checked. Loud [WARN], still exit 0 (owner chose warn, not fail), and the summary count must only
# include rows actually classified archival (year < MODERN_FROM), never modern rows.
EMPTY_WARN_FILES = {
    'index.html': '<div data-start="0" data-duration="2" data-track-index="1" src="media/act1/new.jpg"></div>\n'
                   '<div data-start="2" data-duration="2" data-track-index="1" src="media/act1/untracked.jpg"></div>\n'
                   '<audio id="nx-a1-s1" data-start="0" data-duration="4"></audio>\n',
    'audio/a1-s1.words.json': json.dumps([{"start": 0.1, "text": "2025"}]),
    # new.jpg has a provenance row but it is modern (must not count as archival); untracked.jpg
    # has no provenance row at all AND lives outside ARCHIVAL_DIR_NAMES ("act1", not "archival").
    'media/act1/provenance.csv': 'file,source_url,license,credit,era,note\n'
                                  'new.jpg,https://example,Public domain,Example Archive,2025,modern photo\n',
}
code, out = npc(EMPTY_WARN_FILES)
assert code == 0 and '[WARN] era check had nothing to check: 1 on-screen media file(s) had no provenance era' in out, out
assert 'archival assets tagged: 0' in out, out  # the one provenance row is modern, must not be counted

OLD_MAIN_NPC = S / '_old_main_npc_tmp.py'
# pinned pre-fix commit, never origin/main: after merge origin/main holds the fix and this would go red
OLD_MAIN_NPC.write_text(subprocess.run(['git', 'show', 'f1f435d7:scripts/narration_picture_check.py'],
                                        cwd=S.parent, capture_output=True, text=True, check=True).stdout, encoding='utf-8')
try:
    with tempfile.TemporaryDirectory() as d:
        ep = Path(d)
        _mk(ep, EMPTY_WARN_FILES)
        r = subprocess.run([sys.executable, str(OLD_MAIN_NPC), str(ep)], capture_output=True, text=True)
        assert r.returncode == 0 and '[WARN]' not in r.stdout, \
            f'old code (f1f435d7) should have missed this — silent PASS, no warning: {r.stdout}'
finally:
    OLD_MAIN_NPC.unlink()
print('narration_picture_check self-check PASS (empty-archival loud warn, archival-only count)')

GSAP = (S / '..' / 'library' / 'gallery' / 'gsap.min.js').resolve()


def _stage_ep(files):
    d = tempfile.mkdtemp()
    ep = Path(d)
    _mk(ep, files)
    shutil.copy(GSAP, ep / 'gsap.min.js')
    return ep


def old_rev(rel_path, tmp_name, rev='ad3c9871'):
    out = S / tmp_name
    out.write_text(subprocess.run(['git', 'show', f'{rev}:scripts/{rel_path}'],
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

# Shared staging (stage_comp.mjs): a comp whose timeline comes from a root-relative script
# (`vendor/x.js`, the Three.js convention) must register in overlap_check and occlusion_check the
# same way it does in graphics_qc. Before 26 Sep 26 both staged without <base href="../">, so
# every WebGL comp failed "comp timeline not registered" (MG eval 2).
REL_FILES = {
    'index.html':
        '<div id="host-g-rel" data-composition-id="g-rel" data-composition-src="compositions/g-rel.html" '
        'data-start="0" data-duration="3" data-track-index="2" data-width="1920" data-height="1080"></div>\n',
    'vendor/rel.js':
        "window.__timelines = window.__timelines || {};\n"
        "window.__timelines['g-rel'] = gsap.timeline({ paused: true }).to('#g-rel-lbl', { x: 100, duration: 3 }, 0);\n",
    'compositions/g-rel.html':
        '<!doctype html><html><head><meta charset="UTF-8"></head><body><template>\n'
        '<div id="root" style="position:absolute;inset:0">\n'
        '  <span id="g-rel-lbl" style="position:absolute;left:200px;top:200px;font-size:40px;color:#fff">Label</span>\n'
        '</div>\n<script src="vendor/rel.js"></script>\n</template></body></html>\n',
}
ep = _stage_ep(REL_FILES)
r = subprocess.run(['node', str(S / 'overlap_check.mjs'), str(ep)], capture_output=True, text=True)
assert 'OVERLAP CHECK v2' in r.stdout and 'not registered' not in r.stdout, r.stdout + r.stderr
old_ov = old_rev('overlap_check.mjs', '_old_overlap_rel_tmp.mjs', 'f3a6fece')
r_old = subprocess.run(['node', str(old_ov), str(ep)], capture_output=True, text=True)
old_ov.unlink()
assert 'comp timeline not registered when staged: g-rel' in r_old.stdout, \
    f'old staging should have missed the root-relative script but got: {r_old.stdout}'
shutil.rmtree(ep, ignore_errors=True)
print('stage_comp self-check PASS (root-relative comp scripts register in overlap_check)')

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


def _rows_check(town_a, time_a, town_b, time_b):
    files = {
        'index.html':
            '<div id="host-rows" data-composition-id="rows" data-composition-src="compositions/rows.html" '
            'data-start="0" data-duration="3" data-track-index="2" data-width="1920" data-height="1080"></div>\n',
        'compositions/rows.html': _bar_comp('rows', town_a, time_a, town_b, time_b),
    }
    d = _stage_ep(files)
    r = subprocess.run(['node', str(S / 'overlap_check.mjs'), str(d)], capture_output=True, text=True)
    shutil.rmtree(d, ignore_errors=True)
    return r.returncode, r.stdout


code, out = _rows_check('TANNER · AL', '6:20 PM CDT', 'TANNER · AL', '7:30 PM CDT')
assert code == 0 and 'dup-fact' not in out, f'same town, different time must not dup-fact: {out}'
code, out = _rows_check('TANNER · AL', '6:20 PM CDT', 'TANNER · AL', '6:20 PM CDT')
assert code == 1 and 'dup-fact' in out, f'an identical repeated row must still dup-fact: {out}'
print('overlap_check self-check PASS (repeated place label vs. genuinely repeated row)')

# ep4-el-reno, 10 Oct 26: one label on several different things ("EF1" on each of two tracks) fails
# dup-fact until it is declared with data-repeat-ok="reason"; a collision exemption (data-overlap-ok)
# must not waive the rule.
OVL = '<span data-overlap-ok="x">EF1</span>'
code, out = _rows_check(OVL, 'TRACK A', OVL, 'TRACK B')
assert code == 1 and 'dup-fact: "EF1"' in out, f'data-overlap-ok must not waive dup-fact: {out}'
REP = '<span data-repeat-ok="one rating label per track">EF1</span>'
code, out = _rows_check(REP, 'TRACK A', REP, 'TRACK B')
assert code == 0 and 'dup-fact' not in out, f'a declared repeated label must pass: {out}'
ANC = '<span data-repeat-ok="one rating label per track"><span>EF1</span></span>'
code, out = _rows_check(ANC, 'TRACK A', ANC, 'TRACK B')
assert code == 0 and 'dup-fact' not in out, f'a label declared on an ancestor must pass: {out}'
print('overlap_check self-check PASS (data-repeat-ok declares a label on several things)')

# ---------------------------------------------------------------- graphics_qc.mjs
# qc-gates-07 (stillness HARD) + assets-comps-05 (host duration vs tl duration): a 3s timeline
# mounted in a 7s host window — frozen tail undetected and idle only a warning before. Since
# 26 Sep 26 stillness is one number: a 3 s frozen tail passes, a 4 s one fails as ERROR [idle].
GQC_FILES = {
    'index.html':
        '<div id="host-y-short" data-composition-id="y-short" data-composition-src="compositions/y-short.html" '
        'data-start="0" data-duration="7" data-track-index="2" data-width="1920" data-height="1080"></div>\n',
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
assert r.returncode == 1 and 'ERROR [short-duration]' in r.stdout and 'ERROR [idle]' in r.stdout, r.stdout + r.stderr
old_gqc = old_rev('graphics_qc.mjs', '_old_graphics_qc_tmp.mjs')
r_old = subprocess.run(['node', str(old_gqc), str(ep)], capture_output=True, text=True)
old_gqc.unlink()
assert 'short-duration' not in r_old.stdout and 'ERROR [idle-budget]' not in r_old.stdout, \
    f'old code should have missed the frozen tail and only warned on idle-budget but got: {r_old.stdout}'
shutil.rmtree(ep, ignore_errors=True)
# the 3 s tween ends at 3 s: the 7 s host above (4.0 s tail) fails; a 6.9 s host (3.9 s tail) passes.
# Stillness counts from the END of motion (as beat_density does), so 6.9 s passing proves a
# beat-start-to-cut measure is gone.
ep = _stage_ep({**GQC_FILES, 'index.html': GQC_FILES['index.html'].replace('data-duration="7"', 'data-duration="6.9"')})
r = subprocess.run(['node', str(S / 'graphics_qc.mjs'), str(ep)], capture_output=True, text=True)
shutil.rmtree(ep, ignore_errors=True)
assert '[idle]' not in r.stdout, r.stdout
print('graphics_qc self-check PASS (short-duration vs host window, stillness one number: 4 s hard)')

# A full-frame canvas (Three.js/WebGL) is a rendered background the DOM cannot read. Before
# 26 Sep 26 it counted as "flat background", which with 1 type tier and few DOM elements made every
# WebGL comp 'undesigned' (MG eval 2). Old code: undesigned; new code: not.
CANVAS_FILES = {
    'index.html':
        '<div id="host-g-cv" data-composition-id="g-cv" data-composition-src="compositions/g-cv.html" '
        'data-start="0" data-duration="3" data-track-index="2" data-width="1920" data-height="1080"></div>\n',
    'compositions/g-cv.html':
        '<!doctype html><html><head><meta charset="UTF-8"></head><body><template>\n'
        '<div id="root" style="position:absolute;inset:0;background:#000">\n'
        '  <canvas id="g-cv-gl" width="1920" height="1080" style="position:absolute;left:0;top:0"></canvas>\n'
        '  <span id="g-cv-lbl" style="position:absolute;left:300px;top:300px;font-size:40px;color:#fff">EF5</span>\n'
        '</div>\n<script>\nwindow.__timelines = window.__timelines || {};\n'
        'const tl = gsap.timeline({ paused: true });\n'
        "tl.fromTo('#g-cv-lbl', { x: 0 }, { x: 300, duration: 3, ease: 'power3.out' }, 0);\n"
        "window.__timelines['g-cv'] = tl;\n</script>\n</template></body></html>\n",
}
# The Three.js template animates by redrawing its canvas from a timeline-level onUpdate; the only
# GSAP child is a padding tween on {}. Old code: 'fade-only' (0 kinetic tweens) and a frozen
# window; new code: the onUpdate renderer is one continuous kinetic span.
DRIVEN_FILES = {
    'index.html': CANVAS_FILES['index.html'],
    'compositions/g-cv.html':
        '<!doctype html><html><head><meta charset="UTF-8"></head><body><template>\n'
        '<div id="root" style="position:absolute;inset:0;background:#000">\n'
        '  <canvas id="g-cv-gl" width="1920" height="1080" style="position:absolute;left:0;top:0"></canvas>\n'
        '</div>\n<script>\nwindow.__timelines = window.__timelines || {};\n'
        'const tl = gsap.timeline({ paused: true });\n'
        "const cx = document.getElementById('g-cv-gl').getContext('2d');\n"
        "tl.eventCallback('onUpdate', () => { cx.fillStyle = '#123'; cx.fillRect(0, 0, 1920, 1080); "
        "cx.fillStyle = '#fff'; cx.fillRect(200 + tl.time() * 300, 400, 80, 80); });\n"
        "tl.to({}, { duration: 3 }, 0);\nwindow.__timelines['g-cv'] = tl;\n</script>\n</template></body></html>\n",
}
# One episode, one comp per case, one run per code version: every graphics_qc launch costs a Chromium
# plus render_busy, and a run per case helped push this file past e2e's 600 s cap (27 Sep 26).
# Positives (p): a full-frame canvas is a designed background; an onUpdate canvas renderer is one
# continuous kinetic span (old f3a6fece: undesigned, fade-only). Negatives (n): both relaxations need a
# canvas covering a quarter of the frame, and the span also needs the timeline onUpdate. g-n4: a {}
# clock is not motion for the idle check either (stage_comp.mjs motionSpans, the rule beat_density
# uses): a 1 s slide plus a 7 s clock in a 7 s host idles 6 s; old fbebe442 (pre-fix main) counted
# the clock as a running tween and saw no idle.
small = lambda s: s.replace('width="1920" height="1080"', 'width="100" height="100"')
cv = DRIVEN_FILES['compositions/g-cv.html']
cut = cv.index("tl.eventCallback('onUpdate'")
no_update = cv[:cut] + cv[cv.index('\n', cut) + 1:]
CLOCK = ('<!doctype html><html><head><meta charset="UTF-8"></head><body><template>\n'
         '<div id="root" style="position:absolute;inset:0;background:#000">\n'
         '  <span id="g-cv-lbl" style="position:absolute;left:300px;top:300px;font-size:40px;color:#fff">EF5</span>\n'
         '</div>\n<script>\nwindow.__timelines = window.__timelines || {};\n'
         'const tl = gsap.timeline({ paused: true });\n'
         "tl.fromTo('#g-cv-lbl', { x: 0 }, { x: 300, duration: 1, ease: 'power3.out' }, 0);\n"
         "tl.to({}, { duration: 7 }, 0);\nwindow.__timelines['g-cv'] = tl;\n</script>\n</template></body></html>\n")
# Declared exemptions (t, c, i): a typed sheet with two type tiers by design, and a blurred full-frame copy
# of a photograph behind the whole photograph, are not defects (ep-palm-sunday-1965, 12 Oct 26), and the
# gate could not be told so. data-type-ok="reason" on the comp root exempts flat-type for that comp;
# data-crop-ok="reason" on an img exempts bad-crop for that img. Each one used is printed with its reason.
# An empty reason, a second undeclared img of the same file and the idle rule get nothing. Old 29dfbdca
# (main before this change): the declared comps fail exactly like the undeclared ones.
def _ok_comp(root_attrs, inner, dur=3, clock=''):
    return ('<!doctype html><html><head><meta charset="UTF-8"></head><body><template>\n'
            f'<div id="root" data-composition-id="g-cv" {root_attrs} style="position:absolute;inset:0;background:linear-gradient(#123,#000)">\n'
            f'{inner}'
            '  <div id="ok-box" style="position:absolute;left:200px;top:900px;width:80px;height:80px;background:#c33"></div>\n'
            '</div>\n<script>\nwindow.__timelines = window.__timelines || {};\n'
            'const tl = gsap.timeline({ paused: true });\n'
            f"tl.fromTo('#ok-box', {{ x: 0 }}, {{ x: 400, duration: {dur}, ease: 'power3.out' }}, 0);\n"
            f"{clock}window.__timelines['g-cv'] = tl;\n</script>\n</template></body></html>\n")


# four text nodes in two tiers (60 px and 30 px): flat-type
SHEET = ''.join(f'  <span style="position:absolute;left:200px;top:{top}px;font-size:{px}px;color:#fff">{txt}</span>\n'
                for top, px, txt in ((100, 60, 'State police'), (200, 60, 'Sheriffs'), (320, 30, 'City police'), (400, 30, 'Named stations')))
# a 4:1 picture covering a 1:1 box keeps a quarter of itself: bad-crop, "loses 75%"
photo = lambda attrs, left=0: (f'  <img {attrs} src="media/wide.svg" alt="" style="position:absolute;left:{left}px;top:0;'
                               'width:400px;height:400px;object-fit:cover">\n')
TYPE_WHY, CROP_WHY = 'typed sheet, two tiers by design', 'blurred backdrop behind the whole photograph'
CASES = {  # comp: (source, host s, new output must hold all of, must not hold, why)
    'g-p1': (CANVAS_FILES['compositions/g-cv.html'], 3, [], 'undesigned', 'a full-frame canvas is a designed background'),
    'g-p2': (cv, 3, [], 'fade-only', 'an onUpdate canvas renderer is continuous motion'),
    'g-n1': (small(CANVAS_FILES['compositions/g-cv.html']), 3, ['ERROR [undesigned] flat background'], None, 'a 100 px canvas is not a designed background'),
    'g-n2': (small(cv), 3, ['ERROR [fade-only]'], None, 'a 100 px canvas excuses no stillness'),
    'g-n3': (no_update, 3, ['ERROR [fade-only]'], None, 'a canvas without onUpdate is still'),
    'g-n4': (CLOCK, 7, ['ERROR [idle] 6.0s frozen at 1.0s'], None, 'a {} clock is not motion'),
    'g-t1': (_ok_comp(f'data-type-ok="{TYPE_WHY}"', SHEET), 3, [f'exempt [flat-type] g-t1: only 2 type tier(s) across 4 text elements — mg-quickref Type tiers — declared: {TYPE_WHY}'], 'ERROR', 'a reasoned data-type-ok on the root exempts flat-type and is printed'),
    'g-t2': (_ok_comp('data-type-ok=""', SHEET), 3, ['ERROR [flat-type]'], 'exempt', 'an empty data-type-ok exempts nothing'),
    'g-t3': (_ok_comp('', SHEET), 3, ['ERROR [flat-type]'], 'exempt', 'an undeclared flat sheet still fails'),
    'g-c1': (_ok_comp('', photo(f'data-crop-ok="{CROP_WHY}"')), 3, [f'exempt [bad-crop] g-c1: wide.svg loses 75% (source 4:1 in 1:1 box) — declared: {CROP_WHY}'], 'ERROR', 'a reasoned data-crop-ok on the img exempts bad-crop and is printed'),
    'g-t4': (_ok_comp('', SHEET.replace('<span style="', '<span data-type-ok="x" style="', 1)), 3, ['ERROR [flat-type]'], 'exempt', 'data-type-ok on an inner span of an undeclared root exempts nothing: only the root counts'),
    'g-c2': (_ok_comp('', photo('data-crop-ok="  "')), 3, ['ERROR [bad-crop]'], 'exempt', 'a whitespace-only data-crop-ok exempts nothing'),
    'g-c3': (_ok_comp('', photo('')), 3, ['ERROR [bad-crop]'], 'exempt', 'an undeclared crop still fails'),
    'g-c4': (_ok_comp('', photo(f'data-crop-ok="{CROP_WHY}"') + photo('', 500)), 3, ['ERROR [bad-crop] wide.svg', 'exempt [bad-crop] g-c4:'], None, 'the exemption is per img: an undeclared img of the same file still fails'),
    'g-i1': (_ok_comp(f'data-type-ok="{TYPE_WHY}" data-idle-ok="held on purpose"', SHEET, 1, "tl.to({}, { duration: 7 }, 0);\n"), 7, ['ERROR [idle] 6.0s frozen at 1.0s', 'ERROR [undesigned] 2 type tier(s)', 'exempt [flat-type] g-i1:'], None, 'idle takes no exemption and undesigned still counts the two tiers, flat-type stays exempt beside them'),
}


def case_files(comps):
    """One staged episode holding the named CASES comps."""
    files = {'index.html': ''.join(CANVAS_FILES['index.html'].replace('g-cv', c).replace('data-duration="3"', f'data-duration="{CASES[c][1]}"')
                                   for c in comps),
             'media/wide.svg': '<svg xmlns="http://www.w3.org/2000/svg" width="400" height="100"><rect width="400" height="100" fill="#39c"/></svg>\n'}
    files.update({f'compositions/{c}.html': CASES[c][0].replace('g-cv', c) for c in comps})
    return files


def by_comp(out):
    """graphics_qc stdout split into one block per composition: the lines under its header line plus
    the exempt lines that name it (no block = no defects). The exemptions header ends the last block."""
    blocks, cur = {}, None
    for line in out.splitlines():
        head = line.strip().split(' ')[0]
        if line == '  declared exemptions:':
            cur = None
        elif line.startswith('    exempt ['):
            head = line.split('] ', 1)[1].split(':')[0]
            blocks[head] = blocks.get(head, '') + line + '\n'
        elif line.startswith('  ') and not line.startswith('    ') and head in CASES:
            cur = head
        elif cur:
            blocks[cur] = blocks.get(cur, '') + line + '\n'
    return blocks


ep = _stage_ep(case_files(CASES))
r = subprocess.run(['node', str(S / 'graphics_qc.mjs'), str(ep)], capture_output=True, text=True, encoding='utf-8')
shutil.rmtree(ep, ignore_errors=True)
assert '[graphics_qc]' in r.stdout, r.stdout + r.stderr
got = by_comp(r.stdout)
for c, (_, _, has, lacks, why) in CASES.items():
    assert all(h in got.get(c, '') for h in has) and (lacks is None or lacks not in got.get(c, '')), f'{c} {why}: {r.stdout}'
assert '[idle]' not in got.get('g-p2', ''), f'the renderer span covers the {{}} clock window: {r.stdout}'
assert '\n  declared exemptions:\n    exempt [' in r.stdout and r.stdout.rstrip().endswith(' compositions, 4 exempt'), \
    f'the exempt lines sit under one header and the summary counts them: {r.stdout}'
olds = {}  # each old revision runs only the comps its assertion reads
for rev, comps in (('f3a6fece', ('g-p1', 'g-p2')), ('fbebe442', ('g-n1', 'g-n4')), ('29dfbdca', ('g-t1', 'g-c1'))):
    ep = _stage_ep(case_files(comps))
    old_gq = old_rev('graphics_qc.mjs', f'_old_gqc_{rev}_tmp.mjs', rev)
    olds[rev] = by_comp(subprocess.run(['node', str(old_gq), str(ep)], capture_output=True, text=True, encoding='utf-8').stdout)
    old_gq.unlink()
    shutil.rmtree(ep, ignore_errors=True)
assert 'ERROR [undesigned] flat background' in olds['f3a6fece'].get('g-p1', ''), f'old code should flag the canvas comp: {olds}'
assert 'ERROR [fade-only]' in olds['f3a6fece'].get('g-p2', ''), f'old code should call the canvas renderer fade-only: {olds}'
assert 'flat background' in olds['fbebe442'].get('g-n1', '') and '[idle]' not in olds['fbebe442'].get('g-n4', ''), \
    f'pre-fix main should run and count the {{}} clock as motion: {olds}'
assert 'ERROR [flat-type]' in olds['29dfbdca'].get('g-t1', '') and 'ERROR [bad-crop]' in olds['29dfbdca'].get('g-c1', ''), \
    f'old code should fail the declared comps: {olds}'
print('graphics_qc self-check PASS (canvas background + renderer span, their quarter-frame/onUpdate limits, a {} clock is not motion)')
print('graphics_qc self-check PASS (declared exemptions: data-type-ok and data-crop-ok need a reason, are printed, and reach no other rule or img)')

# ---------------------------------------------------------------- settle frames for the vision pass
# The old reader sampled every 3 s from the comp start, so frame 1 was always mid-reveal. The frames
# must come from the tween schedule: reveal ends 1.2 s (+0.1), exit slide starts 8.5 s (-0.25), and
# the 8 s ambient loop must not count as a reveal.
SETTLE_FILES = {
    'index.html':
        '<div id="host-z" data-composition-id="z" data-composition-src="compositions/z.html" '
        'data-start="0" data-duration="10" data-track-index="2" data-width="1920" data-height="1080"></div>\n',
    'compositions/z.html':
        '<!doctype html><html><head><meta charset="UTF-8"></head><body><template>\n'
        '<div id="root" style="position:absolute;inset:0;background:#000">\n'
        '  <div id="z-card" style="position:absolute;left:200px;top:200px;width:600px;height:200px;background:#c33">Card</div>\n'
        '  <div id="z-glow" style="position:absolute;left:900px;top:600px;width:80px;height:80px;background:#39c"></div>\n'
        '</div>\n<script>\nwindow.__timelines = window.__timelines || {};\n'
        'const tl = gsap.timeline({ paused: true });\n'
        "tl.fromTo('#z-card', { autoAlpha: 0, y: 40 }, { autoAlpha: 1, y: 0, duration: 1.2, ease: 'power3.out' }, 0);\n"
        "tl.to('#z-glow', { rotation: 360, duration: 8, ease: 'none' }, 0.5);\n"
        "tl.to('#z-card', { x: 2200, duration: 1.0, ease: 'power3.in' }, 8.5);\n"
        "tl.to({}, { duration: 0.5 }, 9.5);\nwindow.__timelines['z'] = tl;\n</script>\n</template></body></html>\n",
}
ep = _stage_ep(SETTLE_FILES)
subprocess.run(['node', str(S / 'graphics_qc.mjs'), str(ep)], capture_output=True, text=True)
frames = json.loads((ep / '.qc-tmp' / 'frame_times.json').read_text(encoding='utf-8'))['z']
got = [f['t'] for f in frames]
assert got == [1.3, 4.78, 8.25], f'settle frames should be reveal-done 1.3, mid 4.78, pre-exit 8.25; got {frames}'
shutil.rmtree(ep, ignore_errors=True)
# same comp mounted in a 6 s host: the frames must stay inside what is on screen (ep-1974 g-plane:
# 50 s timeline in a 28.9 s host put frame 3 on the NEXT graphic)
ep = _stage_ep({**SETTLE_FILES, 'index.html': SETTLE_FILES['index.html'].replace('data-duration="10"', 'data-duration="6"')})
subprocess.run(['node', str(S / 'graphics_qc.mjs'), str(ep)], capture_output=True, text=True)
frames = json.loads((ep / '.qc-tmp' / 'frame_times.json').read_text(encoding='utf-8'))['z']
assert max(f['t'] for f in frames) <= 5.95, f'frames past the 6 s host window: {frames}'
shutil.rmtree(ep, ignore_errors=True)


def _one_tween_comp(body):
    return {'index.html': SETTLE_FILES['index.html'],
            'compositions/z.html': SETTLE_FILES['compositions/z.html'].split("const tl = gsap.timeline({ paused: true });\n")[0]
            + "const tl = gsap.timeline({ paused: true });\n" + body
            + "tl.to({}, { duration: 0.5 }, 9.5);\nwindow.__timelines['z'] = tl;\n</script>\n</template></body></html>\n"}


def _frames(files):
    ep = _stage_ep(files)
    subprocess.run(['node', str(S / 'graphics_qc.mjs'), str(ep)], capture_output=True, text=True)
    fr = json.loads((ep / '.qc-tmp' / 'frame_times.json').read_text(encoding='utf-8'))['z']
    shutil.rmtree(ep, ignore_errors=True)
    return [f['t'] for f in fr]

# an exit that fades out at 50 % of the window: pre-exit must sit before it, not at the window end
got = _frames(_one_tween_comp(
    "tl.fromTo('#z-card', { autoAlpha: 0 }, { autoAlpha: 1, duration: 1.0 }, 0);\n"
    "tl.to('#z-card', { opacity: 0, duration: 0.6 }, 5.0);\n"))
assert got[2] == 4.75, f'early exit: pre-exit should be 4.75, got {got}'
# an opening reveal that is still running when the exit starts: frames stay in range, off any tween
got = _frames(_one_tween_comp(
    "tl.fromTo('#z-card', { autoAlpha: 0 }, { autoAlpha: 1, duration: 3.0 }, 0);\n"
    "tl.to('#z-card', { x: 2200, duration: 1.0 }, 2.0);\n"))
assert all(0 <= t <= 9.95 for t in got) and got[0] >= 3.0, f'overlapping opening/exit: frames {got}'
print('graphics_qc self-check PASS (settle frames from the tween schedule, not a fixed 3 s grid)')
