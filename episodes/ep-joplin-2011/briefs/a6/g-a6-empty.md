# g-a6-empty · STANDARD (Sonnet 5.5, high) · a6-s7 9.76 to 12.36

Open numbers: none used.
Exemplar: `library/inhouse/snippets/cards.css` `.glasscard` (the one surface for text over footage).
Overlay over the NIST ground photograph of Joplin High School (credit line checked at sourcing), which runs from a6-s7 0.00 to the cut into the CCTV clip. The label names a place: read the photo's `provenance.csv` row before building; it must be Joplin High School, never East Middle School, never stock.

## 0. Claim
Joplin High School was empty when the tornado hit.

## 1. Source
B40, NIST NCSTAR 3 Sec. 1.2: "Although no one was inside Joplin High School or Franklin Technology Center at the time of the storm, individuals at that time were attending services at the nearby Harmony Heights Baptist Church." (East Middle School, B42, is spoken but not pictured; the chip sits on the high school photo only.)

## 2. Datum, scale, orientation
Lower-third anchor: left 110, bottom 110 (tokens.md "Canvas"). Read the photo first: if the school's name or a key wall sits there, move the chip to the top-left title zone (left 96, top 80).

## 3. Geometry
- Chip: glass surface, radius 28, padding 18 x 32; text headline tier Arial Black 900 52 px, Headline white.
- Photo credit line (from the photo's provenance row, verbatim): bottom-right is the presenter corner, so the credit goes bottom-left under the chip at left 110, bottom 60, `#c8d3e0`, 19 px. If the circle is off over this photo (its corner holds a figure or label), the credit may move bottom-right; reading on frames decides.
- Motion: chip `fromTo(x:-40, autoAlpha 0 → x 0, 1)` 0.4 s power3.out, slight y float (4 px) on the hold, exit `x:-600, autoAlpha:0, 0.6, power3.in` in the last 0.6 s.

## 4. Must be true in the picture
1. The photo under every second of the chip is Joplin High School by its provenance row.
2. The chip enters on "empty", not before (the reveal is the voice's).
3. Nothing in x >= 1600, y >= 680.

## 5. Panel text and cues (a6-s7.words.json)
| Element | Exact text | Cue (word @ start s) |
|---|---|---|
| Credit line | (provenance credit, verbatim) | "Joplin" @ 7.50 |
| Chip in | EMPTY THAT EVENING | "empty." @ 9.76 |
| Hold (the bed drops out on this word) | none | to 11.76 |
| Exit | none | 11.76 to 12.36, before the CCTV cut |
Host window 2.6 s from 9.76; if the editor cuts to the CCTV clip earlier than 12.36, the chip exits in the 0.6 s before that cut and keeps at least 1.4 s of hold.

## 6 to 8
Template §6 to §8, COMPID `g-a6-empty`. 7a item 7: one frame composited over the real photo.
