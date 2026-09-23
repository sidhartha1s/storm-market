"""Fail when the picture contradicts the voice.

The class of defect this exists for: a6-s3b narrated "In March of 2025" over 1925
wreckage photographs for 27 seconds. Nothing caught it — the owner did.

One deterministic check, anchored on word-level timings from audio/<segment>.words.json,
so a claim is tested against whatever is actually on screen at the instant it is spoken:

  ERA   a modern year (>= 1990) spoken while an archival asset is on screen.
        "Archival" is read from the episode's own data, never a hardcoded folder list:
        every media/**/provenance.csv row names a file and (usually) an `era` column —
        the min year found there is authoritative. Rows with no `era` column fall back to
        the oldest year mentioned anywhere else in the row (fetch-date columns excluded,
        so a 2026 scrape date never masks a 1925 photograph). A row that says
        "AI-generated" or "recreation" is never archival, whatever year its notes mention.
        A directory literally named photos/newspapers/film/archival/archive is archival
        for any file inside it that has no provenance row to check at all — the net this
        check used to be, kept only as a fallback once the per-file data runs out.

Exit 1 on any finding, and on any nx-* segment the parser failed to pick up (a regex or
markup gap is a silent hole in this gate, not a clean episode).

A place check used to live here too — town spoken vs town in the filename — and it was
removed under the keep-code-headache-low rule. It needed a growing stoplist of words that
are not towns ("Where", "Morning", "Building", "County", "School") and still printed
thirteen false positives against three real ones. Whether a photograph of the next town
along the track belongs under this sentence is an editorial judgement; it belongs in the
per-segment read, not in a regex.
"""
import csv
import json
import re
import sys
from pathlib import Path

ep = Path(sys.argv[1])
h = (ep / "index.html").read_text(encoding="utf-8", errors="replace")

MODERN_FROM = 1990
ARCHIVAL_DIR_NAMES = {"photos", "newspapers", "film", "archival", "archive"}
YEAR_RE = re.compile(r'\b(1[6-9]\d\d|20\d\d)\b')

# ---------------------------------------------------------------- archival lookup
def _row_year(row):
    """Oldest year in a provenance.csv row, or None. `era`, when present and non-empty, is
    authoritative and nothing else in the row is consulted. `fetched`/`file` are excluded
    from the fallback scan so a scrape date never reads as the asset's era. A row that
    says AI-generated or recreation is never archival."""
    blob = " ".join(str(v) for k, v in row.items() if k not in ("file", "fetched") and v)
    if any(w in blob.lower() for w in ("ai-generated", "recreation")):
        return None
    era = (row.get("era") or "").strip()
    years = [int(y) for y in YEAR_RE.findall(era)] if era else [int(y) for y in YEAR_RE.findall(blob)]
    return min(years) if years else None


def load_asset_years(ep):
    """basename -> declared year, from every media/**/provenance.csv row that names a file."""
    years = {}
    for csv_path in ep.glob("media/**/provenance.csv"):
        with csv_path.open(encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f):
                fname = (row.get("file") or "").strip()
                if not fname:
                    continue
                y = _row_year(row)
                if y is not None:
                    years[Path(fname).name] = y
    return years


ASSET_YEARS = load_asset_years(ep)


def is_archival(name):
    if name.startswith("composition:"):
        return False
    base = Path(name.split("?")[0]).name
    if base in ASSET_YEARS:
        return ASSET_YEARS[base] < MODERN_FROM
    return any(part.lower() in ARCHIVAL_DIR_NAMES for part in Path(name).parts[:-1])


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

total_nx = sorted(set(re.findall(r'<audio\b[^>]*\bid="(nx-[\w-]+)"', h)))

segments = {}       # segment id (dashes kept) -> (start, duration)
for m in re.finditer(r'<audio [^>]*?id="(nx-[\w-]+)"[^>]*data-start="([\d.]+)"[^>]*data-duration="([\d.]+)"', h):
    segments[m.group(1)] = (float(m.group(2)), float(m.group(3)))


def words_file(nx_id):
    """The id and the words.json filename disagree on dashes across episodes (nx-a1-s1 vs
    a1-s1.words.json here, nx-a1s1 vs a1-s1.words.json there) — strip them from both sides."""
    bare = nx_id.replace("nx-", "", 1).replace("-", "")
    for p in (ep / "audio").glob("*.words.json"):
        if p.name.replace(".words.json", "").replace("-", "") == bare:
            return p
    return None


def on_screen(t):
    return [name for a, b, name in pictures if a <= t < b]


era_findings = []
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


def ts(s):
    return f"{int(s) // 60}:{s % 60:05.2f}"


print(f"segments checked: {len(segments)}/{len(total_nx)}   picture windows: {len(pictures)}   archival assets tagged: {len(ASSET_YEARS)}")
print()
missing_ids = sorted(set(total_nx) - set(segments))
if missing_ids:
    print(f"NARRATION/PICTURE FAIL — {len(missing_ids)} nx-* segment(s) not parsed (markup/regex gap):")
    for nx in missing_ids:
        print(f"  {nx:12} id matched but data-start/data-duration did not")
    sys.exit(1)
if era_findings:
    print(f"NARRATION/PICTURE FAIL — {len(era_findings)} era contradiction(s):")
    for nx, t, d in era_findings:
        print(f"  {ts(t)}  {nx:10} {d}")
    sys.exit(1)
print("NARRATION/PICTURE PASS - no modern year spoken over archival footage")
