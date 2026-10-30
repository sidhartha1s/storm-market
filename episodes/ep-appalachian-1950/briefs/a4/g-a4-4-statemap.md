# g-a4-4-statemap: where the losses fell (A4-S8, A4-S9)
Builder: Opus 5.5, high effort. Depth: deep (state choropleth, staged reveals, a pan south). Read `references/mg-quickref.md`, `learnings/mg.md`, `briefs/a4/_list.md`, then this brief.
Start from: `library/inhouse/master-map-us-canada.html` (its admin-1 state paths, projection and camera group). Copy to `compositions/g-a4-4-statemap.html`, prefix `a44-`; delete the Enderlin layers, rail cards and labels. The catalog block `us-map` is the reference for staggered state fills only (do not use its projection: this comp keeps the episode projection so the states line up with every other A4 map).
Sits over: nothing. Full-frame designed map on track 2. Corner circle on: nothing but basemap at x ≥ 1600, y ≥ 680.

## 0. Claim
The state-by-state counts put the heaviest losses in Ohio (64 to 70); West Virginia lost as many as 18, Kentucky as many as 17, and Alabama, far south of the snow, 13. These are secondary tallies and the picture says so.

## 1. Source (quoted, with rows)
- State tallies: `research/nws-facts.md` §5 "State deaths (summary) | OH 64-70, PA 36-40, NY 36, NJ 34, MI 16-22, IN 18, WV 18, KY 17, AL 13" from https://usdeadlyevents.com/?p=3507 (SECONDARY). `factcheck/a4-r1.md` rows 24, 25 (Ohio 70 Schmidlin and Schmidlin 1996; 64 AP Logan Daily News 29 Nov 1950), 26 (WV 18 = AP 30 Nov high; KY 17 = AP 29 Nov; hence "as many as"), 29 (AL 13, AP 27 and 29 Nov; UP 14).
- Callbacks with no figure on screen: Columbus noon 10°F (§3 ILN, a4-r1 row 28, spent in A2-S1); Newark 108 mph (spent in the hook). West Virginia deepest snow: §2 Coburn Creek 62 in (row 27), no figure on screen.

## 2. Datum, scale, orientation
North up. Projection: `_list.md`. Frames:
- Q1: s 0.02, top-left (17991.0, 13696.7). Columbus (760,470), Newark (1438,383), Pittsburgh (991,416), Buffalo (1077,143). State centres OH (775,432), WV (944,622), KY (583,745), PA (1159,365), NY (1336,142), NJ (1405,443), IN (506,477), MI (629,64).
- Q2: s 0.02, top-left (17991.0, 35196.7): Q1 moved 430 px up. AL centre (468,840), GA (729,851), Birmingham (467,760), KY (583,315), WV (944,192).
- Q1 to Q2 is a pan at the same scale (translate only, power2.inOut).

## 3. Geometry (px)
- Basemap as the exemplar (fills `#0b1016` to `#15202b`, lines `#2a3644` 1.2 px non-scaling, coast `#4a5560`).
- Toll shading (crimson `#8e2020`, opacity = 0.15 + 0.8 × high tally / 70, computed by script and listed in the receipt): OH 70 → 0.95; PA 40 → 0.61; MI 22 → 0.40; IN 18 → 0.36; WV 18 → 0.36; KY 17 → 0.34; AL 13 → 0.30. The high end of each range is used; no legend (narration carries the numbers, chips carry the voiced ones).
- New York and New Jersey: NOT shaded. Outlined 3 px `#7fb2e5` (wind blue, their Act 1 colour), no fill.
- Every other state: basemap only.
- Ohio snow (S8 "cold and deep snow"): snow dots 2 to 3 px `#dfe7ee` at 0.7, clipped to Ohio, falling 30 to 50 px/s, from its cue to the end of S8.
- West Virginia snow cue: a white wash `#f2f5f8` at 0.25 over WV, in and out 0.6 s (one breath, "deepest snow").
- Callback points (no numbers): Columbus dot 12 px `#7fb2e5` with label "COLUMBUS" right of it (left edge 784, centred y 470); Newark pin 16 px `#7fb2e5`, label "NEWARK" left of it (right edge 1414, centred y 383) so it stays clear of the corner and the NJ outline label space.
- Chips (glass, tokens.md values, radius 14, padding 10 x 18):
  - Ohio: box x 600 to 960, y 196 to 296 (over Lake Erie; covers part of southern Michigan, which is allowed). Line 1 "OHIO" Arial Black 900 40 px `#f2f5f8`; line 2 to its right, same baseline: "64 TO 70" Arial Black 900 52 px `#e74c3c` (danger red 2), built in two parts "64" and "TO 70".
  - West Virginia: box left 1010, top 600, right ≤ 1400: "WEST VIRGINIA" Arial 700 26 px `#dfe7ee`; "UP TO 18" Arial Black 900 40 px `#e74c3c` under it.
  - Kentucky: box left 300, top 860, right ≤ 640, bottom ≤ 1000: "KENTUCKY" Arial 700 26 px `#dfe7ee`; "UP TO 17" Arial Black 900 40 px `#e74c3c` under it.
  - Alabama (Q2): box left 560, top 790, right ≤ 900: "ALABAMA" Arial 700 26 px `#dfe7ee`; "13" Arial Black 900 52 px `#e74c3c` to its right.
