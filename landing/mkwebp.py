import os
from PIL import Image

ASSETS = "assets"

# (src, dst, target_width or None=keep original width)
JOBS = [
    ("cover.jpg", "cover-hero.webp", 860),
    ("cover.jpg", "cover-mini.webp", 350),
    ("headshot.jpg", "headshot.webp", None),
    ("paul-tornado-selfie.jpg", "paul-tornado-selfie.webp", 880),
    ("paul-plywood.jpg", "paul-plywood.webp", 672),
    ("field-kit.jpg", "field-kit.webp", 672),
    ("paul-stage.jpg", "paul-stage.webp", 672),
    ("inside-protection.png", "inside-protection.webp", None),
    ("inside-money.png", "inside-money.webp", None),
    ("inside-binder.png", "inside-binder.webp", None),
    ("inside-week.png", "inside-week.webp", None),
    ("paul-binder.jpg", "paul-binder.webp", 564),
]

total_orig = 0
total_new = 0
results = []

for src, dst, width in JOBS:
    srcpath = os.path.join(ASSETS, src)
    dstpath = os.path.join(ASSETS, dst)
    im = Image.open(srcpath).convert("RGB")
    w, h = im.size
    if width and width < w:
        new_h = round(h * width / w)
        im = im.resize((width, new_h), Image.LANCZOS)
    im.save(dstpath, "WEBP", quality=80, method=6)
    osz = os.path.getsize(srcpath)
    nsz = os.path.getsize(dstpath)
    total_orig += osz
    total_new += nsz
    results.append((src, dst, im.size, osz, nsz))

print(f"{'src':30}{'dst':26}{'size':>12}{'orig':>10}{'new':>10}")
for src, dst, size, osz, nsz in results:
    print(f"{src:30}{dst:26}{str(size):>12}{osz:>10}{nsz:>10}")
print()
print(f"TOTAL original bytes (converted set): {total_orig}")
print(f"TOTAL webp bytes:                     {total_new}")
print(f"Saved: {total_orig - total_new} bytes ({100*(1-total_new/total_orig):.1f}%)")
