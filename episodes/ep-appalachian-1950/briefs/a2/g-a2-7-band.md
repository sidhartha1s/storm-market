# g-a2-7-band: the 30+ inch band, Erie into West Virginia (A2-S7)
Builder: Opus 5.5, high effort. Depth: deep. Read `references/mg-quickref.md`, `learnings/mg.md` and `briefs/a2/_list.md` (frame table) first.
Start from: `library/inhouse/master-map-us-canada.html` (basemap, projection, camera rig); `logZoom` from `library/inhouse/snippets/helpers.js`. Same basemap as `g-intro-2-hookmap` / `-3` / `-5`. Prefix `b7-`.
Sits over: nothing. Full-frame designed map on track 2, ground on from frame 0 (fade-through from g-a2-6).
Assets: `media/a2/A2-S9_c2_ncei-snowfall-index-nov22-30-1950.png` (NCEI Regional Snowfall Index map, 22 to 30 Nov 1950, 1210 x 935, US gov work; provenance: "over-24 in band Erie through WV"; picks.md names it the S7 pick because the JKL map does not reach Erie).

## 0. Claim
Pittsburgh was not the deepest: over 30 in fell in a band from near Erie, Pennsylvania, south into the heart of West Virginia; Erie and Youngstown each got more than 28 in, and Youngstown's 30.6 in made November 1950 its snowiest November.

