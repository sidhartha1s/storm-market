Host: id=g-a4s02-countyb file=compositions/g-a4s02-countyb.html start=668.56 duration=32.43 s (timeline-map.md tables 1 and 5, read again 12 Oct 26; the mount in index.html wins; last sound at 31.43) track=2

# g-a4s02-countyb · A4-S2, A4-S3, A4-S4, A4-S5 · heard one county over, told his own members, radioed the police, and the path he counted on (wave 1, chain family base for a county chain)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 6, 7, 8. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). Text printed on a moving object fades before it leaves the text-safe margin (rule 2): the map's two labels fade before the map slides out. The root is styled through its id and is never `id="root"` (rule 3). The study's hidden county is labelled `County B` only; `County A` never appears in this comp, and no real county or town name appears anywhere in it (rule 8). A flash is a stroke or fill change, never a scale pop (rule 12). Beat counts were held against each spoken window when this brief was written (rule 13): the closest two beats are 0.20 s apart (A4-S3, "no" and "other") and each is a 0.3 s stroke change.
**Spoken (A4-S2):** "He'd heard about it one county over, where he was helping the sheriff recover a person lost in the water. State Police had told that sheriff a tornado was coming in from the west."
**Spoken (A4-S3):** "He told his own civil defense members, and no other office in his own county."
**Spoken (A4-S4):** "At about seven thirty he saw the tornado himself. He radioed the city police with its location and direction, and asked them to tell the radio station."
**Spoken (A4-S5):** "That was the path he counted on. Civil defense tells the police, the police tell the station, and the station tells everyone."
**One look:** a river with two marks at its bank and a tornado mark coming from the west, while a small grey chain waits to the east; the chain takes the frame and its first desk goes amber; a dotted radio arc carries the light to the police desk; a grey ghost runs on to the microphone and the house, and nothing past the police desk is ever amber.

## 0. What this graphic claims
The civil defense director of County B heard about the tornado in the next county, where he was with that county's sheriff at the water. He told his own civil defense members and no other office in his county. At about 7:30 PM he saw the tornado himself and radioed the city police, asking them to tell the radio station. He counted on the police to pass it to the station and the station to everyone: that part is drawn as a grey ghost, because the picture does not say it happened.

## 1. Source
- `edit_script.md` A4-S2, A4-S3, A4-S4, A4-S5, Rows [A13, C5; study printed p. 21] (County B). The Picture notes of those four segments are the only source of what is drawn.
- "County B" is the study's own code, not a place name. The map of A4-S2 is "a plain map we draw, no names and no real outlines": no file from `media/maps/` is used and nothing on it is traced from a real place. It is labelled nowhere as a county.
- The chain: design sheet section 6 and the built `compositions/g-i1s9-chain.html` (link, light and ring code). The clock stamp: design sheet section 8 and the built `compositions/g-t1s2-warning.html`. The chip: the glass chip of the built `compositions/g-i1s6-page.html` (`.pol-chip`).

## 2. Datum, scale, orientation
SCHEMATIC, NOT TO SCALE, in both halves. West is the left edge: the tornado mark enters from x < 0 and the director's own county, the chain, lies to the east (right).
The chain's line is y 520 at full size and the message runs left to right: civil defense desk, police desk, microphone, house.
The chain is one SVG group authored at its full size. In A4-S2 it waits at scale 0.5 about the authored point (1577, 380): it then spans x 836.5 to 1577 with its authored line at y 450 and its lines 2 px. On A4-S3 it grows to scale 1 about the same point.
**Stage offset (plan rule 22, 12 Oct 26).** The chain, the radio arc, the light, the ghost and the four station labels are one stage. Every number given for them below is the authored number, on a line at y 520, and is kept so later comps copy the blocks unchanged. The whole stage is drawn 132 px lower for the whole window, as one offset on the stage. On screen: the full chain's line is y 652, its skyline (the house aerial) y 539, its station labels y 808 to 836; the waiting chain's line is y 582 and it spans y 525 to 631. The map, the chip and the stamp are not in the stage: their numbers below are screen numbers.
Clock angles, clockwise from 12 (by script): 7:30 is hour 225.0, minute 180; the hands start at 7:25 (hour 222.5, minute 150).
Colours: ground `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)`; Label grey `#93a3b2`; Body light `#dfe7ee`; Headline white `#f2f5f8`; Amber 2 `#e8c56a`; Panel dark `#15202b`; Cold blue 2 `#7fb2e5` (the river only). "Unlit" in this comp is Label grey at full strength, the Picture note's own word, not the intro's 55 % mix.

