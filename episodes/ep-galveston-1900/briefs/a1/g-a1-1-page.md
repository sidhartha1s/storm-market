# g-a1-1-page · A1-S1 0.00 to A1-S2 end · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules" (incl. "The page"). Exemplars: `references/editing-patterns/ep6-glass-panel-camera-clamp.html` (camera as a pure function of time, clamp), `episodes/ep-1974-super-outbreak/compositions/g-cite-paper.html` (paper treatment), `library/inhouse/snippets/helpers.js` `logZoom`. Overlays that sit on this comp: g-a1-2-s1-cards (popfig, lower-third, source line) and g-a1-3-quote (S2 quote card, chips). This comp carries no text of its own.

## 0. Claim
This is the real page Cline's words were printed on, Galveston Daily News, Thursday 16 July 1891, page 5; his sentence is in the column printed around Fig. 7 and Fig. 8, and it is lit as the narrator reads it. Nothing claims what Fig. 7 or Fig. 8 show.

## 1. Source
- Page: `media/candidates/a1/provenance.csv` row 1, Commons `File:Galveston_Daily_News_-_July_16,_1891.jpg`, CC0, verified Y (page 5, dated masthead "THURSDAY, JULY 16, 1891" visible at the top of the scan).
- Cline wrote "a certain part of this article under Fig. 7 and Fig. 8": factcheck/a1-r1.md row 5 (Commons, SECONDARY). Fig. 7/8 content: unknown (rows 4, 7), so they are never labelled.
- The sentence: factcheck/a1-r1.md rows 8, 9; my 3x read of the scan (column 3, source px y 535 to 597) gives the wording in `_list.md` change 2.

## 2. Datum, scale, orientation
- Two image layers, both positioned in SOURCE px of the 1412 x 1802 original and moved by one camera `screen = (960 + (sx − cx)·s, 540 + (sy − cy)·s)`:
  - `media/a1/gdn-1891-p5-full.jpg` (846 x 1080 staged; draw it at 1412 x 1802 source size, so its own scale factor is 1/0.5993).
  - `media/a1/gdn-1891-p5-col3.jpg` (215 x 880 native crop of x 400 to 615, y 0 to 880), drawn exactly over the same source rect, above the full page.
- Camera keys (computed):

| key | comp time | s | cx, cy | what is on screen |
|---|---|---|---|---|
| K0 full page | 0.00 | 0.5993 | 706, 901 | page x 536.9 to 1383.1, y 0 to 1080 |
| K0b drift | 0.00 to 4.62 | 0.5993 to 0.6200, ease none | 706, 901 | whole page, slow push |
| K1 column | 4.62 ("Some") to 9.04 ("Klein") | 0.6200 to 1.15, logZoom, power2.inOut | 706,901 to 507,445 | column 3 x 842.7 to 1078.5, y 51.3 to 1028.8 |
| K1b drift | 9.04 to 11.121 | 1.15 to 1.18, ease none | 507, 445 | column |
| K2 sentence | S2 0.00 ("He") to 1.30 | 1.18 to 4.0, logZoom, power2.inOut | 507,445 to 615,566 | column 3 x 120 to 940; lines below |
| K2b drift | 1.30 to 8.766 | 4.0 to 4.12, ease none, cx/cy fixed | 615, 566 | sentence block |

  (S2 times are comp-local + S1's offset; read the mounts.)
- Layer swap: full page opacity stays 1 under the crop; the crop layer fades 0 → 1 between s 0.9 and 1.1 on the K1 move.
- Whole lines rule (mg-quickref "Text doctrine", document page): from 5.60 to 8.40 everything OUTSIDE column 3 (source x < 405 or > 610) fades 1 → 0 (a mask or a second copy, the builder's choice), so from K1 on only column 3 is on the canvas and no word is cut at a frame edge. Canvas ground: tokens.md radial gradient.

## 3. Geometry (px)
- Column 3 lines of the sentence (source px, baseline-centre y, measured at 3x ±3): L1 543.3 (lit part starts at "The opinion", x ≈ 473), L2 551.7, L3 560.0, L4 568.3, L5 576.7, L6 584.3, L7 591.7 (lit part ends after "reasoning;", x ≈ 548). Text block x 418 to 603.
- At K2 (s 4.0, c 615,566) those lines sit at screen y 449.2, 482.8, 516.0, 549.2, 582.8, 613.2, 642.8; column x 120 to 940. The right half (x 1000 to 1824) is left for g-a1-3's quote card: nothing of this comp's highlight goes past x 940.
- Highlight: one rect per line, height 7.5 source px (30 px at s 4), fill `#d8a13a` at opacity 0.32, `mix-blend-mode: multiply`, drawn `scaleX 0 → 1`, `transformOrigin:"left center"`, 0.5 s power2.out. Rects live in source px inside the camera group, so they move with the page.
- Re-measure all line y's on the staged crop before drawing; list the measured values in the receipt.

## 4. Must be true in the picture
1. Frame 0 is the whole page, masthead "THURSDAY, JULY 16, 1891" legible, nothing cropped on any side (page x 536.9 to 1383.1).
2. From 8.40 on, no word of any other column shows; column 3 is never cut left or right by the frame.
3. Each highlight sits on its printed line (rect centre within ±3 screen px of the line centre at s 4) and covers only the words being read (L1 from "The opinion", L7 only to "reasoning;").
4. No label, arrow or ring is put on Fig. 7 or Fig. 8.
5. The page is never shown in anyone's hands; it is the scan on the canvas.
6. Nothing of this comp enters x >= 1600, y >= 680 after K1 (column is centred); at K0 the page edge (x 1383) stays left of 1600.

## 5. Text and cues (no text in this comp; cues from a1-s1/a1-s2.words.json)
- S1 0.00: K0 page on. /* PAGE @0.00 */
- S1 4.62 ("Some"): K1 push starts. /* PUSH @4.62 */ S1 9.04 ("Klein"): column settled.
- S2 0.00 ("He"): K2 push to the sentence. /* SENTENCE @0.00 */
- S2 1.06 ("held"): L1 lit. 2.04 ("unacquainted"): L2. 3.26 ("conditions"): L3 first part (to "things," x ≈ 500). 4.80 ("Such"): L3 rest and L4. 5.14 ("fear,"): L5. 5.94 ("could"): L6. 7.74 ("and"): L7. /* REASONING @8.28 */ on 8.28 ("reasoning.") all seven rects brighten opacity 0.32 → 0.45 (0.3 s).
- Host: A1-S1 0.00 to A1-S2 8.766 (plus the inter-segment gap).

## Motion for the whole window
The camera never stops: K0b, K1b, K2b drifts are continuous `ease:none` tweens; highlights add beats. No gap of 4 s without a moving element.

## Exit
A1-S3 opens on the island cross-section (cut): fade-through, the root to 0 over the last 0.4 s of the host.

## Footage under it
None. The page is inside the comp (two staged stills, `_list.md` open item).
