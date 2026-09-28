# BRIEF, g-gorge-vs-grand-canyon · section I inset (map beat) · right-third depth comparison

## 0. What this graphic claims
The Kali Gandaki gorge (river to the Dhaulagiri summit beside it) is about 18,000 ft, roughly three times the
depth of the Grand Canyon (rim to river, about 6,000 ft). One fact: the ratio.

## 1. SOURCE
factcheck-A #3: gorge 5,571 m = 18,278 ft (river-to-summit relief, Wikipedia: Kali Gandaki Gorge); Grand Canyon
max depth 6,000 ft rim-to-river (Grand Canyon NPS). 18,278/6,000 = 3.046 (python-checked), stated in the script
and brief as "about 18,000 ft" / "three times the depth" / "about 6,000 ft". NOTE (factcheck-A "other issues" #4):
the two figures use different reference conventions (peak-to-river vs rim-to-river), not a true apples-to-apples
canyon "depth". Label the card SCHEMATIC in spirit by keeping both bars captioned with what they actually measure
("SUMMIT TO RIVER" / "RIM TO RIVER"), never just "DEPTH", so the comparison stays honest on screen.

## 2. DATUM, SCALE, ORIENTATION
Right third of frame only (a map sits left, per script "g-map-kali-gandaki full" is the base layer). Stage = right
640px (x 1280-1920). Baseline (river/rim-bottom line) at y 620 (REVISED in self-review from an initial y 900,
below), both bars grow UP from that baseline. Two bars side by side, 140px wide, gap 80px: Kali Gandaki bar left
edge x 1360, Grand Canyon bar left edge x 1580.

SELF-REVIEW FIX: an initial draft used baseline y=900 (bars grow up, sub-labels sit BELOW the baseline at
y~916). That put the Grand Canyon bar (which reaches up only to y~697) and its sub-label INSIDE the presenter
keep-out (x>=1600, y>=680): the canyon bar's own column sits at abs x 1580-1720, spanning y 697-900, and the
sub-label at abs y~916 crossed x=1600 too. Caught in self-review before any gate ran (mg-quickref "nothing enters
the corner x>=1600, y>=680" while Paul is on screen; this beat is a diagram inset over a map plus muted b-roll,
not a stated presenter-free MG scene, so the strict rule applies, not the "motion-graphics-only" exception).
FIX: moved the baseline to y=620 and both convention/figure labels to stack ABOVE each bar instead of below the
baseline, so the entire diagram (bars, baseline, both label stacks) sits above abs y=680, clearing the keep-out
regardless of x. Scale: kali bar 468px = 18,278 ft (python: 468/18.278 = 25.6 px per 1,000 ft, re-derived from the
new bar height, not the original 33.921 px/1,000ft figure, since the bar height itself changed to fit above y=680).

## 3. GEOMETRY (px; hit within +/-10px)
- Baseline line at y 620, x 1300-1900, 2px #2a3644.
- Kali Gandaki bar: x 1360-1500, bottom y 620, height 468px (top y 152) -> grows scaleY 0->1 from baseline.
  Figure label above bar top: "~18,000 FT" Arial Black 30px #7fb2e5, at (1430, 112), 6px gap above the bar top.
  Convention sub-label above the figure label: "KALI GANDAKI · RIVER TO SUMMIT" 19px #93a3b2 at (1320, 54), 2
  lines within 220px, 8px gap above the figure label.
- Grand Canyon bar: x 1580-1720, bottom y 620, height 153px (top y 467) -> grows scaleY 0->1 from baseline.
  Figure label above bar top: "~6,000 FT" Arial Black 30px #e8c56a at (1650, 427), 6px gap above the bar top.
  Convention sub-label above the figure label: "GRAND CANYON · RIM TO RIVER" 19px #93a3b2 at (1540, 369), 2 lines
  within 220px, 8px gap above the figure label.
- Ratio tag: "3X DEEPER" Arial Black 44px #d0121f popfig-style at (1550, 250), in the empty column above the
  Grand Canyon bar and below its own label stack (never over either bar), appears after both bars settle.
- Every element (bars, baseline, both label stacks, ratio tag) sits with its lowest edge above abs y=620,
  well clear of both the top-safe margin (y>=54) and the presenter keep-out (y>=680).

## 4. MUST BE TRUE IN THE PICTURE
1. Kali Gandaki bar height is ~3.05x the Grand Canyon bar height (468px vs 153px, ratio 3.06 measured, python
   checked, within the template's +/-10px tolerance of the confirmed 3.046 real-world ratio).
2. Both bars share the same baseline y=620 and grow from it (never centered independently).
3. Kali Gandaki bar carries "SUMMIT TO RIVER"; Grand Canyon bar carries "RIM TO RIVER", the two conventions are
   named on screen, never both captioned just "DEPTH".
4. Whole graphic sits entirely in x >= 1280 (right third); nothing left of x 1280 so the map beneath reads clearly.
5. No element (bar, label, ratio tag) has any part at abs y>=680: every top/height value above was computed so the
   lowest point in the whole diagram is the baseline at y=620, 60px clear of the keep-out threshold, verified by
   python arithmetic, not by eye.

## 5. PANEL TEXT (exact) and CUES (175 wpm from beat start; beat = "The Kali Gandaki runs south...")
"~18,000 FT" · "KALI GANDAKI · RIVER TO SUMMIT" · "~6,000 FT" · "GRAND CANYON · RIM TO RIVER" · "3X DEEPER".
Cues (s): baseline draws 0.2 · Kali bar grows 2.0 /* CUE "eighteen thousand feet" @est 7.54, bar lands slightly
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
