# g-a2-4-vines-gangoiti · A2-S2 17.74 to 31.898 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules" (paper card, chip, source line). Base: `compositions/g-a2-3-vines-signs.html` (built first): copy its ground and the Viñes card (state B position and CSS) exactly, renaming every id to this comp's prefix. Card pairing motion: official `split-tilt-cards` (the arrive-from-the-wing feel only; no 3D tilt on text).

## 0. Claim
Havana called Viñes "Father Hurricane". He died in 1893 and Father Lorenzo Gangoiti took over: Belen, under Gangoiti, carried Viñes's storm forecasting on to 1900.

## 1. Source
- Father Hurricane: factcheck/a2-r1.md row 10 (SECONDARY: Rubiera via cubamemorias.com/?p=25235, "Padre Huracán", in Havana); chip confirmed row 11.
- Gangoiti successor, director in 1900: sources-cuba.md §1 (cubamemorias.com "a quien sucedió el Director, el P. Lorenzo Gangoiti"); factcheck/a2-r1.md rows 12 to 14 (spelling Gangoiti kept, row 14).
- Carried on Viñes's work: sources-cuba.md §1 (AOML "had carried on the work of Fr. Benito Viñes in forecasting storms in the vicinity of Cuba"); row 15; a2-r2 row 2.

## 2. Datum, scale, orientation
Full-frame designed scene on the g-a2-3 ground. No map, no scale. Comp-local time = segment time minus 17.74.

## 3. Geometry (px)
- Opening state (frame 0) = g-a2-3's state B: Viñes card at x 1330 to 1825, y 54 to 203 (scale 0.45), source line top-left. Nothing else.
- Viñes card, centre state: back to g-a2-3's state A (1100 x 330, left 410, top 300 here, 75 px higher than in g-a2-3 to leave room for the chip).
- Chip "FATHER HURRICANE", tag line "Padre Huracán" (Shared rules chip): centred x 960, top 700 (under the card, inside x < 1600).
- Two-card state (from 26.26): Viñes card at scale 0.75, box x 96 to 921, y 380 to 628, opacity 0.6 (the past). Gangoiti card full size 840 x 300, x 984 to 1824, y 360 to 660 (bottom 660, clear of the y >= 680 corner): eyebrow "Belen Observatory · Havana" (22 px `#6b6257`), name "P. Lorenzo Gangoiti" (Arial Black 900 52 px `#2a2622`), role "Director, 1900" (Georgia italic 30 px `#6b6257`). Left text padding 48 px; measure the name: it must fit inside 744 px or drop to 48 px (still the big tier).
- Carry-on rule: a 4 px `#d8a13a` line from the Viñes card's right edge (x 921, y 504) to the Gangoiti card's left edge (x 984, y 510), drawn left to right.
- Source line (top-left): "Belen history (1925, reprinted) · José Rubiera · Wikipedia · NOAA AOML, 2015".
- Tiers: 52 (names), 44 / 30 (chip, roles), 22 (eyebrows, tag, source 19).

## 4. Must be true in the picture
1. Viñes's card always reads "P. Benito Viñes, S.J." with "Director from 1870"; Gangoiti's reads "Director, 1900". No death year on screen (the line speaks it; the Picture line puts none on the cards).
2. The two cards never overlap each other or the chip in any frame, mid-tween included.
3. Viñes is on the left (earlier), Gangoiti on the right (later), and the amber line runs from Viñes to Gangoiti.
4. No portrait, no monogram, no photo slot on either card.
5. Nothing in x >= 1600, y >= 680.

## 5. Text and cues (a2-s2.words.json; segment time, comp-local = minus 17.74)
- 17.74 ("People" 17.74): Viñes card returns from state B to the centre state, 17.74 to 18.44, power3.inOut.
- 18.94 ("Father" 18.94) /* FATHER HURRICANE @18.94 */: chip enters; tag line "Padre Huracán" at 19.24 ("Hurricane." 19.24).
- 20.20 to 22.82 (the book line): hold; card and chip drift.
- 23.30: chip exits (`to x:980, autoAlpha 0, 0.6, power3.in`), done 23.90.
- 24.16 ("Venez" 24.16, i.e. Viñes): card holds; its role line dims to 0.6 at 24.98 ("1893." 24.98).
- 26.26 ("Father" 26.26) /* GANGOITI @26.26 */: Viñes card slides left and scales to the two-card state, 26.26 to 26.86, power3.inOut; Gangoiti card slides in from x +600, 26.60 ("Lorenzo" 26.60) to 27.20, power3.out, landing as the name is spoken (27.08).
- 27.82 ("over" 27.82): Gangoiti role line "Director, 1900" in.
- 29.46 ("Venus's" 29.46, i.e. Viñes's) /* CARRIED ON @29.46 */: amber carry-on line draws 29.46 to 30.04.
- 31.36 ("Cuba." 31.36) to 31.898: hold.
- Host: A2-S2 17.74 to 31.898 (comp duration 14.158).

## Motion for the whole window
Card return, chip, card swap, line draw; every visible card drifts y +-4 px (2.4 s yoyo). Longest gap between beats 19.24 to 23.30, covered by the drift.

## Exit
Cut to the A2-S4 map: the whole root fades to 0 over the last 0.35 s (31.548 to 31.898).

## Footage under it
None: full-frame designed (coverage: cards plus ground, no empty block over a third of the frame for more than 3 s; the card or the card pair spans the frame centre throughout).
