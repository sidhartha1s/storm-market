# 10 · I1-S7, I1-S8 · the sheriff's two sentences, then the television (comp `g-i1s7-sheriff`)

Brief on `references/mg-brief-template.md`. Shared look: `00-design-sheet.md` sections 7, 9. **One comp across two segments:** the script holds the same page and moves the underline from one sentence to the next.
**Spoken:**
- I1-S7: "A sheriff in another county found out when the tornado was going over, and said, "We didn't have any warning at all.""
- I1-S8: "The television, the sheriff said, did not even list that county in the danger area."
**One look:** another page of the study, labelled "a different county"; the sheriff's own words underlined and lifted; then a television showing an ordinary programme.

## 0. What this graphic claims
A sheriff in a different county, also unnamed in the study, said "We didn't have any warning at all", and said the television did not list his county as being in the danger area.

## 1. Source
`edit_script.md` I1-S7 and I1-S8, Rows [C6] (County B; "the sheriff's words are 'as being in the danger area'"). Page: the 1966 study, printed p. 23. **Waits for the study scan, printed p. 23** (not a row of `research/picture-inventory.md`; rights line unread; needs a `provenance.csv` row).
Underlined phrase 1: `We didn't have any warning at all`. Underlined phrase 2: the sheriff's next sentence, from `the television didn't even list here` to the end of that sentence as printed. The builder reads the page and copies the second strip from it; the page wins over this brief and over the narration, and the builder reports the exact words in the receipt.

## 2. Datum, scale, orientation
Page scale = 1460 / text column width in page px (design sheet section 9). Line boxes of both phrases measured on the page image, in page px. Crop: from one line above phrase 1 to one line below phrase 2, full column width.

## 3. Geometry (screen px)
| Element | Px |
|---|---|
| Ground | canvas gradient |
| County label | glass chip left 96, top 54, height 46: `a different county` Arial 700 26 px, Body light |
| Document card | left 96, top 116, 1480 x 450 |
| Underlines | Crimson 6 px; phrase 1's underline fades to 35 % when phrase 2's starts |
| Quote strip 1 | left 96, top 606, 1480 x 220: `"We didn't have any warning at all"` Georgia 52 px, Caption dark, left 150, top 640; attribution `a county sheriff · Disaster Research Center, 1966` Arial 700 22 px, Caption dark sub, left 152, top 756 |
| Quote strip 2 | same box and attribution, replaces strip 1: phrase 2 as printed, Georgia 44 px in two lines (line height 56, top 630) |
| Television | box x 600 to 1320, y 200 to 776, screen x 648 to 1109, y 248 to 632 (comp 05's numbers), Programme state |

## 4. Must be true in the picture
1. The label reads `a different county`. No county, town or sheriff's name is on screen. The study's code "County B", if in the crop, is under the unlit page (S1).
2. Nothing from comp 09 is in this comp: not its label, page or quote.
3. Both strips are the page's words in quotation marks, attributed `a county sheriff · Disaster Research Center, 1966`. The narration's paraphrase ("did not even list that county") is never shown as a quote.
4. One strip at a time: strip 1 has left before strip 2 is readable.
5. The television shows the Programme state: no map, no list of counties, no warning text, no dog or figure (S5). We do not draw what the broadcast showed, because nothing of it survives that we may use.
6. No sheriff, badge, car or face is drawn (S5). No voice other than the narrator reads the quote (sound note for the orchestrator).
7. Design sheet S6, S7.

## 5. Text (exact) and cues
Text: `a different county` · `"We didn't have any warning at all"` · phrase 2 as printed · `a county sheriff · Disaster Research Center, 1966`. The attribution is one line of text reused by both strips: pre-author it once, outside the two quote nodes.
| Step | Seg | cue | t= | What |
|---|---|---|---|---|
| 0 | I1-S7 | first frame (word "A") | | canvas ground; document card sliding in (`x:660 to 0`, 0.7, power3.out) |
| 1 | I1-S7 | cue: "another" | | county label drops in |
| 2 | I1-S7 | cue: "We" | | unlit page fades in; underline 1 draws (0.8 s) |
| 3 | I1-S7 | cue: "all" (last word) | | strip 1 rises; hold through the seam |
| 4 | I1-S8 | cue: "television" | | underline 1 to 35 %; underline 2 draws line box by line box |
| 5 | I1-S8 | cue: "said" | | strip 1's quote slides up and out inside the strip, strip 2's quote rises in (masked line swap, 0.4 s) |
| 6 | I1-S8 | cue: "list" | | label, card and strip slide out right (`x:1900`, 0.5, power3.in); television draws on (0.6 s) already in the Programme state, bars drifting |
| 7 | I1-S8 | cue: "area" (last word) | | hold 1.0 s on the television |
| 8 | exit | | | hard cut to 11 |

## 6 to 8. Contract, tools, done line, receipt
As `references/mg-brief-template.md` sections 6, 7, 7a, 8, unchanged. File `compositions/g-i1s7-sheriff.html`, id prefix `shf-`, root id `shf-root`. Host window: first word of I1-S7 to 1.0 s after the last word of I1-S8.
**Closest library exemplar:** El Reno `compositions/g-a4s11-page.html` (two sentences on one page lit separately, in turn) and `library/inhouse/quote-card.html`; the official catalog block `line-swap` for step 5.
