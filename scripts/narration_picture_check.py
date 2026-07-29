"""Fail when the picture contradicts the voice.

The class of defect this exists for: a6-s3b narrated "In March of 2025" over 1925
wreckage photographs for 27 seconds. Nothing caught it — the owner did.

Two deterministic checks, both anchored on word-level timings from
audio/<segment>.words.json, so a claim is tested against whatever is actually on
screen at the instant it is spoken:

  ERA   a modern year (>= 1990) spoken while an archival asset is on screen.
        media/photos, media/newspapers and media/film are all 1925 material.
        media/stock is era-neutral (weather), media/ai is a labelled recreation,
        and a composition is a designed card — none of those can contradict a date.

  PLACE a town named in the narration while a photograph of a DIFFERENT town is
        on screen. Reported as a warning, not a failure: a wide shot under a
        sentence about the next town along the track is an editorial call, and
        only the editor can settle it.

Exit 1 on any ERA finding.
"""
import json
import re
import sys
from pathlib import Path

ep = Path(sys.argv[1])
h = (ep / "index.html").read_text(encoding="utf-8", errors="replace")

MODERN_FROM = 1990
ARCHIVAL_DIRS = ("media/photos/", "media/newspapers/", "media/film/")

# ---------------------------------------------------------------- windows
pictures = []       # (start, end, src-or-composition-id)
for m in re.finditer(r'<(section|video|div|img)\b([^>]*)>', h):
    attrs = m.group(2)
    st = re.search(r'data-start="([\d.]+)"', attrs)
    du = re.search(r'data-duration="([\d.]+)"', attrs)
    tr = re.search(r'data-track-index="(\d+)"', attrs)
    if not (st and du and tr) or int(tr.group(1)) not in (1, 2):
        continue
    cid = re.search(r'data-composition-id="([^"]+)"', attrs)
    if cid:
        name = "composition:" + cid.group(1)
    else:
        src = re.search(r'src="([^"]+)"', attrs)
        if not src:
            inner = h[m.end():m.end() + 900]
            src = re.search(r'src="([^"]+)"', inner)
        name = src.group(1) if src else "?"
    at, dur = float(st.group(1)), float(du.group(1))
    pictures.append((at, at + dur, name))
pictures.sort()

segments = {}       # segment id -> (start, duration)
for m in re.finditer(r'<audio id="nx-([\w]+)"[^>]*data-start="([\d.]+)"[^>]*data-duration="([\d.]+)"', h):
    segments[m.group(1)] = (float(m.group(2)), float(m.group(3)))


def words_file(nx_id):
    """nx ids drop the dashes: nx-a6s3b <- audio/a6-s3b.words.json."""
    for p in (ep / "audio").glob("*.words.json"):
        if p.name.replace(".words.json", "").replace("-", "") == nx_id:
            return p
    return None


def on_screen(t):
    return [name for a, b, name in pictures if a <= t < b]


def is_archival(name):
    return any(d in name for d in ARCHIVAL_DIRS)


# Place vocabulary, learned from the archival filename convention rather than hardcoded:
# the NWS/archive sets name the town in a fixed slot, "1925_-_<Town>_-_<subject>" or
# "<NN>-<Town>_<subject>". Reading every capitalised token instead treated "Where",
# "Morning" and "Building" as towns and buried the real signal in noise.
TOWN_PATTERNS = (r'1925_-_([A-Z][a-z]+(?:_[A-Z][a-z]+)?)_-_',
                 r'^\d+-([A-Z][a-z]+(?:_[A-Z][a-z]+)?)[_-]')
place_tokens = set()
for _, _, name in pictures:
    if not is_archival(name):
        continue
    stem = Path(name).stem
    for pat in TOWN_PATTERNS:
        m = re.match(pat, stem)
        if m:
            # "De_Soto" is spoken as two words; index the last word of a compound name
            place_tokens.add(m.group(1).split("_")[-1])

era_findings, place_findings = [], []
for nx, (seg_start, seg_dur) in sorted(segments.items(), key=lambda kv: kv[1][0]):
    wf = words_file(nx)
    if not wf:
        era_findings.append((nx, seg_start, "no words.json for this segment"))
        continue
    words = json.loads(wf.read_text(encoding="utf-8"))
    for w in words:
        t = seg_start + float(w["start"])
        text = w["text"]
        for y in re.findall(r'\b(1[89]\d\d|20\d\d)\b', text):
            if int(y) < MODERN_FROM:
                continue
            for name in on_screen(t):
                if is_archival(name):
                    era_findings.append(
                        (nx, t, f'says "{y}" while {name} is on screen'))
        tok = text.strip(".,;:'\"").capitalize()
        if tok in place_tokens:
            for name in on_screen(t):
                if not is_archival(name):
                    continue
                stem = Path(name).stem
                if tok in stem:
                    continue
                other = [p for p in place_tokens if p in stem]
                if other:
                    place_findings.append(
                        (nx, t, f'says "{tok}" over a {"/".join(sorted(set(other)))} photograph ({Path(name).name})'))


def ts(s):
    return f"{int(s) // 60}:{s % 60:05.2f}"


print(f"segments checked: {len(segments)}   picture windows: {len(pictures)}   "
      f"place vocabulary: {len(place_tokens)}")
print()
if place_findings:
    print(f"PLACE warnings ({len(place_findings)}) — editorial, not a failure:")
    for nx, t, d in place_findings:
        print(f"  {ts(t)}  {nx:10} {d}")
    print()
if era_findings:
    print(f"NARRATION/PICTURE FAIL — {len(era_findings)} era contradiction(s):")
    for nx, t, d in era_findings:
        print(f"  {ts(t)}  {nx:10} {d}")
    sys.exit(1)
print("NARRATION/PICTURE PASS - no modern year spoken over archival footage")
