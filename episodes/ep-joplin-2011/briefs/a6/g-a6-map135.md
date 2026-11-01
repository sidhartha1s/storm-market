# g-a6-map135 · DEEP (Opus 5.5, high; a state of the master map) · after the CCTV clip, 5.0 s

Open numbers: none used.
Base: the master map of Joplin (first appearance T1-S2, the lit 135-dot state built for I1-S9; `briefs/intro/`). Copy that state; do not redraw dots, outlines or the "below ground" line. The dot positions come from the base, which is built from NIST Table 4-3.
Full-frame graphic. No narration: it follows the CCTV clip (its own sound), after a6-s7's last word. It closes act a6; the chapter blackout into Z1 follows (hand-placed).

## 0. Claim
Most of the people the tornado took were inside buildings.

## 1. Source
- T3, NIST NCSTAR 3 E.4.2 Finding 40: "Of the 155 impact-related fatalities, 135 (87 percent) involved persons who are known to have been located inside structures during the tornado."
- T11 (computed from Table 4-3 rows): 135 inside structures, 19 outside, 154 total (the base the map's dots are placed from; CONFLICT note in facts.md: a Table 4-3 graphic says 154, not 155).

## 2. Datum, scale, orientation
As the master-map base (its north, scale and city outline). No change.

## 3. Geometry
- Frame 0: the I1-S9 lit state as built, with these two changes only: the 19 outside dots at opacity 0.3, the 135 inside dots at full strength.
- Motion: the 135 inside dots breathe (scale 1 to 1.15 to 1, 1.6 s, stagger by distance from the map centre, finite repeats over the window) plus a slow pull-out 1.00 to 0.96 (linear) so the whole case board is in frame.
- Chip (glass chip, row-value tier): "MOST WERE INDOORS", top-left title zone, left 96, top 80.
- Source line: "NIST Finding 40", bottom-left, left 96, bottom 60, `#c8d3e0`, 19 to 22 px.
- No number on screen (the chip is plain words), so no base conflict on screen. No labels other than the base's own.
- Exit: the comp ends on the hand-placed chapter blackout (fade to black 0.6 s in its last 0.6 s); nothing vanishes mid-frame.

## 4. Must be true in the picture
1. 135 dots inside building outlines at full strength and 19 outside at 0.3; no dot added, moved or removed relative to the base.
2. Inside dots visibly outnumber outside dots (135 vs 19) at a glance.
3. The chip carries no number.
4. If any dot, label or outline is in x >= 1600, y >= 680, the presenter circle is off for this comp (tell the orchestrator); never move a dot to clear the corner.

## 5. Panel text and cues
No narration over this comp, so cues are anchored on the last spoken word plus the CCTV clip's length (set at sourcing): t0 = a6-s7 "empty." @ 9.76 + the EMPTY chip hold + the CCTV clip's duration, as mounted in index.html.
| Element | Exact text | Cue (host-local s) |
|---|---|---|
| Map in on the cut from the CCTV clip | none | 0.0 (= t0) |
| Outside dots dim to 0.3 (0.6 s) | none | 0.3 |
| Chip + source line | MOST WERE INDOORS / NIST Finding 40 | 1.0 |
| Breathe and pull-out continue | none | 1.0 to 4.4 |
| Fade to the chapter blackout | none | 4.4 to 5.0 |
Z1-S1 mounts the same master map about 30 s later: its mount carries `data-callback`, and this comp's chip text must not repeat on Z1's chips.

## 6 to 8
Template §6 to §8, COMPID `g-a6-map135`.
