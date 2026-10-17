# g-a2-doc-cues · STANDARD (Sonnet 5.5, high) · act a2, segment a2-s10

**Open numbers:** none.

**The pages:** two renders of the real public-domain PDFs, files from sourcing (named at dispatch), mounted inside
this comp: (1) the NWS Service Assessment page carrying Finding #2d item (c); (2) the NIST NCSTAR 3 page carrying Finding
45 (Sec. E.4.2). Crop each to the paragraph that holds the phrase plus about two lines above and below. If a render is
missing, report; never retype a page.
**Before it:** the live TV clip (FagzNHuI5JI, 4 to 6 s, own audio) opens a2-s10 before the narration; this host starts
on the narration's first word, after the clip.
**After it:** g-a2-map-close starts on a2-s10 "second" @15.18; this comp exits from "And" @14.62.
**Cue clock:** `segment offset + word start`; offset = a2-s10 narration `data-start` minus host `data-start`.
Corner circle stays on: nothing enters x >= 1600, y >= 680.

## 0. What this graphic claims
The record names what moved people: the non-routine second siren for many, and most of all high-intensity cues,
hearing or seeing the tornado or others hurrying.

## 1. SOURCE (confirmed rows, quoted; the underlined words are these exactly)
- E20 (NWS Finding #2d (c)): "It is the Joplin emergency management policy to sound the sirens one time for a severe weather alert."
- E19 (NWS Finding #2d (c)): "A large number of those interviewed noted that this non-routine second siren alert raised their level of awareness". Underline: "non-routine second siren alert".
- E33 (NIST Finding 45): "The main factor that convinced individuals to take shelter was the receipt of high-intensity cues, including hearing or seeing the tornado approaching or witnessing others' urgency related to taking protection." Underline: "high-intensity cues, including hearing or seeing the tornado approaching or witnessing others' urgency".

## 2. DATUM, SCALE, ORIENTATION
- Each page crop sits on a paper card x 330 to 1590 (1260 px wide), centred vertically, top no higher than y 150; the crop scales so its body text x-height is at least 14 px (cap height about 20 px). Report the scale in the receipt.
- Underline position: measured from the render (the phrase's word boxes), never placed by eye; state the measured boxes in the receipt.

## 3. GEOMETRY
- Paper card: #f4f0e6 (tokens.md beige polaroid) with the page crop inside, 1 px rgba(0,0,0,.25) edge, no rotation.
- Page push: card scale 1.00 to 1.04, ease none, origin the phrase centre, through each page's hold. Underlines live inside the card's transform group so they ride with the page.
- Underline: `#d8a13a` (amber 1) 6 px, 4 px under the baseline, one stroke per text line of the phrase, drawn by scaleX 0 to 1 (transformOrigin left) in reading order, 0.25 s per 300 px of line.
- Chip: glass chip top-left, left 96, top 54, Arial Black 900 52 px #f2f5f8: "SECOND SIREN".
- Source line: glass pill top-right, right 96, top 54, Arial 700 20 px #c8d3e0.
- Page swap: page 1 out x 0 to -980 + autoAlpha 0, 0.6 s power3.in; page 2 in x 980 to 0, 0.7 s power3.out; chip leaves with page 1.
- Exit: page 2 out x 0 to -980 + autoAlpha 0, 0.6 s power3.in, source line with it.

## 4. MUST BE TRUE IN THE PICTURE
1. The underlined words are exactly the phrases in §1, no word more or less, on the real page text.
2. The pages are renders of the published PDFs (NWS Assessment; NIST NCSTAR 3), not retyped or re-set.
3. One page on screen at a time; one chip at a time.
4. Text on the page reads at couch distance in a frame read (cap height about 20 px or more).
5. Nothing enters x >= 1600, y >= 680 (card right edge 1590).

## 5. PANEL TEXT (exact) and CUES
| cue (segment · word · start s) | what happens |
|---|---|
| a2-s10 · "Joplin's" · 0.00 | page 1 (NWS) in; source line "NWS Assessment, Finding 2d" |
| a2-s10 · "second" · 3.04 | underline "non-routine second siren alert" draws |
| a2-s10 · "ordinary," · 4.10 | chip "SECOND SIREN" |
| a2-s10 · "But" · 7.52 | page swap to page 2 (NIST); source line "NIST Finding 45" |
| a2-s10 · "hearing" · 10.72 | underline stroke 1: "high-intensity cues, including hearing" |
| a2-s10 · "seeing" · 12.18 | stroke 2: "or seeing the tornado approaching" |
| a2-s10 · "watching" · 12.88 | stroke 3: "or witnessing others' urgency" |
| a2-s10 · "And" · 14.62 | exit, 0.6 s; host ends with it |

If the phrase breaks across lines differently on the render, keep the three cues and split the strokes at those words.

## 6 to 8
As `references/mg-brief-template.md` §6, §7, §7a, §8. File `compositions/g-a2-doc-cues.html`, timeline
`window.__timelines["g-a2-doc-cues"]`, root id `a2dc-root`.
