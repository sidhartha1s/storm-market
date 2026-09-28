# BRIEF — g-himlung-height · section I, WION avalanche clip (peak) · two-bar height comparison

## 0. What this graphic claims
Himlung Himal (23,379 ft) stands about 3,000 ft taller than Denali (20,310 ft), the tallest US mountain. One
fact: the gap.

## 1. SOURCE
factcheck-A #8: Himlung 7,126 m = 23,379 ft (Madison Mountaineering); Denali 6,190 m = 20,310 ft (USGS official via
Madison Mountaineering). 23,379 - 20,310 = 3,069 ft (python-checked), matches "roughly three thousand feet."

## 2. DATUM, SCALE, ORIENTATION
Left-of-frame VE overlay (footage: WION avalanche clip, peak shot) — glass card lower-left is too small for two
tall bars, so this is a bare (no card backing) HUD diagram over the footage per mg-quickref "text lives on a
fixed HUD layer"; bars themselves need no glass, only their labels do (small label chips). Baseline (sea level) at
y 940, both bars grow up from it. Scale: 560px = 23,379 ft -> 0.023953 px/ft (python-checked). Bars at x 200
(Himlung) and x 460 (Denali), each 160px wide, gap 100px.

## 3. GEOMETRY (px; hit within +/-10px)
- Baseline "SEA LEVEL" line at y 940, x 140-780, 2px #2a3644, label "SEA LEVEL" 19px #93a3b2 at (140, 950).
- Himlung bar: x 200-360, bottom y 940, height 560px (top y 380). Label above: "HIMLUNG HIMAL" Arial Black 30px
  #7fb2e5 at (200, 330); figure "23,379 FT" Courier 26px #dfe7ee at (200, 360).
- Denali bar: x 460-620, bottom y 940, height 487px (top y 453). Label above: "DENALI" Arial Black 30px #e8c56a
  at (460, 403); figure "20,310 FT" Courier 26px #dfe7ee at (460, 433).
- Gap bracket: a small horizontal bracket between the two bar tops (y 380 to y 453, at x 400-420), label
  "~3,000 FT TALLER" 22px #93a3b2 tracking 3, positioned at (640, 400), pointing left to the bracket.
- All labels sit above y=680 or left of x=1600 (presenter keep-out); this diagram occupies x 140-780, y 330-960 —
  fully clear of the keep-out zone regardless of whether Paul appears.

## 4. MUST BE TRUE IN THE PICTURE
1. Himlung bar is taller than Denali's, ratio ~1.15:1 (560px vs 487px), matching 23,379/20,310 = 1.151.
2. Both bars share the same sea-level baseline (y=940) and grow from it.
3. The gap bracket sits between the two bar TOPS only (y 380-453), never spanning the full bar heights.
4. Each bar's figure label uses its real elevation in feet, never a rounded "23,000" that contradicts the
   spoken "twenty three thousand four hundred."
5. No text inside the presenter keep-out (x>=1600 y>=680) — diagram is entirely left of x=780, trivially clear.

## 5. PANEL TEXT (exact) and CUES (175 wpm from beat start; beat = "Up north, the same weather...")
"SEA LEVEL" · "HIMLUNG HIMAL" / "23,379 FT" · "DENALI" / "20,310 FT" · "~3,000 FT TALLER".
Cues (s): baseline 0.2 · Himlung bar grows 2.0, labels land /* CUE "twenty three thousand four hundred feet"
@est 6.86 */ · Denali bar grows 7.2, labels land /* CUE "three thousand feet higher than Denali" @est 9.60 */ ·
gap bracket + tag 10.0 · hold to 12.0 · exit 12.4-13.0. Duration 13.0s declared.

## 6. CONTRACT
Standard contract. Root transparent (footage on a lower track). `data-composition-id="g-himlung-height"`,
timeline at `window.__timelines["g-himlung-height"]`. Prefix ids `hh-`.

## 7. TOOLS
Standard gate commands.

## 8. RECEIPT
See builder's final message.
