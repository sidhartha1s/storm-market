# g-intro-3-coast: the coast side, tide and LaGuardia (I1-S1)
Builder: Opus 5.5, high effort. Depth: deep. Read `references/mg-quickref.md`, `learnings/mg.md`, then this brief.
Start from: `compositions/g-intro-2-hookmap.html` once built (same basemap, projection, pin and label styles; prefix `ic3-`). If it is not built yet, start from `library/inhouse/master-map-us-canada.html` with the styles in `briefs/intro/g-intro-2-hookmap.md` §3.
Sits over: nothing. Full-frame designed map on track 2. Its frame 0 equals g-intro-2-hookmap's last frame (camera frame D). Presenter circle may run from here: keep x >= 1600, y >= 680 free of labels, numbers and highlighted shapes.
Footage branch: LaGuardia footage is SOURCE TBD. If the sourcing lane lands a usable LaGuardia flood clip (provenance row read, 1950, public domain or licensed), this comp ends at I1-S1 5.22 (after the shore beat) and the clip plus `g-intro-4-lga-chip` carry the LaGuardia beat. Build the full fallback below either way; the orchestrator trims the host.

## 0. Claim
On the coast side, the wind drove the tide in until the New Jersey shore flooded, and in New York the water broke through the dikes at LaGuardia Airport onto the runways. Loop L1 stays closed: no track, no low, no wind arrows.

## 1. Source
- `research/nws-facts.md` §1: NCEI "onshore winds along the coast caused extreme high tides and flooding in New Jersey and Connecticut"; JKL "The resulting coastal flooding breached dikes at LaGuardia Airport in New York flooding runways." Fact-check intro-r2 rows 18, 19, 20.
- No source gives flood extent, depth or the 1950 runway layout. Everything drawn for extent and runways is SCHEMATIC and is labelled so.

## 2. Datum, scale, orientation
North up. Projection as g-intro-2: map x = 3841 × (lon + 97.576), map y = -5585 × (lat - 46.6213).
Map units: Newark (89893.2, 32871.1), LaGuardia (91039.4, 32641.0), Sandy Hook (90555.4, 34410.9), Atlantic City (88931.1, 40530.3), Cape May (87075.5, 42927.4).
Camera frames:
- D (start): s 0.04024, top-left (59078.1, 18954.6): Newark (1240, 560), Pittsburgh (340, 626).
- E (shore): s 0.06, top-left (74893.2, 26537.8): Newark (900, 380), LaGuardia (969, 366), Sandy Hook (940, 472), Atlantic City (842, 840), Cape May (731, 983).
- G (LaGuardia): s 0.25, top-left (87599.4, 30481.0): LaGuardia (860, 540), Newark (573, 598).
D to E is a 1.5x push (linear is fine); E to G is a 4.2x push: `logZoom` from `library/inhouse/snippets/helpers.js`.

