import os, sys, json, subprocess, csv
import urllib.request

PEXELS_KEY = None
PIXABAY_KEY = None
with open(r"C:\Users\Sidhartha\.claude\.env") as f:
    for line in f:
        line = line.strip()
        if line.startswith("PEXELS_API_KEY="):
            PEXELS_KEY = line.split("=", 1)[1]
        if line.startswith("PIXABAY_API_KEY="):
            PIXABAY_KEY = line.split("=", 1)[1]

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STOCK_DIR = os.path.join(BASE, "media", "stock")
FRAMES_DIR = os.path.join(BASE, "media", "stock_frames")
PROV_CSV = os.path.join(BASE, "media", "provenance.csv")
os.makedirs(STOCK_DIR, exist_ok=True)
os.makedirs(FRAMES_DIR, exist_ok=True)

def pexels_search(query, per_page=8):
    url = f"https://api.pexels.com/videos/search?query={urllib.request.quote(query)}&per_page={per_page}&orientation=landscape"
    req = urllib.request.Request(url, headers={"Authorization": PEXELS_KEY})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def pixabay_search(query, per_page=8):
    url = f"https://pixabay.com/api/videos/?key={PIXABAY_KEY}&q={urllib.request.quote(query)}&per_page={per_page}"
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)

def best_pexels_file(video):
    files = video.get("video_files", [])
    # prefer hd (1080) file, avoid 4k
    candidates = [f for f in files if f.get("width") and f["width"] <= 1920 and f.get("height", 0) <= 1080]
    if not candidates:
        candidates = files
    candidates.sort(key=lambda f: f.get("width", 0), reverse=True)
    return candidates[0] if candidates else None

def download(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r, open(dest, "wb") as out:
        out.write(r.read())

def ffprobe_info(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height,duration",
         "-of", "json", path],
        capture_output=True, text=True
    )
    try:
        d = json.loads(out.stdout)["streams"][0]
        return int(d.get("width", 0)), int(d.get("height", 0)), float(d.get("duration", 0) or 0)
    except Exception:
        return 0, 0, 0

def downscale_1080(path):
    tmp = path + ".tmp.mp4"
    subprocess.run(
        ["ffmpeg", "-y", "-i", path, "-vf", "scale=-2:1080", "-c:a", "copy", tmp],
        capture_output=True
    )
    if os.path.exists(tmp) and os.path.getsize(tmp) > 0:
        os.remove(path)
        os.rename(tmp, path)

def extract_frame(video_path, frame_path):
    subprocess.run(
        ["ffmpeg", "-y", "-i", video_path, "-ss", "1", "-frames:v", "1", frame_path],
        capture_output=True
    )

def append_provenance(fname, source_url, license_, notes):
    header = not os.path.exists(PROV_CSV)
    with open(PROV_CSV, "a", newline="") as f:
        w = csv.writer(f)
        if header:
            w.writerow(["file", "source_url", "license", "fetched", "notes"])
        w.writerow([fname, source_url, license_, "2026-08-01", notes])

def fetch_family(family, terms, source, target=6, min_dur=8):
    accepted = 0
    idx = 1
    for term in terms:
        if accepted >= target:
            break
        try:
            if source == "pexels":
                data = pexels_search(term)
                videos = data.get("videos", [])
            else:
                data = pixabay_search(term)
                videos = data.get("hits", [])
        except Exception as e:
            print(f"[ERR] search failed {source} {term}: {e}")
            continue

        for v in videos:
            if accepted >= target:
                break
            if source == "pexels":
                vf = best_pexels_file(v)
                if not vf:
                    continue
                url = vf["link"]
                src_url = v["url"]
                license_ = "Pexels License"
            else:
                vf_url = None
                vids = v.get("videos", {})
                for q in ("large", "medium", "small"):
                    if q in vids:
                        vf_url = vids[q]["url"]
                        break
                if not vf_url:
                    continue
                url = vf_url
                src_url = f"https://pixabay.com/videos/id-{v['id']}/"
                license_ = "Pixabay License"

            fname = f"{family}-{idx:02d}.mp4"
            dest = os.path.join(STOCK_DIR, fname)
            try:
                download(url, dest)
            except Exception as e:
                print(f"[ERR] download failed {url}: {e}")
                continue

            w, h, dur = ffprobe_info(dest)
            if w == 0:
                print(f"[REJECT] {fname} unreadable")
                os.remove(dest)
                continue
            if dur < min_dur:
                print(f"[REJECT] {fname} too short ({dur:.1f}s)")
                os.remove(dest)
                continue
            if h > 1080 or w > 1920:
                downscale_1080(dest)

            frame_path = os.path.join(FRAMES_DIR, f"{family}-{idx:02d}.jpg")
            extract_frame(dest, frame_path)

            append_provenance(fname, src_url, license_, f"term={term}")
            print(f"[OK] {fname} dur={dur:.1f}s src={src_url}")
            idx += 1
            accepted += 1
    return accepted

if __name__ == "__main__":
    plan = json.loads(sys.argv[1])
    total = 0
    for fam in plan:
        n = fetch_family(fam["family"], fam["terms"], fam["source"], fam.get("target", 6), fam.get("min_dur", 8))
        total += n
        print(f"=== {fam['family']}: {n} accepted ===")
    print(f"TOTAL: {total}")
