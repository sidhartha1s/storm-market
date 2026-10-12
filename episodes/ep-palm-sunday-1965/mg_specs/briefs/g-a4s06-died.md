Host: id=g-a4s06-died file=compositions/g-a4s06-died.html start=700.99 (timeline-map.md table 1, 12 Oct 26; the mount in index.html wins) duration=5.16 s (last sound at 4.17) track=2

# g-a4s06-died · A4-S6 · "The information died with the police." (wave 3, page over the County B chain)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 2, 6, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21, and section 3c row PC-10. Times: `mg_specs/timeline-map.md` tables 1 and 5. Base: `mg_specs/briefs/g-a4s02-countyb.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS (`opacity` or `visibility`) and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id and is never `id="root"` (rule 3). No page crop holds past about 8 s without a visible change (rule 7): this crop is on screen 4.67 s and changes twice. The study's hidden county is labelled `County B` only; `County A` never appears here and no real county or town is named (rule 8). A flash is a stroke or fill change, never a scale pop (rule 12).
**Spoken (A4-S6, tempo 0.85; the wav on disk is already at that tempo):** "It didn't happen. "The information died with the police.""
**One look:** the chain as the last graphic left it, two amber desks and a grey ghost running on to the house; the ghost goes; the study's page comes in over it and one sentence is underlined in red as it is said; a red stop mark lands on the police desk.

## 0. What this graphic claims
In County B the message went from civil defense to the city police and no further. The study's own sentence says so: "The information died with the police." Nothing reached the radio station or a home by this path.

