# g-a5-9-larson · A5-S6 0 to 13.90 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `library/inhouse/quote-card.html` (quote with attribution), `references/editing-patterns/g-person-allen.html` (text-only person card, no photo slot).

## 0. Claim
Erik Larson, author of Isaac's Storm (1999), says no other survivor is known to have backed the ride up, and doubts Cline warned 6,000.

## 1. Source
- "no other survivors are known to have corroborated these accounts" (Wikipedia citing Larson; sources-cline.md §4; fact-check a5-r1 row 24).
- Salon, 29 Sept 1999 (https://www.salon.com/1999/09/29/larson/): "Most likely [Isaac] did go to the beach and warn some people — but did he warn 6,000? I don't see how that is possible." (fact-check row 25).
- Isaac's Storm (1999), Crown (row 28).

## 2. Datum, scale, orientation
Full-frame designed card (tokens radial background). No cover scan (copyright, open item 3): a typeset title block stands in for the book.

## 3. Geometry (px)
- Title block, centred x 960, top 240: "ISAAC'S STORM" Georgia 96 px `#f2f5f8`, under it "1999" Arial 700 32 px `#d8a13a` tracking 6. Thin rule 2 px `#93a3b2`, 360 px wide, under the year.
- Lower-third `left:110px; bottom:110px`: name "ERIK LARSON", role "AUTHOR, ISAAC'S STORM".
- Chip C1 "NO OTHER SURVIVOR KNOWN TO BACK IT", glass, centred x 960, top 560 (below the title block, above the lower-third; card ~ 1000 x 100).
- Quote card Q (glass, `.quotecard.glasscard`, `left:260px; right:260px; top:300px`): Georgia 44 px `#f2f5f8` "“Most likely [Isaac] did go to the beach and warn some people — but did he warn 6,000? I don't see how that is possible.”"; attribution Arial 700 24 px `#d8a13a` "Erik Larson, Salon, Sept. 29, 1999".
- Source line top-left: "Erik Larson, Isaac's Storm, 1999 (as summarised by Wikipedia) · Salon, Sept. 29, 1999".

## 4. Must be true in the picture
1. C1 says "KNOWN TO", never "NO OTHER SURVIVOR BACKED IT" (fact-check row 27).
2. The quote is Larson's exact words with the bracket and the dash; no "did not warn anyone" anywhere (dropped, fact-check row 25).
3. Q never shares the frame with C1 or the title block (one reading target): title and C1 leave before Q enters.
4. The lower-third and Q do not overlap (Q bottom < 820).
5. Nothing in x >= 1600, y >= 680.

## 5. Text and cues (a5-s6.words.json, segment 21.50 s)
- 0.00 ("Eric" 0.00): title block in (y 30 -> 0, 0.5 s); 0.24 ("Larson," 0.24) /* LARSON @0.24 */: lower-third in; source line in 0.4.
- 1.44 ("1999" 1.44): "1999" line types on.
- 3.74 ("says" 3.74): lower-third out.
- 3.94 ("no" 3.94) /* NO OTHER @3.94 */: C1 in, words revealed in spoken order: "NO OTHER SURVIVOR" 3.94, "KNOWN TO" 5.00, "BACK IT" 5.46.
- 6.84 ("He" 6.84): C1 and the title block out (title fade, C1 slide right).
- 7.26 ("interviewer" 7.26) /* SALON @7.26 */: Q in, the quote building line by line: line 1 with "Most likely" at 8.16, "warn some people" at 8.86, "did he warn 6,000?" at 12.16 ("warned"), "I don't see how that is possible." at 13.00; attribution at 7.60.
- Host: A5-S6 0.00 to 13.90 (g-a5-10 at "And" 14.02).

## Motion for the whole window
Title block slow scale 1.00 to 1.03; cards drift; Q's lines reveal keeps it moving through 13.0.

## Exit
Q slides out `x:980, autoAlpha 0, 0.6 s power3.in`, 13.30 to 13.90; source line fades with it.

## Footage under it
None (full-frame card).
