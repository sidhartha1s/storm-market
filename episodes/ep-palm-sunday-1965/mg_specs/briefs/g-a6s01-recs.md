Host: id=g-a6s01-recs file=compositions/g-a6s01-recs.html start=1008.08 (timeline-map.md table 1, read 12 Oct 26 19:27; the mount in index.html wins) duration=7.92 s track=2

# g-a6s01-recs · A6-S1 · ten recommendations, and the first one reaches the announcer (wave 5, page)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21; section 3c rows PC-17 and PC-18. Times: `mg_specs/timeline-map.md` tables 1 and 5.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). No page crop holds past about 8 seconds without a visible change (rule 7: the whole page is on for 5.35 s with three changes on it, the crop for 2.57 s with two). A flash is a stroke or fill change, never a scale pop (rule 12). Five graphics in the opening use two type sizes by design, and page crops in the acts follow them (rule 10): `graphics_qc` flat-type may name this comp.
**Spoken (A6-S1):** "On May second, three weeks after the storms, the team made ten recommendations, and the first one reaches the announcer."
**One look:** the report's page of ten numbered recommendations, then the first one up close with the announcer's words underlined.

## 0. What this graphic claims
The Weather Bureau survey team's report of May 2, 1965 made ten recommendations on one page. The first asks news outlets to install "positive alerting devices (remoted to the announcer's position where necessary)" on their weather teletypewriters.

