Host: id=g-a6s05-wires file=compositions/g-a6s05-wires.html start=1043.62 (timeline-map.md table 1; the mount in index.html wins) duration=16.94 s track=2

# g-a6s05-wires · A6-S5, A6-S6 · two desks get a wire of their own; back-up radio is asked for (wave 5, chain family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 1, 6, 7, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5. Bases: `mg_specs/briefs/g-a1s13-chain.md` (the whole chain) and `mg_specs/briefs/g-a3s04-links.md` (the dark links).
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id, never `root` (rule 3). The study's hidden counties are "County A" and "County B" only (rule 8): this comp shows neither, and the study's p. 29 is not shown because it prints the county letters. A flash is a stroke or fill change, never a scale pop (rule 12).
**Spoken (A6-S5):** "Two desks got a wire of their own in two towns. One fire department and one police department were hooked directly to the Weather Bureau teletype."
**Spoken (A6-S6):** "For the failed telephones, the team asked for back up radio between Weather Bureau offices, and out to civil defense and local offices."
**One look:** the chain; two new desks, each on a solid wire straight from the teletype, both lit; then the dark telephone links with dotted amber radio arcs drawn over them.

## 0. What this graphic claims
After the tornadoes, one fire department and one police department, in two towns, were connected directly to the Weather Bureau teletype. Separately, the survey team recommended back-up emergency radio. The first is a thing done at two desks; the second is a thing asked for.

## 1. Source
- `edit_script.md` A6-S5, Rows [G; study printed p. 29]. A6-S6, Rows [G, Rec. 7; survey printed p. 2].
- The chain is the intro's: design sheet section 6 "Intro version", the built `compositions/g-i1s9-chain.html`, and `g-a1s13-chain.md` section 3 (station boxes, links, labels).

