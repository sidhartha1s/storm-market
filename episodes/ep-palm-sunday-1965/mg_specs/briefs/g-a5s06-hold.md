Host: id=g-a5s06-hold file=compositions/g-a5s06-hold.html start=864.88 (timeline-map.md table 1; the mount in index.html wins) duration=15.98 s track=2

# g-a5s06-hold · A5-S6 · "Hold the line a minute": Fort Wayne types at 9:00 PM (wave 4, photograph family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 3, 4, 8, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, and section 3e row PT-10. Times: `mg_specs/timeline-map.md` tables 1 and 5. Base: `mg_specs/briefs/g-a1s01-kc.md` (stamp over a photograph).
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id, never `root` (rule 3). A photograph's label names what the photograph shows (rule 5). A flash is a stroke or fill change, never a scale pop (rule 12).
**Spoken (A5-S6):** "At nine o'clock Fort Wayne typed, "Hold the line a minute for a definite report on tornado at Berne." It had hit, the office said, ten to fifteen minutes ago. Several houses were destroyed, it typed, and ambulances were rushing to the scene."
**One look:** a teletype operator at his machine, a clock at 9:00, and the office's own typed words lifted onto paper.

## 0. What this graphic claims
At 9:00 PM the Fort Wayne Weather Bureau typed a message asking stations to hold for a report of a tornado at Berne that had already hit 10 to 15 minutes before.

## 1. Source
- `edit_script.md` A5-S6, Rows [A21; survey printed p. 43: "several houses destroyed and ambulances are rushing to scene"]. The first quote is the script's spoken quotation of the same entry.
- Ground: `media/stills/a5-teletype-room-1947.jpg` (1820 x 1220, inventory A5). It shows a teletype operator about 1947, seen from behind and in profile: not Fort Wayne, not 1965. The place and time live on the glass stamp, never bare on the photograph.

## 2. Datum, scale, orientation
- The photograph at cover is enlarged 1.0549 times (1920 x 1287, top -103.5) and loses 16.1 % of its height. On top of that the `<img>` runs scale 1.06 to 1.11 about the frame centre over the whole comp, `ease:"none"`: at 1.06 the scan's pale left border (file x 0 to 50) is already off screen.
- The operator's head and face are file x 310 to 545, y 100 to 385: screen x 289 to 552, y -30 to 288 at scale 1.06, and x 257 to 533, y -57 to 277 at 1.11. Nothing of ours enters x 240 to 570, y 0 to 300.
- Clock angles are clockwise degrees from 12: 9:00 PM is hour hand 270, minute hand 0.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | `<img src="media/stills/a5-teletype-room-1947.jpg">`, left 0, top 0, 1920 x 1080, `object-fit:cover; object-position:50% 50%`, scale 1.06 to 1.11 by GSAP only. Behind it the canvas gradient. On from frame 0 |
| Scrim | `.dim` under this comp's own class name, full frame, `rgba(3,5,8,0.45)`, on from frame 0 |
| Caption | credit corner, left 96, bottom 60, design sheet section 10 type: `Teletypes and operator, about 1947 · NOAA`. On from frame 0 |
| Clock stamp | the stamp of `g-a1s01-kc.md` (glass plate 590 x 200, same inner offsets) moved to left 1234, top 96 (right 1824, bottom 296): it covers the cable board, no face. Eyebrow `WEATHER BUREAU`, time `9:00 PM`, place line `Fort Wayne, Indiana`. Face `media/drawings/wall-clock.svg` values as the base; hour hand 270, minute hand 0 |
| Arc | on the clock face's ring (radius 62), Amber 2, 6 px, from 270 degrees to 360 degrees (8:45 to 9:00), drawn with `strokeDashoffset` |
| Arc label | glass chip under the stamp, left 1234, top 312, height 46, padding 0 x 22, Arial 700 26 px, Body light: `it hit 10 to 15 minutes before` |
| Quote strip | Beige polaroid, left 96, top 700, 1480 x 200 (right 1576, bottom 900), the document card's shadow. It covers the operator's lap, the chair and the keyboards, no face |
| Quote 1 | Georgia 40 px, Caption dark, left 136, two lines, line height 52 px, tops 724 and 776: `“Hold the line a minute for a definite` / `report on tornado at Berne.”` Three pre-authored spans: `“Hold the line a minute`, ` for a definite report`, ` on tornado at Berne.”` |
| Quote 2 | same type and place, pre-authored, hidden: `“several houses destroyed and` / `ambulances are rushing to scene”`. Two spans, split before `ambulances` |
| Attribution | Arial 700 22 px, Caption dark sub, tracking 2, left 136, top 848: `Weather Bureau, Fort Wayne · 9:00 PM` |

