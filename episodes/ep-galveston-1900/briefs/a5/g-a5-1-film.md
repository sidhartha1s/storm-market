# g-a5-1-film · A5-S1 · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules" (and `briefs/intro/_list.md` "Shared rules"). Exemplar: `references/editing-patterns/ep6-glasscard-popfig-bfmg.html`; chip and popfig as built in `compositions/g-intro-3-sept8.html`.

## 0. Claim
The storm had passed by Sunday morning, 9 Sept 1900; the film the viewer then sees was shot in the ruins days later and copyrighted 24 Sept 1900.

## 1. Source
- Sunday 9 Sept: TSHA "September 9 dawned on desolation"; weekday computed (fact-check a5-r1 row 1).
- Film: LoC item 00694301, Edison Manufacturing Co., camera Albert E. Smith, paper print; filmed "probably between September 11-19, 1900"; "copyright to Thomas A. Edison on 24 September 1900" (fact-check a5-r1 rows 2 to 5).

## 2. Datum, scale, orientation
Overlay comp, transparent root, two pictures under it: 0.00 to 7.54 the undated daylight picture (open item 1; until found, the designed ground with a slow light rise, provided by the orchestrator's lower track), 7.54 to end the LoC film. No scale.

## 3. Geometry (px)
- Popfig centred x 960, big line centre y 470: big "SEPT 9, 1900" (Abril, cards.css `.popfig` size), sub "SUNDAY" under it at y 560, Arial 700 32 px `#e8e3d8`.
- Chip bottom-left above the lower-third zone: glass card `left:96px; top:760px`, main line Arial Black 900 44 px `#f2f5f8` "FILMED IN THE RUINS DAYS LATER" (about 900 px wide), tag line Arial 700 22 px `#93a3b2` tracking 4 "© SEPT 24, 1900". Card right edge must stay < 1600.
- Source line top-left `left:96px; top:54px`: "Library of Congress, paper print collection".

## 4. Must be true in the picture
1. The popfig "SEPT 9, 1900" is never on screen over the Broadway film: it is gone (autoAlpha 0) by 4.60, and the film cut is at 7.54 or later.
2. The chip appears only over the film, never over the daylight picture.
3. The film's title is never on screen (flag words).
4. The source line enters with the film, not before.
5. Nothing in x >= 1600, y >= 680.

## 5. Text and cues (a5-s1.words.json, segment 18.64 s)
- 0.16 ("Sunday" 0.16) /* SUNDAY @0.16 */: popfig in (scale 1.35 -> 1, 0.5 s power4.out); sub "SUNDAY" 0.15 s after.
- 0.96 ("9th," 0.96): popfig red line gets a 0.3 s scale pulse 1 -> 1.05 -> 1.
- 4.10 to 4.55: popfig out (scale 0.92, autoAlpha 0, 0.45 s power2.in), after "island." 4.24.
- 7.54 ("In" 7.54): film on the lower track (orchestrator). Source line in at 7.70 (fade + y 8 -> 0, 0.4 s).
- 8.78 ("film" 8.88, "a" 8.78) /* FILM @8.88 */: chip main line in.
- 13.62 ("The" 13.62, "copyrighted" 14.08, "24th" 15.00) /* 24TH @15.00 */: tag line "© SEPT 24, 1900" types on at 15.00 over 0.4 s.
- 16.66 ("Library" 16.66): source line brightens (opacity 0.8 -> 1, 0.3 s).
- Host: A5-S1 0.16 to 18.64 + 1.0 s land time.

## Motion for the whole window
0 to 4.55 popfig drifts (y ±4, 2.4 s yoyo); 4.55 to 7.54 nothing of this comp is on screen: the lower track's light rise moves (a gap of 3 s, under the 4 s idle limit only if the ground moves; say so in the receipt). 7.70 on: source line and chip drift.

## Exit
Chip slides out `x:980, autoAlpha 0, 0.6 s power3.in` in the last 0.6 s; source line fades in the last 0.3 s.

## Footage under it
0 to 7.54: open item 1. 7.54 to end: LoC paper print film, "Searching ruins on Broadway, Galveston" (item 00694301; footage-inventory.md row 9, still "check"), trimmed cut file only.
