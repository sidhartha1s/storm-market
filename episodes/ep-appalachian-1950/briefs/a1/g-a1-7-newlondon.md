# g-a1-7-newlondon: New London's tide among the hurricanes; New York's wind bill (A1-S9)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `library/inhouse/ranked-bars.html` (bars, rotated to vertical), `library/inhouse/master-map-us-canada.html` (scene 2 basemap). Prefix every id and class `nl7-`.
Sits over: nothing. Full-frame designed card on track 2, then a full-frame map.

## 0. Claim
At New London the November 1950 tide reached 7.58 ft; in 100 years of records only three storms pushed it higher, and all three were hurricanes (1938, Carol, Sandy). In New York State the wind damage came to about $20 million at the time.

## 1. Source
- `factcheck/a1-r1.md` rows 42, 43 (NBC Connecticut, SECONDARY): "In New London the tide reached an impressive 7.58ft MLLW"; "The only storms higher in the last 100 years are the 1938 hurricane, hurricane Carol, and hurricane Sandy."
- `research/nws-facts.md` §1 ALY (P): NY State wind damage "totaling 20 million dollars at the time".
- Source line "Source: NBC Connecticut; NWS Albany".

## 2. Datum, scale, orientation
- Bars: floor y 900, 70 px per ft. 1950 bar = 7.58 × 70 = 530.6 px (top y 369). The three hurricane tides have NO sourced height and no sourced order (orchestrator open item 3): draw them equal, open-topped, rising past the 1950 bar to y 200 and fading out from y 300 to y 200 (gradient to transparent), so they read "higher" without a value. Order on screen: date order left to right, 1938, CAROL, SANDY, then NOV 1950 set apart on the right.
- Scene 2 map: frame A1-Y, s 0.03, frame top-left (58158.5, 5498.5), north up. Albany (1000,500), Buffalo (410,461), Newark (952,821, unlabelled).

## 3. Geometry (px, 1920 x 1080)
- Ground: radial gradient `#0b1016` to `#030507`.
- Title (title zone, left 110, top 70): "NEW LONDON, CT" Arial Black 900 52 px `#f2f5f8`; sub "TOP FOUR TIDES IN 100 YEARS" Arial 700 26 px `#93a3b2` tracking 8 at top 140.
- Baseline 2 px `rgba(255,255,255,.14)` y 900, x 200 to 1500.
- Bars (width 180, radius 4 top corners only on the 1950 bar): 1938 at x 260 to 440, CAROL x 520 to 700, SANDY x 780 to 960 (all `#5a768f`, open-topped fade as §2); NOV 1950 at x 1140 to 1320, `#7fb2e5`, solid top at y 369. A dashed 1 px `rgba(255,255,255,.3)` reference line at y 369 from x 260 to 1320 shows the hurricane bars pass it.
- Bar labels under the baseline (y 930): "1938 HURRICANE", "CAROL", "SANDY" Arial 700 22 px `#dfe7ee` tracking 3, each with a 26 px hurricane glyph (SVG spiral, `#d8a13a`) above the label at y 912; "NOV 1950" Arial 700 22 px `#f2f5f8` + "WINTER STORM" Arial 700 19 px `#7fb2e5` tracking 3 under it (y 960).
- Value on the 1950 bar top: "7.58 FT" Arial Black 900 52 px `#f2f5f8`, centred on the bar, bottom at y 350.
- Scene 2: NY State outline fill `#15202b`, 2 px `rgba(255,255,255,.3)` border; neighbours outline only. Chip glass card centred on the state at (760, 420): "$20 MILLION" Arial Black 900 58 px `#f2f5f8`; "NY STATE WIND DAMAGE (1950 $)" Arial 700 22 px `#93a3b2` tracking 4 under it. Albany pin dot `#f2f5f8` with label "ALBANY" Arial 700 22 px (the NWS office), right of the pin.
- Source line left 110, bottom 60 (scene 2: bottom 90, "Basemap: Natural Earth" bottom 60).
- Tiers: 58 / 52 / 26 / 22 / 19.

## 4. Must be true in the picture
1. 1950 bar = 530.6 px tall (±4); every hurricane bar crosses the dashed 7.58 line and shows no value.
2. Nothing implies a rank among the three hurricanes (equal height, date order).
3. Only the 1950 bar carries "WINTER STORM"; the three carry the hurricane glyph.
4. "$20 MILLION" is labelled as 1950 dollars and as NY State wind damage only.
5. Nothing in x >= 1600, y >= 680 (bars end x 1320; the map chip ends about x 1100).

## 5. Panel text (exact) and cues (`audio/a1-s9.words.json`, seconds from A1-S9 start)
Text: `NEW LONDON, CT` · `TOP FOUR TIDES IN 100 YEARS` · `1938 HURRICANE` · `CAROL` · `SANDY` · `NOV 1950` · `WINTER STORM` · `7.58 FT` · `$20 MILLION` · `NY STATE WIND DAMAGE (1950 $)` · `ALBANY` · `Source: NBC Connecticut; NWS Albany` · `Basemap: Natural Earth`
- 0.00: ground, baseline on; whole card drifts y 0 to -10 over the host (ease none). `/* ON @0.00 */`
- 1.02 "New London,": title in (`fromTo` x -60 to 0, autoAlpha, 0.6 s, power3.out). `/* NEWLONDON @1.02 */`
- 2.62 "7": 1950 bar `scaleY` 0 to 1 (transformOrigin bottom, 0.8 s, power4.out); "7.58 FT" counts 0.00 to 7.58 on a leaf, landing on 3.72; "NOV 1950" label in. `/* 7 @2.62 */`
- 4.78 "hundred years": sub line in; reference line draws. `/* HUNDRED @4.78 */`
- 6.66 "three": the three bars rise together past the reference line (scaleY 0 to 1, 0.9 s, power3.out). `/* THREE @6.66 */`
- 9.38 "hurricanes.": three glyphs in, spinning (rotation 0 to 360, 2 s, finite repeats through the hold); "WINTER STORM" in under the 1950 bar. `/* HURRICANES @9.38 */`
- 10.86 "1938,": "1938 HURRICANE" label in. 12.36 "Carol": "CAROL". 12.82 "Sandy.": "SANDY". `/* 1938 @10.86 */ /* CAROL @12.36 */ /* SANDY @12.82 */`
- 13.70 "In New York": card slides up and out (y -200, autoAlpha 0, 0.6 s, power3.in) while the map rises in (y 200 to 0, 0.7 s, power3.out); Albany pin. `/* NEWYORK @13.84 */`
- 16.26 "$20": chip in (`fromTo` scale 0.9 to 1, autoAlpha, 0.5 s, back.out(1.6)); "$20 MILLION" counts $0 to $20 on the digits. `/* 20 @16.26 */`
- Hold: state fill breathes (opacity .9 to 1, finite yoyo), map drift.
- Exit: last 0.6 s: chip slides out (x 980, autoAlpha 0, power3.in); map fades. Cut to g-a1-8.
Host: data-start = A1-S9 start, duration = 17.864 + 0.40 = 18.26 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
