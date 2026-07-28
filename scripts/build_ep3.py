#!/usr/bin/env python3
"""Generate episodes/ep3-tristate/index.html from a shot table.

Why generated: v2 was hand-authored and drifted into 88 visual windows of 10s+ (DESIGN.md
allows 4-7s stills, and demands a written reason for anything over 8s). Here the cutting
rhythm is enforced by code — MAX_STILL is a hard clamp, and any window that would exceed it
is split across more assets. Regenerating is cheap, so retiming is cheap.

Graphics are NOT built here. They are sub-compositions in compositions/*.html (DESIGN.md §1)
and are mounted as hosts.
"""
import json
import re
from pathlib import Path

EP = Path(__file__).resolve().parent.parent / "episodes" / "ep3-tristate"
MAX_STILL = 6.5      # hard clamp on a single archival still
MIN_STILL = 3.4
GAP = 0.75           # breath between narration segments

M = json.loads((EP / "audio" / "manifest.json").read_text(encoding="utf-8"))

# measured by scripts/graphics_qc.mjs — a graphic never outlives its own timeline
_dp = EP / "compositions" / "_durations.json"
GDUR = json.loads(_dp.read_text(encoding="utf-8")) if _dp.exists() else {}

# fallback stills used when a graphic finishes before the narration does
TAIL = {
 "a1": ["media/photos/11-Murphysboro_Pre-Tornado_1.png", "media/photos/Annapolis_Business_street.png",
        "media/photos/1925_-_Murphysboro_20_-_Business_District.jpg", "media/photos/12-Murphysboro_Pre-Tornado_2.png",
        "media/photos/1925_-_Murphysboro_11_-_Residential_District.jpg"],
 "a2": ["media/photos/05-Bollinger_County_Damage.png", "media/photos/1925tornado-p2o-b.jpg",
        "media/photos/06-Biehle_Damage.png", "media/photos/07-Perry_County_Destruction.png"],
 "a3": ["media/photos/1925_tornado_damage_7.webp", "media/photos/1925_-_Murphysboro_9_-_General_Damage.jpg",
        "media/photos/1925_tornado_damage_13.png", "media/photos/16-Murphysboro_SW_of_Logan_School.png"],
 "a4": ["media/photos/1925_-_Griffin_-_More_Damage.jpg", "media/photos/1925_-_Griffin_-_Residential_Damage_2.jpg",
        "media/photos/1925_-_Princeton_-_Twisted_Steel_-_IA_GWC.jpg", "media/photos/1925_-_Griffin_-_Griffin_School_3.jpg"],
 "a5": ["media/photos/1925_tornado_damage_4.jpg", "media/photos/1925_tornado_damage_2.webp",
        "media/photos/1925_tornado_damage_8.webp", "media/photos/23-Royalton-Colp_Road_Bridge.png"],
 "a6": ["media/photos/1925_-_De_Soto_-_Business_District2.jpg", "media/photos/1925_-_Murphysboro_29_-_North_9th_Street_Park.jpg",
        "media/photos/1925_-_Princeton_-_Homes_in_Baldwin_Heights_Area_-_IA_PPL.jpg",
        "media/photos/1925_-_Griffin_-_Griffin_School_1.jpg", "media/photos/13-Murphysboro_Aerial.png"],
 "h1": ["media/photos/Wea00238.jpg", "media/photos/1925_tornado_damage_3.webp"],
}

P = "media/photos/"
F = "media/film/"
S = "media/stock/"
N = "media/newspapers/"
A = "media/ai/"

