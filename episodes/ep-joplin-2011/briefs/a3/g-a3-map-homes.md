# BRIEF g-a3-map-homes · A3-S1 tail + A3-S3 · DEEP (Opus 5.5, high effort) · on base `g-master-map`

Read first: `references/mg-quickref.md`, `learnings/mg.md`, `library/inhouse/snippets/tokens.md`. Base: `g-master-map` (episode master map; copy its `<!--BASEMAP:g-master-map-->` … `<!--/BASEMAP-->` block verbatim, the way `episodes/ep-enderlin-2025/compositions/g-master-map-a3.html` does; never redraw the city, path or streets). If `compositions/g-master-map.html` does not exist yet, this brief waits for it.

**Open (left out of the drawing):** the published figure for residential death positions. No facts.md row cites one. Dots go where the base's fatality layer puts them; if the base has no sourced positions, the dots sit inside the base's residential band of the path and the comp carries the small label "Schematic · not to scale" (19 px, bottom-left, above the source line).

## 0. What this graphic claims
Joplin had no public shelter anywhere (H3, H4), and 59 people were lost in single-family houses, 51 homes, nearly all flattened (H9, H10, H11).

## 1. SOURCE
- H3, Finding 20: "There were no community shelters or safe rooms in the City of Joplin or Jasper County at the time of the May 22, 2011, Joplin tornado."
- H4, E.4.1: "the City did not own or operate any public storm shelters."
- H9, Sec. 4.6.2.2: "These 59 people died in a total of 51 homes along the damage path, since six sets of 2 people and one set of 3 people were together in the same houses".
- H10: "with the majority of fatalities (54 out of 59 or 92 percent) occurring in homes rated as "demolished."" H11: "(50 out of 59, or 85 percent) occurred in one-story homes".
- H26 / Table 4-3: 59 in detached homes, base 154 impact-related (the CONFLICT note under H25/H26: never 62 here).

## 2. DATUM, SCALE, ORIENTATION
The base's projection, north-up orientation, scale bar and street grid, unchanged. Every px this comp adds is in the base's coordinates; compute positions by script from the base's layer data and state them in the receipt (done line 6).

## 3. GEOMETRY
Part A (city view, the base's default framing):
- Scan line: 2 px vertical bar, gradient `rgba(127,178,229,0)` → `.30` → `0`, full map height, sweeps the city limits west → east (≥ 6 px/s; about 1200 px over 2.5 s).
- No shelter icon layer exists. Nothing pings as the scan passes.
- Chip (glass popup-chip): left 96, top 96, "NO PUBLIC SHELTER", Arial Black 900, 52 px.
- Source line (glass source-label, left 96, baseline ≤ 1026, 20 px): "No community shelters or safe rooms · city or county · Finding 20".
Part B (push into the residential area of the path):
- Camera: push from the city view to the bounding box of the 51 house outlines + 80 px margin, with `logZoom` (`library/inhouse/snippets/helpers.js`) if the scale change is over 1.5x.
- 51 house outlines: 18 × 16 px house glyph (square + roof peak), stroke `#dfe7ee` 1.5 px, at the base's residential positions.
- 59 dots: 7 px circles, fill `#c0392b` (danger red 1), inside the outlines: 44 outlines with 1 dot, 6 with 2 (side by side, 3 px gap), 1 with 3. (44 + 6×2 + 1×3 = 59, computed from H9.)
- Chip swaps to "59 LOST IN HOUSES" (same slot).
- Running label: glass lower rail, left 96, width ≤ 1400, baseline y 960, Arial 700 30 px `#dfe7ee`, one line building left to right: "59 people · 51 homes" then " · 54 lost in demolished homes" then " · 50 in one-story homes".
- Source line swaps to "NIST Sec. 4.6.2.2 · Table 4-3".
- Corner x ≥ 1600, y ≥ 680: no label, no dot glyph (if a dot lands there, the circle is off for that span; tell the orchestrator).

## 4. MUST BE TRUE IN THE PICTURE
1. Part A: no shelter icon, marker or legend entry for a shelter anywhere, at any frame.
2. Part B: exactly 59 dots inside exactly 51 house outlines; 44 / 6 / 1 outlines hold 1 / 2 / 3 dots. No dot outside an outline.
3. No apartment dot (those 12 come in g-a3-apartments) and no dot of any non-residential place.
4. No dot sits in or near any "below ground" marker; the comp draws no below-ground row.
5. The running label's numbers are 59, 51, 54, 50 only, and 54 and 50 never exceed 59. The chip's 59 equals the running label's 59.

## 5. PANEL TEXT (exact) and CUES
Text: "NO PUBLIC SHELTER" · "No community shelters or safe rooms · city or county · Finding 20" · "59 LOST IN HOUSES" · "59 people · 51 homes · 54 lost in demolished homes · 50 in one-story homes" · "NIST Sec. 4.6.2.2 · Table 4-3".
Host: a3-s1 "to." @9.58 + 0.8 (fade-through from g-a3-house-section) → a3-s3 "Didn't" @8.98 (cut to the flattened-houses clip; if no clip is sourced, hold to a3-s3 "there?" @11.46 + 0.8 and exit on a pull-out).
- Part A, host 0.0: city view on from frame 0; scan sweep 0.0–2.5; chip "NO PUBLIC SHELTER" at host 0.8; source line at 0.8. The cut A3-S2 line leaves no spoken trigger: the orchestrator keeps ≥ 2.5 s between this host's start and a3-s3 "Fifty" @0.00.
- a3-s3 "Fifty" @0.00: chip swaps (old out 0.3 s, new in), source line swaps, push-in starts (1.2 s). Outlines and dots light west → east, one every ~0.035 s, done by "houses," @2.20.
- a3-s3 "houses," @2.20: running label "59 people · 51 homes".
- a3-s3 "flattened." @5.16: " · 54 lost in demolished homes".
- a3-s3 "path" @7.22: " · 50 in one-story homes".
- Holds: dots blip in small groups (scale 1 → 1.35 → 1, ≤ 1.5 s apart) and the camera drifts 6 px/s.

## 6–8. CONTRACT, TOOLS, DONE LINE, RECEIPT
`references/mg-brief-template.md` §6, §7, §7a and §8 unchanged, COMPID = `g-a3-map-homes`, root id `g-a3-map-homes-root`.