## 4. Must be true in the picture
1. The clock reads 9:00 PM and the stamp says Fort Wayne; neither word sits bare on the photograph.
2. The photograph is never on screen without its own caption.
3. Nothing of ours covers the operator's head (section 2 box) at any scale of the push.
4. Quote 2 is the survey's wording as the script's Rows line gives it, with "are rushing to scene"; it is not the narrator's sentence.
5. The arc says when the tornado hit relative to 9:00 PM (a quarter of the face, ending at 12). No time is printed for the hit.
6. Nothing in x >= 1600 and y >= 680; the strip ends at x 1576.
7. Nothing appears before its spoken word.
8. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). It holds without staging: the photograph fills the frame from the first frame to the last.

## 5. Text (exact) and cues
Text: `WEATHER BUREAU` · `9:00 PM` · `Fort Wayne, Indiana` · `it hit 10 to 15 minutes before` · the two quotes above · `Weather Bureau, Fort Wayne · 9:00 PM` · `Teletypes and operator, about 1947 · NOAA`.
t from comp start = the segment's wav start inside the composition (timeline-map.md table 5: -0.43) plus the word's time; the first word uses table 5's first sound.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A5-S6 | 0 | At | 0.00 | 0.00 | first frame: photograph, scrim, caption; the push starts |
| 1 | A5-S6 | 1 | 9 | 0.54 | 0.11 | clock stamp slides in from the right (`x:700` set at 0, to 0; 0.6 s, power3.out); the minute hand sweeps its last 30 degrees to 12 |
| 2 | A5-S6 | 7 | hold | 2.42 | 1.99 | quote strip rises (`y:60` to 0 with the fade, 0.4 s); span 1 of quote 1 shows |
| 3 | A5-S6 | 12 | for | 3.36 | 2.93 | span 2 fades in (0.25 s) |
| 4 | A5-S6 | 16 | on | 4.48 | 4.05 | span 3 fades in |
| 5 | A5-S6 | 19 | Bern. | 5.26 | 4.83 | attribution fades in |
| 6 | A5-S6 | 26 | 10 | 8.48 | 8.05 | arc draws on the clock face from 8:45 to 9:00 (0.6 s); the arc label chip fades in |
| 7 | A5-S6 | 31 | Several | 10.54 | 10.11 | quote 1 fades out (0.2 s), quote 2 span 1 fades in (0.25 s) in the same place |
| 8 | A5-S6 | 38 | ambulances | 13.40 | 12.97 | quote 2 span 2 fades in |
| 9 | end | | | | 15.98 | comp ends; no exit move (the next picture cuts in) |

## 6. Contract
As `references/mg-brief-template.md` section 6, with plan rule 3 over its `id="root"`. File the builder may write: `compositions/g-a5s06-hold.html` only. Id prefix `hold-`, root id `hold-root`. Base it copies: the stamp and the photograph ground of `compositions/g-a1s01-kc.html` (wave 1). Asset mounted: `media/stills/a5-teletype-room-1947.jpg` (1820 x 1220); `media/drawings/wall-clock.svg` inline for the face. No later composition copies this one.

## 7. Tools
As the template's section 7.

## 7a. Done line
As the template's section 7a, all seven. Fill: full frame (the photograph). Done line 7 does not apply (the comp is opaque).

## 8. Receipt
As the template's section 8, plus: the measured width of quote 1's first line and of the arc label chip, and the screen box of the operator's head at the first and last frame.

## Frames the verifier reads
First frame 0.00 and the frame after it (0.04); then one settled frame per cue: 0.80, 2.50, 3.30, 4.40, 5.20, 8.80, 10.50, 13.40, and the last frame 15.90. On each: section 4 items 1 to 3 first.
