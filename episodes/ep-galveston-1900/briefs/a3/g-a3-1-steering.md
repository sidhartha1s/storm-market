# g-a3-1-steering · A3-S1 · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules" (this folder), which points at `briefs/intro/_list.md` "Shared rules". Exemplars: `compositions/g-intro-4-wire-map.html` (projection, pin style, HUD layer), `library/inhouse/master-map-us-canada.html` (camera rig). This comp is the BASE of the A3 map family: g-a3-2-roads and g-a3-3-lows-north reuse its wide plate, ridge and pins. Send it alone for a full-size frame read before they copy it.

## 0. Claim
A hurricane drifts around the edge of a dome of high pressure over the Atlantic; once far enough north, a dip in the westerly winds usually catches it and swings it northeast. The National Hurricane Center calls that recurving. If it came, the storm would swing away from Texas.

## 1. Source
- Mechanism: factcheck/a3-r1.md rows 1 to 3 (NHC al032014 discussion #4; hurricanescience.org, SECONDARY).
- Bureau expected recurve: sources-cuba.md §3 (NOAA AOML).
- "Away from Texas": factcheck-C.md I1-S5 track (a recurve off Cuba keeps the storm off Texas).
- The path drawn here is a TEXTBOOK recurve, not the 1900 storm's track. No date, no 1900 position on this comp.

## 2. Datum, scale, orientation (the wide plate, P-WIDE)
- Same projection as g-intro-4: `X = (lon + 100) * 90`, `Y = (41 - lat) * 103.95`, extended to lon -100 to -40, lat 10 to 50: plate X 0 to 5400, Y -935.6 to 3222.5 (SVG viewBox `0 -936 5400 4159`). North up. Natural Earth 1:50m land (the file g-intro-4 converted; extend its clip box, same colours: land `#15202b`, coast `#5a768f` 2 px, water `#04070c`).
- Pins (formula, checked 28 Oct 26): Galveston (468.0, 1216.2); Havana (1585.8, 1857.6).
- Camera (screen = 960 + (X - cx) * s, 540 + (Y - cy) * s): V-WIDE cx 2700, cy 1100, s 0.36 (the whole Gulf and the western Atlantic to lon -40). One slow push to s 0.38 over the host, ease none.
- The ridge and the westerly dip are SCHEMATIC (no pressure values). On-screen note: "Schematic" Arial 700 19 px `#93a3b2` at left 96, top 1000.

## 3. Geometry (plate px unless stated)
- Ridge (the dome of high pressure): a soft ellipse centred (lon -55, lat 30) = (4050, 1143.5), radii 1300 x 800, fill radial `#d8a13a` at opacity 0.22 centre to 0 at the edge; label "HIGH" Arial Black 900 64 px `#e8c56a` on the HUD at the centre's screen point.
- Storm dot: white ring 40 screen px, 5 px stroke `#f2f5f8`, glow. Path (dashed 18/12, `#f2f5f8` 4 screen px, drawn behind the dot): (lon -60, lat 19) to (-70, 18) to (-80, 23) to (-82, 28) to (-78, 33) to (-68, 38) to (-55, 43). Plate points: (3600, 2286.9), (2700, 2390.9), (1800, 1871.1), (1620, 1351.4), (1980, 831.6), (2880, 311.9), (4050, -207.9). Curve through them (Catmull-Rom to cubic, `ease:none` per leg, legs timed below).
- Westerly dip: a wavy band from the west at lat 45 dipping to lat 33 near lon -80, stroke `#7fb2e5` 10 px opacity 0.7, arrowheads pointing east; it swings down at its cue. Label on the HUD "WESTERLY WINDS" Arial 700 22 px `#7fb2e5` tracking 3 above the band's west end.
- Galveston pin `#f2f5f8` 14 px, label "Galveston" Arial Black 900 32 px left of the pin.
- Chip "RECURVE" (shared chip spec) top 150, centred x 960; tag "National Hurricane Center term" Arial 700 22 px `#93a3b2`.
- Source line top-left: "National Hurricane Center · hurricanescience.org".

## 4. Must be true in the picture
1. No date, no "1900", no track label: this is the textbook path. Galveston pin and Havana pin by formula within 10 px.
2. The dot moves only along the ridge's southern and western edge before the dip arrives, then curves NE with the dip; it never touches the Gulf west of lon -88 (X 1080).
3. Galveston's pin stays white-unlit (no pulse) through the curve-away; it never turns red or gets a hit.
4. No text rides the camera push (all labels on the HUD, placed when the push is under 1 % from its start).
5. Nothing in x >= 1600, y >= 680 (the ridge's faint fill may pass under; no label, pin or dot there). At V-WIDE the ridge's screen edge reaches about (1914, 844): its faint fill does sit in the circle corner; report it to the orchestrator.

## 5. Text and cues (a3-s1.words.json, segment 23.38 s)
- 0.00: plate, ridge at opacity 0, source line in. Dot parked at the first path point.
- 2.92 ("hurricane") /* HURRICANE @2.92 */: dot pulses once.
- 6.70 ("dome") /* DOME @6.70 */: ridge fades up 0.8 s; "HIGH" label in at 7.28 ("high").
- 7.52 to 10.44: dot runs the first three legs (to (1620, 1351.4)), riding the ridge edge.
- 11.28 ("dip") /* DIP @11.28 */: westerly band swings down 11.28 to 12.50, power2.inOut; "WESTERLY WINDS" label at 11.76 ("westerly").
- 13.00 ("catches") /* CATCHES @13.00 */: dot runs the last three legs 13.00 to 15.30, the band moving with it.
- 17.96 ("recurving") /* RECURVE @17.96 */: chip in.
- 20.64 ("If"): chip out by 21.24.
- 21.82 ("storm") to 23.04 ("Texas") /* TEXAS @23.04 */: Galveston pin and label in, held white; the dashed path brightens once along its length as the dot sits off to the northeast.
- Host 0.00 to 23.38 plus land time to the cut (cap 24.4).

## Motion for the whole window
Camera push s 0.36 to 0.38 over the host; ridge fill breathes opacity 0.18 to 0.24, sine, finite repeats; the dot always has a 1.4 s ring pulse. No window over 4 s without a mover.

## Exit
Cut into A3-S2's page (g-a3-2-roads opens on the MWR p. 395 scan): fade-through, root to 0 over the last 0.4 s.

## Footage under it
None: full-frame designed map (root background tokens.md radial gradient).
