Host: id=g-a2s06-headstart file=compositions/g-a2s06-headstart.html start=328.22 (timeline-map.md) duration=17.66 s (wav sum 17.27 s plus gaps from timeline-map.md) track=2

# g-a2s06-headstart · A2-S6, A2-S7 · two clocks, two head starts, one delay (wave 1, base of the clock family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 8, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21; section 3a row DR-09.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1; the built hook comps' `fromTo` at a cue is not copied). The root is styled through its id and is never `id="root"` (rule 3). A flash is a stroke or fill change, never a scale pop (rule 12). A beat count is checked against its spoken window when the brief is written (rule 13: done in section 5). A shared drawing is read alone at the size it is mounted (rule 11: the clock face at 186 px).
**Spoken (A2-S6):** "The Weather Service has the first Indiana tornado on the ground at five forty five, in Starke County. The nineteen sixty six study has the first touchdown at about six o'clock, in Marshall County."
**Spoken (A2-S7):** "A ten minute delay eats all of a two minute head start, and most of a seventeen minute one."
**One look:** two panels that never touch, a clock in each; then the same amber bar under both, longer than one head start and most of the other.

## 0. What this graphic claims
Two sources give two different first touchdowns: the Weather Service has 5:45 PM in Starke County, the 1966 study has about 6:00 PM in Marshall County. Measured from the 5:43 PM warning that is a head start of 2 minutes or of 17. A delay of at least 10 minutes covers all of the first and most of the second.

