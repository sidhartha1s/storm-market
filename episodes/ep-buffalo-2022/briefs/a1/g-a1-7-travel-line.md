# g-a1-7-travel-line · A1-S7 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md`, `library/inhouse/snippets/tokens.md`, `learnings/mg.md`, template `references/mg-brief-template.md`, and `briefs/a1/g-a1-6-warning-card.md` (frame 0 here = g-a1-6's last frame).
Start from: the built `compositions/g-a1-6-warning-card.html` (copy, prefix `tl-`), plus `library/inhouse/quote-card.html` for the big verbatim line.

## 0. What this graphic claims
The Blizzard Warning said it in four plain words: "Travel is strongly discouraged."

## 1. SOURCE
WWUS41 KBUF 220854, PRECAUTIONARY/PREPAREDNESS text, verbatim: "Strong winds will cause significant blowing and drifting snow, frequently reducing visibilities to zero. Travel is strongly discouraged." `research/nws.md` row 6.3 (PRIMARY); `factcheck/a1-r1.md` row 37.

## 2-3. GEOMETRY (px)
- Everything from g-a1-6 at frame 0. Dimming target: every element except text row R8/R9 to opacity 0.12 (rail, cards, chips, other rows, card fill to 0.25).
- Big line `tl-big`: "Travel is strongly discouraged." Georgia italic 400 96 px `#f2f5f8`, centred x 960, top 420 (one line, about 1250 px wide; if the measured width passes 1500 drop to 88 px). It rises out of R8/R9: a ghost copy of "Travel is strongly" (end of R8) + "discouraged." (R9) at 28 px Courier scales and moves to the big line position while cross-fading into the Georgia line (two leaves, crossfade 0.4 s, never both above 0.5 opacity at once).
- Chip "BLIZZARD WARNING · THU DEC 22 · 3:54 AM": Arial 700 30 px `#e8c56a` letter-spacing 2, centred x 960, top 300 (a mid-tier label above the big line; the 52 px chip slot is empty in this comp).
- Source line "NWS Buffalo, WWUS41 KBUF 220854, IEM archive": stays at left 96, bottom 54, full opacity.
- Thin rule under the big line: 3 px `#d8a13a`, centred, width = big line width, top 540, `scaleX 0 -> 1`.
- Type tiers: 96 (big), 30 (chip), 19 (source).

## 4. MUST BE TRUE
1. The big line is exactly "Travel is strongly discouraged." (capital T, period), the product's wording.
2. At most one reading target after 3.0 s: the big line (chip and source are labels).
3. Nothing in the frame corner x >= 1600, y >= 680 except dimmed rail end below 0.15 opacity (the rail ends at x 1540, so nothing).
4. The dim never hides the source line.

## 5. CUES (seconds from A1-S7 start, `audio/a1-s7.words.json`)
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "Then the warning" | frame 0 = g-a1-6 last frame |
| 0.38 to 1.94 | "warning said it in four plain words," | everything except R8/R9 and source `to(opacity 0.12, 1.2, power2.inOut)` from 0.38; R8 highlight fades |
| 1.94 | "words," @1.94 | chip in (y:12 -> 0, autoAlpha, 0.4) |
| 3.02 to 3.88 | "travel is strongly discouraged." @3.02 to 3.88 | ghost words lift (y, scale to 96 px size, 0.6, power3.out) and crossfade into `tl-big` by 3.70; rule draws 3.46 to 3.96 |
| 3.88 to 4.38 | | big line settles; a slow push `scale 1 -> 1.03` on `tl-big` 3.9 to 5.6, ease none |
| 5.0 to 5.6 | tail | exit: all `to(autoAlpha 0, 0.6, power2.in)` (fade-through toward g-a1-8's ground) |
Comp duration 5.6 s.

## 6-8
One file `compositions/g-a1-7-travel-line.html`, root `id="g-a1-7-travel-line-root"`, `data-composition-id="g-a1-7-travel-line"`, PAUSED timeline `window.__timelines["g-a1-7-travel-line"]`, prefix `tl-`. graphics_qc samples [0.4 s, duration - 1.0 s]: at 5.6 s it is measured. Tools, done line (all seven 7a items) and receipt as the template.