## 3. Geometry (screen px)
Ground, all four segments: canvas gradient, on from frame 0, with the intro's faint sweep band (520 px wide, Label grey at 6 %, drifting left to right, ease none) for the whole window.

The map (A4-S2, comp 0.00 to 10.46), one group `cntb-map`:
| Element | Px |
|---|---|
| River | one path, Cold blue 2, 10 px, round caps, no fill: `M570 120 A520 520 0 0 1 530 420 A420 420 0 0 0 600 700 A520 520 0 0 1 550 960` (the first path moved 100 px right; three circular arcs, bulges 22.5, 25.6 and 17.1 px by script; the line runs x 528 to 601 by script) |
| Sheriff's mark | circle, centre (640, 582), radius 14, 4 px Body light, fill Panel dark; label `the sheriff`, Arial 700 26 px, Body light, centred on x 640, top 518 |
| Civil defense mark | circle, centre (710, 582), radius 14, same stroke; label `civil defense`, same type, centred on x 710, top 614 |
| Tornado mark | `media/drawings/tornado-mark.svg` inline, scale 2 (120 x 160 px), `stroke-width="3"` on the group (6 px lines), stroke Body light, never red. It enters from box left -140 and comes to box x 250 to 370, y 502 to 662, then drifts to box left 290 by 10.06. It never reaches x 500 |
The two marks, their labels and the tornado mark sit on the waiting chain's line, y 582, the frame's middle.

The chain (all four segments), one group `cntb-chain`, authored numbers at full size (on screen every y is 132 lower):
| Element | Px |
|---|---|
| Civil defense desk | `media/drawings/desk.svg` inline, `translate(96 490) scale(0.85)`, `stroke-width="4.7"` (box x 96 to 351, y 490 to 617.5, top surface y 524, centre x 223.5). Its `dw-phone` group is not rendered: he used a radio, and the note gives the telephone to the police desk |
| Police desk | `media/drawings/desk.svg` inline, whole, `translate(582 490) scale(0.85)`, `stroke-width="4.7"`, telephone 3.5 (box x 582 to 837, centre x 709.5; the telephone stands at x 670 to 750 and rises to y 471) |
| Microphone | `media/drawings/microphone.svg` inline, `translate(1068 420) scale(0.85)`, `stroke-width="4.7"` (box x 1068 to 1170, y 420 to 615.5, centre x 1119); lamp (`dw-lamp`) Panel dark in every frame |
| House | `media/drawings/house.svg` inline, `translate(1400 430) scale(0.68)`, `stroke-width="5.9"` (box x 1400 to 1577, y 430 to 600, aerial to y 407, centre x 1488.5); windows Panel dark in every frame |
| Links, y 520, 4 px Label grey, dotted (`stroke-dasharray="0.1 14"`, round caps) | 837 to 1068 and 1170 to 1400. No ground link joins the two desks |
| Unlit state | every line Label grey, bodies Panel dark |
| Labels (HTML, outside the group, hidden until A4-S3) | Arial 700 22 px, line-height 28, Label grey, top 676, each 200 px wide and centred on its station: `civil defense` (x 223.5), `city police` (x 709.5), `the radio station` (x 1119), `a family` (x 1488.5) |

