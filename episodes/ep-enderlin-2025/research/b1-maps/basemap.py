"""Shared Enderlin basemap for the g-master-map family (B1).

Sources (all in this folder):
  osm_local.json  OpenStreetMap ways (rail, Maple River, ND 46/32, 58th/52nd St SE, CR 38, 140th Ave SE, power lines)
                  and place nodes, Overpass API, OSM base 2026-05-31/06-01. (c) OpenStreetMap contributors, ODbL.
  track.json      NWS Grand Forks damage-survey track (weather.gov/media/fgf/Enderlin.pdf p.2), digitised: map
                  georeferenced on the PIS start/end lat-lon (46.5728 -97.6031 / 46.687 -97.5803); centreline length
                  12.07 mi vs 12.10 official; OSM Maple River, ND 46 and Sheldon land on the NWS basemap.
  regional.json   US state outlines (Census-derived, PublicaMundi us-states.json) + Canada border for the a4 pull north.

World units: X = (lon - LON0) * KX, Y = -(lat - LAT0) * KY, KY = 5600 px per degree latitude (1 mi = 81.1 px).
`python3 basemap.py` writes basemap.json ({svg, regional_svg, pts}); a one-shot transform (never committed, CLAUDE.md tripwire) pasted the SVG into each comp.
"""
import json, math, os
HERE = os.path.dirname(os.path.abspath(__file__))
LAT0, LON0 = 46.630, -97.575
KY = 5600.0
KX = KY * math.cos(math.radians(LAT0))
MI = KY / 69.05  # world px per statute mile


def P(lat, lon):
    return ((lon - LON0) * KX, -(lat - LAT0) * KY)


def rdp(pts, eps):
    if len(pts) < 3:
        return pts
    (x0, y0), (x1, y1) = pts[0], pts[-1]
    dx, dy = x1 - x0, y1 - y0
    n = math.hypot(dx, dy) or 1e-9
    dmax, idx = -1, 0
    for i in range(1, len(pts) - 1):
        d = abs(dy * pts[i][0] - dx * pts[i][1] + x1 * y0 - y1 * x0) / n
        if d > dmax:
            dmax, idx = d, i
    if dmax > eps:
        return rdp(pts[:idx + 1], eps)[:-1] + rdp(pts[idx:], eps)
    return [pts[0], pts[-1]]


def smooth(pts, k):
    h = k // 2; n = len(pts); out = []
    for i in range(n):
        w = pts[max(0, i - h):min(n, i + h + 1)]
        out.append((sum(p[0] for p in w) / len(w), sum(p[1] for p in w) / len(w)))
    out[0], out[-1] = pts[0], pts[-1]
    return out


BOX = (-1250, -1150, 1250, 950)  # world clip box


def clip_runs(pts):
    runs, cur = [], []
    for p in pts:
        if BOX[0] <= p[0] <= BOX[2] and BOX[1] <= p[1] <= BOX[3]:
            cur.append(p)
        elif cur:
            runs.append(cur); cur = []
    if cur:
        runs.append(cur)
    return runs


def d_of(runs, eps=1.2, close=False):
    out = []
    for r in runs:
        r = rdp(r, eps)
        if len(r) < 2:
            continue
        out.append("M" + " L".join("%.1f,%.1f" % p for p in r) + (" Z" if close else ""))
    return " ".join(out)


