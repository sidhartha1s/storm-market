# g-a6-doc-rec7 · STANDARD (Sonnet 5.5, high) · a6-s1 6.30 to 17.80

Open numbers: N10 (text "located in tornado hazard areas" is past the 50 words facts.md quotes; its underline is left out until the orchestrator checks it on the page render).
Base: the document page with underline first used at A1-S6 (`briefs/a1/`): same page card, underline colour, stroke and draw speed. Copy it.
Full-frame graphic. Asset: a render of the NIST NCSTAR 3 page carrying Sec. 5.2.2 Recommendation 7 (US government, public domain), from sourcing; mount the trimmed render named in its provenance row, capped at 1920 x 1080.

## 0. Claim
NIST's Recommendation 7 asks for tornado shelters in new and existing apartment buildings, stores, schools and assembly buildings.

## 1. Source
R3, NIST NCSTAR 3 Sec. 5.2.2 Recommendation 7: "(b) tornado shelters be installed in new and existing multi-family residential buildings, mercantile buildings, schools and buildings with assembly occupancies". R4 (the reason, big-store refuge areas) is narration only and is not drawn.

## 2. Datum, scale, orientation
The page render is the datum: underlines are measured on it, never typed. Page card centred, page text column scaled so its body text is at least 26 px tall on screen (the passage must read on a TV). Underline: 6 px, 4 px under the glyph baseline, from the first glyph's left edge minus 4 px to the last glyph's right edge plus 4 px.

## 3. Geometry
- Frame 0 (6.30): the page fills the frame with the Recommendation 7 heading near the top third (matches the zoom-through tile fill colour of g-a6-board-r7 for one frame, then the page resolves, 0.3 s).
- Slow push on the page, scale 1.00 to 1.06 over the whole window (linear is fine under 1.5x), centred on the clause (b) passage.
- Five underlines on clause (b), each drawn left to right in 0.5 s (strokeDashoffset, dash length `ceil(len)+1`): U1 "new and existing", U2 "multi-family residential buildings", U3 "mercantile buildings", U4 "schools", U5 "buildings with assembly occupancies". Each underline sits under its own words only.
- Chip "RECOMMENDATION 7": glass chip (tokens.md surface) top-left title zone, left 96, top 80, row-value tier.
- Source line "NIST Sec. 5.2.2, Recommendation 7": bottom-left, left 96, bottom 60, source credit grey `#c8d3e0`, 19 to 22 px.
- Exit: page card slides out `x:980, autoAlpha:0, 0.6, power3.in` from 17.20, gone by 17.80 (the Walmart refuge photograph sits under the cut).

## 4. Must be true in the picture
1. The page shown is NIST NCSTAR 3 Sec. 5.2.2 Recommendation 7, and the underlined words match R3's text letter for letter.
2. Underlines land in the narration's order: apartments (U2), stores (U3), schools (U4), crowds (U5), new and existing (U1 last, on "new").
3. No underline crosses a word outside its phrase; no chip or source line sits on the underlined passage.
4. Nothing in x >= 1600, y >= 680.

## 5. Panel text and cues (a6-s1.words.json)
| Element | Exact text | Cue (word @ start s) |
|---|---|---|
| Page resolves, push starts | page render | "NIST" @ 6.30 |
| Chip | RECOMMENDATION 7 | "asked" @ 6.76 |
| U2 | (page words) multi-family residential buildings | "apartment" @ 8.24 |
| U3 | mercantile buildings | "stores," @ 9.44 |
| U4 | schools | "schools," @ 10.24 |
| U5 | buildings with assembly occupancies | "places" @ 11.18 |
| (N10 slot, held) | located in tornado hazard areas | "tornado" @ 12.92 (only once released) |
| U1 | new and existing | "new" @ 15.08 |
| Source line | NIST Sec. 5.2.2, Recommendation 7 | with the chip, "asked" @ 6.76 |
| Exit | none | 17.20 to 17.80 ("The" @ 17.80 is the Walmart photo) |
Between 12.92 and 15.08 the push keeps moving (no idle over 4 s).

## 6 to 8
Template §6 to §8, COMPID `g-a6-doc-rec7`.
