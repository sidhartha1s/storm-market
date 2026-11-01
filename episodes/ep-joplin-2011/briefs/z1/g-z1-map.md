# BRIEF · g-z1-map · "inside, right where you'd have gone; nothing below them" · DEEP (Opus 5.5, high) · a state of the MASTER MAP

Episode ep-joplin-2011, segment Z1-S1 (second part), the act's [RS] visual event. Full-frame MG on the channel ground. Host from
z1-s1 "That" 10.06 to the z1-s1 wav end 22.92 (12.86 s; extend to the z1-s3 mount if the orchestrator leaves a gap). It comes in on a cut
from `g-z1-strip`; `g-z1-board` follows on a cut.
Base: the MASTER MAP. Copy the BASEMAP block of `compositions/g-intro-map.html` (grid, city outline, streets, below-ground line, push
values) and the DOT LAYER block of `compositions/g-intro-map-dots.html` (154 Table 4-3 dots, lit 135 inside / 19 outside). Open on the
state `g-a6-map135` opens on, minus its chip and source line. Drop the rail card, the "0" on the line and the "154 placed" label
(the chips and source lines carry those facts once). Never redraw a dot, outline or line.
Open numbers: none.
Host-local time = word start − 10.06 (computed by `python3`, 17 Oct 26); both are given below.

## 0. What this graphic claims
Most of the people the tornado took were inside buildings, 135 of 155 (T3). NIST found no evidence any of those killed were below
ground (H5). 82 percent of Joplin homes had no basement (H1), and neither the city nor the county had a public shelter (H3, H4).

## 1. SOURCE
- T3 "Of the 155 impact-related fatalities, 135 (87 percent) involved persons who are known to have been located inside structures during the tornado." NIST NCSTAR 3, E.4.2 Finding 40.
- H5 "NIST found no evidence that any of those killed were located underground during the tornado." NIST NCSTAR 3, E.4.2 Finding 46.
- H1 "Also, 82 percent of the homes in Joplin lacked basements." NIST NCSTAR 3, E.4.2 Finding 20.
- H3 "There were no community shelters or safe rooms in the City of Joplin or Jasper County at the time of the May 22, 2011, Joplin tornado." Finding 20. H4 "the City did not own or operate any public storm shelters." E.4.1. (Spoken only; no text drawn for it, `_list.md` Ambiguous 1.)
- Dot positions: the base, from NIST Table 4-3 (T11: 135 inside, 19 outside, 154 placed).

## 2. DATUM, SCALE, ORIENTATION
- As the master-map base: north up, its px-per-mile `s`, city outline box, chip zone y 96 to 166 clear.
- BELOW-GROUND LINE: y 880, x 200 to 1500, 2 px `#93a3b2` (`g-intro-map.md` §3).
- Push: the T1-S3 values in `g-intro-map.md` §3, unchanged: uniform scale 1.00 → 1.3292 about the comp, translated so the line's centre
  (850, 880) lands at (960, 540); the line then spans x 96 to 1824. Under 1.5x, so linear scale with ease power2.inOut is fine.
- Source line: x 96, baseline 1010, Arial 700 20 `#c8d3e0`, one at a time.

