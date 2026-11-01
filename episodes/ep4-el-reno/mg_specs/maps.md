# mg_specs/maps.md: the "track maps" family (ep4-el-reno), 9 comps

Builder brief on `references/mg-brief-template.md`, sections 0 to 5, written before drawing (10 Oct 26).

## 0. What the family claims
One tornado, drawn from the weather service's own track file, on one map that never changes shape: it touched down at
6:03 PM west of El Reno, ran about 16 miles over open farmland in about 40 minutes, sped up and turned left, grew to
2.6 miles wide just east of Highway 81, and ended on Interstate 40 at 6:43 PM. The tornadoes that entered Oklahoma City
that evening were EF0 and EF1 and are small beside it.

## 1. Source (every number on screen)
| Thing | Value | Source |
|---|---|---|
| El Reno track centreline (56 points), minute positions 6:04 to 6:42 PM CDT, damage contour (72 points) | coordinates | `media/data/tracks.json` and `media/data/nws-oun-el-reno-tornado-path.kmz` (NWS Norman, ElRenoTornadoPath_final.kmz) |
| Start 6:03 PM, end 6:43 PM, about 40 minutes, 2.6 miles maximum width, 16.2 miles (OUN table: 16) | times, sizes | NWS Norman statement of 4 Jun 2013 (PNS), `fact_check.md` I1-S1, `tracks.json` |
| Width reached 2.6 miles "after the tornado passed east of US Highway 81", maximum size 6:24 to 6:26 PM CDT | width timing | `fact_check.md` A2-S1 (PNS, OUN) |
| Crossed Highway 81 at 6:19 PM, 16 minutes after touchdown | time | `fact_check.md` Acts 1 and 2 (OUN) |
| Forward speed "from approximately 35 mph to more than 50 mph", "a sharp left turn" | speed, turn | NWS Service Assessment, `fact_check.md` Acts 1 and 2 |
| "believed to be the widest tornado on record in the United States" | quote | PNS, `fact_check.md` A2-S8 |
| Hallam, Nebraska, 22 May 2004: maximum width 2.5 miles, F4 | width | NWS Omaha event page, https://www.weather.gov/oax/event_archive_20040522 ("Max Width 2.5 miles"), read 10 Oct 26. Not in `fact_check.md`: new number, flagged in the receipt |
| Oklahoma City tornadoes 10 (EF0 then EF1, ends SW 15th and Meridian 7:09 PM), 13 (EF1), 14 (EF0), 15 (EF1), no lives lost | begin and end points, ratings | `tracks.json` (OUN table and Storm Data; Storm Data points are rounded to 0.01 degree). Tornado 10 also has the NWS EF1 damage polygon (SWOKC_poly.kmz) |
| Survey points: 337 NWS Damage Assessment Toolkit points inside the El Reno contour (134 homes: 71 residences + 63 manufactured homes; 10 business points: retail, small professional, service station) | dots | `media/data/nws-dat-damage-points-el-reno-okc-2013-05-31.geojson`, filtered by script to points inside the NWS contour |
| Manufactured homes cluster: 31 toolkit points at lon -97.880 to -97.876, lat 35.490 to 35.493, about 0.6 mile south of Interstate 40 | place | same geojson (class "Manufactured Home") |
| Under 10 markers per square mile away from one cluster; 69 per square mile in the manufactured homes; 112 oil tank batteries; radar speeds 10 to 30 percent higher | survey figures | Marshall et al. survey paper via `research/facts.md`, `fact_check.md` Acts 4 and 5 |
| "Mobile homes and trailers are not safe. Evacuate immediately and seek shelter in a sturdy building." | exact words | NWS Wilmington, `fact_check.md` "Manufactured homes (A5-S5)" |
| Interstate 40, Interstate 35, Interstate 44, US-81, Reuter Road | road lines | US Census TIGERweb Transportation service (public domain), queried 10 Oct 26, simplified to 0.3 px |

Two limits, stated: the toolkit points are the weather service's survey points, not the 601 markers of the Marshall paper;
the dots are labelled "NWS damage survey points" and the Marshall figures are printed as text with their own source line.
The KMZ centreline measures 17.3 miles because it follows the loop north of Interstate 40; the screen says 16 miles, the official length.

## 2. Datum, scale, orientation
North up. Metro frame 1920 x 1080: x = (lon + 98.20) * 1920, y = (35.70 - lat) / 0.46 * 1080. 1 mile = 34.08 px at zoom 1.
Every map is one SVG whose `viewBox` is a window of the metro frame, so all geometry keeps its metro px; zoom = 1920 / viewBox width.
Lines keep their screen width (`vector-effect: non-scaling-stroke`). Text sits on a fixed layer in screen px.

