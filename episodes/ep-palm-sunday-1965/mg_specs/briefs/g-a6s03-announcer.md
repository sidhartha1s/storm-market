Host: id=g-a6s03-announcer file=compositions/g-a6s03-announcer.html start=1026.15 (timeline-map.md table 1; the mount in index.html wins) duration=17.47 s track=2

# g-a6s03-announcer · A6-S3, A6-S4 · the first recommendation, and the lamp that was not there (wave 5, list family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 5, 6, 7, 10 and 12. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5. Bases: `mg_specs/briefs/g-a5s21-end.md` (this comp opens on that comp's frame) and the built `compositions/g-t1s3-list.html`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id, never `root` (rule 3). The study's hidden counties are "County A" and "County B" only (rule 8): this comp carries neither chip. The teletype room photograph is not used (rule 9). A flash is a stroke or fill change, never a scale pop (rule 12). No map may show Alto (rule 20).
**Spoken (A6-S3):** "A family got it from an announcer, if the announcer had it. The team's first recommendation was to make sure the announcer had it."
**Spoken (A6-S4):** "When the researchers came, one station's warning light still hadn't been installed. And that was one desk, on an evening that broke in four more places."
**One look:** the list, the microphone lit this time, the house still dark; then the microphone alone, its lamp back to an empty outline, and four dark marks in a row.

## 0. What this graphic claims
The survey team's first recommendation was to make sure the announcer had the warning. When the researchers came, one station's alerting device had not yet been installed. That is a recommendation and one station, not a thing done everywhere.

## 1. Source
- `edit_script.md` A6-S3, Rows [C12; G, Rec. 1] (the first sentence is T1-S4, word for word; a recommendation, not a thing done). A6-S4, Rows [study printed p. 31: "such a mechanism had not yet been installed at the time of the DRC study"]; the four places are the writer's count, so no figure 4 is printed.
- The list and the chain are the hook tail's: design sheet sections 5 and 6, source `Disaster Research Center, 1966, p. 14`.

## 2. Datum, scale, orientation
Part 1 is the frame of `g-a5s21-end.md` before its push: design sheet section 5 "Everything" state, screen = world + (0, 110). Sheet x 64 to 824, y 170 to 760; microphone box x 1030 to 1150, y 510 to 740; house box x 1300 to 1560, y 490 to 740.
Part 2 is a new layout on the same ground. The microphone is drawn again at scale 2.0 (object box 240 x 460) at x 200 to 440, y 220 to 680; its lamp (the circle of radius 9 at object (104, 20)) is a circle of radius 18 centred at screen (408, 260).
The four marks stand in four slots 250 px apart, centres x 700, 950, 1200, 1450 on the line y 520, each no wider than 180 px; the last slot ends at x 1540, left of the presenter corner and above y 680.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0 |
| Part 1: sheet, dotted line, microphone, house, labels | exactly `g-a5s21-end.md` section 3: sheet in the Everything state with eight plain rows and the blank ninth row with its cursor; dotted line y 708; microphone box x 1030 to 1150, y 510 to 740; house box x 1300 to 1560, y 490 to 740; labels `an announcer` and `a family`, top 774. At frame 0 the microphone and house are dark |
| Microphone lit | lines Headline white; lamp (`dw-lamp`) fill Amber 2. The house never changes in this comp |
| Chip 1 | glass chip, left 930, top 420, height 46, padding 0 x 22, Arial 700 26 px, Body light: `the survey team's first recommendation` (above the microphone, clear of the sheet's right edge at x 824) |
| Source line | fixed HUD, left 96, bottom 60: `Disaster Research Center, 1966, p. 14` in part 1; in part 2 a second pre-authored element in the same place: `Disaster Research Center, 1966, p. 31` |
| Part 2: big microphone | `media/drawings/microphone.svg` inline, `translate(200 220) scale(2)`, `stroke-width="3"` on the group (6 px lines); lines Headline white, lamp Amber 2 at its entrance |
| Lamp, empty | the same circle with fill Panel dark and stroke Label grey: an outline with nothing in it |
| Chip 2 | glass chip, left 480, top 236, same type as chip 1: `when the researchers came` |
| Mark 1 | slot centre x 700: `media/drawings/desk.svg` inline at scale 0.6 (180 x 90, box x 610 to 790, y 486 to 576), dark (`#55606b`), with the stop mark of the built `compositions/g-i1s9-chain.html` (`#chn-stop`) at 0.6 scale: a Popfig red bar 4 x 44 at x 793, y 498 |
| Mark 2 | slot centre x 950: a dotted line y 520, x 870 to 1030 (`stroke-dasharray="0.1 14"`, 4 px, `#55606b`) with `media/drawings/telephone.svg` inline at scale 0.8 on its middle (box x 909 to 991), dark |
| Mark 3 | slot centre x 1200: a dot of radius 10 at (1200, 520), fill Panel dark, stroke `#55606b` 4 px (an unlit map dot) |
| Mark 4 | slot centre x 1450: `media/drawings/telephone.svg` inline at scale 1.0 (box x 1399 to 1501), dark |
| Mark labels | Arial 700 22 px, Label grey, centred on each slot, top 620: `a police desk` · `the telephone lines` · `Fort Wayne` · `Marion` |

## 4. Must be true in the picture
1. Part 1: the microphone lights; the house stays dark on every frame of the comp. No light travels from the microphone to the house.
2. The list has eight plain rows and a blank ninth row; no numbering, no tick, no tick box; nothing typed in the blank row.
3. Part 2: the lamp ends as an empty outline and stays that way to the last frame. The chip says when, not where: no station, town or county is named for it.
4. The four marks are dark. The only red in the comp is the stop mark on mark 1. No figure 4 is printed and the marks carry no numbers.
5. `Fort Wayne` and `Marion` name places the script named for those marks (A5 and A5-S11); no county chip appears.
6. Nothing in x >= 1600 and y >= 680. Nothing appears before its spoken word.
7. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). Part 1 (steps 0 to 4) is the hook tail's frame and needs no staging. Part 2 is staged: from step 5 (7.83) the microphone, its lamp and chip 2 sit centred, the microphone at scale 3.0 (1.5 times its briefed 2.0: 360 x 690 at x 780 to 1140, y 195 to 885; lamp radius 27 centred (1092, 255)), chip 2 at left 1180, top 216, on a slow push (1.00 to 1.03). The lamp empties at step 6 in that place. At step 6b (word 12 "And", 12.75) the group moves to its briefed place and size over 0.5 s, so the four slots are clear before mark 1 lands on "broke" (14.93). Unstaged, the block x 900 to 1920 (53.1 % of the frame) would be empty for 7.10 s.

