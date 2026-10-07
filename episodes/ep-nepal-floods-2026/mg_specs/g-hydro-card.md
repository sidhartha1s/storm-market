# BRIEF, g-hydro-card · section A1, "Three seconds" (1:52) · RHS panel over Republic World footage

## 0. What this graphic claims
The Kaligandaki A plant (144 MW, largest in Nepal when it opened in 2002) powers roughly 120,000 US-scale homes;
the flood shut it down. Two facts: 144 MW, and its US-home equivalent.

## 1. SOURCE
factcheck-A #7: 144 MW installed capacity confirmed (Wikipedia: Kaligandaki A). Conversion: 144 * 8,760 h/yr *
1,000 / 10,500 kWh (EIA avg US household) = 120,137, "about 120,000 homes" (python-checked), corrected from an
earlier "100,000" draft. factcheck-A #16: the plant's own stated shutdown reason is precautionary (river running
high), not silt damage, the card must not show a silt/blade-damage visual, only a plain power-meter fall.

## 2. DATUM, SCALE, ORIENTATION
RHS panel, right:0 top:0 bottom:0 width:820px, padding 90px 96px 0 170px (mg-quickref RHS stat panel spec). No
map; a vertical power meter (dial or bar) at top, a house-icon grid below, both inside the panel column
(x 170-720 within the 820px panel).

## 3. GEOMETRY (px; hit within +/-10px)
- Headline top 130: "144 MW" 'AbrilFig' popfig 100px #d0121f (3 words-or-fewer figure, per popfig rule), sub
  "KALIGANDAKI A · LARGEST IN NEPAL, 2002" 19px #93a3b2 at top 250.
- Power meter: a vertical bar x 170-210, top 320, height 200px (bottom y 520), fill color #7fb2e5 draining
  (scaleY 1->0, transform-origin bottom) to visualise the shutdown; label beside it "OUTPUT" 19px #93a3b2 at
  (230, 400), "0 MW" landing after the drain at (230, 430) Courier 26px #e74c3c.
- House-icon grid: 10 columns x 12 rows = 120 small house glyphs (each a roof+box glyph, 20x17px), starting at
  x 170 top 580, filling left-to-right/row-by-row as a counter climbs; grid width 320px, height 302px (python
  checked against the panel_left=1100 + left=170 + grid_w constraint so the grid's right edge lands at abs x=1590,
  10px clear of the presenter keep-out at x>=1600, see MUST-BE-TRUE #5 below, this replaced an earlier 12x10/26px
  layout whose right edge reached abs x=1648, INSIDE the keep-out, caught in self-review before any gate ran).
  Each icon represents 1,000 homes (SCHEMATIC, 120 icons x 1,000 = 120,000, not a literal count).
- Counter "120,000" Courier 84px #e74c3c at top 902, label "AMERICAN HOMES, ROUGHLY" 20px #c8d3e0 at top 996.
  "Roughly" label prevents the exact-120,137 vs shown-120,000 mismatch from reading as a false-precision claim.

## 4. MUST BE TRUE IN THE PICTURE
1. "144 MW" is the FIRST number on screen (popfig), before the meter drains or the house grid appears.
2. The power meter drains to a labelled "0 MW", no silt/blade damage imagery (factcheck-A #16 correction).
3. The house-icon grid fills as (or just before) the "120,000" counter lands, never after, the grid is the
   visual payoff the counter confirms.
4. Counter reads "120,000" (rounded), labelled "roughly", never the unrounded 120,137, never the earlier
   incorrect "100,000".
5. No text inside the presenter keep-out (x>=1600 y>=680): panel is x 1100-1920, but every element's right edge
   is checked and kept at or left of abs x=1590 (10px margin), the house grid is the tightest fit, confirmed by
   python computation, not eyeballed.

## 5. PANEL TEXT (exact) and CUES (175 wpm from beat start; beat = "Downstream, the river feeds...")
"144 MW" · "KALIGANDAKI A · LARGEST IN NEPAL, 2002" · "OUTPUT" / "0 MW" · house grid (120 icons, no text per icon)
· "120,000" · "AMERICAN HOMES, ROUGHLY".
Cues (s): panel in 0.0 · "144 MW" popfig 0.6 /* CUE "largest in Nepal" @est 4.11, the "144 megawatts" figure
itself is spoken later in the beat's second sentence per script order; popfig lands on the plant's introduction
since the number is stated in the narration line just before this beat's cue window opens (script line: "It makes
enough power for roughly one hundred and twenty thousand American homes" follows "144 megawatts" in the prior
clause, the 144 MW popfig lands with the plant's naming, ~0.6s in, ahead of the counter) */ · meter drains
2.0-3.2 · house grid fills 5.5-9.0 /* CUE "one hundred and twenty thousand American homes" @est 9.60 */ · counter
climbs 7.5-9.6, lands with the grid · hold to 11.5 · exit 11.9-12.5. Duration 12.5s declared.

## 6. CONTRACT
Standard contract. `data-composition-id="g-hydro-card"`, timeline at `window.__timelines["g-hydro-card"]`.
Prefix ids `hc-`.

## 7. TOOLS
Standard gate commands.

## 8. RECEIPT
See builder's final message.
