Host: id=g-a6s07-power file=compositions/g-a6s07-power.html start=1060.56 (timeline-map.md table 1, read 12 Oct 26 19:27; the mount in index.html wins) duration=12.44 s track=2

# g-a6s07-power · A6-S7 · emergency power for every office, and a screen for the office with no radar (wave 5, drawing then map)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 7, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21; section 3a rows DR-01, DR-02 and DR-05; section 3b row BM-2. Times: `mg_specs/timeline-map.md` tables 1 and 5. Drawings: `media/drawings/README.md`. Map facts: `media/maps/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). A shared drawing is read alone at the size it is mounted (rule 11: the generator at 192 px, the scope at 120 px, the desk at 360 px). A flash is a stroke or fill change, never a scale pop (rule 12). Map geometry comes from a file, nothing is placed by eye (rule 14). Maps: no Alto on any map; inlined map ids take this comp's prefix; the first frame read checks line weight (rule 20; this comp has no zoom).
**Spoken (A6-S7):** "Power failures at Weather Bureau offices brought a call for emergency power at every office. And any office leaning on another city's radar, as South Bend was, was to get a screen showing that radar."
**One look:** a dark office lights when a generator is set beside it; then a map, and a small screen at South Bend tied to a radar in another city.

## 0. What this graphic claims
The survey team recommended emergency power at all Weather Bureau offices (recommendation 8), and a remote radar repeater scope for any office that depends on a radar in another locality, as South Bend did (recommendation 5). Both are things the report asked for.

## 1. Source
- `edit_script.md` A6-S7, Rows [G, Rec. 8; survey printed pp. 2 and 10: lost "in some instances due to power failure"] · [G, Rec. 5; survey printed p. 2: "remote narrow bandwidth radar repeater scope"] (asked for, not done). Picture note: "a drawn Weather Bureau office, dark, no place label; a drawn generator mark comes in beside it and the room lights. On the second sentence our map: a small screen is drawn at South Bend's dot, joined by one line to another city's radar ring. Small paper cards for recommendations 8 and 5."
- The two recommendations, read by eye on `media/docs/survey-pdf-08-orig.png` (2550 x 3300, survey printed p. 2) on 12 Oct 26, every word legible:
  - 8: `Provide adequate emergency power for all radar installations and all communications equipment (including teletypewriters) at all Weather Bureau offices.`
  - 5: `Provide remote narrow bandwidth radar repeater scope (or scopes) to each Weather Bureau office in tornado-prone areas where such office is dependent for protection on a radar in another locality. (Figure 5 is a map of the existing radar network.)`
- The paper cards carry an unbroken run of each: `adequate emergency power for all radar installations and all communications equipment` and `remote narrow bandwidth radar repeater scope`. The page image is a source only; this comp does not mount it.
- The other city: the narration names none. The ring stands at Chicago's dot, the one radar office a source row gives as speaking to South Bend (`mg_specs/briefs/g-a2s01-radar.md`, A2-S2), and it is labelled by recommendation 5's own words, not by a city name.
- Map: `media/maps/midwest-states.svg` (BM-2, viewBox -980 -1280 2220 2560, 148,112 bytes). Points from `media/maps/README.md` (map units): South Bend 462.2, 188.5; Chicago 282.2, 158.9.
- Drawings confirmed on disk 12 Oct 26: `media/drawings/desk.svg` (1,935 bytes), `media/drawings/teletype.svg` (784), `media/drawings/generator.svg` (1,020), `media/drawings/generator-filled.svg` (888), `media/drawings/radar-scope.svg` (988).

