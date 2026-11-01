# g-a3-9-swell · A3-S8 · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplar: `episodes/ep6-katrina-2005/compositions/g-surge-ms.html` (water against land), `compositions/g-intro-7-clines.html` (Cline lower-third style).

## 0. Claim
On the afternoon of the 7th a heavy swell came in from the southeast and kept coming all night; the tide rose unusually high even though the wind was from the north, off the land. Joseph Cline was on duty until nearly midnight.

## 1. Source
MWR Sept 1900 p. 372, Cline's report (factcheck/a3-r1.md rows 29 to 31): "A heavy swell from the southeast made its appearance in the Gulf of Mexico during the afternoon of the 7th. The swell continued during the night without diminishing, and the tide rose to an unusual height when it is considered that the wind was from the north and northwest"; Joseph "having been on duty until nearly midnight" (sources-cline.md §2). No tide height for the 7th is on record: NO number on the tide.

## 2. Datum, scale, orientation
- Plan view, north up, SCHEMATIC (on-screen note "Schematic" Arial 700 19 px `#93a3b2` left 96, top 1000). Galveston's Gulf beach runs SW to NE: shoreline a straight line from (200, 860) to (1500, 300) (bearing about 67° from north, as the island lies). Land (the island) above-left of the line, fill `#15202b`; Gulf below-right, fill `#04070c`.
- Swell crests run perpendicular to their travel. The swell travels FROM the SE toward the NW (heading 315°), so crests run SW-NE (bearing 45°); they arrive at the beach slightly oblique. Five crests `#5a768f` 4 px, 900 px long, spaced 110 px, moving toward the NW at 40 px/s.
- Wind arrow: from the north, pointing south (toward the sea), placed over the land at (520, 240) to (520, 460), `#7fb2e5` 8 px, arrowhead; label "WIND: NORTH" Arial 700 26 px `#7fb2e5` tracking 3 right of the arrow.
- Tide line: a band 14 px `#d8a13a` opacity 0.6 along the shoreline on the land side, creeping inland 0 to 60 px over the host (no scale, no number).

## 3. Geometry
- Chip C1 "SWELL FROM THE SOUTHEAST" left edge x 1000, top 150.
- Part B (from 16.08): lower-third (shared spec) name "JOSEPH CLINE", role "Observer · on duty until nearly midnight" (`#f5d98b`). The role line is long: Arial 700 27 px, card width up to 900 px, one line.
- Source line top-left: "Isaac Cline, Monthly Weather Review, Sept. 1900, p. 372".

## 4. Must be true in the picture
1. Wind arrow points from land to sea (north to south) while the crests move from sea to land: the two visibly oppose.
2. Swell comes from the SE (crests travel toward the NW).
3. Tide band moves inland only, no number, no ft, no water over the island.
4. Whisper writes "Klein" in Part B's cue: on screen it is CLINE.
5. Nothing in x >= 1600, y >= 680 except the Gulf fill (an unlabelled area) and crest lines; report to the orchestrator for the circle.

## 5. Text and cues (a3-s8.words.json, segment 18.54 s)
- 0.00 ("Then"): plan view drawn, crests at rest; source line.
- 1.94 ("swell") /* SWELL @1.94 */: crests start moving; C1 in at 3.24 ("southeast").
- 4.16 ("It kept coming"): C1 out by 4.76; crests keep coming.
- 6.76 ("tide") /* TIDE @6.76 */: tide band starts creeping inland (6.76 to 15.10, ease none).
- 9.24 ("wind") /* WIND NORTH @9.24 */: wind arrow draws, label in at 10.36 ("north").
- 12.14 ("You'd") to 15.10 ("sand"): all three movers continue; arrow pulses once at 12.56 ("wind").
- 16.08 ("Joseph") /* JOSEPH @16.08 */: dissolve 0.5 s to Part B footage; lower-third in at 16.24.
- Host 0.00 to 18.54 plus land time (cap 19.5).

## Motion for the whole window
Crests move from 1.94 to 16.08; tide creeps from 6.76; lower-third drifts in Part B.

## Exit
Lower-third out `x:-980` in the last 0.6 s.

## Footage under it
Part A: none (full-frame designed). Part B: "Weather Bureau office window at night": NO footage sourced. Orchestrator picks a stand-in (a period photo of the Galveston office if found, else hold the plan view dimmed to 0.4 under the lower-third).