Fixed layer:
| Element | Px |
|---|---|
| County chip | glass chip as `.pol-chip`, left 836, top 316, height 46, padding 0 x 22, Arial 700 26 px, Body light: `County B` and nothing else, on from frame 0. While the chain waits it sits at left 836, top 448, 31 px over the waiting chain. As the chain grows (10.16 to 10.82) it moves straight up to left 836, top 250 with a plain `to()` (power2.inOut), where its foot lines up with the stamp's foot at y 296, and it stays there over the full chain. Its old single place was left 836, top 316 |
| Clock stamp (A4-S4 on) | design sheet section 8: glass card left 96, top 96, 590 x 200; clock face `media/drawings/wall-clock.svg` inline at `translate(129 134)` (centre (191, 196)). In the eyebrow slot the word `about`, Arial 700 26 px, Body light, left 286, top 108. Time `7:30 PM`, Courier New 700 84 px, Amber 2, x 284, y 142. The two read as one line of sense, `about 7:30 PM`. No place line |
| Radio arc (A4-S4 on; in the stage, authored numbers) | path `M224 508 Q425 300 626 508` (apex (425, 404) by script; on screen (425, 536)), Amber 2, 4 px, dotted like the links. It starts over the civil defense desk and ends over the bare left end of the police desk's top |
| The light | Amber 2 dot, radius 10, moved along the arc with `getPointAtLength` from a 0 to 1 proxy tween (seek-safe) |
| Ghost (A4-S5; in the stage, authored numbers) | Label grey dot, radius 8, and a 6 px Label grey line that grows behind it over the two dotted links: x 837 to 1068, then x 1170 to 1400, both at y 520 (on screen y 652). Never Amber 2 |

## 4. Must be true in the picture
1. Amber reaches two things and no more: the civil defense desk (A4-S3) and the police desk (A4-S4, only when the light has crossed the arc). The microphone's lamp and lines, the house's lines and windows and both dotted links are never amber in any frame.
2. The ghost is Label grey from its first frame to its last and starts at the police desk. It never touches the civil defense desk or the arc.
3. `County B` is the only county label and its chip carries those two words alone. No `County A`, no real county, town or river name, no state outline. The map carries two labels, `the sheriff` and `civil defense`, and nothing else.
4. The map and the chain are two different counties: the tornado mark, the river, the two marks and their labels stay west of x 800, the waiting chain stays east of x 836, and the chip sits over the chain, never over the map.
5. The tornado mark comes from the left edge and moves east. It is Body light, never red, and it never reaches the river.
6. The civil defense desk has no telephone; the police desk has one, handset on the cradle. Nobody is drawn: the two marks on the map are plain circles.
7. The stamp reads `about` and `7:30 PM` together, hands at 225.0 and 180 degrees, and names no place.
8. Order in A4-S3: the civil defense desk goes amber first; the other three stations are named after it and stay Label grey.
9. Nothing appears before its spoken word. Nothing of ours in x >= 1600, y >= 680. No label under a line, the arc, a dot or another label, including while the chain grows (its labels are hidden until it has stopped).

