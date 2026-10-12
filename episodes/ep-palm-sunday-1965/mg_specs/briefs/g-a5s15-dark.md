Host: id=g-a5s15-dark file=compositions/g-a5s15-dark.html start=948.26 (timeline-map.md table 1, read 12 Oct 26 19:27; the mount in index.html wins) duration=7.71 s track=2

# g-a5s15-dark · A5-S15 · one power company's lines go, and its customers sit in the dark (wave 4, drawing)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 7, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21; section 3a row DR-04. Times: `mg_specs/timeline-map.md` tables 1 and 5. Drawings: `media/drawings/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). A shared drawing is read alone at the size it is mounted (rule 11: the house at 338 px, the tower at 240 px). A flash is a stroke or fill change, never a scale pop (rule 12). A beat count is checked against its spoken window (rule 13: three houses in 0.9 s, inside the 1.5 s the last clause gives).
**Spoken (A5-S15):** "Curran later wrote that one of Fort Wayne's two power companies lost its high voltage lines, and none of its customers had power."
**One look:** a steel tower tips over, and three houses stand in a row with every window dark.

## 0. What this graphic claims
By John Curran's later account, one of Fort Wayne's two power companies lost its high voltage transmission lines, and none of that company's customers had power. It is a recollection, not a log entry, and it says nothing about the Weather Bureau office's own supply.

## 1. Source
- `edit_script.md` A5-S15, Rows [D, Curran; IWX: "Fort Wayne's power was provided by two utility companies"; "The other utility, Indiana and Michigan, lost their high voltage transmission lines"; "none of the I & M customers in Ft. Wayne had power"] (written later; no source says the office was one of those customers). Picture note: "a row of three drawn houses at night, every window dark; behind them one drawn steel tower, leaning. Small line 'John Curran's recollection, not a log'. Nothing ties the towers to the office's own power."
- No photograph and no page is mounted, so no `provenance.csv` row applies.
- Drawings, confirmed on disk 12 Oct 26: `media/drawings/house.svg` (978 bytes; dark state, lines Label grey at 55 %, windows Panel dark), `media/drawings/steel-tower.svg` (713 bytes; DR-04, lattice tower, braces 3 units).
- The source gives no count of towers, no count of houses and no clock time. One tower and three houses are a picture of "lines" and "customers", not a count.

