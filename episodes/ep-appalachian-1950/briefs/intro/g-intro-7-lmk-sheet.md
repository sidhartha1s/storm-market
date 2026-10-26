# g-intro-7-lmk-sheet: Bowling Green November records, the ALL-TIME low row (I1-S3)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` (Text doctrine "A document page in a graphic", Motion and exits) and `learnings/mg.md` first. Build after g-intro-6-pbz-sheet if possible and match its card exactly (same surface, box, eyebrow style, chip style): the two are a pair.
Start from: `library/inhouse/quote-card.html` (beige cite stock over a dark map) or the finished `compositions/g-intro-6-pbz-sheet.html`.
Sits over: `g-intro-5-inland` (map, frame F, Bowling Green pin at (480, 640) with its "-7°F" chip dimmed to 0.35). That comp keeps its text out of this card's box (x 960 to 1580, y 150 to 660) in this window. Overlay host on track 3.

## 0. Claim
In the National Weather Service's November records for Bowling Green, Kentucky, the coldest November reading on the list is still -7°F, set in 1950. This pays loop L2 and the narrator's "when I checked" line.

## 1. Source
- Page: https://www.weather.gov/media/lmk/climate/clibwg/November_Records_Bowling_Green.pdf (NWS Louisville, US government, public domain; "Updated: November 16, 2024", table carries 2025 entries). Rows read by fact-check intro-r2 rows 24, 25: day row "25  74, 1896  -7, 1950" and "ALL-TIME  88, 1909  -7, 1950"; next coldest daily low 0 (1887, Nov 28). Records begin about 1870 (PDF header). `research/nws-facts.md` §3 row "Lexington / Bowling Green KY".
- Media: `media/docs/lmk-bwg-november.png`. If the sourcing lane has not made it, render page 1 at 200 dpi (`pdftoppm -r 200 -png -f 1 -l 1 November_Records_Bowling_Green.pdf media/docs/lmk-bwg-november`) and add a `provenance.csv` row (URL, NWS public domain, date fetched).

## 2. Datum, scale, orientation
Real page image, never retyped. The page shows a day-by-day table (days 1 to 30) with record high and record low columns and an ALL-TIME row. Crop, measured by you on the rendered page: the table's full text width plus 24 px margin each side; vertically from the column header line through the ALL-TIME row. Whole lines only at both ends of the move: no digit or word cut at the left or right edge.

## 3. Geometry (px, 1920 x 1080)
- Card: beige cite stock `rgba(232,222,200,.90)`, radius 18, box x 980 to 1560, y 170 to 590 (as g-intro-6). The page crop is taller than the card: it starts showing the column header and the first rows (scale to card width, `object-fit` none, positioned by translateY), then scrolls up (translateY, power2.inOut) until the ALL-TIME row sits 120 px above the card's bottom edge. Clip the image to the card (overflow hidden on the card); lines cut at the TOP and BOTTOM card edges are fine mid-scroll, lines cut at the left/right are not.
- Eyebrow in the card's top padding strip, on its own beige band so the scrolling page passes under it: "NWS LOUISVILLE · BOWLING GREEN, KY · NOVEMBER RECORDS" Arial 700 22 px `#2a2622` tracking 3. If it does not fit in 540 px at 22 px, use "NWS LOUISVILLE · BOWLING GREEN NOVEMBER RECORDS" at 20 px; never under 19 px.
- Highlight bar on the ALL-TIME row: the row's full width, line height + 8 px, `#5a768f` at 0.40, `mix-blend-mode: multiply`, drawn left to right (scaleX 0 to 1, transformOrigin left center, 0.5 s). Its y is the measured row position after the scroll (state it in the receipt).
- Second, thinner marker on the low cell of that row only: a 3 px `#c0392b` outline box around the "-7, 1950" cell (drawn with strokeDashoffset, 0.4 s).
- Chip, two lines on one glass surface (`rgba(10,16,24,.55)`, blur 18, 1 px `rgba(255,255,255,.14)`, radius 14, padding 10 x 22), overlapping the card foot by 40 px: line 1 "STILL THE" Arial 700 26 px `#dfe7ee` tracking 3, line 2 "NOVEMBER RECORD" Arial Black 900 52 px `#f2f5f8`. Box about 560 x 120 px, spans y 550 to 670, centred on x 1270 (x 990 to 1550). Declare `data-overlap-ok="chip sits on the sheet foot by design"` after a frame read.
- Three tiers: 52 (chip line 2), 26 (chip line 1), 22 (eyebrow).

## 4. Must be true in the picture
1. The highlighted row reads "ALL-TIME" and its low cell reads "-7, 1950" on the page image (read it on the settled frame). If the page's row label differs, keep the page as is and report it.
2. No digit or word is cut at the crop's left or right edge in any frame of the scroll.
3. No overlay text repeats "-7" (the map chip carries "-7°F"; the page image is not text).
4. The chip says the edit_script words exactly: "STILL THE" + "NOVEMBER RECORD".
5. Nothing in x >= 1600, y >= 680; no map text under the card.

## 5. Panel text (exact) and cues
Text: `NWS LOUISVILLE · BOWLING GREEN, KY · NOVEMBER RECORDS` · `STILL THE` · `NOVEMBER RECORD`
Cues from `audio/i1-s3.words.json` (seconds from the I1-S3 start; host starts at the first mark 5.98, so comp time = t - 5.98):
- 5.98 "checked": card slides in (`fromTo` x 660 to 0, autoAlpha 0 to 1, 0.7 s, power3.out), page at its top (header row visible). `/* CHECKED @5.98 */`
- 6.76 "November": scroll to the ALL-TIME row starts (1.2 s, power2.inOut), ends 7.96. `/* NOVEMBER RECORDS @6.76 */`
- 7.96 "it's": highlight bar draws on the ALL-TIME row (0.5 s). `/* ITS @7.96 */`
- 8.22 "still": chip in (`fromTo` autoAlpha 0, y 20 to 0, 0.4 s, back.out(1.4)). `/* STILL @8.22 */`
- 8.62 "coldest": red outline draws on the "-7, 1950" cell (0.4 s). `/* COLDEST @8.62 */`
- 9.02 to 9.76: slow push 1.00 to 1.03 on the page about the ALL-TIME row (motion through the hold).
- 9.76 to 10.36: exit (`to` x 980, autoAlpha 0, 0.6 s, power3.in), ending inside the 0.40 s gap plus 0.2 s of I1-S4 at most; it must be gone before the map's move to Newark settles (I1-S4 0.80).
Host: data-start = I1-S3 start + 5.98, duration 4.38 s (to 10.36; trim to the real gap so the exit finishes inside the host).

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line item 7: one frame at I1-S3 9.4 s composited over g-intro-5-inland; frames at the scroll's start and end for the whole-line check.
