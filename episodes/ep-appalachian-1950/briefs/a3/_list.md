# A3 section graphics: ep-appalachian-1950 (A3-S1 to A3-S8, "The left turn")
Written 28 Oct 26 from `acts/a3.md` (= edit_script.md A3 block, act locked), `audio/a3-s*.words.json`, `research/nws-facts.md`, `research/maps-forecast.md`, `media/candidates/a3/picks.md` + `provenance.csv`.
Every brief carries `references/mg-quickref.md` and `references/mg-brief-template.md` §6-§8 by reference; read both, then `learnings/mg.md`, before building.

| comp id | segments | what it shows (one line) | depth | builder model | library exemplar to start from | sits over |
|---|---|---|---|---|---|---|
| g-a3-1-track | A3-S1 | 25 Nov NWS Jackson chart, dimmed; red track draws from a "CAROLINAS · NOV 24–25" pin north then bends left into Ohio; grey ghost arrow "THE USUAL PATH" runs up the coast and out to sea | deep | Opus 5.5 | `library/official` `svg-stroke-trace` (path draw) + `references/editing-patterns/ep3-map-route-fit.html` (route on a map image) | chart still `A3-S1_c1_nws-jkl-surface-1950-11-25.jpg`, mounted inside the comp (camera C1) |
| g-a3-2-swirl | A3-S2 | Same chart and track; warm-orange arrows sweep in off the Atlantic and curl northwest, cold-blue arrows pour south down the west side, all turning counterclockwise round the low | deep | Opus 5.5 | `references/editing-patterns/ep2-met-explainer.html` (warm/cold air arrows) + `library/official` `arc-motion-path` | same chart still, same camera C1 (continuation of g-a3-1's last frame) |
| g-a3-3-pins | A3-S3 | Newark, Pittsburgh, Buffalo pins land on the swirl; chips "40s · NO SNOW" (Buffalo, warm side), "SINGLE DIGITS · SNOW" (Pittsburgh, cold side); the red track joins the three | standard | Sonnet 5.5 high | `briefs/intro/g-intro-2-hookmap.md` pin and chip spec (same pins as the hook) | same chart still, same camera C1 (continuation of g-a3-2's last frame) |
| g-a3-4-block | A3-S4 | Pull out from the chart to the channel basemap of eastern North America; a broad "H" dome over eastern Canada and the North Atlantic, chip "BLOCKING HIGH"; the grey usual-path arrow runs into it and stops; red track bends inland | deep | Opus 5.5 | `library/inhouse/master-map-us-canada.html` (basemap, projection, camera rig, `logZoom`) | nothing: full-frame designed map (opens as a crossfade from the chart) |
| g-a3-5-gradient | A3-S5 | Same wide map: "L" over the Appalachians between "H" east of Labrador and "H" over the Mississippi Valley; isobar lines bunch tightest over NJ, NY and New England; chip "VERY TIGHT PRESSURE GRADIENT" | deep | Opus 5.5 | `library/inhouse/master-map-us-canada.html` + `references/editing-patterns/ep2-met-explainer.html` | nothing: full-frame designed map |
| g-a3-6-squeeze | A3-S6 | Two gauges "LOW ≈ 980 MB" and "HIGH ≈ 1050 MB" with the gap glowing and the gloss "MB = millibars, a measure of air pressure"; then a coast map: wind arrows ashore onto a Newark pin "108 MPH" and up the Delaware to a Philadelphia pin "RECORD TIDE" | standard | Sonnet 5.5 high | `library/official` `mk-usage-arc` (gauge draw-on) + `library/inhouse/master-map-us-canada.html` (coast basemap, pins) | nothing: full-frame designed card, then full-frame designed map |
| g-a3-7-stall | A3-S7 (0.00 to 9.60) | 26 Nov then 27 Nov NWS Jackson charts crossfade; the red track ends in a tight loop spinning over Lake Erie, chip "STALLED · NOV 27–28" | deep | Opus 5.5 | `svg-stroke-trace` (loop draw) + g-a3-1's chart camera | chart stills `A3-S7_c1_nws-jkl-surface-1950-11-26.jpg`, `A3-S7_c2_nws-jkl-surface-1950-11-27.jpg`, mounted inside the comp |
| g-a3-8-upslope | A3-S7 (9.00 to 15.20) | West Virginia relief map; blue arrows climb the mountain slopes, snow keeps falling, day counter "NOV 29" | standard | Sonnet 5.5 high | `references/editing-patterns/ep5-terrain-map.html` (relief) + `library/inhouse/master-map-us-canada.html` frame A2-W | nothing: full-frame designed map |
| g-a3-9-exit | A3-S7 (14.60 to end) | The hook's split map (frame A2-X) with the red track drawn through it, ending in a dotted line off into Canada, chip "EXITS · NOV 29–30"; Newark pin wind blue, Pittsburgh snow white, Buffalo orange | standard | Sonnet 5.5 high | `library/inhouse/master-map-us-canada.html`; pins from `g-intro-2-hookmap` | nothing: full-frame designed map |
| g-a3-10-south | A3-S8 | Camera pans south off the Lakes; cold-blue arrows keep running past the Ohio River, across Kentucky, down toward Georgia, Alabama and the Florida Panhandle; the snow-white fill stops far short, chip "THE SNOW STOPPED HERE" | deep | Opus 5.5 | `library/inhouse/master-map-us-canada.html` (`logZoom`, camera rig) + `ep2-met-explainer.html` arrows | nothing: full-frame designed map; ends into the chapter blackout |

Count: 10 graphics. Deep 6 (Opus 5.5): g-a3-1, -2, -4, -5, -7, -10. Standard 4 (Sonnet 5.5 high): g-a3-3, -6, -8, -9.
No segment in A3 is "Paul on camera", so no Paul clip and no date/place popfig here. The chapter card "The left turn" belongs to the chapter blackout (DESIGN.md "Chapter blackout table"), not to this list.

## Section-wide decisions (each brief repeats the part it needs)
- **Cues.** Seconds from the segment's own start, on the spoken word (quoted). Multi-word cues land on the first word. Each comp is one segment, so comp time = word time (host data-start = segment start), except the A3-S7 split: g-a3-8 host starts at A3-S7 + 9.00 and g-a3-9 at A3-S7 + 14.60 (each fades in over the previous comp's last 0.6 s); their briefs give both the segment time and the comp time.
- **Whisper text differs from the script in 3 places** (cue words quoted as Whisper wrote them, the voice says the script word): a3-s2 "below." @4.88 = "a low."; a3-s5 "pack" @14.30 = "packed"; a3-s4 "called" @10.32 = "call". No retake (CLAUDE.md retake bar: meaning kept).
- **Corner circle.** Act 3 is narration with the presenter circle on wherever the corner is free (mg-quickref "Corner circle"). Every comp keeps x >= 1600, y >= 680 free of its own labels, numbers, pins, arrows and highlighted shapes for its whole window. On the chart comps (g-a3-1, -2, -3, -7) the scanned chart's own station plots sit in that corner; whether the circle shows there is the orchestrator's frame read, not the builder's.
- **Track colour and ids.** The storm track is one red, `#d0121f` (popfig red, the only red line in the act), 6 px, round caps. The usual-path ghost is `#93a3b2` at 0.55, 5 px, dash 14 10. Warm air `#d8a13a`, cold air `#7fb2e5`, snow `#f2f5f8`. Same values in every comp so the handoffs match.
- **Chart camera C1** (g-a3-1, -2, -3, -7): the chart JPEG (1156 x 759 px) is drawn at scale 2.0 with its top-left at screen (-392, -220), i.e. screen = (chart px - (196, 110)) × 2.0; the image right edge lands exactly on x 1920 and the bottom on y 1298, so the frame is covered. Dim layer `rgba(4,7,12,.38)` over the chart. Chart points (measured by eye off the JPEG, ±15 px; the builder zooms the image, finds each printed station plot and corrects, reporting the values):

| chart point | chart px | screen px (C1) |
|---|---|---|
| low "L" on the 25 Nov chart (Carolinas/Virginia coast) | (838, 398) | (1284, 576) |
| Carolinas pin (track start, just south-west of the L) | (815, 440) | (1238, 660) |
| Washington DC area (track turn) | (845, 320) | (1298, 420) |
| Columbus station (label "Columbus" printed at about (620, 300)) | (651, 311) | (910, 402) |
| Pittsburgh station | (735, 292) | (1078, 364) |
| Buffalo station (east end of Lake Erie) | (762, 222) | (1132, 224) |
| Newark / New York coast | (886, 258) | (1380, 296) |
| Lake Erie centre | (695, 240) | (998, 260) |
| usual-path end, open Atlantic | (1080, 190) | (1768, 160) |

- **Map comps** (g-a3-4, -5, -6, -8, -9, -10) use the episode's one basemap and projection (same as `briefs/a2/_list.md` and `briefs/intro/_list.md`): map x = 3841 × (lon + 97.576), map y = -5585 × (lat - 46.6213); screen = (map - frame top-left) × s. North up. Computed by script 28 Oct 26:

| frame | s | frame top-left (map units) | places on screen (px) |
|---|---|---|---|
| E (eastern North America) | 0.0078 | (-19654.3, -50096.2) | Pittsburgh (680,660), Newark (854,647), Philadelphia (825,681), Buffalo (713,553), Lake Erie centre (644,583), Carolinas 35.5N 78.6W (722,875), H east of Labrador 53.5N 57W (1369,91), H eastern Canada 50N 68W (1039,244), H Mississippi Valley 36N 90W (380,853), L Appalachians 40N 80.5W (665,679), open Atlantic 41N 66W (1099,636) |
| N (coast) | 0.06 | (71559.9, 25871.1) | Newark (1100,420), Philadelphia (871,682) |
| A2-W (West Virginia, from `briefs/a2/_list.md`) | 0.075 | (54186.2, 35931.1) | Parkersburg (549,386), Clarksburg (900,380), Elkins (1043,528), Charleston (529,770) |
| A2-X (split map, from `briefs/a2/_list.md`) | 0.03 | (42191.8, 15852.5) | Newark (1431,511), Pittsburgh (760,560), Buffalo (889,150), Erie (750,277), Lake Erie centre (621,265), Ohio 40.2N 82.8W (437,600), into Canada 45.5N 78.5W (899,-292, off-frame north) |
| T (south) | 0.0125 | (-4474.8, 16919.2) | Pittsburgh (900,220), Lake Erie centre (842,97), Ohio (765,237), Ohio River at Louisville (623,373), Hazard KY (746,443), Atlanta area 33.75N 84.39W (689,687), Pensacola FL (553,919), Carolinas (967,565) |

  The highs, the low and the Carolinas point are schematic positions (no source gives a coordinate); every map comp that draws them says "schematic" in its source line.
- **Source lines.** Arial 700 19 px `#c8d3e0` tracking 2, left 110, bottom 90; basemap credit "Basemap: Natural Earth" at left 110, bottom 60 on map comps; on chart comps the source line sits at bottom 60 alone. Never the right corner.
- **Loops.** g-a3-1 closes cta-hinge and L1 (the track joins the two sides); g-a3-3 opens A3b; g-a3-4 closes A3b, opens A3c; g-a3-6 closes A3c, opens A3d; g-a3-7 closes A3d; g-a3-10 opens A3 (paid in Act 4: no temperature, no town name, no record low on screen).

## Open items for the orchestrator (each brief repeats its own)
1. Chart points are eyeballed (±15 px): the g-a3-1 builder measures them on the JPEG and the rest reuse those values (g-a3-1 receipt lists them).
2. The 25 Nov chart's header date is cropped out of the file (provenance row): no date is printed on screen from the chart itself; the date on screen is the pin's "NOV 24–25" (the disputed formation date, as the Picture line writes it).
3. g-a3-7's loop over Lake Erie sits on the 26/27 Nov charts, whose own low positions differ from 25 Nov; the builder places the loop on the 27 Nov chart's printed low centre and reports it.
4. Asset prep before dispatch: copy `A3-S1_c1_...-25.jpg`, `A3-S7_c1_...-26.jpg`, `A3-S7_c2_...-27.jpg` into `media/a3/` (they are under 1920 px, no trim needed).
5. No numeral on screen without a research row (checked per brief §1). Secondary-only figures: "≈ 980 MB" and "≈ 1050 MB" (NBC Connecticut, factcheck a3-r1 rows 31, 32), carried with "(secondary)" in the source line as the Picture line says.
6. Text added beyond the Picture lines (brief writer's, cut any the orchestrator does not want; each is one line in its brief): g-a3-2 headline "WIND TURNS COUNTERCLOCKWISE"; g-a3-3 question "WHY DID IT TURN INLAND?"; g-a3-4 chip "OMEGA BLOCK"; g-a3-5 headline "AIR FLOWS HIGH TO LOW"; g-a3-7 label "GROUND TO UPPER AIR"; g-a3-8 eyebrow "SNOW STILL FALLING" and label "WEST VIRGINIA". Readings: g-a3-2 swirl centred on the 25 Nov chart's printed low (so Pittsburgh is on the cold side as g-a3-3 needs); g-a3-10 "tilts south" = logZoom pull-out and pan, no 3D tilt.
