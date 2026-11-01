Host: id=g-a6s08-spotters file=compositions/g-a6s08-spotters.html start=1073.00 (timeline-map.md table 1; the mount in index.html wins) duration=12.71 s track=2

# g-a6s08-spotters · A6-S8 · the empty stretch gets its spotters (wave 5, chain family)

Brief on `references/mg-brief-template.md`. Rules: `references/mg-quickref.md` (read it before building). Look: `mg_specs/00-design-sheet.md` sections 1, 6, 7, 9, 10. Plan: `mg_specs/acts-plan.md` section 1, rules 1 to 21. Times: `mg_specs/timeline-map.md` tables 1 and 5. Base: `mg_specs/briefs/g-a5s12-spotters.md` (this comp fills the five slots that comp left empty).
Rules this comp inherits, restated: start-hidden elements are hidden in CSS and their transforms are set in the timeline at 0; a move from rest is a plain `to()` (rule 1). The root is styled through its id, never `root` (rule 3). A flash is a stroke or fill change, never a scale pop (rule 12). A beat count is checked against its spoken window (rule 13). No person is drawn (design sheet section 7).
**Spoken (A6-S8):** "It asked for stronger storm reporting networks in local communities, because tornadoes could go unreported for minutes. The Weather Service says that push led, in time, to the spotter program called Skywarn."
**One look:** the long empty line between a town and the warning office from A5-S12; five marks are drawn along it and light; then one word on glass.

## 0. What this graphic claims
The survey team recommended stronger severe storm reporting networks in local communities. The National Weather Service says that push eventually resulted in the spotter program called SKYWARN. The first is a recommendation; the second is the Weather Service's own account, with no year.

## 1. Source
- `edit_script.md` A6-S8, Rows [G, Rec. 3; survey printed pp. 2 and 7: "can go unreported for a matter of several minutes"] and [G; LOT: "eventually resulted in the formation of SKYWARN"].
- Layout: `g-a5s12-spotters.md` sections 2 and 3 (the office desk, the long dotted link, the town telephone, the house, five slots).

## 2. Datum, scale, orientation
Everything stands where `g-a5s12-spotters` put it: office desk box x 96 to 351, y 490 to 618; long dotted link y 520, x 351 to 1166; town telephone x 1166 to 1274; short solid link x 1274 to 1400; house box x 1400 to 1577, y 430 to 600. The five slot centres are on y 520 at x 470, 610, 750, 890, 1030 (140 px apart).
The spotter mark is ours and is not a person: a ring of radius 14 (4 px stroke) with a centre dot of radius 4, and a 16 px mast rising from the ring's top with a 12 px crossbar 4 px under the mast's tip. Box 28 wide, 44 tall; the ring's centre sits on the slot centre, so the mast's tip is at y 490.
Count against the window: five marks, 0.33 s apart, take 1.32 s from the first to the last; the words run from "reporting" (1.21) to "communities" (2.51), 1.30 s.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient with the intro's faint sweep band, on from frame 0 |
| Office desk, long link, town telephone, short link, house | exactly `g-a5s12-spotters.md` section 3, lines Body light, on from frame 0 |
| Desk label | `the warning office`, Arial 700 22 px, Label grey, left 96, top 676 |
| House label | `a town`, Arial 700 22 px, Label grey, centred on x 1488, top 676. `Marion` is not used here: this segment names no town |
| Spotter marks 1 to 5 | section 2, at x 470, 610, 750, 890, 1030. Drawn in Body light, body of the ring Panel dark (it covers the dotted link behind it). Lit: ring and mast Headline white, centre dot Amber 2 |
| Paper strip | Beige polaroid, left 96, top 780, 1000 x 124 (right 1096, bottom 904), the chain strip's shadow. Type as built and ruled (lead, 12 Oct 26; this brief first said 44 px and 22 px): quote Georgia 52 px, attribution Arial 700 26 px. At 52 px the quote measures 987 px (script, the Georgia file), so the strip's width and the tops inside it are the built ones, with 48 px or more from the text's end to the strip's edge. Quote, Caption dark, left 136: `“severe storm warning reporting networks”`. Attribution, Caption dark sub, tracking 2, left 136: `Weather Bureau survey report, 1965, p. 2, recommendation 3` |
| Glass card | glass plate as the clock stamp's, left 660, top 220, 600 x 190 (right 1260, bottom 410), above the marks' masts (y 490) |
| Glass eyebrow | Arial 700 20 px, Label grey, letter-spacing 6 px, left 700, top 244: `THE SPOTTER PROGRAM` |
| Glass word | Arial Black 900 84 px, Headline white, `letter-spacing:0.06em`, left 700, top 282: `SKYWARN` |
| Source line | fixed HUD, left 96, bottom 60: `National Weather Service, Chicago`. It comes in as the paper strip leaves |

