"""Phone version of the study page for the in-chat viewer: swaps the desktop style for a narrow one
that uses the chat theme colours, and points images at absolute paths so the viewer can inline them.
Usage: python3 mobile.py <devq_dir>   -> <devq_dir>/shorts-study-mobile.html (+ -check.html with a dark
background, only for a local screenshot)."""
import os, re, sys

q = os.path.abspath(sys.argv[1]).replace("\\", "/")
h = open(f"{q}/shorts-study.html", encoding="utf-8").read()

CSS = """<meta name="viewport" content="width=device-width,initial-scale=1"><style>
body{font:15px/1.5 var(--font-sans,system-ui,sans-serif);color:var(--foreground,#e6e8ec);margin:0}
h1{font-size:21px;margin:0 0 4px} h2{font-size:18px;margin:30px 0 10px;border-bottom:1px solid var(--border,#2a2f3a);padding-bottom:6px}
h3{font-size:16px;margin:0 0 6px} small,.note,th,.reel span{color:var(--muted-foreground,#8d95a5)} small{font-weight:400}
a{color:var(--info,#8ab4ff)} p{margin:6px 0} .note{font-size:13px}
.card{background:var(--card,#171a21);border:1px solid var(--border,#262b36);border-radius:var(--radius,10px);padding:16px;margin:12px 0}
.reels{display:flex;gap:10px;flex-wrap:wrap;margin-top:10px}
.reel{width:calc(50% - 5px);color:inherit;text-decoration:none;font-size:13px} .reel img{width:100%;border-radius:6px;display:block;margin-bottom:4px}
.reel span,.reel em{display:block} .reel em{font-size:12px;line-height:1.35;opacity:.8}
.x{overflow-x:auto} .x table{min-width:560px} .x figure img{width:1000px;max-width:none}
table{border-collapse:collapse;width:100%;margin:8px 0;font-size:14px} td,th{border-bottom:1px solid var(--border,#262b36);padding:6px 8px;text-align:left;vertical-align:top}
th{font-weight:500}
.bd,.bd tbody,.bd tr,.bd td{display:block;min-width:0} .bd th{display:none} .bd td{border:0;padding:0}
.bd tr{border-bottom:1px solid var(--border,#262b36);padding:8px 0} .bd td:first-child{font-size:12px;color:var(--muted-foreground,#8d95a5)}
.bd td:nth-child(2){font-weight:600} .bd td:nth-child(3),.why,figcaption{opacity:.8}
figure{margin:14px 0} figure img{border-radius:8px;display:block} figcaption{font-size:13px;margin-top:4px}
.dir .n{display:inline-block;background:var(--warning,#e0b33c);color:#111;border-radius:50%;width:24px;height:24px;text-align:center;line-height:24px;font-size:14px}
</style>"""

h, n = re.subn(r"<style>.*?</style>", lambda m: CSS, h, count=1, flags=re.S)
assert n == 1, "style block not found"
h = h.replace('src="shorts-study-v2/', f'src="{q}/shorts-study-v2/').replace(' loading="lazy"', "")
# wide tables and the 6-across frame sheets scroll sideways; the sentence tables (.bd) stack instead
h = re.sub(r"(<table>.*?</table>)", r'<div class="x">\1</div>', h, flags=re.S)
h = re.sub(r"(<figure>.*?</figure>)", r'<div class="x">\1</div>', h, flags=re.S)
h = re.sub(r">\s+<", "><", h)
# the in-chat frame cannot follow a link to another page on the laptop
h = h.replace('<a href="shorts-study-v1.html">shorts-study-v1.html</a>', "on the laptop")
missing = [s for s in re.findall(r'src="([^"]+)"', h) if not os.path.exists(s)]
assert not missing, missing
open(f"{q}/shorts-study-mobile.html", "w", encoding="utf-8").write(h)
open(f"{q}/shorts-study-mobile-check.html", "w", encoding="utf-8").write(
    h.replace("</style>", "html{background:#0f1115;padding:0 8px}</style>", 1).replace(f'src="{q}/', 'src="'))
print("chars", len(h), "| images", len(re.findall(r"<img ", h)), "| scroll boxes", h.count('class="x"'))
