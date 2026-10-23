# BRIEF · g-z1-strip · "the sirens weren't crying wolf" · STANDARD (Sonnet 5.5, high)

Episode ep-joplin-2011, segment Z1-S1 (first part). Full-frame MG on the channel ground, no footage under it. Host from
z1-s1 "Joplin's" 0.00 to "That" 10.06, where `g-z1-map` takes over on a cut. It opens after the hand-placed chapter blackout out of a6.
Base: SIREN STRIP + warnings tally. Copy `compositions/g-a1-strip-warnings.html` in its finished state (end of a1-s8): siren strip
at offset 0 (229 ticks, 4 red marks, mark labels, gap bracket, row label, year labels) and the amber 12-mark recount row with its
label and "verified" label. Drop the chip, name card and source line. Build after `g-a1-strip-warnings` passes its frame read.
Open numbers: none.

## 0. What this graphic claims
Outside the weekly test, Joplin's sirens sounded for a real storm about once a year since 2007 (S2): the test comb fades and the
four real soundings stand out. The warnings, the count people remembered as false alarms, sit below as a separate set (S8, S28).

## 1. SOURCE
- S2 "Since 2007, the average rate of activation of the 25-siren outdoor warning system in Joplin was once per year (at most), not including the test activations (1 minute in duration) that occurred weekly." NIST NCSTAR 3, E.4.2 Finding 31.
- S5 weekly test, Mondays 10 a.m., 1 min (the grey ticks). S6, S7 the four dated soundings (the red marks), as in `g-a1-strip-sirens`.
- Warnings row: S11, S13 (12 warnings, 1 verified), as in `g-a1-strip-warnings`. S8 "the emergency manager for Joplin was not sounding the sirens for every tornado warning" (why the rows never join).

## 2. DATUM, SCALE, ORIENTATION
- The SIREN STRIP table at offset 0 (`g-a1-strip-sirens.md` §2: axis x 200 to 1720, 0.9429 px per day, tick band y 380 to 420,
  axis y 440, year labels baseline 482, mark labels y 300 to 345).
- Warnings tally as `g-a1-strip-warnings.md` §2 and §3: 64 px pitch, x 200 to 944, band y 670 to 740, row label baseline 640, "verified" label centre x 924, baseline 772.
- Chip zone: glass chip centred x 960, y 96 to 166.
- Presenter circle may stay on: nothing enters x ≥ 1600, y ≥ 680 (the 2011 mark ends at y 444, the tally at x 944).

## 3. GEOMETRY
- Everything from the copied end state, unchanged. No source line (the chip carries the finding).
- Tally dim: the whole warnings row (marks, row label, "verified") goes 100 % → 40 %.
- Tick dim: the 229 ticks go 70 % → 25 % (red marks, their labels and the bracket stay 100 %).
- Chip: "ONCE A YEAR SINCE 2007 · NIST FINDING 31", glass chip (`references/editing-patterns/ep6-glasscard-popfig-bfmg.html`), row-value tier from tokens.md, centred x 960. Measure: it must end inside x 96 to 1824; if not, two lines "ONCE A YEAR SINCE 2007" / "NIST FINDING 31".

## 4. MUST BE TRUE IN THE PICTURE
1. Frame 0 is the finished a1 picture (no build-in): exactly 229 ticks, 4 red marks at x 216.0, 666.7, 1009.0, 1710.6; 12 tally marks, 1 verified.
2. Nothing joins the two rows: no line, bracket or shared axis; the tally keeps amber and no year labels.
3. The chip says "once a year" and "since 2007" only; it never sits over a mark label (chip bottom 166, labels from 300).
4. The red marks are the brightest things on screen from 5.92 to the end.

## 5. PANEL TEXT (exact) and CUES (z1-s1.words.json)
| element | text | cue |
|---|---|---|
| finished state, both rows float y ±3 px over 4 s (whole host) | base text | frame 0 |
| warnings tally dims 100 % → 40 % (0.5 s) | | "sirens" 0.84 |
| test ticks dim 70 % → 25 % (0.6 s) | | "Outside" 3.42 |
| red marks pulse (scale 1 → 1.18 → 1, 0.5 s, stagger 0.1) and stay lit | | "real" 5.92 |
| chip in, `fromTo(autoAlpha 0, y:24 → 0, 0.4)` | "ONCE A YEAR SINCE 2007 · NIST FINDING 31" (S2) | "once" 6.96 |
| exit: fade-through to the ground (0.6 s) | | 9.46 to 10.06 ("That" 10.06) |
Longest gap with no new tween: 6.96 to 9.46 (2.5 s); the float carries it.

## 6 to 8
`references/mg-brief-template.md` §6, §7, §7a, §8. COMPID `g-z1-strip`.