## 4. Must be true in the picture
1. Five marks, in the five slots `g-a5s12-spotters` left empty, between the town and the office. None is a figure or a face.
2. The marks light; nothing travels along the line. The long link stays dotted and Label grey: the comp does not show a report being made.
3. The paper card's words are the survey's recommendation; `SKYWARN` is on glass with the Weather Service as its source. No year is on screen.
4. No town is named: the house label is `a town`.
5. One source per frame: the strip's attribution, then the source line.
6. Nothing in x >= 1600 and y >= 680 (the house ends at x 1577, y 600). Nothing appears before its spoken word.
7. No empty block over a third of the frame for more than about 3 s at any step of the build-up (plan rule 22). **Not met as drawn, and reported to the lead.** The row is the full-width chain row of `g-a5s12-spotters` (x 96 to 1577), so it cannot be enlarged or centred further. The band above it (y 0 to 430, 39.8 % of the frame) is empty from frame 0 until the glass card at 9.87 s; the band below its labels is empty except while the strip is up (3.05 to 6.65 s). Until the lead rules a fix for the chain row (it applies to `g-a5s12-spotters` unchanged), the builder runs the sweep band and a slow push (1.00 to 1.03) on the row and reports the largest empty block in per cent and seconds.

## 5. Text (exact) and cues
Text: `the warning office` · `a town` · `“severe storm warning reporting networks”` · `Weather Bureau survey report, 1965, p. 2, recommendation 3` · `THE SPOTTER PROGRAM` · `SKYWARN` · `National Weather Service, Chicago`.
t from comp start = the segment's wav start inside the composition (timeline-map.md table 5: -0.29) plus the word's time; the first word uses table 5's first sound (0.01).
| Step | Segment | Word index | Word | t in segment (s) | t from comp start (s) | What happens |
|---|---|---|---|---|---|---|
| 0 | A6-S8 | 0 | It | 0.00 | 0.01 | first frame (0.00): the desk, the long empty link, the telephone, the house, both labels |
| 1 | A6-S8 | 5 | reporting | 1.50 | 1.21 | mark 1 draws on and lights (0.25 s); marks 2 to 5 follow 0.33 s apart (1.54, 1.87, 2.20, 2.53) |
| 2 | A6-S8 | 9 | communities | 2.80 | 2.51 | reference: mark 5 lands on this word |
| 3 | A6-S8 | 10 | because | 3.34 | 3.05 | the paper strip rises (`y:60` to 0 with the fade, 0.4 s) |
| 4 | A6-S8 | 14 | unreported | 4.90 | 4.61 | the five centre dots step to Panel dark and back to Amber 2, one after another, 0.1 s apart (a fill change) |
| 5 | A6-S8 | 17 | The | 6.94 | 6.65 | the paper strip leaves (`y:60` with the fade, 0.3 s); the source line fades in |
| 6 | A6-S8 | 22 | push | 8.22 | 7.93 | the five rings step to Amber 2 and back to Headline white, town end first, 0.1 s apart |
| 7 | A6-S8 | 26 | to | 10.16 | 9.87 | the glass card rises with its eyebrow (`y:40` to 0 with the fade, 0.35 s) |
| 8 | A6-S8 | 31 | SkyWarn. | 11.34 | 11.05 | `SKYWARN` fades in on the card (0.25 s) |
| 9 | end | | | | 12.71 | comp ends on the hold |

## 6. Contract
As `references/mg-brief-template.md` section 6, with plan rule 3 over its `id="root"`. File the builder may write: `compositions/g-a6s08-spotters.html` only. Id prefix `spo-`, root id `spo-root`. Base it copies: `compositions/g-a5s12-spotters.html` (wave 4) for every box and the dotted link; the glass plate values of `compositions/g-a1s01-kc.html` (wave 1). Assets mounted, all inline: `media/drawings/desk.svg`, `media/drawings/telephone.svg`, `media/drawings/house.svg`. The spotter mark has no file: it is the px lines of section 2. No later composition copies this one.

## 7. Tools
As the template's section 7.

## 7a. Done line
As the template's section 7a, all seven. Done line 6: the five slot centres are the numbers of `g-a5s12-spotters`, copied, and stated in the receipt.

## 8. Receipt
As the template's section 8, plus: the measured width of `SKYWARN` and of the strip's quote, and a close frame of one lit mark over the dotted link.

## Frames the verifier reads
First frame 0.00 and the frame after it (0.04); 1.40 (mark 1 only); 2.90 (five marks lit); 3.60 (strip); 4.90 (dots mid step); 7.10 (strip gone, source line on); 8.20 (rings mid step); 10.40 (glass card, eyebrow only); 11.50 (`SKYWARN`); last frame 12.60.