## 2. Datum, scale, orientation
- Part 1 (first sentence) is a flat front view of one room standing on a floor line, y 820.
- Part 2 (second sentence) is the map, north up, in an inline SVG with viewBox `122 9 500 300` mounted at left 96, top 300, 1000 x 600: 2.0 px per map unit, screen x = 96 + (u - 122) x 2, screen y = 300 + (v - 9) x 2. By script: Chicago is at screen (416.4, 599.8), South Bend at (776.4, 659.0).
- Desk at scale 1.2 (object box 360 x 180, lines 4.8 px; its telephone rises above the box). Teletype at scale 1.0 (140 x 140). Generator at scale 1.6 (192 x 128, lines 6.4 px). Scope at scale 0.6 (120 x 120, lines 2.4 px).
- The room, its ceiling lamp and the generator's cable have no file: they are the px lines of section 3, in the hand of design sheet section 7.
- The generator's box ends at x 1372 and the map at x 1096: nothing of ours is in x >= 1600, y >= 680.

## 3. Geometry (screen px)
Ground: the canvas gradient, on from frame 0.
| Element | Px |
|---|---|
| Source line | design sheet section 10, left 96, bottom 60: `Weather Bureau survey report, 1965, pp. 2 and 10`. On for the whole comp |
| Strip slot (both paper cards) | Beige polaroid, left 96, top 80, 1180 x 190 (right 1276, bottom 270), `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`. Quote in Georgia 40 px, Caption dark, line height 52 px, left 136. Attribution Arial 700 22 px, Caption dark sub, tracking 2, left 136, top 222 |
| Card 8 | line 1 `“adequate emergency power for all radar installations` top 100, line 2 `and all communications equipment”` top 152; attribution `recommendation 8` |
| Card 5 | one line `“remote narrow bandwidth radar repeater scope”` top 126; attribution `recommendation 5` |
| Floor line (part 1) | y 820, x 96 to 1560, 4 px, Label grey |
| Room | rect x 420 to 1100, y 380 to 820: walls and ceiling 4 px, fill Panel dark. Dark: lines Label grey. Lit: lines Body light |
| Ceiling lamp | cord (760, 380) to (760, 440); shade, closed path (744, 440), (776, 440), (790, 470), (730, 470). 4 px, same stroke as the room; shade fill Panel dark, lit Amber 2 |
| Desk | `desk.svg` inline, `<g transform="translate(480 640) scale(1.2)">`: box x 480 to 840, y 640 to 820 |
| Teletype | `teletype.svg` inline, `<g transform="translate(900 680)">`: box x 900 to 1040, y 680 to 820. Unlit: paper Panel dark. Lit: paper Amber 2, bars Caption dark (the look of `teletype-lit.svg`) |
| Office label | centred on x 760, top 846, Arial 700 26 px, Body light: `a Weather Bureau office` |
| Generator | `generator.svg` inline, `<g transform="translate(1180 692) scale(1.6)">`: box x 1180 to 1372, y 692 to 820. Outline first (the file's own look: the one that is not there); filled is the look of `generator-filled.svg` (box and housing Amber 2, bolt and hub Caption dark), reached by tweening `dw-lamp` fills and `dw-ink` strokes |
| Cable | line (1180, 800) to (1100, 800), 4 px Body light |
| Map (part 2) | inline `<svg>` at left 96, top 300, 1000 x 600, viewBox `122 9 500 300`, holding BM-2's four state paths `st-il`, `st-in`, `st-mi`, `st-wi` with ids prefixed (`pwr-st-il` ...). Lines and colours as `media/maps/README.md`: stroke `#dfe7ee`, 2 px, fill `#15202b`, `vector-effect="non-scaling-stroke"` kept |
| Radar ring | at (416.4, 599.8): two circles radius 46 and 26, Body light 3 px, and one sweep line from the centre to the outer circle (the ring of `mg_specs/briefs/g-a2s01-radar.md`) |
| Ring label | centred on x 416, top 656, Arial 700 22 px, Body light: `a radar in another locality` |
| South Bend | dot radius 6, `#dfe7ee`, at (776.4, 659.0); label `South Bend`, Arial 700 26 px, Headline white, left 796, top 676 |
| Repeater scope | `radar-scope.svg` inline, `<g transform="translate(840 480) scale(0.6)">`: box x 840 to 960, y 480 to 600, centre (900, 540). Group stroke Body light with `stroke-dasharray="6 6"` (file units); `dw-glow` hidden for the whole comp; `dw-sweep` turns about the scope's centre |
| Scope label | centred on x 900, top 438, Arial 700 22 px, Label grey: `asked for: a repeater scope` |
| Leader | 3 px Body light line from South Bend's dot to the scope's rim, along the line joining the dot and the scope's centre |
| Link | 4 px Body light dashed line (`stroke-dasharray` 14 12) from the ring's outer circle to the scope's rim, along the line joining the two centres, (416.4, 599.8) and (900, 540). End points by the builder's script |

## 4. Must be true in the picture
1. Part 1: the room is dark (lines Label grey, no amber) until the generator turns Amber 2; only then do the lamp shade and the teletype's paper light. The order is generator, cable, room.
2. The office carries no place: its label is `a Weather Bureau office`. No "South Bend", no "Fort Wayne", no county, no clock, no time in part 1.
3. Part 2: **the screen and the link are dashed and never amber.** They are what the report asked for. Nothing says the scope was installed, and the scope's label says `asked for`.
4. South Bend has a dot and no radar ring of its own. The ring stands at the other place only.
5. The ring's label is `a radar in another locality`. No city name is typed beside the ring. No ring has a range in miles.
6. Each paper card holds an unbroken run of the page's own words, in quotation marks, with its recommendation number. Card 8 is on only in part 1 and card 5 only in part 2.
7. No Alto, no tornado mark, no track on the map. No person in the room.
8. A flash is a fill or stroke change; nothing changes size (rule 12).
9. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680.
10. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Where this brief's reveal order leaves one, the builder stages the earlier steps as rule 22 says and keeps every cue time and the last-frame geometry.

## 5. Text (exact) and cues
Text: `a Weather Bureau office` · `“adequate emergency power for all radar installations` / `and all communications equipment”` · `recommendation 8` · `“remote narrow bandwidth radar repeater scope”` · `recommendation 5` · `a radar in another locality` · `South Bend` · `asked for: a repeater scope` · `Weather Bureau survey report, 1965, pp. 2 and 10`.
Cue words and times are from `audio/a6-s7.words.json` as it stood on 12 Oct 26 at 19:27 (wav 12.06 s). "t from comp start" is `mg_specs/timeline-map.md` table 5: the segment's "wav start inside the composition" (-0.33) plus the word's time; the first word takes the "first sound" column (0.00). Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A6-S7 | 0 | Power | 0.00 | 0.00 | first frame: ground, floor line, the dark room with its lamp, desk and teletype (all Label grey), the source line |
| 1 | A6-S7 | 5 | offices | 1.74 | 1.41 | `a Weather Bureau office` rises under the room (`y:16` set at 0, then `to`, 0.3 s) |
| 2 | A6-S7 | 10 | emergency | 3.12 | 2.79 | the generator draws on beside the room, outline only (`strokeDashoffset`, 0.35 s) |
| 3 | A6-S7 | 11 | power | 3.48 | 3.15 | the generator fills Amber 2 (0.2 s); the cable draws to the wall (0.2 s); from 3.50 the room lights: room, lamp, desk and teletype lines to Body light, shade and teletype paper to Amber 2 (0.3 s) |
| 4 | A6-S7 | 13 | every | 4.16 | 3.83 | card 8 rises into the strip slot (`y:60` set at 0, then `to y:0, autoAlpha:1`, 0.4 s, power3.out) |
| 5 | A6-S7 | 15 | and | 5.62 | 5.29 | part 1 leaves: room, generator, cable, label and card 8 fade out (0.3 s); the four state outlines fade in (0.4 s) |
| 6 | A6-S7 | 20 | another | 7.06 | 6.73 | the radar ring draws on at the other place (0.4 s), its sweep makes one full turn (1.6 s, `ease:"none"`), `a radar in another locality` fades in under it |
| 7 | A6-S7 | 24 | South | 8.54 | 8.21 | South Bend's dot and `South Bend` come up (0.3 s) |
| 8 | A6-S7 | 31 | screen | 10.38 | 10.05 | the scope draws on by South Bend with its leader (0.4 s), dashed; the dashed link draws from the ring to the scope (0.5 s); `asked for: a repeater scope` fades in; card 5 rises into the strip slot |
| 9 | A6-S7 | 34 | radar. | 11.24 | 10.91 | the ring's sweep and the scope's sweep make one turn together (1.4 s, `ease:"none"`, ending 12.31). Last frame 12.44 |
`a Weather Bureau office` and `asked for: a repeater scope` are this brief's labels, not the Picture note's: the first says what the drawing is without placing it, the second keeps the scope from reading as installed. If the lead strikes either, nothing else moves.

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a6s07-power.html` is the only file the builder writes; `data-composition-id="g-a6s07-power"`; id prefix `pwr-`; root `<div id="pwr-root" ...>` styled through `#pwr-root` (plan rule 3 overrides the template's `id="root"`). Full frame, opaque, own ground on from frame 0.
**Base it copies:** `acts-plan.md` names none for this row. It takes the inline drawing mount of `mg_specs/briefs/g-a1s05-clocks.md`, the radar ring of `mg_specs/briefs/g-a2s01-radar.md`, the inlining and prefixing of map paths from the map family base `mg_specs/briefs/g-a2s14-six.md`, and the quote strip of design sheet section 9. `g-a6s09-third` (wave 5) uses the same generator file to fill the outlines of A3-S15; nothing copies this comp.
Inline mounts: copy each file's `<g class="dw-...">` into the comp's own `<svg>` inside the static wrapper given in section 3; GSAP touches only the children. The files carry classes only: every id takes the `pwr-` prefix. `dw-sweep` and the ring's sweep line: `svgOrigin` set once at build, before any tween, in screen px ((900, 540) and (416.4, 599.8)). The map paths are copied from the file, never redrawn; only the four named states are inlined.
**Assets mounted (paths from the episode folder, each confirmed on disk 12 Oct 26):**
- `media/drawings/desk.svg` (object box 300 x 150, viewBox -6 -28 312 184, line 4), inlined at scale 1.2.
- `media/drawings/teletype.svg` (DR-01, object box 140 x 140, viewBox -6 -6 152 152), inlined at scale 1.0; its lit look is that of `media/drawings/teletype-lit.svg`, reached by tween.
- `media/drawings/generator.svg` (DR-05, object box 120 x 80, viewBox -6 -6 132 92), inlined at scale 1.6; its filled look is that of `media/drawings/generator-filled.svg`, reached by tween.
- `media/drawings/radar-scope.svg` (DR-02, object box 200 x 200, viewBox -6 -6 212 212), inlined at scale 0.6.
- `media/maps/midwest-states.svg` (BM-2): the paths `st-il`, `st-in`, `st-mi`, `st-wi`, inlined.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a6s07-power`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `python3`, never `python`.

## 7a. Done line
All seven lines of template section 7a. Line 2 (fill): state the measured figure at 4.6 (part 1 complete) and at 11.0 (part 2 complete). Line 3: frame 0 shows the dark room, not a bare ground. Line 5: no label sits under the link, the leader, a state outline or the ring; `South Bend` clears its dot and the leader. Line 6: the two map positions are computed by a script from the README's map units and the viewBox of section 2, and the link's and leader's end points from the centres and radii; all are stated in the receipt. Line 7 does not apply: the comp is opaque.

## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): the dark room, no amber, no generator, no card. Then one settled frame per cue: 1.90 (office label), 3.10 (generator outline, room still dark), 3.95 (generator Amber 2, cable, room lit), 4.40 (card 8 in the slot), 5.90 (part 1 gone, four state outlines; read the line weight), 7.30 (ring, its label), 8.70 (South Bend dot and label, no ring on it), 10.80 (scope, leader, dashed link, scope label, card 5), 11.60 (both sweeps mid turn), 12.40 (last frame). Each cue second in both seek orders.
