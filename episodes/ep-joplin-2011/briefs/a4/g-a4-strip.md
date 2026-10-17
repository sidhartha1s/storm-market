# BRIEF · g-a4-strip · "what most of the big stores had instead of a basement" · map push-in · DEEP (Opus 5.5, high)

Episode ep-joplin-2011, act A4, segment A4-S1. Full-frame MG (no footage under it). Opens the act after the A3→A4
chapter blackout (0.6 to 0.9 s, DESIGN.md "Editing grammar"), so frame 0 is a fresh picture, not a continuation.
Base: MASTER MAP (first built for T1-S2; `_list.md` "Shared bases"). Copy it, add the layers below, add no geography.
Exemplar for the push-in and the labels fitted to real landmarks: `references/editing-patterns/ep3-map-route-fit.html`.
Open numbers: none drawn. Store positions come from the base (`_list.md` Open 3).

## 0. What this graphic claims
The big stores on the 20th Street and Range Line Road strip had a refuge area set aside inside them, not a basement.
Two stores carry it: the Walmart (refuge area: the "Site-to-Store" or layaway area, B5) and the Home Depot (refuge
area: the training room, B11). Most big-box stores had designated refuge areas (B2); only a few non-residential
buildings had a basement (B1); the Walmart had none (B8).

## 1. SOURCE
- B2 "Most high-occupancy commercial and critical facilities surveyed by NIST ... (SJRMC, schools, and big-box stores) had in-facility designated refuge areas for tornadoes." NIST E.4.2 Finding 21.
- B1 "Only a few non-residential buildings were equipped with underground locations (e.g., basements)". Finding 20.
- B5 Walmart: "the 'Site-to-Store' or layaway area, which served as the main refuge area". Sec. 1.2.
- B11 Home Depot: "took refuge in the training room located at the back of the store". Sec. 1.2.
- B16 the district: "Businesses in the area included AT&T, Pizza Hut, Macadoodles, Walmart, and Home Depot." Sec. 1.2.
- Geography: the MASTER MAP base's own traced source. Nothing here moves a street or an outline.

## 2. DATUM, SCALE, ORIENTATION
- The base's projection, north-up, and its px-per-mile at the city framing. The push-in is a uniform scale about the
  strip's centre; no rotation. State the end scale factor in the receipt.
- Start framing: the base's city view with the commercial strip lit (the state A3-S11 ends on), so the viewer recognises it after the blackout.
- End framing: the 20th Street / Range Line Road junction centred at (900, 560); the Walmart and Home Depot outlines both
  fully inside x 160 to 1500, y 160 to 860. The presenter circle stays on (graphics-only scene): nothing in x ≥ 1600, y ≥ 680.

## 3. GEOMETRY
- Push-in: `logZoom` (`library/inhouse/snippets/helpers.js`) from the city framing to the end framing; it is well over 1.5x.
- Outline highlight: the Walmart and Home Depot outlines from the base take a 4 px stroke `#f2f5f8` and a fill `rgba(242,245,248,.10)`.
- Refuge marker, one per store: a 22 px diameter filled circle, amber `#d8a13a`, with a 2 px ring that pulses (finite
  repeats) out to 44 px, at the centroid of that store's outline. A centroid, not a side of the building: the map does
  not say where in the store the area was (the floor plans in `g-a4-walmart` and `g-a4-homedepot` do that, schematically).
- Labels, diagram-label tier (tokens.md), each on the open side of its outline, never on a street line or the other
  outline: "WALMART · REFUGE AREA" and "HOME DEPOT · REFUGE AREA". Street labels "20TH ST" and "RANGE LINE RD" come
  from the base; keep them, unchanged.
- Source line bottom-left (x 96, baseline 1026), small tier `#c8d3e0`: "NIST Finding 21 · Sec. 1.2".

## 4. MUST BE TRUE IN THE PICTURE
1. Exactly two refuge markers, each inside its own store's outline; no marker on any other building.
2. No basement or below-ground symbol on either store.
3. Both store labels read and touch no street line, no outline but their own, and not each other.
4. The geography at the end frame is the base's, unmoved: 20th Street and Range Line Road cross where the base puts them.
5. The presenter corner (x ≥ 1600, y ≥ 680) holds no label, marker or highlighted outline at any frame.

## 5. PANEL TEXT (exact) and CUES
Text: "WALMART · REFUGE AREA" · "HOME DEPOT · REFUGE AREA" · source "NIST Finding 21 · Sec. 1.2".
Cues (`_list.md` "Cue notation"):
- frame 0: city framing, strip lit (map ground on from frame 0).
- push-in a4-s1 "Stick" 0.00 → "explain" 2.14 (logZoom, power2.inOut).
- outlines brighten a4-s1 "most" 3.02.
- Walmart marker + label a4-s1 "big" 3.68; Home Depot marker + label a4-s1 "stores," 3.84 + 0.3 s.
- source line a4-s1 "instead" 4.46.
- markers keep pulsing; the map drifts (scale +1 %) to the end.
- host ends at a4-s1 "and" 5.88: a straight cut to the Range Line corridor clip (`_list.md`: S1 clip window). The map
  ends on a cut while it drifts, never a single element vanishing mid-frame.

## 6 to 8. Contract, tools, done line, receipt
`references/mg-brief-template.md` §6 to §8 verbatim, COMPID `g-a4-strip`. Comp-specific: host on the picture track,
nothing under it; the base's ids are re-prefixed `a4s-` so they do not collide with other map copies.
