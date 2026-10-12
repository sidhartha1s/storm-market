Host: id=g-a5s09-alto file=compositions/g-a5s09-alto.html start=900.76 (timeline-map.md table 1; the mount in index.html wins) duration=5.99 s track=2

# g-a5s09-alto · A5-S9 · twenty five lives on one storm's path (wave 4, photograph family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 3, 4, 10, 11. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, and section 3e rows PT-11 and PT-12. Times: `mg_specs/timeline-map.md` tables 1 and 5. Base: `mg_specs/briefs/g-a2s17-funnels.md` (photograph, cut, toll card).
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id, never `root` (rule 3). A photograph's label names what the photograph shows, never the town the voice is on if they differ (rule 5). No map may show Alto (rule 20): this comp has no map.
**Spoken (A5-S9):** "The Weather Service counts twenty five lives lost on that storm's path, from Russiaville to Marion."
**One look:** the tornado over Alto, then Alto from the air after it, and the count.

## 0. What this graphic claims
The National Weather Service counts 25 lives lost along the path of the storm that ran from Russiaville to Marion. The two photographs show that storm at Alto and Alto after it.

## 1. Source
- `edit_script.md` A5-S9, Rows [IWX tornado table: "Russiaville to SE of Marion and Greentown", 25; IWX: the Russiaville tornado "devastated a hundred homes in Alto"]. The script says "storm", not "tornado": the table makes Berne to Ohio a second tornado.
- Photograph 1: `media/stills/c6-alto-tornado-cover.jpg` (1414 x 1080, inventory C6; Kokomo Morning Times special edition, 16 April 1965, front cover). Photograph 2: `media/stills/c5-alto-aerial-damage.jpg` (1543 x 1080, inventory C5; "Alto, Indiana, after the F4 tornado of April 11, 1965"). Read both `provenance.csv` rows before wiring.

## 2. Datum, scale, orientation
- At cover photograph 1 is enlarged 1.3579 times (1920 x 1466.5) and loses 26.4 % of its height; photograph 2 is enlarged 1.2443 times (1920 x 1343.9) and loses 19.6 %. The builder opens each file first and sets `object-position` so the funnel (1) and the damaged streets (2) are whole inside the frame, and states both values in the receipt.
- Each photograph runs a slow push, scale 1.00 to 1.03 about the frame centre, `ease:"none"`, over its own time on screen.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Layer A | `<img src="media/stills/c6-alto-tornado-cover.jpg">`, left 0, top 0, 1920 x 1080, `object-fit:cover`, on from frame 0; canvas gradient behind it |
| Caption A | credit corner, left 96, bottom 60, design sheet section 10 type: `Tornado over Alto, toward Kokomo · Kokomo Morning Times, April 16, 1965`. On with layer A from frame 0 |
| Layer B | `<img src="media/stills/c5-alto-aerial-damage.jpg">`, same box, `visibility:hidden` in CSS, shown by a hard cut |
| Place label B | glass chip, left 110, bottom 110, padding 14 x 26, Arial Black 900 34 px, Headline white (design sheet section 11): `Alto, Indiana`. On with layer B from the cut |
| Toll card | glass card, left 1010, top 792, 560 x 200 (right 1570, bottom 992), radius 28: the card of `g-a2s17-funnels.md` unchanged |
| Toll figure | `25`: the type of `.toll-num` in the built `compositions/g-t1s1-toll.html` at 120 px, left 1040, top 832 |
| Toll label | the type of `.toll-lab` at 30 px, left 1224, three lines, tops 814, 852, 890: `lives lost` / `along this storm's path` / `from Russiaville to Marion`. The third line is its own element |
| Toll source | Arial 700 22 px, the credit colour and shadow, left 1224, top 940: `National Weather Service` |

The toll card's right edge is x 1570: it sits beside the presenter corner, not in it. Measure the widest label line on a frame; it must end 20 px or more inside the card.

## 4. Must be true in the picture
1. Caption A is on every frame of photograph 1 and names what it shows; `Alto, Indiana` is on every frame of photograph 2. Neither label is ever over the other photograph.
2. The figure reads 25 and its label says the storm's path from Russiaville to Marion. The word "tornado" is not in the toll label. No other toll figure is on screen.
3. The toll's source line is on with the figure.
4. Nothing of ours covers the funnel in photograph 1.
5. No map, no dot and no arrow places Alto.
6. Nothing in x >= 1600 and y >= 680.
7. **Photograph 1 is on for 0.97 s** (the Picture note cuts on "twenty five"). Its caption cannot be read in that time. The brief builds the note as written and reports it; if the lead moves the cut, the next natural word is word 7 "on" (2.33 s from the comp's start).

## 5. Text (exact) and cues
Text: `Tornado over Alto, toward Kokomo · Kokomo Morning Times, April 16, 1965` · `Alto, Indiana` · `25` · `lives lost` · `along this storm's path` · `from Russiaville to Marion` · `National Weather Service`.
t from comp start = the segment's wav start inside the composition (timeline-map.md table 5: -0.49) plus the word's time; the first word uses table 5's first sound.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A5-S9 | 0 | The | 0.00 | 0.00 | first frame: photograph 1 and caption A; push starts |
| 1 | A5-S9 | 4 | 25 | 1.46 | 0.97 | hard cut to photograph 2 with `Alto, Indiana`; caption A off on the same frame; push restarts at 1.00 |
| 2 | A5-S9 | 5 | lives | 2.02 | 1.53 | toll card rises (`y:40` to 0 with the fade, 0.35 s, power3.out) with `25`, `lives lost`, `along this storm's path` and the source |
| 3 | A5-S9 | 11 | from | 3.92 | 3.43 | third label line `from Russiaville to Marion` fades in (0.25 s) |
| 4 | end | | | | 5.99 | comp ends; no exit move |

## 6. Contract
As `references/mg-brief-template.md` section 6, with plan rule 3 over its `id="root"`. File the builder may write: `compositions/g-a5s09-alto.html` only. Id prefix `alto-`, root id `alto-root`. Base it copies: the layers, the cut and the toll card of `compositions/g-a2s17-funnels.html` (wave 1). Assets mounted: `media/stills/c6-alto-tornado-cover.jpg` (1414 x 1080), `media/stills/c5-alto-aerial-damage.jpg` (1543 x 1080). No later composition copies this one.

## 7. Tools
As the template's section 7.

## 7a. Done line
As the template's section 7a, all seven. Fill: full frame (photographs). Done line 7 does not apply (the comp is opaque).

## 8. Receipt
As the template's section 8, plus: both `object-position` values, the measured width of the widest toll label line, and a sentence on whether caption A is readable in its 0.97 s.

## Frames the verifier reads
First frame 0.00 and the frame after it (0.04); 0.90 (last frame of photograph 1); 1.01 (first frame after the cut: no caption A, label B on); 2.10; 3.90; last frame 5.90.
