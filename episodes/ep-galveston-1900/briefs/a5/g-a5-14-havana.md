# g-a5-14-havana · A5-S9 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `library/inhouse/title-card.html` (typeset title), `references/editing-patterns/g-cite-tape.html` (label card).

## 0. Claim
In October and November 1900, two Havana papers ran pieces about Stockman, the Bureau's man there, and clippings of them sit in the Weather Bureau's own files at the National Archives (RG 27, box 1475).

## 1. Source
Pietruska (2016), JGAPE 15(4), fn 83 and 87: "Mr. Stockman," La Discusión, Oct. 27, 1900, box 1475, "with a translation in Diario de la Marina, Oct. 30, 1900"; La Discusión Nov. 14, 1900, translated clipping enclosed in "Montrose W. Hayes to Moore, Nov. 18, 1900, box 1475" (sources-cuba.md §5 and §6; fact-check a5-r1 rows 36 to 42). CONFIRMED as archive citations only: text and tone unseen. Author "Jamie L. Pietruska" (row 41).

## 2. Datum, scale, orientation
Full-frame designed card (tokens radial background). No 1900 masthead scan exists on disk: the mastheads are typeset in a period serif and must read as a title card, not a fake scan (no paper texture, no fake print damage).

## 3. Geometry (px)
- Masthead M1: `left:160px; top:220px; width:760px`, beige cite card `rgba(232,222,200,.90)`, padding 40 px; "La Discusión" Georgia bold 72 px `#2a2622`; under it "HAVANA · 1900" Arial 700 22 px `#6b6257` tracking 4.
- Masthead M2: `left:1000px; top:220px; width:760px`, same: "Diario de la Marina".
- Date chips (glass) under each: C1 under M1 at top 480: "LA DISCUSIÓN · OCT 27 · NOV 14, 1900" main Arial Black 900 34 px `#f2f5f8`; C2 under M2: "DIARIO DE LA MARINA · OCT 30, 1900". Each ≤ 760 wide; if C1 wraps, two lines.
- Box label B: centred x 960, top 640: a card styled as an archive box end label, `#f4f0e6` with `#2a2622` text, 520 x 200: "NATIONAL ARCHIVES" Arial 700 22 px tracking 4, "RG 27 · BOX 1475" Arial Black 900 56 px, "WEATHER BUREAU RECORDS" Arial 700 22 px. Bottom 840; x 700 to 1220: clear of the corner.
- Source line top-left: "National Archives, Weather Bureau records, RG 27, box 1475, as cited by Jamie L. Pietruska (2016)".

## 4. Must be true in the picture
1. Diacritics right: "Discusión" with the accent; "Diario" not "Dario".
2. No word implies the clippings' tone (no "attack", "criticism", "blamed").
3. Dates exactly OCT 27, NOV 14 (La Discusión) and OCT 30 (Diario), 1900.
4. Masthead cards never cover the chips; the box label never covers either chip.
5. Dup-fact: "1900" appears on both chips and the mastheads' "HAVANA · 1900": declare `data-repeat-ok="one year on several labels"` on the two masthead year leaves after a frame read, or drop "· 1900" from the mastheads (preferred: drop it, write "HAVANA").

## 5. Text and cues (a5-s9.words.json, segment 20.90 s)
- 0.00: background; 0.46 ("Havana," 0.46): source line in.
- 1.06 ("papers" 1.06): both mastheads rise in, empty of chips, 0.2 s apart.
- 1.60 ("stockmen" 1.60) /* STOCKMAN @1.60 */: a small glass tag "W. B. STOCKMAN · BUREAU, HAVANA" Arial 700 24 px `#f2f5f8` above the mastheads, centred, top 120. (Row: acts/a2.md A2-S4, MWR "W. B. Stockman, Forecast Official".)
- 3.48 ("October" 3.48): tag out.
- 5.20 ("Discusión" 5.20) /* DISCUSION @5.20 */: M1 brightens; C1 in at 5.40 with "OCT 27" first, "NOV 14, 1900" at 4.18 is past, so the whole line in at 5.40.
- 6.74 ("Dario" 6.74) /* DIARIO @6.74 */: M2 brightens; C2 in at 7.44 ("Marina").
- 10.46 ("Clippings" 10.46): mastheads and chips scale to 0.85 and rise 60 px together (one move, 0.6 s power2.inOut) to make room.
- 13.42 ("National" 13.42) /* ARCHIVES @13.72 */: box label B rises in from y +80 at 13.42.
- 19.60 ("Washington" 19.60): B pulses once (scale 1 -> 1.04 -> 1); 20.00 ("kept").
- Host: 0.00 to 20.90 + 1.0 s land time.

## Motion for the whole window
Cards drift (y ±4, offset phases); slow push 1.00 to 1.04 over the host. Between 7.44 and 10.46 the drift carries it (3 s).

## Exit
All cards slide out right, 0.08 s stagger, last 0.6 s.

## Footage under it
None (full-frame card).
