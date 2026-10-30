# g-a2-10-paul-panel · A2-S9 (Paul on camera, ins-paul-3) · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules" (chip, glass). Base: `compositions/g-a2-9-sept4-map.html` (built first): the panel shows the same map crop and the same two arrows, scaled. Exemplar: `library/inhouse/quote-card.html` (quote typography). Why this clip has graphics: `_list.md` change 8 (the owner's 26 Oct rule: Paul holds nothing; what he refers to is a widget on top).

## 0. Claim
The Bureau's own man in Havana, Stockman, later wrote that the storm "was not severe in the West Indies". Beside Paul, the 4 September map shows the two readings: Washington's arrow to south Florida, Belen's into the Gulf. The question (why was Washington so sure?) is Paul's; the graphic only holds the evidence.

## 1. Source
- Quote: sources-cuba.md §4 (MWR Sep 1900, Stockman, Havana forecast district: "The storm was not severe in the West Indies although the rains were, in places, torrential"); factcheck/a2-r1.md row 48; a2-r2 rows 18 (an after-the-fact summary printed in the September issue), 19 (chip text is an exact substring, quote marks allowed).
- Panel map and arrows: as g-a2-9 §1.

## 2. Datum, scale, orientation
Overlay comp, transparent root, over Paul's full-frame clip `ins-paul-3` (not generated; built against `media/paul/paul-start-frame-omni-standin.jpg` scaled to 1920 x 1080). On that frame (measured from the stand-in, x 1.157): Paul's face spans about x 787 to 1111, y 93 to 555; his hands about x 560 to 1300, y 680 to 1000; the right side (x 1150 to 1920, y 160 to 690) is the monitor wall; the logo bug sits at x 1692 to 1788, y 852 to 948 (`references/mg-quickref.md` "Logo on every full-frame clip"). The presenter circle is off on this clip.
Panel scale: 534 / 1920 = 0.2781 of g-a2-9's frame.

## 3. Geometry (px)
- Panel: glass card x 1290 to 1824, y 150 to 488 (radius 20, padding 10 px). Inside: eyebrow "NOAA map · Sept. 4, 1900" Arial 700 20 px `#93a3b2` tracking 4 at top; under it the image `media/a2/noaa-map-1900-09-04-gulf.jpg` at 514 x 289 (x 1300 to 1814, y 189 to 478), with the `.dim` scrim over the image only.
- On the image, every g-a2-9 mark at 0.2781 x its g-a2-9 screen point, offset by the image origin (1300, 189): Galveston dot 6 px, storm ring radius 19 px, Washington arrow dashed `#7fb2e5` 3 px, Belen arrow solid `#d8a13a` 3.5 px. Take the endpoints from g-a2-9's receipt (its measured points), not from this brief's approximations.
- Arrow tags on the image: "Washington" Arial 700 19 px `#7fb2e5` near its arrowhead; "Belen" Arial 700 19 px `#e8c56a` near its arrowhead (each on a small glass pill so it reads over the scan).
- Chip (quote card, glass, radius 28): x 96 to 760, top 120. Main "“Not severe in the West Indies”" Arial Black 900 52 px `#f2f5f8`, two lines ("“Not severe in" / "the West Indies”"), max width 600; tag "W. B. Stockman, Monthly Weather Review, Sept. 1900" Arial 700 22 px `#93a3b2` tracking 2, two lines allowed.
- Tiers: 52 (quote), 22 / 20 / 19 small; add one mid line only if `graphics_qc` asks (it should not: the quote is big, tags small, the rule counts tiers, and the eyebrow can move to 26 px if a third tier is needed).

## 4. Must be true in the picture
1. Paul's face and hands are never covered: the chip's right edge stays at x 760 or less, the panel's left edge at x 1290 or more, and both stay above y 500 on the left side and above y 490 on the right.
2. The logo bug (x 1692 to 1788, y 852 to 948) is never covered.
3. The quote reads exactly "Not severe in the West Indies" inside curly quotes, attributed to Stockman, Monthly Weather Review.
4. On the panel the Belen arrow does not reach or point at Galveston (g-a2-9 truth 2 carries over).
5. Paul holds nothing: no element of the comp is placed to look like it sits on his desk or in his hands.

## 5. Text and cues (a2-s9.words.json, the TTS stand-in; retime to the clip's own transcript once ins-paul-3 exists)
- 0.00: panel slides in from the right (`fromTo(x:660 -> 0, 0.7, power3.out)`), arrows already drawn (this is the reference he points to).
- 0.30 (inside "Stockman," 0.00 to 0.82) /* STOCKMAN @0.30 */: chip enters with the tag visible; main line hidden.
- 3.68 ("not" 3.68) /* NOT SEVERE @3.68 */: main line in word by word: "Not severe" 3.68, "in the" 4.28, "West Indies”" 4.60.
- 5.40 to 5.80: chip exits (`to x:-980, autoAlpha 0, 0.6, power3.in` shortened to 0.4 s); the question is Paul's alone.
- 6.24 ("Washington" 6.24) /* WASHINGTON @6.24 */: the panel's Washington arrow pulses (opacity 0.7 to 1, stroke 3 to 4.5 px, 0.5 s yoyo once).
- 7.64 ("curve" 7.64): hold.
- Host: A2-S9 0.00 to 8.321 (the clip's real length once generated).

## Motion for the whole window
Panel and chip drift y +-4 px from landing; the panel's storm ring breathes (scale 1 to 1.08, 1.6 s yoyo). Paul moves underneath.

## Exit
Panel slides out right (`to x:980, autoAlpha 0, 0.6, power3.in`) over the host's last 0.6 s (7.721 to 8.321), into the chapter blackout before A3.

## Footage under it
`ins-paul-3` (Paul full frame, P3, empty desk). Not generated yet: `paul-clips.md` ins-paul-3 still ends "would turn?" while the locked line ends "would curve away?"; the prompt is fixed before credits are spent (`_list.md` open items).
