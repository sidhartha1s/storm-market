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
HOLDS = {"h1-s2": 3.0, "a1-s5": 2.0, "a3-s6c": 5.0, "a3-s9": 2.0, "a4-s3": 6.0,
         "a5-s3": 3.0, "a5-s4b": 4.0, "a6-s4d": 2.0}

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
    return [(a, each) for a in assets]


def kb_for(i):
    """Alternating Ken Burns moves so consecutive stills never repeat the same push."""
    table = [(1.0, 1.09, 0, -14, 0, -9), (1.09, 1.0, -12, 0, -7, 0), (1.0, 1.08, 0, 12, 0, 8),
             (1.06, 1.14, 0, -10, 0, -12), (1.08, 1.0, 10, 0, 6, 0), (1.0, 1.11, 0, -16, 0, -6)]
    return table[i % len(table)]


def main():
    vis, gfx, chips, audio = [], [], [], []
    kbs, panels_used, reuse = [], [], {}
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
        kind = plan["kind"]

        if kind == "graphic":
            gid = plan["id"]
            gfx.append(f'  <div id="host-{gid}-{idx}" data-composition-id="{gid}" '
                       f'data-composition-src="compositions/{gid}.html" data-start="{seg_start:.2f}" '
                       f'data-duration="{seg_dur:.2f}" data-track-index="2" data-width="1920" data-height="1080"></div>')
            lines_report.append((seg_start, seg_dur, f"GRAPHIC {gid}"))
        elif kind in ("stills", "stock", "papers", "mixed", "panel"):
            if kind == "panel":
                gid = plan["id"]
                gfx.append(f'  <div id="host-{gid}-{idx}" data-composition-id="{gid}" '
                           f'data-composition-src="compositions/{gid}.html" data-start="{seg_start:.2f}" '
                           f'data-duration="{seg_dur:.2f}" data-track-index="2" data-width="1920" data-height="1080"></div>')
            if kind == "mixed":
                shots, acc = [], 0.0
                for (src, typ, want) in plan["assets"]:
                    shots.append((src, typ, want)); acc += want
                scale = seg_dur / acc if acc else 1
                shots = [(s, ty, w * scale) for (s, ty, w) in shots]
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
    return vis, gfx, chips, audio, kbs, total, lines_report


if __name__ == "__main__":
    vis, gfx, chips, audio, kbs, total, report = main()
    longest = sorted([r for r in report if not r[2].startswith("GRAPHIC")], key=lambda r: -r[1])[:8]
    print(f"[build_ep3] total {total:.1f}s = {total/60:.2f} min")
    print(f"[build_ep3] {len(report)} visual windows; longest non-graphic holds:")
    for s, d, w in longest:
        print(f"   {int(s//60)}:{int(s%60):02d}  {d:4.1f}s  {w}")
    Path(EP / "shotlist.json").write_text(json.dumps(
        [{"start": round(s, 2), "dur": round(d, 2), "what": w} for s, d, w in report], indent=1), encoding="utf-8")
    print(f"[build_ep3] shot list -> {EP / 'shotlist.json'}")