| Point | lat, lon | metro px |
|---|---|---|
| El Reno | 35.532, -97.955 | 470, 394 |
| Downtown Oklahoma City | 35.468, -97.516 | 1313, 545 |
| Track start, 6:03 PM | 35.4800, -98.0713 | 247, 517 |
| 6:10 PM (turns east) | 35.4547, -98.0415 | 304, 576 |
| 6:19 PM (Highway 81) | 35.4531, -97.9405 | 498, 580 |
| 6:24 PM (widest, 6:24 to 6:26) | 35.4783, -97.9059 | 565, 520 |
| 6:27 PM (crosses Interstate 40) | 35.4983, -97.8907 | 594, 474 |
| Loop north of the interstate, 6:29 to 6:35 PM | about 35.505, -97.889 | 590 to 607, 452 to 463 |
| Track end, 6:43 PM | 35.5012, -97.8481 | 676, 467 |
| US-81 south of Interstate 40 | lon -97.9371 | x 505 |
| Interstate 40 at the track | lat 35.501 | y 467 |
| Reuter Road | lat 35.477 | y 519 |
| Manufactured homes cluster | 35.4915, -97.878 | 619, 489 |
| City tornado 10 (EF0 then EF1) | 35.45, -97.70 to -97.60 | 960 to 1152, 587 |
| City tornado 13 (EF1) | 35.41, -97.55 to 35.40, -97.53 | 1248, 681 to 1286, 704 |
| City tornado 14 (EF0) | 35.41, -97.46 to -97.45 | 1421 to 1440, 681 |
| City tornado 15 (EF1) | 35.34, -97.61 to 35.35, -97.59 | 1133, 845 to 1171, 822 |

## 3. Geometry per comp (viewBox, zoom, scale)
| Comp | viewBox (metro px) | zoom | 1 mile on screen | true-scale shapes |
|---|---|---|---|---|
| g-i1s1-map | 0 0 1920 1080, then 140 330 640 360 | 1, then 3 | 34 px, then 102 px | 2.6 mile bar = 266 px at zoom 3 (metro x 531 to 620, y 508) |
| g-a1s3-south | 320 95 1600 900 | 1.2 | 41 px | none (the south arrow is a direction, not a distance) |
| g-a1s9-landuse | 140 330 640 360 | 3 | 102 px | 1 mile scale bar 102 px |
| g-a1s10-track | 140 330 640 360 | 3 | 102 px | 1 mile scale bar 102 px |
| g-a2s1-width | 368 440 320 180 | 6 | 204 px | ring and bar 2.6 miles = 532 px, ring centred on the 6:24 PM position; Hallam outline 2.5 miles = 511 px |
| g-a4s9-citymap | 230 300 1280 720 | 1.5 | 51 px | 5 mile scale bar 256 px; El Reno contour at the same scale |
| g-a5s4-strip | 114 431 691.2 194.4 in a 1728 x 486 box | 2.5 | 85 px | 1 mile scale bar 85 px |
| g-a5s5-homes | 540 433 160 90 | 12 | 409 px | half mile scale bar 204 px |
| g-a5s6-citymap | 100 300 1280 720, then 440 300 1280 720 | 1.5 | 51 px | 5 mile scale bar 256 px |

## 4. Must be true in the picture
1. Every place, time, speed, width, distance and rating on screen is in the table in section 1, with "about" where the source says about.
2. The track follows the 56 NWS points: south-east from the start, east from about 6:10, left (north-east, then north) after Highway 81 at 6:19, a loop north of Interstate 40, east to the end on the interstate.
3. The 2.6 mile bar is 88.6 metro px times the zoom; the Hallam outline is 85.2 metro px times the zoom; ratio 1.04.
4. The city tornadoes sit east of the El Reno track, between x 960 and x 1440 in the metro frame, and the longest (tornado 10, about 6 miles) is shorter than half the El Reno track.
5. Dots come only from the toolkit file. No dot, square or icon stands for a person.
6. No pins, no people, no chaser imagery. Death words: "lost" or a count.
7. Nothing on screen runs ahead of or against the sentence being spoken.

