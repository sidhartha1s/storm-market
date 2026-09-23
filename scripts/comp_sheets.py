"""Settle frames of new or changed compositions from a rendered cut, for the one vision pass.

Usage: python3 scripts/comp_sheets.py episodes/<slug> renders/<file>.mp4 <comp>[,<comp>...]
Needs episodes/<slug>/.qc-tmp/frame_times.json from `node scripts/graphics_qc.mjs` (run it first).
For each named composition, extracts the three frames graphics_qc chose from its tween schedule
(reveal done, mid-hold, pre-exit) at host data-start + comp-local time, so no frame lands mid-reveal.
Writes episodes/<slug>/sheets/frame-qc/<comp>_<n>.jpg + index.html (each frame with its timestamp and
the reason it was picked) and prints the list. The reader is one subagent, rubric in CLAUDE.md
"Verifying graphics".
"""
import html as H, json, re, sys, subprocess, pathlib

if len(sys.argv) != 4:
    sys.exit(__doc__)
ep = pathlib.Path(sys.argv[1]); mp4 = ep / sys.argv[2]; want = sys.argv[3].split(',')
times_file = ep / '.qc-tmp' / 'frame_times.json'
if not times_file.exists():
    sys.exit(f'{times_file} missing: run `node scripts/graphics_qc.mjs {ep}` first')
if not mp4.exists():
    sys.exit(f'render not found: {mp4}')
times = json.loads(times_file.read_text(encoding='utf-8'))
index = (ep / 'index.html').read_text(encoding='utf-8')
hosts = {}
for tag in re.findall(r'<[a-z]+\b[^>]*\bdata-composition-src="compositions/[^"]+\.html"[^>]*>', index):
    name = re.search(r'data-composition-src="compositions/([^"]+)\.html"', tag).group(1)
    start = re.search(r'\bdata-start="([\d.]+)"', tag)
    dur = re.search(r'\bdata-duration="([\d.]+)"', tag)
    if start and dur:
        hosts.setdefault(name, []).append((float(start.group(1)), float(dur.group(1))))

# Picture layers that hide a mounted comp: clips, stills, blackouts and other comps on a higher track
# (ep-1974 g-map-a4: a 5 s aerial-photo cutaway on track 3 over the track-2 map). Holds are empty markers.
layers = []
for tag in re.findall(r'<[a-z]+\b[^>]*\bdata-track-index="\d+"[^>]*>', index):
    cls = (re.search(r'\bclass="([^"]*)"', tag) or [None, ''])[1]
    if not ('clip' in cls.split() and 'hold' not in cls.split()) and 'data-composition-src' not in tag:
        continue
    s, d = re.search(r'\bdata-start="([\d.]+)"', tag), re.search(r'\bdata-duration="([\d.]+)"', tag)
    if s and d:
        layers.append((int(re.search(r'data-track-index="(\d+)"', tag).group(1)), float(s.group(1)), float(s.group(1)) + float(d.group(1))))
track_of = {}
for tag in re.findall(r'<[a-z]+\b[^>]*\bdata-composition-src="compositions/[^"]+\.html"[^>]*>', index):
    tr = re.search(r'data-track-index="(\d+)"', tag)
    track_of[(re.search(r'compositions/([^"]+)\.html', tag).group(1), float(re.search(r'data-start="([\d.]+)"', tag).group(1)))] = int(tr.group(1)) if tr else 0


def covered(at, track, start, dur):
    # a layer spanning the whole mount is a persistent overlay (the presenter circle), not a cutaway
    return any(t > track and s <= at < e and not (s <= start and e >= start + dur) for t, s, e in layers)


def visible_time(t, start, dur, track):
    """Nearest comp-local time to t (backward first, then forward) that no higher layer covers."""
    for k in range(int(dur * 10) + 1):
        for c in (t - k / 10, t + k / 10):
            if 0 <= c <= dur - 0.05 and not covered(start + c, track, start, dur):
                return c
    return None


out = ep / 'sheets' / 'frame-qc'; out.mkdir(parents=True, exist_ok=True)
cards, missing = [], [c for c in want if c not in times or c not in hosts]
if missing:
    sys.exit(f'no frame times or no host mount for: {", ".join(missing)}')
for comp in want:
    for start, dur in hosts[comp]:
        for n, f in enumerate(times[comp], 1):
            # graphics_qc sizes frames to the longest mount; a shorter second mount must not be
            # sampled after it leaves the screen
            if f['t'] > dur - 0.05:
                f = {'t': dur - 0.05, 'why': f['why'] + f' (clamped to this {dur:.2f}s mount)'}
            track = track_of.get((comp, start), 0)
            if covered(start + f['t'], track):
                v = visible_time(f['t'], start, dur, track)
                if v is None:
                    print(f'{comp} @ {start:.2f}s: covered by higher layers for its whole window, no frame taken')
                    break
                f = {'t': v, 'why': f['why'] + f' (moved from {f["t"]:.2f}s: a higher-track clip covers the comp there)'}
            at = start + f['t']
            dst = out / f'{comp}_{int(start)}s_{n}.jpg'
            subprocess.run(['ffmpeg', '-y', '-v', 'error', '-ss', f'{at:.3f}', '-i', str(mp4),
                            '-frames:v', '1', '-vf', 'scale=960:-1', '-q:v', '3', str(dst)], check=True)
            mmss = f'{int(at // 60)}:{at % 60:05.2f}'
            print(f'{dst}  {comp} @ {mmss} (comp {f["t"]:.2f}s): {f["why"]}')
            cards.append(f'<figure><img src="{dst.name}"><figcaption><b>{H.escape(comp)} #{n}</b> · video {mmss} · '
                         f'comp {f["t"]:.2f}s<br>{H.escape(f["why"])}</figcaption></figure>')

(out / 'index.html').write_text(
    '<!doctype html><meta charset="utf-8"><title>frame QC</title><style>'
    'body{font:14px system-ui;background:#f3f8fd;color:#123;margin:20px}h1{color:#1c5fb8}'
    'main{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}figure{margin:0;background:#fff;'
    'border:1px solid #d8e3ef;padding:8px}img{width:100%}figcaption{margin-top:6px}</style>'
    f'<h1>Frame QC · {H.escape(ep.name)}</h1><p>{H.escape(mp4.name)} · three settle frames per composition, '
    'picked from its tween schedule (CLAUDE.md "Verifying graphics")</p><main>' + ''.join(cards) + '</main>',
    encoding='utf-8')
print(f'wrote {out / "index.html"}')
