# g-a1-9-update-card · A1-S9 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md`, `library/inhouse/snippets/tokens.md`, `learnings/mg.md`, template `references/mg-brief-template.md`, `briefs/a1/g-a1-5-watch-timeline.md` (family base: axis, lanes, text card) and `briefs/a1/g-a1-6-warning-card.md`.
Start from: the built `compositions/g-a1-6-warning-card.html` (copy, prefix `uc-`). Frame 0 rebuilds g-a1-6's settled timeline (rail, watch card at 0.5, warning card, in-effect tick and label, 27 h bracket) with no chips and no text card: it follows g-a1-8's fade-through, so the timeline fades up from black over 0 to 0.5.

## 0. What this graphic claims
By 6:48 PM Thu the update raised snow to 2 to 3 ft; gusts still 65 to 70 mph; wind chills to 10 to 20 below. And the earlier 3:54 AM warning had already named the change: "A rapid switch from rain to snow with sharply falling temperatures".

## 1. SOURCE
- Update WWUS41 KBUF 222348, "648 PM EST Thu Dec 22 2022" (CON BZ.W.0001): "Total snow accumulations of 2 to 3 feet with locally higher amounts possible. Winds gusting as high as 65 to 70 mph ... Wind chills as cold as 10 to 20 below zero." `research/nws.md` row 1.6; `factcheck/a1-r1.md` rows 41, 42, 44.
- Earlier warning WWUS41 KBUF 220854: "A rapid switch from rain to snow with sharply falling temperatures into the teens and single digits will result in a flash freeze on Friday." `research/nws.md` row 3.4; `factcheck/a1-r1.md` row 43.
Update card rows (product breaks, re-fetched 28 Oct 26):
```
U0 648 PM EST Thu Dec 22 2022
U1 * WHAT...Blizzard conditions expected. Total snow accumulations of
U2   2 to 3 feet with locally higher amounts possible. Winds gusting
U3   as high as 65 to 70 mph Friday and Friday night. A rapid switch
U4   from rain to snow with sharply falling temperatures into the
U5   teens and single digits will result in a flash freeze on Friday.
U6   Blizzard conditions will develop Friday afternoon lasting into
U7   Saturday night. Wind chills as cold as 10 to 20 below zero.
```
Earlier-warning rows (220854, shown after the swap):
```
E0 354 AM EST Thu Dec 22 2022
E1 * WHAT...Blizzard conditions expected. Total snow accumulations of
E2   1 to 3 feet. Winds gusting as high as 70 mph Friday and Friday
E3   night. A rapid switch from rain to snow with sharply falling
E4   temperatures into the teens and single digits will result in a
E5   flash freeze on Friday. Blizzard conditions will develop Friday
E6   afternoon lasting into Saturday night.
```

## 2-3. GEOMETRY (px)
- Axis, rail, lanes, cards, text card frame (x 170 to 1530, y 186 to 632), row style, chip slot, source slot: g-a1-5 and g-a1-6 unchanged.
- Update card, UPPER lane, centred x 1257.4 (x 1067.4 to 1447.4), y 648 to 752, stem x 1257.4 from 752 to 900; line 1 "UPDATE" Arial Black 900 30 px `#f2f5f8`, line 2 "THU DEC 22 · 6:48 PM" Arial 700 22 px `#d8a13a`.
- Text rows at tops 206 (U0/E0, 26 px `#93a3b2`), then 250 + 44 x (n - 1).
- Chips ONE AT A TIME in the slot (left 200, top 110, Arial Black 900 52 px `#e8c56a`), each replacing the last (old out x:-40, autoAlpha 0, 0.3, power3.in; new in scale 1.2 -> 1, 0.4, power4.out): "2 TO 3 FT", then "GUSTS 65 TO 70 MPH", then "WIND CHILL -10 TO -20°F" (about 830 px at 52 px, ends before x 1100).
- Highlights (amber rect): U2 "2 to 3 feet"; U3 "65 to 70 mph"; U7 "10 to 20 below zero"; after the swap E3 to E4 "A rapid switch from rain to snow with sharply falling" + "temperatures".
- Source line: "NWS Buffalo, WWUS41 KBUF 222348" until the swap, then "WWUS41 KBUF 220854" (one source leaf visible at a time).

## 4. MUST BE TRUE
1. Update dot at x 1257.4 (6:48 PM Thu) on the shared scale; its stem passes right of the warning card (x > 1202.6).
2. Rows are product text character for character; the rapid-switch highlight sits on the 220854 rows, with the 220854 header and source showing, and the warning card on the rail lit while it shows.
3. Chips carry exactly the three strings; "WIND CHILL -10 TO -20°F" matches "10 to 20 below zero".
4. Corner x >= 1600, y >= 680 empty.

## 5. CUES (seconds from A1-S9 start, `audio/a1-s9.words.json`)
| t (s) | spoken word | action |
|---|---|---|
| 0.00 to 0.50 | "By a quarter" | timeline fades up from black |
| 0.68 to 1.30 | "seven Thursday evening," | rail dot at 1257.4 pops; update card drops into the upper lane (y:-60 -> 0, 0.5, power3.out); stem draws |
| 2.14 | "they'd raise" | text card in with U0 to U7 (stagger 0.06); source line in |
| 3.68 to 4.30 | "two to three feet." | chip 1 in (scale 1.2 -> 1, 0.4, power4.out); U2 highlight |
| 6.16 to 7.94 | "65 to 70 miles an hour." | chip 2 in at 6.16; U3 highlight 6.16 to 7.94 |
| 10.32 to 10.64 | "20 below." | chip 3 in at 10.32; U7 highlight 9.66 to 10.64 |
| 11.58 to 12.12 | "The warning had already" | update card dims to 0.5, warning card glows (border `#e8c56a`, 0.3); text card rows swap: U rows out (autoAlpha 0, y:-12, 0.3), E rows in (0.3, stagger 0.05); source swaps; chips dim to 0.4 |
| 14.98 to 17.96 | "rapid switch from rain to snow, with sharply falling temperatures." | E3 highlight 14.98 to 16.34 ("rapid" to "snow"), E3 rest + E4 "temperatures" 17.06 to 17.96, ease none |
| 18.44 to 19.4 | tail | hold (bracket dashes flowing); exit 18.8 to 19.4 text card and chips `to(y:-30, autoAlpha 0, 0.6, power3.in)`; rail and cards stay (g-a1-10 opens on rail + three cards) |
Comp duration 19.4 s.

## 6-8
One file `compositions/g-a1-9-update-card.html`, root `id="g-a1-9-update-card-root"`, `data-composition-id="g-a1-9-update-card"`, PAUSED timeline `window.__timelines["g-a1-9-update-card"]`, prefix `uc-`. Tools, done line (all seven 7a items) and receipt as the template.
