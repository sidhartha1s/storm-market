# BRIEF g-a3-map-ranch · A3-S10 (second sentence) + A3-S11 · DEEP (Opus 5.5, high effort) · on base `g-master-map`

Read first: `references/mg-quickref.md`, `learnings/mg.md`, `library/inhouse/snippets/tokens.md`. Base: `g-master-map` (copy its BASEMAP block verbatim, as in `g-a3-map-homes`). Overlay on top during a3-s11 0.00–4.90: `g-a3-counter` (glass card, top right).
Before this host: a3-s10's first sentence (0.00 → 5.10, "In the flattened houses where people got down to the basement, nobody was lost") plays over the basement-survivor clip, the Picture line's first choice. If sourcing finds none, the orchestrator decides that picture; this host still starts on "And".

**BLOCKED layer:** the ranch-home pocket. H15 says what it was, not where. The orchestrator supplies its location (a NIST figure or text) before the pocket layer is built. Build everything else first; the pocket layer is drawn only from a supplied source, never by eye.

## 0. What this graphic claims
A whole neighborhood of early-1980s ranch homes with basements took heavy damage and nobody there was lost (H15); and no one died in a demolished house where people had got down to the basement (H5). Then the turn to the stores: most big stores had a designated refuge area (B2) at 20th Street and Range Line Road (B16).

## 1. SOURCE
- H15, Sec. 1.2: "a residential neighborhood that comprised ranch-style homes, with basements, built primarily during the early 1980s. Although these homes were damaged significantly, no one was killed in this neighborhood."
- H5, Finding 46: "No fatalities occurred in demolished, detached homes in which people took refuge in basements."
- B16, Sec. 1.2: "The commercial district around this location included small stores, restaurants, and large chain stores." (20th Street and Range Line Road)
- B17, Sec. 1.2: "The center of the tornado passed just to the north of 20th Street between Walmart and Home Depot and very near to the Pizza Hut."

## 2. DATUM, SCALE, ORIENTATION
The base's projection, north-up, scale bar and street grid, unchanged; framing = the base's city view. Positions computed by script from the base's data and stated in the receipt.

## 3. GEOMETRY
- The 71 residential dots (59 house + 12 apartment, from g-a3-map-homes and g-a3-apartments) on at opacity .30.
- Pocket (BLOCKED, see above): the neighborhood's outline from the supplied source, stroke `#e8c56a` 2 px, fill rgba(232,197,106,.12), damage hatch (45° lines, `#e8c56a` at .35, 8 px apart) clipped to the outline. Diagram label 22 px `#93a3b2` next to it, outside the outline: "Ranch homes with basements · early 1980s".
- Chip (glass popup-chip, left 96, top 96): "BASEMENTS HELD" 52 px.
- Source line (glass source-label, left 96, baseline ≤ 1026, 20 px): "NIST Finding 46 · Sec. 1.2".
- 20th Street strip: the base's 20th Street segment around Range Line Road (the commercial district, B16; extent from the base's building layer, Walmart to Home Depot), glow stroke `#f5d98b` 6 px at .8 over the street line. Diagram label 22 px: "20th Street & Range Line Road", placed beside the strip, outside the counter card's box.
- While g-a3-counter is on (a3-s11 0.00–4.90): no label, dot cluster or chip of this comp in x ≥ 1100, y ≤ 560 (the card's area).
- Corner x ≥ 1600, y ≥ 680: no label.

## 4. MUST BE TRUE IN THE PICTURE
1. Zero dots inside the pocket outline (the 71 dots are where the earlier comps put them; none moves).
2. The pocket sits inside the damage path (it was "damaged significantly").
3. No shelter icon anywhere; no dot shown below ground.
4. The strip lies on 20th Street at Range Line Road, the tornado's centre line passing just north of it between Walmart and Home Depot (B17), per the base's street layer.
5. Only one chip at a time: "BASEMENTS HELD" is gone before the counter card enters.

## 5. PANEL TEXT (exact) and CUES (a3-s10 and a3-s11 words.json)
Text: "BASEMENTS HELD" · "Ranch homes with basements · early 1980s" · "NIST Finding 46 · Sec. 1.2" · "20th Street & Range Line Road".
Host: a3-s10 "And" @5.10 → a3-s11 "was." @6.08 + 1.0 (cut to the A4 chapter blackout).
- a3-s10 5.10 "And": city view on from frame 0 (71 dots at .30); source line in.
- a3-s10 5.74 "neighborhood": push toward the pocket (≤ 1.5x linear, else `logZoom`, 1.0 s); pocket outline draws on.
- a3-s10 7.06 "basements,": pocket fill in.
- a3-s10 8.70 "early": pocket label in.
- a3-s10 10.08 "hard,": damage hatch wipes in across the pocket (0.5 s).
- a3-s10 11.06 "nobody": chip "BASEMENTS HELD" in; pocket outline pulses once.
- a3-s10 end → a3-s11 0.00: chip out (0.4 s, ending before a3-s11 "Most" @0.00); pull back to the city view (1.0 s).
- a3-s11 0.88 "stores": strip glow draws along 20th Street (0.8 s), no label yet.
- a3-s11 5.12 "staff": strip label in (the counter has exited).
- Holds: dots blip (≤ 1.5 s apart), camera drift ≥ 6 px/s.

## 6–8. CONTRACT, TOOLS, DONE LINE, RECEIPT
`references/mg-brief-template.md` §6, §7, §7a and §8 unchanged, COMPID = `g-a3-map-ranch`, root id `g-a3-map-ranch-root`.
