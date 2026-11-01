# BRIEF g-a3-stair · A3-S9 · STANDARD (Sonnet 5.5, high effort) · on base `g-a3-house-section`

Read first: `references/mg-quickref.md`, `learnings/mg.md`, `library/inhouse/snippets/tokens.md`. Base: `compositions/g-a3-house-section.html` (copy its ground, grade line, floor, walls and roof verbatim; drop the partitions, tub, figure, ghost and foundation band; the basement below replaces the band). Read the base's built frames before starting. Fails the orchestrator's frame read twice → goes to Opus.
First picture after the book ad.

## 0. What this graphic claims
Of the three who had a basement they could reach, at least two were not down in it when the tornado hit; where the third was is unknown (H8, H22). The basement is drawn lit and empty.

## 1. SOURCE
- H8, Sec. 4.6.2.2: "NIST found that at least two of these three individuals did not access their basements before the storm hit. The circumstances of the third death, including the location where he or she took refuge, if any, are unknown."
- H22, footnote 176: "Only three of the 71 individuals who died in residences in the Joplin tornado had access to basements. Two of these three individuals did not take refuge in the basement before the storm hit".
SCHEMATIC, NOT TO SCALE.

## 2. DATUM, SCALE, ORIENTATION
As the base: grade line y 660, floor y 640–660, walls y 400–640 at x 520–540 and 1380–1400, roof (480,400) – (960,220) – (1440,400). Earth below y 660.

## 3. GEOMETRY
- Basement: walls x 540–560 and x 1360–1380, y 660–960; basement floor y 960–980 (x 540–1380); stroke `#4a5560` 4 px, interior fill rgba(74,85,96,.25).
- Floor opening for the stair: x 1120–1250 cut out of the house floor.
- Stair: 8 steps from (1250, 660) down-left to (1010, 960): run 30 px, rise 37.5 px each, stroke `#dfe7ee` 2 px.
- Light: bulb (10 px circle `#f5d98b`) at (800, 690) hanging from the floor underside; radial glow r 260, `#f5d98b` at .35 → 0, clipped to the basement interior.
- Nobody anywhere: no figure in the basement, on the stair or in the house.
- Collapse state: roof falls y +200, rotation 6°; both walls fall inward and flat onto the floor (rotate about their foot, about 80°); every piece rests at or above y 640. Floor, basement, stair and light never move.
- Chip (glass popup-chip, left 96, top 96): "2 OF 3 NOT DOWN THERE" 52 px.
- Source chip (glass source-label, left 96, baseline ≤ 1026, 20 px): "At least 2 of 3 · the third: circumstances unknown · NIST Sec. 4.6.2.2".
- Corner x ≥ 1600, y ≥ 680: earth only.

## 4. MUST BE TRUE IN THE PICTURE
1. The basement is lit and empty at every frame: no figure, no silhouette, no shadow of one.
2. The stair connects the house floor opening to the basement floor.
3. The collapse rests entirely on the house floor (y ≤ 640): nothing breaks through into the basement, and the basement shape and light are identical before and after.
4. "2 OF 3" and "At least 2 of 3" are the only counts; nothing says or shows where the third person was.

## 5. PANEL TEXT (exact) and CUES (a3-s9.words.json)
Text: "2 OF 3 NOT DOWN THERE" · "At least 2 of 3 · the third: circumstances unknown · NIST Sec. 4.6.2.2".
Host: a3-s9 "At" @0.00 → "help?" @10.44 + 0.8.
- 0.00 "At": house, basement and stair on from frame 0; the light fades up 0.0–0.8. Whole comp: slow push 1.00 → 1.05, linear, origin (960, 700).
- 0.96 "two": chip in.
- 1.40: source chip in.
- 2.48 "basement": the stair treads light up top to bottom (stagger 0.06 s).
- 1.5 → 8.2: the bulb's glow breathes (opacity .30 ↔ .38, 1.4 s, finite repeats).
- 8.28 "came": the house comes down (roof and walls, 0.6 s, power2.in), small settle bounce at 8.9; the basement stays lit.
- 9.90 "basement": the basement glow pulses once (.35 → .5 → .35).
- Exit: chips slide out in the last 0.6 s per quickref; fade-through to the next picture.

## 6–8. CONTRACT, TOOLS, DONE LINE, RECEIPT
`references/mg-brief-template.md` §6, §7, §7a and §8 unchanged, COMPID = `g-a3-stair`, root id `g-a3-stair-root`.
