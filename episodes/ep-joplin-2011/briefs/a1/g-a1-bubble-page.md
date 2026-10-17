# BRIEF · g-a1-bubble-page · "a protective bubble around Joplin" · STANDARD (Sonnet 5.5, high)

Episode ep-joplin-2011, act A1, segment A1-S10, first half. The host runs from a1-s10 0.00 to "Since" 8.76 (duration 8.76). It is full-frame
(the page on the channel ground), entered on a cut from `g-a1-quote-58` and the live TV pull after it. `g-a1-ring` follows on a cut at 8.76.
Order note: the Picture line lists this page after the ring map, but the voice says "protective bubble" first (`_list.md` "Picture-line readings").
Base: PAGE UNDERLINE (the intro's I1-S5 base, if built). Exemplar `library/official/vox-annotate.html`.
Open numbers: none.

## 0. What this graphic claims
Residents told the NWS that storms always blew over and missed Joplin, as if the town had a "protective bubble" around it (S23).

## 1. SOURCE
- S23 "It was common in the interviews to hear residents refer to \"storms always blowing over and missing Joplin,\" or that there seemed like there was a \"protective bubble\" around Joplin". NWS Assessment, Finding #2b.
- Page image: `media/candidates/a1/a1-s10_c1_nws-p13-protective-bubble.jpg` (NWS PDF p13, "protective bubble" in the first paragraph).

## 2. DATUM, SCALE, ORIENTATION
- Ground `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)` from frame 0.
- Page box x 300 to 1560, y 200 to 940. Crop to the paragraph holding both phrases. Choose the crop so that capital letters are at least 28 px tall on screen.
- Source line x 96, baseline 1010. No chip (the Picture line has none). Nothing enters x ≥ 1600, y ≥ 680.

## 3. GEOMETRY
- Page: a 1 px `rgba(255,255,255,.14)` edge and a soft shadow (0 20px 60px rgba(0,0,0,.5)).
- Underline U1: a 6 px Amber 1 `#d8a13a` bar under "protective bubble" only (the Picture line underlines that phrase), 6 px below the baseline, ±4 px glyph to glyph.
- Source line: "NWS Central Region Service Assessment, Joplin, 2011 · Finding 2b", Arial 700 20 `#c8d3e0`.

## 4. MUST BE TRUE IN THE PICTURE
1. The bar sits under "protective bubble" and under nothing else.
2. The page's push keeps the phrase inside the text-safe frame.

## 5. PANEL TEXT (exact) and CUES (a1-s10)
| element | text | cue |
|---|---|---|
| ground + page in (y 30 → 0, autoAlpha, 0.6 s) + source line | "NWS Central Region Service Assessment, Joplin, 2011 · Finding 2b" | frame 0. The source line rises on "believed" 1.08 |
| page push toward the phrase (scale 1.00 to 1.12, plain `to()`, power1.inOut) | | "storms" 1.34 to "protective" 5.14 |
| U1 draws | | "protective" 5.14 to "around" 5.88 |
| hold, slow push continues (1.12 to 1.14) | | 5.88 to 8.16 |
| exit: page fades through to the ground | | 8.16 to 8.76 (cut to `g-a1-ring` at 8.76) |

Known gate issue: page crops may flag flat-type or undesigned (`learnings/mg.md` 12 Oct 26). Report it, do not pad.

## 6 to 8
`references/mg-brief-template.md` §6, §7, §7a (all seven), §8.
