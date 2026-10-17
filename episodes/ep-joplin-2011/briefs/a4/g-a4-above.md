# BRIEF · g-a4-above · "were all above ground" · glass text card over footage · STANDARD (Sonnet 5.5, high)

Episode ep-joplin-2011, act A4, segment A4-S12. Overlay on the glass card, over footage.
Footage under it (orchestrator's mount, whole host window): moving footage of the demolished commercial buildings. The
Picture line names none; the DVIDS Range Line corridor flight (`a4-s1_c1`, `a4-s5_c5`) has seconds no other beat uses.
A reuse of the same file needs `data-callback` (CLAUDE.md QC (b)). The card names no place, so no 7a.7 check on the clip.
Our own text card, never the NIST page: B32's printed sentence carries a flag word (`references/flag-words.md`).
Exemplar: `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` (glass card over footage).
Open numbers: none.

## 0. What this graphic claims
In every demolished building NIST studied in this section, the people lost or badly hurt were above ground. The eight
businesses and churches it examined had one basement among them (the theater's), and no one lost was found in it.

## 1. SOURCE
- B32 "In all of the demolished buildings, the persons killed or severely injured were located above ground." NIST Sec. 4.6.2.1.
- B31 "Only one of the eight buildings discussed in this section, the Stained Glass Theater building, contained an underground space or basement" Sec. 4.6.2.1.
- B4 "neither affected residential nor non-residential buildings were able to provide life-safety protection" Finding 9 (context; not on screen).

## 2. DATUM, SCALE, ORIENTATION
Glass card (tokens.md surface, radius 28) left 140, top 300, width 1160; text left-aligned at card-left + 64. Presenter
corner (x ≥ 1600, y ≥ 680) clear.

## 3. GEOMETRY
- Text in three lines, Arial Black 900, 52 px, `#f2f5f8`, revealed line by line: "In all of the demolished buildings," ·
  "those lost or badly hurt" · "were above ground". No quotation marks: it is our sentence from B32, not NIST's wording.
- Source under it (small tier, 20 px `#c8d3e0`): "NIST Sec. 4.6.2.1".
- Chip under the source (mid tier, 30 px Arial 700 `#d8a13a`, tracking 1): "ALL ABOVE GROUND · THE 8 BUSINESSES AND
  CHURCHES STUDIED" (wrap to two lines inside the card if it is wider than the card).

## 4. MUST BE TRUE IN THE PICTURE
1. The text reads exactly as above; the word "killed" appears nowhere.
2. No quotation marks around the sentence.
3. The chip reads after the sentence has landed, never before it.
4. Every glyph sits inside the card; the card leaves the frame's right third to the footage.

## 5. PANEL TEXT (exact) and CUES
Text: "In all of the demolished buildings," · "those lost or badly hurt" · "were above ground" · "NIST Sec. 4.6.2.1" ·
"ALL ABOVE GROUND · THE 8 BUSINESSES AND CHURCHES STUDIED".
Cues (`_list.md` "Cue notation"):
- card in (`fromTo autoAlpha 0, y 24 → 0`, 0.5 s, power3.out) + line 1 a4-s12 "The" 3.90.
- line 2 a4-s12 "people" 4.12 + 0.4 s; line 3 a4-s12 "above" 6.12; source line 6.32.
- chip a4-s12 "Besides" 7.66.
- hold with a 3 px float; card out (`x → 980, autoAlpha 0, 0.6, power3.in`) so the host ends a4-s12 "ground?" 11.18 + 0.6 s.

## 6 to 8. Contract, tools, done line, receipt
`references/mg-brief-template.md` §6 to §8 verbatim, COMPID `g-a4-above`. Comp-specific: overlay comp, transparent root;
done-line frame composited over the mounted clip at a4-s12 9.0 s.
