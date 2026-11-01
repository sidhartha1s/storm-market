# g-a2-9-south: south into Charleston and eastern Kentucky, snow for about a week (A2-S9)
Builder: Opus 5.5, high effort. Depth: deep. Read `references/mg-quickref.md`, `learnings/mg.md`, `briefs/a2/_list.md`, `briefs/a2/g-a2-8-wv.md` first.
Start from: the g-a2-7/-8 basemap and camera code (same projection, same band); counter from `library/inhouse/numbers-rollup.html`. Prefix `s9-`.
Sits over: nothing. Full-frame designed map on track 2; frame 0 identical to g-a2-8's last frame (A2-W, band, three WV city dots).
Map choice: the Picture line says "the NCEI snowfall map again"; the A2 maps stay on the channel basemap so every pin is computed, and the NCEI plate already shown in g-a2-7 is not repeated. The JKL snow map is not used: its printed labels (Charleston 26, Huntington 21) disagree with the chips' 25.7 and 20.9.

## 0. Claim
The snow reached far south: Charleston WV over 25 in (25.7), Huntington 20.9, eastern Kentucky a foot or more (Paintsville 14, Hazard 13), and in parts of the region snow kept falling for about a week (22 to 30 Nov).

## 1. Source
`research/nws-facts.md` §2 RLX "Charleston WV / Huntington WV | 25.7 / 20.9 in" (P); JKL "Paintsville recorded 14", Hazard and Manchester 13"" (P); NCEI/RLX "Several locations received more than 50 inches" (voice only); "Duration | snow fell about a week; storm 22-30 Nov (NCEI)" (P). `factcheck/a2-r1.md` rows 29 to 32 (row 32: RLX "The snow fell for a week straight", NCEI 22 to 30 Nov).

## 2. Datum, scale, orientation
- Frame A2-W (open): s 0.075, top-left (54186.2, 35931.1).
- Frame A2-S (target): s 0.042, top-left (37429.1, 35005.9): Charleston (1000, 470), Huntington (869, 454), Paintsville (811, 596), Hazard (748, 728), Elkins (1288, 335). Move: `logZoom` 0.075 to 0.042 (ratio 1.79) with the pan, then a slow drift south (top-left y +600 map units = 25 px at s 0.042) through the rest.
- Day counter scale: 9 day ticks NOV 22 to NOV 30 across 450 px (56.25 px per day).
- Kentucky/West Virginia state line drawn from the basemap (it is the Big Sandy / Tug Fork): the Kentucky pins sit west of it.

