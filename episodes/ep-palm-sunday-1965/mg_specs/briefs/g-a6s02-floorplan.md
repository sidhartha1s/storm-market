Host: id=g-a6s02-floorplan file=compositions/g-a6s02-floorplan.html start=1016.00 (timeline-map.md table 1, read 12 Oct 26 19:27; the mount in index.html wins) duration=10.15 s track=2

# g-a6s02-floorplan · A6-S2 · the teletype several doors from the announcer, and the alarm that reaches him (wave 5, graphic)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 7, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21; section 3a row DR-01. Times: `mg_specs/timeline-map.md` tables 1 and 5. Drawings: `media/drawings/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). A shared drawing is read alone at the size it is mounted (rule 11: the teletype at 168 px, the microphone at 108 px). A flash is a stroke or fill change, never a scale pop (rule 12: the doors' pulse, the lamp). A beat count is checked against its spoken window (rule 13: three door pulses of 0.4 s, started 0.2 s apart, are over 0.8 s after the first starts, inside the 0.88 s between "doors" and "announcer").
**Spoken (A6-S2):** "The report describes weather teletypes sitting several doors away from the announcer. So it asked stations to put an alarm on the machine, one that goes off where the announcer sits."
**One look:** a floor plan with a teletype at one end and a microphone at the other, three doors between; then a wire runs through the doors and a lamp lights beside the microphone.

## 0. What this graphic claims
The survey report says weather teletypes at news outlets sat several doors away from the announcer's position. Its first recommendation asks those outlets to fit the machines with positive alerting devices, remoted to the announcer's position where necessary. This is what the report asked for, not a record of any station doing it.

## 1. Source
- `edit_script.md` A6-S2, Rows [survey printed p. 4: "located several doors away from the announcer's position"; "such as an alarm indicator lamp or warning bell"] · [G, Rec. 1; survey printed p. 2]. Picture note: "a floor plan we draw: a teletype in one room, three doors, the announcer's booth with the drawn microphone at the far end. On the second sentence a bell mark is drawn on the teletype and a line runs from it through the doors to a lamp beside the microphone; the lamp lights amber. Small paper card with the page's own words: 'positive alerting devices (remoted to the announcer's position where necessary)'."
- The card's words, read on `media/docs/survey-p2-rec1-crop.png` (lines 5 and 6 of recommendation 1, 12 Oct 26): `positive alerting devices (remoted to the` / `announcer's position where necessary)`. The comp retypes them on a paper strip; it does not mount the crop (the comp before it, `g-a6s01-recs`, shows the page).
- "Several doors" is the report's phrase. Three doors is the Picture note's drawing of it: the plan is SCHEMATIC, NOT TO SCALE, and is no station's building.
- No photograph and no page image is mounted. Drawings confirmed on disk 12 Oct 26: `media/drawings/teletype.svg` (784 bytes), `media/drawings/microphone.svg` (689 bytes).

## 2. Datum, scale, orientation
- A plan view, read left to right: the teletype's room at the left end, the announcer's booth at the right end. The wire's line, y 540, is the datum: it runs through the middle of the three door openings.
- Four rooms in one strip, x 200 to 1520, y 380 to 700, each 330 px wide. Three inner walls at x 530, 860 and 1190; each has a door opening from y 505 to y 575.
- The teletype and the microphone are the files' front elevations, set in their rooms as symbols (a plan with pictures in it, as a fire plan has). Teletype at scale 1.2 (object box 168 x 168, lines 4.8 px). Microphone at scale 0.9 (object box 108 x 207, lines 3.6 px).
- The walls, doors, bell, wire and lamp have no file: they are the px lines of section 3, in the hand of design sheet section 7 (4 px, round caps and joins, right angles and circular arcs only).
- The strip ends at x 1520: nothing of ours is in x >= 1600, y >= 680.

## 3. Geometry (screen px)
Ground: the canvas gradient, on from frame 0. All plan lines sit in one full-frame `<svg>`.
| Element | Px |
|---|---|
| Outer walls | rect x 200 to 1520, y 380 to 700, 4 px Body light, no fill |
| Inner walls | three lines at x 530, 860, 1190, each in two parts: y 380 to 505 and y 575 to 700. 4 px Body light |
| Doors | at each inner wall, a leaf line from (x, 505) to (x - 70, 505) and a swing arc, radius 70, centre (x, 505), from (x - 70, 505) to (x, 575). 3 px Label grey. All three open to the left |
| Teletype | `teletype.svg` inline, `<g transform="translate(281 456) scale(1.2)">`: box x 281 to 449, y 456 to 624. Lines Body light, paper Panel dark (unlit) |
| Microphone | `microphone.svg` inline, `<g transform="translate(1301 436) scale(0.9)">`: box x 1301 to 1409, y 436 to 643. Lines Body light, body Panel dark, its own ON AIR lamp unlit for the whole comp |
| Room labels | Arial 700 26 px, Body light: `weather teletype` centred on x 365, top 716; `the announcer` centred on x 1355, top 716 |
| Schematic line | left 200, top 322, Arial 700 22 px, Label grey: `schematic · not any one station's building` |
| Bell mark | above the teletype, centred on x 365: dome, a half circle of radius 20 from (345, 436) over (365, 416) to (385, 436); rim line (339, 436) to (391, 436); clapper, a circle of radius 5 at (365, 445). 4 px Body light, dome fill Panel dark |
| Wire | one line at y 540 from (449, 540), the teletype's right edge, to (1239, 540), the lamp's left edge. 4 px Body light. It passes through the three door openings |
| Alarm lamp | circle radius 16 at (1255, 540), 4 px Body light, fill Panel dark; lit: fill Amber 2 and the stroke Headline white |
| Source line | design sheet section 10, left 96, bottom 60: `Weather Bureau survey report, 1965, p. 4`. It leaves when the strip arrives (the strip carries the attribution; one source line per frame) |
| Quote strip | Beige polaroid, left 96, top 800, 1180 x 180 (right 1276, bottom 980), `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`. Quote in Georgia 40 px, Caption dark, line height 52 px, left 136: line 1 `“positive alerting devices (remoted to the` top 820, line 2 `announcer's position where necessary)”` top 872. Attribution, Arial 700 22 px, Caption dark sub, tracking 2, left 136, top 938: `Weather Bureau survey report, 1965, p. 2 · recommendation 1` |

