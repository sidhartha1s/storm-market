# g-a2-4-flash-freeze · A2-S3 · DEEP · Opus 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `references/editing-patterns/ep2-met-explainer.html` (layered physical explainer: fixed HUD text, animated mechanism). Moves helpers: `library/inhouse/moves/moves.js` (read its README).

## 0. What this graphic claims
1. The roads had been soaked by rain all night at 37 to 39°F.
2. Behind the front the air fell below 32°F at the airport around 8:15 AM, too fast for the water on the pavement to drain or dry, so it froze in place and the snow fell on top of the ice. Forecasters call this a flash freeze.

## 1. SOURCE
- Overnight rain, 37 to 39°F, midnight to 6 AM Fri: `research/nws.md` 2.1; `factcheck/a2-r1.md` row 9 (ASOS 12:01 to 6:18 AM, 37 to 39 F, -RA; CONFIRMED).
- Air below 32°F about 8:15 AM: `factcheck/a2-r1.md` row 10 (ASOS 33.0 F at 8:06, 28.9 F at 8:39; "Air hit 32 F about 8:15 AM"). Linear between the two readings it crosses 32.0 at 8:14.
- Mechanism: NWS Buffalo Winter Summary 2022-23 (PRIMARY, row 10): "The rapidly cooling airmass created a flash freeze on area roads making travel difficult as snow and blowing snow increased." NWS safety page (row 10): black ice "can also form when roadways are slick from rain and temperatures drop below freezing".
- "Flash freeze" is the forecasters' term: WSW 220854 (3:54 AM Thu 22 Dec, PRIMARY), `factcheck/a2-r1.md` rows 11 and 12: "A rapid switch from rain to snow with sharply falling temperatures into the teens and single digits will result in a flash freeze on Friday." The quote is spent in A1-S8, so it is NOT shown here; the source line names the product.
- Source lines: "Buffalo airport ASOS, IEM archive" (temperatures) then "NWS Buffalo Blizzard Warning, 22 Dec 2022" (the term).

## 2. DATUM, SCALE, ORIENTATION
- Full-frame designed graphic, channel ground on the root from frame 0.
- Road cross-section: SCHEMATIC, NOT TO SCALE (the water film is drawn thousands of times thicker than life). That label is on screen.
- Thermometer scale: y(T) = 640 - (T - 20) x 20 px. 40°F at y 240, 32°F at y 400, 30°F at y 440, 20°F at y 640. Mercury top = y(T).

