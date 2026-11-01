# g-intro-6-pbz-sheet: NWS Pittsburgh snow records sheet, rank-1 row (I1-S2)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` (Text doctrine "A document page in a graphic", Motion and exits) and `learnings/mg.md` first.
Start from: `library/inhouse/quote-card.html` (beige cite stock over a dark map, dark text) for the card surface and slide; the page image replaces the quote text.
Sits over: `g-intro-5-inland` (map, frame H, Pittsburgh pin at (560, 520)). That comp keeps its text out of this card's box (x 960 to 1580, y 150 to 660) in this window. Overlay host on track 3.

## 0. Claim
The NWS Pittsburgh record list puts the 24-26 November 1950 storm at rank 1: 27.4 inches, the city's biggest snowstorm on record.

## 1. Source
- Page: https://www.weather.gov/media/pbz/records/snow.pdf (NWS Pittsburgh, US government, public domain). Fact-check intro-r2 row 21: rank 1 "27.4" November 24-26, 1950", next 25.9" Dec 1890 (pdftotext, this round). `research/nws-facts.md` §2 row "Pittsburgh largest storm on record".
- Media: `media/docs/pbz-snow-records.png`. If the sourcing lane has not made it, render the page that holds the "largest snow storms" list at 200 dpi (`pdftoppm -r 200 -png -f <page> -l <page> snow.pdf media/docs/pbz-snow-records`) and add a `provenance.csv` row (source URL, NWS public domain, date fetched). Report the page number used.

## 2. Datum, scale, orientation
The page is not redrawn: it is the real page image, cropped. The crop is measured on the rendered page by you (layout not known in advance): it spans the full width of the "largest snow storms" table's text column plus 24 px margin each side, from the table's title line down to the rank 3 row. Whole lines only: no word or number cut at the left or right edge in any frame, including both ends of the push.

## 3. Geometry (px, 1920 x 1080)
- Card: beige cite stock `rgba(232,222,200,.90)`, radius 18, box x 980 to 1560, y 170 to 590 (580 x 420 px). The page crop sits inside with 20 px padding, scaled to fit the width (`object-fit: contain`, no cover crop; if the crop's aspect leaves space, the card height shrinks to fit, top fixed at 170).
- Eyebrow above the card, inside the card's top padding strip: "NWS PITTSBURGH · LARGEST SNOWSTORMS" Arial 700 22 px `#2a2622` tracking 4 (dark text on the beige stock).
- Highlight bar on the rank 1 row: a rectangle the row's full width and line height + 8 px, `#d8a13a` at 0.35, `mix-blend-mode: multiply`, drawn left to right (scaleX 0 to 1, transformOrigin left center, 0.5 s). Its y comes from the measured row position (state it in the receipt).
- Chip under the card, centred on the card's x (1270), two lines on one glass surface (`rgba(10,16,24,.55)`, blur 18, 1 px `rgba(255,255,255,.14)`, radius 14, padding 10 x 22): line 1 "27.4 IN" Arial Black 900 58 px `#f2f5f8`; line 2 "BIGGEST ON RECORD" Arial 700 26 px `#dfe7ee` tracking 3. Box about 440 x 120 px. Place it to overlap the card's lower edge by 40 px (top = card bottom - 40), and keep its bottom at or above y 670 and its right edge at or left of x 1590 (presenter-circle corner x >= 1600, y >= 680): with the card ending at y 590 the chip spans y 550 to 670, x 1050 to 1490. Declare `data-overlap-ok="chip sits on the sheet foot by design"` on the chip only after a frame read.
- Push: the page image scales 1.00 to 1.06 about the rank 1 row (transformOrigin at that row) over the hold; the crop must still show whole lines at 1.06 (check both ends).
- Three tiers: 58 (chip line 1), 26 (chip line 2), 22 (eyebrow).

## 4. Must be true in the picture
1. The highlighted row is the rank 1 row and it reads "27.4" and "November 24-26, 1950" on the page image (read it on the frame).
2. No word or number is cut at the crop's left or right edge at scale 1.00 or 1.06.
3. "27.4" appears once as overlay text (chip line 1); the page image itself is not text and does not count.
4. Nothing in x >= 1600, y >= 680; no map text under the card (the map comp's keep-out holds).
5. The card is fully gone before the map's tilt south starts (I1-S2 5.12).

## 5. Panel text (exact) and cues
Text: `NWS PITTSBURGH · LARGEST SNOWSTORMS` · `27.4 IN` · `BIGGEST ON RECORD` (the edit_script chip "27.4 IN · BIGGEST ON RECORD" set as two lines so the figure is big)
Cues from `audio/i1-s2.words.json` (seconds from the I1-S2 start; host starts at the first mark 2.04, so comp time = t - 2.04):
- 2.04 "went": card slides in (`fromTo` x 660 to 0, autoAlpha 0 to 1, 0.7 s, power3.out), eyebrow with it. `/* WENT DOWN @2.04 */`
- 2.04 to 4.62: page push 1.00 to 1.06 (ease none).
- 3.26 "biggest": highlight bar draws on the rank 1 row (0.5 s). `/* BIGGEST @3.26 */`
- 3.52 "snowstorm": chip in (both lines together) (`fromTo` autoAlpha 0, y 20 to 0, 0.4 s, back.out(1.4)). `/* SNOWSTORM @3.52 */`
- 4.42 to 5.02: exit (`to` x 980, autoAlpha 0, 0.6 s, power3.in), finished before "cold" (5.12). `/* EXIT before COLD @5.12 */`
Host: data-start = I1-S2 start + 2.04, duration 2.98 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line item 7: one frame at I1-S2 4.0 s composited over g-intro-5-inland; and frames at both ends of the push for the whole-line check.
