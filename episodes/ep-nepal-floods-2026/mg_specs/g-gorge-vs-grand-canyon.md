# BRIEF — g-gorge-vs-grand-canyon · section I inset (map beat) · right-third depth comparison

## 0. What this graphic claims
The Kali Gandaki gorge (river to the Dhaulagiri summit beside it) is about 18,000 ft, roughly three times the
depth of the Grand Canyon (rim to river, about 6,000 ft). One fact: the ratio.

## 1. SOURCE
factcheck-A #3: gorge 5,571 m = 18,278 ft (river-to-summit relief, Wikipedia: Kali Gandaki Gorge); Grand Canyon
max depth 6,000 ft rim-to-river (Grand Canyon NPS). 18,278/6,000 = 3.046 (python-checked), stated in the script
and brief as "about 18,000 ft" / "three times the depth" / "about 6,000 ft". NOTE (factcheck-A "other issues" #4):
the two figures use different reference conventions (peak-to-river vs rim-to-river) — not a true apples-to-apples
canyon "depth". Label the card SCHEMATIC in spirit by keeping both bars captioned with what they actually measure
("SUMMIT TO RIVER" / "RIM TO RIVER"), never just "DEPTH", so the comparison stays honest on screen.

## 2. DATUM, SCALE, ORIENTATION
Right third of frame only (a map sits left, per script "g-map-kali-gandaki full" is the base layer). Stage = right
640px (x 1280-1920). Baseline (river/rim-bottom line) at y 900, both bars grow UP from that baseline. Scale: 620px
= 18,278 ft -> 33.921 px per 1,000 ft (python-checked). Two bars side by side, 140px wide, gap 80px: Kali Gandaki
bar left edge x 1360, Grand Canyon bar left edge x 1580.

## 3. GEOMETRY (px; hit within +/-10px)
- Baseline line at y 900, x 1300-1900, 2px #2a3644.
- Kali Gandaki bar: x 1360-1500, bottom y 900, height 620px (top y 280) -> grows scaleY 0->1 from baseline.
  Label above bar top: "~18,000 FT" Arial Black 30px #7fb2e5, at (1360, 250). Sub-label under baseline:
  "KALI GANDAKI · RIVER TO SUMMIT" 19px #93a3b2 at (1300, 916), wraps to 2 lines within 220px.
- Grand Canyon bar: x 1580-1720, bottom y 900, height 203px (top y 697) -> grows scaleY 0->1 from baseline.
  Label above bar top: "~6,000 FT" Arial Black 30px #e8c56a at (1580, 667). Sub-label under baseline:
  "GRAND CANYON · RIM TO RIVER" 19px #93a3b2 at (1560, 916), wraps to 2 lines within 220px.
- Ratio tag: "3X DEEPER" Arial Black 44px #d0121f popfig-style at (1360, 500), appears after both bars settle.
- Both sub-labels' lowest text line must stay above y=1026 (54px bottom safe margin).

## 4. MUST BE TRUE IN THE PICTURE
1. Kali Gandaki bar height is ~3.05x the Grand Canyon bar height (620px vs 203px, ratio 3.05 measured).
2. Both bars share the same baseline y=900 and grow from it (never centered independently).
3. Kali Gandaki bar carries "SUMMIT TO RIVER"; Grand Canyon bar carries "RIM TO RIVER" — the two conventions are
   named on screen, never both captioned just "DEPTH".
4. Whole graphic sits entirely in x >= 1280 (right third); nothing left of x 1280 so the map beneath reads clearly.
5. No text inside the presenter keep-out (x>=1600 y>=680) — the ratio tag and both bars sit above y=680 or left of
   x=1600; verify sub-labels (y~916, below 680) stay left of x=1600 (they do: rightmost sub-label ends x=1780,
   BUT that is inside keep-out x-range; since keep-out is a screen corner reserved for Paul who is NOT on screen in
   this MG-only inset per mg-quickref ("in a motion-graphics-only scene... he is not shown"), this is acceptable —
   flag in receipt as a judgment call, not a strict violation, since the beat is graphics-only per script's own
   "I" b-roll framing (Lallantop/muted footage, no presenter cut named).

## 5. PANEL TEXT (exact) and CUES (175 wpm from beat start; beat = "The Kali Gandaki runs south...")
"~18,000 FT" · "KALI GANDAKI · RIVER TO SUMMIT" · "~6,000 FT" · "GRAND CANYON · RIM TO RIVER" · "3X DEEPER".
Cues (s): baseline draws 0.2 · Kali bar grows 2.0 /* CUE "eighteen thousand feet" @est 7.54 — bar lands slightly
ahead of the spoken number so the figure confirms what's already drawn, per "reveal on the spoken word" but the
BAR itself is the diagram element, label text lands ON the cue */, label "~18,000 FT" @est 7.54 · Canyon bar grows
8.0, label "~6,000 FT" @est 10.29 /* CUE "three times the depth" @est 10.29 */ · ratio tag "3X DEEPER" 10.8
/* CUE "Grand Canyon" @est 12.34 */ · hold to 13.5 · exit 13.9-14.5. Duration 14.5s declared.

## 6. CONTRACT
Standard contract. Root transparent (map sits below on a lower track). `data-composition-id="g-gorge-vs-grand-canyon"`,
timeline at `window.__timelines["g-gorge-vs-grand-canyon"]`. Prefix ids `gc-`.

## 7. TOOLS
Standard gate commands, run with the rest of the episode's comps.

## 8. RECEIPT
See builder's final message.
