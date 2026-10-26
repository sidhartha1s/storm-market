# Intro section graphics: ep-appalachian-1950 (H1-S1 to H1-S5, I1-S1 to I1-S4)
Written 26 Oct 26 from `edit_script.md` (hook PROVISIONAL, drop-in shape), `audio/*.words.json` (tempo 0.94), `research/nws-facts.md`, `factcheck/intro-r2.md`.
Every brief carries `references/mg-quickref.md` and `references/mg-brief-template.md` §6-§8 by reference; read both before building.

| comp id | segments | what it shows (one line) | depth | builder model | library exemplar to start from | sits over |
|---|---|---|---|---|---|---|
| g-intro-1-date | H1-S1 | Red Abril popfig "NOV 25, 1950" + sub "SATURDAY · NEWARK, NEW JERSEY" on Paul's first clip | standard | Sonnet 5.5 high | `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` (popfig part only), `library/inhouse/snippets/cards.css` `.popfig` | `ins-paul-1` (Paul full-frame clip 1) |
| g-intro-2-hookmap | H1-S2, H1-S3, H1-S4, H1-S5 | Self-made map: Newark gust pin, swing west to a snow-white Pittsburgh pin, toll line, push north to Buffalo (40s, no snow) vs Pittsburgh (single digits), back to Newark; no link between the pins | deep | Opus 5.5 | `library/inhouse/master-map-us-canada.html` (basemap, projection, camera rig) | nothing: full-frame designed map (track 2) |
| g-intro-3-coast | I1-S1 | Same map from the hook's last frame: tide line and flood fill along the New Jersey shore, then a slide to a LaGuardia pin with a schematic runway flood inset (fallback while LaGuardia footage is TBD) | deep | Opus 5.5 | `library/inhouse/master-map-us-canada.html`; ends on its own frame | nothing: full-frame designed map |
| g-intro-4-lga-chip | I1-S1 (second half, only if LaGuardia footage lands) | Glass chip "DIKES BREACHED · LAGUARDIA" over the LaGuardia footage | standard | Sonnet 5.5 high | `library/inhouse/snippets/cards.css` `.lt` + `.glasscard`; `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` | LaGuardia flood footage, SOURCE TBD (sourcing lane) |
| g-intro-5-inland | I1-S2, I1-S3, I1-S4 | Map swings west to Pittsburgh under snow, cold-blue fill slides south to Kentucky (no place named), Bowling Green pin turns deep blue "-7°F", back to Newark where "108 MPH" dims and an unnamed "?" marker pulses | deep | Opus 5.5 | `library/inhouse/master-map-us-canada.html` | nothing: full-frame designed map |
| g-intro-6-pbz-sheet | I1-S2 (first 5 s) | NWS Pittsburgh "largest snow storms" sheet crop slides in, rank-1 row highlighted, chip "27.4 IN · BIGGEST ON RECORD" | standard | Sonnet 5.5 high | `library/inhouse/quote-card.html` (document card, beige cite stock) | g-intro-5-inland (map right half, kept clear of labels) |
| g-intro-7-lmk-sheet | I1-S3 | NWS Louisville Bowling Green November records table, ALL-TIME row "-7, 1950" highlighted, chip "STILL THE NOVEMBER RECORD" | standard | Sonnet 5.5 high | `library/inhouse/quote-card.html` | g-intro-5-inland (map right half, kept clear of labels) |

Count: 7 graphics (6 always built, g-intro-4 only if LaGuardia footage is found). Deep 3 (Opus 5.5), standard 4 (Sonnet 5.5 high).