## 1. Source
- `edit_script.md` A6-S1, Rows [G; survey printed p. 2; survey PDF p. 3: memo dated May 2, 1965; 11 April to 2 May is 21 days by the fact check's script]. Picture note: "the survey's recommendations page (inventory B1, printed p. 2), whole for a moment with the date label 'May 2, 1965' and the name card 'P. H. Kutschenreuter · chairman, Weather Bureau survey team' (on screen only, not spoken). Then a tight crop on recommendation 1."
- Page whole: `media/docs/survey-p2-recs-page.png` (835 x 1080; the 300 dpi page `media/docs/survey-pdf-08-orig.png`, 2550 x 3300, scaled; `provenance.csv` row "Survey printed p.2: crop PC-17"). Ten numbered items; the first lines of the ten items sit at page y 531, 944, 1198, 1358, 1565, 1817, 2087, 2343, 2548 and 2751 (row scan of the 300 dpi page, 12 Oct 26).
- Tight crop: `media/docs/survey-p2-rec1-crop.png` (1460 x 290, `provenance.csv` row "Survey printed p.2: crop PC-18"), read by eye 12 Oct 26. It holds recommendation 1 whole, seven lines: `1. Hold preparedness meetings in collaboration with the appropriate` / `Federal, State, county and local government officials and news dis-` / `seminators in order to develop emergency plans for alerting all` / `segments of communities whenever emergency warnings are issued. Urge` / `news outlets to install positive alerting devices (remoted to the` / `announcer's position where necessary) on weather teletypewriter machines` / `installed on their premises.`
- The date is the covering memo's (survey PDF p. 3), not printed on this page: it is our label, on glass. The chairman's name and title are the Picture note's wording and are on screen only.

## 2. Datum, scale, orientation
- Page whole: the file at 0.9 times, 752 x 972, at screen left 150, top 54 (right 902, bottom 1026). Screen x = 150 + file x times 0.9; in 300 dpi page px, screen x = 150 + page x times 0.2949 and screen y = 54 + page y times 0.2945. **Its type is about 12 px tall at this size and is not meant to be read:** the page is shown as an object, ten numbered paragraphs on one sheet. The reading happens on the tight crop.
- Tight crop: mounted at its own size, 1460 x 290, at screen (106, 395) inside its card: screen x = crop x + 106, screen y = crop y + 395.
- Boxes measured on the crop file by a row and column projection (12 Oct 26):
| Item | Crop px (x0 to x1, y0 to y1) | Screen px |
|---|---|---|
| Line 5 of 7, whole: `news outlets to install positive alerting devices (remoted to the` | 140 to 1296, 168 to 197 | x 246 to 1402, y 563 to 592 |
| `positive alerting devices (remoted to the` (words 5 to 10 of that line) | 565 to 1296, 168 to 197 | x 671 to 1402, y 563 to 592 |
| Line 6 of 7, whole: `announcer's position where necessary) on weather teletypewriter machines` | 140 to 1424, 202 to 235 | x 246 to 1530, y 597 to 630 |
| `announcer's position where necessary)` (words 1 to 4 of that line) | 140 to 789, 202 to 235 | x 246 to 895, y 597 to 630 |
- The typescript is single spaced: line 6's ink starts 5 px under line 5's. So the underline here is 3 px thick and sits 1 px under its line box, not the 6 px at 4 px of design sheet section 9 (the same reason as `mg_specs/briefs/g-a2s15-old.md`). Read both edges on a frame.

## 3. Geometry (screen px)
Ground: the canvas gradient, on from frame 0.
| Element | Px |
|---|---|
| Page whole | `<img>` of `survey-p2-recs-page.png`, left 150, top 54, 752 x 972, `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`. On from frame 0. It drifts `scale` 1.00 to 1.02 about its own centre from 0 to 5.35, `ease:"none"` |
| Margin dots | ten circles radius 6, fill Caption dark (never Popfig red), in the page's left margin at screen x 224, centres y 217, 339, 414, 462, 522, 596, 676, 751, 812, 872 (one beside each item's number; the two-digit "10." starts at x 242). They ride the page's drift (same wrapper) |
| Date label | glass chip, left 916, top 250, height 46, padding 0 x 22, Arial 700 26 px, Body light: `May 2, 1965` |
| Name card | glass plate as `compositions/g-i1s2-station.html` `.stn-card` (same fill, blur, border, radius 28): left 916, top 330, 660 x 170 (right 1576). Name `P. H. Kutschenreuter`: Arial Black 900 52 px, Headline white, left 958, top 352 (about 560 px wide: read it on a frame, it must end inside the plate; if it does not, set it at 46 px; as built and passed the name is at 46 px). Sub `chairman, Weather Bureau survey team`: Georgia italic 30 px, Amber 2, left 960, top 432 |
| Source line | design sheet section 10, left 916 (as built and passed; this brief first said left 96), bottom 60: `Weather Bureau survey report, 1965, p. 2`. On for the whole comp |
| Document card (the crop) | design sheet section 9: left 96, top 385, 1480 x 310 (right 1576, bottom 695), Beige polaroid border 10 px, its shadow; the crop at (106, 395) |
| Unlit page (on the crop) | four Panel dark rects at 45 %: R1 screen x 106 to 1566, y 395 to 560 (lines 1 to 4); R2 x 106 to 659, y 560 to 593 (the first four words of line 5); R3 x 907 to 1566, y 597 to 634 (the last four words of line 6); R4 x 106 to 1566, y 634 to 685 (line 7). The two underlined phrases stay bright |
| Underline A | Popfig red, 3 px, screen x 671 to 1402, y 594 to 597, under `positive alerting devices (remoted to the`; `scaleX` 0 to 1, `transformOrigin:"left center"` |
| Underline B | Popfig red, 3 px, screen x 246 to 895, y 632 to 635, under `announcer's position where necessary)` |
No quote strip in this comp: the same words come as a paper card in the next one (`g-a6s02-floorplan`), and the crop is on for under 3 s.

