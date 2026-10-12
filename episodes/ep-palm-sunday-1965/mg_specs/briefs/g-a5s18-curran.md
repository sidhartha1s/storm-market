Host: id=g-a5s18-curran file=compositions/g-a5s18-curran.html start=975.24 (timeline-map.md table 1, read 12 Oct 26 19:27; the mount in index.html wins) duration=20.33 s track=2

# g-a5s18-curran · A5-S18, A5-S19 · Curran sleeps through it, then finds the teletypes on an extension cord (wave 4, drawing)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 7, 8, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21; section 3a rows DR-01 and DR-09. Times: `mg_specs/timeline-map.md` tables 1 and 5. Drawings: `media/drawings/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). A shared drawing is read alone at the size it is mounted (rule 11: the clock at 186 px, the house at 364 px, the teletype at 196 px). A flash is a stroke or fill change, never a scale pop (rule 12).
**Spoken (A5-S18):** "Curran had finished his shift at four that afternoon, with no severe weather anywhere in Fort Wayne's area. He slept until a roommate woke him, around ten thirty."
**Spoken (A5-S19):** "He was back at midnight. The teletype machines were running on an extension cord from the aviation office down the hall, strung by a technician named Arnie Koch."
**One look:** a clock jumps from 4:00 to 10:30 beside a house that wakes up; then two lit teletypes in a dark room, fed by one cord from a box down the hall.

## 0. What this graphic claims
John Curran, the Fort Wayne observer, went off shift at 4:00 PM with no severe weather in his office's area and slept until about 10:30 PM. When he was back at midnight the office's teletypes were running on an extension cord strung down the hall from the FAA Flight Service Station by the technician Arnie Koch. All of it is his recollection.

## 1. Source
- `edit_script.md` A5-S18, Rows [E, Curran: "At the end of my shift no severe weather was in the Ft. Wayne County warning Area"; IWX, read by the fact check: asleep until a roommate woke him around 10:30 PM]. Picture note: "the name card for John Curran again. A drawn wall clock at 4:00 PM, then the drawn house with a dark window, then the clock at 10:30 PM and the window lit."
- `edit_script.md` A5-S19, Rows [E, Curran; IWX: "the electronics technician Arnie Koch had strung an extension cord down the hall from the FAA Flight Service Station"]. Picture note: "a drawn scene, because no picture of the office exists: a dark room, two drawn teletype icons lit amber, and one line, the extension cord, running along the floor, out of the door and down a hall to a box labelled 'FAA Flight Service Station'. No person is drawn."
- The name card's words are those of `acts-plan.md` row g-a5s01-radar (A5-S2): `John Curran · observer, Fort Wayne Weather Bureau, 1965`. "Again" means the same card: if `mg_specs/briefs/g-a5s01-radar.md` is on disk and gives the card other numbers, use that brief's box and type so one man has one card, and say so in the receipt.
- The transcript writes the technician as "Arne Cook"; the name on screen is the script's and the source's spelling, `Arnie Koch`.
- No photograph is mounted. Drawings confirmed on disk 12 Oct 26: `media/drawings/wall-clock.svg` (1,205 bytes), `media/drawings/house.svg` (978), `media/drawings/house-lit.svg` (1,001), `media/drawings/teletype.svg` (784), `media/drawings/teletype-lit.svg` (689).

## 2. Datum, scale, orientation
- Part 1 (A5-S18) sits on the centre line y 540: the clock's centre and the house's middle.
- Part 2 (A5-S19) stands on a floor line, y 820. It is one flat side view (a section), left to right: the office room, its door, the hall, the box.
- Clock: `wall-clock.svg` at scale 1.5 (object box 186 x 186, lines 6 px, ticks 4.5, hands 7.5). Hand angles, clockwise degrees from 12, by script: 4:00 is hour 120, minute 0; 10:30 is hour 315, minute 180.
- House: scale 1.4 (object box 364 x 350, lines 5.6 px, aerial rising 47.6 px). Teletypes: scale 1.4 (object box 196 x 196, lines 5.6 px).
- The room, door, hall, box and cord have no file: they are the px lines of section 3, in the hand of design sheet section 7 (4 px, round caps and joins, right angles, Panel dark body fill, no perspective, no shadow).
- The box's right edge is x 1560: nothing of ours is in x >= 1600, y >= 680.