def build():
    osm = json.load(open(os.path.join(HERE, "osm_local.json")))
    trk = json.load(open(os.path.join(HERE, "track.json")))
    L = {k: [] for k in ("river", "rail", "hwy", "roads", "power")}
    for w in osm["ways"]:
        t = w["tags"]; pts = [P(a, b) for a, b in w["pts"]]
        if t.get("waterway"):
            k = "river"
        elif t.get("railway"):
            k = "rail"
        elif t.get("power"):
            k = "power"
        elif "46" in t.get("ref", "") or "32" in t.get("ref", ""):
            k = "hwy"
        else:
            k = "roads"
        L[k] += clip_runs(pts)
    # 1-mile section grid (ND section roads run on the survey grid)
    g = []
    lat = 46.48
    while lat < 46.80:
        g.append([P(lat, -97.86), P(lat, -97.29)]); lat += 1 / 69.05
    lon = -97.86
    while lon < -97.29:
        g.append([P(46.48, lon), P(46.80, lon)]); lon += 1 / (69.05 * math.cos(math.radians(LAT0)))
    grid = " ".join("M%.1f,%.1f L%.1f,%.1f" % (a[0], a[1], b[0], b[1]) for a, b in g)
    # county lines: Ransom north / Cass south boundary 46.630; Cass west boundary -97.706 (Census 20m counties)
    county = "M%.1f,%.1f L%.1f,%.1f M%.1f,%.1f L%.1f,%.1f" % (*P(46.630, -97.86), *P(46.630, -97.29),
                                                            *P(46.630, -97.706), *P(46.80, -97.706))
    # track
    c = smooth([P(a, b) for a, b in trk["center"]], 9)
    left = smooth([P(a, b) for a, b in trk["left"]], 13); right = smooth([P(a, b) for a, b in trk["right"]], 13)
    swath = "M" + " L".join("%.1f,%.1f" % p for p in rdp(left, 0.6) + rdp(right, 0.6)[::-1]) + " Z"
    cl = rdp(c, 0.5)
    center = "M" + " L".join("%.1f,%.1f" % p for p in cl)
    clen = sum(math.hypot(cl[i + 1][0] - cl[i][0], cl[i + 1][1] - cl[i][1]) for i in range(len(cl) - 1))
    # widest cross-section
    hw = trk["halfw_mi"]; i_w = max(range(len(hw)), key=lambda i: hw[i])
    tw = osm["towns"]
    pts = {
        "enderlin": P(*tw["Enderlin"]), "sheldon": P(*tw["Sheldon"]), "alice": P(*tw["Alice"]), "fargo": P(*tw["Fargo"]),
        "touchdown": c[0], "lift": c[-1], "widest": c[i_w], "widest_l": left[i_w], "widest_r": right[i_w],
        "elie": P(49.91, -97.75), "winnipeg": P(49.895, -97.138), "border49": P(49.0, -97.2),
    }
    # path crossings, found on the centreline
    def cross(test):
        for i in range(len(trk["center"]) - 1):
            if test(trk["center"][i]) != test(trk["center"][i + 1]):
                return c[i], i / (len(c) - 1)
        return None, None
    pts["x_nd46"], f46 = cross(lambda p: p[0] < 46.6295)
    pts["x_52nd"], f52 = cross(lambda p: p[0] < 46.6586)
    pts["x_power"], fpw = cross(lambda p: p[0] < 46.6372)
    # rail crossing: nearest centreline point to any rail vertex
    best = None
    for w in osm["ways"]:
        if w["tags"].get("railway"):
            for a, b in w["pts"]:
                q = P(a, b)
                for i, p in enumerate(c):
                    d = math.hypot(p[0] - q[0], p[1] - q[1])
                    if best is None or d < best[0]:
                        best = (d, p, i / (len(c) - 1))
    pts["x_rail"], frail = best[1], best[2]
    # exact rail x centreline intersection (segment-segment), replaces the nearest-vertex guess
    def seg_x(p1, p2, p3, p4):
        d = (p2[0] - p1[0]) * (p4[1] - p3[1]) - (p2[1] - p1[1]) * (p4[0] - p3[0])
        if abs(d) < 1e-9:
            return None
        t = ((p3[0] - p1[0]) * (p4[1] - p3[1]) - (p3[1] - p1[1]) * (p4[0] - p3[0])) / d
        u = ((p3[0] - p1[0]) * (p2[1] - p1[1]) - (p3[1] - p1[1]) * (p2[0] - p1[0])) / d
        return (p1[0] + t * (p2[0] - p1[0]), p1[1] + t * (p2[1] - p1[1]), t) if 0 <= t <= 1 and 0 <= u <= 1 else None
    for w in osm["ways"]:
        if w["tags"].get("railway"):
            rp = [P(a, b) for a, b in w["pts"]]
            for j in range(len(rp) - 1):
                for i in range(len(c) - 1):
                    h = seg_x(c[i], c[i + 1], rp[j], rp[j + 1])
                    if h:
                        pts["x_rail"], frail = (h[0], h[1]), (i + h[2]) / (len(c) - 1)
    # Maple River crossings
    rv = [P(a, b) for w in osm["ways"] if w["tags"].get("waterway") for a, b in w["pts"]]
    rbest = min(((math.hypot(p[0] - q[0], p[1] - q[1]), p, i) for i, p in enumerate(c) for q in rv[::2]), key=lambda z: z[0])
    pts["x_river"], friver = rbest[1], rbest[2] / (len(c) - 1)
    frac = {"nd46": f46, "52nd": f52, "power": fpw, "rail": frail, "river": friver, "widest": i_w / (len(c) - 1)}
    pts = {k: [round(v[0], 1), round(v[1], 1)] for k, v in pts.items()}
    svg = f'''<g id="{{P}}-l-grid"><path d="{grid}" fill="none" stroke="#5a768f" stroke-opacity="0.13" stroke-width="1" vector-effect="non-scaling-stroke"/></g>
<g id="{{P}}-l-county"><path d="{county}" fill="none" stroke="#7fb2e5" stroke-opacity="0.55" stroke-width="2" stroke-dasharray="14 8" vector-effect="non-scaling-stroke"/></g>
<g id="{{P}}-l-power"><path d="{d_of(L['power'], 1.5)}" fill="none" stroke="#4a5560" stroke-width="1.5" stroke-dasharray="3 5" vector-effect="non-scaling-stroke"/></g>
<g id="{{P}}-l-roads"><path d="{d_of(L['roads'], 1.5)}" fill="none" stroke="#2a3644" stroke-width="2" vector-effect="non-scaling-stroke"/></g>
<g id="{{P}}-l-river"><path d="{d_of(L['river'], 1.2)}" fill="none" stroke="#5a768f" stroke-width="3" stroke-linejoin="round" vector-effect="non-scaling-stroke"/></g>
<g id="{{P}}-l-hwy"><path d="{d_of(L['hwy'], 1.5)}" fill="none" stroke="#93a3b2" stroke-opacity="0.75" stroke-width="3.5" vector-effect="non-scaling-stroke"/></g>
<g id="{{P}}-l-rail"><path d="{d_of(L['rail'], 1.2)}" fill="none" stroke="#c8d3e0" stroke-opacity="0.8" stroke-width="2.5" vector-effect="non-scaling-stroke"/><path d="{d_of(L['rail'], 1.2)}" fill="none" stroke="#c8d3e0" stroke-opacity="0.8" stroke-width="9" stroke-dasharray="1.5 10" vector-effect="non-scaling-stroke"/></g>
<g id="{{P}}-l-town"><circle cx="{pts['enderlin'][0]}" cy="{pts['enderlin'][1]}" r="30" fill="#2a3644" stroke="#93a3b2" stroke-width="2" vector-effect="non-scaling-stroke"/><circle cx="{pts['sheldon'][0]}" cy="{pts['sheldon'][1]}" r="14" fill="#2a3644" stroke="#4a5560" stroke-width="2" vector-effect="non-scaling-stroke"/><circle cx="{pts['alice'][0]}" cy="{pts['alice'][1]}" r="14" fill="#2a3644" stroke="#4a5560" stroke-width="2" vector-effect="non-scaling-stroke"/></g>
<mask id="{{P}}-swm" maskUnits="userSpaceOnUse" x="-3000" y="-3000" width="6000" height="6000"><path id="{{P}}-swmp" d="{center}" fill="none" stroke="#fff" stroke-width="190" stroke-linecap="round" stroke-dasharray="{math.ceil(clen) + 1}" stroke-dashoffset="{math.ceil(clen) + 1}"/></mask>
<g id="{{P}}-l-swathg" mask="url(#{{P}}-swm)"><path id="{{P}}-swath" d="{swath}" fill="#c0392b" fill-opacity="0.38" stroke="#e74c3c" stroke-opacity="0.7" stroke-width="1.5" vector-effect="non-scaling-stroke"/></g>
<g id="{{P}}-l-trackg"><path id="{{P}}-track" d="{center}" fill="none" stroke="#f2f5f8" stroke-width="3" stroke-linecap="round" stroke-dasharray="{math.ceil(clen) + 1}" stroke-dashoffset="{math.ceil(clen) + 1}"/></g>'''
    return svg, pts, frac, math.ceil(clen) + 1


