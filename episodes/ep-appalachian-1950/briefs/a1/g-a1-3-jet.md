# g-a1-3-jet: fast air a mile up, mixing down; New England trees and power (A1-S3)
Builder: Opus 5.5, high effort. Depth: deep. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `references/editing-patterns/ep2-met-explainer.html` (side-view cutaway layers), `library/inhouse/master-map-us-canada.html` (second scene). Prefix every id and class `jt3-`.
Sits over: nothing. Full-frame designed explainer on track 2, then a full-frame map.

## 0. Claim
A stream of unusually fast air ran about a mile overhead; warm air near the ground let some of it mix down (general mechanism, no place tied to it). Across New England the wind brought down trees and knocked out power.

## 1. Source
- `factcheck/a1-r1.md` row 13 (NBC Connecticut, SECONDARY): "+4 standard deviation 850mb winds"; 850 mb is about 1.5 km, roughly a mile. Row 14: warm sector "turbulent mixing to mix down destructive winds"; NOT tied to Newark or Bear Mountain. Row 58: the band mixes down at several points, none named.
- `research/nws-facts.md` §1 NCEI (P): "intense winds ... caused extensive tree damage, power outages, and coastal flooding in New England" (`factcheck/a1-r4.md` row 1).

## 2. Datum, scale, orientation
- Cutaway (0 to 8.7 s): side view, west left, east right (no compass shown). Ground datum y 860. "About a mile up" = band centre y 380 (480 px = 1 mile, schematic). Horizontal is not to scale. Tag "SCHEMATIC, NOT TO SCALE" Arial 700 19 px `#93a3b2` at right 120, top 70.
- Map (8.7 s on): frame A1-E, s 0.028, frame top-left (68508.0, -2167.7), north up. Marker sites (screen px): Hartford (760,820), Springfield (769,768), Worcester (854,743), Providence (896,812), New Haven (733,891), Boston (934,727), Concord NH (882,594), Burlington (702,396), Portland ME (1020,524). Markers are illustrative of "extensive" damage, not a count.

## 3. Geometry (px, 1920 x 1080)
- Sky: vertical gradient `#0b1016` top to `#15202b` at the ground.
- Ground: band y 860 to 1080 `#04070a`; ridge silhouette (2 to 3 low hills, crest y 760 to 820) `#2a3644`; 14 unlabeled rooftop blocks along y 830 to 860 `#4a5560`. No names, no numbers on the ground.
- Wind band: y 350 to 410, full width, `linear-gradient(90deg, rgba(127,178,229,.0), rgba(127,178,229,.85) 15%, rgba(127,178,229,.85) 85%, rgba(127,178,229,0))`; 24 streak lines (2 px, 80 to 200 px long, `#f2f5f8` at .6) inside it moving x +420 px/s, finite repeats over the window (seeded positions, no Math.random at seek time).
- Height bracket: x 200, a 2 px `#93a3b2` line from y 860 to y 380 with end ticks; no number on it (the chip carries it).
- Warm layer: y 700 to 860 full width, `linear-gradient(0deg, rgba(216,161,58,.35), rgba(216,161,58,0))`, slow shimmer (y 0 to -6 px yoyo, finite repeats).
- Mixing wisps: 4 curved paths from the band down to the rooftops at x 520, 880, 1240, 1560 (the x 1560 wisp ends at y 640, above the circle corner). Each: 3 px `#7fb2e5`, dash draw (`strokeDashoffset` from ceil(len)+1 to 0), curling end; two small arrowheads riding the dash.
- Chip (title zone): glass card left 110, top 70: "FAST WIND" Arial Black 900 58 px `#f2f5f8`, "ABOUT 1 MILE UP" Arial 700 30 px `#dfe7ee` tracking 2 under it. Card bottom about y 220; band starts y 350 (no overlap).
- Map scene: land `#0b1016`, outlines 1.5 px `rgba(255,255,255,.14)`, region label "NEW ENGLAND" Arial 700 26 px `#93a3b2` tracking 8 at (1180, 300). Tree markers: 28 px fallen-tree glyph (SVG, `#dfe7ee`); outage markers: 28 px lightning-bolt-in-circle glyph `#e8c56a`. 9 tree + 9 outage markers at the sites above, each offset 20 px so no two overlap; legend glass card left 110, top 70: "TREES DOWN" (tree glyph) and "POWER OUT" (bolt glyph), Arial 700 26 px `#f2f5f8`.
- Source lines: cutaway "Source: NBC Connecticut report (a Connecticut weather writer's reading)"; map "Source: NCEI" (+ "Basemap: Natural Earth" at bottom 60, source at bottom 90). Left 110.
- Tiers: 58 / 30 / 26 / 19.

## 4. Must be true in the picture
1. The band sits at about a mile up on the bracket (band centre y 380 ±10, ground y 860) and runs across the whole width: it is a stream, not a point.
2. Wisps come down at four separate x positions; none ends on a labelled place, none carries a number.
3. The warm layer is near the ground only (below y 700).
4. No place name, city or number in the cutaway. Nothing says Newark or Bear Mountain anywhere in this comp.
5. Map markers carry no numbers; no marker in x >= 1600, y >= 680 (all sites are x <= 1020).
6. Nothing in x >= 1600, y >= 680 in either scene.

## 5. Panel text (exact) and cues (`audio/a1-s3.words.json`, seconds from A1-S3 start)
Text: `FAST WIND` · `ABOUT 1 MILE UP` · `SCHEMATIC, NOT TO SCALE` · `NEW ENGLAND` · `TREES DOWN` · `POWER OUT` · `Source: NBC Connecticut report (a Connecticut weather writer's reading)` · `Source: NCEI` · `Basemap: Natural Earth`
- 0.00: sky, ground, ridge, rooftops on; tag on. `/* THAT @0.00 */`
- 1.14 "stream": band wipes in left to right (clip or scaleX 0 to 1 from left, 1.0 s, power3.out); streaks start. `/* STREAM @1.14 */`
- 1.88 "fast": a second, faster streak set (560 px/s) fades in over the first (0.5 s), so the band visibly speeds up. `/* FAST @1.88 */`
- 3.46 "mile": height bracket draws up from the ground (0.6 s); chip in (`fromTo` x -60 to 0, autoAlpha, 0.6 s, power3.out). `/* MILE @3.46 */`
- 5.66 "warm": warm layer fades up (0.8 s). `/* WARM @5.66 */`
- 7.76 "mix": four wisps draw down, staggered 0.2 s, 0.8 s each. `/* MIX @7.76 */`
- 8.72 "Across": chip exits (x -60, autoAlpha 0, 0.5 s, power3.in); camera pulls up and through: cutaway layer y 0 to 400 with autoAlpha 0 over 0.8 s while the map fades in under it at scale 1.08 to 1 (0.9 s, power2.out). `/* ACROSS @8.72 */`
- 9.34 "England,": region label and legend card in. `/* ENGLAND @9.34 */`
- 10.88 "trees": 9 tree markers pop in (`fromTo` scale 0 to 1, back.out(2), stagger 0.08). `/* TREES @10.88 */`
- 11.52 "knocked": 9 outage markers pop in, then blink (autoAlpha 1 to .4 to 1, every 0.8 s, finite repeats). `/* KNOCKED @11.52 */`
- Exit: none; the scene ends on a cut to g-a1-4. Markers keep blinking to the last frame.
Host: data-start = A1-S3 start, duration = 12.438 + 0.40 = 12.84 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
