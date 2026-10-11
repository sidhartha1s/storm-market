Host: id=g-i1s7-sheriff file=compositions/g-i1s7-sheriff.html start=87.88 duration=12.09 track=2

# 10 · I1-S7, I1-S8 · the sheriff's two sentences, then the television (comp `g-i1s7-sheriff`)

Brief on `references/mg-brief-template.md`. Shared look: `00-design-sheet.md` sections 7, 9. **One comp across two segments:** the script holds the same page and moves the underline from one sentence to the next. Revised 12 Oct 26 to the page scan.
**Spoken:**
- I1-S7: "A sheriff in another county found out when the tornado was going over, and said, "We didn't have any warning at all.""
- I1-S8: "The television, the sheriff said, did not even list that county in the danger area."
**One look:** another page of the study, labelled "a different county"; the sheriff's own words underlined and lifted; then a television showing an ordinary programme.

## 0. What this graphic claims
A sheriff in a different county, unnamed in the study, said "We didn't have any warning at all", and said the television did not list his county as being in the danger area.

## 1. Source
`edit_script.md` I1-S7 and I1-S8, Rows [C6] (County B; "the sheriff's words are 'as being in the danger area'"). Page image: `media/docs/study-pdf-24-orig.png` (2712 x 3414, printed page number 22, read by eye 12 Oct 26). The block quote the crop holds reads, line by line:
"The (first) time that I knew that we (were) even going to have / one was when it was going over. We didn't have any warning / at all...I knew that there was a storm coming up by listening / to the television. And the television didn't even list here / (County B) as being in the danger area."
"(County B)" is the study's own bracket in place of the county's name. The lines above the quote ("When County B's Sheriff was asked...") and the paragraph below it that names County A are outside the crop.

## 2. Datum, scale, orientation
Crop box, page px: x 630 to 2230, y 1740 to 2055 (1600 x 315), saved as `media/docs/study-p22-sheriff-crop.png` at 1460 x 287 (scale 0.9125). Line pitch on the card is about 51 px (the quote is single spaced), so the strips carry the reading.
| Underline | Words | Page px (x0 to x1, y0 to y1) | Px inside the 1460 crop |
|---|---|---|---|
| A1 | "We didn't have any warning" | 1518 to 2203, 1819 to 1868 | x 810 to 1435, y 72 to 117 |
| A2 | "at all" | 651 to 797, 1873 to 1924 | x 19 to 152, y 121 to 168 |
| B1 | "the television didn't even list here" | 1243 to 2108, 1929 to 1969 | x 559 to 1349, y 172 to 209 |
| B2 | "as being in the danger area." | 928 to 1633, 1984 to 2035 | x 272 to 915, y 223 to 269 |
A2 stops before the page's three dots. B1 starts at "the", after "And". B2 starts after the bracket "(County B)" (page x 651 to 903), which is left without an underline. The builder confirms each box within 10 px on the cut file.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient |
| County label | glass chip left 96, top 54, height 46: `a different county` Arial 700 26 px, Body light |
| Document card | left 96, top 116, 1480 x 307 (right 1576, bottom 423); crop inside at (106, 126) |
| Underlines | Popfig red 6 px; A1 and A2 fade to 35 % when B1 starts |
| Quote strip 1 | left 96, top 470, 1480 x 240 (bottom 710): `"We didn't have any warning at all"` Georgia 52 px, Caption dark, left 150, top 510; attribution `a county sheriff · Disaster Research Center, 1966, p. 22` Arial 700 22 px, Caption dark sub, left 152, top 646 |
| Quote strip 2 | same box and attribution, replaces strip 1: Georgia 44 px, two lines, line height 56, top 494: `"the television didn't even list here` / `(County B) as being in the danger area."` |
| Television | the big television (design sheet section 7): box x 480 to 1440, y 150 to 918; screen x 544 to 1158, y 214 to 726; Programme state |

## 4. Must be true in the picture
1. The label reads `a different county`. No county, town or sheriff's name is on screen. The only county mark is the study's own "(County B)", as printed, inside the quote (S1). "County A" is in no frame.
2. Nothing from comp 09 is in this comp: not its label, page or quote.
3. Both strips are the page's words in quotation marks, attributed `a county sheriff · Disaster Research Center, 1966, p. 22`. The narration's paraphrase ("did not even list that county") is never shown as a quote.
4. One strip at a time: strip 1 has left before strip 2 is readable.
5. The television shows the Programme state: no map, no list of counties, no warning text, no dog or figure (S5). We do not draw what the broadcast showed, because nothing of it survives that we may use.
6. No sheriff, badge, car or face is drawn (S5). No voice other than the narrator reads the quote (sound note for the orchestrator).
7. Design sheet S6, S7.

## 5. Text (exact) and cues
Text: `a different county` · `"We didn't have any warning at all"` · `"the television didn't even list here (County B) as being in the danger area."` · `a county sheriff · Disaster Research Center, 1966, p. 22`. The attribution is one line of text reused by both strips: pre-author it once, outside the two quote nodes.
| Step | Seg | cue | t= | What |
|---|---|---|---|---|
| 0 | I1-S7 | first frame (word "A") | 0.00 | canvas ground; document card sliding in (`x:660 to 0`, 0.7, power3.out) |
| 1 | I1-S7 | cue: "another" | 0.53 | county label drops in |
| 2 | I1-S7 | cue: "We" | 4.09 | unlit page fades in; A1 draws (0.5 s), then A2 (0.2 s) |
| 3 | I1-S7 | cue: "all" (last word) | 5.41 | strip 1 rises; hold through the seam |
| 4 | I1-S8 | cue: "television" | 6.66 | A1 and A2 to 35 %; B1 draws (0.6 s) |
| 5 | I1-S8 | cue: "said" | 7.98 | strip 1's quote slides up and out inside the strip, strip 2's quote rises in (masked line swap, 0.4 s) |
| 6 | I1-S8 | cue: "list" | 9.26 | B2 draws (0.5 s) |
| 7 | I1-S8 | cue: "danger" | 10.30 | label, card and strip slide out right (`x:1900`, 0.5, power3.in); television draws on (0.6 s) already in the Programme state, bars drifting |
| 8 | I1-S8 | cue: "area" (last word) | 10.54 | hold 1.0 s on the television |
| 9 | exit | | 12.09 | hard cut to 11 |

## 6 to 8. Contract, tools, done line, receipt
As `references/mg-brief-template.md` sections 6, 7, 7a, 8, unchanged. File `compositions/g-i1s7-sheriff.html`, id prefix `shf-`, root id `shf-root`. Host window: first word of I1-S7 to 1.0 s after the last word of I1-S8.
**Closest library exemplar:** El Reno `compositions/g-a4s11-page.html` (two sentences on one page lit separately, in turn) and `library/inhouse/quote-card.html`; the official catalog block `line-swap` for step 5.
