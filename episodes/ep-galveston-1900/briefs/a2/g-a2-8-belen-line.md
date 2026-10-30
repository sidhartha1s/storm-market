# g-a2-8-belen-line · A2-S7 (whole) · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules" (the shared map, wires, chips, paper card). Base: `compositions/g-a2-5-two-offices.html` (plate, pins, wire layer, the lit Washington-to-Galveston wire). Mini-cards: copy the Viñes and Gangoiti cards from `compositions/g-a2-4-vines-gangoiti.html` (same text, scaled). Camera state V-HAV is g-intro-4's.

## 0. Claim
Gangoiti, at Belen, observed a new storm on Monday 3 September and read it by Viñes's model. The Americans could hear him (letters both ways since late 1898); Galveston could not: his forecast never left Havana, while Galveston stayed lit by Washington's line alone.

## 1. Source
- Instruments, records, thirty years: mirrors A1-S8; 1870 to 1900 computed (factcheck/a2-r1.md row 16). Not on screen.
- New storm Mon 3 Sep: sources-cuba.md §1 (Roker "On Monday, September 3, Father Lorenzo Gangoite ... observed a new storm", SECONDARY); row 41; a2-r2 row 14 (no position: "east of Cuba" was the writer's, so no storm is drawn anywhere on this map).
- Viñes's model: a2-r2 row 15 (Roker, sky and Viñes's model; "the sea" not supported).
- Letters: rows 23, 25 (Gangoiti to Moore 30 Nov 1898; Moore to Gangoiti 12 Dec 1898; Blythe to Gangoiti 1 Aug 1900, "the Bureau"; contents unseen); a2-r2 rows 16, 17.
- Galveston's warnings came only from Washington: sources-cuba.md §3 (MWR); row 42.

## 2. Datum, scale, orientation
- Plate and formula as g-a2-5. Points: Havana/Belen (1585.8, 1857.6), Galveston (468.0, 1216.2), Washington (2066.4, 218.3).
- Camera states (computed 28 Oct 26):
  - V-HAV: cx 1100, cy 1560, s 1.0. Havana (1446, 838); Galveston (328, 196); Washington off screen (1926, -802).
  - V-WIRE: cx 1267, cy 1000, s 0.5. Galveston (561, 648); Havana (1119, 969); Washington (1360, 149).
  - V-HAV to V-WIRE is a 2x pull-out: `logZoom`.

