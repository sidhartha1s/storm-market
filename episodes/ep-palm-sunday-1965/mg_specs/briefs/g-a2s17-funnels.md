Host: id=g-a2s17-funnels file=compositions/g-a2s17-funnels.html start=431.30 (timeline-map.md table 1; the mount in index.html wins) duration=18.96 s (wav sum 18.68 s plus gaps from timeline-map.md) track=2

# g-a2s17-funnels · A2-S17, A2-S18 · the twin funnels, then Sunnyside (wave 1, base of the photograph family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 3, 4, 10, 11. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21; section 3e rows PT-08 and PT-09; section 6 item 9 (the buildable version of "full frame").
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1; the built hook comps' `fromTo` at a cue is not copied). Text on a moving object fades before it leaves the text-safe margin (rule 2; here no text rides a photograph). The root is styled through its id and is never `id="root"` (rule 3). A photograph's label names what the photograph shows, never the town the voice is talking about if they differ (rule 5). A flash is a stroke or fill change, never a scale pop (rule 12). A picture under 1000 px wide sits in a card at its own size (section 3e).
**Spoken (A2-S17):** "At six thirty two he took this picture, two funnels side by side. The Weather Service calls it one of the most celebrated tornado pictures of all time. Fourteen people lost their lives in the tornado he photographed."
**Spoken (A2-S18):** "And this is the Sunnyside subdivision in Dunlap, after a tornado crossed it that evening."
**One look:** the photograph, whole and slowly nearer; one number in the grass under it; then a hard cut to a small print of what the evening left.

## 0. What this graphic claims
Paul Huffman of The Elkhart Truth took this photograph at 6:32 PM on April 11, 1965. Fourteen people lost their lives in the tornado it shows. The second photograph shows the Sunnyside subdivision in Dunlap, Indiana, after a tornado crossed it that evening.

## 1. Source
- `edit_script.md` A2-S17, Rows [inventory C1: 11 Apr 1965, 6:32 pm] · [IWX: "one of the most celebrated tornado pictures of all-time"] · [IWX tornado table: "the Dunlap twin funnel, first Dunlap tornado", 14]. Picture note: chip "6:32 PM", credit "Paul Huffman, The Elkhart Truth · April 11, 1965", place label "Midway Trailer Court", toll "14 lives lost · this tornado", source line "National Weather Service".
- `edit_script.md` A2-S18, Rows [inventory C2: "Sunnyside subdivision in Dunlap, Indiana, following the F4 tornado of April 11, 1965"].
- Photograph 1: `media/stills/c1-elkhart-twin-funnel.jpg`, 1188 x 1068 (inventory C1). Read by eye 12 Oct 26: sky and the two funnels fill file y 0 to about 740; the horizon (road, house, poles, a billboard at file x 970 to 1110, y 630 to 735) sits at file y 640 to 760; below file y 772 the picture is dark road and grass (row means 36 to 58 of 255). That dark band is where every label goes.
  Its `provenance.csv` row, quoted: type STILL; date "1965-04-11"; title "1965 Elkhart Double Tornado-Palm Sunday"; credit "Paul Huffman (d. 2014), The Elkhart Truth (Commons PD claim; owner approved C1 on 11 Oct 26)"; note "Row C1. Direct file: https://upload.wikimedia.org/wikipedia/commons/3/39/1965_Elkhart_Double_Tornado-Palm_Sunday.jpg. SPARE, not a damage row. Twin funnels over a road, house and trees at left, pest-control billboard at right." What the row limits: "SPARE" is answered by the owner's approval in the same row and the Picture note's "use it."; the photograph is shown as itself, never as a damage picture. The row gives the date, the photographer and the paper, and the credit carries all three. The row does not name the trailer court: `Midway Trailer Court` comes from the Picture note alone. At 1188 px wide it is past the 1000 px floor for a full-frame picture.
