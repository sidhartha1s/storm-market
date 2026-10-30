# g-a3-8-upslope: moist air up the West Virginia slopes (A3-S7, 9.60 to 15.20)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md`, `learnings/mg.md`, `briefs/a3/_list.md` (frame A2-W), then this brief.
Start from: `references/editing-patterns/ep5-terrain-map.html` (relief shading, image-mask pattern) on the basemap of `library/inhouse/master-map-us-canada.html`. Prefix every id and class `a3u-`.
Sits over: nothing. Full-frame designed map, fades in over g-a3-7's last 0.6 s (host starts at A3-S7 + 9.00, see Host).

## 0. Claim
The stalled storm's winds kept pushing moist air up the mountain slopes, and in West Virginia the snow kept falling (to 29 Nov).

## 1. Source
- `research/maps-forecast.md` §3 M7 RLX (fetch summary): "upslope flow kept snow falling to 29 Nov" (SECONDARY; NWS Charleston, https://www.weather.gov/rlx/snow).
- Relief: the basemap's terrain layer (if the exemplar has none, a hillshade drawn as 5 to 7 soft ridge bands running SW to NE through eastern WV, labelled nowhere; SCHEMATIC).

## 2. Datum, scale, orientation
Frame A2-W (`briefs/a2/_list.md`): s 0.075, top-left (54186.2, 35931.1); Parkersburg (549, 386), Clarksburg (900, 380), Elkins (1043, 528), Charleston (529, 770). North up. The Allegheny ridge line runs roughly through Elkins, SW to NE: from about (820, 900) to (1300, 250) on screen.

## 3. Geometry (px)
- Relief: ridge bands `#15202b` to `#2a3644` with highlight edges `#4a5560`, on the north-west-facing slope side lit faintly `#5a768f` .25. West Virginia state outline 2 px `#93a3b2` .6.
- Upslope arrows (4) `#7fb2e5` 8 px with heads, conveyor dashes running continuously: start west/north-west of the ridge (x 560 to 760, y 300 to 700) and run east/south-east UP to the ridge line, each bending upward (shorter dashes and a slight brightening as they climb). None crosses the ridge.
- Snow: 80 flakes (2 to 5 px, opacity .35 to .8) falling 60 to 110 px/s over the ridge zone (x 760 to 1400, y 0 to 1080, clipped to stay out of x >= 1600 y >= 680), seeded positions, finite repeats.
- Label: "WEST VIRGINIA" Arial 700 26 px `#dfe7ee` tracking 4, stroke `#04070c` 5 px, at about (640, 560) (inside the state, clear of arrows).
- Day counter (title zone, glass card left 110, top 90, padding 18 x 28): eyebrow "SNOW STILL FALLING" Arial 700 22 px `#93a3b2` tracking 6, then "NOV 29" Arial Black 900 58 px `#f2f5f8`. The counter rolls NOV 27 → NOV 28 → NOV 29 (text-state swap, pre-authored leaves toggled by autoAlpha, 0.35 s each).
- Source line "Source: NWS Charleston, WV · relief schematic" left 110, bottom 90; basemap credit bottom 60.
- Tiers: 58 / 26 / 22 / 19.

## 4. Must be true in the picture
1. Arrows run up the north-west-facing slopes toward the ridge, never downhill, never across the ridge.
2. Snow falls over the mountains (the ridge zone), and keeps falling to the end.
3. "NOV 29" is the final counter value and lands on "falling." (14.52); no other number.
4. Nothing in x >= 1600, y >= 680.

## 5. Panel text (exact) and cues (`audio/a3-s7.words.json`; segment time, then comp time = segment time - 9.00)
Text: `WEST VIRGINIA` · `SNOW STILL FALLING` · `NOV 27` · `NOV 28` · `NOV 29` · `Source: NWS Charleston, WV · relief schematic` · `Basemap: Natural Earth`
- seg 9.00 / comp 0.00: relief fades in from 0 over 0.6 s (over g-a3-7's fade out). `/* FADE @9.00 */`
- seg 9.84 "winds" / comp 0.84: upslope arrows draw on (stagger .2, 0.8 s each), conveyors start. `/* WINDS @9.84 */`
- seg 11.48 "up" / comp 2.48: arrows brighten as they climb (one pulse). `/* UP @11.48 */`
- seg 13.18 "West" / comp 4.18: "WEST VIRGINIA" label in; snow starts. `/* WEST VIRGINIA @13.18 */`
- seg 14.02 "snow" / comp 5.02: counter card in showing "NOV 27" (y 24 to 0, 0.4 s). `/* SNOW @14.02 */`
- seg 14.26 "kept" / comp 5.26: counter to "NOV 28". `/* KEPT @14.26 */`
- seg 14.52 "falling." / comp 5.52: counter to "NOV 29". `/* FALLING @14.52 */`
- Exit: comp 5.60 to 6.20 (seg 14.60 to 15.20): counter card `to` x -60, autoAlpha 0 (0.6 s, power3.in); map fades to 0 as g-a3-9 fades in.
Host: data-start = A3-S7 start + 9.00, duration = 6.20 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