## 4. Must be true in the picture
1. The page shown whole is the survey's own recommendations page, unaltered, with ten dots beside its ten numbered items: ten, not nine and not eleven.
2. The underlined words are the page's own: `positive alerting devices (remoted to the` and `announcer's position where necessary)`. Nothing on either card is retyped.
3. The date label reads `May 2, 1965` and sits on glass beside the page, never on the page: the page prints no date.
4. The name card reads `P. H. Kutschenreuter` and `chairman, Weather Bureau survey team`. No portrait, no drawn person.
5. The underline is Popfig red, the page's own mark in this episode. The margin dots are Caption dark: they count, they do not accuse.
6. While the crop is on, the whole page, the date label and the name card are at opacity 0.18 or less behind it and nothing of them can be read as a second claim.
7. No county chip, no "County A", no "County B", no station name.
8. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680 (the crop card ends at x 1576).
9. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: `May 2, 1965` · `P. H. Kutschenreuter` · `chairman, Weather Bureau survey team` · `Weather Bureau survey report, 1965, p. 2`. Page words are the image.
Cue words and times are from `audio/a6-s1.words.json` as it stood on 12 Oct 26 at 19:27 (wav 7.59 s). "t from comp start" is `mg_specs/timeline-map.md` table 5: the segment's "wav start inside the composition" (-0.39) plus the word's time; the first word takes the "first sound" column (0.01). Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A6-S1 | 0 | On | 0.00 | 0.01 | first frame: ground, the page whole, the source line |
| 1 | A6-S1 | 1 | May | 0.54 | 0.15 | date label `May 2, 1965` rises beside the page (`y:16` set at 0, then `to y:0, autoAlpha:1`, 0.3 s) |
| 2 | A6-S1 | 9 | team | 3.30 | 2.91 | name card slides in from the right (`x:120` set at 0, then `to x:0`, 0.5 s, power3.out), name then sub 0.15 s apart |
| 3 | A6-S1 | 11 | ten | 3.80 | 3.41 | the ten margin dots land top to bottom, 0.06 s apart (0.54 s in all, each a 0.15 s fade): done by 4.10, inside the word "recommendations" |
| 4 | A6-S1 | 15 | first | 5.74 | 5.35 | the page, the dots and the date label go to opacity 0.18 (0.3 s); the name card fades out over 0.3 s as the crop card comes in (this brief first kept it dimmed to the end; dimmed, it sat half under the card's top edge); the crop card enters from the left (0.45 s, power3.out; as built and passed, this brief first said from the right) |
| 5 | A6-S1 | 17 | reaches | 6.24 | 5.85 | unlit page fades in on the crop (0.3 s); underline A draws (0.35 s) |
| 6 | A6-S1 | 19 | announcer. | 6.74 | 6.35 | underline B draws (0.35 s). Hold to the last frame (7.92) |
The ten margin dots are not in the Picture note: they give "ten recommendations" a visible change. If the lead strikes them, step 3 is empty and the page holds on its drift.

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a6s01-recs.html` is the only file the builder writes; `data-composition-id="g-a6s01-recs"`; id prefix `rec-`; root `<div id="rec-root" ...>` styled through `#rec-root` (plan rule 3 overrides the template's `id="root"`). Full frame, opaque, own ground on from frame 0.
**Base it copies:** `compositions/g-i1s6-page.html` (document card, unlit page, red underline by `scaleX`) and `mg_specs/briefs/g-a2s15-old.md` (a single-spaced page: thin underline close under the line); `compositions/g-i1s2-station.html` for the name card's glass plate and type (`.stn-card`, `.stn-name`, `.stn-sub`), under this comp's class names. The date label is the glass chip of design sheet section 9 ("County label": left, top, height 46, padding 0 x 22, Arial 700 26 px). `g-a5s20-team` (wave 4) carries the same kind of date label for April 12, 1965: if its brief is on disk and gives the chip other numbers, match them and say so in the receipt. Nothing later copies this comp.
**Assets mounted (paths from the episode folder, each confirmed on disk 12 Oct 26):**
- `media/docs/survey-p2-recs-page.png` (PC-17, 835 x 1080, 377,250 bytes), shown at 752 x 972.
- `media/docs/survey-p2-rec1-crop.png` (PC-18, 1460 x 290, 166,298 bytes), shown at its own size.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a6s01-recs`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `python3`, never `python`.

## 7a. Done line
All seven lines of template section 7a. Line 2 (fill): state the measured figure at 4.5 (page, dots, label, name card) and at 7.0 (crop card). Line 3: frame 0 shows the page whole. Line 5: no dot touches a numeral (the "10." starts at screen x 242, the dots' right edge is x 230); neither underline touches the line under it. Line 6: the ten dot centres are computed by a script from the ten page y values of section 1 and the scale of section 2, and stated in the receipt. Line 7 does not apply: the comp is opaque.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.01) and the frame after it (0.05): the page whole and the source line, no label, no card, no dot. Then one settled frame per cue: 0.60 (date label), 3.40 (name card complete, inside its plate), 4.20 (ten dots, count them, one beside each number), 5.90 (crop card in place, the rest at 0.18), 6.30 (unlit page, underline A complete under `positive alerting devices (remoted to the`), 6.80 (underline B complete under `announcer's position where necessary)`), 7.85 (last frame). On 6.30 and 6.80 read the underline's lower edge against the next line's ink. Each cue second in both seek orders.
