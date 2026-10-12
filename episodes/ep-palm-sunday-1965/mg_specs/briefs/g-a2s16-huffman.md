Host: id=g-a2s16-huffman file=compositions/g-a2s16-huffman.html start=415.62 (timeline-map.md table 1; the mount in index.html wins) duration=15.43 s (wav 15.04 s plus its gaps) track=2

# g-a2s16-huffman · A2-S16 · a photographer in Elkhart is told where to look (wave 2, map family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md`. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Map facts: `media/maps/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). Text fades before the thing it sits on moves (rule 2). The root is styled through its id, never `id="root"` (rule 3). A flash is a stroke or fill change (rule 12). Map geometry comes from the file (rule 14). No map shows Alto; inlined map ids take this comp's prefix; line weight is read at both ends of the zoom (rule 20).
**Spoken (A2-S16):** "In Elkhart, a newspaper photographer named Paul Huffman was sifting through the warnings when his editor told him to grab his camera. Before he left, the South Bend weather office told him a tornado was reported northwest of Nappanee, moving northeast."
**One look:** a dot and a name in Elkhart; then the map closes in and a tornado mark sits northwest of Nappanee with an arrow pointing northeast, toward him.

## 0. What this graphic claims
Paul Huffman, a photographer at The Elkhart Truth, was in Elkhart. The South Bend weather office told him a tornado was reported northwest of Nappanee, moving northeast. Elkhart lies north of Nappanee, so northeast of that report is his side of the county.

## 1. Source
- `edit_script.md` A2-S16, Rows [E, Huffman; IWX narrative, confirmed word for word by the fact check]. The account is the National Weather Service's telling, so the frame says so.
- Positions: `media/data/points.csv`: `pt-elkhart` map units (501.1, 185.8), `pt-nappanee` (496.7, 231.1), `pt-south-bend` (462.2, 188.5). Counties: `media/maps/indiana-counties.svg`.
- The source gives no distance for "northwest of Nappanee" and does not say how the office told him (telephone or in person). Neither is drawn as known.

