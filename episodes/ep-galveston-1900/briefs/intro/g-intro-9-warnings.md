# g-intro-9-warnings · I1-S4 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `library/inhouse/stat-timeline.html` (sequential chronology labels) and `library/inhouse/numbers-rollup.html` (rows landing in order); restyle both to glass tiles over footage.

## 0. Claim
Washington's messages reached Galveston every day from September 4 to 8; on Friday the 7th the city was under a storm warning; even Friday's midday warning called it a moderate storm. (OSU adds "not a hurricane"; the narration does not say it, so it is not on screen: reveals follow the voice's wording.)

## 1. Source
- MWR Sept 1900 (Cline, in Garriott): "Warning messages were received from the Central Office at Washington on September 4, 5, 6, 7, and 8." (sources-cuba.md §3; factcheck intro-r1 Apply list).
- TSHA: Central office "placed Galveston under a 'storm warning' on September 7" (sources-cline.md §6; factcheck intro-r1 row 18, Friday verified).
- OSU Origins (SECONDARY, a summary, not the warning's text): officials did not change the forecast until midday Friday, "and that warning still called the storm a moderate one, not a hurricane" (sources-cline.md §6; factcheck intro-r1 row 19).

## 2. Datum, scale, orientation
Overlay comp, transparent root, over the MWR report page with a slow push to the "Warning messages were received ..." line (track 1). Zones: a tile row across the upper centre, one chip under it, source line top-left.

## 3. Geometry (px)
- Day row: five glass tiles, each 150 x 150 px, 24 px gaps, row centred on x 960 at top 200 (row spans x 579 to 1341). Each tile: eyebrow "SEPT" Arial 700 22 px `#93a3b2` tracking 6 on top, the day numeral Arial Black 900 72 px `#f2f5f8` under it: 4, 5, 6, 7, 8. Under each numeral a 6 px `#7fb2e5` bar (Washington's colour, as in the maps) that fills `scaleX 0 -> 1` when the tile lands: one message per day.
- Storm-warning tag: on the "7" tile only, a crimson `#8e2020` band across the tile's bottom 40 px, text "STORM WARNING" Arial 700 19 px `#f4f0e8` tracking 2 (tokens.md `.stamp` colours); the "7" tile scales to 1.08 and the others dim to 0.6.
- Chip "MODERATE STORM" (no quote marks, see §4.3): centred x 960, top 470, Arial Black 900 52 px; tag line "Washington, Friday midday" Arial 700 22 px `#93a3b2` tracking 4.
- Source line top-left: "Isaac Cline, Monthly Weather Review, Sept. 1900 · Texas State Historical Association · Ohio State University, Origins".

## 4. Must be true in the picture
1. The five tiles land in date order, each with its bar, and all five are on screen together by "8th".
2. Only the "7" tile carries STORM WARNING. No tile for the 8th claims a hurricane warning (the flag date is CONFLICTING, sources-cline.md conflict 1).
3. "MODERATE STORM" has no quote marks: the only source is OSU's summary, not the text of the warning; quote marks would claim a verbatim quote (CLAUDE.md: no fabricated quotes). The edit script's Picture line asked for quote marks; the orchestrator restores them only with the warning's verbatim text and a row for it.
4. The tiles and chip do not cover the pushed-to line on the page: the push ends with that line at y 700 to 900; if not, the row moves to top 120 and the chip to top 380, and the receipt says so.
5. Nothing in x >= 1600, y >= 680.

## 5. Text and cues (i1-s4.words.json, segment 10.356 s)
- Source line in at 0.00.
- 0.60 ("messages" 0.60): the empty row frame (five tile outlines at opacity 0.3) fades in.
- 2.78 ("4th" 2.78) /* 4TH @2.78 */: tile 4 lands; tiles 5, 6, 7 land at 2.94, 3.10, 3.26; tile 8 at 3.44 ("8th" 3.44) /* 8TH @3.44 */. Each tile `fromTo(y 24, autoAlpha 0 -> 0, 1, 0.35, back.out(1.6))`, bar fills 0.3 s after it.
- 4.74 ("7th" 4.74) /* 7TH @4.74 */: tile 7 scales to 1.08, the rest dim to 0.6.
- 6.44 ("storm" 6.44): STORM WARNING band wipes in across tile 7 (scaleX 0 to 1 from the left, 0.4 s), landing by "warning" 6.62.
- 7.48 ("But" 7.48): the whole row dims to 0.45 and rises 20 px.
- 9.46 ("moderate" 9.46) /* MODERATE @9.46 */: chip in with "MODERATE STORM"; tag "Washington, Friday midday" at 9.74 ("storm").
- Host 0.00 to 10.356 + land time to the cut into I1-S5 (at least 0.8 s; default 11.20 capped by I1-S5's narration start). Exit anchored to the host's last 0.6 s.

## Motion for the whole window
0.00 to 2.78 has the source line and the outline row fading in (drift on both). Tiles and chip drift +-4 px after landing; the page push under it keeps moving.

## Exit
Row and chip slide out right together (`x:980, autoAlpha 0, 0.6, power3.in`), source line fades.

## Footage under it
MWR September 1900 report page, the paragraph with "Warning messages were received from the Central Office at Washington on September 4, 5, 6, 7, and 8" (archive.org MWR 1900-09, p. 373 to 374; public domain).
