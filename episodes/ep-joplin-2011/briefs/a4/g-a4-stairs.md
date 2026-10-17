# BRIEF · g-a4-stairs · "The stairs down were only about one person wide." · cross-section · STANDARD (Sonnet 5.5, high)

Episode ep-joplin-2011, act A4, segment A4-S10. Full-frame MG, own ground.
Base element: BELOW-GROUND LINE (T1-S3, `_list.md` "Shared bases"): use its stroke, colour and "below ground" label
style for the ground line here. Exemplar for a full-frame labelled SVG diagram: `library/inhouse/radar-beam.html`.
`g-a4-cellar` uses the same ground line; keep the two consistent.
Open numbers: building and stair dimensions (`_list.md` Open 4): SCHEMATIC · NOT TO SCALE.

## 0. What this graphic claims
The theater's basement stairs were about one person wide, and not everyone got down. One interviewee says about 15
made it into the basement. Of the 56 inside, the three who were lost had not reached the basement; the director was
at the top of the stairs when the building was hit.

## 1. SOURCE
- B28 "The basement stairs were approximately one-person wide, and not everyone made it down the stairs before the theater was hit" NIST Sec. 4.4.3.
- B29 "approximately 15 people made it into the basement before the building was hit." Sec. 4.4.3, footnote 153 (NIST Interview 115).
- B24 "There were 56 people in the theater at the time of the tornado." Sec. 1.2.
- B25 "Three of these occupants lost their lives ... According to interviewees, the victims did not make it into the basement before the tornado hit." Sec. 1.2.
- B31 "no evidence was found that any of those killed were located in the basement at the time the tornado hit." Sec. 4.6.2.1.
- B30 "The director, who was standing at the top of the basement stairs when the building was hit, was fatally injured that day". Sec. 4.4.3.
- Counts drawn (computed by script): 56 − 15 = 41 figures above the line, 15 below.

## 2. DATUM, SCALE, ORIENTATION
- SCHEMATIC · NOT TO SCALE (small tier, top-left under the chips).
- Ground line (BELOW-GROUND LINE style) y 560, x 160 to 1500; its "below ground" label at its left end, x ≥ 110, under the line.
- Ground floor (the theater hall): outline x 200 to 1400, y 260 to 560. Basement: outline x 760 to 1360, y 560 to 900.
- Stair: from the hall floor at x 700 to 760 on the ground line, down to the basement floor at (980, 900), 8 steps.
- Width inset ("ONE PERSON WIDE", front view of the stair mouth): frame x 1430 to 1580, y 260 to 520.
- Chips band: y 110 to 210, x 96 to 1400. Presenter corner (x ≥ 1600, y ≥ 680) stays clear.

## 3. GEOMETRY
- Figures: 56 person glyphs, 14 x 30 px, `#dfe7ee`. At the start all 56 stand in the hall on seeded positions, with
  6 to 8 of them queued at the stair head.
- 15 figures walk down the stair single file (per-leg `x`/`y` tweens along the stair's polyline, 0.12 s apart) and stand
  on the basement floor in two rows. 41 stay above.
- Three of the 41 turn Danger red 1 `#c0392b`: one stands at the stair head (x 700 to 760, on the ground line: the
  director, B30, one of the three lost by B24 + B25 + B30); the other two stand on the hall floor away from the stair
  (schematic places: no row says where they were).
- Width inset: a front view of the stair mouth, opening 34 px wide, one figure glyph filling it, label "ONE PERSON WIDE"
  (diagram-label tier) under it.
- Chips (36 px Arial Black 900 `#f2f5f8`): "STAIRS ONE PERSON WIDE" at y 130; "56 INSIDE · ABOUT 15 GOT DOWN" at y 190.
- Label "THE DIRECTOR" (diagram-label tier) beside the stair-head figure, on the hall side, clear of the stair and the queue.
- Source line bottom-left (x 96, baseline 1026): "one interviewee · NIST footnote 153 · Sec. 4.6.2.1".

## 4. MUST BE TRUE IN THE PICTURE
1. 56 figures in total, always; after the walk 15 below the line and 41 above (count by script on the DOM).
2. All three red figures are above the line; none in the basement or on a step below the ground line.
3. One red figure stands at the stair head, and "THE DIRECTOR" labels that figure.
4. The figures go down one at a time: never two side by side on a step.
5. No label sits on a figure, a step or the ground line.

## 5. PANEL TEXT (exact) and CUES
Text: "STAIRS ONE PERSON WIDE" · "56 INSIDE · ABOUT 15 GOT DOWN" · "ONE PERSON WIDE" · "THE DIRECTOR" · "below ground"
(the base's wording) · "SCHEMATIC · NOT TO SCALE" · the source line.
Cues (`_list.md` "Cue notation"):
- frame 0: ground on, ground line drawing; hall, basement and stair draw a4-s10 "The" 0.00 → "down" 0.86; 56 figures in
  (stagger) a4-s10 "stairs" 0.60.
- width inset + "STAIRS ONE PERSON WIDE" a4-s10 "one" 1.82.
- queue shuffles forward a4-s10 "Someone" 3.88.
- "56 INSIDE · ABOUT 15 GOT DOWN" a4-s10 "15" 5.04; the 15 walk down a4-s10 "15" 5.04 → "down." 5.92 + 1.0 s (single
  file, stagger 0.12 s).
- three figures turn red a4-s10 "three" 8.14; the basement outline pulses once, empty of red, a4-s10 "basement" 9.30.
- "THE DIRECTOR" a4-s10 "director" 11.34.
- hold with a 2 px float on every figure; fade-through over the last 0.6 s; host ends a4-s10 "moment." 13.18 + 1.0 s.

## 6 to 8. Contract, tools, done line, receipt
`references/mg-brief-template.md` §6 to §8 verbatim, COMPID `g-a4-stairs`.
