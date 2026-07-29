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
import subprocess
from functools import lru_cache
from pathlib import Path

EP = Path(__file__).resolve().parent.parent / "episodes" / "ep3-tristate"
MAX_STILL = 9.6      # hard clamp on a single archival still. ep2 (shipped, the reference)
                     # runs an 11s median hold; the ceiling exists to stop the 30-60s frozen
                     # stretches the owner flagged, not to force a metronome.
MIN_STILL = 3.4
MAX_FILM = 9.0       # a moving clip earns longer than a still, but not a 16s single pull
RHYTHM = (1.28, 0.82, 1.06, 0.88, 1.18, 0.94)   # cut-length weights, cycled — see chunk()
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
R = "media/portraits/"

# ---------------------------------------------------------------- shot table
# kind: stills | film | stock | graphic | panel | papers
# panel/graphic reference a composition id in compositions/
SHOTS = {
 "h1-s1": dict(kind="stills", assets=[P+"Wea00238.jpg", P+"1925_-_Murphysboro_8_-_General_Damage.jpg",
        P+"1925_-_Murphysboro_25_-_17th___Victory_Streets.jpg", P+"1925_tornado_damage_3.webp"], card="date"),
 "h1-s2": dict(kind="mixed", assets=[(F+"mvtn-hook-aerial-bank-4s.mp4","film",4.0),
        (F+"mvtn-hook-trainwreck-4s.mp4","film",4.0), (P+"Wea00239_-_Flickr_-_NOAA_Photo_Library.jpg","still",4.6)]),
 "a1-s1":  dict(kind="graphic", id="g-wordban", pad_before=0.0),
 # hazen-portrait-01.jpg is Gen. William B. Hazen — the Signal Corps commander who SHUT Finley
 # down, not Finley. Under a panel headlined "JOHN PARK FINLEY" the viewer reads the face as
 # Finley, so it stays out. The two portraits here ARE Finley: the Library of Congress plate
 # is captioned "J.P. FINLEY" on the negative, and the desk photograph came from the owner
 # labelled as him. Both are taller than 1.45:1, so they land in the .pfit treatment — the
 # image sits whole over a blurred copy of itself instead of being cropped to fill.
 # Order (owner 2026-07-29): Finley, Finley-at-desk, the tornado drawing, back to Finley.
 # The old second slot (DocFile__2_.jpg, an unrelated document plate) read as "some building"
 # and is dropped.
 "a1-s1b": dict(kind="panel", id="g-panel-finley", assets=[R+"finley-portrait-01.png",
        R+"finley-desk-01.png", P+"Tri_State_Tornado_Drawing.jpg",
        R+"finley-portrait-01.png"], fit="contain"),
 "a1-s2":  dict(kind="graphic", id="g-forecast"),
 # right-side panel over archival b-roll (owner 2026-07-29, the ep2 7:37 treatment) instead
 # of a sparse full-frame card with too much empty space
 "a1-s2c": dict(kind="panel", id="g-sources", assets=[P+"1925_-_Murphysboro_22_-_Aerial_View(1).jpg",
        P+"13-Murphysboro_Aerial.png", P+"1925_-_De_Soto_-_Birds_Eye_View.jpg",
        P+"X_West_Frankfort2_-_Aerial_View_West_Side_of_Town.jpg"]),
 "a1-s2b": dict(era="pre", kind="stills", assets=[P+"11-Murphysboro_Pre-Tornado_1.png", P+"12-Murphysboro_Pre-Tornado_2.png",
        P+"Annapolis_Business_street.png", P+"1925_-_Murphysboro_20_-_Business_District.jpg",
        P+"1925_-_Murphysboro_11_-_Residential_District.jpg", P+"1925_-_Murphysboro_1_-_Corner_of_17th___Walnut.jpg",
        P+"1925_-_Murphysboro_12b_-_Baptist_Church.jpg"]),
 "a1-s3":  dict(kind="graphic", id="g-metmap"),
 "a1-s4":  dict(kind="graphic", id="g-scale"),
 "a1-s4c": dict(kind="stock", assets=[S+"stock-cloudsomen-02.mp4", S+"stock-cloudsrolling-03.mp4",
        S+"stock-lightning-01.mp4", S+"stock-cloudsomen-01.mp4"]),
 # the narration here is spatial — "not a squall line", "one lone supercell", "400 miles",
 # "seven hours" — so it gets a map, not a stat panel over cloud footage (owner, 5:16).
 "a1-s4d": dict(kind="graphic", id="g-lone",
        tail=[S+"stock-cloudsrolling-01.mp4", S+"stock-tornado-01.mp4"]),
 # weighted, not evenly chunked: "children walked to school" is spoken at +2.58s and
 # "miners went underground" at +7.72s, so the mine has to own the 7-12s slot
 # The three recreations here are the owner's replacements (2026-07-29): the schoolroom of
 # empty desks with the coats still on their hooks, the miners walking INTO the tunnel, and
 # the family on the farmhouse porch. They carry the same beats as the images they replace
 # and read as period photographs rather than illustrations.
 "a1-s5":  dict(era="pre", kind="mixed", assets=[(A+"ai-schoolroom-coats.png","still",7.5),
        # NOT 26-West_Frankfort_Coal_Cars.png — that is post-storm wreckage from the NWS
        # damage set, and this segment is pre-storm daily life. Wreckage here contradicts
        # the narrative before the storm has hit.
        (A+"ai-miners-entering.png","still",5.2),
        (A+"ai-farmhouse-family.png","still",5.0),
        (P+"20-De_Soto_School_1910.png","still",4.4)], chip="Recreation"),
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
        P+"Tri-State_Tornado_JCHS15.jpg"], lower="gorham", quote="gorham"),
 "a3-s1b": dict(kind="panel", id="g-panel-gorham", assets=[P+"1925_-_Gorham_-_Post_Office_Area.jpg",
        P+"09-Gorham_Boxcars.png", P+"1925_tornado_damage_7.webp"]),
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
 # the "rows" quote is credited to the St. Louis Post-Dispatch, which we have no front page
 # for. Showing the Chicago Herald Examiner and Evansville Press mastheads under that credit
 # reads as the wrong source, so this segment carries damage stills instead.
 "a3-s3b": dict(kind="stills", assets=[P+"1925_-_Murphysboro_9_-_General_Damage.jpg",
        P+"1925_-_Murphysboro_20_-_Business_District.jpg", P+"16-Murphysboro_SW_of_Logan_School.png",
        P+"1925_-_Murphysboro_11_-_Residential_District.jpg"], quote="rows"),
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
 # the West Frankfort stat panel was authored and left unmounted — this is the episode's
 # longest segment and it carried no graphic at all
 "a3-s7":  dict(kind="panel", id="g-panel-wf",
        assets=[A+"ai-miners-emerging.png", P+"X_West_Frankfort3_-_Aerial_View_Orient_No_2_Mine.png",
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
 # marvin-portrait-01.jpg (Charles F. Marvin, Weather Bureau chief) was here under narration
 # about disaster relief and the absence of any federal agency — he has nothing to do with
 # that beat and the face read as a stranger (owner 2026-07-29). Replaced with the Griffin
 # relief-tents plate, which is what "rebuilt by churches, neighbors, and a charity" shows.
 "a5-s1d": dict(kind="panel", id="g-panel-nonet", assets=[P+"1925_-_Griffin_-_Tents_Amidst_Damage.jpg",
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
 # "no destruction means no record" — empty country, not wreckage in the wrong state
 "a6-s2c": dict(kind="graphic", id="g-remeasure",
        tail=[S+"stock-windgrass-01.mp4", S+"stock-rainfield-01.mp4", S+"stock-windgrass-02.mp4"]),
 "a6-s2d": dict(kind="graphic", id="g-compare"),
 # the segment ends on a modern event (Kentucky, 2021); the Fujita panel must not still be
 # on screen for it, so the graphic yields and neutral weather footage carries the payoff
 "a6-s3":  dict(kind="graphic", id="g-fujita",
        tail=[S+"stock-cloudsrolling-02.mp4", S+"stock-rainfield-02.mp4", S+"stock-lightning-02.mp4"]),
 "a6-s3c": dict(kind="graphic", id="g-modern"),
 "a6-s3d": dict(kind="graphic", id="g-prep"),
 # This segment narrates MARCH 2025 — the centennial, the new markers, the descendants —
 # and was running 1925 wreckage photographs under it. The picture said 1925 while the
 # voice said 2025. No 2025 footage exists in the pool, so the beat is carried by a
 # designed card that does not pretend to be a photograph of anything.
 # The tail is pinned to era-neutral present-day footage: the act-6 default pool is entirely
 # 1925 wreckage, so any retime that leaves >1.2s after the graphic would put 1925 photographs
 # back under 2025 narration. Grass and rain, not storms — this beat is a memorial, not a hit.
 "a6-s3b": dict(kind="graphic", id="g-centennial",
        tail=[S+"stock-windgrass-02.mp4", S+"stock-rainfield-01.mp4", S+"stock-windgrass-01.mp4"]),
 # "Local cemeteries carry rows of headstones that all say March eighteenth, 1925" is spoken
 # at +19.74s. Weather footage under that line is the "look at stuff" miss — the owner's
 # memorial stone is the picture the sentence is asking for, so it owns the 17-25s slot.
 # It is a present-day photograph, which is also what "walk the path today" needs.
 "a6-s3e": dict(kind="mixed", chip="Recreation", assets=[
        (S+"stock-windgrass-01.mp4","stock",6.0),
        (S+"stock-cloudsrolling-03.mp4","stock",5.5),
        (S+"stock-rainfield-02.mp4","stock",5.5),
        (A+"ai-memorial-2025.png","still",8.0),
        (S+"stock-windgrass-02.mp4","stock",2.9)]),
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
 # h1-s2 was 3.5s: the hook's last still slow-zoomed through 4s of post-narration silence
 # before the first graphic (owner 2026-07-29, "awkward slow-zoom, i would hit esc"). Tightened.
 "h1-s2": 1.0, "a1-s5": 4.0, "a2-s2": 2.5, "a2-s4b": 3.0,
 "a3-s1b": 2.5, "a3-s4c": 5.0, "a3-s6c": 5.0, "a3-s8": 3.0, "a3-s9": 2.5,
 "a4-s1b": 2.5, "a4-s3": 7.0,
 "a5-s1d": 2.5, "a5-s3": 4.0, "a5-s4b": 5.0,
 "a6-s2d": 2.5, "a6-s3e": 3.5, "a6-s4d": 3.0, "a6-s4": 2.5,
 # the outro card is authored at 30s but was clamped to the 15.9s narration and cut off
 # mid-credits; the hold lets it finish on screen
 "a6-s5": 11.0,
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


# Substitutes are era-blind by default, which put a post-storm front page and then a
# DESTRUCTION photo into a segment narrating life BEFORE the tornado. Segments marked
# era="pre" may only ever fall back to imagery that predates the storm.
PRE_STORM_SAFE = [P+"11-Murphysboro_Pre-Tornado_1.png", P+"12-Murphysboro_Pre-Tornado_2.png",
                  P+"Annapolis_Business_street.png", P+"20-De_Soto_School_1910.png",
                  A+"ai-farmhouse-morning.png", A+"ai-children-school.png",
                  P+"1925_-_Murphysboro_2_-_Murphysboro_Township_High_School.jpg"]
_ERA_POOL = None
_LAST = None
_ACT = "a1"           # act of the segment being emitted; keeps pick()'s spares on the map

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
    # unclaimed photos first, but every photo is eligible once they run out — the ceiling
    # matters more than whether a frame was hand-picked for some other segment.
    # Front pages are excluded entirely: they are DATED (March 20 1925, i.e. after the
    # storm), so dropping one into a pre-storm segment as filler breaks the chronology.
    # A substitute has to be era-neutral to be safe anywhere on the timeline.
    # test the CANONICAL path: the front pages also exist under media/photos/ with
    # innocuous names, and canon() rewrites those to media/newspapers/ after the filter
    pool = [a for a in pool if not canon(a).startswith("media/newspapers/")]
    return [a for a in pool if a not in claimed] + [a for a in pool if a in claimed]


@lru_cache(maxsize=None)
def _canon_map():
    """Six newspaper front pages exist byte-identical under BOTH media/newspapers/ and
    media/photos/. Counting uses per path let one page reach nine on-screen appearances
    against a ceiling of three. Identity is the file's content, not its path."""
    import hashlib
    by_hash = {}
    for p in sorted((EP / "media").rglob("*")):
        if p.is_file() and p.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp"):
            rel = p.relative_to(EP).as_posix()
            by_hash.setdefault(hashlib.md5(p.read_bytes()).hexdigest(), []).append(rel)
    return {r: paths[0] for paths in by_hash.values() for r in paths}


def canon(asset):
    return _canon_map().get(asset, asset)


def pick(asset):
    """Return `asset`, or a fresh spare once it has been used MAX_USES times."""
    global _LAST
    asset = canon(asset)
    if _USES.get(asset, 0) < MAX_USES and asset != _LAST:
        _USES[asset] = _USES.get(asset, 0) + 1
        _LAST = asset
        return asset
    # never hand back the frame that is already on screen — with a small era-restricted
    # pool the substitution loop otherwise cuts an image straight to itself.
    # Order matters geographically: the act's own pool comes before the global spares,
    # because _SPARE is flat and once handed an Annapolis, Missouri beat a photograph of
    # the Heinz plant in Princeton, Indiana — the far end of the track, three hours later.
    if _ERA_POOL:
        pool = _ERA_POOL
    else:
        pool = list(TAIL.get(_ACT, [])) + [s for s in _SPARE if s not in TAIL.get(_ACT, [])]
    for sp in pool:
        sp = canon(sp)
        if _USES.get(sp, 0) < MAX_USES and sp != _LAST:
            _USES[sp] = _USES.get(sp, 0) + 1
            _LAST = sp
            return sp
    print(f"[build_ep3] WARNING: spare pool exhausted — {Path(asset).name} exceeds MAX_USES")
    _USES[asset] = _USES.get(asset, 0) + 1
    _LAST = asset
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
    # An even division makes every cut land on the same beat — 90% of v2's windows sat in one
    # 5-7s band, which reads as a slideshow rather than an edit. ep2 (the shipped reference)
    # ranges from 1s to 80s. Breathe the rhythm with a fixed weight cycle: deterministic, sums
    # to exactly `dur`, and still clamped under maxw.
    k = len(assets)
    while True:
        ws = [RHYTHM[i % len(RHYTHM)] for i in range(k)]
        tot = sum(ws)
        each = [dur * w / tot for w in ws]
        if max(each) <= maxw or min(each) <= minw:
            break
        k += 1                                # too long even weighted: add one more cut
        assets = [assets[i % len(assets)] for i in range(k)]
    return [(pick(a), w) for a, w in zip(assets, each)]


def is_video(src):
    return src.lower().endswith((".mp4", ".mov", ".webm", ".m4v"))


@lru_cache(maxsize=None)
def is_tall(src):
    """A source narrower than the 16:9 frame loses most of its height to object-fit:cover
    (measured 54-61% on the portrait-format plates). Those get the letterbox treatment —
    blurred backdrop plus the whole image — which already exists as .pfit."""
    if is_video(src):
        return False
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                          "-show_entries", "stream=width,height", "-of", "csv=p=0:s=x",
                          str(EP / src)], capture_output=True, text=True).stdout.strip()
    try:
        w, hgt = (int(x) for x in out.split("x")[:2])
    except ValueError:
        return False
    return w / hgt < 1.45          # 16:9 is 1.78; below ~1.45 cover starts eating the subject


def _aspect(src):
    """Width/height of a still, or 16:9 if it cannot be read."""
    if is_video(src):
        return 16 / 9
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                          "-show_entries", "stream=width,height", "-of", "csv=p=0:s=x",
                          str(EP / src)], capture_output=True, text=True).stdout.strip()
    try:
        w, hgt = (int(x) for x in out.split("x")[:2])
        return w / hgt
    except ValueError:
        return 16 / 9


