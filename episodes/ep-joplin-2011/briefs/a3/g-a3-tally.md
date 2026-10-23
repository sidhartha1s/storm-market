# BRIEF g-a3-tally · A3-S5 · STANDARD (Sonnet 5.5, high effort)

Read first: `references/mg-quickref.md`, `learnings/mg.md`, `library/inhouse/snippets/tokens.md`. Exemplars: `library/inhouse/numbers-rollup.html` (counts and source close), official `stagger-lattice` (`npx hyperframes catalog --query "stagger lattice"`) for the pip grid.
After this host: the survivor clip (closet, hallway or bathroom, in their own voice), an insert the orchestrator mounts.

**Open (left out of the drawing):** where the 27th survivor was. The Picture line says "1 crawl space"; that comes from factcheck-A1-A3, not facts.md. 27 − 11 − 15 = 1 is computed from H13 and H14, so the pip is drawn, grey and unlabelled. The tally line "· 1 crawl space" is not shown.

## 0. What this graphic claims
Of the 27 survivors NIST talked to from single-family homes in the EF-4 zone, 11 were in basements; 15 rode it out in interior first-floor spaces: 3 closets or laundry areas, 5 hallways, 7 bathrooms (H13, H14).

## 1. SOURCE
- H13, Sec. 4.6.2.2: "NIST spoke with 27 such individuals. Of these 27, 11 took shelter in basements (full or partial, located in newer homes)."
- H14, Sec. 4.6.2.2: "The rest of the 27 individuals (total of 15) survived while located in internal spaces on the first floor of their home, including in internal closets or laundry areas (3 people), internal hallways (5 people), or internal bathrooms (7 people)."
- Computed: 3 + 5 + 7 = 15; 27 − 11 − 15 = 1.

## 2. DATUM, SCALE, ORIENTATION
Full frame, ground per tokens "Canvas". **Grade line y = 620**, full width, `#93a3b2` 2 px, diagram label "Ground" at (110, 606). Earth below as in g-a3-house-section (`#2a3644` → `#04070c`). One pip = one person.

## 3. GEOMETRY
- Pip: person icon 36 × 48 px (head circle + body), fill `#d8a13a` at opacity .55 until sorted.
- Start grid: 3 rows × 9, columns x = 708 + 56·i (i 0–8), row tops y 150, 214, 278.
- Basement bin (below grade): x 300–860, y 660–900, stroke `#93a3b2` 2 px; the 11 pips sit in 2 rows (6 + 5). Count "11" 52 px Arial Black 900 `#f2f5f8` at (890, 740); name "Basement" 30 px Arial 700 `#dfe7ee` at (890, 784).
- Interior bins (above grade, first floor): three boxes y 470–590: closet x 940–1200, hallway x 1220–1480, bathroom x 1500–1760. Pips in 2 rows. Above each box at baseline y 455, 22 px `#93a3b2`: "Closet, laundry · 3", "Hallway · 5", "Bathroom · 7". Group label "Inside, first floor · 15" 30 px `#dfe7ee` at (940, 410).
- The 27th pip stays in its grid slot, recoloured `#4a5560`, no label.
- Chip (glass popup-chip, left 96, top 96): "27 SURVIVORS" 52 px. Eyebrow under it at (96, 200), 22 px `#93a3b2` tracking 6: "EF-4 zone · single-family homes".
- Source line (glass source-label, left 96, baseline ≤ 1026, 20 px): "NIST Sec. 4.6.2.2".
- Corner x ≥ 1600, y ≥ 680: earth only.

## 4. MUST BE TRUE IN THE PICTURE
1. 27 pips in all at every frame after "27"; none appears twice, none vanishes.
2. Exactly 11 pips below the grade line, all inside the basement bin; exactly 3 / 5 / 7 in the closet / hallway / bathroom bins, all above the grade line.
3. Exactly 1 pip unsorted, grey, unlabelled. No text says "crawl space".
4. Counts on screen: 27, 11, 3, 5, 7, 15 only; the bins' pip counts equal their labels.
5. The basement bin is visibly below ground and the interior bins visibly above it.

## 5. PANEL TEXT (exact) and CUES (a3-s5.words.json)
Text: "27 SURVIVORS" · "EF-4 zone · single-family homes" · "Ground" · "11" · "Basement" · "Closet, laundry · 3" · "Hallway · 5" · "Bathroom · 7" · "Inside, first floor · 15" · "NIST Sec. 4.6.2.2".
Host: a3-s5 "Of" @5.78 → "up?" @17.16 + 0.8.
- 5.78 "Of": ground, grade line and source line on from frame 0.
- 6.00 "27": 27 pips pop in (scale .6 → 1, stagger 0.02 s); chip and eyebrow in.
- 7.10 "11": 11 pips travel down into the basement bin (y tween 0.9 s, power2.inOut, stagger 0.04 s); bin draws on; "11" counts up 0 → 11 and "Basement" lands at 8.0.
- 9.72 "lived": the 11 pips go to full opacity `#e8c56a` (amber 2), one pulse.
- 12.74 "closet,": closet box draws on; 3 pips travel into it; its label in.
- 13.50 "hallway,": hallway box; 5 pips; label.
- 14.28 "bathroom.": bathroom box; 7 pips; label. 14.68: group label in; the last grid pip greys.
- Holds: sorted pips breathe (y ±2 px, offset per pip). Exit in the last 0.6 s: chip and labels out per quickref, pips fade with the ground (fade-through to the clip).

## 6–8. CONTRACT, TOOLS, DONE LINE, RECEIPT
`references/mg-brief-template.md` §6, §7, §7a and §8 unchanged, COMPID = `g-a3-tally`, root id `g-a3-tally-root`.