# ---------------------------------------------------------------- shot table
# kind: stills | film | stock | graphic | panel | papers
# panel/graphic reference a composition id in compositions/
SHOTS = {
 "h1-s1": dict(kind="stills", assets=[P+"Wea00238.jpg", P+"1925_-_Murphysboro_8_-_General_Damage.jpg",
        P+"1925_-_Murphysboro_25_-_17th___Victory_Streets.jpg", P+"1925_tornado_damage_3.webp"], card="date"),
 "h1-s2": dict(kind="mixed", assets=[(F+"mvtn-hook-aerial-bank-4s.mp4","film",4.0),
        (F+"mvtn-hook-trainwreck-4s.mp4","film",4.0), (P+"Wea00239_-_Flickr_-_NOAA_Photo_Library.jpg","still",4.6)]),
 "a1-s1":  dict(kind="graphic", id="g-wordban", pad_before=0.0),
 "a1-s1b": dict(kind="panel", id="g-panel-finley", assets=["media/portraits/hazen-portrait-01.jpg",
        P+"Tri_State_Tornado_Drawing.jpg", P+"DocFile__2_.jpg"], fit="contain"),
 "a1-s2":  dict(kind="graphic", id="g-forecast"),
 "a1-s2c": dict(kind="graphic", id="g-sources"),
 "a1-s2b": dict(kind="stills", assets=[P+"11-Murphysboro_Pre-Tornado_1.png", P+"12-Murphysboro_Pre-Tornado_2.png",
        P+"Annapolis_Business_street.png", P+"1925_-_Murphysboro_20_-_Business_District.jpg",
        P+"1925_-_Murphysboro_11_-_Residential_District.jpg", P+"1925_-_Murphysboro_1_-_Corner_of_17th___Walnut.jpg",
        P+"1925_-_Murphysboro_12b_-_Baptist_Church.jpg"]),
 "a1-s3":  dict(kind="graphic", id="g-metmap"),
 "a1-s4":  dict(kind="graphic", id="g-scale"),
 "a1-s4c": dict(kind="stock", assets=[S+"stock-cloudsomen-02.mp4", S+"stock-cloudsrolling-03.mp4",
        S+"stock-lightning-01.mp4", S+"stock-cloudsomen-01.mp4"]),
 "a1-s4d": dict(kind="panel", id="g-panel-lone", assets=[S+"stock-cloudsrolling-01.mp4",
        S+"stock-tornado-01.mp4", S+"stock-cloudsrolling-02.mp4"], stockbed=True),
 "a1-s5":  dict(kind="stills", assets=[A+"ai-farmhouse-morning.png", A+"ai-children-school.png",
        P+"1925_-_Murphysboro_2_-_Murphysboro_Township_High_School.jpg", P+"20-De_Soto_School_1910.png"],
        chip="Recreation"),
 "a2-s1":  dict(kind="graphic", id="g-track-1"),
 "a2-s1c": dict(kind="stills", assets=[P+"02-Annapolis_Destruction.png", P+"03-Leadanna_Damage.png",
        P+"Leadanna_lead_mines_after_1925_tornado.png", P+"05-Bollinger_County_Damage.png",
        P+"1925tornado-p2o-b.jpg", P+"06-Biehle_Damage.png"]),
 "a2-s2":  dict(kind="panel", id="g-panel-annapolis", assets=[P+"02-Annapolis_Destruction.png",
        P+"Annapolis_Business_street.png", P+"03-Leadanna_Damage.png"]),
 "a2-s3":  dict(kind="stills", assets=[P+"06-Biehle_Damage_-_Theo_Holschen_Residence.jpg",
        A+"ai-black-wall-fields.png", P+"07-Perry_County_Destruction.png", P+"1925tornado-p5o-c.jpg",
        P+"1925_tornado_damage_7.webp", P+"1925_tornado_damage_13.png"]),
 "a2-s3b": dict(kind="graphic", id="g-wires"),
 "a2-s4":  dict(kind="graphic", id="g-track-2"),
 "a2-s4b": dict(kind="stills", assets=[P+"25-West_Frankfort_Orient_2_Aerial.png",
        P+"26-West_Frankfort_Coal_Cars.png", P+"X_West_Frankfort3_-_Aerial_View_Orient_No_2_Mine.png",
        P+"1925_tornado_damage_9.webp", P+"1925_tornado_damage_6.webp", S+"stock-cloudsomen-01.mp4"]),
 "a3-s1":  dict(kind="stills", assets=[P+"1925_-_Gorham_-_Main_St.jpg", P+"1925_-_Gorham_-_Missouri_Pacific_Railway.jpg",
        P+"09-Gorham_Boxcars.png", P+"1925_-_Gorham_-_Post_Office_Area.jpg", P+"1925_tornado_damage_3.webp",
        P+"Tri-State_Tornado_JCHS15.jpg"], lower="gorham"),
 "a3-s1b": dict(kind="panel", id="g-panel-gorham", assets=[P+"1925_-_Gorham_-_Post_Office_Area.jpg",
        P+"09-Gorham_Boxcars.png", P+"1925_tornado_damage_7.webp"], quote="gorham"),
 "a3-s2":  dict(kind="mixed", assets=[(F+"mvtn-murphysboro-house-7s.mp4","film",6.0),
        (P+"1925_-_Murphysboro_4_-_M_O_Railroad_Shops.jpg","still",4.6),
        (P+"1925_-_Murphysboro_3_-_14th_St_at_Gartside.jpg","still",4.6),
        (P+"1925_-_Murphysboro_14_-_M_O_Railyards_Aerial.jpg","still",4.6)], lower="murphysboro"),
 "a3-s2b": dict(kind="stills", assets=[P+"1925_-_Murphysboro_22_-_Aerial_View(1).jpg",
        P+"1925_-_Murphysboro_7a_-_Reliance_Mill.jpg", P+"1925_-_Murphysboro_18_-_Brown_Shoe_Company.jpg",
        P+"1925_-_Murphysboro_26_-_Looking_S_from_17th___Hortense.jpg",
        P+"1925_-_Murphysboro_28_-_Corner_of_10th___Walnut.jpg", P+"16-Murphysboro_SW_of_Logan_School.png"]),
 "a3-s3":  dict(kind="stills", assets=[P+"Tri-State_State_Tornado_Damage_Longfellow_School_2.jpg",
        P+"1925_-_Murphysboro_17_-_Longfellow_School.jpg", P+"1925_-_Murphysboro_6_-_Logan_School.jpg",
        P+"1925_-_Murphysboro_10_-_Homes_Destroyed.jpg"]),
 "a3-s3b": dict(kind="papers", assets=[P+"1925_-_Murphysboro_9_-_General_Damage.jpg",
        N+"Chicago_Herald_Examiner_Front_page_1925-03-20.jpg", P+"1925_-_Murphysboro_20_-_Business_District.jpg",
        N+"The_Evansville_Press_Front_page_-_1925_tornado_coverage.jpg"], quote="rows"),
 "a3-s4":  dict(kind="stills", assets=[P+"18-Murphysboro_Fire_Colorized.png", A+"ai-fire-glow-night.png",
        P+"1925_-_Murphysboro_24_-_Blue_Front_Hotel_-_S_17th_St.jpg", P+"1925_-_Murphysboro_21_-_High_School_Aerial.jpg",
        P+"1925_tornado_damage_11.jpg"]),
 "a3-s4c": dict(kind="panel", id="g-panel-murphysboro", assets=[P+"1925_-_Murphysboro_21_-_High_School_Aerial.jpg",
        P+"13-Murphysboro_Aerial.png", P+"1925_-_Murphysboro_8_-_General_Damage.jpg"]),
 "a3-s5":  dict(kind="graphic", id="g-track-3"),
 "a3-s6":  dict(kind="stills", assets=[P+"21-De_Soso_School_Damage_1.png", P+"22-De_Soto_School_Damage_2.png",
        P+"Illinois_-_Desoto_-_NARA_-_23939847.jpg", P+"1925_-_De_Soto_-_Birds_Eye_View.jpg",
        P+"19-De_Soto_Destruction.png", P+"Illinois_-_Desoto_-_NARA_-_23939845.jpg",
        P+"1925_-_De_Soto_-_Aftermath_Where_Homes_Were.jpg"], lower="desoto"),
 "a3-s6b": dict(kind="panel", id="g-panel-desoto", assets=[P+"20-De_Soto_School_1910.png",
        P+"21-De_Soso_School_Damage_1.png", P+"Illinois_-_Desoto_-_NARA_-_23939847__cropped_.jpg"]),
 "a3-s6c": dict(kind="panel", id="g-panel-schools", assets=[P+"24-Plumfield_School_Demolished.png",
        P+"28-White_County_Newman_School.png", P+"X3_Enfield_-_Trousdale_School_SE_of_Town.png",
        P+"1925_-_Griffin_-_Griffin_School_1.jpg"]),
 "a3-s7":  dict(kind="stills", assets=[A+"ai-miners-emerging.png", P+"X_West_Frankfort3_-_Aerial_View_Orient_No_2_Mine.png",
        P+"X_West_Frankfort2_-_Aerial_View_West_Side_of_Town.jpg", P+"X_West_Frankfort1_-_Clyde_Reeds_Home.png",
        P+"X_West_Frankfort4_-_James_Kerley_Home.png", P+"25-West_Frankfort_Orient_2_Aerial.png",
        P+"1925_tornado_damage_10.webp", P+"1925_tornado_damage_12.webp"], lower="wf"),
 "a3-s8":  dict(kind="panel", id="g-panel-parrish", assets=[P+"X1_Hamilton_County_-_Lonnie_Smith_Home.png",
        P+"1925_tornado_damage_5.webp", P+"1925_tornado_damage_1.webp"]),
 "a3-s9":  dict(kind="graphic", id="g-baro"),
 "a4-s1":  dict(kind="graphic", id="g-track-5"),
 "a4-s1d": dict(kind="stills", assets=[P+"29-Griffin_Devastation_1.png",
        P+"1925_-_Griffin_-_Brick_Buildings_Leveled_E_Side_of_Town.jpg", P+"30-Griffin_Devastation_2.png",
        A+"ai-fire-glow-night.png", P+"1925_-_Griffin_-_Home_Demolished_SW_of_Town.jpg",
        P+"1925_-_Griffin_-_More_Damage.jpg"]),
 "a4-s1b": dict(kind="panel", id="g-panel-griffin", assets=[P+"1925_-_Griffin_-_Tents_Amidst_Damage.jpg",
        P+"1925_-_Griffin_-_Residential_Damage_1.jpg", P+"1925_-_Griffin_-_Building_Destroyed.jpg"]),
 "a4-s2":  dict(kind="stills", assets=[P+"1925_-_Princeton_-_Baldwin_Heights_Area_-_IA_PPL.jpg",
        P+"31-Princeton_Heinz_Plant.png", P+"1925_-_Princeton_-_Locomotive_Rolled_-_IA_GWC.jpg",
        P+"1925_-_Princeton_-_Twisted_Steel_-_IA_GWC.jpg",
        P+"1925_-_Princeton_-_Family_on_Foundation_of_Destroyed_Home_-_IA_GWC.jpg"], lower="princeton"),
 "a4-s2b": dict(kind="panel", id="g-panel-princeton", assets=[P+"1925_-_Princeton_-_McCaw_Subdivision_1_-_IA_GWC.jpg",
        P+"1925_-_Princeton_-_McCaw_Subdivision_2_-_IA_GWC.jpg",
        P+"1925_-_Princeton_-_Homes_Destroyed_near_Southern_Shops_-_IA_GWC.jpg",
        P+"1925_-_Princeton_-_Southern_Railway_Blacksmith_Shop_-_IA_PPL.jpg"]),
 "a4-s3":  dict(kind="graphic", id="g-track-7"),
 "a5-s1":  dict(kind="stills", assets=[P+"1925_tornado_damage_14.png", P+"1925_tornado_damage_15.png",
        P+"1925_tornado_damage_11.jpg", A+"ai-wires-down.png", P+"1925_tornado_damage_4.jpg"]),
 "a5-s1b": dict(kind="graphic", id="g-relief"),
 "a5-s1c": dict(kind="panel", id="g-panel-redcross", assets=[P+"23-Royalton-Colp_Road_Bridge.png",
        P+"X_West_Frankfort4_-_James_Kerley_Home.png", P+"1925_tornado_damage_2.webp",
        P+"1925_tornado_damage_8.webp"]),
 "a5-s1d": dict(kind="panel", id="g-panel-nonet", assets=["media/portraits/marvin-portrait-01.jpg",
        P+"1925_tornado_damage_1.webp", P+"07-Perry_County_Destruction.png"], fit="contain"),
 "a5-s2":  dict(kind="papers", assets=[N+"The_Evansville_Press_Front_page_-_1925_tornado_coverage.jpg",
        N+"Marion_Evening_Post_Front_page_-_1925_tornado_coverage.jpg",
        N+"Anderson_Daily_Bulletin_Front_page_-_1925_tornado_coverage.png",
        N+"The_Butte_Daily_Post_Front_page_-_1925_tornado_coverage.jpg"]),
 "a5-s2c": dict(kind="papers", assets=[N+"The_Fresno_Morning_Republican_Front_page_-_1925_tornado_coverage.jpg",
        N+"Chicago_Herald_Examiner_Front_page_1925-03-20.jpg",
        P+"1925_-_Princeton_-_Princeton_Clarion-News_-_IA_GWC.jpg", P+"Pc9-frnt.jpg"]),
 "a5-s3":  dict(kind="mixed", assets=[(F+"mvtn-centerpiece-aerial-30s.mp4","film",14.0),
        (F+"mvtn-aerial-c-8s.mp4","film",8.0), (F+"mvtn-ground-b-6s.mp4","film",6.0),
        (P+"Wea00239_-_Flickr_-_NOAA_Photo_Library.jpg","still",5.0)]),
 "a5-s3b": dict(kind="panel", id="g-panel-cost", assets=[P+"1925_tornado_damage_6.webp",
        P+"1925_tornado_damage_9.webp", P+"07-Perry_County_Destruction.png"]),
 "a5-s4":  dict(kind="panel", id="g-panel-song", assets=[P+"Tri_State_Tornado.jpg",
        P+"1925_-_Murphysboro_29_-_North_9th_Street_Park.jpg"], fit="contain"),
 "a5-s4b": dict(kind="mixed", assets=[(F+"mvtn-rebuild-bricklayers-12s.mp4","film",9.0),
        (P+"1925_-_De_Soto_-_Aftermath_Where_Homes_Were.jpg","still",5.0),
        (P+"1925_-_De_Soto_-_Business_District.jpg","still",5.0),
        (P+"1925_-_De_Soto_-_Business_District2.jpg","still",5.0),
        (P+"1925_-_Princeton_-_Baldwin_Heights_School_2_-_IA_GWC.jpg","still",5.0)]),
 "a6-s1":  dict(kind="graphic", id="g-wordban2"),
 "a6-s2":  dict(kind="graphic", id="g-timeline"),
 "a6-s2b": dict(kind="graphic", id="g-family"),
 "a6-s2c": dict(kind="graphic", id="g-remeasure"),
 "a6-s2d": dict(kind="graphic", id="g-compare"),
 "a6-s3":  dict(kind="graphic", id="g-fujita"),
 "a6-s3c": dict(kind="graphic", id="g-modern"),
 "a6-s3d": dict(kind="graphic", id="g-prep"),
 "a6-s3b": dict(kind="stills", assets=[P+"1925_-_Princeton_-_Princeton_Clarion-News_-_IA_GWC.jpg",
        P+"1925_-_Griffin_-_Building_Destroyed.jpg", P+"1925_-_Griffin_-_Griffin_School_3.jpg",
        P+"1925_-_Princeton_-_Heinz_Plant_1_-_IA_PPL.jpg"]),
 "a6-s3e": dict(kind="stock", assets=[S+"stock-windgrass-01.mp4", S+"stock-rainfield-02.mp4",
        S+"stock-cloudsrolling-03.mp4", S+"stock-windgrass-02.mp4"]),
 "a6-s4d": dict(kind="stills", assets=[P+"13-Murphysboro_Aerial.png", P+"1925_-_Murphysboro_22_-_Aerial_View(1).jpg",
        P+"1925_-_De_Soto_-_Birds_Eye_View.jpg", P+"X_West_Frankfort2_-_Aerial_View_West_Side_of_Town.jpg",
        P+"1925_-_Murphysboro_14_-_M_O_Railyards_Aerial.jpg", P+"1925_tornado_damage_15.png"]),
 "a6-s4":  dict(kind="stills", assets=[P+"1925_-_Princeton_-_Baldwin_Heights_School_1_-_IA_PPL.jpg",
        P+"1925_-_Murphysboro_29_-_North_9th_Street_Park.jpg",
        P+"1925_-_Murphysboro_2_-_Murphysboro_Township_High_School.jpg",
        P+"1925_-_Princeton_-_Homes_in_Baldwin_Heights_Area_-_IA_PPL.jpg",
        P+"20-De_Soto_School_1910.png"]),
 "a6-s5":  dict(kind="graphic", id="g-close"),
}

