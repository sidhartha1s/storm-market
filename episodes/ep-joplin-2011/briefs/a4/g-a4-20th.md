# BRIEF · g-a4-20th · "Was a cooler the wrong place to be, then?" · map with two cooler insets · DEEP (Opus 5.5, high)

Episode ep-joplin-2011, act A4, segments A4-S6 and A4-S7. Full-frame MG, no footage under it.
Base: MASTER MAP (first built for T1-S2; `_list.md` "Shared bases"). Copy it and add the layers below; add no geography.
The start framing matches `g-a4-strip`'s end framing, so the strip reads as the same place.
Exemplar for the pan along a real street and labels on landmarks: `references/editing-patterns/ep3-map-route-fit.html`.
Open numbers: positions (`_list.md` Open 3) come from the base. If the base has no Pizza Hut or Dillon's outline, or its
centre line breaks §4.1, stop and report: the fix is in the base, not here.
Photo note: no lawful ground photo of the Dillon's exists (`media/candidates/a4/candidates.md`); this comp needs none. If
the owner approves the NOAA stand-in aerial, the orchestrator mounts it as a cutaway from a4-s7 "if" 8.54 to "But" 12.80.

## 0. What this graphic claims
The tornado's centre passed just north of 20th Street, between the Walmart and the Home Depot and very near the Pizza
Hut. At the Pizza Hut, staff and customers got into the cooler; the building was demolished and five people were lost.
West along 20th Street at Connecticut, 35 people got into the Dillon's produce cooler; that building was demolished too,
and all 35 survived.

## 1. SOURCE
- B17 "The center of the tornado passed just to the north of 20th Street between Walmart and Home Depot and very near to the Pizza Hut." NIST Sec. 1.2.
- B19 "Around 5:38 p.m., the occupants heard the sirens sound a second time. Some ... discussed whether this was meant to signify an 'all-clear message.'" Sec. 4.4.8.
- B18 "employees and patrons of the Joplin Pizza Hut sought protection in the restaurant's cooler ... it completely demolished the structure. Five people died at the Pizza Hut (two employees and three customers)." Sec. 1.2.
- B20 "35 people took refuge inside the store's produce cooler. Even though the building was demolished, everyone inside the store survived with only minor cuts, bruises, or scratches." Sec. 1.2 (20th Street and Connecticut).
- W6 "a six-mile, roughly west-to-east path through Joplin" (NIST E.3): the centre line draws west to east.
- Geography: the MASTER MAP base's traced source.

## 2. DATUM, SCALE, ORIENTATION
- The base's projection, north-up. Start framing = `g-a4-strip`'s end framing (the 20th / Range Line junction at (900, 560)).
- Mid framing (A4-S7): the 20th Street / Connecticut junction centred at (700, 560). Pan along 20th Street. If the pan is
  more than 1.5 frame widths, it is a `logZoom` pull-out then push-in, not a long flat slide; state which in the receipt.
- Inset frame (both coolers, one at a time): x 1180 to 1560, y 160 to 540, `#15202b` fill, 2 px `#93a3b2` border,
  joined by a 2 px leader line to the lit building. Text rail: bottom-left, x 96 to 1100, y 820 to 960. Presenter corner
  (x ≥ 1600, y ≥ 680) stays clear (graphics-only scene, the circle stays on).

## 3. GEOMETRY
- Centre line: the base's tornado centre line, 5 px, Danger red 2 `#e74c3c`, drawn west to east by `strokeDashoffset`;
  label "TORNADO CENTER" (diagram-label tier) north of the line, clear of every outline and street label.
- Lit buildings: Walmart and Home Depot outlines at 0.6 (context); Pizza Hut, then Dillon's, at full stroke `#f2f5f8` with
  fill `rgba(242,245,248,.10)`, each labelled "PIZZA HUT" / "DILLON'S" on its open side.
- "Demolished": the lit outline splits into its segments, each drifting 6 to 14 px in a seeded direction with a small
  rotation, and its fill drops to 0. One move, no rubble particles.