## 2. Datum, scale, orientation
- Ground line y 820, the datum: the three houses and the tower's feet stand on it.
- Houses: the drawing at scale 1.3 (object box 338 x 325, lines 5.2 px, aerial rising 44.2 px above the box).
- Tower: the drawing at scale 3.0 (object box 240 x 480, lines 12 px at the file's weight, so the builder sets `stroke-width="2"` on the `dw-...` group and 1.5 on the two brace paths: 6 px and 4.5 px on screen, README "line weight by size").
- The lean: 12 degrees clockwise about the tower's right foot, screen (1500, 820). Upright, its corners are top left (1260, 340), top right (1500, 340), left foot (1260, 820). Leaning: top left (1365, 301), top centre (1482, 326), top right (1600, 350), left foot (1265, 770), right foot unmoved. The left foot lifts 50 px off the ground line.
- The tower is drawn first in the markup, the houses after it: the third house stands in front of the tower's left foot.
- Presenter corner: the leaning tower reaches x 1600 only at y 350; nothing of ours is in x >= 1600, y >= 680.

## 3. Geometry (screen px)
Ground: the canvas gradient (design sheet section 2) on the root, on from frame 0. It is night: no sky, no moon, no stars, no second colour.
| Element | Px |
|---|---|
| Ground line | y 820, x 96 to 1560, 4 px, Label grey |
| Tower | `steel-tower.svg` inline in a full-frame `<svg>`, `<g transform="translate(1260 340) scale(3)">`; upright box x 1260 to 1500, y 340 to 820. Group stroke Body light, `stroke-width="2"` (braces 1.5). The tipping part is the file's whole `dw-...` group, given the id `drk-tower`, `rotation` 0 to 12 with `svgOrigin:"1500 820"` set once at build |
| House 1 | `house.svg` inline, `<g transform="translate(150 495) scale(1.3)">`: box x 150 to 488, y 495 to 820, aerial top y 450.8 |
| House 2 | same file, `translate(540 495) scale(1.3)`: box x 540 to 878 |
| House 3 | same file, `translate(930 495) scale(1.3)`: box x 930 to 1268. It overlaps the tower's upright box by 8 px and is drawn after it |
| Recollection line | design sheet section 10 (the source line's place and type): left 96, bottom 60: `John Curran's recollection, not a log` |
The houses keep the file's dark state for the whole comp: stroke `#55606b`, windows `#15202b`. No label under any house, no label on the tower.

## 4. Must be true in the picture
1. **Every window of every house is dark at every frame.** No Amber 2 anywhere in this comp: not a window, not a lamp, not a spark.
2. One tower, and it leans; it does not fall flat, break or burn. Its end state is 12 degrees.
3. **Nothing joins the tower to anything.** No wire runs from it to a house, to the frame's edge or to an office. No Weather Bureau office, teletype or microphone is in this comp: the source does not say the office was one of those customers.
4. No name is on screen but Curran's: no "Indiana and Michigan", no "I & M", no "Fort Wayne" label, no county, no clock, no time.
5. The line `John Curran's recollection, not a log` is on from the first frame to the last.
6. Three houses, in a row, alike. None is singled out. No person, no figure at a window.
7. The tower's tip is a rotation, not a change of size (rule 12).
8. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680.

## 5. Text (exact) and cues
Text: `John Curran's recollection, not a log`. Nothing else is typed.
Cue words and times are from `audio/a5-s15.words.json` as it stood on 12 Oct 26 at 19:27 (wav 7.00 s). "t from comp start" is `mg_specs/timeline-map.md` table 5: the segment's "wav start inside the composition" (0.00) plus the word's time; the first word takes the "first sound" column (0.00). Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A5-S15 | 0 | Curran | 0.00 | 0.00 | first frame: ground, ground line, the recollection line, and the tower upright, already drawn |
| 1 | A5-S15 | 4 | one | 1.18 | 1.18 | the tower's lines go Body light to Headline white (0.3 s, a stroke change): this is the one company's line |
| 2 | A5-S15 | 11 | lost | 3.06 | 3.06 | the tower tips: `rotation` 0 to 12 about (1500, 820), 0.7 s, `power2.in`; then its stroke goes Headline white to Label grey (0.4 s) |
| 3 | A5-S15 | 17 | none | 5.08 | 5.08 | house 1 draws on (`strokeDashoffset`, longest line first, 0.5 s); house 2 from 5.28; house 3 from 5.48. All three complete by 5.98, all dark |
| 4 | A5-S15 | 20 | customers | 5.50 | 5.50 | no new mark: the row is completing under the word. Hold to the last frame (7.71) |
From step 3 the hold is carried by a slow drift of the whole drawing layer (the full-frame `<svg>`): `scale` 1.00 to 1.02 about the frame centre from 5.98 to 7.71, `ease:"none"`. The recollection line is on the HUD and does not move.
The lean in step 2 is this brief's reading of "leaning": the tower stands for one second so that "lost" has something to take away. If the lead wants it leaning from the first frame, steps 1 and 2 become one stroke change on "lost".

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a5s15-dark.html` is the only file the builder writes; `data-composition-id="g-a5s15-dark"`; id prefix `drk-`; root `<div id="drk-root" ...>` styled through `#drk-root` (plan rule 3 overrides the template's `id="root"`). Full frame, opaque, own ground on from frame 0.
**Base it copies:** the house mount and draw-on of `mg_specs/briefs/g-a1s05-clocks.md` (clock family base: `house.svg` inline in a static `<g transform=...>` wrapper, GSAP on the children only). `acts-plan.md` names no built file for this row. Nothing later copies this comp; `g-a3s10-towers` (wave 3) is the other user of the tower file and sets its own sizes.
Inline mounts: copy each file's `<g class="dw-...">` into the comp's own `<svg>` inside the wrapper given in section 3. The files carry classes only: every id takes the `drk-` prefix. `svgOrigin` for the tower is set once at build, before any tween, in screen px.
**Assets mounted (paths from the episode folder, each confirmed on disk 12 Oct 26):**
- `media/drawings/house.svg` (object box 260 x 250, viewBox -6 -42 272 298, line 4), inlined three times at scale 1.3.
- `media/drawings/steel-tower.svg` (DR-04, object box 80 x 160, viewBox -6 -6 92 172, line 4, braces 3), inlined at scale 3.0 with `stroke-width="2"`.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a5s15-dark`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `python3`, never `python`.

## 7a. Done line
All seven lines of template section 7a. Line 2 (fill): state the measured figure at 6.00, when the three houses and the tower are all on. Line 3: frame 0 shows the tower upright and the recollection line, not a bare ground. Line 4: the tip at 3.06 in both seek orders (the `svgOrigin` is set at build, never in a `from`). Line 6: the tower's leaning corners are computed by a script from scale 3.0, pivot (1500, 820) and 12 degrees, and stated in the receipt against section 2. Line 7 does not apply: the comp is opaque.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): tower upright in Body light, the recollection line, no house. Then one settled frame per cue: 1.60 (tower Headline white), 3.90 (tower at 12 degrees, left foot off the ground line, top right at about x 1600, y 350), 4.40 (tower Label grey), 6.10 (three houses complete, every window dark, house 3 in front of the tower's foot), 7.65 (last frame, drift only). Read on each: no amber, no wire, no label but the recollection line. Each cue second in both seek orders.