ORDER = ["h1-s1","h1-s2","a1-s1","a1-s1b","a1-s2","a1-s2c","a1-s2b","a1-s3","a1-s4","a1-s4c","a1-s4d","a1-s5",
 "a2-s1","a2-s1c","a2-s2","a2-s3","a2-s3b","a2-s4","a2-s4b",
 "a3-s1","a3-s1b","a3-s2","a3-s2b","a3-s3","a3-s3b","a3-s4","a3-s4c","a3-s5","a3-s6","a3-s6b","a3-s6c",
 "a3-s7","a3-s8","a3-s9",
 "a4-s1","a4-s1d","a4-s1b","a4-s2","a4-s2b","a4-s3",
 "a5-s1","a5-s1b","a5-s1c","a5-s1d","a5-s2","a5-s2c","a5-s3","a5-s3b","a5-s4","a5-s4b",
 "a6-s1","a6-s2","a6-s2b","a6-s2c","a6-s2d","a6-s3","a6-s3c","a6-s3d","a6-s3b","a6-s3e","a6-s4d","a6-s4","a6-s5"]

# extra breathing room after specific segments (act turns, emotional payoffs)
HOLDS = {  # breathing room after payoffs and at act turns (DESIGN.md: hold 2-4s, then cut hard)
 "h1-s2": 3.5, "a1-s5": 4.0, "a2-s2": 2.5, "a2-s4b": 3.0,
 "a3-s1b": 2.5, "a3-s4c": 5.0, "a3-s6c": 5.0, "a3-s8": 3.0, "a3-s9": 2.5,
 "a4-s1b": 2.5, "a4-s3": 7.0,
 "a5-s1d": 2.5, "a5-s3": 4.0, "a5-s4b": 5.0,
 "a6-s2d": 2.5, "a6-s3e": 3.5, "a6-s4d": 3.0, "a6-s4": 2.5,
}

