# g-a4-3-toll: "at least 160 lives lost" (A4-S7)
Builder: Sonnet 5.5, high effort. Depth: standard (counter, calendar strip, dim map ground). Read `references/mg-quickref.md`, `learnings/mg.md`, `briefs/a4/_list.md`, then this brief.
Start from: `library/inhouse/numbers-rollup.html` (counter pattern: a leaf span written from an onUpdate count-up). Ground: copy the basemap SVG and camera transform from `compositions/g-a4-2-southmap.html` at frame P0 (or from `library/inhouse/master-map-us-canada.html` set to P0: s 0.012, top-left (-15129.9, 11692.7)); no pins, no labels, no camera moves beyond §5. File `compositions/g-a4-3-toll.html`, prefix `a43-`.
Sits over: nothing. Full-frame designed scene on track 2 (it follows Paul's full-frame clip 5). Corner circle on: keep x ≥ 1600, y ≥ 680 empty of text and shapes.

## 0. Claim
By the time the storm wound down at the end of November, at least 160 people had lost their lives.

## 1. Source
`research/nws-facts.md` §5 JKL "By the time the storm wound down on November 29th and 30th, 160 people were dead"; NCEI "it contributed to at least 160 deaths". `factcheck/a4-r1.md` row 20. The storm span shown (NOV 24 to NOV 30) = the act's dates: Chicago record 24 Nov (§3 JKL), wound down 29 to 30 Nov (§5 JKL). The state-count "close to twice that" (row 21) gets no figure on screen (Picture line; g-a4-4 carries state counts).

## 2. Datum, scale, orientation
Text card on a dim map ground. Text-safe 96 / 54 px. Centre column x 960.

## 3. Geometry (px, 1920 x 1080)
- Ground: canvas radial gradient (tokens.md). Over it the P0 basemap with every land state filled `#5a768f` at 0.38 (the drained map). Its opacity: 0.55 at frame 0, fades to 0.14 over 0.00 to 1.00 s ("the map fades to a plain dark field"), then holds at 0.14 while slowly pushing 1.00 to 1.03 scale (ease none, centre 960, 540, for the whole comp, so the field never sits still). No labels on it.
- Calendar strip: 7 cells, each 112 x 64 px, gap 12, total 856 px, x 532 to 1388, top y 250. Cell outline 2 px `#2a3644`, radius 8, fill none. Only the end cells carry text: "NOV 24" in the first cell and "NOV 30" in the last, Arial 700 22 px `#dfe7ee` tracking 2, centred. Each cell fills `#5a768f` at 0.7 left to right in turn (scaleX 0 to 1, transformOrigin left center, 0.16 s each) on the cues in §5.
- "AT LEAST": Arial 700 30 px `#93a3b2` tracking 6, centred, baseline y 400.
- Counter "160": Arial Black 900 200 px `#f2f5f8`, centred, block y 420 to 620. Tabular figures; the leaf span is the only node written by the count-up.
- "LIVES LOST": Arial Black 900 52 px `#f2f5f8`, centred, block y 640 to 700.
- Source line: "Source: NOAA NCEI, NWS Jackson, KY" Arial 700 20 px `#c8d3e0` tracking 1, centred, baseline y 780.
- A thin rule 2 px `#c0392b` (danger red 1), 360 px wide, centred at y 720, drawn left to right with "LIVES LOST" (scaleX 0 to 1, 0.5 s).
- Glass card behind the text block (tokens.md glass values, radius 28): x 520 to 1400, y 340 to 810, fades in with "AT LEAST". It keeps the type off the map texture.
- Three tiers: 200/52 big, 30 mid, 22/20 small.

## 4. Must be true in the picture
1. The counter never shows a value before the word "160" (2.74): it opens on its first tick at 2.74 (value 1 or more, not 0 sitting earlier) and lands on exactly 160, never overshooting.
2. "160" appears once; no other figure on screen (no 300, no 383, no ×2).
3. The calendar shows only "NOV 24" and "NOV 30" as text; it is filled before the counter starts.
4. No black empty frame: the dim map ground is visible and moving from frame 0 to the end.
5. Nothing in x ≥ 1600, y ≥ 680.

## 5. Panel text (exact) and cues
Text: `NOV 24` · `NOV 30` · `AT LEAST` · `160` · `LIVES LOST` · `Source: NOAA NCEI, NWS Jackson, KY`
Cues from `audio/a4-s7.words.json` (seconds from the segment start = comp time; host starts with the segment):
- 0.00 "By": map ground fading 0.55 to 0.14 (1.0 s, power1.out); calendar outlines in (autoAlpha, 0.3 s). `/* BY THE TIME @0.00 */`
- 0.56 "wound": cells fill one by one, 24 to 30, 0.16 s each, 0.19 s apart (0.56 to 1.88). `/* WOUND DOWN @0.56 */`
- 1.32 "end": "NOV 30" cell text brightens `#dfe7ee` to `#f2f5f8` and the cell gets a 2 px `#7fb2e5` outline. `/* END OF THAT MONTH @1.32 */`
- 2.52 "at least": glass card and "AT LEAST" in (`fromTo` y 20 to 0, autoAlpha, 0.4 s, power3.out); calendar dims to 0.5. `/* AT LEAST @2.52 */`
- 2.74 "160": counter in and counting 1 to 160 (power3.out, 0.75 s, fast then slow), lands 3.49. `/* 160 @2.74 */`
- 4.56 "lives.": "LIVES LOST" in (`fromTo` y 16 to 0, autoAlpha, 0.4 s, power3.out), red rule draws; source line in at 4.90. `/* LIVES @4.56 */`
- 5.20 to end: text block floats y 0 to -6 px (sine.inOut, yoyo, finite repeats); map push continues.
- Exit: text block and calendar slide up and out (`to` y -40, autoAlpha 0, 0.6 s, power3.in) in the host's last 0.6 s; the ground holds to the cut (g-a4-4 follows).
Host: data-start = A4-S7 audio start, duration = 8.704 + 0.40 = 9.104 s (assumed gap).

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line item 4: capture 2.74 and 3.49 twice each (fresh forward and seek-back) and confirm both show the same counter value.
