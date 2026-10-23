# g-a6-siren · STANDARD (Sonnet 5.5, high) · a6-s5 9.86 to a6-s6 14.56

Open numbers: N8 ("2018", "NIST TN 2008"): chips "STILL NONE AS OF 2018" and source chip "NIST TN 2008" are held; their slot is fixed below.
Base: the siren icon drawn for I1-S2 (`briefs/intro/`), one icon, enlarged. Copy its SVG; do not redraw.
Full-frame graphic (cuts in from the West Tower photograph at s5 9.86).

## 0. Claim
In 2011 there was no national standard for sounding outdoor sirens, and no national all-clear protocol.

## 1. Source
- S34, NIST NCSTAR 3 E.4.2 Finding 39: "Across the country, there is no standard method for sounding outdoor public siren systems, which has led to variations in siren usage, activation procedures, and sounding patterns among U.S. communities."
- R24, same Finding 39: "Also, there are no nationally accepted standard protocols for the issuance of an all-clear alert following a warning." (Narration only; no chip in the Picture line.)
- facts.md NOTE under section R: Finding 39 speaks for 2011; whether a standard exists today is not in these sources (hence N8 held).

## 2. Datum, scale, orientation
Icon centred at (640, 500), 360 px tall. Three sound arcs to its right, radii 220, 300, 380 px from the horn mouth, Body light `#dfe7ee` 4 px. Chip column left edge x 1060.

## 3. Geometry
- Siren icon: the I1-S2 glyph scaled to 360 px tall, Headline white strokes.
- Arcs: pulse outward one after another (scale 0.9 to 1.05, autoAlpha 0.9 to 0, 1.2 s, stagger 0.4, finite repeats covering the window); this is the continuous motion. On "standard" the arcs desynchronise (each arc's repeat delay jittered by 0.15 to 0.45 s, fixed values, no random) to read as "no one pattern".
- Chip 1 (glass chip, row-value tier): "NO NATIONAL STANDARD · 2011", left x 1060, centre y 420.
- Held slot (N8): chip 2 at left x 1060, centre y 500 ("STILL NONE AS OF 2018"), source chip 3 below it at y 560 ("NIST TN 2008", small tier). Empty until released.
- Source line: "NIST Finding 39", bottom-left, left 96, bottom 60, `#c8d3e0`, 19 to 22 px.
- Corner x >= 1600, y >= 680: empty (chips end above y 600).
- Exit: icon and chips slide out `x:980, autoAlpha:0, 0.6, power3.in` from 13.96; gone by 14.56, cut to g-a6-doc-nwsrec2.

## 4. Must be true in the picture
1. One siren icon, the same glyph as I1-S2.
2. "2011" appears once, on chip 1 only.
3. No "2018" or "TN 2008" text while N8 is open.
4. No chip under an arc: arcs stay left of x 1040.
5. Nothing in x >= 1600, y >= 680.

## 5. Panel text and cues
| Element | Exact text | Cue (segment, word @ start s) |
|---|---|---|
| Icon in (scale 0.8 to 1, 0.5 s, back.out), arcs start | none | a6-s5 "sirens?" @ 9.86 |
| Arcs keep pulsing | none | a6-s6 "In" @ 0.00 |
| Chip 1 | NO NATIONAL STANDARD · 2011 | a6-s6 "standard" @ 2.54 |
| Arcs desynchronise | none | a6-s6 "sounds" @ 3.78 |
| Source line | NIST Finding 39 | a6-s6 "standard" @ 2.54 |
| Arcs dim to 0.4 (no all-clear chip) | none | a6-s6 "all" @ 6.40 |
| (slot 2, held N8) | STILL NONE AS OF 2018 | a6-s6 "2018," @ 10.44, only once released |
| (slot 3, held N8) | NIST TN 2008 | a6-s6 "2018," @ 10.44, only once released |
| Exit | none | a6-s6 13.96 to 14.56 ("The" @ 14.56) |
Words.json writes "veteran" @ 8.94 where the script says "federal": no cue uses it.

## 6 to 8
Template §6 to §8, COMPID `g-a6-siren`.
