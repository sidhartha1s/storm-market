# BRIEF · g-intro-hook · "they were indoors, and none below ground" · STANDARD (Sonnet 5.5, high)

Episode ep-joplin-2011, segment H1-S1, the cold open. Overlay comp, transparent root, over Paul's full-frame clip `ins-paul-1`
for its whole length (frame one of the video). Host from h1-s1 0.00 to the clip's cut on "ground." (word end 16.90).
Presenter circle: off (Paul is full frame). Exemplar: `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` (popfig + glass chip).
Open numbers: none drawn. Cue clock: `_list.md` Open 6 (if the Flow clip has its own audio, re-time every cue to it).

## 0. What this graphic claims
135 of the 155 people the tornado took by impact were inside a structure (T3), and NIST found no evidence any of them were
underground (H5). The viewer's own answer ("get inside") was right, and still was not enough.

## 1. SOURCE
- T3 "Of the 155 impact-related fatalities, 135 (87 percent) involved persons who are known to have been located inside structures during the tornado." NIST Finding 40.
- H5 "NIST found no evidence that any of those killed were located underground during the tornado." NIST Finding 46.
- Date and place: H3 "at the time of the May 22, 2011, Joplin tornado" (NIST Finding 20); "Joplin, Missouri": the NIST NCSTAR 3 title in facts.md "Sources" ("the May 22, 2011, Tornado in Joplin, Missouri").

## 2. DATUM, SCALE, ORIENTATION
- Overlay on live footage of a face: nothing crosses Paul's face. Before building, read one frame of `ins-paul-1` at 1.0, 7.0 and 16.4 s
  and state his face box in the receipt; every element below stays out of it, moving the chip block down or left if needed (report it).
- Zones: popfig top left; glance chip + source chip centre-left. One chip at a time.

## 3. GEOMETRY
- **Popfig** (top left): big line "May 22, 2011", 'AbrilFig' 150 px `#d0121f` with the popfig text-shadow from the exemplar, left x 110,
  top 90. Sub "Joplin, Missouri" Arial 700 40 `#f2f5f8` on the line below, left x 116, with the exemplar's shadow. No card behind it.
- **Glance chip** (glass chip, tokens.md surface, radius 28): left x 110, top 440, height 110, padding 0 40 px; text Arial Black 900 64
  `#f2f5f8`, one line.
- **Source chip** (glass chip): left x 110, top 572, height 52, padding 0 24 px; text Arial 700 22 `#c8d3e0` tracking 2, one line.
  Its right edge stays ≤ 1180.
- Entrances: chips `fromTo(x:-80, autoAlpha 0 → x 0, autoAlpha 1, 0.4, power3.out)`; popfig `fromTo(scale 0.82, autoAlpha 0 → 1, 0.35, back.out(1.6))`, transformOrigin left top.
- Exits: slide left `to(x:-700, autoAlpha 0, 0.4, power3.in)`. Holds: each visible chip floats y ±3 px over 2 s (something moves every second of the window).

## 4. MUST BE TRUE IN THE PICTURE
1. The popfig is fully on screen by 1.0 s (frame one of the video shows Paul, the popfig arriving).
2. Never two glance chips at once; the popfig is gone before "TORNADO SIREN" is fully in.
3. "135 INDOORS" never shows without its source chip under it after 7.20; "0 BELOW GROUND" never without its source chip.
4. No element covers Paul's eyes or mouth in any frame; nothing in the logo spot (centre 1740, 900, 96 px).
5. No like count, no comment card, no other picture.

## 5. PANEL TEXT (exact) and CUES (h1-s1)
| element | text | cue |
|---|---|---|
| popfig in | "May 22, 2011" / "Joplin, Missouri" | "Okay," 0.00 (in by 0.35) |
| popfig out | | "goes" 1.70 (out by 2.00) |
| glance chip 1 | "TORNADO SIREN" | "off." 1.94 |
| chip 1 out | | "You" 3.84 |
| glance chip 2 | "135 INDOORS" (T3) | "135" 6.90 |
| source chip 2 | "135 of 155 impact-related · inside a structure · NIST Finding 40" (T3) | "of" 7.38 |
| chip 2 + source chip out | | "and" 11.78 |
| glance chip 3 | "0 BELOW GROUND" (H5) | "below" 16.26 |
| source chip 3 | "NIST found no evidence any were underground · Finding 46" (H5) | "below" 16.26 + 0.15 |
| end | | the host ends on the clip's cut (16.90 + the editor's tail); chip 3 rides the cut, no exit |

Gaps with no chip (3.84 to 6.90, 11.78 to 16.26) are Paul speaking full frame; the comp is empty there by design. Declare the
empty spans to blank_scan only if it fails them (template 7a item 7: the span names `ins-paul-1` under it).

## 6 to 8
`references/mg-brief-template.md` §6, §7, §7a (item 7: one frame of each chip composited over `ins-paul-1`), §8.
