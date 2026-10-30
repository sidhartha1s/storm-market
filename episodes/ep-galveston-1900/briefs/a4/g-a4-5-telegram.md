# g-a4-5-telegram · A4-S3 0 to 21.90 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `compositions/g-a4-1-gulf-rising.html` (the telegraph form, built first: copy its form), `compositions/g-a3-12-330.html` (page panel), `compositions/g-intro-10-delusion.html` (the ABSURD DELUSION chip, reused unchanged).

## 0. Claim
Saturday morning Cline wired Washington that unusually heavy swells from the southeast were flooding low places three to four blocks from the beach, and that such high water with opposing winds had never been observed before; nine years earlier he had called the idea of a storm badly damaging Galveston an absurd delusion.

## 1. Source
MWR Sept 1900 p. 372 (factcheck/a4-r1.md rows 11 to 14; a4-r2.md rows 1 to 4), telegram text: "Unusually heavy swells from the southeast, intervals one to five minutes, overflowing low places south of city three to four blocks from beach. Such high water with opposing winds never observed previously." Scan: A4-S1_c1 PDF page 2 (printed p. 372, telegram at the bottom right per picks.md), rasterised to `media/a4/mwr-p372.png`. 1891: Galveston Daily News, 16 July 1891, "absurd delusion" (sources-cline.md §1; a4-r2 row 4).

## 2. Datum, scale, orientation
Full-frame designed comp on the tokens gradient. Page panel left (x 140 to 760), telegraph form right (x 840 to 1580). Chip zone top-right above the form; source line top-left.

## 3. Geometry (px)
- Page panel: glass card x 140 to 760, y 180 to 940, p. 372 crop around the telegram (whole lines, measured), amber band behind the telegram lines, page dimmed to 0.55.
- Form: g-a4-1's form at x 840 to 1580, y 230 to 900 (taller: five ruled lines at y 400, 480, 560, 640, 720, 800). Courier New 700 34 px `#2a2622` (mid tier), typed phrase by phrase, exact telegram text in capitals, line breaks: "UNUSUALLY HEAVY SWELLS FROM" / "THE SOUTHEAST, INTERVALS ONE" / "TO FIVE MINUTES, OVERFLOWING" / "LOW PLACES SOUTH OF CITY THREE" / "TO FOUR BLOCKS FROM BEACH." / "SUCH HIGH WATER WITH OPPOSING" / "WINDS NEVER OBSERVED PREVIOUSLY." (7 lines: add rules at y 880 and shrink spacing to 72 px from y 380: 380, 452, 524, 596, 668, 740, 812). Header "TELEGRAM · TO WASHINGTON" Georgia 700 30 px at (880, 300).
- Gold tier: "NEVER OBSERVED PREVIOUSLY" spans turn `#d8a13a` with a 6 px `#d8a13a` underline drawn left to right.
- Chip C1 (glass, main Arial Black 900 52 px) "3 TO 4 BLOCKS FROM BEACH", right edge x 1824, top 100 (its bottom stays under y 220, above the form's top at 230).
- Chip C2 = g-intro-10's ABSURD DELUSION chip (copy its markup and style exactly, text "ABSURD DELUSION", tag "Galveston Daily News, July 1891"), centred x 1210, top 440 over the dimmed form (form dims to 0.25 first so the chip is the one reading target; `data-overlap-ok="1891 chip over dimmed form"` on the chip).
- Source line top-left: "Isaac Cline, Monthly Weather Review, September 1900, p. 372"; at 18.50 it swaps to "Galveston Daily News, 16 July 1891" (out 0.3 s, in 0.3 s; one source line at a time).

## 4. Must be true in the picture
1. Form text is the telegram verbatim (receipt diff against the quote above: 0 differences).
2. Each phrase appears no earlier than the voice reaches its sense (cues below); "intervals one to five minutes" types with the first phrase group, unhighlighted (not spoken).
3. C1 and C2 never on screen together.
4. No word cut at the page crop edge; nothing in x >= 1600, y >= 680.

## 5. Text and cues (a4-s3.words.json)
- 0.00: frame 0 shows page panel, empty form, source line.
- 2.92 ("telegram") /* TELEGRAM @2.92 */: header in; 3.52 ("Washington") header's "TO WASHINGTON" turns `#f2f5f8`.
- 5.38 ("unusually") /* SWELLS @5.38 */: lines 1 to 3 type (5.38 to 7.42, per word, stagger to finish by "were" 7.42).
- 7.72 ("flooding") to 10.32 ("beach"): lines 4 and 5 type; 8.84 ("three") /* BLOCKS @8.84 */: C1 in.
- 11.14 ("It also said"): C1 out (x 980, 0.5).
- 11.78 ("water") to 14.08 ("against"): lines 6 and 7 type up to "WINDS".
- 14.76 ("never") /* NEVER @14.76 */: "NEVER OBSERVED PREVIOUSLY" types and turns gold, underline draws 14.76 to 15.44.
- 16.36 ("Nine") /* 1891 @16.36 */: page and form dim to 0.25 (0.6 s); source line swaps at 18.50.
- 20.82 ("delusion") /* DELUSION @20.82 */: C2 in (g-intro-10 entrance).
- 21.90 segment end; land time to the cut.

## Motion for the whole window
Typing steps every 0.2 to 0.5 s from 5.38 to 15.44; from 15.44 a slow push on the form (scale 1.00 to 1.03) and the gold underline shimmer (opacity 1 to 0.7, 1.2 s yoyo); C2 float.

## Exit
C2 slides out `x:980` in the last 0.6 s; cut to g-a4-6.

## Footage under it
None; MWR p. 372 scan inside the comp (A4-S1_c1, verified Y).