## 3. Geometry (screen px)
Ground: the canvas gradient on the root, on from frame 0.
| Element | Px |
|---|---|
| Name card | glass plate as `compositions/g-i1s2-station.html` `.stn-card` (same fill, blur, border, radius 28): left 96, top 96, 700 x 170. Name `John Curran`: Arial Black 900 52 px, Headline white, left 138, top 118. Sub `observer, Fort Wayne Weather Bureau, 1965`: Georgia italic 30 px, Amber 2, left 140, top 198 (about 570 px wide: read it on a frame, it must end inside the plate). On for the whole comp |
| Source line | design sheet section 10, left 96, bottom 60: `John Curran's recollection, published by the National Weather Service`. On for the whole comp |
| Clock (part 1) | `wall-clock.svg` inline, `<g transform="translate(467 447) scale(1.5)">`: box x 467 to 653, y 447 to 633, centre (560, 540). Rim fill Panel dark, lines Body light. `svgOrigin:"560 540"` on both hands, set once at build |
| Time under the clock | centred on x 560, top 660, Courier New 700 56 px, Amber 2: `4:00 PM`, then `10:30 PM` (two pre-authored lines in the same place, toggled, never retyped) |
| House (part 1) | `house.svg` inline, `<g transform="translate(900 365) scale(1.4)">`: box x 900 to 1264, y 365 to 715, aerial top y 317.4. Dark state first; lit state is the look of `house-lit.svg` (lines Headline white, `dw-win` fill Amber 2 at `fill-opacity` 0.3), reached by tweening the inline group, not by swapping files |
| Floor line (part 2) | y 820, x 96 to 1560, 4 px, Label grey |
| Room | left wall x 140, y 330 to 820; ceiling y 330, x 140 to 760; right wall x 760, y 330 to 640 (the door is the open stretch y 640 to 820). 4 px Label grey. Body: rect x 140 to 760, y 330 to 820, Panel dark, under the lines |
| Teletype 1 | `teletype.svg` inline, `<g transform="translate(220 624) scale(1.4)">`: box x 220 to 416, y 624 to 820 |
| Teletype 2 | same file, `translate(480 624) scale(1.4)`: box x 480 to 676, y 624 to 820 |
| Hall | ceiling line y 640, x 760 to 1240, 4 px Label grey; its floor is the floor line |
| Box | rect x 1240 to 1560, y 600 to 820, 4 px Body light, fill Panel dark. Inside, two lines centred on x 1400, Arial 700 26 px, Body light: `FAA Flight` top 668, `Service Station` top 704 |
| Cord | one path, 4 px, Body light, round joins: from the two machines to the box. Branches (416, 790) to (448, 806) and (480, 790) to (448, 806); then along y 806 from x 448 through the door to x 1240, ending on the box's left wall. It passes in front of teletype 2's foot |
| Cord label | centred on x 1000, top 760, Arial 700 22 px, Label grey: `extension cord` |
| Koch line | centred on x 1000, top 846, Arial 700 22 px, Body light: `strung by Arnie Koch, electronics technician` (ends near x 1240, left of the corner) |
Teletype states, inline from `teletype.svg`: unlit is the group stroke Label grey with the paper (`dw-lamp`) Panel dark; lit is the look of `teletype-lit.svg`: group stroke Body light, paper Amber 2, typed bars (`dw-type`) Caption dark.

