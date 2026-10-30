# g-a2-8-wv: West Virginia totals and Coburn Creek's 62 inches (A2-S8)
Builder: Opus 5.5, high effort. Depth: deep. Read `references/mg-quickref.md`, `learnings/mg.md`, `briefs/a2/_list.md` and `briefs/a2/g-a2-7-band.md` (the band you inherit) first.
Start from: the g-a2-7 basemap/camera code (same projection, same band polygon vertices from g-a2-7's receipt); `library/inhouse/then-now-scale.html` for the height ruler. Prefix `w8-`.
Sits over: nothing. Full-frame designed map on track 2, frame 0 identical to g-a2-7's last frame (A2-B, band, Erie/Youngstown/Pittsburgh dots).

OPEN ITEM (orchestrator, before dispatch): Coburn Creek's location. No research row gives it, and a 28 Oct 26 search found no GNIS feature of that exact name ("Cobun Creek" at Morgantown 39.611, -79.971 and "Coburn" in Wetzel County 39.593, -80.503 are other places, neither "in the mountains"). Build branch A (no Coburn pin) unless the orchestrator writes a confirmed lat/lon with its source into this brief; then branch B adds the pin.

## 0. Claim
In West Virginia Elkins (34.7 in) and Parkersburg (34.6 in) both passed 34 in, Clarksburg (33.0 in) got 24 in in a single day, and Coburn Creek reported 62 in, more than five feet, the most anywhere in the storm.

## 1. Source
`research/nws-facts.md` §2 RLX "Elkins WV / Parkersburg / Clarksburg | 34.7 / 34.6 / 33.0 in" (P), "Clarksburg WV 25 Nov | 24 in, its highest daily total on record" (P), "Greatest storm total, Coburn Creek WV | 62 in" (JKL, RLX, NCEI, RSI; P). `factcheck/a2-r1.md` rows 26, 27, 28 CONFIRMED; row 28: 62 in = 5 ft 2 in, the silhouette scale is correct.

## 2. Datum, scale, orientation
- Frame A2-B (open): s 0.032, top-left (39400.2, 20769.2).
- Frame A2-W (zoom target): s 0.075, top-left (54186.2, 35931.1): Parkersburg (549, 386), Clarksburg (900, 380), Elkins (1043, 528), Charleston (529, 770). Zoom ratio 2.34: `logZoom`.
- Height ruler: 0 in at y 640, 6.0 px per inch: 62 in = 372 px (top y 268); 5 ft 2 in silhouette = 62 in = same 372 px. Ruler ticks every 12 in (1 ft): y 640, 568, 496, 424, 352, 280; labels "1 FT" to "5 FT" at the 12/24/36/48/60 in ticks.
- Branch B pin: px = (map unit - (54186.2, 35931.1)) × 0.075 from the confirmed lat/lon; it must land at x < 1180 (left of the ruler panel) and outside y >= 680 when x >= 1600. If it lands off-frame or under the panel, report and stay on branch A.

## 3. Geometry (px, 1920 x 1080)
- Map layer: band (g-a2-7 polygon) stays on, fill eased to `rgba(242,245,248,.55)` after the zoom so pins read on it.
- City pins at A2-W: 14 px white dots with a `#7fb2e5` ring. Labels on fixed HUD glass pills (`rgba(10,16,24,.55)`, radius 14, padding 8 x 14) so they read over the white band:
  - Parkersburg pill LEFT of its pin (right edge at x 524, centre y 386): "PARKERSBURG" Arial 700 22 px `#93a3b2` tracking 3 / "34.6 IN" Arial Black 900 52 px `#f2f5f8`.
  - Clarksburg pill ABOVE its pin (centre x 900, bottom at y 355): "CLARKSBURG" 22 px / "33.0 IN" 52 px; then a second line added at its cue "24 IN IN ONE DAY" Arial 700 26 px `#d8a13a` (the pill grows; keep its top >= 120).
  - Elkins pill RIGHT of its pin (left edge x 1068, centre y 528): "ELKINS" 22 px / "34.7 IN" 52 px. Right edge must stay < 1230 (ruler panel starts at 1250).
  (edit_script chips "ELKINS 34.7", "PARKERSBURG 34.6", "CLARKSBURG 33.0 · 24 IN IN ONE DAY" set as name + value + unit; same figures.)
- Ruler panel (RHS, fixed HUD): dark panel x 1250 to 1820, y 110 to 670, `rgba(6,9,13,.88)`, radius 18. Heading "COBURN CREEK, WV" Arial Black 900 40 px `#f2f5f8` at left 1290, top 126 (bottom about 166). Ruler: vertical 4 px `#93a3b2` line at x 1330 from y 640 to 268, 20 px ticks to its right, labels Arial 700 22 px `#93a3b2` at x 1360 ("1 FT" ... "5 FT", right edge about 1420). Snow column x 1440 to 1540, fill `#f2f5f8`, `scaleY` origin bottom, to 372 px. Silhouette x 1600 to 1700 (allowed: it spans y 268 to 640, above the circle line y 680): plain standing person outline (SVG path, 1 px stroke `#93a3b2`, fill `rgba(147,163,178,.25)`), head top exactly at y 268, feet at y 640; label "5 FT 2 IN" Arial 700 22 px `#93a3b2` centred under the feet, top y 646 (bottom about 670, inside the panel and above y 680).
  - Value "62 IN" Arial Black 900 84 px `#f2f5f8` above the column top (left 1440, top 176, bottom about 262), the brightest element on screen; sub "MOST ANYWHERE IN THE STORM" is NOT on screen (voice only; edit_script chip is "COBURN CREEK, WV · 62 IN").
- Branch B only: Coburn Creek pin 20 px, `#ffffff` with a white glow (`drop-shadow(0 0 12px #fff)`), label "COBURN CREEK" on a pill; it turns brightest white on "Coburn".
- Source line "Source: NWS Charleston WV; NOAA NCEI" Arial 700 19 px `#c8d3e0`, left 110, bottom 90; "Basemap: Natural Earth" left 110, bottom 60.
- Tiers: 84 / 52 / 40 / 26 / 22 / 19.

## 4. Must be true in the picture
1. Pins at the A2-W px ±10 (formula). Elkins is south-east of Clarksburg, Parkersburg west of Clarksburg at nearly the same latitude.
2. Snow column and silhouette are the same height (372 px ±2): 62 in = 5 ft 2 in. The "5 FT" tick sits 12 px below the column top (60 in vs 62 in).
3. Labels name the thing beside them; no pill covers another pin or another pill.
4. Branch A: no pin, no arrow, no "here" marker for Coburn Creek on the map; the place is named only in the panel heading.
5. Nothing on the coast side; nothing in x >= 1600, y >= 680.
6. Last frame = A2-W with band and the three city pins (dots only, pills and panel gone): g-a2-9 opens on it.

## 5. Panel text (exact) and cues (`audio/a2-s8.words.json`, seconds from A2-S8 start)
Text: `PARKERSBURG` · `34.6 IN` · `CLARKSBURG` · `33.0 IN` · `24 IN IN ONE DAY` · `ELKINS` · `34.7 IN` · `COBURN CREEK, WV` · `1 FT` `2 FT` `3 FT` `4 FT` `5 FT` · `62 IN` · `5 FT 2 IN` · `Source: NWS Charleston WV; NOAA NCEI` · `Basemap: Natural Earth` (branch B adds `COBURN CREEK`)
- 0.00 "West": frame A2-B as g-a2-7 left it; zoom A2-B to A2-W starts (`logZoom`, 1.1 s, expo.inOut), band fill eases to .55. `/* WEST @0.00 */`
- 1.20 "Elkins": Clarksburg/Elkins/Parkersburg pins pop (stagger 0.1 s); Elkins pill in. `/* ELKINS @1.20 */`
- 1.62 "Parkersburg": Parkersburg pill in. `/* PARKERSBURG @1.62 */`
- 2.84 "34": both 34.x values pulse once (scale 1.08, 0.3 s yoyo). `/* 34 @2.84 */`
- 4.36 "Clarksburg": Clarksburg pill in with "33.0 IN". `/* CLARKSBURG @4.36 */`
- 5.04 "24": line "24 IN IN ONE DAY" in (y 16 to 0, autoAlpha, 0.35 s). `/* 24 @5.04 */`
- 7.02 "Then": the three pills dim to 45 %; ruler panel slides in (`fromTo` x 660 to 0, 0.7 s, power3.out) with heading on "Coburn" 7.50. `/* COBURN @7.50 */` (branch B: Coburn pin flares white on 7.50.)
- 8.76 "mountains.": ruler line and ticks draw bottom-up (0.6 s); silhouette fades in (0.5 s).
- 10.14 "62": snow column fills to 372 px (0.9 s, power3.out), "62 IN" in on landing; sound hit sits here (Picture line). `/* 62 @10.14 */`
- 11.78 "five": "5 FT" tick and label flash `#f2f5f8` (0.4 s yoyo). `/* FIVE @11.78 */`
- 12.02 to 14.00: column top glints (light sweep across it, 1.2 s), flakes keep falling on the map.
- Exit to handoff: from 13.90 the panel slides out (`to` x 980, autoAlpha 0, 0.6 s, power3.in), pills fade (0.4 s), leaving the bare A2-W state of §4.6.
Host: data-start = A2-S8 start, duration = 14.30 + 0.40 = 14.70 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Receipt states the branch built (A or B) and, for B, the coordinate source.
