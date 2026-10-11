# 03 · T1-S3, T1-S4, T1-S5 · the telephone list, the blank row, the family (comp `g-t1s3-list`)

Brief on `references/mg-brief-template.md`. Shared look: `00-design-sheet.md` sections 4, 5, 6, 7, 10. **One comp across three segments:** the sheet, the camera and the photograph must be continuous from the first tick to the last word of the hook, and three builds would break the match at each seam. This is the base of the list family (08, 12 copy it): send it alone for a full-size read before those are built.

**Spoken:**
- T1-S3: "State Police. Sheriffs. City police. Named radio and television stations."
- T1-S4: "A family got it from an announcer, if the announcer had it."
- T1-S5: "Whose job was it to tell the family at the end of the list?"
**One look:** a typed telephone list. Four names get a tick. The last row has no name. Past the edge of the paper: a microphone, then a house, both dark.

## 0. What this graphic claims
South Bend's Weather Bureau telephoned its warnings to offices and stations (eight entries in the study; four are read aloud). No household is on the list. A family heard only through a broadcaster, and only if the broadcaster had the warning.

## 1. Source
- `edit_script.md` T1-S3 Rows [A6; study printed p. 14] (four of the eight entries); T1-S4 Rows [C12] [C8] ("the C8 station has no name and no county in the study"); T1-S5 has no row.
- Row text and order: design sheet section 5 table, copied from the T1-S3 Picture note.
- Ground: teletype room photograph, **waits for inventory row A3**.
- The house and microphone are drawings because the inventory holds no 1965 studio or home.

## 2. Datum, scale, orientation
One world, design sheet sections 5 and 6. The blank row's centre line (world y 598) is the datum: the dotted line, the microphone and the house sit on it. Camera states Close, Everything, Push are the design sheet's numbers and are computed in the comp from that table, never placed by eye (template done line 6). SCHEMATIC, NOT TO SCALE: the chain is a diagram of who told whom, not a map.

## 3. Geometry (screen px, per state)
| State | Sheet | Rows | Chain |
|---|---|---|---|
| Close (T1-S3) | x 250 to 1466, y 30 to 974 | centres 276.4, 353.2, 430.0, 506.8, 583.6, 660.4, 737.2, 814.0; text 41.6 px from x 387.6; row 9 zone (centre 890.8) is plain paper: no tick box, no rule, no cursor yet | off frame to the right |
| Everything (T1-S4, T1-S5 start) | x 64 to 824, y 170 to 760 | row n centre = 324 + 48 x (n - 1); row 9 centre 708 | dotted line y 708, x 824 to 1030 and 1150 to 1300; microphone x 1030 to 1150, y 510 to 740; house x 1300 to 1560, y 490 to 740; labels at y 774 |
| Push (T1-S5 end) | scale 1.2 about the blank row, which lands at (560, 560) | text 31.2 px | house right edge at x 1899, y 298 to 598; label "a family" centred (1743, 639) |
Ground: A3 `<img>`, `object-position:50% 40%`, scale 1.06 to 1.14 across the window; scrim tweens `.dim` (0.45) to `.dim-heavy` (0.68) over the sheet's 0.7 s entrance.
HUD (fixed, outside the world): source line left 96, bottom 60: `Disaster Research Center, 1966 · list of offices the Weather Bureau telephoned`.
Row 6's longest neighbour is row 4 (37 characters): at 41.6 px it ends at x 1311, inside the sheet.