LOWERS = {
 "gorham": ("GORHAM, ILLINOIS", "2:26 PM — POPULATION 500"),
 "murphysboro": ("MURPHYSBORO, ILLINOIS", "2:34 PM — POPULATION 12,000"),
 "desoto": ("DE SOTO, ILLINOIS", "2:45 PM — POPULATION 600"),
 "wf": ("WEST FRANKFORT, ILLINOIS", "3:00 PM — POPULATION 18,000"),
 "princeton": ("PRINCETON, INDIANA", "4:18 PM — POPULATION 10,000"),
}
QUOTES = {
 "gorham": ("“The air was full of everything — boards, branches of trees,<br>garments, stoves, all churning around together.”",
            "SURVIVOR ACCOUNT — ST. LOUIS POST-DISPATCH, MARCH 1925"),
 "rows": ("“The dead lay in rows, awaiting names.”", "ST. LOUIS POST-DISPATCH, MARCH 1925"),
}


MAX_USES = 3          # owner rule 2026-07-28: an image may return, but 3 times is the ceiling
_USES = {}
_SPARE = []


def _load_spares():
    """Photos not claimed by the shot table, used to keep any single frame under MAX_USES."""
    claimed = set()
    for plan in SHOTS.values():
        for a in plan.get("assets", []):
            claimed.add(a[0] if isinstance(a, tuple) else a)
    for t in TAIL.values():
        claimed.update(t)
    pool = sorted((P + f.name) for f in (EP / "media" / "photos").iterdir()
                  if f.suffix.lower() in (".jpg", ".png", ".webp"))
    return [a for a in pool if a not in claimed]


