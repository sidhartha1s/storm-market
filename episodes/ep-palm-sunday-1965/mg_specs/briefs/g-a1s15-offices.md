Host: id=g-a1s15-offices file=compositions/g-a1s15-offices.html start=242.52 (timeline-map.md, 12 Oct 26; the mount in index.html wins) duration=34.71 s track=2

# g-a1s15-offices · A1-S15, A1-S16, A1-S17 · the forecast reaches offices that sit on it, then the stations (wave 1, film family base)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 3, 7, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, and section 7 (the two film rows of this comp). Times: `mg_specs/timeline-map.md` tables 1, 3 and 5. Drawings: `media/drawings/README.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). While a training film shot is on screen its label `Civil defense training film, 1967` is the only chip in the frame (rule 4). The siren horn is never shown sounding and this comp carries no audio (rule 6). A flash is a stroke or fill change, never a scale pop (rule 12). The film cut is mounted in `index.html` by the orchestrator under this comp; the comp draws the ground with the 4:3 window, the frame and the label (rule 15). The operations room keeps its desk placards under the one label (rule 16). The announcer is the first angle only, never slowed or looped (rule 17).
**Spoken (A1-S15):** "The Weather Bureau, the State Police and most sheriffs passed the forecast along as routine. Many of the other offices that heard it did nothing more, and the researchers' word for that is inaction."
**Spoken (A1-S16):** "That left the radio and TV stations, on Palm Sunday weekend. Most were short of staff, so the forecast often went out late. A few stations never passed it on at all."
**Spoken (A1-S17):** "Many stations did get it on the air in time to act. But a forecast covered half a state for hours, and a warning named counties and told people to be on the alert."
**One look:** a film window that stands for a kind of room, one word lifted out of it; a second window that empties to a microphone with its lamp off; then the lamp comes on, a house gets the word, and two strips of paper show how little a forecast said beside a warning.

## 0. What this graphic claims
Most offices that heard the forecast did nothing more with it: the researchers' word is "inaction". A few radio and TV stations never passed the forecast on; many did, in time to act. A forecast spoke of half a state, a warning of named counties.

## 1. Source
- `edit_script.md` A1-S15, Rows [C20; study printed pp. 8-9: "rather routinely disseminated"; "it was that of inaction insofar as further dissemination and transmission of the tornado forecasts was concerned"]. On screen: the one word `inaction`.
- `edit_script.md` A1-S16, Rows [C13; study printed p. 10]. On screen, as the Picture note has it, parentheses included (they are the study's own): `(A few stations never passed on the forecast)`.
- `edit_script.md` A1-S17, Rows [C13; study printed p. 10] · [A5; A6: the two texts, study printed p. 7 and survey printed p. 39]. On screen: `A TORNADO OR TWO` (the forecast's words) and `should be on the alert` (the warning's words).
- Page numbers are the script's (its line 36: the acts' page numbers are the fact checkers' readings of the page images, not the numbers in `research/facts.md`, which differ by one).
- Film: the 1967 civil defense training film (inventory A14), shots 14-05 and 14-09. The room stands for a kind of room, not an Indiana office; the man stands for an announcer, not a named station. Provenance rows: `provenance.csv` lines 64 and 65.
- No page crop is mounted: the three quotes are retyped on quote strips (design sheet section 9, "Quote strip").

## 2. Datum, scale, orientation
Frame 1920 x 1080. Three views, hard cuts between them, one layout grid:
| Band | Px | Holds |
|---|---|---|
| Film window (the hole) | x 480 to 1440, y 150 to 870 (960 x 720, 1.5 times the 640 x 480 cut) | views ROOM and ANNOUNCER |
| Film label | left 480, top 886, height 46 (y 886 to 932) | views ROOM and ANNOUNCER |
| Drawing band | y 134 to 560 | view DRAWN |
| Strip band | y 640 to 810, x 96 to 1576 | every view's paper |
| Chip row under the strips | y 826 to 872 | view DRAWN, second sentence |
| Presenter corner | x >= 1600 and y >= 680 | nothing of ours, ever |
The film is not this comp's: `index.html` mounts it on track 1 (class `filmwin`, left 480, top 150, 960 x 720, muted) and this comp sits above it with a transparent hole. The mount box is fixed, so the whole 4:3 frame shows; rule 16's "frame toward the wall board" has no room in this layout and the placards stay in frame under the label.
| Film mount (`timeline-map.md` table 3) | File | Starts in comp (s) | Mounted (s) | Ends in comp (s) | Window open in this comp (s) | Used of the file |
|---|---|---|---|---|---|---|
| `v-a1s15-room` | `media/films/cuts/a14-05-operations-room.mp4` (31.53 s) | 0.00 | 12.99 | 12.99 | 0.00 to 12.99 (dimmed from 6.63) | 12.99 of 31.53 s |
| `v-a1s16-announcer` | `media/films/cuts/a14-09-announcer.mp4` (9.44 s) | 12.99 | 9.44 | 22.43 | 12.99 to 21.45 | 8.46 of 9.44 s |
**The other two announcer angles are not needed.** The window closes on "A" (21.45 s), 0.98 s before the first angle runs out, so `a14-09b-announcer-shoulder.mp4` (7.17 s) and `a14-09c-announcer-microphone.mp4` (7.84 s) stay unmounted. If a later voice moves that cue past 22.43 s, stop and tell the orchestrator: the fix is those two files mounted in sequence in `index.html` (rule 17), never a held, slowed or looped frame, and never a later close.
Drawings are mounted inline at 1.5 times their object box; the file's 4-unit line is 6 px on screen on both drawings (inside the README's half-to-twice range, so no `stroke-width` override).

