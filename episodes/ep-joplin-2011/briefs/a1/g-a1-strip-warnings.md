# BRIEF · g-a1-strip-warnings · "the false alarms were the warnings, a different set from the sirens" · DEEP (Opus 5.5, high)

Episode ep-joplin-2011, act A1, segments A1-S7 and A1-S8 (one host, from a1-s7 0.00 to the a1-s8 wav end 17.36). Full-frame MG
on the channel ground. It comes in on a cut from `g-a1-finding31`. Times in a1-s8 are comp-local = (`nx-a1-s8` data-start −
host data-start) + the word's time.
Base: SIREN STRIP. Copy `g-a1-strip-sirens` in its finished state (all 229 ticks, 4 red marks, labels, bracket, no chip) at
offset 0, the px table in `g-a1-strip-sirens.md` §2 and §3. Build after that comp passes its frame read. Same builder.
Exemplar for two sets that never merge: `library/inhouse/split-shared-scale.html`.
Open numbers: the dates of the 18 warnings are not in facts.md (`_list.md` Open 4). So the warnings row is an
**outcome tally** (sorted unverified, then verified), not a time axis, and it never lines up with the siren strip's dates.

## 0. What this graphic claims
The false alarms people remembered were tornado warnings, not sirens. 14 of 18 warnings from 2005 to 2011 had no
verified tornado (S10), close to the national 74.7 % (S10). In the five years before the storm it was 11 of 12 (S11, S13).
The emergency manager did not sound the sirens for every warning (S8), so they are two different counts, and people
distrusted both (S28, S40). The two rows differ in colour, form and axis. Nothing joins them.
Reading of "the last five years zoom in": with no dates, the zoom is a **recount**. The 18-row folds away and a
12-row builds in its place, so no mark claims a date.

## 1. SOURCE
- S10 "From 2005 through 2011, 78 percent (14 out of 18) of the official tornado warnings issued for Joplin did not result in a verified tornado; this percentage was in line with the 2007-2011 national average storm-based tornado false-alarm rate of 74.7 percent." NIST Finding 30.
- S12 "the NWS issued 18 tornado warnings for all or some part of Joplin. Only 4 of these 18 NWS tornado warnings ... were followed by verified tornadoes." NIST Sec. 4.3.4.
- S13 "Of these 12 warnings, only 1 (May 10, 2008) was verified as an actual storm event." NIST Sec. 4.3.4. S11: "over the 5-year period from 2007 through 2011, the Joplin area false-alarm rate increased to 92 percent." Finding 30.
- S8 "the emergency manager for Joplin was not sounding the sirens for every tornado warning". NIST Sec. 4.3.4.
- S28 "NIST found evidence of high false-alarm rates in Joplin for NWS-issued tornado warnings, but not for Joplin's outdoor siren system ... even though citizens perceived high false-alarm rates for both". NIST Sec. 4.7.3.
- S39, S40 "distrust of or confusion about Joplin's emergency communications system". NIST Finding 44.

## 2. DATUM, SCALE, ORIENTATION
- The siren strip keeps the SIREN STRIP table at offset 0 (band y 380 to 420, labels y 300 to 345, year labels y 482).
  At frame 0 it sits at +170 px (where `g-a1-strip-sirens` ended) and rises to 0 over 0.00 to 0.60 (power2.out).
- Warnings tally (no time axis): marks 40 px wide, 24 px gap, 64 px pitch, left edge x = 200, mark band y 670 to 740.
  Row label baseline y 640. Colour Amber 1 `#d8a13a` (the siren strip is grey and red). The row is a count, so no year labels go under it.
- Gap between rows: y 490 to 615 (125 px), which holds the name card in A1-S8.
- Presenter circle: everything stays out of x ≥ 1600, y ≥ 680 (the tally ends at x 1328).

## 3. GEOMETRY (computed by `python3`, 17 Oct 26)
- **18-row:** mark i (0 to 17) left = 200 + 64·i, so x 200 to 1328. Unverified marks 0 to 13 are hollow (3 px amber stroke,
  no fill). Verified marks 14 to 17 (x 1096 to 1328, centre 1212) are filled amber with a dark check glyph (`#04070c`, 4 px stroke).
  A label "verified" (Arial 700 22 `#d8a13a` tracking 3) is centred at x 1212, baseline y 660, above that group. It must not touch the row label.
- **12-row (recount):** the same pitch, mark i (0 to 11) left = 200 + 64·i, so x 200 to 944. Marks 0 to 10 are hollow, and mark 11 (x 904
  to 944, centre 924) is filled with a check. The "verified" label moves under that mark: centre x 924, baseline y 772.
  Above it, it would cross the longer recount row label, which runs to x 1050.
