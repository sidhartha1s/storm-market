import csv, os, subprocess, sys
from PIL import Image

base = r"C:\Users\Sidhartha\Automation Projects\storm-market\library\mini-storms\el-nino-2026\sept-2026"
csv_path = os.path.join(base, "provenance.csv")

with open(csv_path, encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

csv_files = set(r["file"] for r in rows)
disk_files = set(f for f in os.listdir(base) if os.path.isfile(os.path.join(base, f)) and f != "provenance.csv")

print("CSV rows:", len(rows))
print("Disk files:", len(disk_files))
print("In CSV but not on disk:", csv_files - disk_files)
print("On disk but not in CSV:", disk_files - csv_files)

vid_ext = {".mp4", ".gif", ".mov", ".webm", ".mkv"}
img_ext = {".png", ".jpg", ".jpeg", ".gif"}

fail = []
vid_count = 0
for f in sorted(disk_files):
    path = os.path.join(base, f)
    ext = os.path.splitext(f)[1].lower()
    size = os.path.getsize(path)
    ok = False
    kind = ""
    try:
        if ext in {".mp4", ".mov", ".webm", ".mkv"}:
            vid_count += 1
            kind = "video"
            out = subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","default=nk=1:nw=1",path],
                                  capture_output=True, text=True, timeout=30)
            dur = float(out.stdout.strip())
            ok = dur > 0
        elif ext == ".gif":
            kind = "gif"
            im = Image.open(path)
            n = getattr(im, "n_frames", 1)
            ok = im.size[0] > 0 and n >= 1
            if n > 1:
                vid_count += 1
        elif ext in {".png", ".jpg", ".jpeg"}:
            kind = "image"
            im = Image.open(path)
            im.verify()
            ok = True
        else:
            kind = "other"
    except Exception as e:
        ok = False
        print("ERROR", f, e)
    if not ok:
        fail.append(f)
    print(f"{'OK' if ok else 'FAIL'}  {kind:6s} {size/1024:9.1f} KB  {f}")

print()
print("Video-like files (mp4/gif-animated):", vid_count)
print("Failures:", fail if fail else "none")