## 3. Geometry (screen px)
Views ROOM (0.00 to 12.99) and ANNOUNCER (12.99 to 21.45):
| Element | Px |
|---|---|
| Ground with window | the canvas gradient (design sheet section 2: radial, BG gradient center to BG gradient edge, never flat) as four opaque panels around a transparent hole at x 480 to 1440, y 150 to 870. Each panel carries the full 1920 x 1080 gradient offset by its own left and top, so the gradient shows no seam at a panel edge. Nothing of this comp covers the hole while the window is open, except the dim and the strip of step 1 to 3 |
| Frame | 4 px Body light rectangle on the hole's edge (outer edge x 476 to 1444, y 146 to 874), on from frame 0 |
| Film label | glass chip, left 480, top 886, height 46, padding 0 x 22, Arial 700 26 px, Body light: `Civil defense training film, 1967`. On from frame 0, off with the window at 21.45 |
| Window dim | `rgba(3,5,8,0.60)` over the hole only (x 480 to 1440, y 150 to 870), under the frame line; fades in over 0.4 s |
| Strip A (`inaction`) | quote strip as the built `compositions/g-i1s3-cloud.html` `.cloud-strip` (Beige polaroid `#f4f0e6`, `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`, radius 2): left 96, top 640, 1480 x 170. Quote `“inaction”`, Georgia 52 px, Caption dark, with its quotation marks. Attribution under it: Arial 700 22 px, Caption dark sub, tracking 2: `Disaster Research Center, 1966, pp. 8-9`. It lies over the lower part of the dimmed window and over the frame line at x 480 and x 1440: a deliberate touch, declared `data-overlap-ok` after the frame read |
View DRAWN (21.45 to 34.71):
| Element | Px |
|---|---|
| Hole cover | a fifth opaque panel, the same gradient at the same offset, over x 480 to 1440, y 150 to 870: on in one frame at 21.45 and never off again. Frame and film label go off in that frame |
| Microphone | `media/drawings/microphone.svg` inline (dark state: stroke `#55606b`, fills `#15202b`), ids prefixed `off-`, at 1.5 times: SVG box 198 x 363 at left 411, top 206; object box x 420 to 600, y 215 to 560; line 6 px. Its own small lamp (`dw-lamp`, the circle at object (104, 20)) is screen (576, 245), radius 13.5 |
| ON AIR lamp | the lamp of the built `compositions/g-i1s5-onair.html` (`.air-lamp`: 130 x 36, radius 6, 2 px outline, Arial Black 900 18 px, letter-spacing 1 px) at 1.5 times: 195 x 54, radius 9, 3 px outline, Arial Black 900 27 px, letter-spacing 1.5 px, text `ON AIR`. Left 413, top 135 (x 413 to 608, y 135 to 189), centred over the microphone. **Off** = no fill, outline and letters `#55606b` (this differs from the hook's resting red outline, which meant "expected to"; here off means a station that did not put it on the air). **On** = fill Popfig red `#d0121f`, letters Headline white `#f2f5f8`, and the microphone's own small lamp fills Popfig red in the same frame |
| Microphone group | microphone and ON AIR lamp in one group. From 21.45 to 24.28 the group sits 450 px to the right (`x: 450` set in the timeline at 0): microphone object box x 870 to 1050, lamp x 863 to 1058, centred on x 960 where the announcer was. At step 7 it slides to rest (`x: 0`) |
| Strip B (the stations) | left 96, top 640, 1480 x 170, as strip A. Quote on one line, Georgia 52 px, Caption dark: `“(A few stations never passed on the forecast)”`. Attribution: `Disaster Research Center, 1966, p. 10` (the Picture note gives `p. 10`; the document's name is added because strip A left the screen 8.5 s earlier) |
| House | `media/drawings/house.svg` inline (dark state), ids prefixed `off-`, at 1.5 times: SVG box 408 x 447 at left 1121, top 122; object box x 1130 to 1520, y 185 to 560; aerial top y 134; line 6 px. The house stays dark: it is never swapped for `house-lit.svg` |
| Lit window | the left `dw-win` rect only (object x 44 to 92, y 120 to 168; screen x 1196 to 1268, y 365 to 437): fill Amber 2 `#e8c56a` at `fill-opacity` 0.3 (the README's lit value). The right window stays `#15202b` |
| Dotted link | overlay SVG, Label grey dots 6 px, gap 16 px, round caps, straight from (630, 400) to (1100, 400), 470 px; drawn from the microphone end by a clip that grows along the line |
| Strip C (forecast) | left 96, top 640, 730 x 170 (x 96 to 826). Quote `“A TORNADO OR TWO”`, Georgia, Caption dark. Attribution: `Disaster Research Center, 1966, p. 7` |
| Strip D (warning) | left 846, top 640, 730 x 170 (x 846 to 1576, clear of the corner). Quote `“should be on the alert”`. Attribution: `Weather Bureau survey report, 1965, p. 39` |
| Quote size, C and D | one size for both: Georgia 52 px if each quote measures 650 px or less, else 40 px for both (the design sheet's two quote sizes; no third) |
| Chip under C | glass chip, left 96, top 826, height 46, padding 0 x 22, Arial 700 26 px, Body light: `half a state` |
| Chip under D | same chip, left 846, top 826: `three counties` |
No source line in the credit corner: every paper strip carries its own attribution (design sheet section 10).

## 4. Must be true in the picture
1. Whenever any film pixel shows (0.00 to 21.45), `Civil defense training film, 1967` is on screen and is the only glass chip. No place, office, station, person, time or county is named over the film. The only other text over film is strip A, which is paper and is the Picture note's own.
2. The film is never frozen, slowed, looped or reversed. The room is the first 12.99 s of its file; the announcer is the first 8.46 s of the first angle. From 21.45 to the last frame the hole is opaque (read at 22.50, after the announcer mount has ended at 22.43: no black, no stale frame).
3. The room's placards are neither cropped nor masked; they stand under the label (rule 16). Its first 2 s are placard-free.
4. `inaction` is the only quoted word of A1-S15 and is not on screen before 11.53. Strip A and the dim are gone in the frame the announcer appears (12.99).
5. The microphone has no name and no call letters. The ON AIR lamp is off (grey outline, no fill) from 21.45 to 25.89 and red from 25.89 to the end. It changes by fill only: no pulse, no scale, no glow lines.
6. Strip B's words are the study's, parentheses included, and nothing is added to them.
7. The link runs from the microphone to the house, drawn in that direction. Exactly one window is amber, the left one; the house's lines stay dark.
8. Paper holds only the documents' words; `half a state` and `three counties` are ours and sit on glass. The forecast strip is on the left and lands first; the warning strip is on the right.
9. No county name, no `County A`, no `County B`, no town, no time of day anywhere in this comp.
10. No siren horn, no sound lines, no audio element.
11. Nothing appears before its spoken word; nothing of ours in x >= 1600, y >= 680; all text at least 96 px from the sides and 54 px from top and bottom.
12. The ground shows no seam: the four panels and the hole cover read as one gradient.
Beat check (rule 13): `inaction` is settled 11.83 to 12.99 (1.16 s, one word, the paper already up for 1.5 s). Strip B is settled 21.95 to 24.28 (2.33 s, eight words). Strip D's quote is settled 31.25 to 34.71 (3.46 s).

## 5. Text (exact) and cues
Text: `Civil defense training film, 1967` · `“inaction”` · `Disaster Research Center, 1966, pp. 8-9` · `ON AIR` · `“(A few stations never passed on the forecast)”` · `Disaster Research Center, 1966, p. 10` · `“A TORNADO OR TWO”` · `Disaster Research Center, 1966, p. 7` · `half a state` · `“should be on the alert”` · `Weather Bureau survey report, 1965, p. 39` · `three counties`.
Cue words and times are from `audio/a1-s15.words.json`, `audio/a1-s16.words.json` and `audio/a1-s17.words.json` as they stood on 12 Oct 26 (wavs 12.32, 11.17 and 10.10 s). Wav starts inside the comp, from `mg_specs/timeline-map.md` table 5: A1-S15 0.15, A1-S16 12.65, A1-S17 23.91. A first word reads 0.00 in `words.json`, so it is timed from the table's "first sound" column (0.47, 12.99, 24.28). Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A1-S15 | 0 | The | first sound 0.32 | 0.00 (the cut; voice at 0.47) | first frame: ground, open window on the operations room, frame, film label. Nothing else until step 1 |
| 1 | A1-S15 | 15 | Many | 6.48 | 6.63 | the window dim fades in (0.4 s) |
| 2 | A1-S15 | 28 | researcher's | 9.84 | 9.99 | strip A enters with its attribution and no quote yet (`y: 60` to 0 with the fade, 0.4 s, power3.out) |
| 3 | A1-S15 | 33 | in | 11.38 | 11.53 | `“inaction”` lands on strip A (fade with `y: 16` to 0, 0.3 s). The transcriber splits the word into "in" (33) and "action." (34) |
| 4 | A1-S16 | 0 | That | first sound 0.34 | 12.99 | hard cut: dim and strip A off in one frame; the announcer is in the window; frame and film label stay |
| 5 | A1-S16 | 23 | A | 8.80 | 21.45 | hard cut: hole cover on, frame and film label off. The microphone draws on at centre (0.5 s, longest line first); the ON AIR lamp's outline and letters follow in the off state (0.4 s from 21.65) |
| 6 | A1-S16 | 24 | few | 8.90 | 21.55 | strip B enters (`y: 60` to 0 with the fade, 0.4 s, power3.out) |
| 7 | A1-S17 | 0 | Many | first sound 0.37 | 24.28 | strip B exits right (`x: 1900`, 0.5 s, power3.in); the microphone group slides left to rest (`x: 0`, 0.6 s, power2.inOut) |
| 8 | A1-S17 | 7 | air | 1.98 | 25.89 | the ON AIR lamp turns on: fill and letters change in 0.15 s, the microphone's small lamp with them |
| 9 | A1-S17 | 8 | in | 2.20 | 26.11 | the dotted link grows from the microphone to the house (0.6 s, ease none); the house draws on over the same 0.6 s |
| 10 | A1-S17 | 11 | act, | 2.92 | 26.83 | the left window turns amber (fill change, 0.3 s) |
| 11 | A1-S17 | 14 | forecast | 4.14 | 28.05 | strip C enters with quote and attribution (`y: 60` to 0 with the fade, 0.4 s) |
| 12 | A1-S17 | 16 | half | 4.98 | 28.89 | chip `half a state` fades in (0.3 s) |
| 13 | A1-S17 | 23 | warning | 6.94 | 30.85 | strip D enters with quote and attribution (0.4 s) |
| 14 | A1-S17 | 25 | Counties | 7.58 | 31.49 | chip `three counties` fades in (0.3 s). Hold to the last frame (34.71); the next comp cuts in |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a1s15-offices.html` is the only file the builder writes; `data-composition-id="g-a1s15-offices"`; id prefix `off-`; root `<div id="off-root" ...>` styled through `#off-root` (plan rule 3 overrides the template's `id="root"`). The comp is opaque over the whole frame except the film window from 0.00 to 21.45. It mounts no video and no audio: the two film mounts are the orchestrator's, already typed in `index.html`.
**Style reference it matches:** the approved hook and intro set. Page and strip look from `compositions/g-i1s6-page.html` and `compositions/g-i1s3-cloud.html` (strip); lamp from `compositions/g-i1s5-onair.html`; microphone, house and the draw-on from `compositions/g-t1s3-list.html`.
**Family base role (plan section 5, builder 1-c):** this is the film base. Its film view (ground with hole, frame, label chip, the hard cut that covers the hole) is copied by `g-a2s03-chain` (wave 2, already briefed against these numbers), `g-a3s07-calls` (wave 3), `g-a5s10-alert` (wave 4) and `g-a6s11-sirens` (wave 5); its microphone and lamp by `g-a6s03-announcer` (wave 5). Keep the film view's CSS in one block under plain class names so a copy is a paste. Send this comp alone for a full-size read before any copy.
**Assets (paths from the episode folder; sizes read from the files on 12 Oct 26):**
- `media/films/cuts/a14-05-operations-room.mp4` (FC-01, 640 x 480, 29.97 fps, 31.53 s, a silent audio stream): under the comp, not mounted by it.
- `media/films/cuts/a14-09-announcer.mp4` (FC-02, 640 x 480, 29.97 fps, 9.44 s, a silent audio stream): under the comp, not mounted by it.
- `media/films/cuts/a14-09b-announcer-shoulder.mp4` (7.17 s) and `media/films/cuts/a14-09c-announcer-microphone.mp4` (7.84 s): on disk, not used.
- `media/drawings/microphone.svg` (object box 120 x 230, viewBox -6 -6 132 242, line 4), inlined.
- `media/drawings/house.svg` (object box 260 x 250, aerial to y -34, viewBox -6 -42 272 298, line 4), inlined. `media/drawings/house-lit.svg` is not used.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a1s15-offices`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. The contact sheet shows the hole as empty when the comp is read alone: that is expected for 0.00 to 21.45 and a defect after 21.45.

## 7a. Done line
All seven lines of template section 7a. Line 3 here: frame 0 is the open window with frame and label, the ground on around it. Line 4: seek to 12.99, 21.45 and 24.60 (mid slide) forward and backward and match the frames. Line 7: frames at 3.00, 8.00 and 17.00 composited over the real film (the label is the only chip; at 8.00 the dim is on); a frame at 22.50 over the mount to prove the hole is covered.

## 8. Receipt
As template section 8, plus: the measured width of the two half-strip quotes and the size chosen.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): window open on the room, frame, one label, no seam in the ground. Then, composited over the film where the window is open: 3.00 (room, placards, one label), 7.40 (dim settled), 10.80 (strip A with attribution, no word), 12.40 (`inaction` settled), 13.04 (announcer, dim and strip gone), 17.00 (announcer, one label), 21.40 (last open frame: the first angle still moving), 22.50 (microphone at centre, lamp off, strip B; hole opaque after the mount's end), 23.80 (strip B settled), 25.20 (microphone at left, strip B gone), 26.00 (lamp red), 26.75 (link complete, house drawn), 27.30 (left window amber and readable as lit beside the dark one), 28.60 (strip C), 29.60 (chip `half a state`), 31.30 (strip D), 32.20 (both strips, both chips, corner empty), 34.60 (last frame).
