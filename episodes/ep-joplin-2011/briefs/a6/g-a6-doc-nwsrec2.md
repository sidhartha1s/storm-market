# g-a6-doc-nwsrec2 · STANDARD (Sonnet 5.5, high) · a6-s6 14.56 to a6-s7 0.00

Open numbers: none used.
Base: the document page with underline first used at A1-S6 (`briefs/a1/`), the same treatment as g-a6-doc-rec7. Copy it.
Full-frame graphic. Asset: a render of the NWS Central Region Service Assessment page carrying Recommendation #2 (NOAA, public domain), from sourcing, capped at 1920 x 1080. No NWS logo crop issue: frame the page text, not the cover.

## 0. Claim
The Weather Service asked for impact-based, tiered warnings and a non-routine warning for strong and violent tornadoes.

## 1. Source
- R21, NWS Assessment Recommendation #2: "This evolution should utilize a simple, impact-based, tiered information structure that promotes warning credibility".
- R22, NWS Assessment Recommendation #2 (item b): "provide a non-routine warning mechanism that prompts people to take immediate life-saving action in extreme events like strong and violent tornadoes (finding 2d)."

## 2. Datum, scale, orientation
The page render is the datum (underlines measured on it). Body text at least 26 px tall on screen. Underline 6 px, 4 px under the baseline, glyph run ±4 px, as the base.

## 3. Geometry
- Frame 0: the page, Recommendation #2 heading in the upper third, the R21 sentence and item b both in frame (if they do not fit at 26 px, the camera pans down from the R21 sentence to item b between 19.0 and 19.8, and no underline draws during the pan).
- Slow push 1.00 to 1.05 across the window (linear).
- Underlines, each left to right in 0.5 s: U1 "impact-based", U2 "tiered information structure", U3 "non-routine warning mechanism", U4 "strong and violent tornadoes".
- Chip (glass chip, row-value tier): "STRONG AND VIOLENT TORNADOES · NWS REC. 2", top-left, left 96, top 80.
- Source line: "NWS Assessment, Recommendation 2", bottom-left, left 96, bottom 60, `#c8d3e0`, 19 to 22 px.
- Exit: page slides out `x:980, autoAlpha:0, 0.6, power3.in` in the last 0.6 s before a6-s7 0.00 and at least 1.0 s after the chip lands.

## 4. Must be true in the picture
1. The page is the NWS Assessment's Recommendation #2; underlined words match R21 and R22 letter for letter.
2. Underlines land in the narration's order (U1, U2, U3, U4).
3. Chip and source line sit off the underlined passage.
4. Nothing in x >= 1600, y >= 680.

## 5. Panel text and cues (a6-s6.words.json)
| Element | Exact text | Cue (word @ start s) |
|---|---|---|
| Page in, push starts | page render | "The" @ 14.56 |
| Source line | NWS Assessment, Recommendation 2 | "NWS" @ 14.72 |
| U1 | (page words) impact-based | "impact" @ 16.96 |
| U2 | tiered information structure | "tears," @ 18.52 (whisper's spelling of "tiers") |
| U3 | non-routine warning mechanism | "out" @ 20.10 |
| U4 | strong and violent tornadoes | "strong" @ 22.10 |
| Chip | STRONG AND VIOLENT TORNADOES · NWS REC. 2 | "tornadoes." @ 23.06 |
| Exit | none | last 0.6 s before a6-s7 "The" @ 0.00 |

## 6 to 8
Template §6 to §8, COMPID `g-a6-doc-nwsrec2`.
