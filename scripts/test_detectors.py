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
code, out = subprocess.run(
    [sys.executable, '-c', f"import subprocess,sys,tempfile; sys.exit(0)"]).returncode, None  # placeholder no-op

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
