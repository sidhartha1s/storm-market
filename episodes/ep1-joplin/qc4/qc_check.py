import re, subprocess, json, os, sys

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html = open(os.path.join(base, "index.html"), encoding="utf-8").read()

def ffprobe_dur(path):
    if not os.path.exists(path):
        return None
    try:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "default=noprint_wrappers=1:nokey=1", path],
            capture_output=True, text=True, timeout=30
        )
        d = out.stdout.strip()
        return float(d) if d else None
    except Exception as e:
        return None

def get_attr(tag, name, default=None):
    m = re.search(name + r'="([^"]*)"', tag)
    return m.group(1) if m else default

results = {"video": [], "audio_bad": [], "missing": []}

# find all <video ...> and <audio ...> tags (self-closing or with content, non-greedy up to '>')
for m in re.finditer(r'<video\b[^>]*>', html):
    tag = m.group(0)
    vid = get_attr(tag, "id", "?")
    src = get_attr(tag, "src")
    start = float(get_attr(tag, "data-start", "0"))
    dur = float(get_attr(tag, "data-duration", "0"))
    mstart = float(get_attr(tag, "data-media-start", "0"))
    path = os.path.join(base, src) if src else None
    exists = os.path.exists(path) if path else False
    fdur = ffprobe_dur(path) if exists else None
    needed_end = mstart + dur
    results["video"].append({
        "id": vid, "src": src, "start": start, "dur": dur, "mstart": mstart,
        "needed_end": needed_end, "file_dur": fdur, "exists": exists
    })
    if not exists:
        results["missing"].append(("video", vid, src))

for m in re.finditer(r'<audio\b[^>]*>', html):
    tag = m.group(0)
    aid = get_attr(tag, "id", "?")
    src = get_attr(tag, "src")
    start = float(get_attr(tag, "data-start", "0"))
    dur = float(get_attr(tag, "data-duration", "0"))
    path = os.path.join(base, src) if src else None
    exists = os.path.exists(path) if path else False
    fdur = ffprobe_dur(path) if exists else None
    results["audio_bad"].append({
        "id": aid, "src": src, "start": start, "dur": dur, "file_dur": fdur, "exists": exists
    })
    if not exists:
        results["missing"].append(("audio", aid, src))

for m in re.finditer(r'<img\b[^>]*>', html):
    tag = m.group(0)
    iid = get_attr(tag, "id", "?")
    src = get_attr(tag, "src")
    path = os.path.join(base, src) if src else None
    exists = os.path.exists(path) if path else False
    if not exists:
        results["missing"].append(("img", iid, src))

for m in re.finditer(r'<script\b[^>]*src="([^"]+)"', html):
    src = m.group(1)
    if src.startswith("http"):
        continue
    path = os.path.join(base, src)
    if not os.path.exists(path):
        results["missing"].append(("script", "-", src))

print(json.dumps(results, indent=2))
