# g-a5-6-tsha · A5-S5 2.70 to 6.04 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplar: `references/editing-patterns/g-cite-paper.html` (beige cite card, lit line). Reuse the right page of `g-a5-4-pages` (same typeset sentence) so the viewer recognises it.

## 0. Claim
Texas's state history handbook says Cline drove a horse-drawn cart around low areas warning people to leave.

## 1. Source
TSHA Handbook of Texas, Galveston Hurricane of 1900: "The Weather Bureau official in charge locally, Isaac M. Cline," "drove a horse-drawn cart around low areas warning people to leave." (sources-cline.md §4; fact-check a5-r1 row 20).

## 2. Datum, scale, orientation
Full-frame designed card (tokens radial background). The TSHA entry is a web page: typeset, not a scan. A5-S5 0.00 to 2.70 ("The second story grew over the years") is the orchestrator's: hold g-a5-4's right page alone, or a dark bridge.

## 3. Geometry (px)
- One beige cite card centred: `left:360px; top:220px; width:1200px; height:560px`, padding 64 px, radius 12, background `rgba(232,222,200,.90)`.
- Eyebrow "HANDBOOK OF TEXAS" Arial 700 22 px `#6b6257` tracking 4.
- Body Georgia 40 px `#2a2622`, line-height 1.4: "The Weather Bureau official in charge locally, Isaac M. Cline, … drove a horse-drawn cart around low areas warning people to leave." The second clause starts on its own line ("drove a horse-drawn cart around low areas" must be whole lines to light).
- Foot "Texas State Historical Association" Georgia 24 px `#6b6257`.
- Lit bar on "drove a horse-drawn cart around low areas warning people to leave." per the shared rule.
- Source line top-left: "Texas State Historical Association, Handbook of Texas".

## 4. Must be true in the picture
1. Text is the two TSHA fragments with the ellipsis; no word added.
2. Only the cart clause is lit.
3. Three tiers: 40 (mid... use 52 px for the lit clause? no): body 40 (mid), eyebrow 22 (small), and the card title "Galveston Hurricane of 1900" Georgia 56 px (big) above the body. Add that title line.
4. Card stays clear of x >= 1600, y >= 680.

## 5. Text and cues (a5-s5.words.json, segment 18.46 s; host starts at "Texas'" 2.70)
Comp-local = word time − 2.70.
- 2.70 ("Texas'" 2.70) /* HANDBOOK @3.54 */: card rises in (y 40 -> 0, autoAlpha, 0.5 s power3.out); source line in at 2.90.
- 4.72 ("drove" 4.72) /* DROVE @4.72 */: bar draws under the cart clause, 4.72 to 5.40; the rest of the card dims to 0.55.
- Host: 2.70 to 6.04 (g-a5-7 cuts in at "through" 6.04).

## Motion for the whole window
Card float y ±4; card scale 1.00 to 1.03 over the host.

## Exit
Cut at 6.04: root fades to 0 over the last 0.3 s.

## Footage under it
None (full-frame card).