## 5. Text (exact) and cues
Text: the sheet's text as design sheet section 5 · `an announcer` · `a family` · `the survey team's first recommendation` · `when the researchers came` · `a police desk` · `the telephone lines` · `Fort Wayne` · `Marion` · the two source lines.
t from comp start = the segment's wav start inside the composition (timeline-map.md table 5: A6-S3 -0.41, A6-S4 7.45) plus the word's time; a segment's first word uses table 5's first sound.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A6-S3 | 0 | A | 0.00 | 0.00 | first frame: part 1, everything dark, source line on |
| 1 | A6-S3 | 6 | announcer | 1.42 | 1.01 | the microphone lights: lines to Headline white, lamp to Amber 2 (0.3 s) |
| 2 | A6-S3 | 7 | if | 1.84 | 1.43 | the lamp drops to Panel dark and returns to Amber 2 once (0.15 s each way) |
| 3 | A6-S3 | 15 | recommendation | 4.88 | 4.47 | chip 1 lands (`y:16` to 0 with the fade, 0.3 s) |
| 4 | A6-S3 | 21 | announcer | 6.52 | 6.11 | the dots between the sheet and the microphone turn Body light one after another, sheet end first (12 dots, 0.03 s apart) |
| 5 | A6-S4 | 0 | When | 0.00 | 7.83 | sheet, house, dotted line, labels and chip 1 fade out (0.3 s); the big microphone and its lit lamp fade in (0.3 s); chip 2 lands; the source line swaps |
| 6 | A6-S4 | 9 | hadn't | 3.50 | 10.95 | the lamp's fill goes to Panel dark and its stroke to Label grey (0.4 s): an empty outline |
| 6b | A6-S4 | 12 | And | 5.30 | 12.75 | the microphone, its empty lamp and chip 2 move from the centred, staged place to their briefed place and size (0.5 s, power2.inOut; done at 13.25) |
| 7 | A6-S4 | 21 | broke | 7.48 | 14.93 | mark 1 fades in with its label (0.25 s) |
| 8 | A6-S4 | 22 | in | 7.66 | 15.11 | reference only: marks 2, 3 and 4 follow mark 1 at 0.30 s steps (15.23, 15.53, 15.83) |
| 9 | A6-S4 | 25 | places. | 8.38 | 15.83 | mark 4 lands on this word |
| 10 | end | | | | 17.47 | comp ends on the hold |
Count against the window: four marks at 0.30 s steps take 0.90 s, the time from "broke" (14.93) to "places." (15.83).

## 6. Contract
As `references/mg-brief-template.md` section 6, with plan rule 3 over its `id="root"`. File the builder may write: `compositions/g-a6s03-announcer.html` only. Id prefix `ann-`, root id `ann-root`. Bases it copies: the sheet and chain of the built `compositions/g-t1s3-list.html` at its Everything state (as `compositions/g-a5s21-end.html`), and `#chn-stop` of the built `compositions/g-i1s9-chain.html`. Assets mounted, all inline: `media/drawings/microphone.svg`, `media/drawings/house.svg`, `media/drawings/desk.svg`, `media/drawings/telephone.svg`. No later composition copies this one.

## 7. Tools
As the template's section 7.

## 7a. Done line
As the template's section 7a, all seven. `graphics_qc` flat type: the typed sheet is one of the plan's rule 10 cases. Done line 6: the four slot centres and the big microphone's lamp centre are computed by a script from section 2 and stated in the receipt.

## 8. Receipt
As the template's section 8, plus: the measured right edge of chip 1 and of the `Marion` label.

## Frames the verifier reads
First frame 0.00 and the frame after it (0.04); 1.35 (microphone lit, house dark); 4.90 (chip 1); 6.60 (dots); 8.30 (part 2 settled, lamp lit); 11.50 (lamp empty); 15.00 (mark 1 only); 16.20 (four marks); last frame 17.40.