## 1. Source
- `edit_script.md` A2-S6, Rows [B table; IWX: "two minutes before the Koontz Lake tornado touched down"; table 2245 UTC = 5:45 PM EST] · [study printed p. 14: "approximately seventeen minutes before the first tornado touched down at Lapaz"; 5:43 plus 17 by the checker's script]. Picture note: left "5:45 PM · Starke County", source "National Weather Service, Northern Indiana"; right "about 6:00 PM · Marshall County", source "Disaster Research Center, 1966, p. 14"; "Each lands on its own sentence. They are not merged into one figure."
- `edit_script.md` A2-S7, Rows [A6, F] (ten against two and against seventeen; recomputed by the fact check). Picture note: the amber bar "at least 10 minutes" is laid against each; it covers all of the left card's two minutes and most of the right card's seventeen.
- The delay itself: `edit_script.md` A2-S5, "the delay was generally at least ten minutes" (study printed p. 14), shown in the comp before this one.
- Drawing: `media/drawings/wall-clock.svg` (DR-09; object box 124 x 124, viewBox -6 -6 136 136, line 4, ticks 3, hands 5; `dw-hour` and `dw-minute` turn about (62, 62)).

## 2. Datum, scale, orientation
- **Bars: 40 px per minute, the same in both panels,** measured to the right from a zero tick that stands for the 5:43 PM warning. 2 minutes = 80 px, 17 minutes = 680 px, 10 minutes = 400 px. The amber bar is 400 px in both panels. It covers 80 of 80 px on the left (all) and 400 of 680 px on the right (58.8 %, 10 of 17: "most").
- Clock hands, clockwise degrees from 12: 5:45 is hour 172.5, minute 270. 6:00 is hour 180, minute 0.
- Two panels of one size, side by side, 48 px apart. Both end left of x 1600, so the presenter corner is empty whatever their height.

## 3. Geometry (screen px)
Ground: the canvas gradient (design sheet section 2) on the root, on from frame 0.
Each panel is a glass card (tokens.md "Surfaces"), 720 x 560, top 240 (bottom 800). Left panel L = 96 (x 96 to 816); right panel L = 864 (x 864 to 1584).
| Element | Left panel | Right panel | Style |
|---|---|---|---|
| Clock face | object box top left (126, 284), centre (219, 377) | (894, 284), centre (987, 377) | `wall-clock.svg` inline in a full-frame `<svg>`, `<g transform="translate(X Y) scale(1.5)">`: 186 px wide, lines 6 px on screen. Rim fill Panel dark. Hands hidden until the time lands |
| Word above the time | none | `about` at left 1104, top 284 | Arial 700 34 px, Body light |
| Time | `5:45 PM` at left 336, top 318 | `6:00 PM` at left 1104, top 318 | Courier New 700 104 px, Amber 2, `letter-spacing:-5px`, `line-height:1`; 401.8 px wide (ends x 737.8 and 1505.8) |
| Place | `Starke County` at left 338, top 436 | `Marshall County` at left 1106, top 436 | Arial 700 34 px, Body light |
| Source | `National Weather Service, Northern Indiana` at left 126, top 502 | `Disaster Research Center, 1966, p. 14` at left 894, top 502 | Arial 700 22 px, `rgba(244,240,232,0.88)`, `letter-spacing:0.04em` (design sheet section 10 type, here inside the panel) |
| Rule | y 544, x 116 to 796 | y 544, x 884 to 1564 | 1 px, `rgba(255,255,255,0.14)`. On from frame 0 with the panel |
| Zero tick | x 116, y 612 to 736 | x 884, y 612 to 736 | 3 px, Body light, round caps |
| Tick label | `5:43 PM warning` at left 116, top 748 | the same words at left 884, top 748 | Arial 700 22 px, Label grey |
| Head start label | `2 minute head start` at left 116, top 574 | `17 minute head start` at left 884, top 574 | Arial 700 28 px, Body light |
| Head start bar | x 116 to 196 (80 px), y 620 to 668 | x 884 to 1564 (680 px), y 620 to 668 | 3 px Body light outline drawn inside the box, fill Panel dark |
| Amber wash on the head start bar | x 116 to 196 (all 80 px) | x 884 to 1284 (400 of 680 px) | Amber 2 at 45 %, inside the outline, grown from the left with `scaleX` (`transformOrigin:"left center"`) |
| Delay bar | x 116 to 516 (400 px), y 680 to 728 | x 884 to 1284 (400 px), y 680 to 728 | fill Amber 2, grown from the left with `scaleX` |
| Delay label | `at least 10 minutes` at left 132, centred on y 704 | the same words at left 900 | Arial 700 24 px, Caption dark, on the amber |

Frame source line (A2-S7 only): design sheet section 10, left 96, bottom 60: `Delay: Disaster Research Center, 1966, p. 14`.
Waiting state: from frame 0 both panels are on (glass, rule, clock face without hands). The right panel sits at opacity 0.45 until its sentence. An empty panel makes no claim; it keeps the frame from standing half empty for six seconds (`references/mg-quickref.md` "Frame coverage").

## 4. Must be true in the picture
1. **Two accounts, never one figure.** No line, arrow, bracket, average or shared axis joins the panels. Each time has its own source line inside its own panel. Nothing says which is right.
2. The left clock reads 5:45 (hour hand just short of 6, minute hand on 9) and the right clock 6:00 (hour hand on 6, minute hand on 12). The word `about` stands above `6:00 PM` and nothing like it stands on the left.
3. The counties are `Starke County` and `Marshall County`, spelled so (the transcriber writes "Stark"). No town is named: Koontz Lake and Lapaz are not on screen.
4. One scale for every bar: 40 px per minute. Head starts 80 px and 680 px; the amber delay bar 400 px in both panels, pixel for pixel the same length.
5. The amber wash covers the whole of the 2 minute bar and 400 of the 680 px of the 17 minute bar: 280 px of the right bar stay Panel dark. The picture never prints a figure for what is left.
6. Every bar starts on its zero tick, and the tick is labelled `5:43 PM warning`. The delay is `at least 10 minutes`, never "10 minutes" alone.
7. Each time lands on its own sentence: nothing of the right panel's text is on before A2-S6 word 17, and no bar is on before A2-S7.
8. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680 (the right panel ends at x 1584).

## 5. Text (exact) and cues
Text: `5:45 PM` · `Starke County` · `National Weather Service, Northern Indiana` · `about` · `6:00 PM` · `Marshall County` · `Disaster Research Center, 1966, p. 14` · `5:43 PM warning` (twice) · `2 minute head start` · `17 minute head start` · `at least 10 minutes` (twice) · `Delay: Disaster Research Center, 1966, p. 14`.
Cue words and times are from `audio/a2-s6.words.json` and `audio/a2-s7.words.json` as they stood on 12 Oct 26 at 18:55, after the voice conversion's re-transcription (wavs 11.721 s and 5.551 s, sum 17.27 s). "t from comp start" is `mg_specs/timeline-map.md` table 5: the segment's "wav start inside the composition" (A2-S6 -0.47, A2-S7 11.44) plus the word's time; a segment's first word takes the "first sound" column (0.00 and 11.69). The gaps are therefore already in the last time column. Retime from the word, never from the seconds.
Beat check (rule 13): A2-S7 holds five beats in 4.53 s of speech (11.69 to 16.22), the shortest gap 0.40 s (steps 10 to 11); each beat below is 0.3 to 0.5 s long, so none is still moving when the next starts except where stated.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A2-S6 | 0 | The | 0.00 | 0.00 | first frame: ground; both panels with rule and clock face, no hands; the right panel at opacity 0.45 |
| 1 | A2-S6 | 1 | Weather | 0.56 | 0.09 | left source line fades in (0.3 s) |
| 2 | A2-S6 | 12 | 545 | 3.48 | 3.01 | left hands appear (0.15 s fade): hour at 172.5, minute sweeps from 240 to 270 (0.5 s, power3.out); `5:45 PM` lands (`y:16` set at 0, then `to y:0, autoAlpha:1`, 0.35 s, power3.out). The transcriber writes "545" |
| 3 | A2-S6 | 14 | Stark | 4.98 | 4.51 | `Starke County` rises (`y:16` set at 0, then `to`, 0.3 s) |
| 4 | A2-S6 | 17 | 1966 | 6.60 | 6.13 | right panel to opacity 1 (0.3 s); right source line fades in with it |
| 5 | A2-S6 | 24 | about | 9.42 | 8.95 | `about` fades in (0.2 s) |
| 6 | A2-S6 | 25 | 6 | 9.60 | 9.13 | right hands appear: hour at 180, minute sweeps from 330 to 360 (0.5 s, power3.out); `6:00 PM` lands (as step 2) |
| 7 | A2-S6 | 29 | Marshall | 10.68 | 10.21 | `Marshall County` rises (as step 3) |
| 8 | A2-S7 | 0 | A | 0.00 | 11.69 | both zero ticks draw (0.25 s) and both `5:43 PM warning` labels fade in; the frame source line fades in |
| 9 | A2-S7 | 1 | 10 | 0.38 | 11.82 | both delay bars grow from their ticks at once (`scaleX` 0 to 1, 0.5 s, power2.out); both `at least 10 minutes` labels fade in over the last 0.2 s |
| 10 | A2-S7 | 8 | 2 | 2.02 | 13.46 | left head start bar grows (0.3 s) and `2 minute head start` fades in |
| 11 | A2-S7 | 10 | head | 2.42 | 13.86 | amber wash covers all of the left head start bar (0.3 s, ease none) |
| 12 | A2-S7 | 16 | 17 | 4.16 | 15.60 | right head start bar grows (0.5 s, power2.out) and `17 minute head start` fades in |
| 13 | A2-S7 | 18 | one. | 4.78 | 16.22 | amber wash covers 400 of the right bar's 680 px (0.4 s, ease none). Hold to the last frame (17.66) |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a2s06-headstart.html` is the only file the builder writes; `data-composition-id="g-a2s06-headstart"`; id prefix `hs-`; root `<div id="hs-root" ...>` styled through `#hs-root` (plan rule 3 overrides the template's `id="root"`). Full frame, opaque, own ground on from frame 0.
**This comp is a family base (clock family).** Later comps copy from it once it has passed its read: `g-a3s12-seven` (wave 3: two clock faces and the span between them) and `g-a5s07-marion` (wave 4: a stopped clock beside a stamp), both named in `acts-plan.md` section 2 "Reuses". What they take: the panel with an inline `wall-clock.svg` at 1.5, the hands set by `rotation` with `svgOrigin`, the Courier time, and the bars on a stated px-per-minute scale. Keep the panel and the bar row in their own blocks of CSS and markup so they lift out whole. Send it alone for a full-size read before anything copies it (template section 7a, last line). The clock face it starts from is the built `compositions/g-t1s2-warning.html` (same face, drawn there by script); here the face is the drawing file.
Hands: copy the file's `<g class="dw-clock">` into the comp's SVG, give `dw-hour` and `dw-minute` ids, and set `svgOrigin` once at build, before any tween, in the SVG's own user units: the face centre in screen px (219, 377) and (987, 377). The hub is a zero-length line: fade it, never draw it on.
**Assets mounted (paths from the episode folder):**
- `media/drawings/wall-clock.svg` (DR-09, object box 124 x 124, viewBox -6 -6 136 136), inlined twice at scale 1.5.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a2s06-headstart`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `python3`, never `python`.

## 7a. Done line
All seven lines of template section 7a. Line 2 (fill): the two panels cover x 96 to 1584, y 240 to 800; the empty bands are 22.2 % of the frame above and 25.9 % below. Line 6: the six bar lengths (80, 680, 400, 400 and the two washes 80, 400) are computed from the minutes by a script at 40 px per minute, measured on a frame with `getBoundingClientRect`, and stated in the receipt. Line 7 does not apply: the comp is opaque.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): two panels, two faces without hands, right panel dim, no text. Then one settled frame per cue: 0.60 (left source), 3.70 (5:45, hands at 172.5 and 270), 5.00 (Starke County), 6.60 (right panel full, its source), 9.05 (`about` alone, no time yet), 9.80 (6:00, hands at 180 and 0), 10.70 (Marshall County), 11.78 (ticks and labels, no bar), 12.50 (both delay bars, equal length), 13.80 (2 minute bar, not yet washed), 14.30 (left bar fully amber), 16.10 (17 minute bar, not yet washed), 16.80 (right wash stops at x 1284), 17.60 (last frame). Each cue second in both seek orders.
