Host: id=g-a5s07-marion file=compositions/g-a5s07-marion.html start=880.86 (timeline-map.md table 1, 12 Oct 26; the mount in index.html wins) duration=19.90 s track=2

# g-a5s07-marion · A5-S7, A5-S8 · The storm had been through Marion; the 9:20 message and the clock stopped at 8:10 (wave 4, map family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 8, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, section 3a row DR-09, section 3c row PC-13, section 6 item 13. Times: `mg_specs/timeline-map.md` tables 1 and 5. Map facts: `media/maps/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). Text fades before the thing it sits on moves: the stamp's three lines fade before the stamp slides and return after it (rule 2). The root is styled through its id, never `id="root"` (rule 3). No page crop holds past about 8 s without a visible change (rule 7). A flash is a stroke or fill change (rule 12). Beat counts are checked against the window (rule 13). Map geometry comes from the file (rule 14). No map shows Alto; inlined ids take this comp's prefix (rule 20). Real places are named here, so `County A` and `County B` never appear. A zone is written in a stamp's place line or not at all, never beside the time.
**Spoken (A5-S7):** "That same storm had already been through Marion. At nine twenty Fort Wayne put it on the wire: three tornadoes had struck the city, with extensive damage."
**Spoken (A5-S8):** "Marion was hit near eight o'clock. Fort Wayne's message went out a full hour and twenty minutes later. A clock in a Marion hospital had stopped at eight ten."
**One look:** one storm path runs east through Marion to the Ohio line; Fort Wayne's 9:20 message about Marion comes in on paper; then a hospital clock stopped at 8:10 sits beside the stamp at 9:20.
No photograph sits under these two sentences.

## 0. What this graphic claims
The storm the 8:40 warning was about had already passed Marion. At 9:20 PM Fort Wayne's office wired that three tornadoes had struck the city of Marion. Marion was hit near 8 o'clock, an hour and twenty minutes before that message, and a clock at a Marion hospital stopped at 8:10 PM.

## 1. Source
- `edit_script.md` A5-S7, Rows [survey printed p. 45: one path, out of Howard County at 7:50, near Marion near 8, Linn Grove at 8:40] · [A22; survey printed p. 43]. A5-S8, Rows [A22; survey printed p. 45] · [C16] · [survey printed p. 45: "The clock at the hospital stopped at 8:10 PM."].
- Page crop `media/docs/survey-p43-920pm-crop.png` (PC-13, 1460 x 377, survey printed p. 43), ten single-spaced lines. Line 4 reads `EST that three tornadoes had struck the city of Marion with extensive damage.`
- Positions, map units (`media/data/points.csv`): `pt-marion` (539.5, 396.7), `pt-linn-grove` (619.0, 379.1), `pt-fort-wayne` (605.1, 297.0). Howard County's box centre from its path in `media/maps/indiana-counties.svg`: (481.2, 411.5). Indiana's east line: x 648.4.
- The path is SCHEMATIC: straight legs between the places the survey names, not a surveyed track. It is one construction for this comp and `g-a5s10-alert`: Howard County's centre, a point 8 map units south of Marion's dot (539.5, 404.7), Linn Grove, then the same leg carried on to the state line at (648.4, 369.6). The point is south of Marion's dot because a leg through the dot itself would miss Blackford County, which the survey names (it would pass 2.8 units north of Blackford's north edge); the survey's own word is "near Marion".