- Photograph 2: `media/stills/c2-dunlap-sunnyside-damage.jpg`, 800 x 647 (inventory C2), with a faded white edge. Measured on the file 12 Oct 26 (column and row means): the fade ends by column 20 on the left and column 779 on the right, and by row 626 at the bottom. The top fades more slowly: the share of near-white pixels (over 235 of 255) in a row is 0.78 at row 22, 0.47 at row 30 and 0.05 at row 40 (measured again 12 Oct 26, 19:13). The clean picture is file x 20 to 780, y 40 to 626 (760 x 586).
  Its `provenance.csv` row, quoted: type STILL; date "1965-04"; uploader "Wikimedia Commons (source: National Weather Service)"; title "Sunnyside subdivision in Dunlap, Indiana, following the F4 tornado of April 11, 1965"; credit "Blake Naftel / National Weather Service (Commons PD claim; origin Elkhart Truth or South Bend Tribune, unclear)"; note "Row C2. Direct file: https://upload.wikimedia.org/wikipedia/commons/5/57/Sunnyside_subdivision_in_Dunlap%2C_Indiana%2C_following_the_F4_tornado_of_April_11%2C_1965.jpg. Aerial of a flattened subdivision, bare slabs and debris, road curving through, cars among the wreckage. Largest size on the page is 800x647." What the row limits: 800 px wide, so a card only, never full frame and never enlarged; the first publisher is unclear, so the credit is the row's own credit line and names no newspaper.

