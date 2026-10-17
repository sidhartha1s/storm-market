# g-a2-radar · STANDARD (Sonnet 5.5, high) · act a2, segment a2-s8

**Open numbers (left out of the drawing):** the comment like count (1,500) is in `research/comments-for-writer.md` only;
the card's likes slot stays hidden.
**Open claim:** "NO TORNADO EMERGENCY" has no facts.md row (script cites the NWS Assessment paragraph before Finding 8
via factcheck-acts row A2-S8, not in this worktree). Build the chip; the orchestrator confirms the row before the render.

**Reused, never redrawn:** the clock card from g-a2-countdown (copy its CSS and dial; read its full-size frame first).
Comment card: the A1-S3 component (briefs/a1), as in g-a2-lead-time.
**The radar still:** NWS Assessment Appendix A, Figure 4 panel (G), KSGF 0.5 degree base reflectivity, valid 22 May 2011
22:34Z (5:34 pm CDT); file from sourcing, named at dispatch, cropped so no NWS logo and no third-party basemap shows.
Mounted inside this comp. Panel (H) is not used (the Picture line does not ask for it).
**Host:** a2-s8 narration start to a2-s8 end. **Cue clock:** `segment offset + word start`; offset = a2-s8 narration
`data-start` minus host `data-start`. Corner circle stays on: nothing enters x >= 1600, y >= 680.

## 0. What this graphic claims
The storm gave people little to see: rotation tightened from 5:29, the tornado was down by 5:34 and wrapped in rain.

## 1. SOURCE (confirmed rows, quoted)
- E25 (NWS Finding #10): "Low-level rotational intensification and tornadogenesis occurred very rapidly with the Joplin tornado from 529 pm CDT to tornado touchdown around 534 pm CDT".
- E13 (NWS Table 1): "534 pm CDT - Approximate initial Tornado touchdown".
- E32 (NWS Finding #2d (a)): "a "rain-wrapped" tornado that made the tornado more difficult to recognize until it was very close."
- Comment, verbatim (`research/comments-for-writer.md`, under FagzNHuI5JI): "Joplin didn’t receive a tornado emergency because of how fast it developed."
- Credit line on the still: "NOAA/NWS".

## 2. DATUM, SCALE, ORIENTATION
The still keeps its own geometry: no redraw, no added marks on it, aspect locked. North as printed in the figure.

## 3. GEOMETRY
- Ground: tokens.md canvas radial gradient. Radar still fitted inside the box x 410 to 1190, y 220 to 1000, centred; if the extracted panel is under 600 px tall, report before building (an upscale past 1.3x blurs it).
- Credit "NOAA/NWS" Arial 700 20 px #c8d3e0 under the still's lower-left corner.
- Push: the still scales 1.00 to 1.06 over the host, ease none, origin its centre.
- Clock card: as g-a2-countdown, left 96, top 54. Its dial keeps the comp moving.
- Source line: glass pill right 96, top 54: "NWS Assessment, Finding 10 and the paragraph before Finding 8".
- Chip slot: right column, right-aligned at x 1824, y 140 to 205; glass chip Arial Black 900 40 px #f2f5f8. One chip at a time.
- Comment card: x 1220 to 1824, y 300 to 600; comment Georgia italic 34 px #f2f5f8, under it "Comment under a live TV broadcast re-upload" Arial 700 20 px #93a3b2; slides in from x 660 to 0 + autoAlpha, 0.7 s power3.out.
- Exit: comment card and chip slide x to 980 + autoAlpha 0, 0.6 s power3.in in the host's last 0.6 s; still and clock fade in the same window.

## 4. MUST BE TRUE IN THE PICTURE
1. The still is panel (G), valid 22:34Z, with no NWS logo, no third-party basemap, credited "NOAA/NWS" (never NIST Fig. 2-7).
2. The clock reads 5:29 then 5:34 and never runs past 5:34 (E25, E13).
3. No overlay covers the still (all text sits outside x 410 to 1190 except the credit line under it).
4. The comment is verbatim, curly apostrophe as sourced; no like count.
5. Nothing enters x >= 1600, y >= 680 (comment card ends at y 600).

## 5. PANEL TEXT (exact) and CUES
| cue (segment · word · start s) | what happens |
|---|---|
| a2-s8 · "The" · 0.00 | still in (autoAlpha 0.4 s), push starts; clock card shows "5:17 PM" carried over; source line |
| a2-s8 · "529," · 4.44 | clock rolls to "5:29 PM" |
| a2-s8 · "534," · 6.24 | clock rolls to "5:34 PM" |
| a2-s8 · "wrapped" · 8.88 | chip "RAIN-WRAPPED" |
| a2-s8 · "tornado" · 11.92 | chip "NO TORNADO EMERGENCY" replaces it |
| a2-s8 · "fast," · 16.04 | comment card slides in |
| a2-s8 · "moving?" · 22.10 | hold; exit in the host's last 0.6 s |

## 6 to 8
As `references/mg-brief-template.md` §6, §7, §7a, §8. File `compositions/g-a2-radar.html`, timeline
`window.__timelines["g-a2-radar"]`, root id `a2rd-root`.