## 3. Geometry
- Standing state from frame 0: Washington to Galveston wire lit (Shared rules lit wire), Galveston pin lit `#f2f5f8`. In V-HAV the wire enters from the top edge and runs to Galveston at (328, 196).
- Belen pin at Havana `#d8a13a` (no blue ring here: this is Belen alone).
- V-HAV HUD labels: "Belen, Havana" Arial 700 30 px `#e8c56a`, right edge 1430, baseline 800 (above the pin, right of the cards); "Galveston" Arial Black 900 40 px `#f2f5f8`, right edge 305, baseline 208.
- Mini-cards (V-HAV only, HUD, beside the Belen pin): Viñes card at scale 0.45, box x 700 to 1195, y 590 to 739; Gangoiti card at scale 0.6 (from 840 x 300), box x 700 to 1204, y 760 to 940. Viñes card at opacity 0.75 (the past), Gangoiti at 1.
- Chip "MON SEPT 3 · BELEN: A NEW STORM" (Shared rules chip, no tag): centred x 960, top 120.
- V-WIRE HUD labels: "Belen, Havana" 26 px `#e8c56a`, right edge 1095, baseline 978; "Washington" 30 px `#7fb2e5`, left x 1385, baseline 158; "Galveston" Arial Black 900 40 px, right edge 535, baseline 660; "Letters" Arial 700 22 px `#e8c56a` tracking 3, left x 1262, baseline 566 (right of the letters line's midpoint).
- Letters line (plate units): Havana to Washington, `#d8a13a` 3 px, dotted (2 px dots, 10 px gaps), opacity 0.8. A return dot (10 px `#7fb2e5`) travels Washington to Havana along it on the "still writing to him" cue.
- Belen line (plate units): from Havana toward Galveston, `#d8a13a` 3 px, solid, ending at 60 % of the way: plate (915.9, 1473.6) = screen (784, 776) in V-WIRE, with an open end (a 10 px gap then a 6 px dot, no arrowhead).
- Source line (top-left): "Al Roker, HistoryNet (secondary) · NOAA AOML, 2015".

## 4. Must be true in the picture
1. Pins on their formula points within 10 px in both states.
2. The Belen line never reaches Galveston: it stops at 60 % of the distance (at least 200 screen px short of the Galveston pin in V-WIRE) and then retracts toward Havana.
3. The only line touching Galveston is Washington's, lit from frame 0 to the end.
4. No storm symbol, track or position anywhere (the storm's 3 Sept position is unsourced).
5. Cards never overlap the pin, its label, the chip or each other; they are gone before the camera moves.
6. Nothing enters x >= 1600, y >= 680 (V-HAV Havana is at x 1446; its ring pulse stays inside x < 1600).
7. No label rides the pull-out.

## 5. Text and cues (a2-s7.words.json; Whisper writes Gangoiti "Ganguetti", Viñes "Venez's")
- 0.00 ("Ganguetti" 0.00) /* GANGOITI @0.00 */: plate in V-HAV with the standing state; Belen pin pulsing and its label on; Gangoiti mini-card slides in from x -60 (0.5 s, power3.out). Source line in. Camera drifts s 1.00 to 1.03, 0 to 9.0.
- 3.82 ("Monday," 3.82) /* SEPT 3 @3.82 */: chip enters, landing as "3rd" is said (4.26).
- 6.04 ("new" 6.04): Belen pin flashes (scale 1 to 1.7 to 1, 0.5 s) on "new storm".
- 8.00 ("Venez's" 8.00, i.e. Viñes's) /* VINES MODEL @8.00 */: Viñes mini-card slides in above Gangoiti's.
- 8.60 to 9.20: chip exits; cards and V-HAV labels fade out, done 9.28.
- 9.32 ("He'd" 9.32) to 10.40: camera pulls V-HAV to V-WIRE, logZoom.
- 10.06 ("Willis" 10.06) /* MOORE @10.06 */: Washington pin pulses brighter (it was on the plate; its label in at 10.40 after the settle, with the other V-WIRE labels).
- 10.58 ("since" 10.58): letters line draws Havana to Washington 10.58 to 11.20; "Letters" label in at 11.20 ("1898," 11.20).
- 12.80 ("Bureau" 12.80): return dot travels Washington to Havana 12.80 to 14.32 ("August." 14.32).
- 16.06 ("hear" 16.06): letters line brightens (opacity 0.8 to 1 and back, 0.6 s).
- 17.40 ("Galveston" 17.40) /* GALVESTON @17.40 */: Belen line draws from Havana 17.40 to 18.10 and stops at its 60 % point; open end appears.
- 17.78 ("couldn't." 17.78): a pulse runs Washington to Galveston 17.78 to 18.50 (Galveston is lit by Washington only); Galveston pin flashes.
- 18.74 ("His" 18.74) /* NEVER LEFT @18.74 */: Belen line retracts to Havana 18.74 to 19.96 ("Havana." 19.96), power2.in; Belen pin pulses once at 19.96.
- Host: A2-S7 0.00 to 20.517.

## Motion for the whole window
Pin pulses throughout; drift 0 to 9.0; pull-out; letters draw, return dot, Belen line draw and retract. Longest gap between beats 14.32 to 16.06, covered by pulses.

## Exit
Cut to the A2-S8 weather map: the whole root fades to 0 over the last 0.35 s (20.167 to 20.517).

## Footage under it
None: full-frame designed map (coverage 100 %).
