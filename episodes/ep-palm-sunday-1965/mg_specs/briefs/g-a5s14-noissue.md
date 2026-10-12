Host: id=g-a5s14-noissue file=compositions/g-a5s14-noissue.html start=942.11 (timeline-map.md table 1; the mount in index.html wins) duration=6.15 s track=2

# g-a5s14-noissue · A5-S14 · "No issuances ... due to power failure." (wave 4, page family, tempo 0.85)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 8, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, and section 3c row PC-14. Times: `mg_specs/timeline-map.md` tables 1 and 5. Base: `mg_specs/briefs/g-a2s15-old.md` (page card) and `mg_specs/briefs/g-a1s01-kc.md` (stamp).
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id, never `root` (rule 3). No page crop holds past about 8 s without a visible change (rule 7). A flash is a stroke or fill change, never a scale pop (rule 12).
**Spoken (A5-S14):** ""No issuances between nine thirty and ten thirty, due to power failure.""
**One look:** the page's own line, underlined in red, and the room going dark round it.

## 0. What this graphic claims
The Fort Wayne Weather Bureau's log prints one line for the hour from 9:30 PM to 10:30 PM: no issuances, due to power failure.

## 1. Source
- `edit_script.md` A5-S14, Rows [A23; survey printed p. 44].
- Crop: `media/docs/survey-p44-nowarn-crop.png` (1460 x 591, cut from `media/docs/survey-pdf-72-orig.png`, survey printed p. 44; read by eye 12 Oct 26). It reads, top to bottom: the heading `FORT WAYNE (Continued)`; `No issuances between 9:30 PM EST and 10:30 PM EST due to power failure.`; a row of asterisks; then the whole entry `Issued at 10:45 PM EST.` (eight lines, an all clear statement that names Van Wert, Ohio). The page has no entry above the line.

## 2. Datum, scale, orientation
The crop is mounted at its own size, 1460 px wide. Boxes measured on the file by a row and column scan:
| Line | Px inside the crop | Screen px (crop at 106, 126) |
|---|---|---|
| `FORT WAYNE (Continued)` | x 31 to 510, y 24 to 58 | x 137 to 616, y 150 to 184 |
| `No issuances between 9:30 PM EST and 10:30 PM EST due to power failure.` | x 38 to 1340, y 108 to 137 | x 144 to 1446, y 234 to 263 |
| asterisks and the 10:45 PM entry | y 160 to 591 | y 286 to 717 |
Clock angles, clockwise degrees from 12: 9:30 PM is hour hand 285, minute hand 180.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0 |
| Document card | design sheet section 9: left 96, top 116, 1480 x 611 (right 1576, bottom 727), Beige polaroid border 10 px, its shadow; the crop at (106, 126). On from frame 0 (the cut lands on the page) |
| Unlit page | one Panel dark rect at 45 %, screen x 106 to 1566, y 286 to 717 (the asterisks and the 10:45 PM entry), on from frame 0. The heading and the line stay bright |
| Underline | Popfig red, 6 px, screen x 144 to 1446, y 267 to 273 (4 px under the line box); `scaleX` 0 to 1 from the left |
| Dark | two layers that rise together: the unlit rect goes from 45 % to 92 %; a second Panel dark rect, screen x 106 to 1566, y 126 to 226 (the heading), goes 0 to 92 %; and a full-frame scrim above the ground and the card's border, `rgba(3,5,8,0.80)`, with a hole over screen x 126 to 1466, y 228 to 280 (built as four rects round the hole). The line and its underline stay at full brightness |
| Clock stamp | the stamp of `g-a1s01-kc.md` (590 x 200) at left 96, top 780 (bottom 980): eyebrow `WEATHER BUREAU`, time `9:30 PM`, place line `Fort Wayne, Indiana`; hour hand 285, minute hand 180. It sits above the dark scrim |
| Hour arc | on the clock face's ring, Amber 2, 6 px, a full circle drawn clockwise from 180 degrees (the half past mark) back to it, `strokeDashoffset` |
| Page source | design sheet section 10, left 720, bottom 60 (right of the stamp, left of x 1600): `Weather Bureau survey report, 1965, p. 44` |

## 4. Must be true in the picture
1. The underlined words are the page's own line; nothing on the card is retyped.
2. The line is on screen and lit on every frame; the dark never covers it.
3. The clock reads 9:30 PM, Fort Wayne. The arc is one full hour.
4. The 10:45 PM entry is never brighter than the line and is never underlined.
5. A visible change at least every 2 s: underline, stamp, arc, dark.
6. Nothing in x >= 1600 and y >= 680; the card ends at x 1576 and the stamp at x 686.

## 5. Text (exact) and cues
Text: `WEATHER BUREAU` · `9:30 PM` · `Fort Wayne, Indiana` · `Weather Bureau survey report, 1965, p. 44`. Page words are the image.
t from comp start = the segment's wav start inside the composition (timeline-map.md table 5: 0.15) plus the word's time; the first word uses table 5's first sound (0.57). The comp starts on the cut out of Paul's clip, so the voice follows the picture.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | cut | | | | 0.00 | first frame: card, unlit page at 45 %, page source |
| 1 | A5-S14 | 0 | No | 0.00 | 0.57 | underline starts: `scaleX` 0 to 1 over 4.0 s, `ease:"none"`, so it runs with the voice |
| 2 | A5-S14 | 4 | 930 | 1.68 | 1.83 | clock stamp slides in from the left (`x:-700` set at 0, to 0; 0.6 s, power3.out) |
| 3 | A5-S14 | 6 | 1030 | 2.64 | 2.79 | the hour arc draws once round the face (0.9 s, `ease:"none"`) |
| 4 | A5-S14 | 7 | due | 3.38 | 3.53 | the dark rises (0.9 s, power2.inOut): the page round the line and the frame go almost black |
| 5 | A5-S14 | 10 | failure. | 4.42 | 4.57 | underline complete; hold |
| 6 | end | | | | 6.15 | comp ends on the dark frame; no exit move |

## 6. Contract
As `references/mg-brief-template.md` section 6, with plan rule 3 over its `id="root"`. File the builder may write: `compositions/g-a5s14-noissue.html` only. Id prefix `noiss-`, root id `noiss-root`. Bases it copies: the page card of `compositions/g-i1s6-page.html` (built) and the stamp of `compositions/g-a1s01-kc.html` (wave 1). Assets mounted: `media/docs/survey-p44-nowarn-crop.png` (1460 x 591); `media/drawings/wall-clock.svg` inline for the face. No later composition copies this one.

## 7. Tools
As the template's section 7.

## 7a. Done line
As the template's section 7a, all seven. Fill: state the card's share of the frame. `graphics_qc` flat type: a page crop is one of the plan's rule 10 cases.

## 8. Receipt
As the template's section 8, plus: the measured brightness of the 10:45 PM entry against the line on the last frame (read on a frame), and whether the hole's edges touch any ink of the heading or the asterisks.

## Frames the verifier reads
First frame 0.00 and the frame after it (0.04); 1.20 (underline part drawn); 2.50 (stamp settled); 3.40 (arc part drawn); 4.60 (dark settled, underline complete); last frame 6.05. On each: section 4 item 2 first.