def pick(asset):
    """Return `asset`, or a fresh spare once it has been used MAX_USES times."""
    if _USES.get(asset, 0) < MAX_USES:
        _USES[asset] = _USES.get(asset, 0) + 1
        return asset
    for sp in _SPARE:
        if _USES.get(sp, 0) < MAX_USES:
            _USES[sp] = _USES.get(sp, 0) + 1
            return sp
    _USES[asset] = _USES.get(asset, 0) + 1
    return asset


def chunk(dur, assets, minw=MIN_STILL, maxw=MAX_STILL):
    """Split a narration window across assets so no single visual exceeds maxw."""
    n_needed = max(1, int(dur / maxw + 0.9999))
    n = max(n_needed, 1)
    if n > len(assets):                       # cycle assets rather than hold one long
        assets = [assets[i % len(assets)] for i in range(n)]
    else:
        assets = assets[:n]
        # if fewer cuts than assets available and each would be < min, use fewer
        while len(assets) > 1 and dur / len(assets) < minw:
            assets = assets[:-1]
    each = dur / len(assets)
    return [(pick(a), each) for a in assets]


def kb_for(i):
    """Alternating Ken Burns moves so consecutive stills never repeat the same push."""
    table = [(1.0, 1.09, 0, -14, 0, -9), (1.09, 1.0, -12, 0, -7, 0), (1.0, 1.08, 0, 12, 0, 8),
             (1.06, 1.14, 0, -10, 0, -12), (1.08, 1.0, 10, 0, 6, 0), (1.0, 1.11, 0, -16, 0, -6)]
    return table[i % len(table)]