## Section-wide decisions (each brief repeats the part it needs)
- **L1 stays closed.** No graphic in this section draws a storm track, a low ("L") symbol, a front, isobars, pressure numbers, wind arrows, a line or band joining Newark to Pittsburgh, Buffalo or Bowling Green, or any shading that spans both coast and inland. The pins are separate dots on a plain basemap. Act 3 owns the mechanism.
- **Paul's clip rule.** H1-S1's Picture line also asks for chips "108 MPH" and "WINTER STORM" on Paul. Brief rule: Paul's full-frame clips get only the date/place popfig. "108 MPH" moves onto the Newark pin as the map's frame 0 (g-intro-2); "WINTER STORM" is dropped (the narration says it; no second text over his face).
- **Chip wording.** fact-check intro-r2 row 11 apply list: "200 MI NORTH" becomes "ABOUT 200 MI NORTH" (edit_script.md still carries the old chip text; narration already says "about"). The straight-line distance is about 179 mi (computed, fact-check), so the map shows no scale bar and no measured ruler.
- **Two-line chips.** Chips too wide for one big line keep the edit_script words, split into a big line and a smaller line: "27.4 IN" / "BIGGEST ON RECORD", "STILL THE" / "NOVEMBER RECORD", and (footage branch) "DIKES BREACHED" / "LaGuardia Airport".
- **Popfig date.** "SAT, NOV 25, 1950 · NEWARK, NJ" breaks the popfig limit (big line 16 characters or fewer, 3 words or fewer). Split: big "NOV 25, 1950" (12 characters), sub "SATURDAY · NEWARK, NEW JERSEY".
- **One map, one coordinate system.** g-intro-2, -3 and -5 copy the same basemap and projection: map x = 3841 × (lon + 97.576), map y = -5585 × (lat - 46.6213). Camera frames (A to H) are defined once below and each brief quotes the ones it uses. Screen px = (map unit - frame top-left) × s.

| frame | s (px per map unit) | anchor pin at screen px | frame top-left in map units | pins on screen (px) |
|---|---|---|---|---|
| A | 0.12 | Newark (1100, 560) | (80726.5, 28204.4) | NWK (1100,560), LGA (1238,532), Sandy Hook (1179,745) |
| B | 0.04024 | Pittsburgh (520, 600) | (54602.7, 19608.7) | NWK (1420,534), PIT (520,600), BUF (693,50) |
| C | 0.04024 | Pittsburgh (760, 820) | (48638.5, 14141.5) | NWK (1660,754), PIT (760,820), BUF (933,270) |
| D | 0.04024 | Newark (1240, 560) | (59078.1, 18954.6) | NWK (1240,560), PIT (340,626), BUF (513,77) |
| E | 0.06 | Newark (900, 380) | (74893.2, 26537.8) | NWK (900,380), LGA (969,366), Sandy Hook (940,472), Atlantic City (842,840), Cape May (731,983) |
| G | 0.25 | LaGuardia (860, 540) | (87599.4, 30481.0) | NWK (573,598), LGA (860,540) |
| H | 0.04024 | Pittsburgh (560, 520) | (53608.7, 21596.7) | NWK (1460,454), PIT (560,520), Columbus (96,628) |
| F | 0.025 | Bowling Green (480, 640) | (23416.7, 28310.9) | BWG (480,640), Louisville (549,461), PIT (1103,155), NWK (1662,114) |

Pin lon/lat (decimal, W negative): Newark 40.7357, -74.1724 · Pittsburgh 40.4406, -79.9959 · Buffalo 42.8864, -78.8784 · LaGuardia 40.7769, -73.8740 · Bowling Green 36.9685, -86.4808 · Sandy Hook 40.4600, -74.0000 · Atlantic City 39.3643, -74.4229 · Cape May 38.9351, -74.9060. Map-unit values in each brief; compute any new point with the formula, never by eye.

- **Segment offsets inside multi-segment comps** assume a 0.40 s gap between narration segments (no index.html exists yet). Each map brief's script keeps a `SEG` offset table at the top; the orchestrator's real `data-start` differences replace those numbers, and every cue is `SEG[seg] + word time`.
- **Hook swap.** If the owner picks another hook shape, g-intro-1 and g-intro-2 are redone; g-intro-3 is kept but its frame-0 state (frame D, which is g-intro-2's last frame) is re-matched to the new hook's last picture. g-intro-4 to -7 stand.
- **Corner circle.** Hidden in the hook (H1-S1 to H1-S5). From I1-S1 on, every map comp keeps the corner x >= 1600, y >= 680 free of labels, numbers and highlighted shapes so the circle can run.
- **Track and mounts.** Map hosts on track 2; sheet and chip overlays on track 3. The overlays sit over map regions the map brief keeps label-free in that window (occlusion_check).