- Source line "Source: state tallies, usdeadlyevents.com (secondary)" Arial 700 20 px `#c8d3e0` (left 110, bottom 92); basemap credit (left 110, bottom 60). Both on from frame 0.
- Scan line as g-a4-1 for the whole comp.
- Type tiers: 52 big, 40/26 mid, 22/20/19 small.

## 4. Must be true in the picture
1. Ohio is the deepest shade on screen in every frame; no state shown deeper.
2. New York and New Jersey are outlined, never filled.
3. Each chip value appears on its word, never before: "64" at 4.02, "TO 70" at 5.08, "UP TO 18" at 18.66, "UP TO 17" at 20.80 (S8); "13" at 6.72 (S9). Columbus and Newark show no number.
4. One reading target: when a new chip lands the previous chip dims to 0.45; at most one chip at full opacity.
5. States sit in true positions (shared projection); Alabama is fully on screen and under its chip only in Q2.
6. No house-fire or cause chip anywhere (Picture line; the fire sentence covers the whole storm, a4-r1 row 30).
7. The word "(secondary)" stays in the source line for the whole comp.
8. Corner x ≥ 1600, y ≥ 680 holds only basemap.

## 5. Panel text (exact) and cues
Text: `OHIO` · `64` · `TO 70` · `COLUMBUS` · `NEWARK` · `WEST VIRGINIA` · `UP TO 18` · `KENTUCKY` · `UP TO 17` · `ALABAMA` · `13` · `Source: state tallies, usdeadlyevents.com (secondary)` · `Basemap: Natural Earth`

Segment offsets (0.40 s gaps assumed): `SEG = { a4s8: 0.000, a4s9: 21.929 }` ; lengths 21.529, 15.308 s.

Cues (from `audio/a4-s8.words.json`, `a4-s9.words.json`; comp time = SEG + t):
- S8 0.00 "Those": frame Q1, basemap on, NY and NJ outlines draw (stroke-dashoffset, 0.6 s). `/* THOSE STATE COUNTS @0.00 */`
- S8 0.24 "state": shaded states fill in (opacity 0 to their value, 0.4 s each, staggered 0.12 s: PA, MI, IN, WV, KY), Ohio held empty. `/* STATE @0.24 */`
- S8 2.30 "Ohio,": Ohio fills to 0.95 with a fill sweep west to east (0.6 s); chip box and "OHIO" in. `/* OHIO @2.30 */`
- S8 4.02 "64": "64" in (`fromTo` autoAlpha 0, y 14 to 0, 0.35 s, power3.out). `/* 64 @4.02 */`
- S8 5.08 "70": "TO 70" in. `/* 70 @5.08 */`
- S8 7.86 "deep": Ohio snow starts. `/* DEEP SNOW @7.86 */`
- S8 9.18 "Columbus": Columbus dot and label in; Ohio chip dims to 0.45. `/* COLUMBUS @9.18 */`
- S8 12.76 "Newark": Newark pin and label in, one pulse ring 30 to 70 px; Columbus label out. `/* NEWARK @12.76 */`
- S8 14.94 "West Virginia,": WV fill brightens (0.36 to 0.5, 0.4 s), WV chip box and "WEST VIRGINIA" in; Newark label out. `/* WEST VIRGINIA @14.94 */`
- S8 16.34 "deepest": WV white wash breath. `/* DEEPEST SNOW @16.34 */`
- S8 18.66 "18.": "UP TO 18" in. `/* 18 @18.66 */`
- S8 19.86 "Kentucky": KY fill brightens, KY chip and "KENTUCKY" in; WV chip dims. `/* KENTUCKY @19.86 */`
- S8 20.80 "17.": "UP TO 17" in. `/* 17 @20.80 */`
- S8 21.40 to S9 0.00: every chip out (0.4 s, power3.in); Ohio snow stops; Columbus dot and Newark pin out.
- S9 0.00 "The cold side": pan Q1 to Q2 (1.6 s, power2.inOut). `/* COLD SIDE @0.00 */`
- S9 3.30 "Alabama,": Alabama fills to 0.30 (sweep north to south 0.6 s); chip box and "ALABAMA" in. `/* ALABAMA @3.30 */`
- S9 5.32 "heaviest snow": WV (at the top of Q2) white wash breath, so "south of the heaviest snow" has its two ends on screen. `/* HEAVIEST SNOW @5.32 */`
- S9 6.72 "13": "13" in. `/* 13 @6.72 */`
- S9 9.54 to end: hold; slow 3 % push toward Alabama (centre 468, 840; ease none) and the scan line.
- Exit: the chip slides out (`to` x -60, autoAlpha 0, 0.6 s, power3.in) in the host's last 0.6 s; the map holds to the cut to g-a4-5.
Host: data-start = A4-S8 audio start, duration = SEG.a4s9 + 15.308 + 0.40 = 37.637 s (assumed gaps).

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line item 6: the shading opacities and chip anchors computed by script from the tally table above, printed in the receipt. Report any §4 vs §3 conflict instead of choosing.
