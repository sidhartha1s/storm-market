Host: id=g-a3s10-towers file=compositions/g-a3s10-towers.html start=555.89 duration=11.47 s (timeline-map.md tables 1 and 5, read 12 Oct 26, 19:33; the mount in index.html wins; last sound at 10.47) track=2

# g-a3s10-towers · A3-S10 · one name on the list was the power company: 11 breaks, 54 steel towers down (wave 3, list family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 5, 7, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, section 3a row DR-04 and section 6 item 14. Times: `mg_specs/timeline-map.md` tables 1 and 5. Drawings: `media/drawings/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). Text printed on a moving object fades before it leaves the text-safe margin (rule 2): the sheet fades in place, it does not slide off. The root is styled through its id and is never `id="root"` (rule 3). The ground is the canvas gradient, not the teletype room photograph, which is held to its three uses (rule 9). The typed sheet uses two type sizes by design (rule 10). A flash is a stroke or fill change, never a scale pop (rule 12). **The count of 54 was held against its spoken window** (rule 13): from the word "54" to the last sound is 1.69 s; 54 falls at 0.03 s apart take 1.62 s, so the count reaches 54 at 10.37 and the last tower lands at 10.57. A slower beat does not fit the line.
**Spoken (A3-S10):** "One name on South Bend's list was a power company, Indiana and Michigan Electric. It reported eleven breaks in its major lines in Indiana, and fifty four steel towers down."
**One look:** the telephone list close up, one row lit amber, the power company; then the list gives way to three rows of small steel towers under "11 breaks in major lines", and they fall one after another while a count runs to 54.

## 0. What this graphic claims
One of the organizations on South Bend's telephone list was a power company, the Indiana and Michigan Electric Company. It reported 11 breaks in its major lines in Indiana and 54 steel towers down.

