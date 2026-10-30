# g-a2-6-pittsburgh: Pittsburgh, three days of snow (A2-S6)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `library/inhouse/then-now-scale.html` (one measured column on a scale) for the stack and gauge; `library/inhouse/quote-card.html` document stock for the sheet. Prefix `p6-`.
Sits over: nothing. Full-frame designed card on track 2 (hard cut from g-a2-5), channel radial background on from frame 0.
Asset: NWS Pittsburgh `snow.pdf` (`media/candidates/a2/A2-S6_c1_nws-pbz-snow-records.pdf`, US gov work, provenance row verified). The orchestrator renders pages 1 and 3 to `media/a2/pbz-snow-p1.png` and `media/a2/pbz-snow-p3.png` (`pdftoppm -r 150 -png`) before dispatch. The builder finds the three rows by reading the PNGs (and `pdftotext -layout` for the text) and records their pixel boxes in the receipt.

## 0. Claim
In Pittsburgh 14.0 in fell on Fri 24 Nov and 10.1 in on Sat 25 Nov, and by Sun 26 Nov 22 in lay on the ground.

## 1. Source
`research/nws-facts.md` §2 PBZ "Pittsburgh daily snow | 14.0 in on 24 Nov; 10.1 in on 25 Nov" and "Pittsburgh snow depth | 22 in on 26 Nov 1950" (P, pdftotext). `factcheck/a2-r1.md` row 21 CONFIRMED; Fri/Sat/Sun from Thanksgiving Thu 23 Nov (row 4). Provenance row: "14.0 in Nov 24 1950, 10.1 in Nov 25, 22 in depth Nov 26".

## 2. Datum, scale, orientation
Shared vertical scale for the stack and the gauge: 0 in at y 880, 20 px per inch. 14.0 in = 280 px (top y 600); 10.1 in on top = 202 px (top y 398); fallen total 24.1 in. Depth 22 in = 440 px (top y 440). Tick labels every 6 in: 0, 6, 12, 18, 24 at y 880, 760, 640, 520, 400.

## 3. Geometry (px, 1920 x 1080)
- Title (title zone): eyebrow "PITTSBURGH" Arial 700 22 px `#93a3b2` tracking 6 at left 110, top 70; headline "THANKSGIVING WEEKEND, 1950" Arial Black 900 52 px `#f2f5f8` at left 110, top 104.
- Scale axis: x 300, y 400 to 880, 2 px `#4a5560`; tick labels Arial 700 22 px `#93a3b2` right-aligned at x 285 ("0 in" at the bottom, then "6", "12", "18", "24").
- Snow stack column: x 340 to 520. FRI segment `#f2f5f8` y 600 to 880; SAT segment `#dfe7ee` with a 2 px `#7fb2e5` seam at y 600, y 398 to 600. Labels right of the column at x 545, vertically centred on each segment: "FRI 24" Arial 700 22 px `#93a3b2` over "14.0 IN" Arial Black 900 52 px `#f2f5f8` (centre y 740); "SAT 25" over "10.1 IN" (centre y 499).
- Depth gauge: x 780 to 840, rounded tube, stroke 3 px `#93a3b2`, fill `#7fb2e5` at 70 % from y 880 to 440; a 2 px dashed line across both columns at y 440 (x 340 to 860). Label right of the gauge at x 865: "SUN 26" Arial 700 22 px `#93a3b2`, "22 IN" Arial Black 900 52 px `#f2f5f8`, "ON THE GROUND" Arial 700 26 px `#dfe7ee` tracking 4 (block centre y 440, right edge about 1150).
- Records sheet (behind, right): the two page crops stacked into one "sheet" card, beige `#f4f0e6` 4 px radius, left 1180, top 170, width 560, height 480 (bottom 650, right 1740: above the circle line), rotation 1.5° set at 0, opacity 0.92, shadow `0 18px 50px rgba(0,0,0,.55)`. Show only the region holding the three rows (crop by `object-position`); scale so the row text reads (about 22 px cap height). Each matched row gets a highlight box: 3 px `#d8a13a` stroke, `rgba(216,161,58,.18)` fill, drawn by `scaleX` 0 to 1 left to right (0.5 s). Rows: "14.0" Nov 24 1950 (daily list), "10.1" Nov 25 1950 (daily list), "22" Nov 26 1950 (greatest depths list). If the two lists sit on different pages, show page 1's crop first and slide page 3's crop up over it at the "Sunday" cue.
- Source line "Source: NWS Pittsburgh" Arial 700 19 px `#c8d3e0`, left 110, bottom 60.
- Tiers: 52 / 26 / 22 / 19.

## 4. Must be true in the picture
1. Segment heights 280 and 202 px, gauge 440 px, ±3 px: the 22 in depth is LOWER than the 24.1 in stacked top (snow settles; never draw them equal).
2. The stack grows bottom-up in time order, FRI first; nothing before its word.
3. The highlighted rows are the real rows on the NWS sheet (receipt names their text), never a retyped table.
4. No "27.4" or "30.5" total on screen (the storm total is not this beat; intro spent 27.4).
5. Nothing in x >= 1600, y >= 680.

## 5. Panel text (exact) and cues (`audio/a2-s6.words.json`, seconds from A2-S6 start)
Text: `PITTSBURGH` · `THANKSGIVING WEEKEND, 1950` · `0 in` `6` `12` `18` `24` · `FRI 24` · `14.0 IN` · `SAT 25` · `10.1 IN` · `SUN 26` · `22 IN` · `ON THE GROUND` · `Source: NWS Pittsburgh`
- 0.00 "If": axis and empty column outline on; sheet card already on at 40 % opacity, out of focus (blur 6 px). `/* IF @0.00 */`
- 4.12 "Pittsburgh,": eyebrow + headline in (y 24 to 0, autoAlpha, 0.4 s); sheet to 92 %, blur to 0 (0.6 s). `/* PITTSBURGH @4.12 */`
- 5.12 "14": FRI segment fills (`scaleY` 0 to 1, origin bottom, 0.7 s, power3.out); label pair in; row 1 highlight draws. `/* 14 @5.12 */`
- 8.64 "10": SAT segment stacks on (`scaleY` 0 to 1, origin bottom, 0.6 s); label pair; row 2 highlight. `/* 10 @8.64 (.1 @8.96) */`
- 11.04 "Sunday,": gauge tube draws, dashed line draws left to right (0.5 s). `/* SUNDAY @11.04 */`
- 11.74 "22": gauge fills to 440 (0.8 s, power3.out); "SUN 26" / "22 IN" / "ON THE GROUND" in; row 3 highlight. `/* 22 @11.74 */`
- 12.90 to exit: a few flakes settle on the stack top (12 flakes, 40 px/s, finite repeats).
- Exit: the comp hands off to g-a2-7, which opens on the NCEI map: crossfade the whole card to `#04070c` over the last 0.6 s (fade-through allowed for a full-frame scene).
Host: data-start = A2-S6 start, duration = 13.16 + 0.40 = 13.56 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
