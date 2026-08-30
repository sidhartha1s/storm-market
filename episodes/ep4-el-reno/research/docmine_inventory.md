# Shot Inventory — NWS Norman "Lessons of the Most Dangerous Tornado" (full 1547s)

Source: `media/nwsnorman/nwsnorman-lessons-most-dangerous-tornado-full.mp4` (960x720, 30fps, 1546.97s), NWS Norman / NOAA.

## Method and coverage honesty

1. ffmpeg scene-change detection (`select='gt(scene,0.08)'` after testing 0.3 and 0.12, which returned only 45 and 85 cuts respectively — too sparse for a graphics-heavy documentary) found 95 hard-cut boundaries.
2. 21 of the resulting gaps were longer than 20s (1137s / 73% of runtime) — these are stretches where scene detection sees no hard cut but the content still changes (slide bullet builds, radar loops, slow overlays). Fixed-interval samples (~12s spacing) were added inside every such gap.
3. Total 181 frames extracted and read by 5 parallel reviewers, one per ~310s segment, each cross-referencing the word-level transcript for narration sync.
4. Reviewers merged same-background "shot" spans (e.g. a slide holding one photo plate through 3-4 bullet builds) into a single row rather than one row per bullet — this is a deliberate simplification, not a coverage gap. Every second of the 1547s runtime is accounted for in the 84 rows below.
5. One suspected coverage gap was explicitly checked and resolved: the largest raw gap (1291–1547s, 256s) was NOT one continuous shot — it is a static radar still under changing callout text (1291–1372s), then the slide deck resumes (1372–1500s), then black end-credit cards (1500–1547s).
6. No TALKING-HEAD shots were found anywhere in the film — it is 100% chase footage, NWS/NOAA graphics, radar loops, slide decks, and text cards.

## Class totals (84 shots)

| Class | Count |
|---|---|
| GRAPHIC | 47 |
| REAL-FOOTAGE | 28 |
| TEXT-SLIDE | 6 |
| PHOTO-STILL | 3 |

## HARD EXCLUSION — private family photo

**916.2s–922.5s** (single occurrence, confirmed not recurring anywhere else in the film — explicitly re-checked by the 620–930s, 930–1240s, and 1240–1547s reviewers, plus verified directly by the orchestrator via bracketing frames at 908/910/912/914/916/916.5/917/917.5/918/920/922/923/924/925/926/930s). A picture-in-picture inset (top-left) of a man wearing glasses with two young blond boys, faded in over a radar heatmap graphic labeled "Henderson" / "Bettes/TWC" (a chase-team position tracker). This is Richard Henderson's private family photo. **Never recommend, in any form, at any crop.**

## CREDIT-FLAGGED — third-party chaser/videographer names found burned into footage or as photo credits

The film's own end-credit card ("Video by") confirms nearly all raw ground footage is individually credited:
**Ray Bohac, Dave Demko, Heidi Farrar, Gabe Garfield, Mikey Gribble, Chris Gullikson, Justin Hoyt, Dick McGowan, Forrest Mitchell, Dan Robinson, Brandon Sullivan, Skip Talbot** ("Produced by: Gabe Garfield, Skip Talbot").

Confirmed burned into specific shots we sampled (exact on-screen text): **Garfield** (~17–27s, ~580–620s, ~930–935s), **Tempest Tours** (~6–17s, ~628–700s, tied to Chris Gullikson), **Skip Talbot** (~73–83s, ~380–399s photo credit, ~800–872s, ~1080–1093s, ~1189–1222s), **Jennifer C Brindley** (background-photo credit on nearly every "What We (Re)Learned"/"Suggestion"/"Closing Thoughts" slide, ~1104–1488s — a recurring credited still, not raw footage, but still third-party), **Dan Robinson** (~985–1046s), **Mikey Gribble** (~935–945s), **Dick McGowan** (~872–886s), **Dave Demko / Heidi Farrar** (~746–815s, paired), **Brandon Sullivan** (~717–746s, ~1165–1189s inset), **"Sullivan/Wright"** pin label (~700–717s — "Wright" is not on the film's own credit card; likely a co-rider, uncertain), **Sean Schofer** (photo credit on the wrecked Weather Channel SUV still, ~973–985s — also not on the film's own credit card), **Roger Edwards & Rich Thompson** and **Brett Roberts / www.skyinmotion.com** (photo credits on two illustrative historical-tornado inset stills used in the "multiple simultaneous tornadoes" slide, ~1240–1291s).

