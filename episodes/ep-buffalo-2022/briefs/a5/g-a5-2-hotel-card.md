# g-a5-2-hotel-card · A5-S2 (0 to 7.90 s) · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: `library/inhouse/title-card.html` (stacked centred line reveal) with official `per-word-rise` (`library/official/`, words rise blur-to-sharp). Not a title card: two lines and one figure, quiet.

## 0. What this graphic claims
One family went to a hotel after losing power, and a three-year-old girl lost her life in the hotel's pool. No photo, no name: plain type carries it.

## 1. SOURCE
- WIVB final-count page: "3-year-old girl drowned in a hotel pool after her family stayed at the hotel due to loss of power": `research/deaths.md` section 1 row "final" and section 4 (SECONDARY; name UNCONFIRMED, never shown); `factcheck/a5-r1.md` rows 8 and 9 ("girl", never "daughter"; "whose house" and "to stay warm" are NOT in the source).
- Card wording: the Picture line's "A FAMILY LEFT A DARK HOUSE FOR A HOTEL" is replaced by the narration's own checked words (`_list.md` open item 1).

## 2. DATUM, SCALE, ORIENTATION
Full-frame designed ground from frame 0: `radial-gradient(ellipse at 50% 45%, #0b1016, #030507 78%)` on a layer `hc-ground`. Centre column x 960. No scale. Text inside x 96 to 1824, y 54 to 1026. Corner x >= 1600, y >= 680 empty (nothing sits below y 680 right of x 1600).

## 3. GEOMETRY (px)
- Line 1 "A FAMILY WENT TO A HOTEL": Arial Black `font-weight:900` 58 px `#f2f5f8`, letter-spacing 2, centred x 960, top 380 (box about x 470-1450, y 380-448).
- Line 2 "AFTER LOSING POWER": Arial 700 34 px `#93a3b2`, letter-spacing 8, centred x 960, top 470 (about x 640-1280, y 470-510).
- Figure "AGE 3": "AGE" Arial 700 22 px `#93a3b2` tracking 6 above "3" in 'AbrilFig' 150 px `#f2f5f8` (white, not popfig red: this is a person, not a stat), centred x 960; "AGE" top 560, "3" top 590 (box about y 590-760, x 915-1005). Fonts: `@font-face { font-family:'AbrilFig'; src:url('fonts/AbrilFatface-Regular.ttf'); }`.
- A thin rule 2 px `rgba(255,255,255,.14)`, x 760-1160, y 540, between line 2 and "AGE": draws `scaleX 0 -> 1` from centre.
- Faint light: a radial glow `rgba(127,178,229,0.06)` 900 x 500 behind the text, drifting x -40 -> +40 over the window (keeps something moving).
- Type tiers: 150/58 big, 34 mid, 22 small.

## 4. MUST BE TRUE IN THE PICTURE
1. Strings exactly as §5. No "DARK HOUSE", no "DAUGHTER", no name, no photo, no monogram, no pool image or water icon.
2. One reading target at a time: line 2 lands after line 1 settles; "AGE 3" after both.
3. Nothing in x >= 1600, y >= 680; all text 96 px from the sides.
4. Ground is on at frame 0 (no dark empty frame flash); the comp ends on the ground with no text, so g-a5-3's map ground can cut in clean.

## 5. PANEL TEXT (exact) and CUES (seconds from A5-S2 start, `audio/a5-s2.words.json`)
Strings: `A FAMILY WENT TO A HOTEL` · `AFTER LOSING POWER` · `AGE` · `3`

| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "Some families did leave." | ground on frame 0; glow drift starts (whole window, linear) |
| 1.88 | "family" @1.88, "hotel" @2.70 | line 1 per-word rise: each word `fromTo(autoAlpha 0, y:24 -> 0, filter blur(8px) -> blur(0), 0.4, power3.out)`, stagger 0.14 from 1.88 (last word "HOTEL" lands by 2.70) |
| 3.46 | "after losing power," @3.10-4.22 | line 2 `fromTo(autoAlpha 0, y:14 -> 0, 0.45, power3.out)` at 3.46; rule draws at 3.80, 0.5 s |
| 4.94 | "three-year-old girl" @4.94-5.70 | "AGE" `fromTo(autoAlpha 0, 0.3)` at 4.94; "3" `fromTo(autoAlpha 0, scale 1.2 -> 1, 0.5, power4.out)` at 5.00 |
| 5.70 to 7.10 | "lost her life in the hotel's pool." @5.70-7.58 | lines 1-2 settle to 85 % opacity (0.8 s); "3" holds with a float `y 0 -> -4`, sine, yoyo, 1 repeat |
| 7.30 to 7.90 | after "pool." @7.58 (host end - 0.6) | all text out `to(autoAlpha 0, y:-12, 0.6, power2.in)`, stagger 0.05; ground and glow stay |

Comp duration 7.90 s; g-a5-3's host starts at S2 +7.90.

## 6. CONTRACT
One file `compositions/g-a5-2-hotel-card.html`, root `id="g-a5-2-hotel-card-root"`, `data-composition-id="g-a5-2-hotel-card"`, PAUSED timeline `window.__timelines["g-a5-2-hotel-card"]`. Prefix `hc-`. Start-hidden in CSS too; `filter` tweens only on the word spans. Three type tiers are present (150/58, 34, 22), so no flat-type exemption is needed. Rest: `references/mg-quickref.md`. Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a5-2-hotel-card`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a5-2-hotel-card`.

## 7a. DONE LINE
All seven items of the template 7a. Item 7: full-frame, no footage; read one settled frame at 6.5 s.

## 8. RECEIPT
As the template.
