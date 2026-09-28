# BRIEF — g-search-card · section A3, "Base camp" (6:09) · glass card over WION rescue footage

## 0. What this graphic claims
Sixteen workers were at Himlung base camp; four were found by Sept 28, twelve still missing; searchers dug through
snow about 15 ft deep. Two facts carry it: the search numbers, and the snow depth against a human scale.

## 1. SOURCE
factcheck-D #3: "Total at base camp: 16... By 28 Sept 2026: 4 recovered... 12 still missing. No survivors
reported... rescuers quoted saying survival is very unlikely given 15+ feet of snow." Script A3: "a ground team...
dug through snow about fifteen feet deep. Sixteen workers had been at the camp. By the twenty eighth, the
searchers had found four, and twelve were still missing."

## 2. DATUM, SCALE, ORIENTATION
Glass card, NOT the full RHS panel — a mid-lower card per mg-quickref "lower-third" zone, left 96px, bottom 110px
anchor (tokens.md lower-third convention), width 760px, so the snow-depth diagram can sit beside it in the
card's own body rather than needing the full 820px RHS rail. Card top calculated from its height (below). Scale
for the snow/human diagram: 220px = 15 ft -> 14.667 px/ft (python-checked); human silhouette 88px = 6 ft (same
scale), baseline shared.

## 3. GEOMETRY (px; hit within +/-10px)
- Card: left 96, width 760, bottom 110 (so top = 1080-110-card_height; card_height 520px -> top 450). Glass surface
  per tokens.md (rgba(10,16,24,.55), blur 18px saturate 1.15, border rgba(255,255,255,.14), radius 28), padding
  50px 60px.
- Row 1 top 40 (within card): "16" Courier 60px #dfe7ee inline + "AT BASE CAMP" 19px #93a3b2.
- Row 2 top 120: "4" Courier 60px #7fb2e5 inline + "FOUND · SEPT 28" 19px #93a3b2.
- Row 3 top 200: "12" Courier 60px #e74c3c inline + "MISSING" 19px #93a3b2.
- Snow-depth mini-diagram, right side of the card body, x (card-local) 480-720, baseline y (card-local) 460:
  human silhouette bar 30px wide, height 88px (6 ft), at x 480; snow-depth bar 30px wide, height 220px (15 ft), at
  x 560, both growing UP from the shared baseline. Label above snow bar: "~15 FT SNOW" 19px #93a3b2 at (555, 220).
  Label above human bar: "6 FT" 16px #93a3b2 at (475, 352) (16px is the named cite-card-style exception floor —
  actually this is NOT a cite card, so keep it at 19px minimum per the TV-readability floor; use 19px, not 16px).

## 4. MUST BE TRUE IN THE PICTURE
1. Rows land in the order 16 -> 4 -> 12 (base camp total first, then found, then still missing), matching the
   script's own sentence order.
2. "4" is colored to read as the positive/found figure (blue #7fb2e5), "12" as the danger/missing figure
   (#e74c3c) — never both the same color, never swapped.
3. Snow bar is materially taller than the human silhouette (220px vs 88px, ratio 2.5), both sharing one baseline.
4. Snow bar and human silhouette sit inside the card, never floating separately over the footage without the
   glass backing (mg-quickref: no bare text/diagram on moving footage).
5. No text inside the presenter keep-out (x>=1600 y>=680) — card right edge is x=856, fully clear.

## 5. PANEL TEXT (exact) and CUES (175 wpm from beat start; beat = "A helicopter reached the camp...")
"16" / "AT BASE CAMP" · "4" / "FOUND · SEPT 28" · "12" / "MISSING" · "~15 FT SNOW" · "6 FT".
Cues (s): card in 0.0 · row "16" 2.5 /* CUE "Sixteen workers had been at the camp" @est 8.91 — row reveals ahead
of its own cue is wrong per doctrine; correct to row 1 landing AT 8.91, see note below */. Corrected order (the
snow-depth line is spoken BEFORE the headcount in the script): snow/human diagram in 0.5, snow bar grows
1.0-3.0 /* CUE "snow about fifteen feet deep" @est 7.20 */ (bar grows across the words leading to the cue, landing
on it) · row 1 "16" 7.6 /* CUE "Sixteen workers had been at the camp" @est 8.91 */ · row 2 "4" 13.2 /* CUE "found
four" @est 13.71 */ · row 3 "12" 14.3 /* CUE "twelve were still missing" @est 14.74 */ · hold to 16.5 · exit
16.9-17.5. Duration 17.5s declared.

## 6. CONTRACT
Standard contract. `data-composition-id="g-search-card"`, timeline at `window.__timelines["g-search-card"]`.
Prefix ids `sc-`.

## 7. TOOLS
Standard gate commands.

## 8. RECEIPT
See builder's final message.