Per channel rule (storm-market CLAUDE.md: "credit ≠ license," "hosting ≠ license"), **none of these named shots are safe to lift**, regardless of NWS Norman hosting the compilation.

Radar/map GRAPHIC shots that carry a named position-pin (e.g. "Henderson," "Bettes/TWC," "Talbot/Brindley," "Sullivan/Wright," "Robinson," "McGowan" as a label on an NWS-made radar heatmap, not as a credit on raw footage) are listed separately below as MEDIUM-RISK — the underlying radar graphic is NWS's own analytical product, but the pin identifies a specific person's tracked position, so they are not blanket-clean.

## Full shot table (0–1547s)

### Segment 0–310s

| in_s | out_s | dur_s | class | description | credit/flag | audio |
|---|---|---|---|---|---|---|
| 0 | 6 | 6 | REAL-FOOTAGE | Wide shot, rain-wrapped wedge tornado over farmland, two vehicles roadside | unconfirmed (dark) — treat as credited | narrated |
| 6 | 17 | 11 | REAL-FOOTAGE | Fisheye wide, wedge tornado over pasture, red corral fence, chase vehicle | **Tempest Tours** | narrated |
| 17 | 27 | 10 | REAL-FOOTAGE | Tornado behind barbed-wire fence, on-screen "300 mph" caption | **Gabe Garfield** | narrated |
| 27 | 38 | 11 | TEXT-SLIDE | Black card, "El Reno" title | none | silence/music |
| 38 | 59 | 21 | GRAPHIC | Satellite map, EF-0 contour outline, storm-motion arrows, legend | none | narrated |
| 59 | 73 | 14 | REAL-FOOTAGE | Dark low-contrast tornado over field, vehicle hood in frame | unconfirmed (dark) — treat as credited | narrated |
| 73 | 83 | 10 | REAL-FOOTAGE | Tornado under green HP-supercell sky, rural road, oncoming headlights | **Skip Talbot** | narrated |
| 83 | 93 | 10 | PHOTO-STILL | Triptych headshots, TWISTEX crew memorial (Tim/Paul Samaras, Carl Young) | needs provenance check | narrated |
| 93 | 114 | 21 | GRAPHIC | Split screen: animated "TWISTEX" dot-map across Plains + roadside memorial marker photo | marker photo needs check; dot-map clean | narrated then silence |
| 114 | 131 | 17 | REAL-FOOTAGE | Time-lapse cumulus building, blue sky (generic) | unconfirmed provenance | narrated |
| 131 | 140 | 9 | GRAPHIC | NWS convective outlook, "This Evening: 6 PM to 10 PM," threat bullets + map | none | narrated |
| 140 | 159 | 19 | REAL-FOOTAGE | Dark tornado b-roll, tarp/fence foreground, power lines | unconfirmed (dark) — treat as credited | narrated |
| 159 | 202 | 43 | GRAPHIC | Animated jet-stream ribbon + moisture-transport region + arrows | none | narrated |
| 202 | 226 | 24 | GRAPHIC | Illustrated hot-air balloon, COOL/WARM buoyancy explainer | none | narrated |
| 226 | 238 | 12 | REAL-FOOTAGE | NWS Norman rooftop weather-balloon launch (radome/water tower visible) | none — NWS's own facility, PD | narrated |
| 238 | 297 | 59 | GRAPHIC | Skew-T sounding (OUN 130601/0000) building to "THE CAP" callout | none | narrated |
| 297 | 310+ | 13+ | GRAPHIC | OK/AR map, "CAPE 6 PM," color contours + legend (continues into next segment) | none | narrated |

### Segment 310–620s

