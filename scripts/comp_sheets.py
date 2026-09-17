"""One contact sheet per composition window of a rendered draft, for the reader pass.

Usage: python3 scripts/comp_sheets.py episodes/<slug> renders/<file>.mp4 [seconds_per_frame=3]
Writes episodes/<slug>/sheets/<comp-id>_<start>s.jpg (6 columns, 480 px tiles, tile k = start + k*step) and prints the list.
The reader (Sonnet subagent) looks at every sheet; green gates never clear a draft on their own
(owner 17 Sep 26, Dujuan U1 review).
"""
import re, sys, subprocess, pathlib

ep = pathlib.Path(sys.argv[1]); mp4 = ep / sys.argv[2]; step = float(sys.argv[3]) if len(sys.argv) > 3 else 3.0
out = ep / 'sheets'; out.mkdir(exist_ok=True)
html = (ep / 'index.html').read_text(encoding='utf-8')
hosts = re.findall(r'<div[^>]*data-composition-id="([^"]+)"[^>]*data-composition-src="[^"]+"[^>]*data-start="([\d.]+)"[^>]*data-duration="([\d.]+)"', html)
if not hosts:
    sys.exit('no composition hosts in index.html')
for cid, s, d in hosts:
    s, d = float(s), float(d)
    n = max(1, int(d // step) + 1)
    dst = out / f'{cid}_{int(s)}s.jpg'
    cols = 6; rows = -(-n // cols)
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', str(s), '-t', str(d), '-i', str(mp4),
                    '-vf', f'fps=1/{step},scale=480:-1,tile={cols}x{rows}',
                    '-frames:v', '1', '-q:v', '4', str(dst)], check=True)
    print(f'{dst}  {cid} {s:.1f}-{s + d:.1f}s  {n} frames')