- Pizza Hut inset: a walk-in cooler door in elevation (frame 220 x 300, door 180 x 270, long vertical handle, two
  hinges, label "COOLER" above it). The door closes (a `scaleX` swing from its hinge side, 0.5 s). No figures: no row gives
  how many were inside the Pizza Hut cooler.
- Dillon's inset: a cooler room box 320 x 220, label "PRODUCE COOLER" above it; 35 figures (14 x 30 px person glyphs,
  `#dfe7ee`) on a 7 x 5 grid at 40 px pitch, filing in from the box's door side with a stagger. The box itself never
  breaks: no row says how the cooler stood.
- Rail chips (Arial Black 900, `#f2f5f8` unless noted): "5 LOST" (big tier, 72 px, `#e74c3c`); "35 IN THE COOLER · ALL
  SURVIVED" (mid tier, 40 px). Source line bottom-left (x 96, baseline 1026): "NIST Sec. 1.2 · Sec. 4.4.8" (A4-S6), then
  "NIST Sec. 1.2" (A4-S7).

## 4. MUST BE TRUE IN THE PICTURE
1. The centre line runs just north of 20th Street, passes between the Walmart and Home Depot outlines, and passes very near
   the Pizza Hut outline; it draws from west to east.
2. One inset at a time. The Pizza Hut inset shows a door and no people; the Dillon's inset shows exactly 35 figures (count by script).
3. "5 LOST" is on only while the Pizza Hut is the lit building; "35 IN THE COOLER · ALL SURVIVED" only while the Dillon's is.
4. The pan follows 20th Street from the Range Line junction to the Connecticut junction as the base draws them.
5. No basement, stair or below-ground element.
6. Every leader line joins its own inset to its own building; no label sits on the centre line or a street.
7. Nothing in the presenter corner.

## 5. PANEL TEXT (exact) and CUES
Text: "TORNADO CENTER" · "PIZZA HUT" · "COOLER" · "5 LOST" · "DILLON'S" · "PRODUCE COOLER" · "35 IN THE COOLER · ALL
SURVIVED" · "NIST Sec. 1.2 · Sec. 4.4.8" · "NIST Sec. 1.2".
Cues (`_list.md` "Cue notation"):
- frame 0: ground on at the start framing, Walmart and Home Depot outlines at 0.6.
- centre line draws a4-s6 "That" 0.56 → "538." 2.04; "TORNADO CENTER" label 2.04.
- Pizza Hut lights + label a4-s6 "Some" 3.42; slow push (scale +4 %) runs 3.42 → 7.02 so nothing idles.
- inset in with its leader + door open a4-s6 "Staff" 7.02; door closes a4-s6 "cooler." 8.20; source line 7.02.
- Pizza Hut outline breaks a4-s6 "demolished" 9.78; "5 LOST" a4-s6 "five" 10.90.
- hold with a 3 px float on the inset; inset, leader and chip out a4-s7 0.00 → "At" 0.46.
- pan to 20th and Connecticut a4-s7 "At" 0.46 → "store," 1.60; Dillon's lights + label a4-s7 "Dillon's" 1.04 (it is
  on screen by then) and settles by 1.60.
- Dillon's inset in a4-s7 "35" 2.46; figures file in "got" 2.96 → "cooler," 3.86.
- Dillon's outline breaks a4-s7 "demolished" 5.28.
- "35 IN THE COOLER · ALL SURVIVED" a4-s7 "All" 6.70; source line switches 6.70.
- hold with figure floats and a slow push to the end (no gap ≥ 4 s); fade-through over the last 0.6 s; host ends
  a4-s7 "basement?" 14.12 + 0.8 s.

## 6 to 8. Contract, tools, done line, receipt
`references/mg-brief-template.md` §6 to §8 verbatim, COMPID `g-a4-20th`. Comp-specific: the base's ids re-prefixed `a420-`.