## 1. Source
`research/nws-facts.md` §2: RSI/RLX "Over 30 inches of snow was reported in a band from Erie, PA southward into the heart of West Virginia" (P); NCEI "both Erie, Pennsylvania, and Youngstown, Ohio, received more than 28 inches" (P); YNG "30.6 inches, ranked #1" monthly November (P). `factcheck/a2-r1.md` rows 23, 24, 25 CONFIRMED (YNG list updated 10/2/2026: #1 1950 30.6, #2 1971 20.1). Band shape: the NCEI PNG's dark-red (> 24 in) area, the published figure the band traces.

## 2. Datum, scale, orientation
Projection and frames from `briefs/a2/_list.md`: map x = 3841 × (lon + 97.576), map y = -5585 × (lat - 46.6213). North up.
- Frame A2-P: s 0.08, top-left (56275.2, 28019.2): Pittsburgh (900, 520), Youngstown (699, 225).
- Frame A2-B: s 0.032, top-left (39400.2, 20769.2): Erie (889, 138), Youngstown (820, 322), Pittsburgh (900, 440), Clarksburg (857, 647), Elkins (918, 711).
Band: read the outline of the NCEI dark-red (> 24 in) area against the state lines printed on the PNG (Lake Erie shore, PA-OH line, Ohio River, WV borders), write 12 to 20 lon/lat vertices, convert with the formula, and list them in the receipt. The band polygon must sit inside that published > 24 in area (it is the 30+ core, so it may be narrower, never wider). Expected extent: north tip near Erie (lat 42.1), south end in central West Virginia (lat 38.6 to 38.9), west edge near the PA-OH line / eastern Ohio, east edge west of the Allegheny Front.

## 3. Geometry (px, 1920 x 1080)
- Frame 0 = A2-P: basemap (land `#0b1016`, state lines 1.5 px `#2a3644`, Lake Erie `#0e1a26`), Pittsburgh pin white 16 px with label "PITTSBURGH" Arial 700 26 px `#f2f5f8` tracking 4, 20 px right of the pin. Light snow (40 flakes) on a layer above the map.
- Pull-back A2-P to A2-B: `logZoom` (s 0.08 to 0.032, ratio 2.5), 2.0 s, expo.inOut.
- NCEI plate (source inset, right side, fixed HUD layer, never on the moving map): framed card left 1220, top 110, width 520 (height 402; bottom 512, right 1740: clear of the circle corner), 2 px `rgba(255,255,255,.14)` border, radius 12, shadow. Caption above it "NOAA NCEI · TOTAL SNOWFALL, NOV 22-30, 1950" Arial 700 19 px `#c8d3e0` tracking 2 at left 1220, top 80. The PNG's own legend shows "Ohio Valley 34.7" (spent in A2-S11): crop the plate to image region x 300 to 1210, y 100 to 935 (the legend box at x 22 to 518, y 575 to 905 mostly drops out; any remaining legend sliver must hold no number: check the frame) and scale it to fit 520 wide.
- Band: polygon from §2, fill `rgba(242,245,248,.85)` with a 2 px `#f2f5f8` edge, revealed north to south by a mask rect sweeping from Erie's y down to the south tip (clip `scaleY` 0 to 1, origin top), so it "draws itself" from Erie.
- Pins (on the map layer at A2-B): Erie (889, 138), Youngstown (820, 322), Pittsburgh (900, 440): 14 px dots, Erie and Youngstown `#7fb2e5` ring around white. Labels (fixed HUD, enter when the camera settles): "ERIE, PA" right of Erie (x 915, y 138); "YOUNGSTOWN, OH" LEFT of Youngstown (right-aligned at x 795, y 322: west side, so it does not sit on the band); "PITTSBURGH" right of Pittsburgh (x 925, y 440). Every label is outside the band polygon or on a glass backing (`rgba(10,16,24,.55)` pill): no label over the white band without backing.
- Band chip: glass card left 980, top 560 (bottom about 660, clear of y 680), "30+ IN" Arial Black 900 58 px `#f2f5f8`, one line only (edit_script chip is "30+ IN"). A 2 px `#93a3b2` leader from the card's left edge to the band's east edge at Pittsburgh's latitude (y 470).
- Erie/Youngstown chip: glass card left 420, top 170, two lines "28+ IN" Arial Black 900 52 px `#f2f5f8` and "ERIE AND YOUNGSTOWN, EACH" Arial 700 22 px `#93a3b2` tracking 3 (one card for both: one fact, one instance). Card right edge <= 780 so it clears the band and the Youngstown label (x 795): check with the label's real width.
- Youngstown swap (same card, text-state swap): "30.6 IN" Arial Black 900 52 px and "YOUNGSTOWN · SNOWIEST NOVEMBER ON RECORD" Arial 700 22 px tracking 3 (card widens; keep right edge <= 795 or move the card to left 140).
- Source line "Source: NOAA NCEI; NWS Charleston WV" Arial 700 19 px `#c8d3e0`, left 110, bottom 90; "Basemap: Natural Earth" left 110, bottom 60.
- Tiers: 58 / 52 / 26 / 22 / 19.

## 4. Must be true in the picture
1. Pins at the A2-B px above ±10 (formula, not by eye). Erie is north of Youngstown and east of it (dx +69, dy -184 px at s 0.032).
2. The band lies inside the NCEI > 24 in area: compare the settled frame with the plate side by side; its north tip is at or just south of Erie, its south end inside West Virginia, and it never crosses into Ohio west of Youngstown's longitude by more than the published area does.
3. The band touches nothing on the coast side (no extension east of the Allegheny Front): it is a snow band, not a track (L1 open).
4. "28+ IN" appears once for both cities; "30.6 IN" is labelled as Youngstown's November total, not a storm total.
5. Plate, chips and labels never overlap one another or the band without a backing; nothing in x >= 1600, y >= 680.
6. Last frame = A2-B exactly, with band, three pins (dots only) and nothing else (g-a2-8 opens on it).

## 5. Panel text (exact) and cues (`audio/a2-s7.words.json`, seconds from A2-S7 start)
Text: `PITTSBURGH` · `NOAA NCEI · TOTAL SNOWFALL, NOV 22-30, 1950` · `30+ IN` · `ERIE, PA` · `YOUNGSTOWN, OH` · `28+ IN` · `ERIE AND YOUNGSTOWN, EACH` · `30.6 IN` · `YOUNGSTOWN · SNOWIEST NOVEMBER ON RECORD` · `Source: NOAA NCEI; NWS Charleston WV` · `Basemap: Natural Earth`
- 0.00 "Pittsburgh": frame A2-P, PIT pin + label on, flakes falling. `/* PITTSBURGH @0.00 */`
- 0.84 "deepest": PIT label out (0.3 s, before the camera moves: no text rides a move); pull-back A2-P to A2-B starts, 2.0 s, arrives 2.84. `/* DEEPEST @0.84 */`
- 2.86 "Over": NCEI plate + caption slide in (`fromTo` x 660 to 0, 0.7 s, power3.out). `/* OVER @2.86 */`
- 3.02 "30": "30+ IN" chip in (y 20 to 0, autoAlpha, 0.4 s), leader draws. `/* 30 @3.02 */`
- 4.28 "band": band reveal starts at the north tip. `/* BAND @4.28 */`
- 5.44 "Erie,": Erie pin pops (scale 0 to 1, back.out), "ERIE, PA" in. `/* ERIE @5.44 */`
- 8.02 "south": band reveal sweeps south, 1.4 s, power2.inOut, reaching the south tip at 9.40 "Virginia." `/* SOUTH @8.02 */ /* VIRGINIA @9.40 */`
- 10.54 "Erie": Erie pin pulse; 10.90 "Youngstown,": Youngstown pin + label in. `/* YOUNGSTOWN @10.90 */`
- 12.82 "28.": "28+ IN" card in (`fromTo` x -60 to 0, autoAlpha, 0.6 s). `/* 28 @12.82 */`
- 13.76 "Youngstown": Youngstown pin pulse; 15.40 "30": card text swaps to "30.6 IN" / "YOUNGSTOWN · SNOWIEST NOVEMBER ON RECORD". `/* 30.6 @15.40 */`
- 15.40 to 18.48: band edge shimmer (a 40 px light sweep travelling north to south along the band, 2.5 s, one pass), flakes keep falling.
- Exit to the handoff: from 18.40, plate + caption, both chips, labels and the leader slide/fade out (`to` x 980 / -60, autoAlpha 0, 0.5 s, power3.in), so the last frame is the bare A2-B state of §4.6. Hard cut into g-a2-8 (identical frame).
Host: data-start = A2-S7 start, duration = 18.92 + 0.40 = 19.32 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Receipt also lists the band's lon/lat vertices and the settled A2-B pin px.