## 3. Geometry (px, 1920 x 1080)
- Band (from g-a2-7) stays on at `rgba(242,245,248,.55)`; Elkins/Clarksburg/Parkersburg dots fade to 0 during the zoom (Elkins would sit at (1288, 335), under the chip card).
- Pins (A2-S, 14 px white dots, `#7fb2e5` ring) with glass pills (`rgba(10,16,24,.55)`, radius 14, padding 8 x 14), name Arial 700 22 px `#93a3b2` tracking 3 over value Arial Black 900 52 px `#f2f5f8`:
  - Charleston pill RIGHT (left edge x 1025, centre y 470): "CHARLESTON, WV" / "25.7 IN".
  - Huntington pill LEFT (right edge x 844, centre y 430; lifted 24 px so it clears Charleston's dot 131 px east): "HUNTINGTON, WV" / "20.9 IN".
  - Paintsville pill LEFT (right edge x 786, centre y 596): "PAINTSVILLE, KY" / "14 IN".
  - Hazard pill LEFT (right edge x 723, centre y 728): "HAZARD, KY" / "13 IN".
  (edit_script pins "CHARLESTON, WV 25.7", "HUNTINGTON, WV 20.9", "PAINTSVILLE 14", "HAZARD 13": same figures with the unit; state added for the two Kentucky towns since the camera just left West Virginia.)
- Day counter (top-right HUD, clear of the circle corner): glass card left 1290, top 110, width 520, height 190. Label "SNOW FALLING" Arial 700 22 px `#93a3b2` tracking 6; date readout "NOV 22" Arial Black 900 52 px `#f2f5f8` (leaf span, written by an onUpdate counter over the day index, never in onStart/tl.call); a 450 px track below (x 1325 to 1775, y 260) with 9 ticks; a `#7fb2e5` fill `scaleX` 0 to 1 (origin left) as days advance.
- Chip "SNOW FOR ABOUT A WEEK" Arial Black 900 40 px `#f2f5f8` on a glass card at left 1290, top 320 (bottom about 400), under the counter.
- Source line "Source: NWS Charleston WV; NWS Jackson KY; NOAA NCEI" Arial 700 19 px `#c8d3e0`, left 110, bottom 90; "Basemap: Natural Earth" left 110, bottom 60.
- Tiers: 52 / 40 / 22 / 19.

## 4. Must be true in the picture
1. Pins at A2-S px ±10 after the zoom (the slow drift moves all pins together by the same 25 px: assert relative positions, not absolute, after 4 s).
2. Paintsville and Hazard sit in Kentucky (west of the state line); Charleston and Huntington in West Virginia.
3. The counter ends on NOV 30 exactly when the chip lands; it never shows a date outside 22 to 30 Nov.
4. No "50 IN" anywhere (spoken "several spots passed fifty" names no place; one number per frame).
5. No pill over another pin or pill; nothing in x >= 1600, y >= 680 (Hazard pill and source lines are all x < 1600).
6. Last frame: A2-S settled state with band, four pins, pills, counter and chip on (g-a2-10 is a hard cut to the NCEI map).

## 5. Panel text (exact) and cues (`audio/a2-s9.words.json`, seconds from A2-S9 start)
Text: `CHARLESTON, WV` · `25.7 IN` · `HUNTINGTON, WV` · `20.9 IN` · `PAINTSVILLE, KY` · `14 IN` · `HAZARD, KY` · `13 IN` · `SNOW FALLING` · `NOV 22` ... `NOV 30` · `SNOW FOR ABOUT A WEEK` · `Source: NWS Charleston WV; NWS Jackson KY; NOAA NCEI` · `Basemap: Natural Earth`
- 0.00 "It": A2-W as g-a2-8 left it; at 0.14 "reached" the zoom/pan to A2-S starts (`logZoom`, 1.6 s, expo.inOut, arrives 1.74). `/* REACHED @0.14 */`
- 1.74 to 15.34: slow southward drift (ease none).
- 2.58 "Charleston,": Charleston pin pops + pill in (`fromTo` y 16 to 0, autoAlpha, 0.4 s). `/* CHARLESTON @2.58 */`
- 3.30 "Virginia": Huntington pin + pill in (on screen only; the voice names Charleston). `/* VIRGINIA @3.30 */`
- 4.18 "25": Charleston value pulse (scale 1.08, 0.3 s yoyo). `/* 25 @4.18 */`
- 6.48 "Kentucky": state line glows `#93a3b2` 0.6 s. `/* KENTUCKY @6.48 */`
- 8.94 "Paintsville": Paintsville pin + pill in. `/* PAINTSVILLE @8.94 */`
- 9.60 "Hazard.": Hazard pin + pill in. `/* HAZARD @9.60 */`
- 12.86 "parts": counter card in (`fromTo` x 660 to 0, 0.7 s, power3.out), reading NOV 22. `/* PARTS @12.86 */`
- 13.68 "snow": counter runs NOV 22 to NOV 30 and the fill grows, 1.5 s, power3.out, landing at 15.18. `/* SNOW @13.68 */`
- 15.18 "week.": chip in (y 20 to 0, autoAlpha, 0.4 s). `/* WEEK @15.18 */`
- Exit: hard cut to g-a2-10 at the host end, with the land time after "week." being 0.16 + 0.40 gap: too short for a slide. Instead the chip lands at 15.18 and everything holds; the cut is the exit (full-frame MG scene may end on a cut).
Host: data-start = A2-S9 start, duration = 15.34 + 0.40 = 15.74 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
