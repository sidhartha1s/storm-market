Host: id=g-a5s20-team file=compositions/g-a5s20-team.html start=995.57 (timeline-map.md table 1; the mount in index.html wins) duration=9.19 s track=2

# g-a5s20-team · A5-S20 · the survey team, and the word "excellent" (wave 4, page family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, section 3c rows PC-15 and PC-16, section 7. Times: `mg_specs/timeline-map.md` tables 1 and 5. Base: `mg_specs/briefs/g-a2s15-old.md` (page card).
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id, never `root` (rule 3). No page crop holds past about 8 s without a visible change (rule 7). The "excellent" crop carries a third line, the toll approaching 200, and it stays in frame (rule 19).
**Spoken (A5-S20):** "The next day the Chief of the Weather Bureau named a team of five. Its job was to find out why so many lives were lost after forecasts called excellent."
**One look:** the team's own memo, then the report's first page with one word underlined.

## 0. What this graphic claims
A Weather Bureau survey team was established on April 12, 1965. Its report says the tornado forecasts were excellent, and in the next line that the reported death toll was already approaching 200.

## 1. Source
- `edit_script.md` A5-S20, Rows [E, Kutschenreuter memo; survey PDF p. 3] and [survey printed p. 1: "a survey team of five Weather Bureau officials"; "excellent" forecasts].
- Memo crop: `media/docs/survey-memo-p3-crop.png` (1460 x 868, from `media/docs/survey-pdf-03-orig.png`; read by eye 12 Oct 26). It holds the printed heading `UNITED STATES GOVERNMENT` / `Memorandum`, `TO : Chief of Bureau`, `DATE: May 2, 1965`, `FROM : Chairman, Tornado Survey Team`, `SUBJECT: Tornado Survey - Series of April 11, 1965, Tornadoes`, and the first paragraph, which starts `The tornado survey team which you established on April 12,` / `1965, has completed its assigned task.`
- Page crop: `media/docs/survey-p1-excellent-crop.png` (1460 x 169, from `media/docs/survey-pdf-07-orig.png`, printed p. 1). Three lines: `A post analysis early on April 12 indicated that the Weather Bureau's` / `tornado forecasts issued on April 11, 1965, were excellent. Yet the` / `reported death toll was already approaching 200 and still rising rapidly.`

## 2. Datum, scale, orientation
Both crops are mounted at their own size, 1460 px wide. Boxes measured on the files by a row and column scan.
Memo (crop at screen 106, 64):
| Words | Px inside the crop | Screen px |
|---|---|---|
| `The tornado survey team which you established on April 12,` | x 270 to 1207, y 623 to 651 | x 376 to 1313, y 687 to 715 |
| `1965,` (first word of the next line) | x 275 to 343, y 656 to 684 | x 381 to 449, y 720 to 748 |
| rest of that line | x 355 to 1270, y 654 to 686 | x 461 to 1376, y 718 to 750 |
| paragraph lines 3 to 7 | x 260 to 1270, y 688 to 868 | x 366 to 1376, y 752 to 932 |
| blank paper right of the `FROM` line | x 1044 to 1440, y 290 to 440 | x 1150 to 1546, y 354 to 504 |
The paragraph is single-spaced (33 px from line to line), so the underline here is 3 px at 1 px under the line box, not the design sheet's 6 px at 4 px.
Page 1 (crop at screen 106, 390): the scan is skewed, its lines rise to the right by 0.033 px per px (1.89 degrees). The word `excellent.` is crop x 961 to 1140, y 66 to 95 at its centre. Its underline runs from crop (961, 100) to (1140, 94): screen (1067, 490) to (1246, 484), 3 px thick, turned to the page's slope. The third line's ink starts at crop y 108 under the word's left end and y 102 under its right end, so the underline clears it.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0 |
| Memo card | left 96, top 54, 1480 x 888 (right 1576, bottom 942), Beige polaroid border 10 px, the document card's shadow; crop at (106, 64). On from frame 0 |
| Date label | glass chip on the memo card's blank paper (it is a child of the card and leaves with it): left 1170, top 396, padding 14 x 26, Arial Black 900 34 px, Headline white: `April 12, 1965`. It stays inside screen x 1150 to 1546, y 354 to 504 |
| Underline 1 | Popfig red, 3 px, screen x 376 to 1313, y 716 to 719; `scaleX` from the left |
| Underline 2 | Popfig red, 3 px, screen x 381 to 449, y 749 to 752 |
| Unlit memo | two Panel dark rects at 45 %, under the underlines in z order: screen x 461 to 1376, y 718 to 750; and x 366 to 1376, y 752 to 932. The printed heading, `TO`, `DATE`, `FROM` and `SUBJECT` lines stay bright |
| Memo source | design sheet section 10, left 96, bottom 60: `Weather Bureau survey team memo, May 2, 1965` |
| Page card | left 96, top 380, 1480 x 189 (right 1576, bottom 569), same border and shadow; crop at (106, 390). `visibility:hidden` in CSS, `x:1900` set at 0 |
| Underline 3 | Popfig red, 3 px, from screen (1067, 490) to (1246, 484): one line element turned to the slope, drawn from its left end |
| Page source | same place as the memo source, a second pre-authored element: `Weather Bureau survey report, 1965, p. 1` |