## 5. Per comp: claim, text, cues (seconds from the segment's words.json)
The comp files are the record of the final text and cue times (each cue carries its word and second in a comment); the lists
below are the plan they were built from. Added while building: "NWS table: no one lost inside them" (g-a1s9-landuse),
"IN ANY OF THEM · NWS NORMAN" under "NO LIVES LOST" and "TRACKS: NWS NORMAN, STORM DATA" (both city maps), "WIDE · NWS NORMAN"
(g-i1s1-map), "THE ASSESSMENT'S WORD" and "THE ADVICE THAT EVENING" (g-a1s3-south), "storage tanks beside oil wells" and
"WIND SPEED WHERE BOTH COULD BE COMPARED" (g-a5s4-strip), "THE DENSEST CLUSTER OF DAMAGE" (g-a5s5-homes).
Schematic, not surveyed, and labelled or noted as such: the 1 mile field grid and the El Reno block (g-a1s9-landuse), the storm
arcs and the south arrow (g-a1s3-south), the built-up block texture (g-a5s6-citymap), the ring before 6:24 PM (g-a2s1-width),
the traffic dashes (g-i1s1-map).

### g-i1s1-map (window 19.56)
Claim: where and when. Text: "CENTRAL OKLAHOMA · FRIDAY, MAY 31, 2013", "Oklahoma City", "El Reno", "6:03 PM" / "TOUCHDOWN", "ABOUT 40 MINUTES ON THE GROUND", "2.6 MILES WIDE".
| Cue | s |
|---|---|
| map and roads open, "Friday" | 0.68 |
| traffic dashes on the interstates, "already in their cars" | 4.80 |
| "6:03 PM" rail and touchdown blip, "6" | 7.14 |
| root transparent for the tornado clip | 8.70 to 12.20 |
| El Reno and Oklahoma City, "a town west of" | 12.24 |
| track draws, "stayed on the ground" | 14.74 |
| "about 40 minutes", "40" | 15.94 |
| push to zoom 3, "grew" | 16.20 to 17.20 |
| 2.6 mile bar, "2.6" | 17.22 |

### g-a1s3-south (18.66)
Claim: the advice was to drive south; the assessment calls it atypical. Text: "Oklahoma City", "STORMS", "DRIVE SOUTH", beige cite card "atypical" / "NWS Service Assessment · May 2013 Oklahoma Tornadoes and Flash Flooding", sub "not what Oklahomans are normally told".
Cues: arrow "drive" 4.98 · storms band "storms" 6.60 · card "assessment's" 9.70 · word "atypical" 11.22 · sub "not" 12.86 · arrow pulse "overrode" 15.80.

### g-a1s9-landuse (15.64)
Claim: it damaged homes and a few businesses near El Reno; most of the 16 miles was farmland; it crossed three roads. Text: "El Reno", "HOMES" / "BUSINESSES" legend, "NWS DAMAGE SURVEY POINTS", "16 MILES", "OPEN FARMLAND", "HIGHWAY 81", "REUTER ROAD", "INTERSTATE 40", "1 MILE".
Cues: home dots "homes" 1.24 · business dots "businesses" 2.12 · "El Reno" 2.90 · track "16" 7.38 · "open farmland" 8.48 · Highway 81 11.78 · Reuter Road 13.28 · Interstate 40 13.96.

### g-a1s10-track (12.61)
Claim: forward speed rose from about 35 mph to more than 50, then a sharp left turn. Text: "FORWARD SPEED", "ABOUT 35 MPH" then "50+ MPH", "NWS SERVICE ASSESSMENT", "SHARP LEFT TURN", "Highway 81", "1 MILE".
Cues: head starts "tornado" 0.66 · readout "speed" 3.80 · 35 "35" 5.08 · climbs to 50+ "50" 6.94 · turn "left" 9.12 · hold "difficult" 11.36.

### g-a2s1-width (25.64)
Claim: 6:19 PM at Highway 81; within minutes 2.6 miles edge to edge; believed widest on record in the United States; Hallam 2004 was the old mark. Text: "6:19 PM", "HIGHWAY 81", "16 MIN AFTER TOUCHDOWN", "THE CIRCULATION", "2.6 MILES", cite "believed to be the widest tornado on record in the United States · National Weather Service, Norman", "HALLAM, NEBRASKA · 2004" "2.5 MILES", "EL RENO · 2013" "2.6 MILES", "SAME SCALE".
Cues: time "6" 0.42 · 16 min "16" 2.02 · ring at the highway "crossed" 5.16 · ring grows and moves "Within" 7.42 · "circulation" 10.78 · bar "2.6" 12.24 · edge ticks "edge" 13.88 · cite "believed" 16.68 · Hallam outline "old" 21.22 · "Hallam" 22.32 · "2004" 24.04.

### g-a4s9-citymap (15.51)
Claim: several tornadoes entered the city, all EF0 or EF1, the two lowest ratings; none took a life. Text: "Oklahoma City", "EL RENO TORNADO" (dim, for scale), "EF0" / "EF1" tags, "SW 15th / Meridian · 7:09 PM · EF1", scale "EF0 EF1 EF2 EF3 EF4 EF5" bottom two lit, "NO LIVES LOST", "5 MILES".
Cues: tracks draw "Several" 3.26 · tags "EF0" 7.70, "EF1" 9.10 · scale lit "two lowest" 11.00 · "None" 13.66.