## 1. Source
- `edit_script.md` A3-S10, Rows [A6; study printed p. 14] (the list) and [D; study printed p. 16] (the company's report). The Picture note: one row lights, "Indiana and Michigan Electric Company"; then 54 small drawn steel towers in rows, falling one after another while a count runs to "54"; above them "11 breaks in major lines"; label "Indiana · reported by the Indiana and Michigan Electric Company". No map. Nothing of the study's footnote for this line is shown.
- The list: design sheet section 5 (our typed setting of the study's sentence on printed p. 14) and the built `compositions/g-t1s3-list.html`. Slot 4 of the sheet reads `Indiana and Michigan Electric Company`.
- The two figures, 11 and 54, are the only numbers on screen. They are the company's report as the study prints it, and the label says so.

## 2. Datum, scale, orientation
Part A, the list: design sheet section 5 world coordinates under the **Close** camera state (s 1.6, tx 147.6, ty -66; sheet on screen x 250 to 1466, y 30 to 974; row text 41.6 px). Row centres on screen, slots 1 to 9 (by script): 276.4, 353.2, 430.0, 506.8, 583.6, 660.4, 737.2, 814.0, 890.8. Row box 70.4 px tall; a band runs x 301.2 to 1414.8. Slot 4 is centre y 506.8. The camera does not move.
Part B, the towers: SCHEMATIC, NOT TO SCALE, and not a map. 54 towers stand in three rows of 18. One tower is one tower of the report; their places on screen mean nothing.
Tower size (by script): `media/drawings/steel-tower.svg` object 80 x 160 at scale 0.36 is 28.8 x 57.6 px, the README's "about 26 px wide" case: `stroke-width="6"` on the group (2.16 px lines) and 4.5 on the two brace paths (1.62 px), as the README states. Column pitch 83 px. A tower falls to its right, turning 90 degrees about its base centre; lying down it reaches 57.6 px right of that centre and ends 11.0 px short of the next tower's left edge, so a fallen tower never touches a standing one.
Colours (the built hex): ground `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`; Beige polaroid `#f4f0e6`; Caption dark `#2a2622`; Caption dark sub `#6b6257`; Amber 2 `#e8c56a`; Label grey `#93a3b2`; Body light `#dfe7ee`; Headline white `#f2f5f8`; Panel dark `#15202b`.

## 3. Geometry (screen px)
Ground: canvas gradient, on from frame 0, for both parts.

Part A (comp 0.00 to 5.34):
| Element | Px |
|---|---|
| List sheet | design sheet section 5, all nine slots, Close state: sheet x 250 to 1466, y 30 to 974. Eyebrow, title `Organizations notified included:`, telephone glyph, rule, eight rows in the **Plain** state (all eight Caption dark), the ninth slot with its row rule and nothing on it. No number, tick, tick box, red line or cursor |
| Lit band | design sheet "Lit": Amber 2 at 35 % behind slot 4, x 301.2 to 1414.8, 70.4 px tall on centre y 506.8, `scaleX` 0 to 1 from the left (`transformOrigin:"left center"`, set at timeline 0) |
| List source | credit corner, left 96, bottom 60, source-line type (design sheet section 10): `Disaster Research Center, 1966, p. 14` |

Part B (comp 5.34 to 11.47):
| Element | Px |
|---|---|
| Heading | left 96, top 140: `11 breaks in major lines`, Arial Black 900 60 px, Headline white |
| Count | left 96, top 232: a number in Arial Black 900 140 px, Headline white, in a box 230 px wide (so `54` does not move the label). It reads `0` to `54`, written by the fall loop below |
| Count label | left 340, top 316: `steel towers down`, Arial 700 34 px, Body light |
| Towers | 54 inline copies of the `dw-...` group of `media/drawings/steel-tower.svg` in one full-frame `<svg>`, each in a static wrapper `translate(X Y) scale(0.36)`, lines Body light, `stroke-width="6"` (4.5 on the two braces). Box left X = 100 + 83 x column (column 0 to 17: 100, 183, ... 1511); box top Y = 502.4, 642.4, 782.4 for rows 1 to 3 (base lines y 560, 700, 840). Tower n (1 to 54) is row by row, left to right. The last box ends at x 1539.8; the last fallen tower's tip is at x 1583.0, left of the corner |
| Fall | each tower's inner group turns 0 to 90 degrees about its base centre, `svgOrigin` in the SVG's own user units: (X + 14.4, base y), set once at build before any tween. A fallen tower lies on its base line, y band 545.6 to 574.4 for row 1, 685.6 to 714.4 for row 2, 825.6 to 854.4 for row 3 |
| Report label | left 96, top 900: `Indiana · reported by the Indiana and Michigan Electric Company`, Arial 700 26 px, Body light |
| Source line | credit corner, left 96, bottom 60: `Disaster Research Center, 1966, p. 16` (it replaces the list's line; one source at a time) |

## 4. Must be true in the picture
1. The lit row is `Indiana and Michigan Electric Company`, slot 4, and no other row is lit. The sheet is the study's "included" list: no numbering, no tick box, no count of rows.
2. There are exactly 54 towers, 18 in each of three rows. All 54 fall. The count reads `54` when the last one starts to fall and never shows a larger number.
3. The heading reads `11 breaks in major lines`. No drawing shows 11 of anything: the breaks are a figure, the towers are the towers.
4. The label reads `Indiana · reported by the Indiana and Michigan Electric Company`. Both figures stand as the company's report, not as our count.
5. No map, no state outline, no place dot, no line joining the towers. Nothing of the study's footnote for this line is on screen.
6. A tower is Body light standing and Label grey lying down. No tower is red and none is amber. Red means "nobody was told" and has no place here.
7. A fallen tower never overlaps a standing one (11.0 px clear), and no tower, standing or fallen, is under the heading, the count, the labels or the source line.
8. The list and the towers are never on screen together: the sheet has faded before the heading rises.
9. Nothing appears before its spoken word: the heading on "11", the towers standing on "lines", the falls and the count on "54". Nothing of ours in x >= 1600, y >= 680.
10. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: `SOUTH BEND WEATHER BUREAU · BY TELEPHONE` · `Organizations notified included:` · rows `State Police` · `Sheriffs' Departments` · `City Police Departments` · `Indiana and Michigan Electric Company` · `Red Cross` · `Specified radio and TV stations` · `Flying services` · `Airlines` · `Disaster Research Center, 1966, p. 14` · `11 breaks in major lines` · `0` to `54` · `steel towers down` · `Indiana · reported by the Indiana and Michigan Electric Company` · `Disaster Research Center, 1966, p. 16`.
Cue words and times are from `audio/a3-s10.words.json` (29 words), read on 12 Oct 26. t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A3-S10 -0.38) plus the word's time; the first word uses the table's "first sound" (0.00). Retime from the word, never from the seconds. The transcript writes "eleven" as `11` and "fifty four" as `54`.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A3-S10 | 0 | One | 0.38 | 0.00 | first frame: ground, the list in the Close state with all eight rows plain, the list's source line. No band |
| 1 | A3-S10 | 8 | power | 2.28 | 1.90 | the Lit band wipes onto `Indiana and Michigan Electric Company` (0.3 s) and stays |
| 2 | A3-S10 | 10 | Indiana | 3.62 | 3.24 | the other seven rows' text goes from Caption dark to Caption dark sub (0.3 s); the lit row stays Caption dark |
| 3 | A3-S10 | 14 | It | 5.72 | 5.34 | the sheet, its band and the list's source line fade out in place (0.3 s, gone at 5.64) |
| 4 | A3-S10 | 16 | 11 | 6.22 | 5.84 | the heading `11 breaks in major lines` rises (`y:30` to 0 with the fade, 0.4 s, power3.out); the source line `Disaster Research Center, 1966, p. 16` fades in |
| 5 | A3-S10 | 21 | lines | 7.58 | 7.20 | the 54 towers fade in standing, row 1, then row 2, then row 3, 0.12 s apart, 0.3 s each (all standing by 7.74) |
| 6 | A3-S10 | 23 | Indiana | 8.10 | 7.72 | the report label fades in (0.3 s) |
| 7 | A3-S10 | 25 | 54 | 9.16 | 8.78 | the count appears at `0` and the towers fall in order: tower n starts at 8.78 + 0.03 x (n - 1), turns 90 degrees in 0.2 s (power2.in) and its lines go to Label grey as it lands; the count shows n from the moment tower n starts. Build the 54 tweens in a loop from one start time and one beat, so a retime moves them together |
| 8 | A3-S10 | 26 | steel | 9.62 | 9.24 | the count label `steel towers down` fades in (0.2 s) |
| 9 | A3-S10 | 28 | down. | 10.32 | 9.94 | nothing new starts: 39 towers have begun to fall by this word. The count reaches `54` at 10.37 and the last tower lands at 10.57. Hold to 11.47: 54 grey towers lying down, `54`, the heading, both labels |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a3s10-towers.html` is the only file the builder writes; `data-composition-id="g-a3s10-towers"`, `data-duration="11.47"`; id prefix `tow-`; root `<div id="tow-root" ...>` styled through `#tow-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0. Do not edit `index.html`.
The 54 towers are placed by a loop in the comp's own script from the table in section 3 (one group markup, 54 instances, ids `tow-t1` to `tow-t54`). That is arithmetic on this brief's numbers inside the comp, not a script that authors the file.
**Base it copies:** the list sheet markup and the Lit band of the built `compositions/g-t1s3-list.html` and `compositions/g-i1s5-onair.html`, in the Close state those comps use, on the canvas ground. The tower is new here; `compositions/g-a5s15-dark.html` (wave 4) uses the same drawing, one tower leaning. Nothing copies this comp.
**Assets (paths from the episode folder; confirmed on disk 12 Oct 26):**
- `media/drawings/steel-tower.svg` (object 80 x 160, viewBox -6 -6 92 172, file 92 x 172, line 4, braces 3; the whole group tips about the base centre (40, 160)). Inlined 54 times at scale 0.36, ids under `tow-`; mount rules in `media/drawings/README.md`, which wins over any number here.
- The sheet's telephone glyph is the drawn telephone of `media/drawings/telephone.svg` (file 102 x 106), as `g-t1s3-list.html` inlines it.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a3s10-towers`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `graphics_qc` flat-type may name this comp for the typed sheet (plan rule 10): state it in the receipt, do not restyle.

## 7a. Done line
All seven lines of template section 7a. Line 2 here: state the measured fill for part B at 8.00 (54 standing) and at 11.00 (54 fallen). Line 4 here: every tower's rotation and `svgOrigin` are set at timeline 0; capture 9.60 (mid run) both ways and count the fallen and the standing towers in each frame: the two counts must match each other and the number shown. Line 6 here: the 54 box positions, the fallen tip of the last tower, the 11.0 px clearance and the count's end time are computed by a script from this brief's table and stated in the receipt.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): the list close, eight plain rows, the source line, no band. Then settled frames: 2.40 (band on the power company's row), 3.80 (the other seven rows grey, still readable on the paper), 5.70 (sheet gone, empty ground for a moment), 6.40 (heading), 7.90 (54 towers standing in three rows of 18: count them; report label on), 9.00 (count running, the first towers of row 1 down), 9.60 (mid run: fallen plus standing is 54, the count matches the fallen), 10.70 (all 54 down, `54`), 11.40 (hold: nothing in the corner, no tower under a label).
