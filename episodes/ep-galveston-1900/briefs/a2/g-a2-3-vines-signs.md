# g-a2-3-vines-signs · A2-S2 0.00 to 17.74 · DEEP · Opus 5.5 high
Shared rules: `_list.md` "Shared rules" (paper card, chip, source line). Exemplars: `library/inhouse/then-now-scale.html` (layered diagram on the dark ground), `compositions/g-intro-6-island.html` (HUD labels, start-hidden SVG parts). g-a2-4 copies this comp's ground and the Viñes card: send this comp alone for a full-size read first.

## 0. Claim
Benito Viñes ran the Belen observatory from 1870 and read the signs a hurricane sends ahead of itself: the clouds, the long swell, the barometer. In 1875 he warned Havana before a hurricane arrived.

## 1. Source
- Director from 1870: factcheck/a2-r1.md row 7 (cubamemorias.com "En 1870 se puso al frente del Observatorio el P. Benito Viñes"; Wikipedia: arrived 7 March 1870).
- Signs: row 8 (Wikipedia quoting NOAA: he looked "at ocean swell and waves"; a paper on "storms and barometer data in Havana"). Row 8 CORRECTED the script: "high, thin" clouds and a "falling" barometer are NOT in the source. The diagram shows clouds, a swell and a barometer, and claims no cloud type and no needle direction.
- 1875 warning: row 9 (Wikipedia "On September 11, 1875, Viñes very likely issued the first-ever hurricane warning"); chip confirmed row 11. The chip never says "first".
- No portrait: `media/candidates/a2/picks.md` (only portrait is CC BY-SA 4.0). Text card only, no photo slot, no monogram.

