# g-a1-4-ladder: the footnote, the ladder, New York's two numbers (A1-S4, A1-S5, A1-S6)
Builder: Opus 5.5, high effort. Depth: deep. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: g-a1-2-bearmtn's built file (copy its map panel and ladder under the `ld4-` prefix; frame 0 here = g-a1-2's last frame); `library/inhouse/ranked-bars.html`. Ladder geometry: `briefs/a1/_list.md` "The gust ladder" (one scale for both comps: 3.5 px per mph from x 900).
Sits over: nothing. Full-frame designed map + chart on track 2.

## 0. Claim
The 160 mph often quoted as the storm's wind was one mountaintop station (Mount Washington) and belongs in a footnote; where people lived the gusts climbed from Albany 83 (its record) and Allentown 88 to Newark 108 (its record); New York City has two numbers that do not agree: 94 (NWS Jackson, station not named) and Central Park 70 (NWS Mount Holly, the park's record). Closes A1a and A1b.

## 1. Source
`research/nws-facts.md` §1: Mount Washington 160 mph (JKL; NCEI, P); Albany 83 mph gust, strongest ever (ALY, P); Allentown 88 mph (PHI, P); Newark 108 mph, strongest ever there (PHI, JKL, P); NYC 94 mph (JKL, P); Central Park 70 mph, strongest ever there (PHI, P); "Conflicts" item 3 (which station took 94 is not stated). Source lines: S4 "Source: NCEI; NWS Jackson KY"; S5 "Source: NWS Albany; NWS Mount Holly"; S6 "Source: NWS Jackson KY; NWS Mount Holly".

## 2. Datum, scale, orientation
- Map panel: frame A1-N (s 0.058, top-left (81836.7, 19751.4)). Pins: Albany (560,140), Bear Mountain (504,575), Central Park (513,746), Newark (467,761), Allentown (178,804). No pin for "New York City 94": the station is not named. No pin for Mount Washington (off this map; it is a footnote).
- Ladder rows, bar ends and colours: the `_list.md` table. Bar length = mph × 3.5 px.

