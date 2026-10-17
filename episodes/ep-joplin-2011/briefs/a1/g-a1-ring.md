# BRIEF · g-a1-ring · "one strong tornado in the city, 182 all around it" · DEEP (Opus 5.5, high)

Episode ep-joplin-2011, act A1, segment A1-S10, second half. The host runs from a1-s10 "Since" 8.76 to the wav end 19.56
(duration 10.80). It is a full-frame map on the channel ground, entered on a cut from `g-a1-bubble-page`. `g-a1-second-siren` follows.
Exemplar: `library/inhouse/master-map-us-canada.html` (Natural Earth 50m admin-1 states, public domain). Copy its
projection and state lines and retune the framing. This is not the MASTER MAP: it is a regional map. The city outline
is the only thing taken from the MASTER MAP base.
Open numbers: the 182 tornado positions (`_list.md` Open 5). The dots are illustrative and the source line says so.

## 0. What this graphic claims
Since 1950 the city itself had been hit by one tornado rated EF-2 or stronger, on 5 May 1971 (S36). Within 80 miles,
182 of that strength had struck (S37). That is why people believed Joplin was spared (S23, S38). The city must look
like a speck inside a crowded ring.

## 1. SOURCE
- S36 "Prior to 2011, the roughly 30-square-mile City of Joplin had experienced one tornado rated EF-2 or greater since 1950; this tornado occurred on May 5, 1971." NIST Finding 33.
- S37 "also since 1950, 182 tornadoes rated EF-2 or higher had struck within an 80-mile radius of the City." NIST Finding 33.
- Reading (flagged in `_list.md`): "within an 80-mile radius of the City" includes the city, so 182 = 181 outside the outline + the 1971 dot inside.

## 2. DATUM, SCALE, ORIENTATION
- North up, the exemplar's projection. Scale **5.0 px per mile**: the ring radius is 80 mi = 400 px.
- Ring centre = the centroid of Joplin's city outline, placed at (720, 560). The ring spans x 320 to 1120, y 160 to 960.
- Right rail for the chips: x 1240 to 1780, rows at y 380 and y 480. Everything stays out of x ≥ 1600, y ≥ 680, so the presenter circle may stay on.
- State lines (Missouri, Kansas, Oklahoma, Arkansas) come from the exemplar's data at the same scale: 2 px Diagram grey 2
  `#2a3644`. State names are optional small labels (Arial 700 19 `#93a3b2`). Each sits clear of every dot, and none goes on the ring.

## 3. GEOMETRY (computed by `python3`, 17 Oct 26)
- **City outline:** the MASTER MAP base's Joplin outline path, scaled to 5.0 px/mi, 2 px stroke `#f2f5f8`, fill
  `rgba(242,245,248,.10)`. Area check: 30 sq mi × 25 px² per sq mi = 750 px², within ±15 % (637.5 to 862.5 px²). The
  equal-area radius is about 15.5 px. If the base has no outline yet, draw an equal-area circle of r 15.5 px and label it in the receipt.
- **"Joplin" label:** Arial 700 26 `#f2f5f8`, left of the outline at x ≈ 690 (right-aligned), baseline 568. It must clear the city dot and the 1971 label.
- **City dot (1971):** r 5 px, Danger red 2 `#e74c3c`, inside the outline at its centroid. Label "May 5, 1971" in Arial 700 22
  `#f2f5f8`, right of the outline, left edge x 748, baseline 552. No dot falls under that label (keep-out box x 740 to 900, y 528 to 562).
- **Ring:** circle r 400, 3 px stroke Cold blue 2 `#7fb2e5`, no fill. Dash length = ceil(2π·400)+1, measured with `getTotalLength()` and never typed.
- **Radius line + label:** a 2 px `#7fb2e5` line from the centre to the ring at 315° (up and right), reaching (1002.8, 277.2)
  (compute it). Label "80 miles" in Arial 700 26 `#7fb2e5`, beside the line's midpoint, offset 24 px perpendicular to the upper left, never on the line.
- **182 field:** 181 dots, r 4 px, Danger red 1 `#c0392b` at 90 %, placed by a seeded Poisson-disc fill (fixed seed,
  stated in the receipt): every dot is inside r ≤ 392 (8 px inside the ring), outside the city outline + 10 px, outside
  the label keep-out boxes (the "Joplin", "May 5, 1971" and "80 miles" labels + 6 px), with a minimum spacing of 14 px.
  That gives about 3.6 dots per 100 × 100 px (computed). The positions are illustrative.
- **Eyebrow:** "EF2 or stronger · since 1950", Arial 700 22 `#93a3b2` tracking 6, top-left x 120, baseline 110.
- **Rail chips:** glass chips with left edge x 1240. Row 1 "1 IN THE CITY" (y 350 to 410). Row 2 "182 WITHIN 80 MILES" (y 450 to 510).
- **Source line:** "NIST Finding 33 · dot positions illustrative", x 96, baseline 1010. The ring's lowest point near x 96 to
  700 is above y 960, so the line clears the ring by ≥ 30 px.

## 4. MUST BE TRUE IN THE PICTURE
1. There are exactly 182 red dots after the fill: 1 inside the city outline and 181 outside it, all inside the ring. Count them by script on the final frame.
2. The ring radius is 400 px ±4, and the city's equal-area radius is 15.5 px ±1.2. The city disc is 0.149 % of the ring's disc
   (computed). On the frame, the city reads as a speck, not a district.
3. No dot touches the city outline, a label or the ring stroke.
4. "May 5, 1971" names the one dot inside the outline and nothing else.
5. The ring is a circle (not an ellipse) in screen px. If the projection distorts at this scale, the ring is drawn in screen space.

## 5. PANEL TEXT (exact) and CUES (a1-s10, comp-local = word − 8.76)
| element | text | cue |
|---|---|---|
| ground, state lines, city outline, "Joplin" | "Joplin" | frame 0 (a1-s10 "Since" 8.76). The map settles from scale 1.04 to 1.00 over 1.2 s (`to`, small linear) |
| eyebrow | "EF2 or stronger · since 1950" | "1950," 8.94 |
| city outline brightens (stroke to 3 px, fill to 18 %) | (none) | "city" 9.98 |
| city dot drops in (y −30 to 0, back.out) + label | "May 5, 1971" (S36) | "one" 11.28, label on "tornado" 11.76 |
| rail chip 1 | "1 IN THE CITY" (S36) | "stronger." 13.76 |
| ring draws clockwise from 12 o'clock | (none) | "Within" 14.86, closed by "miles" 15.44 |
| radius line + label | "80 miles" (S37) | "80" 15.10 |
| 181 dots pop (scale 0 to 1, seeded order, about 0.0045 s apart) | (none) | "182" 16.92, done by "of" 17.74 |
| rail chip 2 | "182 WITHIN 80 MILES" (S37) | "of" 17.74 |
| hold | | to 19.56. The dots twinkle in finite repeats (opacity 0.75 to 1, staggered), and the map drifts 6 px/s right to left. Cut on the host end |

The last discrete beat is 17.74, followed by a 1.8 s hold. Gaps stay under 4 s.

## 6 to 8
`references/mg-brief-template.md` §6, §7, §7a (all seven), §8. The receipt states the dot count inside and outside (script),
the seed, the outline area in px² and the radius-line endpoint.
