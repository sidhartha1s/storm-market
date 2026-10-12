Host: id=g-a2s08-first file=compositions/g-a2s08-first.html start=345.88 (timeline-map.md table 1; the mount in index.html wins) duration=6.69 s (wav 6.53 s plus its gaps) track=2

# g-a2s08-first · A2-S8 · the first tornado's path, then its toll (wave 2, map family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md`. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, and section 6 item 6 (the buildable version of this Picture note). Map facts: `media/maps/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). A flash is a stroke or fill change, never a scale pop (rule 12). Map geometry comes from the file, nothing is placed by eye (rule 14). No map shows Alto; inlined map ids take this comp's prefix; the first frame read checks line weight (rule 20).
**Spoken (A2-S8):** "That first tornado ran from Starke County to just south of South Bend. Ten people did not survive it."
**One look:** a short dotted path across three county lines, a mark that travels it, then one number.

## 0. What this graphic claims
The 5:45 PM tornado ran from near Koontz Lake in Starke County to just south of South Bend. Ten people lost their lives in that one tornado.

## 1. Source
- `edit_script.md` A2-S8, Rows [B table; IWX tornado table: "NE of Knox (Koontz Lake) to S of South Bend", 5:45 PM, 10].
- The table's coordinates are not on disk (plan section 6 item 6). So the path is drawn between the table's two named ends and claims nothing about the line between them. The track map (inventory B7) is not used in this comp.
- Positions: `media/data/points.csv` (US Census gazetteer): `pt-koontz-lake` map units (435.6, 237.4), `pt-south-bend` (462.2, 188.5). County outlines: `media/maps/indiana-counties.svg`.

## 2. Datum, scale, orientation
North is up. One inline SVG holds the map: BM-1 mounted at left 620, top 62, width 960, height 900 with `viewBox="376 166 136 127.5"` (state TRACK: 7.0588 px per map unit; screen x = 620 + 7.0588 x (u - 376), screen y = 62 + 7.0588 x (u - 166)). The box's right edge is x 1580 and its bottom y 962: the presenter corner (x >= 1600, y >= 680) stays empty. The camera does not move in this comp.
"Just south of South Bend" has no figure in the source. The end point is fixed at 6 map units due south of `pt-south-bend` (about 3.6 km at this latitude): (462.2, 194.5). It is a schematic end, which is why the line is dotted.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient (design sheet section 2), on from frame 0 |
| Map | BM-1 groups `map-neighbours`, `map-counties`, `map-state` inlined with ids prefixed `first-`; county lines 1.5 px, Indiana's outline 3 px (the file's `vector-effect="non-scaling-stroke"` keeps them). Every `pt-` group is hidden except the two named below |
| Town dots | `first-pt-koontz-lake` at (1040.7, 566.0) and `first-pt-south-bend` at (1228.5, 220.8). Set each circle's `r` to 0.85 map units (6 px on screen); fill Body light |
| Label `Koontz Lake` | Arial 700 22 px, Body light, right aligned to x 1024, top 574 (below and left of the dot, clear of the path) |
| Label `South Bend` | Arial 700 22 px, Body light, left 1246, top 209 |
| Label `STARKE COUNTY` | Arial 700 22 px, Label grey, tracking 2, centred on (843, 709), the county's box centre |
| Path | full-frame overlay SVG: straight line from (1040.7, 566.0) to (1228.5, 263.2), 356.3 px long; Body light dots 4 px, gap 14 px, round caps. Drawn from the Koontz Lake end by a clip that grows along the line |
| Tornado mark | `media/drawings/tornado-mark.svg` inline at 0.75 scale (45 x 60 px, line 4.5 px), group stroke Body light, never red. Its lowest point rides the path from (1040.7, 566.0) to (1228.5, 263.2). It stops 42 px south of the South Bend dot and stays |
| Chip | glass chip, left 96, top 96, height 46, padding 0 x 22, Arial 700 26 px, Body light: `The 5:45 PM tornado` |
| Toll figure | `10`: the popfig type of `compositions/g-t1s1-toll.html` (`.toll-num`: AbrilFig 150 px, Popfig red, its shadow), left aligned at left 96, top 360 |
| Toll label | two lines, Arial Black 900 38 px, Headline white, tracking 0.2em, left 96: `lives lost` top 522, `this tornado` top 572 |
| Map dim | when the toll lands: a `rgba(3,5,8,0.45)` scrim over the map box only (x 620 to 1580, y 62 to 962) |
| Source line | design sheet section 10: left 96, bottom 60: `National Weather Service` |

