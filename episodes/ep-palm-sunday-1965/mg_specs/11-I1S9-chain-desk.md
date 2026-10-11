Host: id=g-i1s9-chain file=compositions/g-i1s9-chain.html start=99.97 duration=9.32 track=2

# 11 · I1-S9 · the whole chain, and the desk where the light stops (comp `g-i1s9-chain`)

Brief on `references/mg-brief-template.md`. Shared look: `00-design-sheet.md` sections 6 (intro version), 7. This is the claim of the episode in one frame.
**Spoken (I1-S9):** "On Palm Sunday nineteen sixty five the forecast did not fail and the warnings were sent. They stopped one desk short of the people."
**One look:** five things in a row, left to right. Light runs through the first three and stops. At the place it stops, a desk with a telephone still on its hook. The microphone and the house stay dark.

## 0. What this graphic claims
The forecast went out and the warnings were sent as far as the list. They did not reach the announcer or the family: they stopped one desk short of the people.

## 1. Source
`edit_script.md` I1-S9, Rows [claim, angle.md]: the locked claim, copied word for word. The chain's five stations are the Picture note's: Kansas City, South Bend, the eight-row list, the microphone, the house. No photograph: a diagram. Needs no file from `media/stills/`.

## 2. Datum, scale, orientation
SCHEMATIC, NOT TO SCALE: a diagram of who told whom, left to right in the order the message travelled. It is not a map and distances mean nothing. Datum: the link line at y 520. The stop point is x 840, the left edge of the desk zone.

## 3. Geometry (screen px)
Stations, desk and links: the design sheet section 6 intro table, as written. Plus:
| Element | Px |
|---|---|
| Ground | canvas gradient |
| Eyebrow | left 96, top 96: `PALM SUNDAY · APRIL 11, 1965` Arial 700 22 px, Label grey, tracking 6 |
| Row A | left 96, top 142: `The forecast did not fail` Arial 700 30 px, Body light; a pen tick 26 px wide at x 96 to 122, text from x 136 |
| Row B | left 96, top 192: `The warnings were sent`, same style |
| Light | Amber 2 line 6 px drawn over a link with `scaleX` from its left end, with a leading dot radius 8; a lit station's lines turn Headline white and its paper or lamp parts Amber 2 |
| Stop mark | Popfig red bar 6 px wide, x 837 to 843, y 484 to 556 |
| Headline | left 96, top 780: `They stopped one desk short of the people.` Arial Black 900 52 px, Headline white; the words `one desk short` in Popfig red |
The headline is about 1,200 px wide at 52 px: checked on a frame to end before x 1560. Every label and the headline are fixed; nothing here rides a camera, because there is no camera move.

## 4. Must be true in the picture
1. Five stations, left to right: Kansas City forecasters, Weather Bureau · South Bend, the list, an announcer, a family.
2. The light passes stations 1, 2 and 3 and never passes x 840. No amber is on the desk, the microphone or the house in any frame.
3. The desk is drawn at the stop point, between the list and the microphone, on the word "desk" and not before. Its telephone handset is **on the hook**. Station 2's handset is off the hook.
4. The two links right of the desk stay dotted and grey to the last frame.
5. The miniature list has eight bars and a ninth empty row, no readable name, no numbering and no tick box: no organization is singled out here (S1, S2).
6. Rows A and B and the headline are the locked claim's words, unchanged.
7. The ticks on rows A and B are Body light pen ticks, never red. Popfig red is on the stop mark and on `one desk short` only.
8. No person at the desk, at the microphone or in the house (S5).
9. Design sheet S4, S6, S7: the microphone carries no station name.

## 5. Text (exact) and cues
Text: `PALM SUNDAY · APRIL 11, 1965` · `The forecast did not fail` · `The warnings were sent` · `They stopped one desk short of the people.` · the five station labels (design sheet section 6).
| Step | cue | t= | What |
|---|---|---|---|
| 0 | first frame (word "On") | 0.00 | all five stations and the links drawn dark (Label grey at 55 %), labels on; the 800 to 1170 stretch is one dotted line; no desk |
| 1 | cue: "Palm" | 0.14 | eyebrow in |
| 2 | cue: "forecast" | 2.50 | station 1 lights; light runs link 236 to 316 (0.5 s) |
| 3 | cue: "fail" | 3.36 | row A and its tick |
| 4 | cue: "warnings" | 4.36 | station 2 lights; light runs link 460 to 540 (0.5 s) |
| 5 | cue: "sent" | 4.90 | station 3 lights (its paper to full Beige polaroid); row B and its tick; light runs 800 to 840 |
| 6 | cue: "stopped" | 5.98 | the dot reaches x 840 and dies in one ring pulse (radius 8 to 40); stop mark draws top to bottom (0.25 s) |
| 7 | cue: "desk" | 6.68 | desk and telephone draw on (0.6 s), lines Body light, no amber; headline rises (`y:30 to 0`, 0.4) |
| 8 | cue: "people" (last word) | 7.56 | microphone and house pulse once to Body light at 80 % and back to dark; hold 1.5 s. The lit stations' amber parts breathe (finite repeats) to carry the hold |
| 9 | exit | 9.32 | hard cut to 12 |

## 6 to 8. Contract, tools, done line, receipt
As `references/mg-brief-template.md` sections 6, 7, 7a, 8, unchanged. File `compositions/g-i1s9-chain.html`, id prefix `chn-`, root id `chn-root`. Done line 2: state the measured fill; the chain band, the claim rows above it and the headline below it are placed so no empty block passes a third of the frame.
**Closest library exemplar:** official catalog block `flowchart` (nodes joined by SVG connectors that draw in order) for the links and the travelling light; El Reno `compositions/g-a4s8-timeline.html` (a line that runs and stops at a marked point). In-house: `library/inhouse/stat-timeline.html` (a progress rail that stalls).
