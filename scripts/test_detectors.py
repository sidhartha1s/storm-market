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
OLD_MAIN_NPC.write_text(subprocess.run(['git', 'show', 'origin/main:scripts/narration_picture_check.py'],
                                        cwd=S.parent, capture_output=True, text=True).stdout, encoding='utf-8')
with tempfile.TemporaryDirectory() as d:
    ep = Path(d)
    _mk(ep, EMPTY_WARN_FILES)
    r = subprocess.run([sys.executable, str(OLD_MAIN_NPC), str(ep)], capture_output=True, text=True)
    assert r.returncode == 0 and '[WARN]' not in r.stdout, \
        f'old code (origin/main) should have missed this — silent PASS, no warning: {r.stdout}'
OLD_MAIN_NPC.unlink()
print('narration_picture_check self-check PASS (empty-archival loud warn, archival-only count)')

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

# comp_sheets.py: a cutaway clip on a higher track hides the comp, so the frame moves earlier; the
# presenter ring spanning the whole mount is an overlay and must not move anything
ep = Path(tempfile.mkdtemp(prefix='cs_'))
(ep / '.qc-tmp').mkdir()
(ep / '.qc-tmp' / 'frame_times.json').write_text(json.dumps({'z': [
    {'t': 1.3, 'why': 'a'}, {'t': 4.78, 'why': 'b'}, {'t': 8.25, 'why': 'c'}]}), encoding='utf-8')
(ep / 'index.html').write_text(
    '<div id="host-z" data-composition-src="compositions/z.html" data-start="0" data-duration="10" data-track-index="2"></div>\n'
    '<section class="clip still-wrap" id="c-1" data-start="7.0" data-duration="2.5" data-track-index="3"></section>\n'
    '<section class="clip" id="pip-ring" data-start="0" data-duration="12" data-track-index="9"></section>\n', encoding='utf-8')
subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'lavfi', '-i', 'color=c=gray:s=320x180:d=12', str(ep / 'cut.mp4')], check=True)
r = subprocess.run([sys.executable, str(S / 'comp_sheets.py'), str(ep), 'cut.mp4', 'z'], capture_output=True, text=True)
assert r.returncode == 0, r.stdout + r.stderr
lines = [l for l in r.stdout.splitlines() if ' z @ ' in l]
assert 'moved from 8.25s' in lines[2] and '(comp 6.95s)' in lines[2], lines
assert 'moved' not in lines[0] and 'moved' not in lines[1], lines
shutil.rmtree(ep, ignore_errors=True)
print('graphics_qc self-check PASS (settle frames from the tween schedule, not a fixed 3 s grid)')
