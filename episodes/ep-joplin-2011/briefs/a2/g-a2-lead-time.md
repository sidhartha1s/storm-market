# g-a2-lead-time · STANDARD (Sonnet 5.5, high) · act a2, segment a2-s7

**Open numbers (left out of the drawing):** the comment like counts (1,800 and 2,500) are in
`research/comments-for-writer.md` only, not facts.md. Each card keeps its likes slot built but hidden until the orchestrator confirms.

**Comment card design:** the same component as A1-S3's RODALCO2007 card (briefs/a1). If that brief is built first, copy
it; this spec applies only where it says nothing.
**Over:** designed full-frame ground (tokens.md canvas radial gradient), no footage. Corner circle stays on: nothing enters x >= 1600, y >= 680.
**Host:** a2-s7 narration start to a2-s7 end; enters as g-a2-countdown fades through.
**Cue clock:** `segment offset + word start`; offset = a2-s7 narration `data-start` minus host `data-start`, read at dispatch.

## 0. What this graphic claims
Joplin had real lead time, 17 minutes from the city-wide warning and 23 from the first siren, so neither comment is
right on its own terms; but most people surveyed did not act on a warning alone.

## 1. SOURCE (confirmed rows, quoted)
- E21 (NIST Sec. 2.2.2): "The issuance of TO.W 30 and the sounding of the first sirens in Joplin occurred 25 and 23 minutes respectively before the first reported tornado touchdown at 5:34 p.m."
- E22 (NWS Sec. 4): "WFO Springfield issued Tornado Warning #31 (TO.31) with 17 minutes of lead time for touchdown".
- E6 (NWS Table 1): first siren "511 pm CDT". E9 (NWS Table 1): polygon 31 "517 pm CDT". E13 (NWS Table 1): touchdown "534 pm CDT".
- E37 (NWS Finding #2d): "The majority of surveyed Joplin residents did not take protective action until receiving and processing additional, credible confirmation of the threat and its magnitude from a non-routine trigger."
- Comments, verbatim (`research/comments-for-writer.md`, under the live TV broadcast re-upload FagzNHuI5JI): "Residents of Joplin had plenty of warning time." and "even the best of technology wouldnt have helped alert the people on time".

## 2. DATUM, SCALE, ORIENTATION
- Time axis left to right, 40 px per minute, computed by script: 5:11 at x 500, 5:17 at x 740, 5:34 at x 1420.
- Bar centre line y 720, thickness 16.

## 3. GEOMETRY
- Card L (comment 1): glass card x 120 to 900, y 150 to 470. Card R (comment 2): x 1020 to 1800, y 150 to 470. Inside each: comment Georgia italic 38 px #f2f5f8 (wraps, max 3 lines); under it "Comment under a live TV broadcast re-upload" Arial 700 20 px #93a3b2 tracking 2; the hidden likes slot right of that line.
- Bar: segment A 5:11 to 5:17, x 500 to 740, `#d8a13a`; segment B 5:17 to 5:34, x 740 to 1420, `#e74c3c`. Each draws scaleX 0 to 1, transformOrigin left, 0.5 s.
- Tick labels above the bar, centred on each tick, y 640 to 690: "5:11 PM" Arial 700 30 px #dfe7ee with "First siren" Arial 700 20 px #93a3b2 under it; "5:17 PM" / "Warning"; "5:34 PM" / "Touchdown". Ticks 2 px x 28 px #dfe7ee.
- Chip "17 MIN": glass chip Arial Black 900 52 px #f2f5f8, centred x 1080 (segment B mid), y 560 to 625, above the tick labels.
- Bracket 23: a 3 px `#e8c56a` bracket under the bar from x 500 to 1420 at y 770, end hooks 14 px up. Chip "23 MIN" centred x 960, y 795 to 860.
- Source line: glass pill bottom-left, left 96, bottom 60, Arial 700 20 px #c8d3e0; the three lines swap in this one slot.
- Hold motion: cards float y +-5 px (sine, finite repeat, offset phases); a 6 px light dot runs along the bar from x 500 to 1420 once per 4 s (230 px/s) after the bar is drawn.
- Exit: cards slide out (L to x -980, R to x 980) + autoAlpha 0, 0.6 s power3.in, bar and chips fade in the same last 0.6 s.

## 4. MUST BE TRUE IN THE PICTURE
1. Segment B (17 min) is 680 px and the 23-min span is 920 px: ratio 0.7391, the same as 17/23 (script-computed).
2. Segment A (5:11 to 5:17) is 240 px, 6 minutes (E10's "6 min earlier" agrees).
3. Both spans end at the same 5:34 tick (E13); no span runs past it.
4. The comments are verbatim, including "wouldnt" without an apostrophe; no username shown (none in the sources).
5. No like count shows until it has a facts.md row.
6. Nothing enters x >= 1600, y >= 680 (the bar ends at 1420; card R ends at y 470).

## 5. PANEL TEXT (exact) and CUES
| cue (segment · word · start s) | what happens |
|---|---|
| a2-s7 · "From" · 0.00 | card L in |
| a2-s7 · "citywide" · 0.90 | 5:17 tick + label; segment B draws |
| a2-s7 · "17" · 2.58 | chip "17 MIN"; source line "17 min · 5:17 warning to touchdown · NIST Sec. 2.2.2 · NWS Sec. 4" |
| a2-s7 · "touchdown." · 3.72 | 5:34 tick + label |
| a2-s7 · "From" · 5.12 | card R in |
| a2-s7 · "first" · 5.42 | 5:11 tick + label; segment A draws, then the 23 bracket draws left to right, 0.6 s |
| a2-s7 · "23." · 6.66 | chip "23 MIN"; source line "23 min · first siren to touchdown" |
| a2-s7 · "didn't" · 12.54 | source line "most did not act on a warning alone · NWS Assessment" |
| a2-s7 · "coming?" · 18.16 | hold; exit in the host's last 0.6 s |

## 6 to 8
As `references/mg-brief-template.md` §6, §7, §7a, §8 (item 6: bar positions computed by script from §2, stated in the
receipt). File `compositions/g-a2-lead-time.html`, timeline `window.__timelines["g-a2-lead-time"]`, root id `a2lt-root`.