| in_s | out_s | dur_s | class | description | credit/flag | audio |
|---|---|---|---|---|---|---|
| 310 | 336 | 26 | GRAPHIC | "SURFACE WINDS 6 PM" map, red arrows, "DEWPOINTS > 70F" | none | narrated |
| 336 | 348 | 12 | GRAPHIC | "500 MB WINDS 6 PM" map, blue arrows | none | narrated |
| 348 | 360 | 12 | GRAPHIC | "SURFACE – 500 MB SHEAR 6 PM" map, arrow pairs | none | narrated |
| 360 | 380 | 20 | GRAPHIC | Toy paddle-wheel + rotation-arrow diagram (differential-flow rotation) | none | narrated |
| 380 | 399 | 19 | PHOTO-STILL | Towering-cumulus still + motion arrows | **Skip Talbot** (www.skip.cc) | narrated |
| 399 | 418 | 19 | GRAPHIC | Animated 3D diagram, counter-rotating horizontal vortex tubes | none | narrated |
| 418 | 439 | 21 | GRAPHIC | Vortex tube tilted into horseshoe by updraft arrow | none | narrated |
| 439 | 449 | 10 | GRAPHIC | Simplified diagram, one circulation loop remaining | none | narrated |
| 449 | 460 | 11 | GRAPHIC | Same diagram + green "RAINY DOWNDRAFT" arrow (hook-echo mechanism) | none | narrated |
| 460 | 483 | 23 | GRAPHIC | "May 31, 2013 Surface Overview" map — front, dryline, "enhanced lift" arrow at El Reno | none | narrated |
| 483 | 508 | 25 | GRAPHIC | Grayscale visible-satellite time-lapse, 1425–2155 UTC | none | narrated |
| 508 | 517 | 9 | REAL-FOOTAGE | Ground-level developing storm tower, blue sky | unconfirmed provenance | narrated |
| 517 | 527 | 10 | GRAPHIC | Road-map radar loop, OKC metro, green report dots, reflectivity building | none | narrated |
| 527 | 536 | 9 | — | Black transition frame | none | — |
| 536 | 554 | 18 | GRAPHIC | Wide KTLX reflectivity loop, supercells NW–SE across OK, "4:48–5:23 PM" | none | narrated |
| 554 | 560 | 6 | GRAPHIC | Zoomed reflectivity, CALUMET/EL RENO labels, hook structure, "5:51:40 PM" | none | narrated |
| 560 | 571 | 11 | GRAPHIC | Storm-relative velocity radar (red/green couplet), same labels/time | none | narrated |
| 571 | 580 | 9 | REAL-FOOTAGE | Hazy dark funnel/wall-cloud silhouette, low contrast | unconfirmed (dark) | narrated |
| 580 | 599 | 19 | REAL-FOOTAGE | Wide NW shot, rotating wall cloud/tornado, direction bar "NW" | **"Garfield"** | narrated/possible sync |
| 599 | 610 | 11 | REAL-FOOTAGE | Very dark exposure, car silhouette, wall cloud barely visible | **"Garfield"** | possible sync |
| 610 | 620 | 10 | REAL-FOOTAGE | Wide W-NW, large wedge behind trees, yellow gate/fence, "Garfield 6:03 p.m." | **Gabe Garfield** | narrated/possible sync |

### Segment 620–930s

