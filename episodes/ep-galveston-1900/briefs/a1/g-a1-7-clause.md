# g-a1-7-clause · A1-S4 1.64 to 4.62 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules" (incl. "The page"). Base: `compositions/g-a1-1-page.html` (build it first): copy its two page layers, the column-only mask end state and the camera function into this file with renamed ids. Do not edit g-a1-1.

## 0. Claim
Cline's reason is in the same sentence: "as there is too large a territory to the north which is lower than the island, over which the water may spread".

## 1. Source
- Scan, column 3: the sentence ends line L7 "...and not from reasoning; as there is too" (source y 591.7) and runs on under Fig. 8 (source y ≈ 823 onward): "large a territory to the north which is lower / than the island, over which the water may / spread, it would be impossible for any cyclone / to create a storm wave which could materially / injure the city." (my 3x read; `_list.md` change 2: the scan has "could", Commons has "would").
- factcheck/a1-r1.md rows 17, 18; sources-cline.md §1. Held with g-a1-3 until a human reads the scan.

## 2. Datum, scale, orientation
Same page layers and camera as g-a1-1 (source px, `screen = (960 + (sx − cx)·s, 540 + (sy − cy)·s)`), column-only from frame 0 (outside column 3 at opacity 0). Camera keys (computed):
- P0 (frame 0 to 0.84): s 4.0, c (507, 592): column x 552 to 1372; L7 at y 538.8. Drift s 4.0 → 4.04.
- P1 (S4 2.82 to 3.60, comp-local 1.18 to 1.96): pan straight down to c (507, 832), s 4.0, power2.inOut (the camera passes over Fig. 8; nothing labels it).
- P1b: hold c (507, 832) with drift s 4.04 → 4.10 to the end. Lines then at screen y: A (823) 504, B (831.5) 538, C (840) 572.

## 3. Geometry (px)
- Highlights as g-a1-1 (`#d8a13a` 0.32 multiply, 7.5 source px tall, scaleX left origin 0.5 s), in the camera group:
  - H0: L7 tail "as there is too" (source x ≈ 548 to 603, y 591.7).
  - HA: line A full width (x 418 to 603, y ≈ 823) "large a territory to the north which is lower".
  - HB: line B full width (y ≈ 831.5) "than the island, over which the water may".
  - HC: line C first word only "spread," (x 418 to ≈ 452, y ≈ 840).
  Re-measure A, B, C on the staged crop; list them in the receipt.
- Source line top-left: "Isaac Cline, Galveston Daily News, July 16, 1891".
- No other text (no chip: the chip is in g-a1-8, `_list.md` change 6).

## 4. Must be true in the picture
1. Frame 0 matches g-a1-1's look (same page, same column, no other column visible): the viewer reads it as "back to the column".
2. No word is cut left or right by the frame at any time (column x 552 to 1372 at s 4).
3. Each highlight sits on its printed words (±3 px at s 4); nothing is lit beyond "spread,".
4. No label or mark on Fig. 8 as the camera passes it.
5. Nothing in x >= 1600, y >= 680.

## 5. Text and cues (a1-s4.words.json; comp-local = S4 time − 1.64)
- 1.64 ("sentence,"): column on at P0, source line in (0.3 s). /* COLUMN @1.64 */
- 2.48 ("and"): H0 lit. /* AS THERE IS TOO @2.48 */
- 2.82: pan P1 starts (lands 3.60).
- 3.62 ("island."): wait; 3.00 ("land") is spoken before the pan lands, so HA lights at 3.62 on landing, HB at 3.78 ("island." end) and HC at 4.10. /* TERRITORY @3.62 */
- 4.32 to 4.62: root fades for the cut.
- Host: A1-S4 1.64 to 4.62.

## Motion for the whole window
Camera drift, the pan, highlights. Window 2.98 s.

## Exit
Fade-through to g-a1-8 at 4.62 ("He").

## Footage under it
None: the page is inside the comp (staged stills from `_list.md` open item).