## 2. Datum, scale, orientation
- Photograph 1 is fitted to the frame's height, not to cover: scale 1080 / 1068 = 1.0112, box 1201 x 1080 at left 359, top 0 (x 359 to 1561). At cover it would lose 37.4 % of its height and the cut would fall on the funnels (plan section 6 item 9). Screen x = 359.3 + 1.0112 x file x; screen y = 1.0112 x file y, before the push.
- Push on photograph 1: scale 1.00 to 1.05 about the frame centre (960, 540), from 0.00 to 13.10 s, `ease:"none"`. At 1.05 the picture spans x 329.3 to 1590.7, so it never reaches the presenter corner (x >= 1600, y >= 680). At 9.24 s (the toll's cue) the scale is 1.0353 and file y 772 sits at screen y 789.
- Photograph 2 is shown at its own size or smaller, never enlarged: the print's window is 722 x 556 and the `<img>` runs scale 0.95 to 1.00 about file point (400, 333), from 13.10 to 18.96 s, `ease:"none"`. At 0.95 the window holds file x 20 to 780, y 40.4 to 625.6; at 1.00 it holds file x 39 to 761, y 55 to 611; at 1.00 the picture is at one file pixel per screen pixel.

## 3. Geometry (screen px)
Layer A (A2-S17, on from frame 0, off at 13.10):
| Element | Px |
|---|---|
| Soft copy | the same file in a second `<img>`: left -40, top -40, 2000 x 1160, `object-fit:cover` (1.6835 x the file), `filter: blur(22px) brightness(0.6)`. It does not move |
| Scrim | `.dim` (`rgba(3,5,8,0.45)`, tokens.md "Scrim") over the soft copy, under the fitted picture |
| Fitted picture | `<img>` left 359, top 0, width 1201, height 1080, `transform-origin:50% 50%`, `box-shadow:0 0 60px rgba(0,0,0,0.6)`. Scale 1.00 to 1.05 as section 2. No border: it is a photograph, not paper |
| Clock chip | glass chip (tokens.md "Surfaces"), left 96, top 96, height 62, padding 0 x 22: `6:32 PM` in Courier New 700 44 px, Amber 2, `line-height:62px`. Text 184.8 px wide, chip right edge x 324.8: it sits on the soft copy, left of the fitted picture at every push (329.3) |
| Place chip | design sheet section 11: glass chip, left 110, bottom 110 (top 908), padding 14 x 26, Arial Black 900 34 px, Headline white: `Midway Trailer Court` |
| Credit | design sheet section 10 style (Arial 700 22 px, `rgba(244,240,232,0.88)`, the credit shadow), left 96, bottom 60: `Paul Huffman, The Elkhart Truth · April 11, 1965` |
| Toll card | glass card, left 1010, top 792, 560 x 200 (right 1570, bottom 992), radius 28 |
| Toll figure | `14`: the type of `.toll-num` in the built `compositions/g-t1s1-toll.html` (AbrilFig, Popfig red, its `text-shadow`, `letter-spacing:0.04em`, `line-height:1`) at 120 px, left 1040, top 832 |
| Toll label | two lines, the type of `.toll-lab` (Arial Black 900, Headline white, its stroke and shadow) at 34 px with `letter-spacing:0.12em`, left 1224: `lives lost` top 822, `this tornado` top 866 |
| Toll source | Arial 700 22 px, the credit colour and shadow, left 1224, top 922: `National Weather Service` |

Layer B (A2-S18, on from 13.10 to the end):
| Element | Px |
|---|---|
| Soft copy | `media/stills/c2-dunlap-sunnyside-damage.jpg` in an `<img>`: left -40, top -40, 2000 x 1160, `object-fit:cover` (2.5 x the file), `filter: blur(9px) brightness(0.7)` (the built `.toll-soft`). It does not move |
| Print | card left 589, top 252, 742 x 576 outer: Beige polaroid border 10 px, `box-shadow:0 18px 50px rgba(0,0,0,0.55)`, `overflow:hidden`; inner window 722 x 556 |
| Picture in the print | `<img>` of the file at width 800, height 647, `position:absolute; left:-39px; top:-55px; transform-origin:400px 333px`. Scale 0.95 to 1.00 as section 2 |
| Place chip | same chip style and place as layer A's (left 110, top 908): `Sunnyside · Dunlap, Indiana`. A second, pre-authored element |
| Credit | same style and place as layer A's credit (left 96, bottom 60), a second, pre-authored element: `Blake Naftel / National Weather Service · April 1965`. On with layer B from the cut: the photograph is never on screen without it |

Ground under both layers: the canvas gradient on the root (design sheet section 2), so no frame is bare if an image is late.

## 4. Must be true in the picture
1. The whole of photograph 1 is in frame at 0.00: both funnels, the sky above them and the road. It is never shown at cover.
2. **No label over the funnels.** The clock chip sits left of the fitted picture (right edge 324.8 against 329.3). The place chip, the credit and the toll card sit below screen y 789, which is file y 772 or lower at every moment they are on: road and grass only. Nothing of ours covers the house, the poles or the horizon.
3. `6:32 PM` is the time of the photograph (inventory C1). It is the only time on screen.
4. The credit names the photographer, the paper and the date, exactly as section 3.
5. `14` is the toll of the tornado in the photograph: the words `this tornado` sit beside it and `National Weather Service` under them. No other figure is on screen in this comp.
6. `Midway Trailer Court` is on screen only with photograph 1 and `Sunnyside · Dunlap, Indiana` only with photograph 2 (rule 5). The two chips never share a frame, and neither do the two credits. Each photograph carries its own place, date and source for every frame it is on.
7. Photograph 2 is never larger than its own pixels (scale 1.00 at most), and the print's window never shows the faded edge: file x 20 to 780, y 40 to 626 at its widest. No near-white band runs along the top of the window at 13.14; if one shows, lower the top cut and report it.
8. The change from layer A to layer B is a hard cut on one frame: at 13.10 nothing of layer A remains, soft copy included.
9. Neither photograph is recoloured, cropped to hide a part, or drawn on. The billboard in photograph 1 stays as printed.
10. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680: the fitted picture ends at x 1590.7 and the toll card at x 1570.

## 5. Text (exact) and cues
Text: `6:32 PM` · `Midway Trailer Court` · `Paul Huffman, The Elkhart Truth · April 11, 1965` · `14` · `lives lost` · `this tornado` · `National Weather Service` · `Sunnyside · Dunlap, Indiana` · `Blake Naftel / National Weather Service · April 1965`. Every word is from the Picture notes of A2-S17 and A2-S18 or the two `provenance.csv` rows.
Cue words and times are from `audio/a2-s17.words.json` and `audio/a2-s18.words.json` as they stood on 12 Oct 26 at 18:55, after the voice conversion's re-transcription (wavs 13.126 s and 5.551 s, sum 18.68 s). "t from comp start" is `mg_specs/timeline-map.md` table 5: the segment's "wav start inside the composition" (A2-S17 -0.50, A2-S18 12.74) plus the word's time; a segment's first word takes the "first sound" column (0.00 and 13.10). The gaps are therefore already in the last time column. Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A2-S17 | 0 | At | 0.00 | 0.00 | first frame: soft copy, scrim, fitted picture and the credit are on; the push starts (1.00 to 1.05, ends at 13.10) |
| 1 | A2-S17 | 1 | 6 | 0.76 | 0.26 | clock chip `6:32 PM` slides in from the left (`x:-40` set at 0, then `to x:0, autoAlpha:1`, 0.4 s, power3.out). The transcriber writes "6 .32" |
| 2 | A2-S17 | 5 | this | 1.94 | 1.44 | place chip `Midway Trailer Court` slides in (`x:-60` set at 0, then `to x:0, autoAlpha:1`, 0.3 s, power3.out) |
| 3 | A2-S17 | 12 | The | 5.22 | 4.72 | nothing new: the second sentence is carried by the push alone. The photograph is the subject; do not add a mark |
| 4 | A2-S17 | 27 | Fourteen | 9.74 | 9.24 | toll card fades in (0.3 s); `14` lands with it (`y:24` set at 0, then `to y:0, autoAlpha:1`, 0.35 s, power4.out); `lives lost`, `this tornado` and the source follow 0.25 s later (0.3 s). Hold |
| 5 | A2-S18 | 0 | And | 0.00 | 13.10 | hard cut: layer A off and layer B on with its credit, on the same frame (`tl.set`). The print's picture starts its move (0.95 to 1.00, ends at 18.96) |
| 6 | A2-S18 | 4 | Sunnyside | 0.96 | 13.70 | place chip `Sunnyside · Dunlap, Indiana` slides in (as step 2). Hold to the last frame |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a2s17-funnels.html` is the only file the builder writes; `data-composition-id="g-a2s17-funnels"`; id prefix `fun-`; root `<div id="fun-root" ...>` styled through `#fun-root` (plan rule 3 overrides the template's `id="root"`). Full frame, opaque, own ground on from frame 0.
**This comp is a family base (photograph family).** `acts-plan.md` section 5 puts it in wave 1 so the later photograph comps copy three things from it once it has passed its read: the fitted picture over a soft copy of itself, the place chip, and a toll on a glass card. The comps that take from it are `g-a5s06-hold` and `g-a5s09-alto` (wave 4, with `g-a5s16-toledo` for the toll card); `g-a1s07-tracks` (wave 2) names it for the caption and push habits. The other base of this family is `compositions/g-a1s01-kc.html` (one photograph at cover, brief `mg_specs/briefs/g-a1s01-kc.md`). Keep those three pieces in their own blocks of CSS and markup so they lift out whole. Send it alone for a full-size read before anything copies it (template section 7a, last line).
It takes its own toll type from the built `compositions/g-t1s1-toll.html` (`.toll-num`, `.toll-lab`, `.toll-chip`, `.toll-soft`, `.toll-print`): copy the values under this comp's class names.
**Assets mounted (paths from the episode folder):**
- `media/stills/c1-elkhart-twin-funnel.jpg`, 1188 x 1068, twice (soft copy, fitted picture).
- `media/stills/c2-dunlap-sunnyside-damage.jpg`, 800 x 647, twice (soft copy, print).
Note for the orchestrator, not the builder: C2 was also shown in the hook (`g-t1s1-toll`); if `lint_timeline.py` names the repeat, the host takes `data-callback` with its reason.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a2s17-funnels`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `python3`, never `python`.

## 7a. Done line
All seven lines of template section 7a. Line 2 (fill): state the fitted picture's share of the frame at 0.00 and at 13.00, and the print's at 18.90. Line 6: the boxes of section 2 and 3 (fit scale, the 1.05 edges, the print window, the `<img>` offsets) are recomputed from the two files' pixel sizes by a script and stated in the receipt. Line 7 does not apply as an overlay (the comp is opaque), but its last sentence does: each chip and each credit is read against the `provenance.csv` row of the photograph it sits with.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): the whole photograph, soft copy and credit on both, no chip yet. Then one settled frame per cue: 0.90 (clock chip, clear of the picture's left edge), 2.00 (place chip), 7.00 (second sentence: picture nearer, no new mark), 10.20 (toll card complete, nothing above screen y 789, right edge inside x 1600), 13.00 (last frame of layer A: picture's right edge at about x 1591), 13.10 and 13.14 (the cut: only layer B on both, its credit on, no white band at the top of the print), 14.30 (Sunnyside chip), 18.90 (print at its own size, no faded edge in the window). Each cue second in both seek orders.
