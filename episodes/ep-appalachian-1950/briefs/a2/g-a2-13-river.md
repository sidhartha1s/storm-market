# g-a2-13-river: the Ohio River rises, Pittsburgh then Cincinnati (A2-S13)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `library/inhouse/then-now-scale.html` (measured column with a threshold line). Gauges are self-drawn SVG. Prefix `v13-`.
Sits over: nothing. Full-frame designed card on track 2, channel radial background on from frame 0.

## 0. Claim
When the snow melted it ran into the rivers: the Ohio at Pittsburgh reached 28.5 ft, 4 ft over flood stage, and downstream at Cincinnati it reached 56 ft.

## 1. Source
`research/nws-facts.md` §6 NCEI "Ohio River floods (after storm) | Pittsburgh 28.5 ft (4 ft over stage); Cincinnati 56 ft" (P). `factcheck/a2-r1.md` rows 42 (NCEI: "In Pittsburgh the Ohio River reached 28.5 feet, 4 feet above flood stage." "In Cincinnati it reached 56 feet, 4 feet above flood stage."), 43 (NCEI: "fast snowmelt, which flooded several tributaries and major rivers"). Flood stages used for the red lines are derived from NCEI's sentences: Pittsburgh 28.5 - 4 = 24.5 ft, Cincinnati 56 - 4 = 52 ft (not checked against an NWS flood-stage table: factcheck "Not settled"). Only Pittsburgh's line carries a number-free "FLOOD STAGE" label; no "24.5" or "52" on screen.

## 2. Datum, scale, orientation
Two separate gauges, each on its OWN scale (river stages are local datums: never one shared axis, never compare heights across gauges).
- Pittsburgh gauge: 0 to 30 ft, 16 px per ft: 0 ft at y 880, 30 ft at y 400. Flood stage 24.5 ft at y 488; crest 28.5 ft at y 424.
- Cincinnati gauge: 0 to 60 ft, 8 px per ft: 0 ft at y 880, 60 ft at y 400. Flood stage 52 ft at y 464; crest 56 ft at y 432.

## 3. Geometry (px, 1920 x 1080)
- Title: eyebrow "OHIO RIVER · AFTER THE STORM" Arial 700 22 px `#93a3b2` tracking 6, left 110, top 70; headline "THE MELT REACHES THE RIVER" Arial Black 900 52 px `#f2f5f8`, left 110, top 104.
- Pittsburgh gauge (left): staff board x 420 to 520, y 400 to 880, `#15202b` with a 2 px `#93a3b2` edge; ft ticks every 5 ft on its left with labels "0" "5" ... "30" Arial 700 22 px `#93a3b2` at x 405 right-aligned; water body x 300 to 640 behind the staff, `rgba(90,118,143,.85)` (`#5a768f`) with a 3 px `#7fb2e5` surface line, rising by `y` translate of a full-height rect (never tween height), wavy surface (SVG path, x-offset loop 30 px/s).
- Pittsburgh flood line: 3 px `#c0392b` horizontal at y 488 from x 280 to 680, label "FLOOD STAGE" Arial 700 22 px `#e74c3c` tracking 4 at x 690, y 488.
- Pittsburgh readout right of the gauge (x 700, centred on y 424 once crested): "28.5 FT" Arial Black 900 58 px `#f2f5f8`, sub "4 FT OVER" Arial 700 26 px `#e74c3c` tracking 2 (edit_script "28.5 FT · 4 FT OVER", split). Readout block y 380 to 470: sits above the flood label (y 488): check spacing ≥ 10 px.
- Pittsburgh name under the gauge: "PITTSBURGH" Arial 700 26 px `#dfe7ee` tracking 4, centred x 470, y 910.
- Cincinnati gauge (right): same build at staff x 1180 to 1280, water x 1060 to 1400, ticks every 10 ft labels "0" ... "60" at x 1165. Flood line 3 px `#c0392b` at y 464 from x 1040 to 1420, NO text label (one "FLOOD STAGE" per frame; the line's colour carries it, `data-repeat-ok` not needed since no text repeats). Readout at x 1420? No: right of x 1420 up to 1580 is tight; place the Cincinnati readout ABOVE its gauge: "56 FT" Arial Black 900 58 px centred x 1230, top 330 (bottom about 395, just above the 60 ft top at 400). Name "CINCINNATI" under the gauge at y 910 (x 1230).
- A thin connector arrow between gauges is NOT drawn (no "flows to" line; "downstream" stays in the voice).
- Source line "Source: NOAA NCEI" Arial 700 19 px `#c8d3e0`, left 110, bottom 60.
- Tiers: 58 / 52 / 26 / 22 / 19.

## 4. Must be true in the picture
1. Pittsburgh crest at y 424 and flood line at y 488 (64 px = 4 ft at 16 px/ft) ±3 px; Cincinnati crest y 432, line y 464 (32 px = 4 ft at 8 px/ft) ±3 px.
2. The two gauges show different scales with their own tick labels; nothing invites comparing the two water heights.
3. Water only rises during the window (a rising river), never drains.
4. Nothing in x >= 1600, y >= 680 (Cincinnati water ends x 1400).

## 5. Panel text (exact) and cues (`audio/a2-s13.words.json`, seconds from A2-S13 start; Whisper wrote "then" for "Then")
Text: `OHIO RIVER · AFTER THE STORM` · `THE MELT REACHES THE RIVER` · `0` `5` `10` `15` `20` `25` `30` · `FLOOD STAGE` · `28.5 FT` · `4 FT OVER` · `PITTSBURGH` · `0` `10` `20` `30` `40` `50` `60` · `56 FT` · `CINCINNATI` · `Source: NOAA NCEI`
- 0.00 "then": ground; Pittsburgh staff + low water (at 8 ft, y 752) on, surface rippling; snow flakes melting into the water (12 flakes fall and fade at the surface). `/* THEN @0.00 */`
- 2.72 "melted,": eyebrow + headline in. `/* MELTED @2.72 */`
- 4.36 "rivers.": Pittsburgh water starts a slow rise to 20 ft (y 560), 2.6 s, ease none. `/* RIVERS @4.36 */`
- 5.42 "Pittsburgh,": "PITTSBURGH" name brightens; flood line draws left to right (`scaleX`, 0.5 s) with "FLOOD STAGE". `/* PITTSBURGH @5.42 */`
- 6.62 "rose": water rises to 28.5 ft (y 424), 1.0 s, power2.out, passing the red line. `/* ROSE @6.62 */`
- 7.12 "28": "28.5 FT" in (y 16 to 0, autoAlpha, 0.35 s). `/* 28.5 @7.12 */`
- 8.82 "4": "4 FT OVER" in; the 64 px band between line and surface flashes `rgba(231,76,60,.25)` 0.6 s. `/* 4 @8.82 */`
- 10.68 "Downstream": Cincinnati gauge slides in from the right (`fromTo` x 660 to 0, 0.7 s, power3.out) with its water at 30 ft; Pittsburgh dims to 60 %. `/* DOWNSTREAM @10.68 */`
- 11.30 "Cincinnati,": Cincinnati water rises to 56 ft (y 432), 1.0 s, power2.out; flood line draws as the water nears it. `/* CINCINNATI @11.30 */`
- 12.32 "56.": "56 FT" in. `/* 56 @12.32 */`
- Exit: the comp hands off to g-a2-14 (full map): last 0.6 s crossfade the whole card to `#04070c` (fade-through).
Host: data-start = A2-S13 start, duration = 12.72 + 0.40 = 13.12 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