def main():
    global _SPARE
    _SPARE = _load_spares()
    vis, gfx, chips, audio = [], [], [], []
    kbs, panels_used, reuse = [], [], {}
    seg_at = {}
    t = 0.0
    idx = 0
    lines_report = []

    for sid in ORDER:
        if sid not in M:
            raise SystemExit(f"[build_ep3] missing narration segment in manifest: {sid}")
        d = M[sid]["duration"]
        plan = SHOTS[sid]
        audio.append(f'  <audio id="nx-{sid.replace("-","")}" src="audio/{sid}.wav" '
                     f'data-start="{t:.2f}" data-duration="{d:.2f}"></audio>')
        seg_start, seg_dur = t, d + HOLDS.get(sid, 0.0)
        seg_at[sid] = seg_start
        kind = plan["kind"]

        if kind == "graphic":
            gid = plan["id"]
            gw = min(GDUR.get(gid, seg_dur), seg_dur)
            gfx.append(f'  <div id="host-{gid}-{idx}" data-composition-id="{gid}" '
                       f'data-composition-src="compositions/{gid}.html" data-start="{seg_start:.2f}" '
                       f'data-duration="{gw:.2f}" data-track-index="2" data-width="1920" data-height="1080"></div>')
            lines_report.append((seg_start, gw, f"GRAPHIC {gid}"))
            leftover = seg_dur - gw
            if leftover > 2.5:      # never park on a finished graphic
                pool = TAIL[sid.split("-")[0]]
                ct2 = seg_start + gw
                for a, w in chunk(leftover, pool):
                    eid = f"t{idx}"
                    reuse[a] = reuse.get(a, 0) + 1
                    cb = f' data-callback="tail cutaway after {gid} completes"' if reuse[a] > 1 else ""
                    vis.append(f'  <section class="clip still-wrap" id="{eid}" data-start="{ct2:.2f}" '
                               f'data-duration="{w:.2f}" data-track-index="1"{cb}>'
                               f'<img id="kb-{eid}" class="archgrade" src="{a}" alt=""></section>')
                    s0, s1, x0, x1, y0, y1 = kb_for(idx)
                    kbs.append(f'["#kb-{eid}",{ct2:.2f},{w:.2f},{s0},{s1},{x0},{x1},{y0},{y1}]')
                    lines_report.append((ct2, w, f"tail {Path(a).name}"))
                    ct2 += w
                    idx += 1
        elif kind in ("stills", "stock", "papers", "mixed", "panel"):
            if kind == "panel":
                gid = plan["id"]
                pw = min(GDUR.get(gid, seg_dur), seg_dur)
                gfx.append(f'  <div id="host-{gid}-{idx}" data-composition-id="{gid}" '
                           f'data-composition-src="compositions/{gid}.html" data-start="{seg_start:.2f}" '
                           f'data-duration="{pw:.2f}" data-track-index="2" data-width="1920" data-height="1080"></div>')
            if kind == "mixed":
                shots, acc = [], 0.0
                for (src, typ, want) in plan["assets"]:
                    shots.append((src, typ, want)); acc += want
                scale = seg_dur / acc if acc else 1
                shots = [(pick(s) if ty == 'still' else s, ty, w * scale) for (s, ty, w) in shots]
                shots = split_overlong(shots, TAIL[sid.split("-")[0]])
            else:
                typ = "stock" if kind == "stock" else ("paper" if kind == "papers" else "still")
                shots = [(a, "stock" if a.endswith(".mp4") else typ, w)
                         for a, w in chunk(seg_dur, plan["assets"])]
            ct = seg_start
            for (src, typ, w) in shots:
                eid = f"v{idx}"
                reuse[src] = reuse.get(src, 0) + 1
                cb = (f' data-callback="motif returns — use {reuse[src]} of this asset"'
                      if reuse[src] > 1 else "")
                if typ in ("film", "stock"):
                    cls = "archgrade" if typ == "film" else "stockgrade"
                    vis.append(f'  <video id="{eid}" class="clip {cls}" src="{src}" data-start="{ct:.2f}" '
                               f'data-duration="{w:.2f}" data-track-index="1" muted{cb}></video>')
                elif typ == "paper" or plan.get("fit") == "contain":
                    vis.append(f'  <section class="clip pfit" id="{eid}" data-start="{ct:.2f}" '
                               f'data-duration="{w:.2f}" data-track-index="1"{cb}>'
                               f'<img class="pbg" src="{src}" alt=""><img id="kb-{eid}" class="pfg archgrade" src="{src}" alt=""></section>')
                else:
                    vis.append(f'  <section class="clip still-wrap" id="{eid}" data-start="{ct:.2f}" '
                               f'data-duration="{w:.2f}" data-track-index="1"{cb}>'
                               f'<img id="kb-{eid}" class="archgrade" src="{src}" alt=""></section>')
                if typ not in ("film", "stock"):
                    s0, s1, x0, x1, y0, y1 = kb_for(idx)
                    kbs.append(f'["#kb-{eid}",{ct:.2f},{w:.2f},{s0},{s1},{x0},{x1},{y0},{y1}]')
                lines_report.append((ct, w, f"{typ} {Path(src).name}"))
                ct += w
                idx += 1

        if plan.get("lower"):
            loc, tm = LOWERS[plan["lower"]]
            chips.append(f'  <section id="lt-{idx}" class="lt clip" data-start="{seg_start + 0.4:.2f}" '
                         f'data-duration="7.0" data-track-index="7"><div class="lt-loc">{loc}</div>'
                         f'<div class="lt-time">{tm}</div></section>')
        if plan.get("quote"):
            q, attr = QUOTES[plan["quote"]]
            qs = seg_start + min(6.0, seg_dur * 0.35)
            chips.append(f'  <section id="q-{idx}" class="quotecard clip" data-start="{qs:.2f}" '
                         f'data-duration="{min(9.0, seg_dur - (qs - seg_start) - 1):.2f}" data-track-index="5">'
                         f'<div class="q">{q}</div><div class="attr">{attr}</div></section>')
        if plan.get("chip"):
            chips.append(f'  <section id="chip-{idx}" class="srclab clip" data-start="{seg_start:.2f}" '
                         f'data-duration="{min(6.0, seg_dur):.2f}" data-track-index="3">{plan["chip"]}</section>')
        if plan.get("card") == "date":
            chips.append(f'  <section class="clip" id="card-date" data-start="0.30" data-duration="14.0" '
                         f'data-track-index="3" style="z-index:8"></section>')
        idx += 1
        t = seg_start + seg_dur + GAP

    total = t + 14.0    # credits tail
    return vis, gfx, chips, audio, kbs, total, lines_report, seg_at