## 3. Geometry (px, 1920 x 1080)
- Frame 0 = g-a1-2's last frame: map panel, Newark pin, Bear Mountain pin + labels, header, Bear Mountain row full, Newark row dim 35 %.
- Mount Washington row (y 190): bar `#93a3b2` at 45 %, name `MOUNT WASHINGTON, NH · SUMMIT *`, value `160` in `#93a3b2`; divider y 250 and footnote tag `* ONE MOUNTAINTOP STATION`. It sits above the divider, set apart; never wind blue.
- City pins (Albany, Allentown, Central Park): 14 px dot `#7fb2e5`, label Arial 700 22 px `#f2f5f8` tracking 3: "ALBANY" right of the pin; "ALLENTOWN" right of the pin; "CENTRAL PARK" right of its pin at (535, 735) and "NEWARK" stays left of its pin (the two pins are 46 px apart: labels on opposite sides). Each pin lights (pulse) as its bar lands.
- Split NYC slot (S5 end): both NYC and Central Park rows show one ghost bar spanning y 533 to 657 (both rows' height), dashed 2 px `#7fb2e5` outline, no fill, length to x 1180, with "?" Arial Black 900 52 px `#d8a13a` at x 1200, centre y 595, name line `NEW YORK CITY` at y 519.
- Resolved (S6): ghost and "?" go; two real bars: NYC y 550 to x 1229 value `94`; Central Park y 640 to x 1145 value `70`; full name lines per the table. Tag `STATION NOT NAMED` Arial 700 19 px `#e8c56a` tracking 3, right of the NYC name line at the same baseline (x 1300 or after the name, whichever is further right; must end left of x 1824).
- Newark row at S5 "108": bar goes from 35 % to full, name gains `· ITS RECORD` in `#d8a13a`; Albany name carries `· ITS RECORD` from its landing.
- Source line left 110, bottom 90 (swaps per segment, crossfade 0.3 s); "Basemap: Natural Earth" bottom 60.
- Tiers: 52 / 26 / 22 / 19.

## 4. Must be true in the picture
1. Every bar = mph × 3.5 px from x 900, ±4 px: 160 → 560, 140 → 490, 108 → 378, 94 → 329, 88 → 308, 83 → 290.5, 70 → 245. The Mount Washington bar is longest and still reads as set apart (dimmed, above the divider, footnote star).
2. Rows land in spoken order: Mount Washington (S4), Albany, Allentown, Newark highlight, NYC split (S5), NYC 94 and Central Park 70 (S6); never before the word.
3. "NEW YORK CITY 94" has no pin; Central Park has a pin. Nothing places 94 at a station.
4. Each number appears once per frame (the bar value label only).
5. Nothing in x >= 1600, y >= 680: Allentown (y 750) and Albany (y 860) labels end near x 1530 at most.

## 5. Panel text (exact) and cues
Text: `PEAK GUSTS · MPH` · `MOUNT WASHINGTON, NH · SUMMIT *` · `160` · `* ONE MOUNTAINTOP STATION` · `BEAR MOUNTAIN, NY` · `140 MPH` · `NEWARK, NJ` · `· ITS RECORD` · `108 MPH` · `NEW YORK CITY` · `?` · `NEW YORK CITY · NWS JACKSON` · `94` · `STATION NOT NAMED` · `CENTRAL PARK · NWS MOUNT HOLLY · PARK RECORD` · `70` · `ALLENTOWN, PA` · `88` · `ALBANY, NY · ITS RECORD` · `83` · pin labels `NEWARK`, `BEAR MOUNTAIN, NY`, `STATE PARK ON THE HUDSON`, `ALBANY`, `ALLENTOWN`, `CENTRAL PARK` · the three source lines · `Basemap: Natural Earth`
Segment offsets in comp time (0.40 s gaps assumed; replace with the real data-start differences): `SEG = {s4: 0, s5: 13.359, s6: 30.777}`. Cue = SEG + word time.
- S4 0.00: frame 0 as g-a1-2's end; map drift continues (scale 1.03 to 1.06 over the host, ease none). `/* YOULL @s4 0.00 */`
- S4 2.32 "160,": Mount Washington bar `scaleX` 0 to 1 (0.8 s, power4.out) in full `#7fb2e5`, value counts to 160. `/* 160 @s4 2.32 */`
- S4 6.06 "summit": name line in; bar recolours to `#93a3b2` and dims to 45 % (0.6 s); divider draws. `/* SUMMIT @s4 6.06 */`
- S4 8.70 "station": the star and footnote tag in. `/* STATION @s4 8.70 */`
- S4 12.46 "footnote.": the whole Mount Washington row shifts x 0 to -8 and back (settle beat). `/* FOOTNOTE @s4 12.46 */`
- S5 2.82 "ladder,": empty slots show faint tick marks at x 900 for Albany, Allentown, NYC (opacity .3), one after another bottom to top (0.15 s stagger). `/* LADDER @s5 2.82 */`
- S5 4.12 "83,": Albany bar in (scaleX, 0.6 s, power4.out), value counts to 83, Albany pin lights. `/* 83 @s5 4.12 */`
- S5 5.42 "strongest": `· ITS RECORD` on the Albany name line. `/* STRONGEST @s5 5.42 */`
- S5 9.06 "88,": Allentown bar + value + pin (note: Whisper puts "Allentown" at 7.44; the bar lands on the number). `/* 88 @s5 9.06 */`
- S5 11.52 "108,": Newark bar dim to full (0.4 s) with a scaleX 1 to 1.02 to 1 punch; pin pulses. `/* 108 @s5 11.52 */`
- S5 12.90 "record": Newark `· ITS RECORD`. `/* RECORD @s5 12.90 */`
- S5 15.44 "two": ghost split bar draws (dash draw, 0.6 s), "?" pops in (back.out(2)) and pulses every 1.0 s. `/* TWO @s5 15.44 */`
- S6 2.40 "94": ghost and "?" out (0.3 s); NYC bar in, value to 94; NYC name line in. `/* 94 @s6 2.40 */`
- S6 5.86 "70,": Central Park bar in, value to 70, Central Park pin lights. `/* 70 @s6 5.86 */`
- S6 6.84 "strongest": `PARK RECORD` part of the Central Park name brightens from `#93a3b2` to `#d8a13a`. `/* STRONGEST @s6 6.84 */`
- S6 10.48 "station": `STATION NOT NAMED` tag in (`fromTo` y 12 to 0, autoAlpha, 0.4 s). `/* STATION @s6 10.48 */`
- S6 12.50 "both.": NYC and Central Park bars pulse together once. `/* BOTH @s6 12.50 */`
- Exit: last 0.8 s: ladder panel slides x 0 to 980 with autoAlpha 0 (power3.in), map dims to ground; cut to g-a1-5.
Host: data-start = A1-S4 start, duration = SEG.s6 + 13.047 + 0.40 = 44.22 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