## 4. Must be true in the picture
1. The clock reads 4:00 (hour hand on 4, minute hand on 12), then 10:30 (hour hand between 10 and 11, minute hand on 6). The typed time under it agrees at every settled frame. No other time is on screen; "midnight" is not typed.
2. The house window is dark until the word "10" of "ten thirty" and lit after it. Nothing else in part 1 is amber except the typed time.
3. Part 1 carries no storm, no tornado mark, no radar: the line says there was no severe weather in Fort Wayne's area when he left.
4. Part 2: two teletypes, both lit, in a room whose own lines stay Label grey (the room is dark). **One cord, one line,** from the machines out of the door and down the hall to the box. No second cable, no wall socket, no lamp, no generator.
5. The box reads `FAA Flight` / `Service Station` and nothing else. The room carries no name on it.
6. No person is drawn: no Curran, no roommate, no technician, no figure at the window or in the hall. Koch is a typed name only.
7. The name card reads `John Curran` and `observer, Fort Wayne Weather Bureau, 1965`, and the source line says the account is his recollection, for the whole comp.
8. The clock's jump is the hands turning, never a change of size (rule 12).
9. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680.

## 5. Text (exact) and cues
Text: `John Curran` · `observer, Fort Wayne Weather Bureau, 1965` · `4:00 PM` · `10:30 PM` · `FAA Flight` / `Service Station` · `extension cord` · `strung by Arnie Koch, electronics technician` · `John Curran's recollection, published by the National Weather Service`.
Cue words and times are from `audio/a5-s18.words.json` and `audio/a5-s19.words.json` as they stood on 12 Oct 26 at 19:27 (wavs 9.59 s and 9.93 s). "t from comp start" is `mg_specs/timeline-map.md` table 5: the segment's "wav start inside the composition" (A5-S18 0.00, A5-S19 9.64) plus the word's time; a segment's first word takes the "first sound" column (0.00 and 10.12). Gaps are already in the last time column. Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A5-S18 | 0 | Curran | 0.00 | 0.00 | first frame: ground, the name card complete, the source line |
| 1 | A5-S18 | 6 | four | 1.46 | 1.46 | the clock draws on at 4:00 (rim and ticks by `strokeDashoffset`, 0.5 s; hands and hub fade in); `4:00 PM` rises under it (`y:16` set at 0, then `to`, 0.3 s) |
| 2 | A5-S18 | 9 | with | 2.92 | 2.92 | the clock's rim goes Body light to Label grey and back to Body light (0.8 s in all, a stroke change): a quiet afternoon, nothing else arrives |
| 3 | A5-S18 | 19 | slept | 6.56 | 6.56 | the house draws on, dark (`strokeDashoffset`, longest line first, 0.6 s) |
| 4 | A5-S18 | 23 | woke | 7.54 | 7.54 | the hands run to 10:30: hour 120 to 315, minute 0 to 2340 (six and a half turns, ending on 180), 0.8 s, `power2.inOut`; `4:00 PM` is swapped for `10:30 PM` at 8.34, when the hands land |
| 5 | A5-S18 | 26 | 10 | 8.46 | 8.46 | the house lights: lines to Headline white, both windows to Amber 2 at 0.3 (0.3 s) |
| 6 | A5-S19 | 0 | He | 0.00 | 10.12 | part 1 has left (clock, time and house fade out 9.64 to 10.04); the floor line and the room draw on (0.6 s) with the two teletypes in it, unlit |
| 7 | A5-S19 | 6 | teletype | 2.58 | 12.22 | both teletypes light (stroke to Body light, paper to Amber 2, bars to Caption dark, 0.3 s; the second 0.15 s after the first) |
| 8 | A5-S19 | 12 | extension | 4.24 | 13.88 | the cord draws from the machines to the door, x 448 to 760 with its two branches (0.5 s, `strokeDashoffset`); `extension cord` fades in at 14.30 |
| 9 | A5-S19 | 16 | aviation | 5.38 | 15.02 | the hall ceiling and the box draw on (0.5 s) and the cord runs on down the hall to the box, x 760 to 1240 (0.6 s, ending 15.62) |
| 10 | A5-S19 | 17 | office | 5.78 | 15.42 | `FAA Flight` / `Service Station` fades in inside the box (0.3 s) |
| 11 | A5-S19 | 21 | strung | 7.38 | 17.02 | `strung by Arnie Koch, electronics technician` rises under the hall (`y:16` set at 0, then `to`, 0.3 s). Hold to the last frame (20.33) |
The hold from 17.4 to 20.33 is carried by the two paper strips: each teletype's three typed bars (`dw-type`) step their `stroke-opacity` 1 to 0.4 and back in turn, one bar every 0.3 s, finite repeats ending before 20.0: the machines are running.
Steps 2 and 11 and the cord label are not in the Picture notes. Step 2 gives the clause "with no severe weather anywhere" a visible change; the Koch line gives the last clause one. If the lead strikes either, the comp holds on the step before it.

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a5s18-curran.html` is the only file the builder writes; `data-composition-id="g-a5s18-curran"`; id prefix `cur-`; root `<div id="cur-root" ...>` styled through `#cur-root` (plan rule 3 overrides the template's `id="root"`). Full frame, opaque, own ground on from frame 0.
**Base it copies:** the clock family base `mg_specs/briefs/g-a1s05-clocks.md` and its built comp once it has passed (the drawn clock from `wall-clock.svg` inline, hands turned by `rotation` with `svgOrigin`, a drawn house beside it), and `compositions/g-i1s2-station.html` for the name card's glass plate and type (`.stn-card`, `.stn-name`, `.stn-sub`), under this comp's class names. Nothing later copies this comp.
Inline mounts: copy each file's `<g class="dw-...">` into the comp's own `<svg>` inside the static wrapper given in section 3; GSAP touches only the children. The files carry classes only: every id takes the `cur-` prefix. Hands: `svgOrigin` set once at build, before any tween. Zero-length dots (the clock hub) fade in; they take no draw-on.
**Assets mounted (paths from the episode folder, each confirmed on disk 12 Oct 26):**
- `media/drawings/wall-clock.svg` (DR-09, object box 124 x 124, viewBox -6 -6 136 136), inlined at scale 1.5.
- `media/drawings/house.svg` (object box 260 x 250, viewBox -6 -42 272 298), inlined at scale 1.4; its lit look is that of `media/drawings/house-lit.svg`, reached by tween.
- `media/drawings/teletype.svg` (DR-01, object box 140 x 140, viewBox -6 -6 152 152), inlined twice at scale 1.4; its lit look is that of `media/drawings/teletype-lit.svg`, reached by tween.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a5s18-curran`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `python3`, never `python`.

## 7a. Done line
All seven lines of template section 7a. Line 2 (fill): state the measured figure for part 1 at 9.0 and part 2 at 17.5. Line 3: frame 0 shows the name card and the source line, not a bare ground. Line 4: the hands at 7.54 and 8.40 in both seek orders (`svgOrigin` at build, never in a `from`). Line 5: `extension cord` and the Koch line sit clear of the cord, the hall ceiling and the box. Line 6: the two hand angle pairs are computed by a script (hour = hours x 30 + minutes x 0.5, minute = minutes x 6) and stated in the receipt. Line 7 does not apply: the comp is opaque.

## 8. Receipt
As template section 8, plus one line saying whose numbers the name card took (this brief's or `g-a5s01-radar`'s).

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): name card and source line only. Then one settled frame per cue: 2.10 (clock at 4:00, `4:00 PM`), 3.80 (clock back to Body light, nothing new), 7.20 (house drawn, dark), 8.40 (clock at 10:30, `10:30 PM`, house still dark), 8.90 (house lit), 9.90 (part 1 leaving), 10.80 (room and two unlit teletypes), 12.60 (both lit, room lines still grey), 14.60 (cord to the door, `extension cord`), 15.80 (hall, box, box label, cord complete), 17.50 (Koch line), 20.25 (last frame). Each cue second in both seek orders.