No part of the page card is dimmed: all three lines stay at full brightness.

## 4. Must be true in the picture
1. `April 12, 1965` is our label on glass. The memo's own printed date, May 2, 1965, is readable on the same frame and is not covered.
2. The underlined memo words are `The tornado survey team which you established on April 12, 1965,` and no others.
3. On page 1 only `excellent` is underlined. The third line, with "approaching 200", is in frame and as bright as the others.
4. Nothing on either card is retyped. "a team of five" is spoken, not shown: no figure 5 is on screen.
5. One source line per frame, and it names the page that is on screen.
6. A visible change at least every 3 s. Nothing in x >= 1600 and y >= 680.
7. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Steps 0 to 3: the memo card fills the frame (y 54 to 942). Step 4 on: the memo card does not leave. It stays in place and dims to opacity 0.22, and the page card (y 380 to 569) sits over it; a page card alone would leave the band below it (y 569 to 1080, 47.3 % of the frame) empty for 5.26 s.

## 5. Text (exact) and cues
Text: `April 12, 1965` · `Weather Bureau survey team memo, May 2, 1965` · `Weather Bureau survey report, 1965, p. 1`. Page words are the images.
t from comp start = the segment's wav start inside the composition (timeline-map.md table 5: -0.41) plus the word's time; the first word uses table 5's first sound.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A5-S20 | 0 | The | 0.00 | 0.00 | first frame: memo card whole and bright, memo source |
| 1 | A5-S20 | 2 | day, | 0.68 | 0.27 | date label lands (`y:16` to 0 with the fade, 0.3 s) |
| 2 | A5-S20 | 9 | named | 2.16 | 1.75 | unlit memo rects fade in (0.4 s); underline 1 draws (0.6 s) |
| 3 | A5-S20 | 11 | team | 2.56 | 2.15 | underline 2 draws (0.2 s) once underline 1 is complete |
| 4 | A5-S20 | 14 | Its | 4.34 | 3.93 | memo card stays in place and dims to opacity 0.22 with its label, unlit rects and underlines (0.4 s; plan rule 22, see section 4 item 7); page card enters from the right over it (to `x:0`, 0.7 s, power3.out); the source line swaps to the page in front |
| 5 | A5-S20 | 29 | Excellent. | 7.96 | 7.55 | underline 3 draws under `excellent` (0.4 s) |
| 6 | end | | | | 9.19 | comp ends; no exit move |
Between step 4 and step 5 the page card sits for 2.9 s with no mark: it is the entrance that carries that stretch.

## 6. Contract
As `references/mg-brief-template.md` section 6, with plan rule 3 over its `id="root"`. File the builder may write: `compositions/g-a5s20-team.html` only. Id prefix `team-`, root id `team-root`. Base it copies: the page card of `compositions/g-i1s6-page.html` (built) and the two-card swap of `compositions/g-i1s7-sheriff.html` (built). Assets mounted: `media/docs/survey-memo-p3-crop.png` (1460 x 868), `media/docs/survey-p1-excellent-crop.png` (1460 x 169). `g-a6s01-recs` uses the same date-label chip; match its size if that comp is built first.

## 7. Tools
As the template's section 7.

## 7a. Done line
As the template's section 7a, all seven. `graphics_qc` flat type: a page crop is one of the plan's rule 10 cases.

## 8. Receipt
As the template's section 8, plus: a close frame of underline 3 showing it under `excellent` and clear of the line below, and the date label's measured box.

## Frames the verifier reads
First frame 0.00 and the frame after it (0.04); 0.70 (label settled); 2.60 (both memo underlines); 4.80 (page card settled, memo gone, source swapped); 8.10 (underline 3); last frame 9.10.