def regional():
    """ND/MN/SD outlines + the 49th parallel, in the same world units, for the a4 pull north."""
    st = json.load(open(os.path.join(HERE, "regional.json")))
    paths = []
    for name, rings in st["states"].items():
        for ring in rings:
            q = rdp([P(a, b) for b, a in ring], 60)
            paths.append("M" + " L".join("%.0f,%.0f" % p for p in q) + " Z")
    border = "M%.0f,%.0f L%.0f,%.0f" % (*P(49.0, -104.5), *P(49.0, -94.5))
    return (f'<path d="{" ".join(paths)}" fill="#0b1016" stroke="#4a5560" stroke-width="1.5" vector-effect="non-scaling-stroke"/>'
            f'<path d="{border}" fill="none" stroke="#7fb2e5" stroke-width="2.5" stroke-dasharray="10 6" vector-effect="non-scaling-stroke"/>')


if __name__ == "__main__":
    svg, pts, frac, tlen = build()
    reg = regional() if os.path.exists(os.path.join(HERE, "regional.json")) else ""
    json.dump({"svg": svg, "regional_svg": reg, "pts": pts, "frac": frac, "track_len": tlen, "MI": MI},
              open(os.path.join(HERE, "basemap.json"), "w"))
    print("svg bytes", len(svg), "regional bytes", len(reg), "track_len", tlen)
    print(json.dumps(pts)); print(json.dumps({k: round(v, 3) for k, v in frac.items()}))
