# BRIEF — g-pore-pressure · A2 full mechanism · grains, water, friction vs weight, slip

## 0. Claim
A slope stands because friction between soil grains resists the weight pulling it down. Rain fills the
gaps between grains and pushes them apart (pore pressure); once pore pressure climbs enough, friction
drops below weight and the slope slips. Build the mechanism; the label "pore pressure" names it only
when the voice says the word (text doctrine).

## 1. SOURCE
factcheck-B row 7 (CONFIRMED): USGS "Regulation of landslide motion by dilatancy and pore pressure
feedback"; American Geosciences Institute — water separates grains, raises pore pressure, cuts friction,
slope fails once it crosses the Mohr-Coulomb threshold. No published diagram traced; grain packing and
the friction/weight bars are SCHEMATIC, NOT TO SCALE.

## 2. DATUM, SCALE, ORIENTATION
- Stage 1920x1080. Left: cross-section box (x 96-1020, y 260-940) containing ~30 grain circles (r 22-30px)
  in a loose packed grid. Right: a two-bar "friction vs weight" gauge (x 1200-1500, y 260-900), gridline
  at y 900 = ground/zero.
- Ground line y = 940 (the slope's toe/base, below the grain box).

## 3. GEOMETRY (px)
- Grain box outline dashed #4a5560, grains #5a768f fill, #7fb2e5 stroke, packed with ~8px gaps.
- Water fill: rect clipped to the grain box, rises from y 940 (empty) to y 320 (near full), #1d3b57 -> #7fb2e5
  gradient at 55% opacity, scaleY tween from the bottom.
- 6 small outward arrows (svg paths, #d0121f) seeded among the grains at mid-height, appearing once water
  passes their row, pushing grains apart (grains nudge +/-6px on x as arrows fire).
- Friction bar: rect x1220 y(dynamic)-900 w90, starts full height (y260-900), amber #d8a13a, shrinks
  (scaleY 1->0.35, transformOrigin bottom) as pore pressure climbs.
- Weight bar: rect x1360 y(fixed)620-900 w90, danger red #e74c3c, static height (the pulling weight never changes).
- Slip mark: once friction bar's top (y) drops below the weight bar's top (y620), the whole grain box
  shears (skewX ~8deg + x:-40) to show the slope giving way.
- Label "PORE PRESSURE" (diagram label tier, #93a3b2, tracking 3) appears at (760,220), pointing at the
  water fill, ONLY at the cue where the voice says "Geologists call that pore pressure."

## 4. MUST BE TRUE
1. Water fill height increases monotonically; never exceeds the grain box (y>=320 never less, i.e. stays within 260-940).
2. The 6 push-arrows only appear after the water level has reached their row (no arrow fires before its water contact).
3. Friction bar height only decreases (or holds); weight bar height is constant throughout.
4. The "PORE PRESSURE" label is invisible until the exact cue and then stays through the rest of the comp — never appears before the word is spoken.
5. The grain box visibly shears/slips ONLY after the friction bar's top has crossed above the weight bar's top (friction < weight).
6. Both bars, the grain box and the label sit inside the 96/54 px text-safe margin.

## 5. PANEL TEXT (exact) and CUES
Labels: "FRICTION" (amber bar top), "WEIGHT" (red bar top), "PORE PRESSURE" (water-fill pointer, cue-gated).
Headline (top-left, x96 y70): "Why a Soaked Slope Gives Way".
Cues (s, local @175wpm):
- headline @0.4
- grain box + bars draw in @1.0
- water begins rising @5.49 (`/* CUE "Rain fills the tiny gaps" @est 5.49 */`)
- push-arrows fire in sequence @8.0-10.8 (`/* CUE "pushes them apart from the inside" @est 10.5 */`)
- "PORE PRESSURE" label reveals @11.31 (`/* CUE "Geologists call that pore pressure" @est 11.31 */`)
- friction bar begins shrinking @13.03 (`/* CUE "the friction holding the slope drops" @est 13.03 */`)
- weight bar label pulses, grain box shears/slips @18.86 (`/* CUE "A soaked slope doesn't need the biggest storm" @est 18.86 */`)
- exit @27.0 (both halves slide out, power3.in)
Declared duration 29.5 s (narration ~28.11 s + ~1.4 s tail).

## QC fix log (self-audit, headless screenshot at t=12s)
1. `#pp-grains` (the parent `<g>`) was set `autoAlpha:0` at t=0 and never released — every grain circle
   was individually revealed but invisible inside a hidden parent. Fix: removed the parent from the
   initial hide list; each grain circle now carries its own `autoAlpha:0` set at t=0 instead.
2. `#pp-water` was authored `x=96 y=940 width=924 height=680` — a rect starting AT the box's bottom edge
   and extending 680px further DOWN (off-frame, y940-1620), so the "rising water" scaleY tween (anchored
   at the bottom via svgOrigin) had nothing visible to grow. Fix: rect now `y=260` (box top) `height=680`,
   so it fills the box exactly and scaleY from the bottom-anchored svgOrigin reveals it correctly.
