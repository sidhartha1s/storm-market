# g-a1-8-afd-rare · A1-S8 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md`, `library/inhouse/snippets/tokens.md`, `learnings/mg.md`, template `references/mg-brief-template.md`, `briefs/a1/g-a1-1-afd-scroll.md` (family base) and `briefs/a1/g-a1-7-travel-line.md` (the big-line lift).
Start from: the built `compositions/g-a1-1-afd-scroll.html` (panel, header, rows; no scroll needed here) and the lift from `compositions/g-a1-7-travel-line.html`. Prefix `ar-`.

## 0. What this graphic claims
74 minutes after the warning (5:08 AM Thu 22 Dec) the discussion admitted: "True blizzard conditions are rare in Western NY, and it's unusual to even consider blizzard headlines this far in advance of a storm."

## 1. SOURCE
AFD FXUS61 KBUF 221008, "508 AM EST Thu Dec 22 2022". `research/nws.md` row 6.1 (PRIMARY); `factcheck/a1-r1.md` rows 38 to 40. On screen the product's "NY" stays (the voice says "New York"). Rows (re-fetched 28 Oct 26, product breaks):
```
header: Area Forecast Discussion / National Weather Service Buffalo NY / 508 AM EST Thu Dec 22 2022
C0 .SHORT TERM /FRIDAY THROUGH SUNDAY NIGHT/...
C1 ...A DANGEROUS WINTER STORM WILL IMPACT THE REGION FRIDAY THROUGH
C2 MUCH OF THE CHRISTMAS WEEKEND...
C3 (gap)
C4 True blizzard conditions are rare in Western NY, and it's unusual to
C5 even consider blizzard headlines this far in advance of a storm.
C6 However, the magnitude of this storm justifies this consideration.
C7 The worst conditions will be downwind of the lakes, particularly
C8 Lake Erie where the southwest winds will be the strongest. Expect
```

## 2-3. GEOMETRY (px)
- Ground, panel (x 170 to 1530, y 200 to 900), header (tops 226, 262, 298, 26 px), product id "FXUS61 KBUF 221008" (right-aligned to 1470, top 230), divider y 344: exactly g-a1-1.
- Rows C0 to C8 static (no scroll): Courier New 700 28 px, left 230, tops 376 + n x 44 (C8 top 728). C0 to C2 `#93a3b2`, rest `#dfe7ee`.
- Chip "THU DEC 22 · 5:08 AM": Arial Black 900 52 px `#e8c56a`, left 200, top 110.
- Big quote `ar-big`, two lines, Georgia italic 400 64 px `#f2f5f8`, centred x 960, tops 380 and 470: line 1 "True blizzard conditions are rare in Western NY," line 2 "and it's unusual to even consider blizzard headlines" and line 3 at top 560: "this far in advance of a storm." (three lines; if any line measures over 1500 px drop all to 58 px). Opening and closing quote marks are NOT added: the text is shown as the product's own sentence, attributed by the chip and source.
- Amber rule 3 px `#d8a13a` under the quote, centred, top 650, width 600.
- Source line "NWS Buffalo Area Forecast Discussion, FXUS61 KBUF 221008": Arial 19 `#c8d3e0`, left 96, bottom 54.
- Type tiers: 52 / 64 (big), 26 to 28 (mid), 19.

## 4. MUST BE TRUE
1. Card rows and the big quote are the product's text character for character ("Western NY", "it's", "this far in advance of a storm.").
2. When the quote lifts, the panel dims to 0.12 so one reading target remains; no quote line sits over a readable row.
3. Chip date/time agrees with the header (508 AM EST Thu Dec 22 2022).
4. Corner x >= 1600, y >= 680 empty; margins kept.

## 5. CUES (seconds from A1-S8 start, `audio/a1-s8.words.json`)
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "A little over an hour later," | ground on (fade up from black 0 to 0.3, it follows g-a1-7's fade-through); chip in at 0.12 (scale 1.2 -> 1, 0.4) |
| 0.60 | "hour" @0.72 | panel in (y:60 -> 0, 0.6, power3.out); header rows stagger 0.9, 1.1, 1.3; source in |
| 1.76 | "discussion" @1.76 | rows C0 to C8 in (stagger 0.08) |
| 2.84 to 3.82 | "how unusual all this was." | highlight rects on C4 and C5 (whole rows) `scaleX 0 -> 1` ease none, 2.84 to 3.82 |
| 4.76 to 5.20 | "It said true" | panel and rows `to(opacity 0.12, 0.6)`; big line 1 lifts from C4 (fromTo y:40 -> 0, autoAlpha, 0.5, power3.out) at 5.14 |
| 5.14 to 8.16 | "true blizzard conditions are rare in western New York." | line 1 holds; its words "rare" brighten amber at 6.62 |
| 8.94 | "Even considering" @8.94 | line 2 in like line 1 |
| 10.60 | "this far ahead" @10.60 | line 3 in; rule draws 11.12 to 11.62 |
| 11.62 | "unusual," @11.62 | "unusual" in line 2 brightens amber |
| 12.76 to 14.2 | "it said." + tail | slow push on the quote `scale 1 -> 1.03`, 12.0 to 14.2; exit 13.6 to 14.2 all `to(autoAlpha 0, 0.6, power2.in)` |
Comp duration 14.2 s.

## 6-8
One file `compositions/g-a1-8-afd-rare.html`, root `id="g-a1-8-afd-rare-root"`, `data-composition-id="g-a1-8-afd-rare"`, PAUSED timeline `window.__timelines["g-a1-8-afd-rare"]`. Note: the big quote repeats C4/C5 text; overlap_check's dup-fact counts digit strings only, so no declaration is needed, and the panel sits at 0.12 (under overlap_check's 0.15 visibility floor) while the quote shows. Tools, done line (all seven 7a items) and receipt as the template.