## 5. Text (exact) and cues
Text: `County B` · `the sheriff` · `civil defense` (on the map, and again under the first desk) · `city police` · `the radio station` · `a family` · `about` · `7:30 PM`.
Cue words and times are from `audio/a4-s2.words.json` (34 words), `a4-s3.words.json` (15), `a4-s4.words.json` (27) and `a4-s5.words.json` (22), read on 12 Oct 26. t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A4-S2 -0.40, A4-S3 9.84, A4-S4 14.52, A4-S5 23.57) plus the word's time; a segment's first word uses the table's "first sound" (0.00, 10.06, 14.77, 24.14). Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A4-S2 | 0 | He'd | 0.40 | 0.00 | first frame: ground, the chain waiting at half size in Label grey with its two dotted links, the chip `County B` over it. No map yet |
| 1 | A4-S2 | 4 | one | 0.98 | 0.58 | the river draws on from top to bottom (0.8 s, `strokeDashoffset`) |
| 2 | A4-S2 | 8 | he | 2.56 | 2.16 | the civil defense mark lands (0.3 s fade with `y:16` to 0) with its label |
| 3 | A4-S2 | 12 | sheriff | 3.28 | 2.88 | the sheriff's mark lands the same way with its label |
| 4 | A4-S2 | 19 | water. | 5.10 | 4.70 | the river's stroke goes to Headline white and back to Cold blue 2 (0.3 s each way) |
| 5 | A4-S2 | 23 | told | 6.82 | 6.42 | the sheriff's mark fills Amber 2 (0.3 s) and stays |
| 6 | A4-S2 | 27 | tornado | 7.84 | 7.44 | the tornado mark comes in from the left edge to box left 150 (1.4 s, power2.out), then drifts to box left 190 (ease none, to 10.06) |
| 7 | A4-S2 | 33 | west. | 9.24 | 8.84 | the civil defense mark fills Amber 2 (0.3 s): he has heard |
| 8 | A4-S3 | 0 | He | 0.22 | 10.06 | the map's two labels fade (0.15 s), then the whole map group slides out left with its fade (`x:-1000`, 0.4 s, power3.in; gone by 10.46) |
| 9 | A4-S3 | 1 | told | 0.32 | 10.16 | the chain grows from 0.5 to 1 about (1577, 380) (0.66 s, power2.inOut, done at 10.82) |
| 10 | A4-S3 | 4 | civil | 0.98 | 10.82 | the civil defense desk's lines turn Amber 2 (0.3 s) and stay; label `civil defense` fades in |
| 11 | A4-S3 | 8 | no | 2.48 | 12.32 | police desk: lines to Body light and back to Label grey (0.3 s, yoyo), label `city police` fades in |
| 12 | A4-S3 | 9 | other | 2.68 | 12.52 | microphone: the same stroke pulse, label `the radio station` |
| 13 | A4-S3 | 10 | office | 2.90 | 12.74 | house: the same stroke pulse, label `a family` |
| 14 | A4-S4 | 1 | about | 0.38 | 14.90 | the clock stamp slides in from the left (`x:-660` to 0, 0.6 s, power3.out) with `about`; hands at 7:25. On "7" (index 2, 15.08) the minute hand sweeps 150 to 180 and the hour hand 222.5 to 225.0 (0.5 s, power3.out) and `7:30 PM` lands |
| 15 | A4-S4 | 10 | radioed | 3.76 | 18.28 | the radio arc draws from the civil defense desk to the police desk, dot by dot (0.6 s) |
| 16 | A4-S4 | 13 | police | 4.52 | 19.04 | the light leaves the civil defense desk and crosses the arc (0.8 s, ease none) |
| 17 | A4-S4 | 16 | location | 5.30 | 19.82 | when the light arrives (19.84) it hides and the police desk's lines turn Amber 2 (0.3 s) and stay |
| 18 | A4-S4 | 25 | radio | 7.80 | 22.32 | the microphone's lines go to Body light and back to Label grey (0.3 s, yoyo). No amber: he asked, nothing was sent |
| 19 | A4-S5 | 3 | path | 1.04 | 24.61 | the ghost dot appears at (837, 520) on the police desk's right edge with one Label grey ring (radius 8 to 30, 0.45 s) |
| 20 | A4-S5 | 8 | defense | 3.00 | 26.57 | the arc's dots go to Headline white and back to Amber 2 in a wave from left to right (0.6 s in all) |
| 21 | A4-S5 | 12 | the | 4.66 | 28.23 | the ghost runs x 837 to 1068 (0.8 s, ease none), its grey line growing behind it; on arrival ("station,", index 16, 29.03) the microphone's lines pulse to Body light and back |
| 22 | A4-S5 | 19 | station | 6.62 | 30.19 | the ghost jumps to x 1170 and runs to x 1400 (0.64 s, ease none); on arrival ("everyone.", index 21, 30.83) the house's lines pulse to Body light and back, windows dark. Hold to 32.43: two amber desks, the amber arc, the grey ghost line |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a4s02-countyb.html` is the only file the builder writes; `data-composition-id="g-a4s02-countyb"`, `data-duration="32.43"`; id prefix `cntb-`; root `<div id="cntb-root" ...>` styled through `#cntb-root` (plan rule 3 overrides the template's `id="root"`). Full frame, opaque, own ground on from frame 0 for the whole 32.43 s. The host is already mounted in `index.html` as `host-a4s02-countyb`; do not edit `index.html`.
**It is a family base.** Keep the county chain (four stations, two dotted links), the radio arc with its light, and the ghost as plain, separately named blocks. Later comps that copy it: `compositions/g-a4s06-died.html` and `compositions/g-a4s09-clock.html` (wave 3; they start from this comp's last frame: both desks amber, the ghost drawn), `compositions/g-a2s11-backup.html` (wave 2, its brief names this file for the county chain and dotted paths). The stamp with `about` in the eyebrow slot is the pattern for `compositions/g-a4s01-eyes.html` and `g-a4s09-clock.html`. It is sent alone for a full-size read before anyone copies it.
**What it copies:** link, light and ring code of the built `compositions/g-i1s9-chain.html`; the stamp of `compositions/g-t1s2-warning.html`; the chip of `compositions/g-i1s6-page.html`.
**Assets (paths from the episode folder; all confirmed on disk 12 Oct 26):**
- `media/drawings/desk.svg` (object 300 x 150, telephone to y -22, viewBox -6 -28 312 184, file 312 x 184, line 4, telephone 3), inlined twice.
- `media/drawings/microphone.svg` (object 120 x 230, viewBox -6 -6 132 242, file 132 x 242, line 4).
- `media/drawings/house.svg` (object 260 x 250, viewBox -6 -42 272 298, file 272 x 298, line 4).
- `media/drawings/tornado-mark.svg` (object 60 x 80, viewBox -6 -6 72 92, file 72 x 92, line 6).
- `media/drawings/wall-clock.svg` (object 124 x 124, viewBox -6 -6 136 136, file 136 x 136, line 4, ticks 3, hands 5; `dw-hour` and `dw-minute` turn about (62, 62)).
All inlined, ids under `cntb-`; mount rules in `media/drawings/README.md`, which wins over any number here. No map file, no page crop and no film cut is mounted: the film after the book ad sits under `g-a4s01-eyes`, the composition before this one (lead ruling, 12 Oct 26).

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a4s02-countyb`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`.

## 7a. Done line
All seven lines of template section 7a. Line 2 here: state the measured fill for 10.9 to 14.9 (the chain alone, before the stamp) as well as for the whole comp. Line 4 here: the chain's scale and `svgOrigin`, the hand rotations and the light's proxy are set at timeline 0; capture 10.50 (mid growth) both ways. Line 6 here: the four station boxes (gap 230.7 px), the waiting chain's box, the arc's apex and the two hand angles are computed by a script and stated in the receipt.
## 8. Receipt
As template section 8.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): the small grey chain and the chip `County B`, no map. Then settled frames: 1.60 (river), 2.60 and 3.40 (one mark, then two, labels clear of the river), 5.40 (river back to blue), 6.90 (sheriff's mark amber), 9.20 (tornado mark west of the river, both marks amber), 10.50 (mid growth: no label on screen, map gone), 11.30 (chain full size, first desk amber, one label), 13.30 (four labels, three stations grey), 15.80 (stamp, `about` over `7:30 PM`, hands at 7:30; chip still `County B` alone), 19.00 (arc drawn), 19.45 (light on the arc), 20.40 (police desk amber), 23.00 (microphone grey again, lamp dark), 25.30 (ghost dot at the police desk), 29.40 (ghost line to the microphone, grey), 31.40 and 32.30 (ghost line to the house, no amber past the police desk).
