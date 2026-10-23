# BRIEF · g-a4-churches · "Three women were lost there, and four more" · two glass chips · STANDARD (Sonnet 5.5, high)

Episode ep-joplin-2011, act A4, segment A4-S11. Overlay on the glass card, over footage.
Footage under it (orchestrator's mount): the Harmony Heights Baptist still, then the Full Gospel Church site still, cut on
a4-s11 "and" 15.14. **[BLOCKED on owner]** for the footage only: no lawful ground photo of either church exists; the
sourcing candidates are NOAA aerials centred on a geocoded address, building not confirmed
(`media/candidates/a4/candidates.md`, picks c1 and c2). A chip saying "3 LOST" over a lot that may not be the church is
a claim about that picture (mg-brief-template 7a.7). The chips below do not change whatever the owner picks.
Exemplar: `references/editing-patterns/ep5-glass-stat-panel.html` (glass card, big figure, source line).
Open numbers: none.

## 0. What this graphic claims
Three women were lost at Harmony Heights Baptist, and four people at the Full Gospel Church: seven in the two churches.

## 1. SOURCE
- B36 "Three women died in this building during the May 22, 2011, Joplin tornado, all from impact-related injuries." NIST Sec. 4.4.5.
- B45 Table 4-3: "Full Gospel Church 4 ... Harmony Heights Baptist Church 3".
- B39 "places of worship (the Full Gospel Church and Harmony Heights Baptist Church) where a total of 7 died" Sec. 4.4 (Table 4-1). Per the facts.md CONFLICT note, 7, never B50's 8.

## 2. DATUM, SCALE, ORIENTATION
One glass card (tokens.md surface), left 96, top 680, width 520, height 260; it stays in the lower-left so the still is
seen. Presenter corner (x ≥ 1600, y ≥ 680) clear.

## 3. GEOMETRY
- Card holds one figure at a time: "3 LOST", then "4 LOST" (big tier, 84 px Arial Black 900, `#e74c3c`), with the
  small-tier label under it: "HARMONY HEIGHTS BAPTIST", then "FULL GOSPEL CHURCH" (19 px Arial 700 `#93a3b2`, tracking 4).
  The church names sit inside the card as labels of the figure, not as captions on the still.
- The swap: "3 LOST" lifts out (`y → -30`, autoAlpha 0, 0.3 s) before "4 LOST" rises in (`fromTo y 24 → 0`, 0.4 s), on the cut.
- Source line inside the card, bottom (19 px `#c8d3e0`): "NIST Sec. 4.4.5 · 7 in churches per Table 4-1".

## 4. MUST BE TRUE IN THE PICTURE
1. "3 LOST" is on only over the Harmony Heights still; "4 LOST" only over the Full Gospel still.
2. The source line carries 7 (never 8).
3. The two figures are never on screen together.
4. The card covers no more than the lower-left of the still.

## 5. PANEL TEXT (exact) and CUES
Text: "3 LOST" · "HARMONY HEIGHTS BAPTIST" · "4 LOST" · "FULL GOSPEL CHURCH" · "NIST Sec. 4.4.5 · 7 in churches per Table 4-1".
Cues (`_list.md` "Cue notation"):
- card in (`x -660 → 0`, 0.7 s, power3.out) with "3 LOST" a4-s11 "Three" 13.44; label 13.64.
- swap to "4 LOST" + label a4-s11 "four" 15.46 (the cut to the second still is at "and" 15.14).
- source line a4-s11 "church." 16.60.
- hold with a 3 px float; card out (`x → -980, autoAlpha 0, 0.6, power3.in`) so the host ends a4-s11 "it?" 21.64 + 0.6 s.

## 6 to 8. Contract, tools, done line, receipt
`references/mg-brief-template.md` §6 to §8 verbatim, COMPID `g-a4-churches`. Comp-specific: overlay comp, transparent
root; do not start the build until the owner has ruled on the stills; the done-line frame is composited over each still.
