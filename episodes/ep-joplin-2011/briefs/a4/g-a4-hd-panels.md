# BRIEF · g-a4-hd-panels · "63 of 73 wall panels collapsed" · glass label over the site aerial · STANDARD (Sonnet 5.5, high)

Episode ep-joplin-2011, act A4, segment A4-S5 (its last sentence and question). Overlay on the glass card, over footage:
the DVIDS Home Depot site aerial (sourcing pick c5, `a4-s5_c5_dvids-homedepot-site-aerial.mp4`, trimmed to about 4 to
26 s of the cut; the Picture line's "CLIP NEEDED: moving footage of the Home Depot site with its wall panels down"),
mounted by the orchestrator from a4-s5 "The" 21.80 to the segment end.
Why here and not on the still: the Picture line puts this label on the NIST photo, but the photo has only a4-s5 0.00 to
4.56 and the comment card fills that (`g-a4-comment`). Over the moving site footage the label gets 4 s to read. The
orchestrator may move it back.
Exemplar: `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` (glass card over footage, big figure).
Open numbers: none.

## 0. What this graphic claims
Of the Home Depot's 73 concrete wall panels, 63 collapsed and 10 stayed standing. Unspoken: the narration is on the
tornado's centre line here, so the label is the quiet second fact under the picture.

## 1. SOURCE
- B13 "In total, 63 of the 73 wall panels collapsed either inward or outward, leaving 10 standing after the storm." NIST Sec. 4.6.2.1 (Home Depot).

## 2. DATUM, SCALE, ORIENTATION
- Glass card (tokens.md surface) left 96, bottom 96, width 760, height 300; nothing in the presenter corner (x ≥ 1600, y ≥ 680).
- Tick strip: 73 ticks, 6 px wide, 9 px pitch = 654 px wide (computed by script), x from card-left + 52, at card-top + 200, 40 px tall.

## 3. GEOMETRY
- Eyebrow "HOME DEPOT" (tokens.md eyebrow, 22 px) at card-top + 40.
- Big line "63 of 73" (Arial Black 900, 72 px, `#f2f5f8`) at card-top + 70; sub "wall panels collapsed" (mid tier, 30 px,
  `#dfe7ee`) beside or under it, inside the card.
- Ticks: all 73 start standing (`#dfe7ee`, 40 px tall). 63 of them fall: each `rotation 0 → 90`, `transformOrigin:
  "bottom center"`, colour to crimson `#8e2020`, staggered left to right over 1.4 s. The last 10 stay standing white.
  The strip is a count, not a map of the building: print no wall names on it.
- Source (small tier, 19 px `#c8d3e0`) inside the card at card-bottom − 24: "NIST Sec. 4.6.2.1".

## 4. MUST BE TRUE IN THE PICTURE
1. 73 ticks in total; after the fall, 63 down and 10 standing (count by script on the DOM).
2. "63 of 73" and the sub line read as one sentence: "63 of 73 wall panels collapsed".
3. No tick or text leaves the card; no label of a direction or a wall.
4. The site footage beneath is not covered at its centre: the card stays in the lower-left third.

## 5. PANEL TEXT (exact) and CUES
Text: "HOME DEPOT" · "63 of 73" · "wall panels collapsed" · "NIST Sec. 4.6.2.1".
Cues (`_list.md` "Cue notation"):
- card in (`x -660 → 0`, 0.7 s, power3.out) a4-s5 "tornado" 22.24; big line + sub a4-s5 "center" 22.52.
- ticks fall a4-s5 "passed" 22.88 → 24.28.
- hold with a 3 px float on the card; card out (`x → -980, autoAlpha 0, 0.6, power3.in`) from a4-s5 "What" 26.64.
  Host ends a4-s5 "What" 26.64 + 0.6 s.

## 6 to 8. Contract, tools, done line, receipt
`references/mg-brief-template.md` §6 to §8 verbatim, COMPID `g-a4-hd-panels`. Comp-specific: overlay comp, transparent
root; the done-line frame is composited over the c5 clip at a4-s5 25.0 s, and the clip under every second of the label is
the Home Depot site by its `provenance.csv` row (it names the store, so 7a.7 applies).
