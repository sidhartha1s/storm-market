# g-a6-8-warn24 · A6-S5 12.92 to end · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Base: the wire layer of `g-intro-4-wire-map` (plate, projection, Washington and Galveston pins, lit-wire style); copy after that base passed its frame read.

## 0. Claim
In 1915 the Weather Bureau's warning went out a full day (24 hours) ahead.

## 1. Source
- NWS Houston/Galveston 1910s (sources-a6.md §4): "the Weather Bureau had issued warnings 24 hours in advance".
- No row names the route or office of the 1915 warning: the wire is drawn Washington to Galveston as the Bureau's line, with no date or route label.

## 2. Datum, scale, orientation
g-intro-4 plate and projection: `X = (lon + 100) * 90`, `Y = (41 - lat) * 103.95`; Galveston (468.0, 1216.2), Washington (2066.4, 218.3). Camera framing both pins (the base's V-WIRE state). Havana pin and its line are NOT shown (1915 is not about Havana).

## 3. Geometry (px)
- Washington to Galveston wire: base style `#7fb2e5` lit with glow; a 40 px bright pulse `#f2f5f8` runs Washington to Galveston on the cue.
- Chip "WARNING · 24 HOURS AHEAD": glass, main line "24 HOURS AHEAD" Arial Black 900 56 px, eyebrow "WARNING" Arial 700 24 px `#93a3b2` tracking 4; centred x 960, top 150 (over open plate, not on the wire; check the wire path under it and move the chip down to top 700 if they cross, never over the pins).
- Day bar inside the chip under the main line: 24 tick marks (2 x 12 px, `#93a3b2`) across 480 px, filling `#f5d98b` left to right (one tick per hour, a clock, not a calendar).
- Source line top-left: "National Weather Service Houston/Galveston".

## 4. Must be true in the picture
1. Only Washington's line is drawn; no Havana line, no date.
2. "24 HOURS AHEAD": the bar has exactly 24 ticks, and it fills before the comp ends.
3. The 1900 wire's dark Havana line is not shown here (it returns in g-a6-9 for 1900).
4. Presenter circle: off if the Galveston pin or the chip sits in x >= 1600, y >= 680 on the chosen camera; state which.

## 5. Text and cues (a6-s5.words.json, 16.227 s; host starts at "And" 12.92)
Comp-local = word time − 12.92. Frame 0: plate, both pins, wire drawn but unlit (opacity 0.35).
- 12.92: source line in.
- 13.72 ("Weather") : wire lights (0.4 s); pulse runs Washington to Galveston 13.90 to 14.60.
- 14.34 ("warning") /* WARNING @14.34 */: chip in, eyebrow first.
- 15.20 ("full") /* 24 HOURS @15.46 */: day bar fills 15.20 to 16.10 (`ease:none`); main line lands at 15.46 ("day").
- Host end 16.227 + land time (at least 1.0 s: the chip holds while the pulse repeats every 1.2 s, finite repeats).

## Motion for the whole window
Pulse runs on the wire (repeats), camera drifts 1.00 to 1.02 linear, chip floats.

## Exit
A6-S6 opens on g-a6-9 with the same plate: cut, no fade (g-a6-9 frame 0 starts on this wire view).

## Footage under it
None: full-frame map.