| in_s | out_s | dur_s | class | description | credit/flag | audio |
|---|---|---|---|---|---|---|
| 620 | 628 | 8 | — | Black transition/cut | none | narrated |
| 628 | 645 | 17 | GRAPHIC | Radar heatmap, position pin, "6:03:09 PM CDT" | MEDIUM-RISK — pin: Tempest Tours | narrated |
| 645 | 691 | 46 | REAL-FOOTAGE | Static tripod shot, rain-wrapped wedge over farmland/grain bins, tourists flee | **Gullickson/Tempest Tours** | narrated |
| 691 | 700 | 9 | REAL-FOOTAGE | Close/rear-view, twin sub-vortices ahead on road | **Gullickson/Tempest Tours** | narrated |
| 700 | 717 | 17 | GRAPHIC | Radar heatmap, position pin, "6:06:21 PM CDT" | MEDIUM-RISK — pin: Sullivan/Wright | narrated |
| 717 | 746 | 29 | REAL-FOOTAGE | Static wide, distant funnel over field, barn/farmhouse | **Sullivan** | narrated |
| 746 | 765 | 19 | GRAPHIC | Radar heatmap, dual pins | MEDIUM-RISK — pins: Sullivan/Wright, Demko/Farrar | narrated |
| 765 | 790 | 25 | REAL-FOOTAGE | Dark rain-obscured field, tornado barely visible as lit shaft | **Farrar/Demko** | narrated |
| 790 | 800 | 10 | GRAPHIC | Zoomed radar/satellite map, dual pins, "6:12:08 PM CDT" | MEDIUM-RISK — pins: Talbot/Brindley, Demko/Farrar | narrated |
| 800 | 815 | 15 | REAL-FOOTAGE | Road-level facing tornado/dust wall, two vehicles headlights on | **Talbot** | narrated |
| 815 | 844 | 29 | GRAPHIC | Annotated aerial map, "CONDENSATION FUNNEL" vs "TORNADO EDGE" wind-field circle | MEDIUM-RISK — label: Talbot/Brindley | narrated |
| 844 | 852 | 8 | GRAPHIC | Distance-scale overlay over stormy-sky footage | MEDIUM-RISK — Talbot/Brindley, Samaras/Young | narrated |
| 852 | 853 | 1 | — | Black transition frame | none | narrated |
| 853 | 862 | 9 | REAL-FOOTAGE | Road view, person standing on car hood, tornado dust obscured | **Talbot** | narrated |
| 862 | 870 | 8 | REAL-FOOTAGE | White water tower/grain structure, distant storm clouds | **Talbot** | narrated |
| 870 | 872 | 2 | REAL-FOOTAGE | Dark rainy field, faint funnel silhouette | **Talbot** | narrated |
| 872 | 886 | 14 | GRAPHIC | Radar heatmap, pins, "6:13:59–6:14:37 PM CDT" | MEDIUM-RISK — pins: Talbot/Brindley, McGowan | narrated |
| 886 | 915 | 29 | REAL-FOOTAGE | Vehicle-POV into rain, then twin-funnel/satellite-tornado shot | **Bohac** | narrated |
| **915** | **922.5** | **7.5** | GRAPHIC | Radar heatmap, "Henderson"/"Bettes/TWC" pins | **HARD EXCLUDED — carries private family photo inset, see above** | narrated |
| 922.5 | 930 | 7.5 | REAL-FOOTAGE (low-conf) | Near-black, indistinct | too dark to classify | narrated (likely) |

### Segment 930–1240s

| in_s | out_s | dur_s | class | description | credit/flag | audio |
|---|---|---|---|---|---|---|
| 930 | 935 | 5 | REAL-FOOTAGE | Wide roadside, rain-wrapped tornado crossing field | **Garfield** (partial overlay) | narrated |
| 935 | 945 | 10 | REAL-FOOTAGE | Dash/hood-cam push toward tornado through rain/dust | **Gribble** | narrated |
| 945 | 973 | 28 | GRAPHIC | Radar heatmap loop, Hwy 81/Reno Rd, marker "3" tracked, "6:18–6:21 PM" | MEDIUM-RISK — pins: Henderson, Bettes/TWC | narrated |
| 973 | 985 | 12 | PHOTO-STILL | Wrecked "Tornado Hunt 2013" SUV, roof crushed, field at night (TWC rollover) | **Sean Schofer** (photo credit) | narrated |
| 985 | 1014 | 29 | GRAPHIC | Radar loop continues, marker "3" north on Hwy 81, "6:19–6:20 PM" | MEDIUM-RISK — pin: Robinson | narrated |
| 1015 | 1046 | 31 | GRAPHIC | Annotated aerial map: condensation funnel (blue) vs full wind-field edge (red), width-comparison arrows | MEDIUM-RISK — caption: Robinson | narrated |
| 1046 | 1057 | 11 | GRAPHIC | Aerial map, looping yellow DOW-derived sub-vortex path over TWISTEX crew location, "6:23:00–6:23:57" | **none — clean, "TWISTEX location" label only** | narrated |
| 1057 | 1069 | 12 | GRAPHIC | Radar reflectivity loop, marker "3" north, "6:25–6:33 PM" | **none — clean** | narrated |
| 1070 | 1080 | 10 | GRAPHIC | Radar reflectivity, single frame near El Reno, "6:42 PM" | MEDIUM-RISK — pin: Talbot/Brindley | narrated |
| 1080 | 1093 | 13 | REAL-FOOTAGE | Blurry handheld/vehicle push through wind-whipped branches | **Talbot** | narrated |
| 1093 | 1104 | 11 | GRAPHIC | Radar loop continues, marker "3" past airport, "6:33–6:42 PM" | **none — clean** | narrated |
| 1104 | 1124 | 20 | TEXT-SLIDE | Title card "What We (Re)Learned" over wedge-tornado photo | bg credit: Jennifer C Brindley | narrated |
| 1124 | 1165 | 41 | GRAPHIC | Same slide, bullet "Tornado motion is unpredictable" + EF-0 contour inset map | bg credit: Jennifer C Brindley | narrated |
| 1165 | 1189 | 24 | GRAPHIC | Same slide, "Tornadoes can expand rapidly" + inset chaser-video still | Brindley bg; Sullivan inset | narrated |
| 1189 | 1222 | 33 | GRAPHIC | Same slide, "winds often extend beyond condensation funnel" + funnel/edge map + annotated photo | Brindley; Talbot/Brindley; Talbot | narrated |
| 1222 | 1240 | 18 | GRAPHIC | Same slide, "Multiple simultaneous tornadoes...", "Satellite tornadoes" sub-bullet | bg credit: Jennifer C Brindley | narrated |