CSS = """
    body { margin: 0; background: #000; font-family: Georgia, 'Times New Roman', serif; }
    #root { position: relative; width: 1920px; height: 1080px; overflow: hidden; background: #05070a; }
    video, .still-wrap { position: absolute; inset: 0; }
    video { width: 100%; height: 100%; object-fit: cover; }
    .still-wrap { overflow: hidden; }
    .still-wrap img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; will-change: transform; }
    .pfit { overflow: hidden; }
    .pfit .pbg { position: absolute; inset: -60px; width: calc(100% + 120px); height: calc(100% + 120px);
      object-fit: cover; filter: blur(34px) brightness(0.5) saturate(0.7); }
    .pfit .pfg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: contain; }
    .clip { position: absolute; inset: 0; }
    .archgrade { filter: sepia(0.28) contrast(1.08) brightness(0.96) saturate(0.8); }
    .stockgrade { filter: saturate(0.55) contrast(1.12) brightness(0.82) sepia(0.12); }
    .lt { position: absolute; inset: auto; left: 110px; bottom: 110px; z-index: 5; font-family: Arial, sans-serif; }
    .lt .lt-loc { display: table; font-family: 'Arial Black', Arial, sans-serif; font-weight: 900; font-size: 52px;
      color: #f2f5f8; background: rgba(5,8,12,0.78); padding: 4px 16px; text-shadow: 0 3px 24px rgba(0,0,0,0.85); }
    .lt .lt-time { display: table; font-weight: 700; font-size: 27px; color: #f5d98b; background: rgba(5,8,12,0.78);
      padding: 6px 14px; margin-top: 10px; letter-spacing: 1px; }
    .quotecard { position: absolute; inset: auto; left: 140px; right: 900px; bottom: 150px; z-index: 6; }
    .quotecard .q { font-family: Georgia, serif; font-style: italic; font-size: 40px; color: #f2f5f8;
      background: rgba(5,8,12,0.74); padding: 16px 30px; line-height: 1.35; text-shadow: 0 2px 18px rgba(0,0,0,0.9); }
    .quotecard .attr { display: table; margin-top: 12px; font-family: Arial, sans-serif; font-weight: 700;
      font-size: 22px; letter-spacing: 3px; color: #d8a13a; background: rgba(5,8,12,0.74); padding: 8px 20px; }
    .srclab { position: absolute; inset: auto; right: 40px; bottom: 34px; z-index: 7; font-family: Arial, sans-serif;
      font-size: 19px; color: rgba(200,211,224,0.78); background: rgba(5,8,12,0.6); padding: 5px 12px; }
    #vignette { position: absolute; inset: 0; pointer-events: none; z-index: 90;
      background: radial-gradient(ellipse at 50% 50%, transparent 52%, rgba(0,0,0,0.5) 100%); }
    #grain { position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; z-index: 91;
      opacity: 0.13; mix-blend-mode: overlay; }
    #grade { position: absolute; inset: 0; pointer-events: none; z-index: 89; mix-blend-mode: soft-light;
      background-color: rgba(255,205,150,0.26); }
"""

BEDS = [  # id, src, start, dur, [(t, vol)] automation
    ("bgm-dread1", "dread-build-loop.mp3"),
    ("bgm-tense1", "tense-curious-loop.mp3"),
    ("bgm-somber1", "aftermath-somber-loop.mp3"),
    ("bgm-tense2", "tense-curious-loop.mp3"),
    ("bgm-somber2", "aftermath-somber-loop.mp3"),
    ("bgm-neutral1", "neutral-underscore-loop.mp3"),
    ("bgm-hope1", "hopeful-resolve-loop.mp3"),
]


def emit(vis, gfx, chips, audio, kbs, total, report, seg_at):
    """Assemble index.html. Music beds are laid against real act boundaries."""
    a2 = seg_at["a2-s1"]; a3 = seg_at["a3-s1"]; a4 = seg_at["a4-s1"]
    a5 = seg_at["a5-s1"]; a6 = seg_at["a6-s1"]; end = total
    beds, bedjs = [], []
    plan = [("bgm-dread1", 36.0, a2 - 1, [(37, 0.09), (a2 - 4, 0.0)]),
            ("bgm-tense1", a2 - 1, a3 - a2 + 1, [(a2, 0.10), (a3 - 4, 0.0)]),
            ("bgm-somber1", a3 - 1, a4 - a3 + 1, [(a3, 0.09), (a4 - 4, 0.0)]),
            ("bgm-tense2", a4 - 1, a5 - a4 + 1, [(a4, 0.09), (a5 - 4, 0.0)]),
            ("bgm-somber2", a5 - 1, a6 - a5 + 1, [(a5, 0.09), (a6 - 4, 0.0)]),
            ("bgm-neutral1", a6 - 1, end - a6 - 60, [(a6, 0.09), (end - 66, 0.0)]),
            ("bgm-hope1", end - 68, 68, [(end - 66, 0.10), (end - 16, 0.14), (end - 4, 0.0)])]
    seen = {}
    for bid, st, dur, autom in plan:
        src = dict(BEDS)[bid]
        seen[src] = seen.get(src, 0) + 1
        cb = f' data-callback="bed returns for the next act"' if seen[src] > 1 else ""
        # loops are 354s; chunk long windows into successive loop windows
        rem, cur, part = dur, st, 0
        while rem > 0:
            w = min(350.0, rem)
            pid = bid if part == 0 else f"{bid}-{part}"
            extra = cb if part == 0 else ' data-callback="bed continues across the act"'
            beds.append(f'  <audio id="{pid}" src="media/music/{src}" data-start="{cur:.2f}" '
                        f'data-duration="{w:.2f}" data-volume="0" data-bed="1"{extra}></audio>')
            bedjs.append(f'  tl.to("#{pid}", {{ volume: 0.09, duration: 2 }}, {cur + 0.5:.2f});')
            bedjs.append(f'  tl.to("#{pid}", {{ volume: 0.0, duration: 1.8 }}, {cur + w - 2.0:.2f});')
            cur += w; rem -= w; part += 1
    sfx = [
        f'  <audio id="sfx-rumble" src="media/sfx/04_distant_storm_rumble.mp3" data-start="0" data-duration="36" data-volume="0" data-bed="1"></audio>',
        f'  <audio id="sfx-wind1" src="media/sfx/02_wind_ominous_steady.mp3" data-start="{seg_at["a1-s5"]-1:.2f}" data-duration="24" data-volume="0" data-bed="1"></audio>',
    ]
    sfxjs = ['  tl.to("#sfx-rumble", { volume: 0.55, duration: 2.0 }, 0.3);',
             '  tl.to("#sfx-rumble", { volume: 0.75, duration: 1.0 }, 16.0);',
             '  tl.to("#sfx-rumble", { volume: 0.0, duration: 2.5 }, 33.0);',
             f'  tl.to("#sfx-wind1", {{ volume: 0.7, duration: 3 }}, {seg_at["a1-s5"]:.2f});',
             f'  tl.to("#sfx-wind1", {{ volume: 0.0, duration: 2.5 }}, {seg_at["a1-s5"]+19:.2f});']

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=1920, height=1080">
  <title>The Tornado With No Photograph — The Warning Hour Ep. 3</title>
  <script src="gsap.min.js"></script>
  <style>{CSS}</style>