@lru_cache(maxsize=None)
def vdur(src):
    """Real length of a clip. hyperframes will not loop a short video to fill a long window —
    it fails the render with a frame-coverage error — so the window must fit the source."""
    if not is_video(src):
        # ffprobe reports ~0.04s for a still image; trusting that silently shredded a 6.3s
        # window into 158 one-frame cuts. A non-video typed as film/stock is a data error.
        raise SystemExit(f"[build_ep3] {src} is typed as a clip but is not a video file")
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                          "-of", "default=nw=1:nk=1", str(EP / src)],
                         capture_output=True, text=True).stdout.strip()
    if not out:
        raise SystemExit(f"[build_ep3] ffprobe returned nothing for {src}")
    return float(out)


def split_overlong(shots, pool):
    """`mixed` segments carry hand-declared beat weights, which the seg_dur rescale can push
    past the clamps chunk() enforces everywhere else. Split what it stretched: a still never
    holds past MAX_STILL, a clip never past MAX_FILM, and the overflow cuts to a fresh frame."""
    out, k = [], 0
    for (src, typ, w) in shots:
        cap = MAX_STILL if typ not in ("film", "stock") else min(MAX_FILM, vdur(src))
        if w <= cap or not pool:
            out.append((src, typ, w))
            continue
        # Split evenly rather than head-plus-remainder: a head clamped to its own cap left a
        # 0.04s tail, i.e. a one-frame flash. Every piece answers to the tighter of the two
        # caps, so the overflow stills never inherit the film ceiling.
        step = min(cap, MAX_STILL)
        n = int(w / step + 0.9999)
        each = w / n
        out.append((src, typ, each))
        prev = src
        for _ in range(n - 1):
            nxt = next((p for p in pool[k:] + pool[:k] if p != prev), pool[k % len(pool)])
            k = (pool.index(nxt) + 1) % len(pool)
            out.append((pick(nxt), "still", each))
            prev = nxt
    return out


