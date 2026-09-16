#!/usr/bin/env python3
"""One-shot: emit the JS data literals (COASTLINE, TRACK) to embed inline in
compositions/track-map.html, sourced from coastline.json + track.json in this dir.
Not fetched at render time -- pasted by hand into the composition per DESIGN.md's
single-file sub-composition contract. python3 build_js_embed.py > _embed.js
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
coast = json.load(open(os.path.join(HERE, "coastline.json"), encoding="utf-8"))
track = json.load(open(os.path.join(HERE, "track.json"), encoding="utf-8"))

coast_min = {k: v["d"] for k, v in coast.items()}

pts = track["points"]
jma_past = [[p["lat"], p["lon"]] for p in pts if p["agency"] == "JMA" and p["kind"] == "past"]
jma_current = next(p for p in pts if p["agency"] == "JMA" and p["kind"] == "current")
jma_forecast = [p for p in pts if p["agency"] == "JMA" and p["kind"] == "forecast"]
jtwc_current = next(p for p in pts if p["agency"] == "JTWC" and p["kind"] == "current")
jtwc_forecast = [p for p in pts if p["agency"] == "JTWC" and p["kind"] == "forecast"]

def strip(p, keys):
    return {k: p[k] for k in keys if k in p and p[k] is not None}

CK = ["advanced_hours", "time", "lat", "lon", "pressure_hPa", "wind_mph", "gust_mph",
      "category", "location_label", "course_en", "speed_mph", "probability_circle_radius_km"]
JK = ["advanced_hours", "time_z", "lat", "lon", "wind_mph", "gust_mph"]

data = {
    "meta": {"jma_issue_jst": track["jma_issue_jst"], "jtwc_warning_no": track["jtwc_warning_no"],
              "jtwc_issue_z": track["jtwc_issue_z"]},
    "jma": {
        "past": jma_past,
        "current": strip(jma_current, ["time", "lat", "lon", "pressure_hPa", "wind_mph", "gust_mph",
                                        "category", "location_label", "course_en", "speed_mph"]),
        "forecast": [strip(p, CK) for p in jma_forecast],
    },
    "jtwc": {
        "current": strip(jtwc_current, ["lat", "lon", "wind_mph", "gust_mph", "movement_deg", "movement_mph"]),
        "forecast": [strip(p, JK) for p in jtwc_forecast],
    },
    "guam": {"lat": 13.444, "lon": 144.794},
}

print("const COASTLINE = " + json.dumps(coast_min, separators=(",", ":")) + ";")
print("const TRACK = " + json.dumps(data, separators=(",", ":")) + ";")
