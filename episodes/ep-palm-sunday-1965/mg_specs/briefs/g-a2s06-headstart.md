Host: id=g-a2s06-headstart file=compositions/g-a2s06-headstart.html start=328.22 duration=17.66 s (timeline-map.md tables 1 and 5; last sound at 16.65) track=2

# g-a2s06-headstart · A2-S6, A2-S7 · two first touchdowns from two sources, and what a ten minute delay leaves of each head start (wave 1, clock family base)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 8, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). Two real county names are printed here, so neither `County A` nor `County B` may appear anywhere in this comp (rule 8). A flash is a stroke or fill change, never a scale pop (rule 12). Beat counts were held against the spoken windows when this brief was written (rule 13): A2-S7 carries six beats in 3.8 s, the closest two 0.14 s apart (a bar and its own label).
**Spoken (A2-S6):** "The Weather Service has the first Indiana tornado on the ground at five forty five, in Starke County. The nineteen sixty six study has the first touchdown at about six o'clock, in Marshall County."
**Spoken (A2-S7):** "A ten minute delay eats all of a two minute head start, and most of a seventeen minute one."
**One look:** two glass cards side by side, each a clock, a time, a county and its own source; then under each an amber bar of the same length, which swallows the short head start whole and covers most of the long one.

## 0. What this graphic claims
Two sources give two different first touchdowns: the National Weather Service has 5:45 PM in Starke County, the 1966 study has about 6:00 PM in Marshall County. They stay two figures. Against a delay of at least 10 minutes, the first leaves a head start of 2 minutes and the delay covers all of it; the second leaves 17 minutes and the delay covers most of it (10 of 17).