## 2. Datum, scale, orientation
SCHEMATIC, NOT TO SCALE (a side view: sky above, sea below, the hurricane off to the right, the observer's instrument at the left). No distances, no heights, no pressure values. Fixed lines: sea surface y 700 from x 160 to 1560; the hurricane mass sits at the right, x 1330 to 1560, y 330 to 690; everything the storm "sends ahead" travels right to left, toward the barometer.

## 3. Geometry (px)
- Ground: canvas radial gradient (tokens.md), full frame from frame 0.
- Viñes card, state A (0.00 to 5.24): paper card centred, 1100 x 330, left 410, top 375. Eyebrow "Belen Observatory · Havana" (22 px) at top 40 inside; name "P. Benito Viñes, S.J." (Arial Black 900 52 px `#2a2622`); role "Director from 1870" (Georgia italic 30 px `#6b6257`). Inner padding 48 px left.
- Viñes card, state B (5.24 to end): the same card scaled to 0.45 and moved so its box is x 1330 to 1825, y 54 to 203 (top-right, clear of the circle corner). The text scales with the card (it is one object moving once, before the diagram builds; no text rides a camera move). In state B the name renders at about 23 px: that is a tag, not a reading target.
- Sea surface: line `#5a768f` 3 px, x 160 to 1560, y 700. Sea body below it: gradient `rgba(90,118,143,0.18)` to 0, y 700 to 1000.
- Hurricane mass: a cloud wall built from 6 to 8 overlapping ellipses, fills `#2a3644` and `#4a5560`, x 1330 to 1560, y 330 to 690; slow internal churn (each ellipse rotates +-3 deg, finite yoyo). Label "Hurricane" diagram label (Arial 700 22 px `#93a3b2` tracking 3), right-aligned at x 1560, baseline y 312.
- Clouds: 5 thin streak clouds (stroked paths, `#93a3b2` 3 px, opacity 0.8, 120 to 220 px long), spread across y 250 to 360, x 520 to 1300, fanning out leftward from the storm top. Label "Clouds" at x 520, baseline 232.
- Long swell: a sine path on the sea, amplitude 16 px, wavelength 260 px, x 400 to 1330, centred y 730, `#7fb2e5` 4 px; it rolls right to left (path x offset tween) for the rest of the comp. Label "Long swell" at x 760, baseline 800.
- Barometer: dial centre (330, 470), radius 130: rim `#d8a13a` 6 px, face `#0b1016`, 9 tick marks (no numbers, no words on the face), needle `#f2f5f8` 4 px from the centre, resting at -20 deg. Label "Barometer" centred under it at baseline 640.
- Chip "1875: A WARNING BEFORE THE STORM" (Shared rules chip, no tag line): centred at x 960, top 840 (over the sea body, under the swell label, inside x < 1600).
- Source line (top-left): "Belen history (1925, reprinted) · Wikipedia · NOAA AOML, 2015".

## 4. Must be true in the picture
1. Everything the hurricane sends out (cloud streaks, swell) starts at the storm side and travels toward the barometer: right to left, never the other way.
2. The barometer face has no numbers, no "falling", no pressure unit; the needle only trembles around its rest (+-6 deg) and never sweeps in one direction (row 8).
3. Cloud label says "Clouds" only (no "cirrus", no "high, thin").
4. The chip says "A WARNING", never "first".
5. No label sits under a cloud streak, the swell or the storm mass in any frame, including the first 0.5 s of each entrance.
6. Nothing in x >= 1600, y >= 680 (storm mass right edge 1560; card B is above y 203).

## 5. Text and cues (a2-s2.words.json; Whisper writes Viñes as "Venez")
- 0.00: ground on, card A rises in (y 24 to 0, autoAlpha 0 to 1, 0.5 s, power3.out) with eyebrow and name visible; role hidden. Source line in at 0.00.
- 0.78 ("Father" 0.78) /* VINES @0.78 */: name line pulses once (scale 1 to 1.03 to 1, 0.4 s).
- 3.96 ("1870." 3.96) /* 1870 @3.96 */: role line "Director from 1870" in (y 10 to 0, autoAlpha 0 to 1, 0.35 s).
- 5.24 ("He" 5.24): card A to state B, 5.24 to 5.94, power3.inOut.
- 6.20 ("signs" 6.20): sea line draws left to right 6.20 to 6.80; sea body fades in.
- 7.84 ("ahead" 7.84): hurricane mass grows in from the right (x +80 to 0, scale 0.9 to 1, autoAlpha 0 to 1, 0.6 s, power3.out); label at 8.16 ("itself." 8.16).
- 9.14 ("clouds," 9.14) /* CLOUDS @9.14 */: cloud streaks draw one by one (strokeDashoffset, 0.12 s apart), each from the storm side; label "Clouds" at 9.30.
- 10.32 ("swell," 10.32) /* SWELL @10.32 */: swell path draws right to left 10.32 to 10.92, then rolls; label at 10.50.
- 11.28 ("barometer." 11.28) /* BAROMETER @11.28 */: dial pops in (scale 0.6 to 1, back.out(1.6), 0.45 s), needle trembles from 11.60 (+-6 deg, 0.3 s yoyo, finite repeats to the end); label at 11.45.
- 12.40 ("1875," 12.40) /* 1875 @12.40 */: chip enters.
- 15.36 ("hurricane" 15.36): storm mass nudges left 20 px (0.8 s, sine.inOut): it is "coming".
- 16.74 ("arrived." 16.74): hold; chip exits 17.14 to 17.74 (`to y:-24, autoAlpha 0, 0.6, power2.in`).
- Host: A2-S2 0.00 to 17.74 (comp duration 17.74).

## Motion for the whole window
Card rise and move, then storm churn from 7.84, swell roll from 10.92, needle tremble from 11.60, cloud streaks drift left 8 px/s from their draw. Longest gap between beats 12.40 to 15.36, covered by the churn, roll and tremble.

## Exit
Hard cut to g-a2-4 at 17.74 ("People"): g-a2-4 opens on the same ground with card B in the same place, so the cut is invisible for the ground and the card. The diagram parts (sea, storm, clouds, swell, barometer) fade out 17.39 to 17.74 (fade-through of the diagram layer only).

## Footage under it
None: full-frame designed (coverage 100 %).
