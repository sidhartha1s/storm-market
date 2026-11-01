# g-a1-2-s1-cards · A1-S1 0.00 to A1-S2 end · standard · Sonnet 5.5 high
Shared rules: `_list.md` "Shared rules". Exemplars: `compositions/g-intro-1-pop1891.html` (popfig, already in this episode: copy its CSS, rename ids), `compositions/g-intro-7-clines.html` (lower-third card), cards.css `.srclab`.

## 0. Claim
The date of the page is Thursday, 16 July 1891; the man whose words are in it is Isaac Cline of the Weather Bureau at Galveston.

## 1. Source
- Date and weekday: factcheck/a1-r1.md row 1 (python date check: Thursday; Commons date 1891-07-16); the masthead on the scan reads "THURSDAY, JULY 16, 1891".
- Cline, Weather Bureau, Galveston: sources-cline.md §2 (NWS Heritage: in Galveston by 1889), factcheck/a1-r1.md rows 5, 6.
- Page credit: `media/candidates/a1/provenance.csv` row 1 (Commons, CC0); Portal to Texas History holds the original (act A1-S1 source line).

## 2. Datum, scale, orientation
Overlay comp, transparent root, over g-a1-1-page (lower track, whole window). Zones: centre popup (popfig), lower-third (bottom-left), source line (top-left). No scale.

## 3. Geometry (px)
- Popfig, centred on x 960: sub line "THURSDAY" Arial 700 32 px `#e8e3d8` letter-spacing 6, top 372; big line "JULY 16, 1891" AbrilFig 150 px `#d0121f`, cards.css text-shadow, top 420 (about 1,100 px wide, x ≈ 410 to 1510). Positioned with `left:50%` and `xPercent:-50` set in `tl.set` at 0, never a CSS transform. It sits over the full page (page x 536.9 to 1383.1), which is a still, not a card or map.
- Lower-third card: `left:110px; bottom:110px`; name "ISAAC CLINE" Arial Black 900 52 px `#f2f5f8`; role "Weather Bureau, Galveston" Arial 700 27 px `#f5d98b` letter-spacing 1; 3 px `#d8a13a` accent rule under the name, `scaleX 0 → 1`, left origin, 0.5 s. Card about 620 x 130, right edge ≤ 740 (column 3 starts at screen x 842.7 then: no overlap).
- Source line top-left: "Galveston Daily News, July 16, 1891, p. 5 · Portal to Texas History; Wikimedia Commons, CC0" (two lines allowed, max width 900).
- Tiers: 150 / 52 / 32, 27 / 19.

## 4. Must be true in the picture
1. The popfig's big line is exactly "JULY 16, 1891" (13 characters, 3 words) and the sub is "THURSDAY"; together they match the masthead.
2. The popfig has left before the push starts (gone by 4.62): it never rides the camera move.
3. The lower-third is never on screen with the popfig, and has left before A1-S2's quote card enters (g-a1-3 at S2 0.58).
4. The lower-third does not cover column 3 (right edge ≤ 740 vs column at 842.7).
5. Source line holds the whole window and is the only text in the top-left zone; nothing enters x >= 1600, y >= 680.

## 5. Text and cues (a1-s1.words.json)
- 0.00: source line in (y 8 → 0, autoAlpha 0 → 1, 0.4 s power2.out). /* SRC @0.00 */
- 0.64 ("Thursday,"): sub "THURSDAY" in (autoAlpha, y 12 → 0, 0.35 s). /* THURSDAY @0.64 */
- 1.68 ("16th"): big "JULY 16, 1891" in, popfig enter spec; it holds through "1891." 3.18. /* JULY 16 @1.68 */
- 4.10 to 4.55: popfig exit (sub and big together), done before "Some" 4.62.
- 9.04 ("Klein" = Cline): lower-third in; accent rule draws 9.30 to 9.80; role line in at 9.28 ("had") y 10 → 0, 0.35 s. /* CLINE @9.04 */
- 10.40 to 11.00: lower-third exit, before S1 ends 11.121.
- Source line holds to the host end (A1-S2 8.766 plus the gap), fading out over the last 0.3 s.

## Motion for the whole window
Popfig and lower-third drift y ±4 px from land; the source-line card drifts too (it is alone on screen 4.55 to 9.04 apart from the camera push under it, which also counts as motion in g-a1-1, not here: keep this comp's own drift running so it never idles 4 s).

## Exit
Lower-third slides out left (Shared rules). Source line fades with g-a1-1's fade-through at the end of S2.

## Footage under it
g-a1-1-page for the whole window (the 1891 page).