- **Row labels:** "Tornado warnings for Joplin · 2005 to 2011", then on the recount "Tornado warnings · the 5 years before
  May 22, 2011", both Arial 700 26 `#d8a13a` tracking 4, left x 200, baseline y 640, right end ≤ 1050 so they stay clear of the "verified" label.
- **Siren strip row label** "Joplin's outdoor sirens" (from the base) stays as is.
- **Name card** (A1-S8): a glass card centred at x 960, y 521 to 583, with "Joplin-Jasper County emergency manager" in Arial 700 30 `#f2f5f8`.
  It sits in the gap and touches neither strip.
- **Chip zone:** top centre, x 960, y 96 to 166, one chip at a time (the base's zone).
- **Source line:** bottom-left, x 96, baseline 1010.

## 4. MUST BE TRUE IN THE PICTURE
1. The 18-row has exactly 18 marks, 4 of them verified. The 12-row has exactly 12 marks, 1 verified. Count them on the frame.
2. The warnings row never shares the siren strip's axis: no year labels under it, no mark placed at a date, no line or
   bracket joining the two rows, a different colour (amber against grey and red).
3. The 18-row and the 12-row never show at the same time above 15 % opacity. A recount is a replacement.
4. The 74.7 % is printed only with "national" and "(NIST)" in the same line (S10 CONFLICT).
5. The name card overlaps neither strip's ink, and no chip covers a mark.
6. The siren strip is pixel-identical to the base table after the 0.6 s rise (diff one frame against `g-a1-strip-sirens` at offset 0).

## 5. PANEL TEXT (exact) and CUES
| element | text | cue |
|---|---|---|
| siren strip (finished state) rises to offset 0 | base text | a1-s7 frame 0, 0.00 to 0.60 |
| warnings row label | "Tornado warnings for Joplin · 2005 to 2011" (S10) | a1-s7 "From" 2.64 |
| 18 marks build left to right | (none) | a1-s7 "18" 6.16, 0.03 s stagger (0.54 s), scaleY 0 to 1 from the bottom |
| source line 1 | "NIST Finding 30" | a1-s7 "18" 6.16 |
| 4 verified fill + check; 14 dim to 55 % | "verified" | a1-s7 "Fourteen" 7.80 (fill 0.4 s), dim on "confirmed." 9.88 |
| chip | "14 OF 18 · NO TORNADO" (S10) | a1-s7 "confirmed." 9.88 |
| source line 2 (replaces 1) | "NIST Finding 30 · national 2007 to 2011 average 74.7% (NIST)" (S10) | a1-s7 "national" 11.62 |
| recount: 18-row folds (scaleY to 0, right to left, 0.4 s); row label swaps | "Tornado warnings · the 5 years before May 22, 2011" (S13) | a1-s7 "In" 13.00 (fold), label on "five" 13.32 |
| 12 marks build | (none) | a1-s7 "five" 13.32, 0.03 s stagger (0.36 s) |
| 1 verified fill; 11 dim | "verified" | a1-s7 "11" 15.34 |
| chip (replaces) | "11 OF 12" (S11, S13) | a1-s7 "12." 16.34 |
| both rows at full brightness (siren strip back from 85 % to 100 %) | (none) | a1-s7 "sirens" 19.08 |
| name card in (y 24 to 0, autoAlpha) | "Joplin-Jasper County emergency manager" (S4, S8) | a1-s8 "emergency" 1.00 |
| source line 3 (replaces 2) | "NIST Sec. 4.3.4" | a1-s8 "emergency" 1.00 |
| chip (replaces) | "TWO DIFFERENT COUNTS" | a1-s8 "same" 6.72 |
| both rows pulse once (marks scale 1 to 1.12 to 1, 0.5 s) | (none) | a1-s8 "both" 8.46 |
| name card out | | a1-s8 "And" 10.80 |
| source line 4 (replaces 3) | "NIST Finding 44 · Sec. 4.7.3" | a1-s8 "investigators" 11.10 |
| hold, exit | | to the a1-s8 wav end 17.36. Both rows float 3 px up and down over 4 s for the whole host. The last 0.6 s fades through to the ground (the next comp is a full-frame cite card) |

Longest gap with no new tween is a1-s8 1.00 to 6.72 (5.7 s). The continuous float carries it, and it must be a real tween on the rows (beat_density).
The siren strip dims to 85 % from a1-s7 6.16 so the new row reads first.

## 6 to 8
`references/mg-brief-template.md` §6, §7, §7a (all seven), §8. The receipt states the 18-row and 12-row x tables, computed by script.