## 3. GEOMETRY
- Frame 0: base map and the empty below-ground line with its "Below ground" label; dots hidden (CSS opacity 0 plus `tl.set`).
- Dot stamp: 135 inside dots `fromTo(scale 0 → 1, autoAlpha 0 → 1)`, stagger by distance from the map centre, 0.8 s total; the 19 outside dots land with them at 0.3.
- Dots breathe from the stamp to host end: inside dots scale 1 → 1.15 → 1, 1.6 s, finite repeats, stagger by distance.
- Inside-dot pulse on "inside": scale 1 → 1.25 → 1, 0.5 s, all 135 at once.
- Push onto the line, then the HUD label "Below ground" (Arial 700 26 `#93a3b2` tracking 8, left x 110, baseline 512, fixed layer, not scaled), as T1-S3. The base's own "Below ground" label at baseline 864 fades to 0 before the push starts, because text never rides a move.
- Pull-out: scale 1.3292 → 1.00 back to the base framing, power2.inOut; the HUD label fades out (0.3 s) before the pull-out starts.
- City outline lift: stroke opacity 70 % → 100 % (0.5 s) and holds. No label.
- Chips (glass chip, row-value tier, centred x 960, y 96 to 166), one at a time, each in `fromTo(autoAlpha 0, y:24 → 0, 0.4)`, out `autoAlpha 0, 0.3`:
  "135 INDOORS", then "NONE FOUND BELOW GROUND", then "8 IN 10: NO BASEMENT".
- Exit: cut to `g-z1-board` on the host end; ~1 s land time after the last tween (city lift ends 21.86, host end 22.92).

## 4. MUST BE TRUE IN THE PICTURE
1. After the stamp: 135 dots at full strength inside building outlines and 19 at 0.3; no dot added, moved or removed against the base.
2. The below-ground line is empty in every frame: no dot, mark or number on it.
3. One chip at a time; each chip shows with its own source line and never with another chip's source line.
4. The Finding 46 source line says "those killed", so it never reads as "no one was below ground" (facts.md NOTE under B49).
5. After the push the line runs x 96 to 1824 at y 540, and the chip, HUD label and source line touch neither it nor each other.
6. Presenter corner: if any dot, outline or label lies in x ≥ 1600, y ≥ 680 at any point (the pull-out included), the circle is off for this comp; tell the orchestrator. Never move a dot to clear it.
7. No text from `g-a6-map135` ("MOST WERE INDOORS") appears here.

## 5. PANEL TEXT (exact) and CUES (z1-s1.words.json)
| element | text | cue: word @ segment s (host-local s) |
|---|---|---|
| map in on the cut, base framing, line empty | base labels | "That" @ 10.06 (0.00) |
| dot stamp, 0.8 s; breathe starts after it | | "evening," @ 10.24 (0.18) |
| chip 1 | "135 INDOORS" (T3) | "most" @ 11.28 (1.22) |
| source line 1 | "135 of 155 impact-related · NIST Finding 40" (T3) | "most" @ 11.28 (1.22) |
| inside-dot pulse | | "inside," @ 12.98 (2.92) |
| chip 1 out; base line label fades; push 0.8 s | | "right?" @ 13.92 (3.86) to 14.72 (4.66) |
| HUD label | "Below ground" | "gone." @ 14.76 (4.70) |
| chip 2 | "NONE FOUND BELOW GROUND" (H5) | "gone." @ 14.76 (4.70) |
| source line 2 (replaces 1) | "no evidence any of those killed were underground · NIST Finding 46" (H5) | "gone." @ 14.76 (4.70) |
| chip 3 (replaces 2) | "8 IN 10: NO BASEMENT" (H1) | "basement," @ 17.52 (7.46) |
| source line 3 (replaces 2) | "82% of homes · no basement · NIST Finding 20" (H1) | "basement," @ 17.52 (7.46) |
| HUD label out (0.3 s), then pull-out 2.0 s | | "there" @ 18.80 (8.74) to 20.80 (10.74) |
| city outline lift (0.5 s) | | "city" @ 21.36 (11.30) |
| hold, dots breathe; cut | | to wav end 22.92 (12.86) |
Longest gap with no new tween: 7.46 to 8.74 host (1.28 s); the breathe runs throughout.
Whisper wrote "right? Where" (13.92, 14.32) for the script's "right where"; cue words are as words.json spells them.

## 6 to 8
`references/mg-brief-template.md` §6, §7, §7a, §8. COMPID `g-z1-map`. The receipt states the dot counts read off a frame (135 full, 19 at 0.3) and the push transform computed from §2.
