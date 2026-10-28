# g-a2-10-people: people under the snow on the NCEI map (A2-S10)
Builder: Opus 5.5, high effort. Depth: deep. Read `references/mg-quickref.md`, `learnings/mg.md` and `briefs/a2/_list.md` first.
Start from: counter from `library/inhouse/numbers-rollup.html` (count-up writing a leaf span); image-with-highlight-mask pattern from `references/editing-patterns/ep5-terrain-map.html`. Prefix `p10-`.
Sits over: nothing on the track below. Full-frame designed scene on track 2 that mounts the NCEI map inside the comp: `media/a2/A2-S9_c2_ncei-snowfall-index-nov22-30-1950.png` (NCEI Regional Snowfall Index, 22 to 30 Nov 1950, 1210 x 935, US gov work; provenance: "S7 and S10 pick"; picks.md: "red 18-24 plus dark >24 = 18 in+; the 6.1 and 1.3 million figures are not on the map"). Channel radial background around it.

## 0. Claim
By the census count NCEI's index uses (2000), more than 6.1 million people in the Ohio Valley live where at least 18 in fell; in the Northeast, 1.3 million live under 30 in or more.

## 1. Source
`research/nws-facts.md` §2 and §6 NCEI "more than 6.1 million people lived in areas that received at least 18 inches of snow" and "Over 30 inches of snow affecting 1.3 million people in the region" (P). `factcheck/a2-r1.md` rows 33, 34 CORRECTED (Ohio Valley region only; population basis is the 2000 Census per NCEI record C00465) and the apply-list NOTE: "label the chip "6.1 MILLION PEOPLE · OHIO VALLEY" and apply the contour to the Ohio Valley region only"; `grades/a2-r2.md` item 2 repeats it.
Region membership (NOT in research; orchestrator confirms on NCEI's U.S. climate regions page before dispatch): NCEI's Ohio Valley region = Ohio, West Virginia, Kentucky, Tennessee, Indiana, Illinois, Missouri; Pennsylvania and New York are in the Northeast region.

## 2. Datum, scale, orientation
Image placement (fixed, no camera move on the image beyond a 2 % push): scale 1080 / 935 = 1.1551 (image 1397.6 x 1080), left 201 px, top 0. Screen px = (201 + 1.1551 × ix, 1.1551 × iy) for image px (ix, iy). Placed so the image ends at x 1599 and the NOAA logo (image x 1030 to 1200, y 780 to 915; screen x 1391 to 1587) stays out of the circle corner. Right strip x 1599 to 1920: channel ground.
18 IN+ area = image pixels of the two top legend colours: red (18 to 24 in, about rgb(255,0,0)) and dark red (> 24 in, about rgb(115,0,0)); sample both from the legend swatches (image y about 685) before thresholding.
Ohio Valley clip: exclude everything east of the Pennsylvania-Ohio line and north of the Pennsylvania-West Virginia / Maryland line as printed on the PNG. My read of the PNG (builder measures and records the real values): PA-OH line near image x 865 from the Lake Erie shore (y about 440) to the Ohio River (y about 548); PA southern line near y 548 from x 865 east. The clip polygon follows those printed lines, not a straight guess.

## 3. Geometry (px, 1920 x 1080)
- Base: the PNG at the placement above, desaturated to 35 % (`filter: saturate(.35) brightness(.8)`) once the highlight comes up, so the lit area reads.
- Highlight layer: an SVG path (or mask image) of the 18 IN+ pixels clipped to the Ohio Valley polygon, in image px inside a `<g>` with the same transform as the image; fill `rgba(255,255,255,.0 → .55)` plus a 3 px `#f2f5f8` outline. Trace with a read-only threshold pass that prints the polygon; paste its numbers; state the point count and area (px²) in the receipt.
- Label on the lit area: "18 IN+" Arial Black 900 40 px `#f2f5f8` on a glass pill, placed inside the lit area over Ohio (screen near (1080, 640); confirm it sits on lit pixels).
- Counter card (covers the PNG's legend box, which carries the "Ohio Valley 34.7 / Category 5" table that is A2-S11's reveal): glass card, background `rgba(10,16,24,.82)` (opaque enough to hide the legend), left 210, top 640, width 620, height 380 (bottom 1020). Contents: eyebrow "OHIO VALLEY" Arial 700 22 px `#93a3b2` tracking 6; counter "6.1" Courier New 700 84 px `#e74c3c` + " MILLION" Arial Black 900 52 px `#f2f5f8` on the same line; label "PEOPLE UNDER 18 IN OR MORE" Arial 700 20 px `#c8d3e0` tracking 6. (edit_script "6.1 MILLION PEOPLE · OHIO VALLEY": same words, split across lines.) Legend box on screen = image (22..518, 575..905) → x 226 to 799, y 664 to 1045: the card covers it except its bottom 25 px; extend the card to bottom 1045 only if a legend number shows there (it must not).
- Northeast ring: ellipse stroke 3 px `#7fb2e5` (dashed 10 6) around the dark-red area north of the PA-WV line (centre near image (900, 470) = screen (1241, 543); size to enclose that area with 12 px clearance, record rx/ry). Label right of the ring, x 1370 to 1590, y 420 to 530: "30 IN+" Arial Black 900 40 px `#f2f5f8`, "1.3 MILLION" Arial Black 900 40 px `#7fb2e5`, "NORTHEAST" Arial 700 22 px `#93a3b2` tracking 6 (edit_script "30 IN+ · 1.3 MILLION (NORTHEAST)", parentheses dropped, same words). Glass backing behind the label (it sits over the grey/blue map).
- Source line "Source: NOAA NCEI, 2000 census population" Arial 700 19 px `#c8d3e0`, top-right on the dark strip: right 96, top 60, right-aligned (x <= 1824, y 60 to 80, far above the circle corner; the usual bottom-left spot sits on the image and the counter card).
- Tiers: 84 / 52 / 40 / 22 / 20 / 19.

## 4. Must be true in the picture
1. Lit area = the published 18 IN+ colours inside Ohio Valley states only; nothing lit in Pennsylvania or New York; the unlit 18 IN+ pixels in PA stay visible (desaturated) so the cut at the state line is honest, not hidden.
2. "6.1 MILLION" sits with "OHIO VALLEY" and "18 IN"; "1.3 MILLION" sits with "NORTHEAST" and "30 IN+". The two never share a card.
3. The ring is a ring, not a contour: it encloses the Northeast heavy-snow area and claims no edge.
4. The legend's RSI values (34.7, 14.5) are never visible (A2-S11 reveals 34.7).
5. Counter opens on the first tick's value (0.1), fast then slow into 6.1; one decimal throughout.
6. Nothing in x >= 1600, y >= 680; all our text 96 px / 54 px inside the frame.

## 5. Panel text (exact) and cues (`audio/a2-s10.words.json`, seconds from A2-S10 start)
Text: `18 IN+` · `OHIO VALLEY` · `6.1` · ` MILLION` · `PEOPLE UNDER 18 IN OR MORE` · `30 IN+` · `1.3 MILLION` · `NORTHEAST` · `Source: NOAA NCEI, 2000 census population`
- 0.00 "Now": map on at full colour, source line on; slow push 1.00 to 1.02 over the whole window (ease none, origin at screen (900, 560)). `/* NOW @0.00 */`
- 1.06 "map.": base desaturates (0.6 s); highlight fills up from 0 to .55 (0.8 s). `/* MAP @1.06 */`
- 1.98 "More": counter card slides in (`fromTo` y 40 to 0, autoAlpha, 0.6 s, power3.out), eyebrow on. `/* MORE @1.98 */`
- 2.34 "6": counter runs 0.1 to 6.1 (power4.out, 1.3 s, landing 3.64), " MILLION" on at 3.30 "million". `/* 6.1 @2.34 */ /* MILLION @3.30 */`
- 4.16 "Ohio": lit area outline pulses (stroke 3 to 5 px, 0.4 s yoyo). `/* OHIO @4.16 */`
- 5.82 "18": "18 IN+" pill in and the card label in. `/* 18 @5.82 */`
- 7.72 "Northeast": ring draws (stroke-dashoffset, 0.7 s). `/* NORTHEAST @7.72 */`
- 9.06 "1": "30 IN+" and "1.3 MILLION" lines in (y 16 to 0, 0.35 s, 0.15 s apart), "NORTHEAST" with them. `/* 1.3 @9.06 */` Note: the voice says "1.3 million" before "30 inches"; the label shows both together on the number.
- 10.88 "30": "30 IN+" flashes `#f2f5f8` to `#7fb2e5` 0.4 s. `/* 30 @10.88 */`
- 11.86 to exit: push continues; outline breathes (opacity .8 to 1, sine).
- Exit: last 0.6 s: counter card `to` x -980, autoAlpha 0; ring label `to` x 980, autoAlpha 0; map holds and the cut to g-a2-11 is the scene exit.
Host: data-start = A2-S10 start, duration = 12.12 + 0.40 = 12.52 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Receipt includes the measured PA-OH and PA-south line image px, the threshold colours, highlight point count and area.