## 2. Datum, scale, orientation
The chain line is y 520 and no intro station moves: teletype box x 96 to 236, y 450 to 590; South Bend telephone x 316 to 460; miniature list x 540 to 800, y 350 to 650; the chain's own desk x 840 to 1095, y 490 to 618; microphone x 1170 to 1272; house x 1400 to 1577.
Two new desks stand off the line, one above and one below, both between the teletype and the list in x so their wires do not cross the telephone or the list:
| New desk | Drawing | Box (x, y) | Wire, solid |
|---|---|---|---|
| A | `media/drawings/desk.svg` at 0.7 (210 x 105) | 300 to 510, 150 to 255 | from the teletype's top (166, 450) up to y 216, then right to the desk's left edge (300, 216) |
| B | `media/drawings/desk.svg` at 0.7 | 300 to 510, 760 to 865 (40 px lower than first drawn: at y 720 its telephone sat on `South Bend`) | from the teletype's bottom (166, 590) down to y 826, then right to (300, 826) |
In this comp the teletype is the Weather Bureau's: its label reads `Weather Bureau teletype`, not `Kansas City forecasters`.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient with the intro's faint sweep band, on from frame 0 |
| Chain | the five stations, the chain's desk and the links of `g-a1s13-chain.md` section 3, all at rest (lines `#55606b`), as `g-a3s04-links` leaves them: telephone links dotted and dark, the miniature list at opacity 0.36. Labels as that brief, except the teletype's: `Weather Bureau teletype` (left-aligned, left 180, three lines, x 180 to 266, y 676 to 760, beside wire B, which runs down x 166; `Weather Bureau` on one line would run into station 2's label) |
| Desks A and B | section 2; lines `#55606b` at rest, Headline white when lit; their own telephones on the cradle |
| Wires A and B | 4 px, round caps and joins, Amber 2, drawn from the teletype outward with `strokeDashoffset` |
| Desk labels | Arial 700 22 px, Label grey: `a fire department` at left 530, top 190; `a police department` at left 530, top 800 (with desk B) |
| Source line | fixed HUD, left 96, bottom 60: `Disaster Research Center, 1966, p. 29`. It leaves when the paper strip arrives |
| Second office | `media/drawings/telephone-lifted.svg` inline at scale 1.2, box x 700 to 822, y 150 to 277, lines `#55606b`; label `another Weather Bureau office`, Arial 700 22 px, Label grey, left 840, top 200 |
| Radio arc 1 | from the South Bend telephone's top (388, 433) to the second office's left (700, 220): a quadratic curve with its control point at (480, 190), dotted (`stroke-dasharray="0.1 14"`), 5 px, round caps, Amber 2 |
| Radio arc 2 | from the South Bend telephone's top (388, 433) over the list to the chain desk's top (967, 487): control point (680, 140), same stroke ((680, 290) crosses the list) |
| Desk label | `civil defense and local offices`, Arial 700 22 px, Label grey, centred on x 967, top 640 (under the chain's desk, above the labels row) |
| Paper strip | Beige polaroid, left 96, top 780, 1000 x 124 (right 1096, bottom 904), the chain strip's shadow. Quote, Georgia 44 px, Caption dark, left 136, top 796: `“back-up emergency radio communications”`. Attribution, Arial 700 22 px, Caption dark sub, tracking 2, left 136, top 862: `Weather Bureau survey report, 1965, p. 2, recommendation 7` |
Arc 2 passes above the miniature list (top y 350) only if its curve stays above y 340 between x 540 and x 800: check it by script and lift the control point if it does not.

## 4. Must be true in the picture
1. Two new desks, no more, and each has its own solid wire from the teletype. No town, county or department name beyond `a fire department` and `a police department`.
2. `Kansas City` is not on screen: the teletype here is the Weather Bureau's.
3. The telephone links stay dark and dotted through the whole comp; nothing amber travels along them.
4. The radio arcs are dotted: a recommendation, not a thing built. They appear only in A6-S6, after desks A and B and their wires have left.
5. The microphone and the house stay dark on every frame.
6. One source per frame: the p. 29 line, then the strip's attribution.
7. Nothing in x >= 1600 and y >= 680 (the strip ends at x 1096). Nothing appears before its spoken word.
8. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). It holds without staging: at every step the largest empty block is the band above the chain (y 0 to 350, 32.4 % of the frame) or the band below its labels (y 735 to 1080, 31.9 %), each under a third. Desks A and B fill both bands from 0.18 s to 8.68 s, the strip fills the lower one from 10.90 s and the second office the upper one from 12.10 s.

## 5. Text (exact) and cues
Text: the chain's labels as `g-a1s13-chain.md` with `Weather Bureau teletype` · `a fire department` · `a police department` · `another Weather Bureau office` · `civil defense and local offices` · `“back-up emergency radio communications”` · `Weather Bureau survey report, 1965, p. 2, recommendation 7` · `Disaster Research Center, 1966, p. 29`.
t from comp start = the segment's wav start inside the composition (timeline-map.md table 5: A6-S5 -0.32, A6-S6 8.26) plus the word's time; a segment's first word uses table 5's first sound.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A6-S5 | 0 | Two | 0.00 | 0.00 | first frame: the chain at rest, sweep band running |
| 1 | A6-S5 | 1 | desks | 0.50 | 0.18 | desks A and B draw on, dark (0.5 s) |
| 2 | A6-S5 | 4 | wire | 1.18 | 0.86 | wire A draws from the teletype to desk A (0.5 s); the source line fades in |
| 3 | A6-S5 | 9 | two | 2.28 | 1.96 | wire B draws to desk B (0.5 s) |
| 4 | A6-S5 | 12 | fire | 3.98 | 3.66 | desk A lights (lines to Headline white, 0.3 s) and its label fades in |
| 5 | A6-S5 | 16 | police | 5.30 | 4.98 | desk B lights and its label fades in |
| 6 | A6-S5 | 23 | weather | 7.12 | 6.80 | the teletype lights (lines Headline white, paper Amber 2) |
| 7 | A6-S6 | 0 | For | 0.00 | 8.68 | desks A and B, their wires and labels fade out (0.4 s); the teletype returns to rest |
| 8 | A6-S6 | 3 | telephones, | 0.84 | 9.10 | the dotted telephone links step to Label grey and back to `#55606b` once (0.2 s each way) |
| 9 | A6-S6 | 8 | backup | 2.64 | 10.90 | the paper strip rises (`y:60` to 0 with the fade, 0.4 s); the p. 29 source line has gone out in the 0.15 s before this cue (from 10.75), so there is one source on every frame |
| 10 | A6-S6 | 11 | Weather | 3.84 | 12.10 | the second office draws on with its label (0.4 s); radio arc 1 draws to it (0.6 s) |
| 11 | A6-S6 | 17 | civil | 5.92 | 14.18 | radio arc 2 draws over the list to the chain's desk (0.7 s); the desk's label fades in |
| 12 | end | | | | 16.94 | comp ends on the hold |

## 6. Contract
As `references/mg-brief-template.md` section 6, with plan rule 3 over its `id="root"`. File the builder may write: `compositions/g-a6s05-wires.html` only. Id prefix `wir-`, root id `wir-root`. Bases it copies: `compositions/g-a1s13-chain.html` (wave 1) for stations, links, labels and strip; `compositions/g-a3s04-links.html` (wave 3) for the dark dotted links. Assets mounted, all inline: `media/drawings/teletype.svg`, `media/drawings/telephone-lifted.svg`, `media/drawings/desk.svg`, `media/drawings/microphone.svg`, `media/drawings/house.svg`. No later composition copies this one.

## 7. Tools
As the template's section 7.

## 7a. Done line
As the template's section 7a, all seven. Done line 5: read the first half second of each arc for a label under it. Done line 6: both arcs' points and the two wire paths are computed by a script from section 2 and stated in the receipt, with the lowest y of arc 2 between x 540 and x 800.

## 8. Receipt
As the template's section 8, plus: the measured width of the quote on the strip and of the label `another Weather Bureau office`.

## Frames the verifier reads
First frame 0.00 and the frame after it (0.04); 0.80 (desks drawn, dark); 1.50 (wire A); 2.60 (wire B); 4.10 (desk A lit); 5.40 (both lit); 7.20 (teletype lit); 9.40 (S5 parts gone); 11.40 (strip); 12.90 (arc 1); 15.00 (arc 2); last frame 16.85.