## 3. Geometry (px)
- Basemap, pins, labels: as g-intro-2 §3. Pittsburgh pin and label fade out during the D to E push (they leave frame). Newark keeps its blue pin and "NEWARK" label (label left of pin).
- Tide line (frame E): a polyline in map units that follows the New Jersey Atlantic coastline from Sandy Hook to Cape May, offset 40 map units seaward (trace the basemap's own coastline vertices between those two points; do not invent a coast). Stroke `#7fb2e5` 3 px non-scaling, plus a second softer stroke 10 px at 0.25 opacity. It starts 25 px seaward of the coast (screen) and pushes onto the coast: `to` a translate of about 25 px westward (screen) over 1.0 s, power2.out.
- Shore flood fill: a band 12 px wide (screen, at frame E) on the land side of the same coastline, `#5a768f` at 0.55 with a 45-degree hatch `#7fb2e5` at 0.35; it grows south from Sandy Hook to Cape May (clip rect or strokeDashoffset on a thick stroked path, 1.2 s, power2.inOut). This band is SCHEMATIC (no source gives extent); keep it narrow.
- Chip "SHORE FLOODED" (glass chip as g-intro-2, Arial Black 900 52 px `#f2f5f8`) in the ocean, in open ocean east of the coast between Sandy Hook and Atlantic City: box x 1000 to 1500, y 590 to 670 at frame E (above the circle corner x >= 1600, y >= 680, and at least 60 px from the coastline).
- LaGuardia pin (frame G): core 18 px `#7fb2e5`, ring 34 px, label "LAGUARDIA AIRPORT" Arial 700 26 px `#dfe7ee` with the dark stroke, right of the pin.
- Runway inset (fallback only; the basemap is too coarse to show runways): a glass card 560 x 360 px at x 1000 to 1560, y 230 to 590 (clear of the circle corner), leader line 2 px `#93a3b2` from the card's left edge to the LaGuardia pin ring. Inside: two crossing runway strips 400 x 34 px and 300 x 34 px, `#2a3644` with `#93a3b2` 2 px edges, at 45 and 135 degrees, crossing near the centre; a shoreline curve along the card's top edge (water above it). Water fill `#5a768f` at 0.6 spreads from the shoreline down across the strips (clip-path or scaleY from the top edge, 1.3 s, power2.inOut). A small label under the card's lower edge, inside it: "SCHEMATIC, NOT TO SCALE" Arial 700 19 px `#93a3b2` tracking 2. No runway numbers, no headings (the 1950 layout is not sourced).
- Chip "DIKES BREACHED · LAGUARDIA" (glass, Arial Black 900 40 px `#f2f5f8`) centred under the inset card at y 630 to 700, x about 980 to 1580 (keep right edge at or left of 1590).
- Scan line as g-intro-2 for the whole comp.
- Type tiers: big 52 ("SHORE FLOODED"), mid 40 ("DIKES BREACHED · LAGUARDIA", too wide at 52 for the 600 px under the inset) and 26 (labels), small 19 (inset label).

## 4. Must be true in the picture
1. Frame 0 equals g-intro-2-hookmap's last frame (frame D, same pins, labels, colours, scan line position aside).
2. L1: no track, arrow, low symbol, isobar or wind vector anywhere; the tide line follows the coast only.
3. The tide line and flood band follow the real New Jersey coastline from the basemap's own vertices (Sandy Hook at (940, 472) to Cape May at (731, 983) in frame E, ±10 px).
4. Every invented extent or layout is labelled "SCHEMATIC, NOT TO SCALE" (the inset); the shore band is narrow and claims no depth.
5. One chip at full opacity at a time; "SHORE FLOODED" is gone before the LaGuardia chip lands.
6. Nothing with text or a highlight sits in x >= 1600, y >= 680 in any frame (the "SHORE FLOODED" chip sits at y 590 to 670).
7. Connecticut flooding is not drawn (narration names New Jersey and New York only).

## 5. Panel text (exact) and cues
Text strings: `NEWARK` · `SHORE FLOODED` · `LAGUARDIA AIRPORT` · `SCHEMATIC, NOT TO SCALE` · `DIKES BREACHED · LAGUARDIA`
Cues from `audio/i1-s1.words.json` (seconds from the segment start = comp-local seconds; host starts on I1-S1 audio start):
- 0.00 "On": frame D, held from the hook; pins pulse every 1.4 s. `/* ON @0.00 */`
- 0.26 "coast": push D to E (1.1 s, power2.inOut), Pittsburgh pin and label out during it. `/* COAST @0.26 */`
- 2.12 "drove": tide line in and pushes onto the coast (to 3.20). `/* DROVE @2.12 */`
- 4.06 "shore": flood band grows south (1.2 s). `/* SHORE @4.06 */`
- 4.36 "flooded.": chip "SHORE FLOODED" in (`fromTo` autoAlpha 0, y 20 to 0, 0.4 s, back.out(1.4)). `/* FLOODED @4.36 */`
- 5.22 "In": chip "SHORE FLOODED" out (0.35 s); push E to G (logZoom, 1.4 s, expo.inOut), "NEWARK" label fades during the push. [Footage branch: host ends at 5.60 with a fade-through instead.] `/* IN NEW YORK @5.22 */`
- 6.64 "broke": LaGuardia pin and label in (after the push settles at 6.62). `/* BROKE @6.64 */`
- 7.34 "dikes": inset card slides in (`fromTo` x 120 to 0, autoAlpha, 0.6 s, power3.out), leader line draws (strokeDashoffset, 0.4 s); chip "DIKES BREACHED · LAGUARDIA" in at 7.60. `/* DIKES @7.34 */`
- 8.88 "ran": water spreads across the strips (to 10.16 "runways."). `/* RAN @8.88 */`
- 10.16 to end: hold with a 1.5 % slow drift of the inset water edge (sine yoyo) and the scan line; then inset and chip exit (`to` x 980, autoAlpha 0, 0.6 s, power3.in) anchored to the host's last 0.6 s.
Host: data-start = I1-S1 audio start, duration = 10.427 + the gap to I1-S2 (default 0.40) = 10.83 s. g-intro-5-inland opens on its own frame (H), so this comp ends on its exit, not on a shared frame.

## 6-8
Contract, tools, done line, receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line item 3: capture this host's first frame next to g-intro-2-hookmap's last frame and state that they match.
