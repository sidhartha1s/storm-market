#!/usr/bin/env python3
"""One-shot: clip Natural Earth 110m admin_0_countries (public domain) to the NW-Pacific
frame (lon 110-160, lat 5-50), project equirectangular onto a 1920x1080 canvas, and emit
SVG path 'd' strings per country -> coastline.json (embedded inline in track-map.html,
never fetched at render time). Source: ne110m.geojson (raw pull already in this dir).
Countries per the map spec: Japan, Taiwan, Philippines, South Korea, North Korea.
Run once; not part of any render pipeline. python3 build_coastline.py
"""
import json, os

LON0, LON1 = 110, 160
LAT0, LAT1 = 5, 50
W, H = 1920, 1080
WANT = {"Japan", "Taiwan", "Philippines", "South Korea", "North Korea"}

def project(lon, lat):
    x = (lon - LON0) / (LON1 - LON0) * W
    y = (LAT1 - lat) / (LAT1 - LAT0) * H
    return round(x, 1), round(y, 1)

def ring_to_path(ring, step=1):
    pts = ring[::step]
    if pts[-1] != ring[-1]:
        pts.append(ring[-1])
    d = []
    for i, (lon, lat) in enumerate(pts):
        x, y = project(lon, lat)
        d.append(f"{'M' if i == 0 else 'L'}{x} {y}")
    d.append("Z")
    return " ".join(d)

HERE = os.path.dirname(os.path.abspath(__file__))
src = json.load(open(os.path.join(HERE, "ne110m.geojson"), encoding="utf-8"))

out = {}
for feat in src["features"]:
    name = feat["properties"].get("NAME")
    if name not in WANT:
        continue
    geom = feat["geometry"]
    polys = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
    paths = []
    total_pts = 0
    for poly in polys:
        exterior = poly[0]
        # keep only rings that touch our frame (avoid unrelated exclaves ballooning the path)
        lons = [c[0] for c in exterior]
        lats = [c[1] for c in exterior]
        if max(lons) < LON0 - 2 or min(lons) > LON1 + 2 or max(lats) < LAT0 - 2 or min(lats) > LAT1 + 2:
            continue
        step = 2 if len(exterior) > 300 else 1
        paths.append(ring_to_path(exterior, step))
        total_pts += len(exterior)
    if paths:
        out[name] = {"d": " ".join(paths), "source_points": total_pts}

out_path = os.path.join(HERE, "coastline.json")
json.dump(out, open(out_path, "w", encoding="utf-8"))
for k, v in out.items():
    print(k, "rings ok, source_points≈", v["source_points"], "path_len", len(v["d"]))
print("wrote", out_path)
