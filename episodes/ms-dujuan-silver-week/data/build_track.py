#!/usr/bin/env python3
"""One-shot extraction: JMA specifications.json + forecast.json + JTWC warning text ->
data/track.json (agency, time ISO, lat, lon, pressure_hPa, wind_ms/kt/mph, category).
Run once per advisory re-point; not part of any render pipeline. python3 build_track.py
"""
import json, re, glob, os

MS_TO_MPH = 2.2369362920544
KT_TO_MPH = 1.1507794480235

def mph(ms=None, kt=None):
    if ms is not None:
        return round(float(ms) * MS_TO_MPH, 1)
    if kt is not None:
        return round(float(kt) * KT_TO_MPH, 1)
    return None

HERE = os.path.dirname(os.path.abspath(__file__))
spec_path = sorted(glob.glob(os.path.join(HERE, "jma-*-specifications.json")))[-1]
fc_path = sorted(glob.glob(os.path.join(HERE, "jma-*-forecast.json")))[-1]
jtwc_path = os.path.join(HERE, "jtwc-warning04-16sep0900z.txt")

spec = json.load(open(spec_path, encoding="utf-8"))
fc = json.load(open(fc_path, encoding="utf-8"))

title = spec[0]
issue_jst = title["issue"]["JST"]

CAT_LABEL = {"TD": "Tropical Depression", "TS": "Tropical Storm", "STS": "Severe Tropical Storm",
             "TY": "Typhoon", "STY": "Strong Typhoon", "VSTY": "Very Strong Typhoon"}

points = []

# --- JMA past track (preTyphoon polyline, from fc analysis record) ---
analysis_fc = fc[1]
past_track = analysis_fc.get("track", {}).get("preTyphoon", [])
for i, (lat, lon) in enumerate(past_track):
    points.append({
        "agency": "JMA", "kind": "past", "time": None,
        "lat": lat, "lon": lon,
        "pressure_hPa": None, "wind_ms": None, "wind_kt": None, "wind_mph": None,
        "category": None,
    })

# --- JMA current analysis (spec[1]) ---
a = spec[1]
points.append({
    "agency": "JMA", "kind": "current",
    "time": a["validtime"]["UTC"],
    "lat": a["position"]["deg"][0], "lon": a["position"]["deg"][1],
    "pressure_hPa": int(a["pressure"]),
    "wind_ms": int(a["maximumWind"]["sustained"]["m/s"]),
    "wind_kt": int(a["maximumWind"]["sustained"]["kt"]),
    "wind_mph": mph(ms=a["maximumWind"]["sustained"]["m/s"]),
    "gust_mph": mph(ms=a["maximumWind"]["gust"]["m/s"]),
    "category": CAT_LABEL.get(a["category"]["en"], a["category"]["en"]),
    "location_label": a["location"],
})

# --- JMA forecast checkpoints (spec[2:]) matched with fc[2:] for probability circle radius ---
for s_rec, f_rec in zip(spec[2:], fc[2:]):
    radius_km = f_rec.get("probabilityCircle", {}).get("radius")
    radius_km = round(radius_km / 1000, 1) if radius_km else None
    points.append({
        "agency": "JMA", "kind": "forecast",
        "advanced_hours": s_rec["advancedHours"],
        "time": s_rec["validtime"]["UTC"],
        "lat": s_rec["position"]["deg"][0], "lon": s_rec["position"]["deg"][1],
        "pressure_hPa": int(s_rec["pressure"]),
        "wind_ms": int(s_rec["maximumWind"]["sustained"]["m/s"]),
        "wind_kt": int(s_rec["maximumWind"]["sustained"]["kt"]),
        "wind_mph": mph(ms=s_rec["maximumWind"]["sustained"]["m/s"]),
        "gust_mph": mph(ms=s_rec["maximumWind"]["gust"]["m/s"]),
        "category": CAT_LABEL.get(s_rec["category"]["en"], s_rec["category"]["en"]),
        "location_label": s_rec["location"],
        "probability_circle_radius_km": radius_km,
    })

# --- JTWC warning text parse ---
txt = open(jtwc_path, encoding="utf-8").read()
warning_no = re.search(r"WARNING NR (\d+)", txt).group(1)
issue_z = re.search(r"^\w+ \w+ (\d{6})$", txt, re.M).group(1)

def dms_to_dd(s):
    m = re.match(r"(\d+(?:\.\d+)?)([NSEW])", s)
    val, hemi = float(m.group(1)), m.group(2)
    if hemi in ("N", "E") and len(m.group(1).split(".")[0]) <= 2 and hemi == "N":
        val = val  # already decimal-degree form e.g. 15.4N
    if hemi in ("S", "W"):
        val = -val
    return val

# JTWC current position
cur = re.search(r"WARNING POSITION:\s*\n\s*(\d{6})Z --- NEAR ([\d.]+)N ([\d.]+)E", txt)
cur_time, cur_lat, cur_lon = cur.group(1), float(cur.group(2)), float(cur.group(3))
cur_wind = re.search(r"PRESENT WIND DISTRIBUTION:\s*\n\s*MAX SUSTAINED WINDS - (\d+) KT, GUSTS (\d+) KT", txt)
mcp = re.search(r"MINIMUM CENTRAL PRESSURE AT \d+Z IS (\d+) MB", txt)

points.append({
    "agency": "JTWC", "kind": "current",
    "time_z": cur_time + "Z (16 Sep 2026)",
    "lat": cur_lat, "lon": cur_lon,
    "pressure_hPa": int(mcp.group(1)) if mcp else None,
    "wind_kt": int(cur_wind.group(1)),
    "wind_mph": mph(kt=cur_wind.group(1)),
    "gust_mph": mph(kt=cur_wind.group(2)),
    "category": "Tropical Depression",
    "warning_no": warning_no,
})

# JTWC forecast checkpoints
for m in re.finditer(
    r"(\d+) HRS, VALID AT:\s*\n\s*(\d{6})Z --- ([\d.]+)N ([\d.]+)E\s*\n\s*MAX SUSTAINED WINDS - (\d+) KT, GUSTS (\d+) KT",
    txt):
    hrs, z, lat, lon, wind_kt, gust_kt = m.groups()
    points.append({
        "agency": "JTWC", "kind": "forecast",
        "advanced_hours": int(hrs),
        "time_z": z + "Z",
        "lat": float(lat), "lon": float(lon),
        "wind_kt": int(wind_kt), "wind_mph": mph(kt=wind_kt),
        "gust_mph": mph(kt=gust_kt),
        "warning_no": warning_no,
    })

out = {
    "generated_from": {
        "jma_specifications": os.path.basename(spec_path),
        "jma_forecast": os.path.basename(fc_path),
        "jtwc_warning": os.path.basename(jtwc_path),
    },
    "jma_issue_jst": issue_jst,
    "jma_issue_utc": title["issue"].get("UTC") or a["validtime"]["UTC"],
    "jtwc_warning_no": warning_no,
    "jtwc_issue_z": issue_z + "Z",
    "points": points,
}

out_path = os.path.join(HERE, "track.json")
json.dump(out, open(out_path, "w", encoding="utf-8"), indent=2)
print("wrote", out_path, "points:", len(points))
