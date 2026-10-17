# BRIEF g-a3-counter · A3-S11 · STANDARD (Sonnet 5.5, high effort) · counter visit 1, BASE of the toll counter

Read first: `references/mg-quickref.md` ("RHS stat panel", "Motion and exits": counters), `learnings/mg.md`, `library/inhouse/snippets/tokens.md` (counter tier: Courier New 700 84 `#e74c3c`; counter label Arial 700 20 `#c8d3e0` tracking 6). Exemplars: `library/inhouse/examples/joplin-stat-panel.html`, `episodes/ep-nepal-floods-2026/compositions/g-toll-counter.html`.
Under it: `g-a3-map-ranch` (the master map; it keeps the card's area clear). Visits 2 (A4, structure.md: 102 of 135) and 3 (A5, 135 of 135) copy this file and change only the from/to values and the source line; build every value as its own text leaf so that is a text edit.

## 0. What this graphic claims
So far on the case board: 71 of the 135 people lost inside a building were at home, and none of those the investigators could place was below ground (H26, H19, T3/T11, H5/H6).

## 1. SOURCE
- 71: H26, Table 4-3, "Residences: apartments 12c Residences: homes (detached) 59d" (59 + 12 = 71), base 154 impact-related.
- 135: T11, Table 4-3 rows add to 154, 135 inside structures; T3, Finding 40: "Of the 155 impact-related fatalities, 135 (87 percent) involved persons who are known to have been located inside structures".
- Below ground: H5, Finding 46: "NIST found no evidence that any of those killed were located underground during the tornado." H6, Sec. 4.6.2.2: "NIST found no evidence that any fatalities occurred to individuals located below grade in this storm."
- Wording rule (edit_script header): "none found", never "nobody".

## 2. DATUM, SCALE, ORIENTATION
Overlay, transparent root, 1920 × 1080. Card anchored top right.

## 3. GEOMETRY
- Glass card (tokens "Surfaces"): right 96, top 96, width 640, padding 36 px, radius 28.
- Row 1: label "INSIDE A BUILDING" (counter label tier). Under it the counter "71" (Courier New 700, 84 px, `#e74c3c`) followed on the same baseline by " of 135" (Arial 700, 30 px, `#dfe7ee`).
- Divider: 1 px `rgba(255,255,255,.14)`, full card width, scaleX 0 → 1.
- Row 2: label "BELOW GROUND" (counter label tier); value "NONE FOUND" (Arial Black 900, 52 px, `#f2f5f8`).
- Source line inside the card, 19 px `#c8d3e0`: "NIST Table 4-3 · impact-related · Finding 46".
- Card bottom ≤ y 560. Nothing in x ≥ 1600, y ≥ 680.

## 4. MUST BE TRUE IN THE PICTURE
1. The counter ends exactly on 71 and its denominator reads 135; the count never passes 71.
2. "NONE FOUND" appears, never "0", "nobody" or "none".
3. "71" here and "71 LOST AT HOME" (A3-S8) are never on screen together (different scenes).
4. Three tiers: 84 (counter), 52 (NONE FOUND), 30 (" of 135"), plus the 19–20 px labels.

## 5. PANEL TEXT (exact) and CUES (a3-s11.words.json)
Text: "INSIDE A BUILDING" · "71" · " of 135" · "BELOW GROUND" · "NONE FOUND" · "NIST Table 4-3 · impact-related · Finding 46".
Host: a3-s11 "Most" @0.00 → "cover," @4.20 + 0.7 (about 5 s, as the Picture line asks).
- 0.00 "Most": card in (fromTo x 660 → 0, 0.7 s, power3.out); label row 1 at 0.3.
- 0.40 → 1.60: counter `to({v})` 0 → 71, power4.out, writing the leaf, opening on the first tick's value; " of 135" in at 0.4.
- 1.70: divider draws.
- 2.26 "didn't,": row 2 in (fromTo autoAlpha 0, y 24 → 0, 0.4 s); "NONE FOUND" lands with a small scale settle 1.06 → 1.
- 2.80: source line in.
- 2.8 → 4.3: card floats (y ±3 px).
- 4.30 → 4.90: card exits (to x 980, autoAlpha 0, 0.6 s, power3.in).

## 6–8. CONTRACT, TOOLS, DONE LINE, RECEIPT
`references/mg-brief-template.md` §6, §7, §7a and §8 unchanged, COMPID = `g-a3-counter`, root id `g-a3-counter-root`.