## 2. Datum, scale, orientation
North is up. No camera move.
| State | Box | viewBox | Px per map unit | Used |
|---|---|---|---|---|
| EAST (shared with `g-a5s04-berne` and `g-a5s10-alert`) | left 716, top 62, 1080 x 450 | `330 284 384 160` | 2.8125 (screen x = 2.8125u - 212.125, y = 2.8125u - 736.75) | whole comp |
Underline box, measured on the crop by a row and column scan: line 4 is y 119 to 148 (line 5 starts at y 154); `three tornadoes had struck the city of Marion` is its words 3 to 10, crop x 205 to 994.
Clock hands, degrees clockwise from 12: 9:20 is hour 280, minute 120; 8:10 is hour 245, minute 60.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient (design sheet section 2), on from frame 0 |
| Map | BM-1 groups `map-neighbours`, `map-counties`, `map-state` inlined with ids prefixed `mrn-`; county lines 1.5 px, neighbour outlines 2 px, Indiana's outline 3 px, non-scaling. Every `pt-` group hidden except Fort Wayne, Marion and Linn Grove. Dot radius 6 px (`r` 2.133 map units), Body light. No county is lit |
| Fort Wayne | dot (1489.7, 98.6); label `Fort Wayne` left 1503, top 87. Town labels Arial 700 22 px, Body light |
| Path | one polyline in the map SVG, Body light 4 px, non-scaling, round joins: screen (1141.2, 420.6), (1305.2, 401.5), (1528.8, 329.5), (1611.5, 302.8). A 6 px open circle marks its start. Never red, no arrowhead |
| Marion | dot (1305.2, 379.0), 22.5 px north of the path; label `Marion` left 1317, top 350 |
| Linn Grove | dot (1528.8, 329.5); label `Linn Grove` right aligned to x 1600, top 345 (below the path, by hand) |
| `OHIO` | Arial 700 22 px, Label grey, tracking 6, left 1626, top 262 (east of the state line at x 1611.5) |
| Path caption | left 716, top 520, Arial 700 20 px, Label grey: `places the survey names · path schematic` |
| Clock stamp | design sheet section 8: glass card left 96, top 96, 590 x 200; `WEATHER BUREAU` / `9:20 PM` / `Fort Wayne, Indiana`; hands 280 and 120. In A5-S8 it slides to left 986 (x 986 to 1576), same top |
| Document card | design sheet section 9: left 96, top 560, 1480 x 397 (bottom 957); Beige polaroid border 10 px; the crop 1460 x 377 inside at (106, 570) |
| Underline | Popfig red 4 px, 2 px under the line box (the page is single-spaced; a 6 px line would touch line 5): screen x 311 to 1100, y 720 to 724 |
| Unlit page | Panel dark at 45 % over the whole crop except the box x 303 to 1108, y 685 to 722 |
| Document source | under the card, right aligned at x 1560, top 969: Arial 700 20 px, Body light with the credit shadow: `Weather Bureau survey report, 1965, p. 43` |
| `hit near 8:00 PM` chip | glass chip, height 46, padding 0 x 22, Arial 700 26 px, Body light, right aligned to x 1289, top 312 (west of and above Marion's dot, clear of the path) |
| Map dim | the whole map SVG to opacity 0.2; every map label, the caption and the chip to 0 |
| Hospital clock card | glass card left 96, top 96, 590 x 200, laid out as the stamp: face radius 62 centred (191, 196), `media/drawings/wall-clock.svg` inline, hands fixed at 245 and 60 from its first frame (they never sweep: the clock is stopped); eyebrow `STOPPED AT` at x 284, y 116; time `8:10 PM` at x 284, y 142, Courier New 700 84 px, Amber 2. No place line inside |
| Clock label | under the card, left 96, top 310, Arial 700 20 px, Body light with the credit shadow: `a hospital clock, Marion · Weather Bureau survey report, 1965, p. 45` (the survey's one source form, lead's ruling of 12 Oct 26; if the line runs past the card's right edge at x 686, break it after `Marion ·` into two lines) |
| Quote strip | as `g-a1s15-offices`: Beige polaroid, left 96, top 640, 1480 x 170; quote Georgia 52 px, Caption dark, with quotation marks; attribution Arial 700 22 px, Caption dark sub, tracking 2 |
The card and the strip end at x 1576: the presenter corner (x >= 1600, y >= 680) stays empty. The card (top 560) covers nothing of the map (bottom 512) or the caption (bottom 540).

## 4. Must be true in the picture
1. One path, in one colour, with no second or third track: the "three tornadoes" are the message's words on paper, not three drawn paths.
2. The path runs west to east: Howard County, past Marion, through Linn Grove, to the state line. It ends on the line. The caption `places the survey names · path schematic` is on screen whenever the path is at full strength.
3. The stamp reads `9:20 PM` with the hour hand a third of the way from 9 to 10 and the minute hand on the 4. No zone beside the time.
4. The card is the page's own image. The underline sits under `three tornadoes had struck the city of Marion` and stops before `with`; it does not touch the line below.
5. The hospital clock's hands show 8:10 (hour hand just past 8, minute hand on the 2) and never move. The clock card is on the left, the 9:20 stamp on the right, the same size and the same top.
6. The quote strip reads `“a full hour and twenty minutes earlier”` with the attribution `National Weather Service, Northern Indiana`. The narrator says "later"; the strip keeps the source's word.
7. Beat check: the crop is on screen 4.89 s (5.07 to 9.96) and changes at 6.03. The clock's time appears at 18.20 and holds 1.70 s.
8. Nothing of ours in x >= 1600, y >= 680; text at least 96 px from the sides and 54 px from top and bottom.
9. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.
10. No county label other than those the Picture note names. The label `HOWARD` is struck by the lead's ruling of 12 Oct 26: it is true (survey printed p. 45), but the study's hidden counties must stay hidden, and Howard shown west of Marion beside the county-seat hit would let a viewer place County B. Nothing replaces it: the path starts with no label at its west end.

## 5. Text (exact) and cues
Text: `Fort Wayne` · `Marion` · `Linn Grove` · `OHIO` · `places the survey names · path schematic` · `WEATHER BUREAU` · `9:20 PM` · `Fort Wayne, Indiana` · `Weather Bureau survey report, 1965, p. 43` · `hit near 8:00 PM` · `“a full hour and twenty minutes earlier”` · `National Weather Service, Northern Indiana` · `STOPPED AT` · `8:10 PM` · `a hospital clock, Marion · Weather Bureau survey report, 1965, p. 45`. Page words are the image.
Cue words and times are from `audio/a5-s7.words.json` and `audio/a5-s8.words.json` as they stood on 12 Oct 26. t from comp start = the segment's wav start inside the composition (`mg_specs/timeline-map.md` table 5: A5-S7 -0.23, A5-S8 9.96) plus the word's time; a segment's first word uses table 5's first sound (0.00, 9.96). Retime from the word, never from the seconds. The transcriber writes "nine twenty" as "920" and "eight ten" as "8" and "10.".
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A5-S7 | 0 | That | first sound 0.23 | 0.00 | first frame: ground, the map in EAST (lines only), Fort Wayne's dot and label, `OHIO` |
| 1 | A5-S7 | 2 | storm | 0.74 | 0.51 | the path draws west to east (1.2 s, `strokeDashoffset`, power1.inOut, to 1.71); Linn Grove's dot and label as the line reaches it |
| 2 | A5-S7 | 7 | Marion. | 2.08 | 1.85 | Marion's dot and label (0.3 s); the dot's stroke flashes Headline white once (stroke change); the path caption fades in |
| 3 | A5-S7 | 9 | 920 | 3.54 | 3.31 | clock stamp slides in from the left (`x: -660` to 0, 0.6 s, power3.out); the minute hand sweeps its last 30 degrees onto the 4 |
| 4 | A5-S7 | 16 | wire, | 5.30 | 5.07 | document card slides in from the right (`x: 660` to 0, 0.7 s, power3.out); the document source fades in after it |
| 5 | A5-S7 | 17 | three | 6.26 | 6.03 | unlit page fades in (0.4 s); the underline draws left to right (0.7 s) |
| 6 | A5-S8 | 0 | Marion | first sound 0.00 | 9.96 | the document source fades, the card leaves to the right (`x: 1600`, 0.4 s, power3.in); chip `hit near 8:00 PM` fades in beside Marion's dot (0.3 s) |
| 7 | A5-S8 | 7 | Fort | 2.54 | 12.50 | the map dims (0.4 s): map to 0.2, labels, caption and chip to 0; the stamp's three lines fade (0.15 s), the stamp slides to left 986 (0.5 s, power2.inOut), its lines return (0.2 s) |
| 8 | A5-S8 | 13 | full | 3.80 | 13.76 | quote strip rises in (`y: 40` to 0, 0.5 s, power3.out): the quote, then the attribution 0.2 s later |
| 9 | A5-S8 | 20 | clock | 6.26 | 16.22 | hospital clock card slides in from the left (`x: -660` to 0, 0.6 s, power3.out), hands already at 8:10, eyebrow `STOPPED AT`, no time yet |
| 10 | A5-S8 | 28 | 8 | 8.24 | 18.20 | `8:10 PM` fades in on the card (0.25 s); the clock label fades in under it. Hold to the last frame (19.90) |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a5s07-marion.html` is the only file the builder writes; `data-composition-id="g-a5s07-marion"`; id prefix `mrn-`; root `<div id="mrn-root" ...>` styled through `#mrn-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the map family base `compositions/g-a2s14-six.html` (brief `mg_specs/briefs/g-a2s14-six.md`) for the mount, the inlining and prefixing, the stamp and the paper card; the quote strip from `compositions/g-a1s15-offices.html`; the wall clock's inline mount from `compositions/g-a2s06-headstart.html`. The EAST state and the path construction are the same in `g-a5s10-alert`.
**Assets mounted (paths from the episode folder; sizes read from the files on 12 Oct 26):**
- `media/maps/indiana-counties.svg` (BM-1, viewBox 96 100 664 880, 70,592 bytes), inlined.
- `media/docs/survey-p43-920pm-crop.png` (PC-13, 1460 x 377).
- `media/drawings/wall-clock.svg` (DR-09, object box 124 x 124, viewBox -6 -6 136 136; `dw-hour` and `dw-minute` turn about (62, 62)), inlined for the hospital clock and, if the builder uses it for the stamp's face, twice with prefixed ids.
- `media/data/points.csv` is the source of the positions; it is read, not mounted.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a5s07-marion`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `graphics_qc` may flag two type sizes on the page card: the family's accepted flag (plan rule 10).

## 7a. Done line
All seven lines of template section 7a. Line 4 here: seek to 1.10 (path mid draw) and 12.90 (stamp mid slide, its lines hidden) forward and backward and match the frames. Line 6: the path's four points and every dot are computed from `media/data/points.csv`, the Howard County path and the section 2 numbers by a script and stated in the receipt.

## 8. Receipt
As template section 8, plus: the measured width of the clock label (if it runs past x 686, say so; do not shrink the type), and a frame at 7.00 showing the underline clear of line 5.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): EAST lines, Fort Wayne, `OHIO`, line weights. Then one settled frame per cue: 1.80 (path complete, Linn Grove, no county label anywhere), 2.40 (Marion and the caption), 4.10 (stamp at 9:20), 5.90 (card and source), 7.00 (underline complete, unlit page), 10.50 (card gone, `hit near 8:00 PM`), 13.50 (map dim, stamp on the right with its lines back), 14.60 (quote strip), 17.00 (clock card, hands at 8:10, no time), 18.60 (`8:10 PM` and the label), 19.80 (last frame).
