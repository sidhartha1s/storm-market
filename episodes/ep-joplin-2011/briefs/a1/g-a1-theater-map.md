# BRIEF · g-a1-theater-map · "three people in that theater were lost" · DEEP (Opus 5.5, high)

Episode ep-joplin-2011, act A1, segment A1-S2, tail. The host runs from a1-s2 "Three" 10.26 to the wav end 15.96 (duration 5.70).
It is a full-frame map, entered on a cut from `g-a1-quote-120` (the glass quote card over the NOAA aerial). `g-a1-numb` follows.
Base: MASTER MAP (first built for T1-S2, intro briefs). Copy it, add the layer below, add no geography. Same builder
as `g-a1-second-siren` and the a2 map comps. Exemplar for labels fitted to real landmarks: `references/editing-patterns/ep3-map-route-fit.html`.
Open numbers: the theater position (`_list.md` Open 3). It comes from the base's outline layer. If the base has no Stained Glass Theater outline, stop and report: do not place it from a geocode yourself.

## 0. What this graphic claims
Three of the people in the Stained Glass Theater lost their lives (B25). The theater is one building on the case board.
This is the first time a location's losses land on the master map in A1.

## 1. SOURCE
- B25 "Three of these occupants lost their lives due to injuries sustained as the tornado struck. According to interviewees, the victims did not make it into the basement before the tornado hit." NIST Sec. 1.2.
- Geography: the MASTER MAP base's own traced source. Nothing here moves an outline.

## 2. DATUM, SCALE, ORIENTATION
- The base's projection, north up, and its px per mile at the city framing. The push-in is one uniform scale about the theater outline's centroid, with no rotation.
- Start framing: the base's city view (the state T1-S2 and I1-S7 establish), so the viewer recognises the board.
- End framing: the theater centroid at (900, 540), with a scale factor chosen so that the theater outline's longer side is ≥ 90 px on screen.
  State the factor in the receipt. Over 1.5×, use `logZoom` (`library/inhouse/snippets/helpers.js`); otherwise a linear `to()` is fine.
- Presenter circle: graphics-only scene, circle stays on. Nothing enters x ≥ 1600, y ≥ 680.

## 3. GEOMETRY
- **Theater outline highlight:** the base's outline, stroke to 3 px `#f2f5f8`, fill `rgba(242,245,248,.14)`.
- **Label:** "Stained Glass Theater", Arial 700 26 `#f2f5f8`, a leader 24 px to the upper right of the outline. Text
  never sits over the outline, a street label or a marker.
- **3 markers:** filled circles r 9 px, Danger red 2 `#e74c3c`, with a 2 px `#04070c` keyline, in a row of three 26 px apart
  (centre to centre), centred on the outline's centroid. All three sit inside the outline at the end scale. The markers are
  counts, not positions: NIST does not say where in the building the three were.
- **Chip:** glass chip "3 LOST HERE", top centre (x 960, y 96 to 166).
- **Source line:** "NIST NCSTAR 3 · Sec. 1.2", x 96, baseline 1010.
- Every other base label that would sit under the new label or the chip at the end framing dims to 30 %.

## 4. MUST BE TRUE IN THE PICTURE
1. There are exactly 3 markers, all inside the theater outline at the end framing.
2. The highlighted outline is the Stained Glass Theater per the base's layer (name it in the receipt with the base's id).
3. The map geometry is unchanged from the base: overlay one frame at scale 1 on the base and check that the outlines match within 2 px.
4. Neither the label nor the chip covers a marker or the outline.

## 5. PANEL TEXT (exact) and CUES (a1-s2, comp-local = word − 10.26)
| element | text | cue |
|---|---|---|
| base map at city framing | base text | frame 0 (a1-s2 "Three" 10.26) |
| push-in to the theater; outline highlights | (none) | "Three" 10.26 to "theater" 11.16 (0.90 s, power2.inOut) |
| 3 markers pop (scale 0 to 1, back.out, 0.12 s apart) + label | "Stained Glass Theater" | "theater" 11.16, after the push has landed (the markers must sit still when they appear) |
| chip | "3 LOST HERE" (B25) | "lost." 11.64 |
| source line | "NIST NCSTAR 3 · Sec. 1.2" | "lost." 11.64 |
| hold | | "Were" 12.96 to 15.96. The markers pulse in finite repeats (scale 1 to 1.15, 1.2 s period) and the map drifts 6 px/s. Cut on the host end |

Note: the Picture line says the markers light "on 'three people'" (10.26 to 10.54). They land at 11.16, after the push settles, because
markers placed during a camera move are text on a moving object. If the orchestrator wants them on 10.54, shorten the push to finish by 10.54.

## 6 to 8
`references/mg-brief-template.md` §6, §7, §7a (all seven), §8. The receipt states the end scale factor and the outline id from the base.