### g-a5s4-strip (21.72)
Claim: few things to hit; 112 were oil tank batteries; radar ran 10 to 30 percent above damage. Text: "WHAT THE TORNADO HAD TO HIT", "NWS DAMAGE SURVEY POINTS", "ONE CLUSTER", "UNDER 10 MARKERS PER SQUARE MILE", "112" "OIL TANK BATTERIES", "DAMAGE" / "RADAR" bars, "+10 TO 30 %", "Marshall et al. · damage survey and radar analysis", "1 MILE". Photo slot 480 x 300 at left 96, top 676 (`#s4-photo`), holds a line drawing of tanks until a public domain photo is supplied.
Cues: dots west to east "counted" 1.24 · cluster ring "cluster" 4.20 · "under 10" 6.56 · "112" 8.90 · bars "radar" 15.92, damage 16.50, radar 18.30 · "+10 to 30 %" 19.36.

### g-a5s5-homes (27.21)
Claim: the densest damage was a group of manufactured homes just south of Interstate 40; the weather service says a mobile home is not safe. Text: "INTERSTATE 40", "MANUFACTURED HOMES", "69 MARKERS PER SQUARE MILE", "NWS TABLE: NO ONE LOST IN THEM", safety card with the exact NWS words, "National Weather Service", "1/2 MILE".
Cues: track and road "reach" 1.28 · squares light "cluster" 4.40 · label "manufactured" 6.00 · Interstate 40 "Interstate" 9.90 · table line "no one" 13.06 · safety card "That" 18.08, second sentence "sturdy" 25.82, held to 27.3 with no exit.

### g-a5s6-citymap (10.15)
Claim: in the city every tornado was EF0 or EF1; none took a life. Text: "Oklahoma City", "BUILT-UP AREA (SCHEMATIC)", "EF0" / "EF1" tags, "NO LIVES LOST", "5 MILES".
Cues: slide east "In" 0.00 to 1.70 · city label "City" 0.98 · building blocks "buildings" 2.08 · tracks "every tornado" 3.20 · tags "EF0" 5.26, "EF1" 6.60 · "None" 8.42.

## 6. Fix round, 10 Oct 26 (verifier 2's rows; this section wins where it differs from section 5)
No fact, figure or map position changed. Cue times changed: two, both named by the verifier.
- g-i1s1-map: the base map (roads, both city markers, both city names) is on from frame 0; nothing draws in. Roads are 3 px cold blue, traffic dashes 4.5 px yellow. **"Oklahoma City" is on screen from frame 0, before the voice names it at 12.6 s, on purpose:** the script's picture note for this beat opens on the metro map with Oklahoma City labelled, and for the first 8.7 s the name is the only thing that tells a viewer which road loop they are looking at. Without it the opening is unlabelled lines. The name then beats (scale 1.05) on its word at 13.12. The eyebrow is two lines at left 500 so it clears US-81.
- g-a1s3-south: US-81 is not drawn (it ran through three labels and the beat is about Oklahoma City, not El Reno). "Oklahoma City" sits inside the road loop. Start states are set once at build time and every tween is a plain `to`, so a given second shows the same picture whatever was seeked before.
- g-a1s10-track: panel title "FORWARD SPEED" at 3.80, the number row and source at 5.08 ("35"). "SHARP LEFT TURN" starts at left 1372, clear of the arrow head.
- g-a2s1-width: the ring rides on the head from 0.2 s (schematic before 6:24 PM, as section 5 already says) and beats at 5.16; roads and track are fully out by 21.3 s under the comparison; "HIGHWAY 81" at left 838, top 196; "SAME SCALE" at left 745, top 950; scale bar at left 1250.
- g-a4s9-citymap: the end label is right-aligned to x 1410, about 40 px left of the road line; eyebrow at left 384. Centre-bottom block left empty: the spec plans nothing there.
- g-a5s4-strip: the photo slot (480 x 300 at left 96, top 660) and the outlines of the two bars are on from frame 0 at low strength, then come up on their cues; "UNDER 10" block at left 524, top 152 to 265, off the contour; "ONE CLUSTER" at left 1476 outside the contour with a leader line to the ring.
- g-a5s5-homes: "69 markers per square mile" / "Marshall et al." and "NWS TABLE:" / "NO ONE LOST IN THEM" each break into two lines so they end before the survey dots; the "MANUFACTURED HOMES" label under the ring sits at top 846, below the dots.
