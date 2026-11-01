# BRIEF: the "radar replot" family (ep4-el-reno, 11 comps, built 10 Oct 26)

Our own plan-view redraw of what the mobile research radars measured. Not a copy of any figure in the paper: no figure
was downloaded, traced or pasted. Geometry comes from the numbers quoted in `fact_check.md` and
`research/angle-facts-2026-10-09.md` through the scale below.

## 0. What the family claims
One very wide circulation (2.6 miles across at its widest) with one much smaller interior sub-vortex inside it. That one
sub-vortex met two crews on two roads: the TV crew on US-81 while it crossed at about 56 mph, and the research car on
Reuter Road between four and five minutes later while it sat nearly still for about 20 seconds.

## 1. SOURCE (quoted passages; W14 = Wurman et al. 2014, BAMS 95(1); OUN = NWS Norman event page; PNS = NWS Norman statement 4 Jun 2013)
- Width: PNS "PATH WIDTH /MAXIMUM/: 2.6 MILES", measured after the tornado passed east of US-81 (fact_check A2-S1).
- Sub-vortex size: W14, 90 to 230 m across (295 to 755 ft). Drawn at the middle, 160 m (525 ft), labelled "about 300 to 750 ft".
- One sub-vortex: W14 "a large tornado/MVMC with a single (at this time) embedded subvortex"; "the interior subvortex, which was nearly concentric with the larger tornado/MVMC and moving with a similar Vp, is displaced"; "it was an interior subvortex that impacted both the Samaras and Weather Channel teams".
- US-81: W14 centre of both circulations crossed US-81 "moving rapidly east-northeastward, with Vp ~ 25 m/s" (55.9 mph); "Westerly winds on the southern side of the central vortex exceeded 83 m/s at 120 m AGL" (394 ft); vehicle carried "to the east side of US-81"; about 200 yards (`facts.md`, weather.com). OUN: crossing at 6:19 PM CDT.
- Reuter Road: W14 sub-vortex intensified about 500 m (547 yards) to the south-southeast, moved north-northwest, "nearly stationary over Reuters Road from 2323:35 to 2323:57 UTC" (6:23:35 to 6:23:57 PM CDT, 22 s), "centered just to the east of the inferred starting position" of the car; winds in it over 81 m/s (181.2 mph); car about 530 m (580 yards) west of the Reuter and Radio roads crossing, found 50 to 100 m north-east of it, about 600 m (656 yards) in about 20 s; "was not especially heavy or armored, likely adding to its vulnerability"; "With only 30-s potential warning ... it is likely that no clear direction to safety was apparent."
- Speeds: W14 sub-vortex forward speed "Vp as high as 79 m/s" (176.7 mph, 259 ft/s); OUN "winds of at least 295 mph very close to the surface ... in very small sub-vortices"; OUN "none of these intense sub-vortices impacted any structures in rural Canadian County".
- Others: `facts.md` (survey paper, Marshall et al.): intermittent sub-vortices; an anticyclonic (clockwise) tornado east-southeast of the main tornado.
- Roads: OpenStreetMap road geometry, read 10 Oct 26 (team lead's Overpass measurement; my own Overpass pull the same day agrees within 0.02 mile). US-81 at longitude -97.9379; Reuter Road at latitude 35.4790; Reno Road 1.00 mile south of Reuter Road; Radio Road 2.04 miles east of US-81; the research car, 530 m west of Radio Road (W14), 1.71 miles east of US-81. My pull: US-81 -97.9381, Radio Road -97.9016 (2.05 miles), car 1.73 miles, Reno Road 35.4645; in it the way named "Radio Road" ends at Reno Road, so its longitude at Reuter Road is read off the same section line. The lead's numbers are the one layout for all families and are the ones drawn.
- Rating: PNS 4 Jun 2013 upgrade to EF5; OUN reason for EF3. Date of the return to EF3: NOT CONFIRMED, not shown.

## 2. DATUM, SCALE, ORIENTATION
- North is up in every frame. Compass mark top right (x 1760, y 120). US-81 is a vertical line, Reuter Road a horizontal line, Radio Road a vertical line.
- **Family scale: 300 px per mile** (overview frames). Scale bar "1 mile" = 300 px at x 96 to 396, y 986.
- **Road-level frames are the same drawing at a declared 4x zoom: 1200 px per mile** (0.6818 px per yard, 0.7456 px per m). Scale bar "500 yards" = 341 px at x 96 to 437, y 986. Used by a3s2, a3s8, a3s9, a3s13.
- a2s6 has one inset lens at 1 px = 2.5 ft with its own printed bar.

## 3. GEOMETRY (px, hit within 10)
| Thing | Overview (300 px/mi) | Road level (1200 px/mi) | From |
|---|---|---|---|
| Wide ring | r 390, diameter 780. Road-map comps (i1s8, a2s11, a3s11): centre (1000, 630) at 6:19 PM, then moved by (+300, -160), schematic. Other overviews (a2s6, a2s7, a2s8, a5s2): centre (1040, 548), no roads drawn | r 1560: off frame, stated in a label | 2.6 miles (PNS) |
| Sub-vortex | diameter 30 (r 15) | diameter 119 (r 60) | 160 m, middle of 90 to 230 m (W14) |
| US-81 | vertical line x 1000 | a3s2: x 1000; a3s13 left: x 420 | N to S; ring centre crossed it (W14); OpenStreetMap |
| Reuter Road | horizontal line y 330 | a3s8/a3s9: y 430; a3s13 right: y 420 | E to W; OpenStreetMap |
| Reno Road | horizontal line y 630 = Reuter Road + 300 | not drawn | 1.00 mile south of Reuter Road (OpenStreetMap) |
| TV crew marker | on US-81 at (1000, 630), labelled "position approximate" | on US-81, on the circle's south side | OUN: the crossing was near Reno Road; where on US-81 the crew was is not measured |
| Research car marker | on Reuter Road at (1513, 330) = US-81 + 513 | (940, 430) | 1.71 miles east of US-81 (OpenStreetMap + W14) |
| Radio Road | vertical line x 1612 = US-81 + 612 | vertical line x 1335 = car + 395 | 2.04 miles east of US-81 (OpenStreetMap); 530 m east of the car (W14) |
| Track, last leg | from (1549, 416) to the car: 93 px from the south-southeast | see "Vortex strengthens" | 500 m (W14); the rest of the track is schematic |
| Vortex strengthens | not drawn | (1083, 774) = car + (143, 344), south-southeast | 500 m (W14) |
| Vortex stops | at the car marker | centre (975, 430), "just east", offset schematic | W14 |
| Carried to | not drawn | (1374, 390) = crossing + 75 m north-east; line 447 px | 600 m, 50 to 100 m NE (W14) |
| 200 yards | not drawn | 136 px | weather.com via facts.md |
| Motion at US-81 (a3s2) | | 18.6 px per second toward east-northeast = real speed at this scale | 25 m/s (W14) |

## 4. MUST BE TRUE IN THE PICTURE
1. Ring diameter 780 px against a 300 px "1 mile" bar (2.6 to 1). Small circle 30 px in overview, 119 px at road level; never larger than 1/18 of the ring in an overview frame.
2. One small bright circle only at the two roads. Its earlier position is a hollow dashed outline of the same mark, never a second filled circle. Other sub-vortices (a2s8, a5s2) are thin pale dashed circles and named; the clockwise tornado (a2s8) is a red mark outside the ring to the east-southeast and named.
3. Every number on screen is in section 1. "about" kept where the source or script says about. 175 mph = forward speed, "Wurman et al. 2014". 295 mph = wind inside the sub-vortices, "National Weather Service". No EF3 date.
4. North up. US-81 vertical, Reuter Road horizontal. US-81 event first, Reuter Road second. Vortex at US-81 moves toward east-northeast; at Reuter Road it comes from the south-southeast moving north-northwest. Car carried east, past Radio Road, to a point north-east of the crossing. SUV carried to the east side of US-81.
5. Not measured here, so dashed and labelled: the track between the two roads; where on US-81 the TV crew was ("position approximate", no distance from Reuter Road printed); where the ring sat after 6:19 PM; the route the car was carried along (only start and end are sourced); the clockwise tornado's distance and size; every track and building dot in a5s2.
6. Crews are a square (TV crew) and a diamond (research car) with a label. No vehicle, person or wreckage drawing. "survived" is the only outcome word.
7. Ring ticks turn counter-clockwise (the usual direction); only the a2s8 second tornado turns clockwise.

## 5. PER COMP: claim, text, cues (seconds, from audio/<segment>.words.json)
- **g-i1s8-replot** (11.67 s). Claim: 3 of 3 survived in the SUV, 0 of 3 in the Cobalt; one small circle, two positions. Text: "3 of 3" "survived · TV crew, SUV"; "0 of 3" "survived · research car, Cobalt"; "Our redraw of mobile-radar measurements · Wurman et al. 2014"; "1 mile"; "Positions between the roads: schematic". Map marks, shapes as in g-a2s11-replot, drawn above the circle with a dark outline (square 22 px, diamond 32 px tip to tip, so the corners reach past the circle's edge): a square at the first position (US-81 at Reno Road) lands on "both", a diamond at the second (the car on Reuter Road) lands at 10.54. Cues: survived 1.48 · Cobalt 3.66 · radar 5.16 · both 7.78 · two 9.34 · same 10.72.
- **g-a2s6-replot** (14.7 s). Claim: the sub-vortex was about 300 to 750 ft across inside a circulation more than 45 fields wide. Text: "Sub-vortex"; "about 300 to 750 ft"; "across · Wurman et al. 2014"; "1 field"; "2½ fields"; "More than 45 fields across"; "1 mile"; "Lens: 1 field = 300 ft". Cues: sub-vortex 1.36 · 300 5.66 · 750 6.30 · one 8.84 · two and a half 9.16 · inside 10.98 · 45 12.68.
- **g-a2s7-replot** (20.83 s). Claim: forward speed up to about 175 mph (about 260 ft a second); wind inside about 295 mph. Text: "about 175 mph" "Forward speed, up to · Wurman et al. 2014"; "about 260 feet every second"; "about 295 mph" "Wind inside · National Weather Service"; "Track shown: schematic". "about 260 feet every second" and the field strip land together on "field". Cues: direction 2.84 · 175 8.28 · field 11.74 · second 12.50 · faster 15.24 · 295 18.26.
- **g-a2s8-replot** (12.02 s). Claim: other sub-vortices came and went; a second tornado nearby spun clockwise. Text: "Other sub-vortices" "came and went"; "Second tornado" "spinning clockwise"; "Marshall et al., damage survey and radar analysis"; "Usual direction"; "Second tornado: position and size schematic". Cues: alone 1.62 · other 4.94 · went 6.70 · second 7.70 · clockwise 9.12 · usual 10.48. The satellite tornado is left out: this segment's narration does not speak it (it moved to A2-S9).
- **g-a2s11-replot** (21.89 s). Claim: one sub-vortex, US-81 first, Reuter Road between four and five minutes later. Text: "US-81"; "Reuter Road"; "One sub-vortex"; "TV crew"; "6:19 PM · NWS"; "4 to 5 minutes later"; "Research car"; "One vortex. Two roads."; "Track between the roads not measured here · schematic". Cues: Highway 1.46 · one 4.58 · struck 7.42 · Between 10.42 · struck 12.36 · Cobalt 13.12 · Reuter 13.82 · one small 15.56 · What 20.22.
- **g-a3s2-replot** (8.02 s). Claim: crossing US-81 at about 56 mph toward east-northeast; air on its south side blowing east. Text: "about 56 mph" "Forward speed · Wurman et al. 2014"; "US-81"; "TV crew"; "Air blowing east" "south side · measured about 400 ft up"; "Shown at real speed · 500 yards"; bottom left, two lines that both end left of the US-81 line: "The wide circulation's edge is outside this view" and "Our redraw of mobile-radar measurements". Cues: met 0.46 · 56 2.80 · south 5.30 · east 6.86.
- **g-a3s8-replot** (20.79 s). Claim: strengthened about 550 yards south-southeast of the car, moved north, reached Reuter Road at 6:23:35 PM and nearly stopped for about 20 s. Text: "Reuter Road"; "Radio Road"; "Research car"; "about 550 yards"; "Strengthens here"; "4 to 5 minutes after US-81"; "6:23:35 PM"; counter "0 to 20" "about 20 seconds · nearly still"; "Loop from US-81 not measured here". Cues: looped 2.60 · strengthened 5.74 · 550 6.48 · north 9.60 · Between 11.58 · reached 15.00 · stopped 16.60 · 20 19.28.
- **g-a3s9-replot** (18.75 s). Claim: centre just east of the car; wind over 180 mph; carried about 650 yards in about 20 s past Radio Road. Text: "over 180 mph" "Wind inside it · Wurman et al. 2014"; "Vortex center, just east"; "Not especially heavy or armored"; "about 650 yards" "in about 20 seconds"; "about 580 yards to Radio Road"; "Carried to here"; "Start and end from the paper · route between not measured". Cues: east 1.62 · 180 5.98 · heavy 9.92 · 20 12.84 · 650 14.48 · past 15.88 · Radio 17.32.
- **g-a3s11-replot** (12.28 s). Claim: 30 s of possible warning; the paper's sentence. Text: "30 seconds" "of possible warning"; quote card "it is likely that no clear direction to safety was apparent" "Wurman et al., Bulletin of the American Meteorological Society, 2014"; "Looping track: schematic". Cues: 30 1.64 · changing 6.56 · concludes 8.46 · no clear 10.08.
- **g-a3s13-split** (24.23 s). Claim: same vortex, same scale: crossing at about 56 mph and 200 yards; nearly still about 20 s and 650 yards. Text left: "US-81 · TV crew" "about 56 mph" "about 200 yards"; right: "Reuter Road · research car" "nearly still · about 20 seconds" "about 650 yards"; quotes "This high [forward speed] likely contributed to injuries among a media team" and "not especially heavy or armored, likely adding to its vulnerability", each "Wurman et al. 2014"; "Both sides to one scale · 500 yards". Cues: SUV 0.46 · 200 4.20 · Cobalt 6.22 · still 7.16 · three times 10.06 · speed 13.56 · light 18.96 · no single 22.32.
- **g-a5s2-rating** (11.94 s). Claim: EF5 back to EF3 (no date); fastest air in the small sub-vortices; none crossed a structure. Text: "EF5"; "EF3"; "Rating"; "Fastest air: inside the small sub-vortices"; quote card "none of these intense sub-vortices impacted any structures in rural Canadian County" "NWS Norman"; "Structures"; "Tracks and structures: schematic, not a survey map". The three sub-vortices are thin pale dashed circles (item 2), no fill, no glow; no structure square sits on the ring line. Cues: EF3 2.62 · fastest 4.24 · sub-vortices 5.88 · wrote 7.08 · none 8.02 · structure 9.30.

## Not confirmed in the fact files, left off or drawn as schematic
- Where along US-81 the TV crew was. It is drawn at the Reno Road crossing because OUN puts the tornado's highway crossing "near Reno Road", and labelled "position approximate". (The east to west distance to the research car is now sourced: 1.71 miles, OpenStreetMap + W14.)
- The ring's width and position at each of the two moments (2.6 miles is the maximum, reached minutes after US-81). The car is 1.98 miles from the US-81 point on this layout, more than the ring's 1.3 mile radius, so the ring is shown moving to keep the interior sub-vortex inside it; how far it moved is schematic.
- The sub-vortex track between 6:19 and 6:23:35 PM.
- The clockwise tornado's distance from the main tornado and its size; where any structure stood (a5s2).
- The date of the return to EF3.
