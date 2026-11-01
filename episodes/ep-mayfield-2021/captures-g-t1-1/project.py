# scratch (never committed): projects the g-t1-1 map data to screen px and checks label boxes against every line.
# Prints numbers; writes only basemap_d.txt into this capture folder. Usage: project.py <repo> [name:x0:y0:x1:y1 ...]
import json, re, sys
R = sys.argv[1]
E = R + '/episodes/ep-mayfield-2021'
S = 0.058                          # camera scale, px per basemap unit
ANCH = (-90.12, 39.30, 795, 140)   # this lon, lat lands on screen x, y
X = lambda lon: 3841 * (lon + 97.576)
Y = lambda lat: -5585 * (lat - 46.6213)
TX = ANCH[2] - X(ANCH[0]) * S
TY = ANCH[3] - Y(ANCH[1]) * S
px = lambda lon, lat: (X(lon) * S + TX, Y(lat) * S + TY)
print('camera: basemap <g transform="translate(%.2f,%.2f) scale(%s)">' % (TX, TY, S))
print('frame lon %.3f..%.3f lat %.3f..%.3f' % ((0 - TX) / S / 3841 - 97.576, (1920 - TX) / S / 3841 - 97.576,
      46.6213 - (1080 - TY) / S / 5585, 46.6213 - (0 - TY) / S / 5585))

def simplify(pts, tol):  # Douglas-Peucker on px points
    if len(pts) < 3: return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1; L = (dx * dx + dy * dy) ** .5 or 1e-9
    d = [abs(dy * (x - x1) - dx * (y - y1)) / L for x, y in pts[1:-1]]
    i = max(range(len(d)), key=d.__getitem__)
    if d[i] <= tol: return [pts[0], pts[-1]]
    return simplify(pts[:i + 2], tol)[:-1] + simplify(pts[i + 1:], tol)
def ring_d(ring, tol=None):
    pts = [px(*c) for c in ring]
    if pts[0] == pts[-1]: pts = pts[:-1]
    if tol: h = len(pts) // 2; pts = simplify(pts[:h + 1], tol)[:-1] + simplify(pts[h:] + [pts[0]], tol)[:-1]
    return 'M' + ' L'.join('%.1f,%.1f' % p for p in pts) + ' Z', pts

lines = {}
w = json.load(open(E + '/research/geo/warnings.geojson'))
for f in w['features']:
    p = f['properties']
    if p['eventid'] == 38: continue
    ring = f['geometry']['coordinates'][0][0]
    d, pts = ring_d(ring)
    lines['poly-' + p['wfo']] = pts
    xs = [a for a, b in pts]; ys = [b for a, b in pts]
    print('polygon %s issued %s (%d vertices) bbox x %.1f..%.1f y %.1f..%.1f\n  d="%s"' % (
        p['wfo'], p['issue'], len(ring), min(xs), max(xs), min(ys), max(ys), d))
c = json.load(open(E + '/compositions/data/g-t1-1-counties-raw.geojson'))
for f in c['features']:
    g = f['geometry']; rings = g['coordinates'] if g['type'] == 'Polygon' else [r[0] for r in g['coordinates']]
    for r in rings:
        d, pts = ring_d(r, 0.4)
        lines['county-' + f['properties']['NAME']] = pts
        print('county %s %s: %d -> %d vertices\n  d="%s"' % (f['properties']['GEOID'], f['properties']['NAME'], len(r), len(pts), d))
s = open(R + '/library/inhouse/master-map-us-canada.html', encoding='utf-8').read()
us = re.search(r'id="mastermap-us" d="([^"]*)"', s).group(1)
subs = [x for x in re.split(r'(?=M)', us) if x.strip()]
keep = []
for i, sp in enumerate(subs):
    n = list(map(float, re.findall(r'-?\d+\.?\d*', sp)))
    pts = [(n[k] * S + TX, n[k + 1] * S + TY) for k in range(0, len(n) - 1, 2)]
    if max(a for a, b in pts) < -50 or min(a for a, b in pts) > 1970 or max(b for a, b in pts) < -50 or min(b for a, b in pts) > 1130:
        continue
    keep.append(sp.strip()); lines['state%d' % i] = pts
print('basemap subpaths in frame: %d of %d, %d chars' % (len(keep), len(subs), sum(map(len, keep))))
open(E + '/captures-g-t1-1/basemap_d.txt', 'w').write(' '.join(keep))

towns = {}
for f in json.load(open(E + '/research/geo/places.geojson'))['features']:
    nm = f['properties']['name']
    if nm in ('Edwardsville', 'Mayfield'):
        lon, lat = f['geometry']['coordinates']; towns[nm] = px(lon, lat)
        print('pin %s (%.6f, %.6f) -> x %.1f y %.1f' % (nm, lon, lat, *towns[nm]))

segs = lambda pts: [(pts[i], pts[(i + 1) % len(pts)]) for i in range(len(pts))]
def seg_hits_box(a, b, box):
    x0, y0, x1, y1 = box
    for k in range(81):
        t = k / 80; x = a[0] + (b[0] - a[0]) * t; y = a[1] + (b[1] - a[1]) * t
        if x0 <= x <= x1 and y0 <= y <= y1: return True
    return False
def edge_x(poly, y):
    return sorted(a[0] + (b[0] - a[0]) * (y - a[1]) / (b[1] - a[1]) for a, b in segs(lines[poly]) if (a[1] - y) * (b[1] - y) <= 0 and a[1] != b[1])
for t, poly in (('Edwardsville', 'poly-LSX'), ('Mayfield', 'poly-PAH')):
    x, y = towns[t]; print(t, 'polygon boundary x at pin height:', ['%.1f' % v for v in edge_x(poly, y)])
for a in sys.argv[2:]:
    n, x0, y0, x1, y1 = a.split(':'); box = tuple(map(float, (x0, y0, x1, y1)))
    hits = [k for k, pts in lines.items() if any(seg_hits_box(p, q, box) for p, q in segs(pts))]
    print('  box %-8s x %.0f..%.0f y %.0f..%.0f  lines crossed: %s' % (n, *box, hits or 'none'))
