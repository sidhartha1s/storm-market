# g-a5-map-sjrmc · A5-S4 · DEEP (Opus 5.5, high or above) · copy of the master-map base

Open numbers: St. John's position on the map (no coordinates in facts.md; it comes from the master-map base, traced from NIST Fig 4-23). Destinations of the seven moved patients: not in facts.md, so no destination is drawn.
Copy the master-map base (first drawn at I1-S2; id in `briefs/i1/_list.md`) to `compositions/g-a5-map-sjrmc.html`. Keep the base's city, path, dots and palette as they are; add only the layers below. The St. John's outline is already lit when A4-S14 ends ("St. John's outline lights on the master map"): open on that state.
**Host start = a5-s4 6.60** (after g-a5-cc-standing exits), duration 12.00 s (wav 18.00 + 0.60 tail).

## 0. Claim
The towers stood, but twelve people who had been inside St. John's were lost to the storm's impact; four were in intensive care, and seven of the twelve were moved to other hospitals and were lost there, later.

## 1. Source
- C1: "Twelve impact-related fatalities occurred in the hospital, four of which involved patients in intensive care units" (Finding 42).
- C3: "four of the five [who died at SJRMC on May 22] were patients located in ICUs" (Sec. 4.6.2.1).
- C5 / C6: "seven people were injured at the hospital, but died in other health care facilities days, weeks, or months later"; Table 4-3 footnote f counts them at St. John's.
- C2: 14 at St. John's counting all causes (Table 4-1, Sec. 1.2). On the source line only, per the hospital CONFLICT (facts.md line 277).
- 12 - 7 = 5 (computed, python): the five lost at St. John's on 22 May.

## 2. Datum, scale, orientation
The base's datum, scale and north. Camera: from the base's view push to St. John's (logZoom if over 1.5x) so the outline spans about 520 px wide, its centre at x 760, y 520 (left of centre, so the chips have the right side clear of the corner).

## 3. Geometry
- 12 dots in the base's death-dot style, inside the St. John's outline, a 4 x 3 grid with 44 px pitch centred on the outline. SCHEMATIC: Table 4-3 places them at the hospital, not at a room.
- The 4 ICU dots: four of the five dots that stay solid (grid row 1). One bracket over those four, one label `ICU` (diagram label 22 px `#93a3b2`) above the bracket.
- The 7 lost-later dots: the other seven; they stay inside the outline (Table 4-3 counts them at St. John's) and turn hollow (fill 0, 3 px ring). One short arrow (120 px, `#93a3b2`) from the group's east edge outward, no arrowhead label, no destination.
- Chips in the base's map rail (the base names where map numbers ride; quickref: no popfig over a map comp). If the base has no rail: chip at left 1080, top 300, then the second chip under it at top 400. Both left of x 1600.
- Source line bottom-left.

## 4. Must be true in the picture
1. Exactly 12 dots; count them on the frame.
2. The four ICU dots are among the five solid dots, never among the seven hollow ones (12 - 7 = 5 >= 4).
3. The seven hollow dots stay inside the St. John's outline.
4. "14" appears only on the source line, never as a chip or a dot count.
5. The towers outline stays intact (the towers did not collapse, C1): no collapse animation on the outline.
6. Nothing at x >= 1600, y >= 680.

## 5. Panel text and cues
| element (exact text) | cue |
|---|---|
| camera push to St. John's | a5-s4 6.60 to "took"@7.28 |
| 12 dots land (stagger 0.05 s) | a5-s4 "12"@7.48 |
| chip `12 FROM THE STORM` | a5-s4 "12"@7.48 |
| source line `12 impact-related · Finding 42 · Table 4-3 · 14 all causes · Table 4-1` | a5-s4 "12"@7.48 |
| ICU bracket + label `ICU` | a5-s4 "Four"@10.12 |
| arrow draws from the group of seven | a5-s4 "moved"@13.16 |
| chip `7 LOST LATER, ELSEWHERE` (first chip stays, second stacks under it) | a5-s4 "Seven"@12.36 |
| seven dots turn hollow | a5-s4 "lost"@14.86 |
| labels and chips fade, camera eases toward the West Tower side of the outline | a5-s4 "What"@16.46 to 18.00 |
Motion: dot pulse (scale 1 -> 1.08, 1.2 s, finite repeats) after each landing so nothing idles 4 s.

§6 to §8: `references/mg-brief-template.md`; shared rules `_list.md`.