### Segment 1240–1547s (end)

**Coverage correction:** the automated pass's presumed 256s single "shot" (1291–1547s) is actually three distinct content blocks — confirmed by direct inspection, not assumed.

| in_s | out_s | dur_s | class | description | credit/flag | audio |
|---|---|---|---|---|---|---|
| 1240 | 1291 | 51 | GRAPHIC | "What We (Re)Learned" slide, multi-tornado bullet, cycling 3 illustrative historical-tornado insets (Chickasha OK 1999, El Reno OK 2006, Cherokee OK 2012) | Brindley bg; insets credited Roger Edwards & Rich Thompson, Brett Roberts/skyinmotion.com | narrated |
| 1291 | 1372 | 81 | GRAPHIC | Static NEXRAD radar still (KTLX, "6:14:37 PM") under sequential callouts: LARGE HAIL / NOTCH / TORNADO circles, then "SHARP LEFT TURNS," "POOR VISIBILITY" + HEAVY RAIN, "INFLOW WINDS," "NEW TORNADOES" | **none — clean** | narrated |
| 1372 | 1395 | 23 | GRAPHIC | "Quick escapes may not exist" slide, sub-bullets building | bg credit: Jennifer C Brindley | narrated |
| 1395 | 1442 | 47 | GRAPHIC | "Suggestion" slide, bullets (give tornadoes more space, volatile parameters, etc.) | bg credit: Jennifer C Brindley | narrated |
| 1442 | 1488 | 46 | GRAPHIC | "Closing Thoughts" slide, bullets (chasers have survived; sub-vortex winds; close encounters increase odds) | bg credit: Jennifer C Brindley | narrated |
| 1488 | 1512 | 24 | TEXT-SLIDE | Final "Closing Thoughts" bullets + ghosted memorial names fading in: Tim Samaras, Paul Samaras, Carl Young | Brindley bg; ghosted memorial names | narrated then silence |
| 1512 | 1524 | 12 | TEXT-SLIDE | End-credit card: "Produced by" — Gabe Garfield, Skip Talbot | production credit | silence/music |
| 1524 | 1535 | 11 | TEXT-SLIDE | End-credit card: "Video by" — Ray Bohac, Dave Demko, Heidi Farrar, Gabe Garfield, Mikey Gribble, Chris Gullikson, Justin Hoyt, Dick McGowan, Forrest Mitchell, Dan Robinson, Brandon Sullivan, Skip Talbot | production credit (master name list) | silence/music |
| 1535 | 1546 | 11 | TEXT-SLIDE | End-credit card: "Consulting" — Marc Austin, Chuck Doswell, Jon Garner, Rick Smith, Bryan Smith, Jeff Snyder, Skip Talbot, Rich Thompson | consulting credit (not footage owners) | "Thank you" near end |
| 1546 | 1547 | 1 | GRAPHIC | Sponsor/agency logo card — NWS, CIMMS, SKYWARN, NOAA | none | "Thank you." |

## No talking-heads

Zero TALKING-HEAD shots found anywhere in the 1547s runtime — the film never cuts to a person speaking to camera. No unidentifiable-speaker exclusion applies.