## 2. Datum, scale, orientation
North is up. One inline SVG holds BM-1; the camera is its `viewBox` and its CSS box, tweened together.
| State | Box (left, top, width, height) | viewBox | Px per map unit | Used |
|---|---|---|---|---|
| NORTH (family state) | 716, 62, 1080, 450 | `296 166 360 150` | 3.0 (screen x = 3u - 172, y = 3u - 436) | first sentence |
| ELKHART (this comp's) | 620, 62, 960, 900 | `438 152 128 120` | 7.5 (screen x = 620 + 7.5 x (u - 438), y = 62 + 7.5 x (u - 152)) | second sentence |
NORTH to ELKHART is a 2.5 times push: move the viewBox numbers geometrically (the `logZoom` maths of `library/inhouse/snippets/helpers.js` on a proxy with `onUpdate`), box and viewBox in the same 0.9 s tween, and set the end values exactly. Both boxes end left of x 1600 or above y 680: the presenter corner stays empty.
The tornado mark's place is schematic: 7 map units west and 7 north of `pt-nappanee` (about 6 km, 74 px on screen), which is "northwest" and nothing more exact.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0 |
| Map | BM-1 groups inlined, ids prefixed `huff-`; county lines 1.5 px, Indiana's outline 3 px, non-scaling. Every `pt-` group hidden except Elkhart, Nappanee and South Bend, each shown only from its cue. Dot radius 6 px on screen: `r` 2 map units in NORTH, 0.8 in ELKHART (tween `r` with the push) |
| Elkhart dot | NORTH (1331.3, 121.4); ELKHART (1093.3, 315.5) |
| Label `Elkhart` | Arial 700 22 px, Body light. NORTH: centred on x 1331, top 84. ELKHART: centred on x 1093, top 270. It fades out 0.2 s before the push and back in after it |
| Name card | glass plate as `compositions/g-i1s2-station.html` `.stn-card` (same fill, blur, border, radius 28): left 96, top 96, 520 x 170. Name `Paul Huffman`: Arial Black 900 52 px, Headline white, left 138, top 118 (382 px wide). Sub `photographer, The Elkhart Truth`: Georgia italic 30 px, Amber 2, left 140, top 198 (445 px wide) |
| Source line | design sheet section 10, left 96, bottom 60: `as told by the National Weather Service` |
| Elkhart County outline | `huff-co-in-elkhart` stroke goes Label grey to Headline white, 3 px (a stroke change, no scale) |
| South Bend dot | ELKHART (801.5, 335.8). Label `Weather Bureau · South Bend`: Arial 700 22 px, Body light, centred on x 801, top 352 (307 px wide, under the dot and under the link) |
| Link | overlay SVG, dotted (Label grey, 4 px dots, 14 px gap), from the South Bend dot (801.5, 335.8) to the Elkhart dot (1093.3, 315.5); drawn from South Bend. Dotted because the source does not say how he was told |
| Nappanee dot | ELKHART (1060.2, 655.2). Label `Nappanee`: Arial 700 22 px, Body light, left 1078, top 644 |
| Tornado mark | `media/drawings/tornado-mark.svg` inline at 0.75 scale (45 x 60 px, line 4.5 px), group stroke Body light, never red; its lowest point at (1007.7, 602.8) |
| Arrow | overlay SVG, Body light 4 px, round caps, from (1024, 586) to (1109, 501) (pointing up and right at 45 degrees, 120 px long), with a two-stroke head 18 px. It points northeast, toward the Elkhart dot's side of the frame, and stops 186 px short of that dot |

## 4. Must be true in the picture
1. Elkhart's dot is north of Nappanee's and a little east; both sit inside Elkhart County's outline. All three dots come from `media/data/points.csv` by the formulas in section 2, within 2 px.
2. The tornado mark is northwest of the Nappanee dot (left of it and above it). The arrow points northeast (up and right).
3. The mark is a report, not a sighting by Huffman: no line joins the mark to the Elkhart dot, and the arrow stops well short of it.
4. The link from South Bend to Elkhart is dotted and carries no telephone, no time and no arrowhead.
5. The name card reads `Paul Huffman` and `photographer, The Elkhart Truth`; the account is credited `as told by the National Weather Service`. No portrait, no drawn person, no camera icon.
6. No county is filled amber. No time is on screen (6:32 PM belongs to the next comp). No Dunlap, no Goshen, no Alto.
7. Line weights are the same at both ends of the push (read both frames).
8. Nothing appears before its spoken word; nothing of ours in x >= 1600, y >= 680.

## 5. Text (exact) and cues
Text: `Elkhart` · `Paul Huffman` · `photographer, The Elkhart Truth` · `as told by the National Weather Service` · `Weather Bureau · South Bend` · `Nappanee`.
Cue words and times are from `audio/a2-s16.words.json` as it stood on 12 Oct 26 at 17:53, after the voice conversion's re-transcription (file time 17:50; wav 15.04 s). One segment, so the two time columns are equal; a lead-in gap from `mg_specs/timeline-map.md`, if any, is added to every row. Retime from the word, never from the seconds. The transcriber writes "Oakhart" for Elkhart and "Napanee" for Nappanee; the labels use the true spellings.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A2-S16 | 0 | In | 0.00 | 0.00 | first frame: ground and the map in NORTH, no dot, no label |
| 1 | A2-S16 | 1 | Oakhart, | 0.40 | 0.11 | Elkhart dot and label fade in (0.3 s) |
| 2 | A2-S16 | 6 | Paul | 2.70 | 2.41 | name card slides in from the left (0.6 s, power3.out), name then sub (0.15 s apart) |
| 3 | A2-S16 | 9 | sifting | 4.12 | 3.83 | source line fades in (0.3 s) |
| 4 | A2-S16 | 15 | editor | 5.70 | 5.41 | Elkhart County's outline turns Headline white (0.4 s) |
| 5 | A2-S16 | 22 | Before | 8.24 | 7.95 | label `Elkhart` fades (0.2 s, starting 0.2 s earlier); push NORTH to ELKHART (0.9 s, ends 9.14); label back at its new place at 9.20 |
| 6 | A2-S16 | 26 | South | 9.42 | 9.13 | South Bend dot and label fade in (0.3 s) |
| 7 | A2-S16 | 30 | told | 10.62 | 10.33 | dotted link draws from South Bend to Elkhart (0.5 s) |
| 8 | A2-S16 | 38 | Napanee, | 12.90 | 12.61 | Nappanee dot and label (0.3 s); the tornado mark fades in northwest of it 0.15 s later |
| 9 | A2-S16 | 40 | northeast. | 14.04 | 13.75 | the arrow draws from the mark toward the northeast (0.4 s). Hold to the end |
Time basis (converted 12 Oct 26 from wav sums): t from comp start = the segment's wav start inside the composition (`mg_specs/timeline-map.md` table 5) plus the word's time in words.json; a segment's first word uses table 5's first sound. Gaps are now included. Where another line of this brief quotes a second from the comp's start, this table wins.
Longest stretch with no change: 12.9 minus 10.6 (2.3 s), inside the beat rule.

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: file `compositions/g-a2s16-huffman.html` is the only file the builder writes; `data-composition-id="g-a2s16-huffman"`; id prefix `huff-`; root `<div id="huff-root" ...>` styled through `#huff-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0.
**Family base it copies:** the map family base `compositions/g-a2s14-six.html` (wave 1; brief `mg_specs/briefs/g-a2s14-six.md`) for the NORTH mount, the inlining and the prefixing; the name card's glass plate and type from the built `compositions/g-i1s2-station.html` (`.stn-card`, `.stn-name`, `.stn-sub`). The state ELKHART is this comp's own.
**Assets mounted (paths from the episode folder):**
- `media/maps/indiana-counties.svg` (BM-1, viewBox 96 100 664 880, 70,592 bytes), inlined.
- `media/drawings/tornado-mark.svg` (DR-03, object box 60 x 80, viewBox -6 -6 72 92, line 6), inlined.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a2s16-huffman`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 4 here: the push is driven by a proxy, so seek to 8.7 (mid push) forward and backward and match the frames. Line 6: every dot position of section 3 is computed from `media/data/points.csv` by a script and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): map only. Then one settled frame per cue: 1.00 (Elkhart), 3.60 (name card), 4.60 (source line), 6.40 (county outline lit), 8.10 and 9.30 (the two ends of the push: line weight, dot size), 10.00 (South Bend), 11.30 (link), 13.50 (Nappanee and the mark), 14.70 (arrow).