## 1. Source
- `edit_script.md` A4-S6, Rows [C5; study printed p. 22] (County B; the study's own sentence, voiced once).
- Page crop `media/docs/study-p22-died-crop.png` (PC-10, 1460 x 225, study printed p. 22, the page's first three lines). Read on the file and on the scan's text: line 1 ends `...aware of the tornado's`; line 2 is `progress. But the police apparently did not notify the local radio station nor`; line 3 is `any other organization within the county. The information died with the police.` The crop names no county.
- The chain, the arc, the ghost and the chip: `mg_specs/briefs/g-a4s02-countyb.md` section 3 and the built `compositions/g-a4s02-countyb.html` (its last frame is this comp's first frame). The stop mark: the built `compositions/g-i1s9-chain.html` (`#chn-stop`, a Popfig red bar 6 x 72 at the desk's edge).

## 2. Datum, scale, orientation
The chain is County B's, at full size, exactly where the base places it: line y 520, message left to right, civil defense desk, police desk, microphone, house. SCHEMATIC, NOT TO SCALE.
Line boxes on the crop, measured by a row and column scan on the file (12 Oct 26):
| Line | Crop px (x0 to x1, y0 to y1) |
|---|---|
| 1 | 81 to 1342, 23 to 55 |
| 2 | 80 to 1379, 99 to 130 |
| 3, whole | 81 to 1415, 174 to 206 |
| 3, the sentence `The information died with the police.` | 804 to 1415, 174 to 206 (the sentence gap before `The` is x 765 to 804) |
Line pitch is 75 px, so the typed line is large enough to read without a quote strip.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient with the base's faint sweep band, on from frame 0 |
| Chain | the base's `cntb-chain` block, copied without change: civil defense desk box x 96 to 351 (no telephone), police desk box x 582 to 837 (telephone at x 670 to 750), microphone box x 1068 to 1170, house box x 1400 to 1577; dotted links y 520, x 837 to 1068 and x 1170 to 1400; labels top 676: `civil defense`, `city police`, `the radio station`, `a family` |
| First-frame state | as the base's last frame: both desks' lines Amber 2; the radio arc `M224 508 Q425 300 626 508` Amber 2, dotted; the ghost's Label grey 6 px line over both dotted links (x 837 to 1068 and x 1170 to 1400) and its dot at (1400, 520); microphone, house and links Label grey |
| County chip | the base's chip, unmoved: left 836, top 316, height 46: `County B · where the tornado was` (both spans on from frame 0) |
| Clock stamp | the base's stamp (`about` / `7:30 PM`, hands 225.0 and 180 degrees) at left 96, top 96, 590 x 200, on in the first frame only; it leaves as the card arrives |
| Document card | left 96, top 54, 1480 x 245 (right 1576, bottom 299); Beige polaroid border 10 px, `box-shadow: 0 18px 50px rgba(0,0,0,0.55)`; the crop 1460 x 225 inside at (106, 64). It clears the chip (top 316) by 17 px and the arc's apex (y 404) by 105 px |
| Unlit page | Panel dark at 45 % over the whole crop from the card's first frame; on step 4 it lifts from the sentence box only: screen x 898 to 1529, y 232 to 276 |
| Underline | Popfig red `#d0121f`, 6 px, under the sentence only: screen x 910 to 1521, y 274 to 280 (4 px under the line box, whose screen y is 238 to 270) |
| Stop mark | Popfig red rect, x 840, y 484, 6 x 72 (3 px right of the police desk's right edge, across the chain line), as `#chn-stop` of the built intro chain |
| Source line | design sheet section 10: left 96, bottom 60: `Disaster Research Center, 1966, p. 22` |

## 4. Must be true in the picture
1. The underlined words are the page's own `The information died with the police.` and no others. Nothing on the card is retyped. The rest of line 3 (`any other organization within the county.`) is not underlined.
2. The stop mark is on the police desk's outgoing edge, between the police desk and the microphone. It is the only red thing in the chain. Nothing right of it is amber in any frame: microphone lamp and lines, house lines and windows, both dotted links.
3. The light stays: both desks and the arc are Amber 2 from the first frame to the last. The message did reach the police.
4. The ghost is Label grey and is gone (opacity 0) before the card has stopped moving. It never turns red or amber.
5. `County B` is the only county label, on the chip; the crop names no county; `County A` and every real place name are absent.
6. The chain's stations, links and labels sit within 2 px of the base's numbers. The card covers no station, label, arc or chip.
7. Nothing of ours in x >= 1600, y >= 680; text at least 96 px from the sides and 54 px from top and bottom. The crop holds 4.67 s (0.49 to 5.16) with changes at 1.93 and 3.51.

## 5. Text (exact) and cues
Text: `County B` · ` · where the tornado was` · `civil defense` · `city police` · `the radio station` · `a family` · `about` · `7:30 PM` (first frame only) · `Disaster Research Center, 1966, p. 22`. Page words are the image.
Cue words and times are from `audio/a4-s6.words.json` (9 words), read on 12 Oct 26. t from comp start = the segment's "wav start inside the composition" in `mg_specs/timeline-map.md` table 5 (A4-S6 -0.27) plus the word's time; the first word uses the table's "first sound" (0.00). Retime from the word, never from the seconds.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A4-S6 | 0 | It | 0.27 | 0.00 | first frame: the base's last frame (chain, two amber desks, amber arc, grey ghost line and dot, chip, stamp). No card, no stop mark |
| 1 | A4-S6 | 1 | didn't | 0.40 | 0.13 | the ghost's line and dot fade out (0.35 s); the microphone's and the house's lines stay Label grey |
| 2 | A4-S6 | 2 | happen. | 0.76 | 0.49 | the stamp slides out left with its fade (`x:-700`, 0.4 s, power3.in) while the card slides in from the right (`x:660` set at 0, to 0; 0.5 s, power3.out), wholly unlit; the source line fades in |
| 3 | A4-S6 | 3 | The | 2.20 | 1.93 | the unlit page lifts from the sentence box (0.3 s) and the underline starts: one `scaleX` 0 to 1, `transformOrigin:"left center"`, ease none, 1.93 to 3.95, so it runs with the voice |
| 4 | A4-S6 | 5 | died | 2.84 | 2.57 | the underline is passing `died` (its leading edge at screen x 1103.6, by script); nothing new starts: read this frame for pace |
| 5 | A4-S6 | 8 | police. | 3.78 | 3.51 | the stop mark comes on (fade 0.15 s) and the police desk's label `city police` turns Headline white (0.2 s). Hold to 5.16 |

## 6. Contract
As `references/mg-brief-template.md` section 6, with these: `compositions/g-a4s06-died.html` is the only file the builder writes; `data-composition-id="g-a4s06-died"`, `data-duration="5.16"`; id prefix `died-`; root `<div id="died-root" ...>` styled through `#died-root` (plan rule 3 overrides the template's `id="root"`). Full frame, own ground on from frame 0. Do not edit `index.html`.
**Family base it copies:** `compositions/g-a4s02-countyb.html` (wave 1), after it has passed its read: the `cntb-chain` block, the arc, the ghost, the chip and the stamp, re-prefixed `died-`, set to that comp's last-frame state at timeline 0. Page card, unlit page and underline from the built `compositions/g-i1s6-page.html`. Stop mark from the built `compositions/g-i1s9-chain.html`. `compositions/g-a4s09-clock.html` (wave 3) starts from this comp's last frame: chain, arc and stop mark.
**Assets (paths from the episode folder, read on disk 12 Oct 26):**
- `media/docs/study-p22-died-crop.png` (PC-10, 1460 x 225).
- `media/drawings/desk.svg` (object 300 x 150, viewBox -6 -28 312 184, line 4, telephone 3), inlined twice.
- `media/drawings/microphone.svg` (object 120 x 230, viewBox -6 -6 132 242, line 4).
- `media/drawings/house.svg` (object 260 x 250, viewBox -6 -42 272 298, line 4).
- `media/drawings/wall-clock.svg` (object 124 x 124, viewBox -6 -6 136 136), the stamp's face in the first half second.
Mount rules: `media/drawings/README.md`, which wins over any number here.

## 7. Tools
As template section 7, from the worktree root: `node scripts/freeze_scan.mjs episodes/ep-palm-sunday-1965 --comp g-a4s06-died`, then `node scripts/graphics_qc.mjs episodes/ep-palm-sunday-1965`, then `python3 scripts/run_gates.py episodes/ep-palm-sunday-1965`. `graphics_qc` may flag two type sizes on the page card (the scan's type beside ours): the family's accepted flag (plan rule 10).

## 7a. Done line
All seven lines of template section 7a. Line 3 here: frame 0 is the base's last frame, compared side by side with a frame of `g-a4s02-countyb` at 32.30. Line 4 here: the card's `x`, the underline's `scaleX` and the stamp's `x` are set at timeline 0; capture 2.60 both ways. Line 6 here: the underline and unlit-box screen numbers are the section 2 crop boxes plus (106, 64), computed by a script and stated in the receipt.

## 8. Receipt
As template section 8, plus the measured screen x of the underline's leading edge at 2.57.

## Frames the verifier reads
First frame (0.00) and the frame after it (0.04): the base's last frame, stamp on, no card. Then: 0.40 (ghost almost gone), 1.10 (card in and unlit, stamp gone, source line on, chip and arc clear of the card), 2.60 (sentence lit, underline part way, under no other words), 4.00 (underline complete, stop mark on, label white, nothing amber right of the mark), 5.10 (last frame).
