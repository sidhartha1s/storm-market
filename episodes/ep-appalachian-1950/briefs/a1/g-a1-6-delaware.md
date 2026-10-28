# g-a1-6-delaware: onshore wind stacks the Delaware; Philadelphia's record tide (A1-S8)
Builder: Opus 5.5, high effort. Depth: deep. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: image-in-comp push from `references/editing-patterns/ep5-terrain-map.html` (scene 1); `library/inhouse/master-map-us-canada.html` (scene 2). Prefix every id and class `dl6-`.
Sits over: nothing on the track below. The chart still is mounted INSIDE the comp (scene 1); scene 2 is a designed map. Full frame, track 2.
Asset: `media/candidates/a1/A1-S8_c1_nws-jkl-surface-1950-11-25.jpg` (1156 x 759, provenance row: NWS Jackson KY, US government work, verified Y; date from filename and listing, not printed on the chart). The orchestrator copies it to `media/a1/` before dispatch; mount only that copy. Backup `A1-S8_c2_...12z.png` only if the verifier fails c1. Never c3 (26 Nov).

## 0. Claim
Onshore wind off the ocean stacked water up the Delaware River: Philadelphia's tide gage reached a record 10.8 ft (severe flooding starts at 10.2 ft), and down on Delaware Bay in New Jersey the tide set a record too.

## 1. Source
- `research/nws-facts.md` §1 NCEI (P): "onshore winds along the coast caused extreme high tides and flooding in New Jersey and Connecticut".
- §1 PHI (P): Philadelphia "tide rose to a record 10.8 feet" above MLLW, severe flooding begins 10.2 ft.
- §1 PHI (P): Greenwich Piers 8.8 ft above mean sea level, highest of record to then (spoken only as "set a record too"; no number on screen).
- Chart: `research/maps-forecast.md` §1 item 1; `media/candidates/a1/provenance.csv` row c1. Source line "Source: NWS Jackson KY, surface chart, 25 Nov 1950", then "Source: NWS Mount Holly".

## 2. Datum, scale, orientation
- Scene 1 (0 to 5.9 s): chart image px. Measured on the 1156 x 759 image (builder re-measures and states its numbers): New Jersey coast about (905, 300), mouth of Delaware Bay about (885, 345), Atlantic east of it; a low ("L") near (840, 398). Frame 0 shows the chart scaled so the image region x 640 to 1156, y 120 to 460 fills 1920 x 1080 (scale 3.72, a 2.5x crop; the source is 1156 px wide, so expect softness: soften with a 0.3 px blur rather than sharpen). Push: scale 3.72 to 4.4 toward (900, 320) by `logZoom` over 5.5 s. At the end the low is at the left edge or out of frame; the comp never labels it, rings it or draws from it (L1 stays closed; orchestrator open item 1).
- Scene 2 (5.9 s on): frame A1-D, s 0.13, frame top-left (79156.8, 35398.5), north up. Philadelphia (900,240), Greenwich NJ (815,649), Cape May (1029,979). Delaware River course from the Bay mouth to Philadelphia, lat/lon points to project with the formula: Cape May Point 38.93,-74.96 · Bay mouth west (Cape Henlopen) 38.80,-75.09 · Bay centre 39.20,-75.25 · Greenwich NJ shore 39.39,-75.37 · Delaware Memorial Bridge 39.69,-75.52 · Chester 39.85,-75.36 · Philadelphia 39.95,-75.14.
- Tide gauge (scene 2, Philadelphia): 0 to 12 ft over 480 px (40 px per ft); 10.2 ft line at 408 px, 10.8 ft at 432 px above the gauge floor.

