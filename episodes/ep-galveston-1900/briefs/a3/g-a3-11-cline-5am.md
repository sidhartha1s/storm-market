# g-a3-11-cline-5am · A3-S10 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `compositions/g-intro-7-clines.html` (Cline lower-third), cards.css `.popfig`, the A1 elevation chip (A1 brief, when built: same chip text and style).

## 0. Claim
Cline counted himself among those in large strong buildings a few blocks from the beach who thought they could weather the wind and tide (his house ground: 5.2 ft). About 5 a.m. on Saturday the 8th, Joseph called him: the tide was well up in the low parts of the city.

## 1. Source
MWR Sept 1900 p. 373 (factcheck/a3-r1.md row 35): "Those who lived in large strong buildings, a few blocks from the beach, one of whom was the writer of this report, thought that they could weather the wind and tide"; p. 372 (rows 36 to 38): "About 5 a.m. of the 8th Mr. J. L. Cline, Observer, called me and stated that the tide was well up in the low parts of the city". 5.2 ft: sources-cline.md §3 ("The ground was 5.2 feet elevation"), planted in A1-S8.

## 2. Datum, scale, orientation
Overlay comp, transparent root. Part A (0.00 to 7.68) over the MWR page (track 1); Part B (7.68 to end) over the pre-dawn street footage. Zones: lower-third bottom-left, chip mid-left, popfig centre, source line top-left.

## 3. Geometry
- Lower-third (shared spec): "ISAAC CLINE" / "Local Forecast Official, Galveston" (as g-intro-7).
- Chip "CLINE'S HOUSE, 1900: 5.2 FT" (A1-S8's exact wording; the act Picture's "CLINE'S HOUSE: 5.2 FT" is aligned to A1, one terminology), left edge x 110, top 420, tag "ground elevation, his report" Arial 700 22 px `#93a3b2`.
- Popfig (cards.css `.popfig`): big "ABOUT 5 AM" (10 characters), sub "SATURDAY, SEPT 8". Over footage only.
- Source line top-left: "Isaac Cline, Monthly Weather Review, Sept. 1900, pp. 372-373".

## 4. Must be true in the picture
1. Whisper writes "Klein": on screen CLINE.
2. "ABOUT" stays on the popfig (the source says "About 5 a.m.").
3. The chip text matches A1's chip exactly (callback: declare `data-callback` per lint rules if the gate asks).
4. Popfig never over the chip or the lower-third: chip and lower-third are out before 7.68.
5. Nothing in x >= 1600, y >= 680.

## 5. Text and cues (a3-s10.words.json, segment 16.66 s)
- 0.00 ("Klein"): source line in; lower-third in at 0.00 /* CLINE @0.00 */.
- 3.40 ("few blocks"): lower-third out by 4.00.
- 4.28 ("beach") /* 5.2 FT @4.28 */: chip in (callback to A1).
- 7.08: chip out by 7.68.
- 7.68 ("At about five") /* 5 AM @7.98 */: popfig sub at 7.80, big at 7.98 ("five"); "SATURDAY" sub reads with 8.56 ("Saturday").
- 9.80 ("Joseph called"): popfig out 9.80 to 10.25.
- 10.76 to 16.66: no text over the street (the voice carries it); footage moves. Gap 6.4 s with the footage as the mover (an overlay over moving footage, allowed).
- Host 0.00 to 16.66.

## Motion for the whole window
Page push in Part A (footage layer); text drifts; Part B footage moves.

## Exit
Nothing on screen at the end (popfig out at 10.25); A3-S11 is Paul (cut).

## Footage under it
- Part A: MWR page with "one of whom was the writer of this report": sourcer's `A3-S10_c1_mwr-sept1900-p373_cline-3-30.png` (p. 373; OCR running head reads 378, page number to check) or c2 (p. 372). Orchestrator checks which scan holds the line.
- Part B: "dark-blue pre-dawn street, water in a low block". Sourcer's `A3-S10_c3_pexels-9481659_cars-flooded-street-night.mp4` shows modern cars: an era mismatch under 1900 narration (CLAUDE.md footage rules: era mismatch disqualifies). Orchestrator call: a crop with no cars, a grade-only dark water surface, or the page held.
