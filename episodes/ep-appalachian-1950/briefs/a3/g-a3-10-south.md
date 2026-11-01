# g-a3-10-south: the cold did not stop in Ohio (A3-S8)
Builder: Opus 5.5, high effort. Depth: deep (camera move + flow + fill, opens loop A3 for Act 4). Read `references/mg-quickref.md`, `learnings/mg.md`, `briefs/a3/_list.md` (frames A2-X and T), then this brief.
Start from: `library/inhouse/master-map-us-canada.html` (camera rig, `logZoom` from `library/inhouse/snippets/helpers.js`); cold arrow style from g-a3-2. Prefix every id and class `a3c-`.
Sits over: nothing. Full-frame designed map; frame 0 = g-a3-9's last frame (frame A2-X, pins, track, no chip). Ends into the chapter blackout.

## 0. Claim
The cold air from the low's west side ran far past the Ohio River, across Kentucky, toward Georgia, Alabama and the Florida Panhandle, much farther south than the snow reached.

## 1. Source
- `research/nws-facts.md` §6 NCEI: cold reached FL, AL, GA, NC; Pensacola FL reached (the number is Act 4's, not shown).
- Snow's southern edge: §2 JKL snow in eastern Kentucky (Paintsville, Hazard), used for where the white fill stops (no town named on screen).
- The arrows' paths and the snow fill outline are SCHEMATIC; only "cold reached the Gulf states" and "snow stopped in eastern Kentucky" are claims.

## 2. Datum, scale, orientation
Camera from A2-X (s 0.03, top-left (42191.8, 15852.5)) to T (s 0.0125, top-left (-4474.8, 16919.2)): a 2.4x pull-out plus a pan south, so `logZoom` (not linear scale), 2.0 s, power2.inOut. The Picture line's "tilts south" is read as this pull-out-and-pan (no 3D tilt: text and pins stay legible); reported to the orchestrator. Frame T places (px): Pittsburgh (900, 220), Lake Erie centre (842, 97), Ohio (765, 237), Ohio River at Louisville (623, 373), Hazard KY (746, 443), Atlanta area (689, 687), Pensacola FL (553, 919), Carolinas (967, 565). North up.

## 3. Geometry (px, frame T)
- Before the move, the pin labels fade to 0 (no text rides the camera move); pins shrink with the map; after the move only the pins (no labels) stay, at .5 opacity. The track stays at .4.
- Snow fill: a soft white area `#f2f5f8` at .35, blurred edge 20 px, covering PA, OH, WV and eastern KY: its southern edge runs from about (620, 400) through Hazard (746, 443) to (900, 470), i.e. just south of the Ohio River in the east and stopping in eastern Kentucky. It fades in after the move.
- Cold arrows (5) `#7fb2e5` 9 px with heads, conveyor dashes running, drawn on in a southward wave (stagger .25): starting along the Ohio/Lake Erie latitudes (y 120 to 260) and running south across the Ohio River and Kentucky toward Georgia/Alabama (y 650 to 760) and one to the Florida Panhandle (head at about (560, 880)). Heads end well south of the snow fill's edge: the gap is the picture.
- Snow edge marker: a 3 px `#f2f5f8` .8 dashed line along the fill's southern edge.
- Chip (glass chip, radius 14, padding 10 x 18): "THE SNOW STOPPED HERE" Arial Black 900 40 px `#f2f5f8`, box left 1000, top 420 (east of the edge line's end, a 2 px leader to (900, 470)); right edge <= 1600 (it sits above y 680 anyway).
- No temperatures, no town names, no state names on screen (Act 4 owns them). Credit "Basemap: Natural Earth" left 110, bottom 60; source "Source: NCEI; NWS Jackson, KY · arrows schematic" left 110, bottom 90.
- Scan line 60 px/s throughout.
- Tiers: 40 / 19 (3 text nodes, under the flat-type count of 4, so no exemption needed).

## 4. Must be true in the picture
1. The arrow heads reach far south of the snow edge: the nearest head is at least 200 px south of the edge line; one head reaches the Florida Panhandle (y >= 860).
2. The snow fill stops in eastern Kentucky; it never reaches Tennessee, Georgia or the Gulf.
3. No number, temperature or place name on screen.
4. The camera move is logZoom; no label visible while it moves.
5. Nothing in x >= 1600, y >= 680 (arrows sit at x <= 1100).

## 5. Panel text (exact) and cues (`audio/a3-s8.words.json`, seconds from A3-S8 start)
Text: `THE SNOW STOPPED HERE` · `Source: NCEI; NWS Jackson, KY · arrows schematic` · `Basemap: Natural Earth`
- 0.00 "But": frame 0 = g-a3-9 last frame; pin labels fade (0.3 s). `/* BUT @0.00 */`
- 0.26 "cold": camera logZoom A2-X to T starts (2.0 s, arrives 2.26); first two cold arrows start drawing south as the camera moves (they are shapes, not text). `/* COLD @0.26 */`
- 1.16 "Ohio,": the arrows cross the Ohio River line. `/* OHIO @1.16 */`
- 2.58 "south": remaining three arrows draw on southward (stagger .25, 1.0 s each), heads reaching Georgia/Alabama and the Panhandle by 3.84. Sound riser starts. `/* SOUTH @2.58 */`
- 3.14 "get?": snow fill fades in (0.6 s) and the edge line draws (0.6 s). `/* GET @3.14 */`
- 4.32 "farther": chip "THE SNOW STOPPED HERE" in with its leader (x 30 to 0, autoAlpha, 0.45 s, power3.out). `/* FARTHER @4.32 */`
- 5.68 "reached.": the riser ends here; arrow conveyors keep moving. `/* REACHED @5.68 */`
- Exit: last 0.6 s (from 5.80): the whole map fades through to `#04070c` (0.6 s, power2.in) into the chapter blackout; no single element vanishes alone.
Host: data-start = A3-S8 start, duration = 6.00 + 0.40 = 6.40 s.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8.