def kb_for(i):
    """Alternating Ken Burns moves so consecutive stills never repeat the same push."""
    table = [(1.0, 1.09, 0, -14, 0, -9), (1.09, 1.0, -12, 0, -7, 0), (1.0, 1.08, 0, 12, 0, 8),
             (1.06, 1.14, 0, -10, 0, -12), (1.08, 1.0, 10, 0, 6, 0), (1.0, 1.11, 0, -16, 0, -6)]
    return table[i % len(table)]


def check_hyperframes_current():
    """Warn at COMPOSE time if a newer hyperframes is published (owner 2026-07-29).

    This is the production-start check: it runs every time the episode is built, which is
    before any render, so a stale pin is caught while re-pinning is still cheap — not in a
    render log after a 40-minute render. Non-fatal: a build must not fail because npm is
    unreachable. The render gate keeps the offline pin-drift check; currency lives here.
    """
    repo = EP.parent.parent
    cfg = (repo / "config.yaml").read_text(encoding="utf-8", errors="replace")
    m = re.search(r'hyperframes_version:\s*"([\d.]+)"', cfg)
    if not m:
        return
    pinned = m.group(1)
    try:
        r = subprocess.run(["npm", "view", "hyperframes", "version"],
                           capture_output=True, text=True, shell=True, timeout=30)
        newest = r.stdout.strip()
    except Exception:
        newest = ""
    if not re.fullmatch(r'[\d.]+', newest or ""):
        print(f"[version] pin {pinned}; could not reach npm to check for a newer release (not fatal)")
        return
    if newest != pinned:
        print(f"[VERSION] pinned {pinned}, but hyperframes {newest} is published.")
        print(f"[VERSION] Decide NOW, at compose time — bump config.yaml + every npx pin together,")
        print(f"[VERSION] or stay deliberately. Read the diff for the extract stage and any timeout")
        print(f"[VERSION] first (0.7.81 shortened the ffprobe deadline from 120s to 30s).")
    else:
        print(f"[version] pin {pinned} is the latest published.")


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
        seg_start, seg_dur = round(t, 2), round(d + HOLDS.get(sid, 0.0), 2)
        seg_at[sid] = seg_start
        global _ERA_POOL
        _ERA_POOL = PRE_STORM_SAFE if plan.get("era") == "pre" else None
        global _ACT
        _ACT = sid.split("-")[0]
        kind = plan["kind"]

        if kind == "graphic":
            gid = plan["id"]
            gw = min(GDUR.get(gid, seg_dur), seg_dur)
            gfx.append(f'  <div id="host-{gid}-{idx}" data-composition-id="{gid}" '
                       f'data-composition-src="compositions/{gid}.html" data-start="{seg_start:.2f}" '
                       f'data-duration="{gw:.2f}" data-track-index="2" data-width="1920" data-height="1080"></div>')
            lines_report.append((seg_start, gw, f"GRAPHIC {gid}"))
            leftover = seg_dur - gw
            # The closing card is the last thing in the episode; cutting away from it to a
            # damage photograph for the leftover hold put a 1.5s archival flash after the
            # credits. The video ends on the card.
            if sid == ORDER[-1]:
                leftover = 0.0
            if leftover > 1.2:      # never park on a finished graphic, and never on nothing
                pool = plan.get("tail") or TAIL[sid.split("-")[0]]
                ct2 = round(seg_start + gw, 2)
                vids = [x for x in pool if is_video(x)]
                # a footage tail is capped by its own shortest clip, or hyperframes fails the
                # window on frame coverage
                tmax = min([MAX_FILM] + [vdur(x) for x in vids]) if vids else MAX_STILL
                for a, w in chunk(leftover, pool, maxw=tmax):
                    w = round(w, 2)
                    eid = f"t{idx}"
                    reuse[a] = reuse.get(a, 0) + 1
                    cb = f' data-callback="tail cutaway after {gid} completes"' if reuse[a] > 1 else ""
                    if is_video(a):     # a tail pool may be footage rather than stills
                        vis.append(f'  <video id="{eid}" class="clip stockgrade" src="{a}" '
                                   f'data-start="{ct2:.2f}" data-duration="{w:.2f}" '
                                   f'data-track-index="1" muted{cb}></video>')
                        lines_report.append((ct2, w, f"tail {Path(a).name}"))
                        ct2 = round(ct2 + w, 2)
                        idx += 1
                        continue
                    if is_tall(a):      # same letterbox rule as the main visual path
                        vis.append(f'  <section class="clip pfit" id="{eid}" data-start="{ct2:.2f}" '
                                   f'data-duration="{w:.2f}" data-track-index="1"{cb}>'
                                   f'<img class="pbg" src="{a}" alt="">'
                                   f'<img id="kb-{eid}" class="pfg archgrade" src="{a}" alt=""></section>')
                    else:
                        vis.append(f'  <section class="clip still-wrap" id="{eid}" data-start="{ct2:.2f}" '
                                   f'data-duration="{w:.2f}" data-track-index="1"{cb}>'
                                   f'<img id="kb-{eid}" class="archgrade" src="{a}" alt=""></section>')
                    s0, s1, x0, x1, y0, y1 = kb_for(idx)
                    kbs.append(f'["#kb-{eid}",{ct2:.2f},{w:.2f},{s0},{s1},{x0},{x1},{y0},{y1}]')
                    lines_report.append((ct2, w, f"tail {Path(a).name}"))
                    ct2 = round(ct2 + w, 2)
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
                # Scale against the NARRATION, not narration+hold. Scaling by seg_dur spread
                # the hold across every beat, so a weight tuned to a spoken word drifted late
                # in proportion to the hold (a1-s5's 4s hold pushed its 7.0s beat to 8.3s and
                # the coal-mine cut landed 0.58s after the word "miners"). The hold is silence
                # at the end of the segment, so it belongs to the last shot only.
                scale = d / acc if acc else 1
                # everything that is not a clip goes through pick(), not just ty=='still' —
                # newspaper front pages typed 'paper' were bypassing the reuse ceiling
                shots = [(s if is_video(s) else pick(s), ty, w * scale) for (s, ty, w) in shots]
                if shots and seg_dur > d:
                    s, ty, w = shots[-1]
                    shots[-1] = (s, ty, w + (seg_dur - d))
            else:
                # type follows the FILE, not the segment kind: a photo listed inside a
                # kind="stock" segment was being typed "stock" and emitted as <video
                # src="...jpg">, which renders as a black window.
                vid_typ = "stock" if kind == "stock" else "film"
                still_typ = "paper" if kind == "papers" else "still"
                shots = [(a, vid_typ if is_video(a) else still_typ, w)
                         for a, w in chunk(seg_dur, plan["assets"])]
            shots = split_overlong(shots, TAIL[sid.split("-")[0]])
            # emit on the 2-decimal grid the attributes are printed at, so a window's end is
            # bit-identical to the next window's start (float drift showed up as 0.01s
            # same-track overlaps in hyperframes' contract check)
            ct = round(seg_start, 2)
            for (src, typ, w) in shots:
                w = round(w, 2)
                eid = f"v{idx}"
                reuse[src] = reuse.get(src, 0) + 1
                cb = (f' data-callback="motif returns — use {reuse[src]} of this asset"'
                      if reuse[src] > 1 else "")
                if typ in ("film", "stock"):
                    cls = "archgrade" if typ == "film" else "stockgrade"
                    vis.append(f'  <video id="{eid}" class="clip {cls}" src="{src}" data-start="{ct:.2f}" '
                               f'data-duration="{w:.2f}" data-track-index="1" muted{cb}></video>')
                # fit="contain" is a segment-wide hint, but applying it to an image that is
                # already near 16:9 pillarboxes a photo that would have filled the frame
                # (four stills at 1.58-1.75 were running inside blurred bars for no reason).
                # Papers stay contained at any aspect — cropping a front page cuts the text.
                elif typ == "paper" or is_tall(src) or (
                        plan.get("fit") == "contain" and _aspect(src) < 1.60):
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
                ct = round(ct + w, 2)
                idx += 1

        if plan.get("lower"):
            loc, tm = LOWERS[plan["lower"]]
            chips.append(f'  <section id="lt-{idx}" class="lt clip" data-start="{seg_start + 0.4:.2f}" '
                         f'data-duration="7.0" data-track-index="7"><div class="lt-loc">{loc}</div>'
                         f'<div class="lt-time">{tm}</div></section>')
        if plan.get("quote"):
            q, attr = QUOTES[plan["quote"]]
            # .lt sits at bottom:110px and .quotecard at bottom:150px, so a lower third
            # still on screen collides with the quote attribution. Wait for it to clear.
            qs = seg_start + min(6.0, seg_dur * 0.35)
            if plan.get("lower"):
                qs = max(qs, seg_start + 8.0)
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
        t = round(seg_start + seg_dur + GAP, 2)

    # g-close carries the title, episode line and credits inside its own timeline and fades
    # itself out at the end; that fade IS the ending. The old `t + 1.0` ran past the closing
    # card by the whole trailing hold, and close_picture_gaps then stretched the g-close host
    # to reach it — 3.7s of frozen black after the last visible frame. ep2, the shipped
    # reference, ends on picture with a 0.0s tail. End on the last picture window instead.
    W_END = re.compile(r'data-start="([\d.]+)" data-duration="([\d.]+)"')
    ends = [float(m.group(1)) + float(m.group(2))
            for s in vis + gfx if (m := W_END.search(s))]
    total = -(-max(ends) // 1)      # ceil: the root prints its duration at {total:.0f}
    close_picture_gaps(vis, gfx, kbs, total)
    return vis, gfx, chips, audio, kbs, total, lines_report, seg_at


def close_picture_gaps(vis, gfx, kbs, total):
    """Hold the outgoing frame through every breath instead of cutting to black.

    Segments advance by seg_dur + GAP, but the picture windows only ever spanned
    seg_dur — so the 0.75s breath between narration segments had nothing on the
    picture tracks and rendered as a hard cut to black. Measured on the v3 draft:
    81 black spans, 63 of them at segment boundaries (ep2, the shipped reference,
    has 2). Fix by extending whatever window ends at the gap to the next window's
    start; the composite freezes for the breath and cuts on the new line.
    """
    total = round(total)    # the root element prints its duration at {total:.0f}
    W = re.compile(r'data-start="([\d.]+)" data-duration="([\d.]+)"')
    wins = []
    for lst in (vis, gfx):
        for i, s in enumerate(lst):
            m = W.search(s)
            if m:
                wins.append([float(m.group(1)), float(m.group(2)), lst, i])

    edges = sorted({round(a + d, 2) for a, d, _, _ in wins} | {0.0})
    starts = sorted({round(a, 2) for a, _, _, _ in wins})

    # a gap is an instant where coverage drops to zero before the next window opens
    def covered(t0):
        return any(a <= t0 < round(a + d, 2) for a, d, _, _ in wins)

    grow = {}
    for e in edges:
        if covered(e) or e >= total:
            continue
        nxt = next((s for s in starts if s > e), total)
        if nxt - e < 0.01:
            continue
        for w in wins:
            if abs(round(w[0] + w[1], 2) - e) < 0.005:
                grow[id(w[2]), w[3]] = round(nxt - w[0], 2)

    for (lst_id, i), newdur in grow.items():
        lst = vis if id(vis) == lst_id else gfx
        old = lst[i]
        lst[i] = W.sub(lambda m: f'data-start="{m.group(1)}" data-duration="{newdur:.2f}"',
                       old, count=1)
        eid = re.search(r'id="(?:host-)?([\w-]+)"', old)
        if eid:
            kid = f'"#kb-{eid.group(1)}",'
            for k, kb in enumerate(kbs):
                if kb.startswith("[" + kid):
                    parts = kb[1:-1].split(",")
                    parts[2] = f"{newdur:.2f}"
                    kbs[k] = "[" + ",".join(parts) + "]"
                    break


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
    # 02_wind_ominous_steady.mp3 read as grey-noise disturbance under the TTS at ~5:48
    # (owner 2026-07-30). Removed and banned — see LEARNINGS.md. Only the distant-rumble
    # bed under the cold open remains.
    sfx = [
        f'  <audio id="sfx-rumble" src="media/sfx/04_distant_storm_rumble.mp3" data-start="0" data-duration="36" data-volume="0" data-bed="1"></audio>',
    ]
    sfxjs = ['  tl.to("#sfx-rumble", { volume: 0.55, duration: 2.0 }, 0.3);',
             '  tl.to("#sfx-rumble", { volume: 0.75, duration: 1.0 }, 16.0);',
             '  tl.to("#sfx-rumble", { volume: 0.0, duration: 2.5 }, 33.0);']

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
    check_hyperframes_current()
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
