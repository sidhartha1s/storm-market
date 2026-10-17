# BRIEF · g-intro-map-dots · "where everybody was: 135 inside a building, none below ground" · DEEP (Opus 5.5, high) · DOT LAYER BASE

Episode ep-joplin-2011, segments I1-S7 and I1-S8. Full-frame MG. One host from i1-s7 "They" 0.00 to the i1-s8 wav end 6.12 + a 1.5 s hold
(the Picture line's "Hold"; the orchestrator sets the gap before i1-s9). Comp-local i1-s8 times = `nx-i1-s8` data-start − host data-start + word time.
It comes in on a cut from `g-intro-nist`.
Base: MASTER MAP (`g-intro-map` BASEMAP block, verbatim; layers toggled, no geography added). **This comp owns the DOT LAYER**: the 154 dots
sit in `<!--DOTS:g-intro-map-dots--> … <!--/DOTS-->` with ids `g-intro-map-dots-*`, one group per Table 4-3 row. Its end state is the lit
state `g-a6-map135` copies. Same Opus builder as `g-intro-map`. Exemplar for the rail card: `library/inhouse/examples/joplin-stat-panel.html`.
Open: `_list.md` Open 4. A location with no row in `research/map-positions.md` is not drawn: stop and report rather than guess.
Homes, apartments and outside dots are schematic (no source figure for their positions) and the source line says so.

## 0. What this graphic claims
NIST placed 154 of the 155 impact-related deaths (T9, T12): homes, apartments, two big box stores, a pizza restaurant, two churches,
the hospital, two nursing homes, a phone store, a lodge, a theater, and outside (Table 4-3). 135 were inside a structure (T3, T11),
19 outside, 12 of them in vehicles (T17). NIST found no evidence any were underground (H5, H6): the below-ground line stays empty.

## 1. SOURCE (Table 4-3, base 154; sums checked by python 17 Oct 26: 14 rows, total 154, inside 135, outside 19)
| group | count | row |
|---|---|---|
| Homes (detached) | 59 | H26 |
| Apartments | 12 | H26 |
| Walmart · Home Depot | 3 · 8 | B45 |
| Pizza Hut | 5 | B45 |
| Full Gospel Church · Harmony Heights Baptist | 4 · 3 | B45 |
| St. John's (SJRMC) | 12 | C6 |
| Greenbriar · Meadows Healthcare | 19 · 2 | C23, C25 |
| AT&T store · Elks Lodge · Stained Glass Theater | 1 · 4 · 3 | B45 |
| Outside (12 in vehicles) | 19 | T17 |
- T3 "Of the 155 impact-related fatalities, 135 (87 percent) involved persons who are known to have been located inside structures". NIST Finding 40.
- T12 one death (Golden Corral) has no known location, so it is not a dot. H5 / H6 "NIST found no evidence that any fatalities occurred to individuals located below grade". Finding 46, Sec. 4.6.2.2.

## 2. DATUM, SCALE, ORIENTATION
- The base's `s`, centroid and framing (box x 200 to 1500, y 200 to 770), north up; base layers grid, city, streets, path and places on, sirens and ring off.
- Rail card (I1-S8): glass card x 1360 to 1800, y 120 to 520, over the map's east edge (map ground only beneath; read the frame).
- Below-ground line: the base layer, y 880, x 200 to 1500.
- Presenter circle: may stay on; nothing enters x ≥ 1600, y ≥ 680.

## 3. GEOMETRY
- Dots: 7 px circles, Danger red 1 `#c0392b` (the a3 dot style). Named buildings: the group's dots inside that location's base marker,
  in a tight grid, 3 px gaps (the marker grows to fit the group, centred on its position). Homes and apartments: inside the path polygon,
  away from every marker by ≥ 12 px; apartments in the complexes' markers if `map-positions.md` has them, else three schematic clusters of 4.
  Outside: along streets inside the path polygon. Vehicle dots (12 of the 19): the dot plus a 2 px `#dfe7ee` ring at radius 7.
  Every position comes from a seeded script (state the seed); dots ≥ 4 px apart.
- Type labels: Arial 700 26 `#f2f5f8`, tracking 2, beside their group, 16 px clear of every dot and marker, inside the text-safe frame.
  One spoken label at a time (each leaves 0.15 s before the next lands); the four unspoken labels share one window.
- Lit state (I1-S8): inside dots to full opacity with one pulse; outside dots to 50 %, vehicle rings stay visible; markers' strokes to 100 %.
- Placed label: "154 placed · 1 not placed · location unknown", Arial 700 22 `#93a3b2` tracking 3, left x 200, baseline 820.
- Rail card: "135" Courier New 700 110 `#e74c3c` (a count-up leaf); "of 155 impact-related" Arial 700 30 `#dfe7ee`; "Inside a structure"
  Arial 700 26 `#f2f5f8`; "87% · NIST Finding 40" Arial 700 20 `#c8d3e0`. Left-aligned at x 1396; rows 0.3 s apart.
- Zero: "0" Arial Black 900 96 `#f2f5f8`, centred x 850, sitting on the line (glyph bottom y 872); beside it "NIST found no evidence any were
  underground · Finding 46" Arial 700 22 `#c8d3e0`, left x 920, baseline 868. Nothing else touches the line.
- Source line: x 96, baseline 1010, Arial 700 20 `#c8d3e0`.

## 4. MUST BE TRUE IN THE PICTURE
1. Exactly 154 dots; per group the counts in §1 (count them by script from the DOM, state the counts in the receipt). 12 of the 19 outside dots carry the vehicle ring.
2. No dot inside a marker belongs to another group; no outside dot inside any marker; no dot outside the path polygon.
3. The rail reads "135" over "of 155 impact-related", never "of 154".
4. Nothing but "0" and its source text is on the below-ground line; no dot is on or under it.
5. Never two spoken type labels at once; no label under a dot, marker or the path edge.
6. Frame 0 shows the map with no dots (dots begin on "home,").

## 5. PANEL TEXT (exact) and CUES
| element | text | cue |
|---|---|---|
| base map, no dots; map drift scale +1 % over the host (ease none) | | i1-s7 frame 0 |
| source line | "Positions schematic · NIST Table 4-3, 154 placed" (T9) | i1-s7 "They" 0.00 + 0.3 |
| 59 home dots (stagger 0.01 s) + label | "Homes" (H26) | i1-s7 "home," 0.90 |
| 12 apartment dots + label | "Apartments" (H26) | i1-s7 "apartments," 1.68 |
| Walmart 3, Home Depot 8 + label | "Big box stores" (B45) | i1-s7 "big" 2.88 |
| Pizza Hut 5 + label | "Pizza restaurant" (B45) | i1-s7 "pizza" 4.14 |
| Full Gospel 4, Harmony Heights 3 + label | "Churches" (B45) | i1-s7 "churches," 5.14 |
| SJRMC 12 + label | "Hospital" (C6) | i1-s7 "hospital," 6.00 |
| Greenbriar 19, Meadows 2 + label | "Nursing homes" (C23, C25) | i1-s7 "nursing" 7.06 |
| AT&T 1, Elks 4, Stained Glass 3 + three labels together | "Phone store" · "Lodge" · "Theater" (B45) | i1-s7 "few" 8.16 |
| 19 outside dots + vehicle rings + label | "Outside" (T17) | i1-s7 "spots." 8.48 |
| all type labels out (0.3 s); lit state; rail card in `fromTo(x:660 → 0, 0.7, power3.out)` | | i1-s8 "135" 0.00 |
| rail count-up 0 → 135 (power4.out, 0.7 s), rows follow | "135" · "of 155 impact-related" · "Inside a structure" · "87% · NIST Finding 40" (T3) | i1-s8 "135" 0.00 |
| placed label | "154 placed · 1 not placed · location unknown" (T9, T12) | i1-s8 "building," 2.12 |
| below-ground line draws left to right (0.8 s), label | "Below ground" | i1-s8 "investigators" 3.00 |
| "0" drops onto the line (y −40 → 0, 0.35 s, back.out) + its text | "0" · "NIST found no evidence any were underground · Finding 46" (H5, H6) | i1-s8 "below" 5.20 |
| hold | | to the host end: inside dots blip in small groups (≤ 1.5 s apart), rail floats y ±3 px; cut on the host end |

## 6 to 8
`references/mg-brief-template.md` §6, §7, §7a (item 6: per-group dot counts, the seed and marker sizes computed by script), §8.