## 3. Geometry (px, 1920 x 1080)
- Scene 1 arrows: 5 onshore arrows, 6 px `#7fb2e5` shafts with heads, 140 to 220 px long, starting over the ocean east and southeast of the New Jersey coast and ending at the coast; 2 of them turn up into the bay mouth and run 120 px up the bay. Positions are set on the measured coast in screen px after the crop (state them in the receipt). Each arrow draws by dash (`strokeDashoffset`), then a pulse of brightness travels along it every 1.2 s (finite repeats). Arrows start nowhere near the low.
- Scene 1 source line on a small glass strip at left 110, bottom 60 (the chart is busy under it).
- Scene 2 map: land `#0b1016`, water `#04070a`, outlines 1.5 px `rgba(255,255,255,.14)`. River/bay course drawn 4 px `#5a768f`. Tide line: a 6 px `#7fb2e5` line that grows along the course from Cape May Point to Philadelphia (dash draw), with a lighter glow 14 px wide under it.
- Philadelphia pin: 16 px dot `#f2f5f8`, ring `#7fb2e5`; label "PHILADELPHIA" Arial 700 26 px `#f2f5f8` tracking 3, left of the pin (right edge x 876, y 240).
- Gauge (glass card, left 1060, top 120, 360 x 540; ends y 660): column x 1120 to 1200, floor y 620; water fill rises to 432 px (y 188); faint line at y 212 (10.2 ft) dashed 2 px `rgba(242,245,248,.45)` with label "FLOODING STARTS 10.2 FT" Arial 700 22 px `#93a3b2` right of the column (x 1220, y 212); value chip at the water top: "10.8 FT" Arial Black 900 58 px `#f2f5f8` + "RECORD" Arial 700 26 px `#e74c3c` tracking 6, right of the column at y 150 to 200. The two text blocks are 40 px apart vertically at least (no overlap).
- Delaware Bay pin (Greenwich NJ, (815,649)): dot `#f2f5f8`; chip "RECORD TIDE" glass card left of the pin (right edge x 790, y 620 to 680), Arial Black 900 52 px. No number on it.
- Source line scene 2 "Source: NWS Mount Holly" left 110, bottom 90; "Basemap: Natural Earth" bottom 60.
- Tiers: 58 / 52 / 26 / 22 / 19.

## 4. Must be true in the picture
1. Scene 1: the arrows blow from the ocean onto the New Jersey coast and up the bay; none starts at, points to, or circles the low; no "L", front or track is added.
2. Scene 1 shows whole chart content at every frame of the push (no letterboxing; image covers the frame from 0 to 5.9 s).
3. Gauge: 10.8 ft fill is 24 px above the 10.2 ft line (0.6 ft × 40), ±3 px; the record fill is above the flooding line.
4. Philadelphia is far up the river from the sea: the tide line visibly travels the whole course (Cape May to Philadelphia, about 760 px of path) before the gauge fills.
5. "RECORD TIDE" carries no number; the 8.8 ft is not shown.
6. Nothing in x >= 1600, y >= 680 (Cape May (1029,979) is unlabelled; gauge card ends x 1420).

## 5. Panel text (exact) and cues (`audio/a1-s8.words.json`, seconds from A1-S8 start)
Text: `Source: NWS Jackson KY, surface chart, 25 Nov 1950` · `PHILADELPHIA` · `10.8 FT` · `RECORD` · `FLOODING STARTS 10.2 FT` · `RECORD TIDE` · `Source: NWS Mount Holly` · `Basemap: Natural Earth`
- 0.00: chart on at the frame-0 crop; push starts (ends 5.5 s). `/* FARTHER @0.00 */`
- 2.44 "wind": arrows draw in, staggered 0.15 s, 0.6 s each. `/* WIND @2.44 */`
- 3.36 "ocean": arrow pulses start. `/* OCEAN @3.36 */`
- 4.14 "stacked": the two bay arrows extend up the bay (0.6 s). `/* STACKED @4.14 */`
- 5.30: crossfade chart to scene 2 map (0.6 s, done 5.90). `/* AT @5.92 */`
- 6.04 "Philadelphia,": Philadelphia pin + label. `/* PHILADELPHIA @6.04 */`
- 6.94 "a long way": tide line grows Cape May to Philadelphia (1.6 s, power2.inOut). `/* LONG @7.14 */`
- 8.76 "tide": gauge card in (`fromTo` x 200 to 0, autoAlpha, 0.6 s, power3.out); water fill rises to 10.8 (counter on "10.8 FT" leaf from 0.0, power3.out, 1.0 s; land on 9.54 "10"). `/* TIDE @8.76 */ /* 10 @9.54 */`
- 11.20 "record.": "RECORD" in (stamp scale 1.15 to 1, 0.3 s). `/* RECORD @11.20 */`
- 12.40 "flooding": the 10.2 ft line and its label fade in (0.4 s). `/* FLOODING @12.40 */`
- 15.20 "Delaware Bay": Greenwich NJ pin in; tide line around it pulses. `/* DELAWARE @15.20 */`
- 17.60 "record": "RECORD TIDE" chip in. `/* RECORD @17.60 */`
- Hold to end: waterline wave in the gauge (x drift, finite repeats), pins pulse.
- Exit: last 0.6 s: gauge card and chip slide out (x 980, autoAlpha 0, power3.in). Cut to g-a1-7.
Host: data-start = A1-S8 start, duration = 18.250 + 0.40 = 18.65 s.

## Open items
1. The low on the chart (L1). 2. "Greenwich Piers" place: research says Delaware Bay, southern New Jersey; a Greenwich Point gauge also exists on the Philadelphia waterfront. Confirm before build; if it is Philadelphia, move the "RECORD TIDE" beat to a bay pin only if another bay record is sourced, else ask the writer.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line item 7: one frame of scene 1 at 4.5 s read for the arrows against the chart's coast.