## 1. Source
- `edit_script.md` A2-S6, Rows [B table; IWX: "two minutes before the Koontz Lake tornado touched down"; table 2245 UTC = 5:45 PM EST] and [study printed p. 14: "approximately seventeen minutes before the first tornado touched down at Lapaz"; 5:43 plus 17 by the checker's script]. Picture note: left "5:45 PM · Starke County", source "National Weather Service, Northern Indiana"; right "about 6:00 PM · Marshall County", source "Disaster Research Center, 1966, p. 14".
- `edit_script.md` A2-S7, Rows [A6, F] (ten against two and against seventeen; recomputed by the fact check). Picture note: the amber bar "at least 10 minutes" laid against each.
- Both head starts are counted from the 5:43 PM warning of the comp before this one (`mg_specs/briefs/g-a2s03-chain.md`, clock at 5:43). The time 5:43 is not printed here; it is the angle each arc starts from.
- Clock face: `media/drawings/wall-clock.svg`, the face of design sheet section 8.

## 2. Datum, scale, orientation
One scale for both columns: 30 px per minute, left to right, each column starting at its card's left edge (x 96 and x 876). By script: 2 minutes is 60 px, 10 minutes is 300 px, 17 minutes is 510 px.
Clock angles, clockwise from 12 (by script): 5:45 is hour 172.5, minute 270; 6:00 is hour 180.0, minute 0; the left hands start at 5:40 (hour 170.0, minute 240) and the right at 5:55 (hour 177.5, minute 330). The 5:43 minute mark is 258 degrees; ten minutes is 60 degrees of the minute ring, so the delay arc on both faces runs 258 to 318.
Colours: ground `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`; Label grey `#93a3b2`; Body light `#dfe7ee`; Amber 2 `#e8c56a`; Panel dark `#15202b`; glass `rgba(10,16,24,0.55)` with `backdrop-filter:blur(18px) saturate(1.15)`, border `1px solid rgba(255,255,255,0.14)`, radius 28 (the stamp of `compositions/g-t1s2-warning.html`).

## 3. Geometry (screen px)
A2-S6:
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0, with the intro's faint sweep band (520 px wide, Label grey at 6 %, drifting left to right, ease none) for the whole window |
| Left card | glass card, left 96, top 150, 700 x 280 (right 796, bottom 430) |
| Left clock | `media/drawings/wall-clock.svg` inline, `translate(132 191) scale(1.6)`, `stroke-width="3.5"` on the group (box x 132 to 330.4, y 191 to 389.4; centre (231.2, 290.2)); hands end at 172.5 and 270 |
| Left time | `5:45 PM`, Courier New 700 84 px, Amber 2, left 376, top 236 (352.8 px wide by script, ends x 729) |
| Left place | `Starke County`, Arial 700 26 px, Body light, left 378, top 334 |
| Left source | design sheet section 10 type (Arial 700 22 px, `rgba(244,240,232,0.88)`, the credit shadow), left 96, top 444: `National Weather Service, Northern Indiana` |
| Right card | glass card, left 876, top 150, 700 x 280 (right 1576, bottom 430) |
| Right clock | the same drawing, `translate(912 191) scale(1.6)` (centre (1011.2, 290.2)); hands end at 180.0 and 0 |
| Right `about` | `about`, Arial 700 26 px, Body light, left 1158, top 196 (the eyebrow slot; the left card leaves this slot empty) |
| Right time | `6:00 PM`, same type as the left time, left 1156, top 236 (ends x 1509) |
| Right place | `Marshall County`, same type as the left place, left 1158, top 334 |
| Right source | same type, left 876, top 444: `Disaster Research Center, 1966, p. 14` |

A2-S7 (the cards stay):
| Element | Px |
|---|---|
| Delay arc, each face | circle arc, centre the face's centre, radius 113, from 258 to 318 degrees (118.3 px long by script), Amber 2, 10 px, round caps, grown clockwise with `strokeDashoffset`. Left: it passes the minute hand at 270 after 12 degrees. Right: it stops 42 degrees short of the minute hand |
| Left amber bar | rect x 96 to 396, y 652 to 688 (300 x 36), Amber 2, grown from its left end with `scaleX` |
| Left bar label | `at least 10 minutes`, Arial Black 900 30 px, Amber 2, left 96, top 718 |
| Left head start | outline rect x 96 to 156, y 642 to 698 (60 x 56), 3 px Body light, no fill, drawn over the bar |
| Left head start label | `2 minute head start`, Arial Black 900 30 px, Body light, left 96, top 590 |
| Right amber bar | rect x 876 to 1176, y 652 to 688, same fill |
| Right bar label | `at least 10 minutes`, same type, left 876, top 718 |
| Right head start | outline rect x 876 to 1386, y 642 to 698 (510 x 56), same stroke |
| Right head start label | `17 minute head start`, same type, left 876, top 590 |

## 4. Must be true in the picture
1. Two figures, never one: no line, arrow, bracket or bar joins the two cards, and no difference between 5:45 and 6:00 is printed. Each source line sits under its own card and nowhere else.
2. `about` is on the right card only. The left time is `5:45 PM` with no qualifier.
3. Both amber bars are 300 px and both sit on the 30 px per minute scale: the left head start is 60 px, the right 510 px. Bar to head start is 5.0 on the left (the head start is wholly inside the bar) and 0.588 on the right (210 px of the outline stay empty).
4. The empty 210 px carry no label and no number. Neither "7 minutes" nor "5:43" is printed.
5. Both delay arcs span 60 degrees from 258. On the left the arc runs past the minute hand; on the right it ends before it. Hands: left 172.5 and 270, right 180.0 and 0.
6. No town is named (not Koontz Lake, not Lapaz): the Picture note gives counties only. No `County A`, no `County B`.
7. Each card lands on its own sentence: nothing of the right column is on screen before "nineteen sixty six" (6.13).
8. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680. No label under a bar, an outline, an arc or a hand.

## 5. Text (exact) and cues
Text: `5:45 PM` · `Starke County` · `National Weather Service, Northern Indiana` · `about` · `6:00 PM` · `Marshall County` · `Disaster Research Center, 1966, p. 14` · `at least 10 minutes` (twice, one per bar) · `2 minute head start` · `17 minute head start`.
Cue words and times are from `audio/a2-s6.words.json` (31 words) and `a2-s7.words.json` (19 words), read on 12 Oct 26. t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A2-S6 -0.47, A2-S7 11.44) plus the word's time; a segment's first word uses the table's "first sound" (0.00, 11.69). Retime from the word, never from the seconds. The transcript writes numbers as figures ("545", "1966", "6", "10", "2", "17"): the index is what counts.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A2-S6 | 0 | The | 0.47 | 0.00 | first frame: ground and sweep band only |
| 1 | A2-S6 | 1 | Weather | 0.56 | 0.09 | the left card slides in from the left (`x:-800` to 0, 0.6 s, power3.out) with its clock, hands at 5:40, no time yet; its source line fades in at 0.29 ("Service", index 2) with `y:12` to 0 |
| 2 | A2-S6 | 12 | 545 | 3.48 | 3.01 | the left minute hand sweeps 240 to 270 and the hour hand 170.0 to 172.5 (0.5 s, power3.out); `5:45 PM` lands (0.3 s fade) |
| 3 | A2-S6 | 14 | Stark | 4.98 | 4.51 | `Starke County` fades in (0.3 s, `y:12` to 0) |
| 4 | A2-S6 | 17 | 1966 | 6.60 | 6.13 | the right card slides in from the right (`x:1100` to 0, 0.6 s, power3.out) with its clock, hands at 5:55; its source line fades in at 6.91 ("study", index 18) |
| 5 | A2-S6 | 24 | about | 9.42 | 8.95 | `about` fades in (0.2 s) |
| 6 | A2-S6 | 25 | 6 | 9.60 | 9.13 | the right minute hand sweeps 330 to 360 and the hour hand 177.5 to 180.0 (0.5 s); `6:00 PM` lands |
| 7 | A2-S6 | 29 | Marshall | 10.68 | 10.21 | `Marshall County` fades in |
| 8 | A2-S7 | 1 | 10 | 0.38 | 11.82 | left column: the amber bar grows x 96 to 396 and the left face's delay arc grows 258 to 318, together (0.78 s, ease none, done at 12.60 on "eats") |
| 9 | A2-S7 | 2 | minute | 0.60 | 12.04 | left bar label `at least 10 minutes` lands (0.3 s, `y:16` to 0 with the fade) |
| 10 | A2-S7 | 8 | 2 | 2.02 | 13.46 | the left head start outline draws on (0.3 s) over the bar's first 60 px; `2 minute head start` fades in |
| 11 | A2-S7 | 12 | and | 3.54 | 14.98 | right column: the amber bar grows x 876 to 1176 and the right face's delay arc grows 258 to 318 (0.5 s, ease none, done at 15.48) |
| 12 | A2-S7 | 13 | most | 3.68 | 15.12 | right bar label `at least 10 minutes` lands |
| 13 | A2-S7 | 16 | 17 | 4.16 | 15.60 | the right head start outline draws on left to right (0.5 s), running 210 px past the bar's end; `17 minute head start` fades in. Hold to 17.66 |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a2s06-headstart.html` is the only file the builder writes; `data-composition-id="g-a2s06-headstart"`, `data-duration="17.66"`; id prefix `hds-`; root `<div id="hds-root" ...>` styled through `#hds-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0. The host is already mounted in `index.html` as `host-a2s06-headstart`; do not edit `index.html`.
**It is a family base.** Keep the clock (the inlined drawing, a `hands(hourDeg, minuteDeg)` setter with `svgOrigin` set once at timeline 0) and the arc (`arc(cx, cy, r, fromDeg, toDeg)` returning a path, grown with `strokeDashoffset`) as plain, separately named blocks. Later comps that copy it: `compositions/g-a3s12-seven.html` (wave 3: two faces, 7:00 and 7:45, an arc between) and `compositions/g-a5s07-marion.html` (wave 4: a clock stopped at 8:10); the arc is the one `compositions/g-a2s03-chain.html` and `compositions/g-a2s11-backup.html` (wave 2) share: same face scale 1.6, radius 113, 10 px, round caps. It is sent alone for a full-size read before anyone copies it.
**What it copies:** the glass card and the hand sweep of the built `compositions/g-t1s2-warning.html`.
**Assets (paths from the episode folder; confirmed on disk 12 Oct 26):**
- `media/drawings/wall-clock.svg` (object 124 x 124, viewBox -6 -6 136 136, file 136 x 136, line 4, ticks 3, hands 5; `dw-hour` and `dw-minute` point at 12, carry no transform and turn about (62, 62)), inlined twice, ids under `hds-`. Mount rules in `media/drawings/README.md`, which wins over any number here.
No page crop, map or film cut is mounted.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a2s06-headstart`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 2 here: state the measured fill for 0.7 to 6.1 (one card alone) as well as for the whole comp. Line 4 here: hand rotations, `svgOrigin`, each bar's `scaleX` and each arc's dash are set at timeline 0. Line 6 here: the three bar lengths from the 30 px per minute scale, the eight hand angles and the arc's two angles are computed by a script and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): ground only. Then settled frames: 1.00 (left card, clock at 5:40, source line, no time), 3.80 (`5:45 PM`, hands at 5:45), 5.00 (`Starke County`), 7.40 (right card and its source, hands at 5:55, no time), 9.80 (`about` over `6:00 PM`), 10.80 (`Marshall County`; two cards, nothing joining them), 12.20 (left bar and arc part way), 12.90 (left bar full, arc past the minute hand, bar label), 13.90 (60 px outline inside the bar, `2 minute head start`), 15.30 (right bar part way), 16.30 (right bar full, 510 px outline with 210 px empty, both labels, arc short of the minute hand), 17.50 (hold).
