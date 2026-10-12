Host: id=g-a5s21-end file=compositions/g-a5s21-end.html start=1004.76 (timeline-map.md table 1; the mount in index.html wins) duration=2.62 s track=2

# g-a5s21-end · A5-S21 · "Did anyone fix the end of the list?" (wave 4, list family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 5, 6, 7, 10 and 12. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5. Base: the built `compositions/g-t1s3-list.html` (its last state) and `mg_specs/briefs/g-a1s18-list.md`.
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id, never `root` (rule 3). The teletype room photograph is not used here: the ground is the canvas gradient (rule 9). A flash is a stroke or fill change, never a scale pop (rule 12).
**Spoken (A5-S21):** "Did anyone fix the end of the list?"
**One look:** the list, the dark microphone, the dark house; the eye is taken to the microphone.

## 0. What this graphic claims
Nothing new: it asks the act's exit question. The list's last link, from the offices to the announcer, is the one still open.

## 1. Source
- `edit_script.md` A5-S21 (the act's exit question; no row). The list and the chain are the hook tail's: design sheet sections 5 and 6, source `Disaster Research Center, 1966, p. 14`.
- The comp is followed by 0.7 s of black (timeline-map.md table 4).

## 2. Datum, scale, orientation
World px and the "Everything" camera state of design sheet section 5: s 1.0, tx 0, ty 110, so screen = world + (0, 110). The sheet is screen x 64 to 824, y 170 to 760; the microphone box is screen x 1030 to 1150, y 510 to 740; the house box is screen x 1300 to 1560, y 490 to 740 (aerial to y 456).
The push is 1.00 to 1.06 about the microphone, screen point (1090, 625), `ease:"none"`, over the whole 2.62 s. At 1.06 the house's right edge is screen x 1588, left of the presenter corner.

## 3. Geometry (screen px, before the push)
| Element | Px |
|---|---|
| Ground | canvas gradient, on from frame 0 |
| List sheet | design sheet section 5, Everything state: sheet x 64 to 824, y 170 to 760; eyebrow, title `Organizations notified included:`, the eight rows plain (Caption dark, no tick, no band, no mark), the blank ninth row with its cursor block blinking on finite repeats |
| Dotted line | y 708 (the blank row's centre), x 824 to 1030 and x 1150 to 1300; 4 px dots, 14 px gap, Label grey |
| Microphone | `media/drawings/microphone.svg` inline, box x 1030 to 1150, y 510 to 740, dark: lines Label grey at 55 % (`#55606b`), lamp Panel dark |
| Label | `an announcer`, centred x 1090, top 774, Arial 700 26 px, Body light |
| House | `media/drawings/house.svg` inline, box x 1300 to 1560, y 490 to 740, dark |
| Label | `a family`, centred x 1430, top 774, Arial 700 26 px, Body light |
| Source line | fixed HUD (it does not ride the push), left 96, bottom 60: `Disaster Research Center, 1966, p. 14` |
World, sheet and chain sit in one container that takes the push; the source line sits outside it.

## 4. Must be true in the picture
1. The microphone and the house are dark on every frame: no amber, no red, no lit window, no lit lamp.
2. The list has eight plain rows and a blank ninth row. No numbering, no tick, no tick box, no row count; nothing is typed in the blank row.
3. The dots brighten toward the microphone in Body light, never Amber 2: no light has travelled.
4. The microphone has no name and sits off the paper.
5. Nothing in x >= 1600 and y >= 680 at any moment of the push (house right edge 1588 at the end).
6. The last frame is a clean hold: black follows it.

## 5. Text (exact) and cues
Text: the list sheet's eyebrow, title and eight rows exactly as design sheet section 5 · `an announcer` · `a family` · `Disaster Research Center, 1966, p. 14`.
t from comp start = the segment's wav start inside the composition (timeline-map.md table 5: -0.43) plus the word's time; the first word uses table 5's first sound.
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A5-S21 | 0 | Did | 0.00 | 0.00 | first frame: everything in section 3 on; the push starts |
| 1 | A5-S21 | 4 | end | 1.34 | 0.91 | the dots between the sheet and the microphone turn Body light one after another, sheet end first (12 dots at the 18 px pitch, 0.03 s apart, 0.36 s in all) |
| 2 | A5-S21 | 7 | list? | 1.68 | 1.25 | the microphone's lines step from 55 % Label grey to full Label grey (a stroke change, 0.3 s); the lamp stays Panel dark |
| 3 | end | | | | 2.62 | comp ends on the hold; black follows |
The dot count is checked against the window: 15 dots at 0.03 s is 0.45 s, inside the 0.34 s to the next cue plus its 0.3 s move.

## 6. Contract
As `references/mg-brief-template.md` section 6, with plan rule 3 over its `id="root"`. File the builder may write: `compositions/g-a5s21-end.html` only. Id prefix `end-`, root id `end-root`. Base it copies: the sheet, the chain and the labels of the built `compositions/g-t1s3-list.html` at its Everything state. Assets mounted: `media/drawings/microphone.svg`, `media/drawings/house.svg`, both inline. `g-a6s03-announcer` opens on this same frame with the microphone lit: keep every box here unchanged.

## 7. Tools
As the template's section 7.

## 7a. Done line
As the template's section 7a, all seven. `graphics_qc` flat type: the typed sheet is one of the plan's rule 10 cases. Done line 6: the push's end scale (1.06) and its origin (1090, 625) are the shared numbers with `g-a6s03-announcer`.

## 8. Receipt
As the template's section 8, plus: the house's right edge on the last frame, measured.

## Frames the verifier reads
First frame 0.00 and the frame after it (0.04); 1.20 (dots lit); 1.70 (microphone stepped up); last frame 2.55 (corner empty, hold clean).