</head>
<body>
<div id="root" data-composition-id="ep3-tristate" data-start="0" data-width="1920" data-height="1080"
     data-duration="{total:.0f}" data-fps="30">

  <!-- narration -->
{chr(10).join(audio)}

  <!-- music beds -->
{chr(10).join(beds)}

  <!-- sfx -->
{chr(10).join(sfx)}

  <!-- track 1: base visuals -->
{chr(10).join(vis)}

  <!-- track 2: graphic sub-compositions -->
{chr(10).join(gfx)}

  <!-- tracks 3/5/7: chips, quotes, lower thirds -->
{chr(10).join(chips)}

  <div id="vignette"></div>
  <canvas id="grain" width="480" height="270"></canvas>
  <div id="grade"></div>
</div>

<script src="grain.js"></script>
<script>
window.__timelines = window.__timelines || {{}};
(function() {{
  const tl = gsap.timeline({{ paused: true }});
  const DUR = {total:.0f};

{chr(10).join(bedjs)}
{chr(10).join(sfxjs)}

  function kb(sel, at, dur, s0, s1, x0, x1, y0, y1) {{
    tl.fromTo(sel, {{ scale: s0, x: x0, y: y0, transformOrigin: "50% 50%" }},
                   {{ scale: s1, x: x1, y: y1, duration: dur, ease: "none" }}, at);
  }}
  const KB = [
{",".join(chr(10) + "  " + k for k in kbs)}];
  KB.forEach(a => kb(...a));

  /* date card */
  (function() {{
    const d = document.getElementById("card-date");
    if (!d) return;
    d.innerHTML = '<div style="position:absolute;left:0;right:0;top:70px;text-align:center;">' +
      '<div style="display:table;margin:0 auto;font-family:\\'Arial Black\\',Arial,sans-serif;font-weight:900;' +
      'font-size:56px;color:#f2f5f8;background:rgba(5,8,12,0.7);padding:8px 40px;letter-spacing:6px;">MARCH 18, 1925</div>' +
      '<div style="display:table;margin:12px auto 0;font-family:Arial,sans-serif;font-weight:700;font-size:26px;' +
      'color:#d8a13a;background:rgba(5,8,12,0.7);padding:6px 26px;letter-spacing:8px;">MISSOURI &middot; ILLINOIS &middot; INDIANA</div></div>';
    gsap.set(d, {{ autoAlpha: 0 }});
    tl.to(d, {{ autoAlpha: 1, duration: 0.5 }}, 0.3);
    tl.to(d, {{ autoAlpha: 0, duration: 0.8 }}, 13.2);
    tl.set(d, {{ autoAlpha: 0 }}, 14.1);
  }})();

  /* chips, quotes and lower thirds: rise in, leave fully */
  document.querySelectorAll('.lt.clip, .quotecard.clip, .srclab.clip').forEach(function(el) {{
    const at = parseFloat(el.dataset.start), dur = parseFloat(el.dataset.duration);
    gsap.set(el, {{ autoAlpha: 0, y: 22 }});
    tl.to(el, {{ autoAlpha: 1, y: 0, duration: 0.5, ease: "power3.out" }}, at + 0.15);
    tl.to(el, {{ autoAlpha: 0, y: -14, duration: 0.45, ease: "power3.in" }}, at + dur - 0.55);
    tl.set(el, {{ autoAlpha: 0 }}, at + dur - 0.05);
  }});

  filmLayer(tl, DUR);
  window.__timelines["ep3-tristate"] = tl;
}})();
</script>
</body>
</html>
"""
    (EP / "index.html").write_text(html, encoding="utf-8")


if __name__ == "__main__":
    vis, gfx, chips, audio, kbs, total, report, seg_at = main()
    emit(vis, gfx, chips, audio, kbs, total, report, seg_at)
    longest = sorted([r for r in report if not r[2].startswith("GRAPHIC")], key=lambda r: -r[1])[:8]
    print(f"[build_ep3] total {total:.1f}s = {total/60:.2f} min")
    print(f"[build_ep3] {len(report)} visual windows; longest non-graphic holds:")
    for s, d, w in longest:
        print(f"   {int(s//60)}:{int(s%60):02d}  {d:4.1f}s  {w}")
    Path(EP / "shotlist.json").write_text(json.dumps(
        [{"start": round(s, 2), "dur": round(d, 2), "what": w} for s, d, w in report], indent=1), encoding="utf-8")
    print(f"[build_ep3] shot list -> {EP / 'shotlist.json'}")