## 4. Must be true in the picture
1. Eight typed rows in the study's order and spelling (design sheet section 5 table). All eight are on the sheet before the first tick.
2. Exactly four ticks at the end of T1-S3: rows 1, 2, 3, 6. Rows 4, 5, 7, 8 are grey, unticked and still readable on a frame at television distance.
3. The count of ticks on screen never exceeds the count of names spoken so far.
4. Row 9 has a tick box, a rule and a blinking cursor, and no text and no tick, to the end of the comp.
5. The sheet never says how many offices, "all", "complete" or "warning system" (S2).
6. The microphone is off the paper: at least 200 px of ground between sheet and microphone in the Everything state, no tick box beside it, no call letters, no station name (S4).
7. The microphone and the house are dark from their first frame to the last: no amber on either. The lamp on the microphone flickers on "if" and ends off.
8. The dotted line runs from the blank row, not from row 6. It never becomes solid and nothing travels along it to the house.
9. The house has no person at a window (S5).
10. Reveal order follows the voice: house on "family", microphone on "announcer".
11. In the last frame the blank row, the microphone and the house are all inside the frame.
12. Design sheet S1, S6, S7.

## 5. Text (exact) and cues
Sheet text: `WEATHER BUREAU · SOUTH BEND, INDIANA` · `Warnings telephoned to:` · the eight rows. Chain labels: `an announcer` · `a family`. Source line as section 3.
| Step | Seg | cue | t= | What |
|---|---|---|---|---|
| 0 | T1-S2 | cue: "list" (comp starts on this word; match cut from 02) | | ground at scale 1.06, `.dim`; sheet rises in Close state (`y:1100 to 0`, 0.7, power3.out); scrim to 0.68 |
| 1 | seam | 0.15 s after the sheet lands | | eight rows type in, one row every 0.09 s, each a 0.08 s `autoAlpha` step (pre-authored text, never typed into the DOM); source line in |
| 2 | T1-S3 | cue: "State" | | tick row 1, text to Caption dark; one soft key strike (sound, orchestrator) |
| 3 | T1-S3 | cue: "Sheriffs" | | tick row 2 |
| 4 | T1-S3 | cue: "City" | | tick row 3 |
| 5 | T1-S3 | cue: "Named" | | tick row 6; rows 4, 5, 7, 8 stay grey |
| 6 | T1-S4 | cue: "A" (first word) | | row 9's tick box and rule draw on (0.3 s), cursor starts to blink; camera Close to Everything with `logZoom`, 0.9 s, power2.inOut; dotted line draws left to right as the frame widens |
| 7 | T1-S4 | cue: "family" | | house draws on (0.6 s), label `a family` after the last line |
| 8 | T1-S4 | cue: "announcer" (first) | | microphone draws on (0.5 s), label `an announcer` |
| 9 | T1-S4 | cue: "if" | | lamp on the microphone: Amber 2 for 0.12 s, off 0.1 s, on 0.12 s, then off for good |
| 10 | T1-S5 | cue: "Whose" | | camera Everything to Push, linear, lasting to the last word (a 1.2x move, no `logZoom` needed) |
| 11 | T1-S5 | cue: "family" | | house outline pulses once to Body light at 100 % and back to dark (0.5 s); no amber |
| 12 | T1-S5 | cue: "list" (last word) | | the cursor's blink is in its on phase at this word; hold 1.0 s (land time) |
| 13 | exit | | | hard cut into comp 04, whose first frame is this house in sun. No fade, no black (script: "no void") |
Motion through every hold: the cursor blink (1 s cycle), the photograph push, and from step 10 the camera.

## 6 to 8. Contract, tools, done line, receipt
As `references/mg-brief-template.md` sections 6, 7, 7a, 8, unchanged. File `compositions/g-t1s3-list.html`, id prefix `list-`, root id `list-root`. The host window runs from cue "list" in T1-S2 to 1.0 s after T1-S5's last word; the timeline is at least that long.
Receipt must state: the three camera states as computed, the measured contrast read of a grey row on a frame, and the frame at step 12.
**Closest library exemplar:** `library/official/` block `mk-specs-list` (rows that slide in staggered with a check; copy the row and check mechanics, replace the look with the paper sheet) and `typewriter` (deterministic cursor blink). In-house: El Reno `compositions/g-a4s7-table.html` (a rail of rows lit on spoken words, then a camera step) and `library/inhouse/moves/moves.js` camera rig for the three states.
