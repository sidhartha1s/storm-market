# g-intro-10-delusion · I1-S5 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Copies the "ABSURD DELUSION" chip from `g-intro-2-cline1891` (same family: build g-intro-2 first, copy its chip block and restyle nothing). Exemplar for the popfig: cards.css `.popfig`.

## 0. Claim
Long before the 1900 messages, the city had Cline's word in print: July 16, 1891, "absurd delusion". This opens the question carried into Act 1.

## 1. Source
sources-cline.md §1: Commons transcription of the Galveston Daily News, 16 July 1891, p. 5 ("Date: 16 July 1891"; "is simply an absurd delusion"). The same open item as g-intro-2: one human look at the 1891 scan before the quote goes on screen.

## 2. Datum, scale, orientation
Overlay comp, transparent root, over a slow return push onto the 1891 Galveston Daily News page (track 1). Zones: centre popfig, then centre chip (one after the other), source line top-left.

## 3. Geometry (px)
- Popfig: `.popfig` centred, `top:38%`. Big line "JULY 16, 1891" (13 characters) Abril 150 px `#d0121f`; no sub line (the hook's popfig already named the place).
- Chip: exactly g-intro-2's chip (centred, top 600, "ABSURD DELUSION" Arial Black 900 64 px, tag "Isaac Cline, 1891" Georgia italic 26 px `#d8a13a`, the red rule under it).
- Source line top-left: "Galveston Daily News, July 16, 1891 · text: Wikimedia Commons transcription".

## 4. Must be true in the picture
1. The popfig has gone (autoAlpha 0) before the chip enters.
2. The chip's text and look match g-intro-2 exactly (it is the callback, edit script "chip back on").
3. The popfig date reads JULY 16, 1891 (not 1892: sources-cline.md conflict 6, the scan metadata says 1891).
4. Nothing in x >= 1600, y >= 680.
5. Not over the column the push ends on (same rule as g-intro-2 §4.2).

## 5. Text and cues (i1-s5.words.json, segment 9.191 s)
- Source line in at 0.00.
- 3.92 ("print" 3.92) /* PRINT @3.92 */: popfig slams in.
- 4.78 ("Why" 4.78): popfig holds and drifts; out 7.00 to 7.45 (before "an" 7.72).
- 8.16 ("absurd" 8.16) /* ABSURD @8.16 */: chip in; red rule draws 8.50 to 9.00 ("delusion" 8.50, the telegraph-key click on the last line).
- Host 0.00 to 9.191 + land time (at least 1.0 s; this is the section's last beat before Act 1's chapter blackout, so default end 10.20). Exit in the last 0.6 s.

## Motion for the whole window
0.00 to 3.92 has only the source line on screen: its drift plus the page push under it (3.92 s, under the 4 s limit; do not let the popfig slip later than 3.92). Popfig and chip drift +-4 px.

## Exit
Chip slides out `x:980, autoAlpha 0, 0.6, power3.in` into the chapter blackout.

## Footage under it
The 1891 Galveston Daily News page scan (as g-intro-2).