## 4. Must be true in the picture
1. The path starts on the Koontz Lake dot, inside Starke County's outline, and ends 6 map units due south of the South Bend dot. Both ends come from `media/data/points.csv` by the formula in section 2, within 2 px.
2. The path is dotted and straight: it is the two ends of the Weather Service's table row, not a surveyed track. It is never laid over the track map.
3. The mark stops short of South Bend's dot and never touches it ("just south of").
4. `10` is this tornado's toll: the words `this tornado` sit under it. No other toll figure is on screen.
5. No county is filled amber (in this family an amber county is a warned county). Starke is named, not lit.
6. The only time on screen is `5:45 PM` in the chip. No Alto, no other town.
7. Nothing appears before its spoken word; nothing of ours in x >= 1600, y >= 680.

## 5. Text (exact) and cues
Text: `The 5:45 PM tornado` · `Koontz Lake` · `STARKE COUNTY` · `South Bend` · `10` · `lives lost` · `this tornado` · `National Weather Service`.
Cue words and times are from `audio/a2-s8.words.json` as it stood on 12 Oct 26 at 17:50, after the voice conversion's re-transcription (wav 6.53 s). The comp holds one segment, so the two time columns are equal; if `mg_specs/timeline-map.md` puts a lead-in gap before the segment, add it to every row. Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A2-S8 | 0 | That | 0.00 | 0.00 | first frame: ground and the county map, nothing else |
| 1 | A2-S8 | 2 | tornado | 0.88 | 0.39 | chip `The 5:45 PM tornado` slides in from the left (0.5 s, power3.out); source line fades in (0.3 s) |
| 2 | A2-S8 | 5 | Stark | 1.82 | 1.33 | Koontz Lake dot and label, `STARKE COUNTY` label (0.3 s fades); the tornado mark fades in on the dot. The transcriber writes "Stark"; the label is spelled `STARKE` |
| 3 | A2-S8 | 7 | to | 2.40 | 1.91 | the dotted path grows from Koontz Lake to its end and the mark rides its head (1.0 s, ease none; it arrives at 3.40) |
| 4 | A2-S8 | 11 | South | 3.28 | 2.79 | South Bend dot and label (0.3 s) |
| 5 | A2-S8 | 13 | Ten | 4.66 | 4.17 | map dim fades in (0.3 s); `10` lands (0.35 s, `y:24` to 0 with the fade); `lives lost` and `this tornado` follow 0.25 s later. Hold to the end |
Time basis (converted 12 Oct 26 from wav sums): t from comp start = the segment's wav start inside the composition (`mg_specs/timeline-map.md` table 5) plus the word's time in words.json; a segment's first word uses table 5's first sound. Gaps are now included. Where another line of this brief quotes a second from the comp's start, this table wins.

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: file `compositions/g-a2s08-first.html` is the only file the builder writes; `data-composition-id="g-a2s08-first"`; id prefix `first-`; root `<div id="first-root" ...>` styled through `#first-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the map family base `compositions/g-a2s14-six.html` (wave 1; brief `mg_specs/briefs/g-a2s14-six.md`) for the way BM-1 is inlined, prefixed and lit; the toll type from the built `compositions/g-t1s1-toll.html`. The state TRACK above is this comp's own.
**Assets mounted (paths from the episode folder):**
- `media/maps/indiana-counties.svg` (BM-1, viewBox 96 100 664 880, 70,592 bytes), inlined.
- `media/drawings/tornado-mark.svg` (DR-03, object box 60 x 80, viewBox -6 -6 72 92, line 6), inlined.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a2s08-first`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 6 here: the four screen points of section 3 (two dots, the path's two ends) are computed from `media/data/points.csv` by a script with the section 2 formula and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): map only, line weights as section 3. Then one settled frame per cue: 1.50 (chip), 2.30 (Koontz Lake, Starke label, mark on the dot), 3.50 (path complete, mark at its end, short of South Bend), 4.00 (South Bend label), 5.60 (toll and both label lines, map dimmed), 6.40 (last frame).