## 4. Must be true in the picture
1. The teletype and the microphone are in different rooms, at opposite ends, with three doors between them. No door is numbered and no distance is given.
2. Before the word "alarm" there is no bell, no wire and no lamp: the two ends are not joined by anything.
3. The wire runs from the teletype to the lamp, and the lamp is beside the microphone, in the announcer's room. The lamp lights only after the wire has reached it.
4. **The microphone's own ON AIR lamp stays unlit.** The alarm lamp is a separate circle. Nothing in this comp says a warning was broadcast.
5. The bell is a mark, drawn still: no ring lines, no shake.
6. The strip's words are the page's, in quotation marks, with their page and recommendation number. The comp says "the report asked"; nothing says a station fitted the alarm.
7. The plan is marked schematic for the whole comp. No station name, no call letters, no town, no county chip.
8. No person is drawn in any room.
9. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680.

## 5. Text (exact) and cues
Text: `weather teletype` · `the announcer` · `schematic · not any one station's building` · `“positive alerting devices (remoted to the` / `announcer's position where necessary)”` · `Weather Bureau survey report, 1965, p. 2 · recommendation 1` · `Weather Bureau survey report, 1965, p. 4`.
Cue words and times are from `audio/a6-s2.words.json` as it stood on 12 Oct 26 at 19:27 (wav 9.93 s; the transcript hears "asks" where the script says "asked"). "t from comp start" is `mg_specs/timeline-map.md` table 5: the segment's "wav start inside the composition" (-0.51) plus the word's time; the first word takes the "first sound" column (0.00). Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A6-S2 | 0 | The | 0.00 | 0.00 | first frame: ground, the empty plan (outer walls, inner walls, three doors), the schematic line, the source line |
| 1 | A6-S2 | 4 | teletypes | 1.74 | 1.23 | the teletype draws on in the left room (`strokeDashoffset`, 0.5 s); `weather teletype` rises under it (`y:16` set at 0, then `to`, 0.3 s) |
| 2 | A6-S2 | 7 | doors | 3.08 | 2.57 | the three doors pulse left to right, 0.2 s apart: each leaf and arc goes Label grey to Headline white (0.15 s) and back (0.25 s) |
| 3 | A6-S2 | 11 | announcer. | 3.96 | 3.45 | the microphone draws on in the right room (0.5 s); `the announcer` rises under it |
| 4 | A6-S2 | 15 | stations | 5.44 | 4.93 | the source line leaves (0.2 s); the quote strip rises (`y:60` set at 0, then `to y:0, autoAlpha:1`, 0.4 s, power3.out) |
| 5 | A6-S2 | 19 | alarm | 6.30 | 5.79 | the bell mark draws on above the teletype (0.4 s) |
| 6 | A6-S2 | 23 | one | 7.64 | 7.13 | the wire draws from the teletype through the three doors to the lamp (`strokeDashoffset`, 0.9 s, `ease:"none"`, ending 8.03); the lamp's outline fades in as the wire arrives |
| 7 | A6-S2 | 29 | announcer | 8.76 | 8.25 | the lamp lights: fill to Amber 2, stroke to Headline white (0.25 s). Hold to the last frame (10.15) |
The hold from 8.5 to 10.15 is carried by the lamp: its fill steps Amber 2 at 1.0 to 0.55 and back, twice (0.4 s each way, finite), a fill change only.

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a6s02-floorplan.html` is the only file the builder writes; `data-composition-id="g-a6s02-floorplan"`; id prefix `fpl-`; root `<div id="fpl-root" ...>` styled through `#fpl-root` (plan rule 3 overrides the template's `id="root"`). Full frame, opaque, own ground on from frame 0.
**Base it copies:** `acts-plan.md` names none for this row. The inline drawing mount is that of `mg_specs/briefs/g-a1s05-clocks.md` (a file's `<g class="dw-...">` inside a static `<g transform=...>` wrapper, GSAP on the children only); the quote strip is design sheet section 9 as written in `mg_specs/briefs/g-a2s15-old.md` (Beige polaroid strip, Georgia 40 px, attribution under it). Nothing later copies this comp.
The files carry classes only: every id takes the `fpl-` prefix. The lamp's centre dot, if drawn as a zero-length line, fades in; it takes no draw-on.
**Assets mounted (paths from the episode folder, each confirmed on disk 12 Oct 26):**
- `media/drawings/teletype.svg` (DR-01, object box 140 x 140, viewBox -6 -6 152 152, line 4), inlined at scale 1.2.
- `media/drawings/microphone.svg` (object box 120 x 230, viewBox -6 -6 132 242, line 4), inlined at scale 0.9.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a6s02-floorplan`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `python3`, never `python`.

## 7a. Done line
All seven lines of template section 7a. Line 2 (fill): state the measured figure at 9.0, when the plan, the strip and the lit lamp are all on. Line 3: frame 0 shows the empty plan, not a bare ground. Line 5: neither room label sits under the wire, a wall or a door arc; the schematic line clears the top wall. Line 6: the three wall positions (530, 860, 1190) are the strip's width divided by four, by script, stated in the receipt. Line 7 does not apply: the comp is opaque.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): the empty plan with three doors, the schematic line, the source line; no teletype, no microphone. Then one settled frame per cue: 1.90 (teletype and its label), 2.75 (middle door at its brightest, same size as at rest), 3.40 (doors back to Label grey), 4.10 (microphone and its label, nothing joining the ends), 5.50 (strip in place, source line gone), 6.30 (bell), 7.60 (wire half way: through the first door, short of the third), 8.10 (wire at the lamp, lamp unlit), 8.60 (lamp Amber 2, the microphone's own lamp still unlit), 10.10 (last frame). Each cue second in both seek orders.