## 3. GEOMETRY (px)
- Air region (rain/snow particles only here): x 420 to 1420, y 200 to 584. Particles never enter the HUD box (x <= 760, y <= 200) or the label column (x < 400).
- Layers, all x 400 to 1440:
  | layer | y | fill |
  |---|---|---|
  | snow (appears at 17.10) | 584 to 612 | `#f2f5f8`, grows `scaleY 0 -> 1` from its bottom edge |
  | water film, then ice | 612 to 640 | water `rgba(127,178,229,.55)` (#7fb2e5); ice `#dfe7ee` with 1 px `#7fb2e5` crack lines |
  | asphalt | 640 to 820 | `#2a3644` with `#4a5560` aggregate dots (static, seeded) |
  | road base | 820 to 900 | `#15202b` |
- Diagram labels, Arial 700 22 px letter-spacing 3, right-aligned at x 380, each beside its layer with a 1 px `#93a3b2` leader to x 400:
  "SNOW" `#f2f5f8` centre y 570 (leader down to y 598) · "RAINWATER" `#7fb2e5` centre y 626, crossfades to "ICE" `#dfe7ee` at the freeze · "ASPHALT" `#93a3b2` centre y 730.
- "SCHEMATIC, NOT TO SCALE": Arial 700 19 px `#93a3b2`, left 400, glyph box y 916 to 938.
- Thermometer: tube x 1540 to 1580 (rounded, 1 px `rgba(255,255,255,.3)` border, fill `#0b1016`), y 230 to 640; bulb centre (1560, 662) radius 26 (bottom y 688, x 1534 to 1586: outside x >= 1600). Mercury 24 px wide, colour `#d8a13a` (Amber 1) at or above 32°F, `#7fb2e5` (Cold blue 2) below; colour change happens as the top crosses y 400.
  - 32°F line: 2 px `#c0392b`, x 1520 to 1600, y 400; label "32°F" Arial 700 22 px `#c0392b`, left 1610, centre y 400.
  - End ticks: "40°F" at y 240 and "20°F" at y 640, Arial 700 19 px `#93a3b2`, left 1610.
  - Eyebrow "AIR, BUFFALO AIRPORT" Arial 700 22 px `#93a3b2` letter-spacing 6, right edge x 1700, glyph box y 150 to 176.
  - Readout slot: Courier New 700 30 px, right edge x 1700, glyph box y 190 to 222; one string at a time: "BELOW 32°F" `#7fb2e5`, "37 TO 39°F" `#e8c56a`.
- HUD title slot (top-left, fixed, never moves with anything): left 110, top 110. One string at a time, Arial Black `font-weight:900` 52 px `#f2f5f8`: "ABOUT 8:15 AM" · "OVERNIGHT" · "BEHIND THE FRONT"; then "FLASH FREEZE" at 84 px (glyph box y 110 to 194).
- Cold front: polygon `rgba(90,118,143,.35)` (Cold blue 1) filling the air region from x 400 to its leading edge, the edge leaning forward (top ahead of bottom by 120 px); edge travels x 400 -> 1440.
- Source line Arial 400 19 px `#c8d3e0`, `left:96px; bottom:54px`; one string at a time.
- Type tiers 84/52 big, 30 mid, 19 to 22 small. Corner x >= 1600, y >= 680 empty.

## 4. MUST BE TRUE IN THE PICTURE
1. Order of states follows the voice: crossing at about 8:15, flashback to the overnight rain, the front, the freeze, the snow on top, the term.
2. Mercury below the red line exactly when the readout says "BELOW 32°F"; at or above it when the readout says "37 TO 39°F" (mercury between y 260 and y 300).
3. The water layer is liquid (blue, shimmering) until "freezes" @15.34, then ice; it never drains away or thins before freezing ("no time to drain or dry").
4. Snow lies ON the ice (snow above, ice below), never under or mixed into it.
5. "SCHEMATIC, NOT TO SCALE" is on screen whenever the layers are.
6. No label sits under rain, snow or the front polygon; no particle crosses a label or the HUD.
7. No temperature number other than 32, 37 TO 39, and the 20/40 end ticks.

## 5. PANEL TEXT (exact) and CUES (seconds from A2-S3 start, `audio/a2-s3.words.json`)
Strings: `ABOUT 8:15 AM` `OVERNIGHT` `BEHIND THE FRONT` `FLASH FREEZE` · `AIR, BUFFALO AIRPORT` `BELOW 32°F` `37 TO 39°F` `32°F` `40°F` `20°F` · `SNOW` `RAINWATER` `ICE` `ASPHALT` `SCHEMATIC, NOT TO SCALE` · `Buffalo airport ASOS, IEM archive` `NWS Buffalo Blizzard Warning, 22 Dec 2022`
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | frame 0 | ground, layers (water film, asphalt, base), thermometer with mercury at 33°F (y 380), light rain falling, "SCHEMATIC" label, ASOS source line. HUD and readout empty |
| 0.44 | "quarter" @0.44 | HUD "ABOUT 8:15 AM" `fromTo(autoAlpha 0, x:-24 -> 0, 0.4, power3.out)` |
| 2.58 | "dropped" @2.58 | mercury 33 -> 31 (y 380 -> 420), 0.7 s, power2.in; colour flips to cold blue at y 400 |
| 3.32 | "freezing." @3.32 | readout "BELOW 32°F" in; red line pulses `scaleY 1 -> 2 -> 1, 0.4` |
| 4.32 | "The rain" @4.32 | flashback: HUD swaps to "OVERNIGHT" (crossfade 0.3); readout out; mercury rises to 38 (y 280), 0.6 s, power2.out (colour back to amber at y 400); rain density up (more streaks) |
| 5.42 | "roads" @5.42 | water film shimmer starts (a highlight band sweeping left to right every 1.4 s, finite) |
| 6.78 | "37" @6.78 | readout "37 TO 39°F" in; mercury breathes 37 <-> 39 (y 300 <-> 260), 1.2 s yoyo, finite |
| 9.02 | "When" @9.02 | HUD swaps to "BEHIND THE FRONT"; readout out; cold-front polygon enters at x 400 |
| 9.54 to 10.70 | "behind a front drops that fast" | front edge travels x 400 -> 1440 (1.16 s, power2.inOut); mercury 38 -> 29 (y 280 -> 460), same span, colour flips at y 400 |
| 10.70 | "fast," @10.70 | readout "BELOW 32°F" in |
| 11.82 | "water" @11.82 | "RAINWATER" label + leader in; film shimmer continues |
| 13.66 | "drain" @13.66 | two small evaporation wisps rise 20 px from the film and fade out (the water does not leave); film unchanged |
| 15.34 | "freezes" @15.34 | film turns to ice: colour sweep left to right 0.8 s, crack lines draw in; "RAINWATER" crossfades to "ICE"; rain stops |
| 17.10 | "snow" @17.10 | snowflakes fall in the air region; snow layer grows 584 to 612 over 1.2 s; "SNOW" label + leader in |
| 17.36 to 18.40 | "keeps falling on it" | wind smear: flakes near the surface slide right 60 px with short streaks; snow layer top edge ripples (2 px), finite |
| 19.98 | "flash" @19.98 | HUD swaps to "FLASH FREEZE" at 84 px `fromTo(scale 1.12 -> 1, autoAlpha 0 -> 1, 0.45, power4.out)` |
| 21.24 | "and it's" @21.24 | source line swaps to "NWS Buffalo Blizzard Warning, 22 Dec 2022" |
| 0 to 24.6 | whole window | particles always moving; HUD fixed (no float on text riding particles) |
| 24.62 to 25.42 | after "before." @24.24 | exit fade-through: every element `to(autoAlpha 0, 0.8, power2.in)`; ground stays |
Comp duration 25.42 s.

## 6. CONTRACT
One file `compositions/g-a2-4-flash-freeze.html`, root `<div id="g-a2-4-flash-freeze-root" data-composition-id="g-a2-4-flash-freeze" data-width="1920" data-height="1080">`, ground on the root. PAUSED timeline at `window.__timelines["g-a2-4-flash-freeze"]`. Ids/classes `ff-`. Particles: seeded positions, driven by the timeline (no Math.random at seek time, no CSS keyframes, finite repeats); if drawn on a canvas, paint from `tl.eventCallback('onUpdate', ...)`. Everything else: `references/mg-quickref.md`.
Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a2-4-flash-freeze`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a2-4-flash-freeze`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 6: state mercury y at 1.0, 3.5, 7.0, 11.0 s and the thermometer formula used.

## 8. RECEIPT
As the template.
