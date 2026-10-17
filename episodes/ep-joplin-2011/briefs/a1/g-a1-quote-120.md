# BRIEF · g-a1-quote-120 · "nine times out of ten, nothing really happens" · STANDARD (Sonnet 5.5, high)

Episode ep-joplin-2011, act A1, segment A1-S2. The host runs from a1-s2 0.00 to "Three" 10.26 (duration 10.26). This is an **overlay**: a glass
quote card over footage. `g-a1-theater-map` follows on a cut at 10.26.
Picture beneath (index.html, lower track, spanning the whole host): the NOAA NGS aerial `media/candidates/a1/a1-s2_c1_noaa-ngs-aerial-26th-st-crop.jpg`
(24 May 2011 flight, public domain, the collapsed theater just south of W 26th St). No lawful ground photo of the theater exists (`candidates.md`).
The still is held about 10 s, so the editor gives it a slow push (sweep check 9). The card's label names the place, and that is a claim about the
picture (template 7a item 7): read the file's `provenance.csv` row before the frame read.
Exemplars: `references/editing-patterns/ep6-glasscard-popfig-bfmg.html` (`.quotecard.glasscard`), `library/inhouse/quote-card.html` (phrase-by-phrase reveal).
Open numbers: none ("NIST Interview 120" and "9 times out of 10" are in S24).

## 0. What this graphic claims
An actor at the Stained Glass Theater gave the siren little weight because "9 times out of 10, you hear the sirens but nothing
really happens" (S24). These are the actor's own words, attributed, and nothing else is on screen.

## 1. SOURCE
- S24 "I didn't put much stock in that siren, because I'd heard them before, and 9 times out of 10, you hear the sirens but nothing really happens". NIST NCSTAR 3, Sec. 4.4.3 Stained Glass Theater (NIST Interview 120). No gender is given, so the card has no pronoun.

## 2. DATUM, SCALE, ORIENTATION
- Glass card (tokens.md surface): `rgba(10,16,24,.55)`, `backdrop-filter: blur(18px) saturate(1.15)`, 1 px `rgba(255,255,255,.14)` border,
  radius 28, no box-shadow. Box: left 200, right edge x 1560, top 500, height from content (≤ 440, so the bottom is ≤ 940). `inset: auto`.
- The card stays out of x ≥ 1600, y ≥ 680, so the presenter circle may stay on.
- No chip and no source line (the Picture line names none). The attribution carries the source.

## 3. GEOMETRY (text inside the card, padding 44 px)
- Eyebrow: "Stained Glass Theater", Arial 700 22 `#93a3b2`, tracking 6.
- Quote, Georgia italic `#f2f5f8`, line height 1.25, four leaves:
  - L1 "“I didn't put much stock in that siren," at 38 px
  - L2 "because I'd heard them before," at 38 px
  - L3 "and 9 times out of 10," at 56 px in Amber 1 `#d8a13a` (the emphasis line and the big tier)
  - L4 "you hear the sirens but nothing really happens”" at 38 px
- Attribution: "an actor in the play · NIST Interview 120", Georgia italic 26 `#d8a13a`.
- That gives three tiers: 22 (small), 26 and 38 (mid), 56 (big).

## 4. MUST BE TRUE IN THE PICTURE
1. The quote is verbatim from S24, split only at the commas shown, and no word is changed.
2. No pronoun appears for the actor.
3. Under the card is the 26th St aerial for every second of the host, with no stock and no other place.
4. The card covers no broadcaster mark (there is none on a NOAA aerial; confirm it on the frame).

## 5. PANEL TEXT (exact) and CUES (a1-s2)
| element | text | cue |
|---|---|---|
| card in (`fromTo(y:40, autoAlpha:0 → 0, 1, 0.7, power3.out)`), eyebrow | "Stained Glass Theater" | card 0.00 (on "One" 0.00), eyebrow on "Stained" 1.28 |
| L1 | "“I didn't put much stock in that siren," | "didn't" 2.16 |
| L2 | "because I'd heard them before," | "In" 4.42 (unspoken, so it lands as the voice turns to the quote) |
| attribution | "an actor in the play · NIST Interview 120" | "actor's" 4.70 |
| L3 | "and 9 times out of 10," (S24) | "nine" 6.02 (lands with a 1.0 to 1.04 to 1.0 scale tick, 0.4 s) |
| L4 | "you hear the sirens but nothing really happens”" | "you" 7.30 |
| hold: card floats y ±3 px, 4 s sine | | 8.84 to 9.66 |
| exit: card slides out (`to x:980, autoAlpha:0, 0.6, power3.in`) | | 9.66 to 10.26, finished before the cut to the map |

Rows `fromTo(autoAlpha 0, y 24 → 0, 0.4)`. Every leaf is hidden in CSS as well as by the timeline.

## 6 to 8
`references/mg-brief-template.md` §6, §7, §7a (all seven; item 7 overlay read over the aerial), §8.
