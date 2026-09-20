"""Data transform for g-master-map (no HTML authored here):
1. wiki_tornado_list.txt -> tornadoes_1974.json  (rating, start lat/lon, path miles, UTC start, deaths, states, path text)
2. us-states.geojson -> states_paths.json (SVG path d-strings for the 13 outbreak states + neighbours, projected)
Projection: equirectangular centred on the outbreak box, scaled so the box fills a 1180x1000 stage.
   px = X0 + (lon - LON0) * KX ; py = Y0 - (lat - LAT0) * KY   (KY = KX / cos(mean lat)) - printed for the brief.
"""
import json, math, re, pathlib

here = pathlib.Path(__file__).resolve().parent
ep = here.parent

# ---- 1. tornado rows ----
t = (here / "wiki_tornado_list.txt").read_text(encoding="utf8")
rows = re.split(r"\n\|-\s*\n", t)
out = []
for r in rows:
    m = re.search(r"Storm colour\|cat(\d)\}\}\|\s*F(\d)", r)
    if not m:
        continue
    c = re.search(r"\{\{[Cc]oord\|([-\d.]+)\|([-\d.]+)", r)
    if not c:
        continue
    lines = [l.strip() for l in r.split("\n") if l.strip().startswith("|")]
    path = re.sub(r"\[\[([^\]|]*\|)?([^\]]*)\]\]", r"\2", lines[1][1:]).strip() if len(lines) > 1 else ""
    states = re.findall(r"\[\[[^\]|]*\|([A-Z]{2})\]\]", r)
    tm = re.search(r"\|(\d\d:\d\d)[–-](\d\d:\d\d)", r)
    ln = re.search(r"convert\|([\d.]+)\|mi", r)
    dead = re.search(r"(\d+)(?:–\d+)?&nbsp;deaths", r)
    out.append({"f": int(m.group(2)), "lat": float(c.group(1)), "lon": float(c.group(2)),
                "path": path, "states": states, "utc_start": tm.group(1) if tm else None,
                "utc_end": tm.group(2) if tm else None, "miles": float(ln.group(1)) if ln else None,
                "deaths": int(dead.group(1)) if dead else 0})
(here / "tornadoes_1974.json").write_text(json.dumps(out, indent=1), encoding="utf8")
f5 = [o for o in out if o["f"] == 5]
print("tornadoes parsed:", len(out), "F5:", len(f5), "F4:", sum(o["f"] == 4 for o in out), "deaths:", sum(o["deaths"] for o in out))
for o in f5:
    print("  F5", o["utc_start"], o["miles"], "mi", o["deaths"], "dead |", o["path"][:70])

# ---- 2. projection + state outlines ----
lats = [o["lat"] for o in out]; lons = [o["lon"] for o in out]
LAT0, LON0 = (min(lats) + max(lats)) / 2, (min(lons) + max(lons)) / 2
cosm = math.cos(math.radians(LAT0))
STAGE_W, STAGE_H, X0, Y0 = 1180, 1000, 590, 540
span_lon = (max(lons) - min(lons)) * cosm + 2.0 * cosm
span_lat = (max(lats) - min(lats)) + 2.0
KX = min(STAGE_W / span_lon, STAGE_H / span_lat) * cosm
KY = KX / cosm


def proj(lon, lat):
    return round(X0 + (lon - LON0) * KX, 1), round(Y0 - (lat - LAT0) * KY, 1)


gj = json.loads((ep / "media/maps/us-states.geojson").read_text(encoding="utf8"))
keep = {"Alabama", "Georgia", "Tennessee", "Mississippi", "Kentucky", "Indiana", "Ohio", "Illinois", "Michigan",
        "West Virginia", "Virginia", "North Carolina", "South Carolina", "Missouri", "Arkansas", "Pennsylvania",
        "New York", "Wisconsin", "Iowa", "Florida", "Louisiana"}
paths = {}
for f in gj["features"]:
    name = f["properties"]["name"]
    if name not in keep:
        continue
    g = f["geometry"]
    polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
    d = []
    for poly in polys:
        for ring in poly:
            pts = [proj(lon, lat) for lon, lat in ring]
            d.append("M" + " L".join(f"{x},{y}" for x, y in pts) + " Z")
    paths[name] = " ".join(d)
data = {"projection": {"LAT0": LAT0, "LON0": LON0, "KX": round(KX, 4), "KY": round(KY, 4), "X0": X0, "Y0": Y0,
                       "formula": "px = X0 + (lon - LON0) * KX ; py = Y0 - (lat - LAT0) * KY"},
        "states": paths,
        "tornadoes": [{"f": o["f"], "x": proj(o["lon"], o["lat"])[0], "y": proj(o["lon"], o["lat"])[1],
                       "miles": o["miles"], "deaths": o["deaths"], "utc": o["utc_start"], "path": o["path"]} for o in out]}
(ep / "media/maps/states_paths.json").write_text(json.dumps(data), encoding="utf8")
print("projection:", data["projection"])
print("states written:", len(paths), "| sample px for Xenia 39.63,-84.05 ->", proj(-84.05, 39.63), "| Guin 33.97,-87.91 ->", proj(-87.91, 33.97))
