# g-a4-1-gulf-rising · A4-S1 0 to 4.58 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `compositions/g-a3-12-330.html` (p. 373 panel on glass, same scan family), catalog `inline-highlight` (marker behind words).

## 0. Claim
At 3:30 p.m. on Saturday Isaac Cline added one line to the special observation: "Gulf rising, water covers streets of about half city."

## 1. Source
MWR Sept 1900 p. 373 (factcheck/a4-r1.md rows 1, 2, 5; factcheck/a3-r1.md rows 39, 40): "added the following to the special observation at 3:30 p. m.: 'Gulf rising, water covers streets of about half city.'" MWR wording wins over the NWS reprint's "half of city". Scan: `media/candidates/a4/A4-S1_c1_mwr-1900-09-issue.pdf`, PDF page 3 (printed p. 373, header verified at 200 dpi), rasterise at 200 dpi to `media/a4/mwr-p373.png` (builder's one-shot, not a script that authors HTML).

## 2. Datum, scale, orientation
Full-frame designed comp on the tokens radial gradient (this is the first picture out of the CTA: no footage under it). Page panel left, telegraph form right. Zones: source line top-left, chip top-right, page panel left, form right.

## 3. Geometry (px)
- Page panel: glass card x 160 to 900, y 170 to 950 (740 x 780), the p. 373 scan cropped to whole lines around the 3:30 sentence (crop measured on the scan, listed in the receipt), page dimmed to 0.55, amber band `#d8a13a` at 0.28 behind the 3:30 lines. Slow push scale 1.00 to 1.04 over the window (`to`, ease none), crop holds whole lines at both ends.
- Telegraph form: a period Western Union style blank, card `#f4f0e6` (Beige polaroid), x 980 to 1760, y 300 to 760, radius 6, 1 px `#6b6257` rules. Printed header "TELEGRAM" Georgia 700 34 px `#2a2622` tracking 6 at top-left of the form (x 1020, y 330). Ruled message lines at y 470, 560, 650.
- Message text Courier New 700 44 px `#2a2622`, typed word by word (one leaf span per word, autoAlpha), three lines: "GULF RISING" / "WATER COVERS STREETS" / "OF ABOUT HALF CITY". Words sit on the ruled lines, left x 1030.
- Chip (glass, shared spec) "SAT · 3:30 PM", right edge x 1824, top 120; tag "special observation" Arial 700 22 px `#93a3b2`.
- Source line top-left: "Isaac Cline, Monthly Weather Review, September 1900, p. 373".
- Type tiers: chip 44 (mid), header 34 (mid), message 44 (mid), tag 22 / source 19 (small): add the big tier with the chip main line at 52 px Arial Black 900 (chip spec allows 44; use 52 here so the comp has three tiers).

## 4. Must be true in the picture
1. Message words are the MWR words, in order, nothing added ("about half city", not "half of city"; no "the").
2. Each word appears no earlier than its spoken start.
3. The panel's amber band sits on the 3:30 sentence of the scan (receipt names the measured box), no word cut at the crop edge in any frame.
4. Nothing in x >= 1600, y >= 680 (form right edge 1760 reaches y 760: shift form to x 940 to 1580 if the circle is on; default: circle off for this window, orchestrator decides).

## 5. Text and cues (a4-s1.words.json, comp-local = segment time)
- 0.00 /* CUT FROM CTA @0.00 */: frame 0 shows the page panel with band, the empty form and the source line (cut lands on a finished layout).
- 0.14 ("wrote"): chip in.
- 0.82 "GULF" /* GULF @0.82 */, 1.14 "RISING", 1.62 "WATER", 2.26 "COVERS", 2.68 "STREETS", 3.04 "OF", 3.22 "ABOUT", 3.42 "HALF", 3.74 "CITY" /* CITY @3.74 */: each word types in over 0.12 s (autoAlpha plus x 8 to 0), a telegraph-key click is the editor's SFX at each word.
- 4.14 ("city." ends): band pulses once (opacity 0.28 to 0.45 to 0.28).
- 4.00 to 4.58: exit.

## Motion for the whole window
Page push continuous; type-in steps every 0.3 to 0.6 s; chip drifts.

## Exit
Form and chip slide out `x:980, autoAlpha 0, 0.5, power3.in` from 4.00; page fades 4.20 to 4.58 into g-a4-2's map (cut at 4.58).

## Footage under it
None; the MWR scan is inside the comp (provenance row A4-S1_c1, verified Y).
