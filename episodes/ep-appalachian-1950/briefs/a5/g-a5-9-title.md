# g-a5-9-title: THE WARNING HOUR (A5-S9, signature closing footnote)
Builder: Sonnet 5.5, high effort. Depth: standard. Read `references/mg-quickref.md` and `learnings/mg.md` first.
Start from: `library/inhouse/title-card.html` (layout, motion) and `library/inhouse/outro-brand.html` (channel name treatment). Prefix every id/class `a59-`. Root transparent.
Sits over: `g-a5-8-splitmap` during its A5-S9 window (map fading 1.0 to 0.25, centre kept clear). Mounted on track 3.

## 0. Claim
The episode ends on the channel name while the narrator gives the closing footnote (DESIGN.md "Signature closing footnote"): one storm can bring two dangers, the weather service warns for both, learn what yours sound like.

## 1. Source
- `factcheck/a5-r2.md` rows 46-49 (all CONFIRMED; no new fact). Channel name: DESIGN.md "Signature closing footnote (channel = The Warning Hour)".

## 2. Datum, scale, orientation
Overlay text only. Frame 1920 x 1080; text-safe 96/54 px. Corner circle is OFF under the close card (mg-quickref "Presenter circle": hidden under the close card), so no corner rule here, but keep the corner empty anyway.

## 3. Geometry (px)
- Title: "THE WARNING HOUR" Arial Black 900 120 px `#f2f5f8`, letter-spacing 0.06em, centred x 960, block top y 430, text-shadow `0 3px 26px rgba(0,0,0,0.9)` (no card: the map under it is at 0.25 or lower by the time it is fully on; if the frame read shows the map competing, add a soft radial scrim `rgba(3,5,8,0.55)` 1100 x 360 behind the title, never a box).
- Rule: a 2 px line `#d0121f`, 0 to 520 px wide (scaleX from centre), 22 px under the title.
- No kicker or sub-line: the picture line asks for the title only, and "ONE STORM · TWO SIDES" was already spent in S8. One text tier by design: declare `data-type-ok="title card: single line by design"` on the root.

## 4. Must be true in the picture
1. The title reads "THE WARNING HOUR" exactly, fully on before "This was" (10.34) and held through "Hour." (11.38) plus at least 1.0 s.
2. Nothing else on screen at full strength while the title is on: the map under it is at 0.5 or lower when the title lands and 0.25 by the end.
3. No number, no URL, no call-to-action text (the end ask is elsewhere; this is the footnote only).
4. Exit is a fade-through with the map at the very end, never a hard vanish.

## 5. Panel text (exact) and cues
Text: `THE WARNING HOUR`
Cues from `audio/a5-s9.words.json`:
- 2.84 "Today,": title in (`fromTo` autoAlpha 0, y 30 to 0, scale 0.96 to 1, 0.8 s, power3.out); rule draws 0.3 s later (0.6 s). `/* TODAY @2.84 */`
- 3.70 to 10.30: title drifts y 0 to -10 and scale 1.00 to 1.02, ease none (slow breath; motion every second).
- 11.04 "Warning": rule one brightness pulse (opacity 1 to 0.5 to 1, 0.5 s) and title letter-spacing stays put (never tween letterSpacing). `/* WARNING HOUR @11.04 */`
- 11.72 to 13.72: hold, then all fade to 0 over the last 0.8 s in step with g-a5-8's fade to black.
Host: data-start = A5-S9 audio start + 2.84 (first mark), duration 10.88 s (to A5-S9 13.72). Root `id="g-a5-9-title-root"`.

## 6-8
Contract, tools, done line and receipt: `references/mg-brief-template.md` §6, §7, §7a, §8. Done line 7: composite frames at A5-S9 4.0, 8.0 and 12.0 s over g-a5-8 mounted beneath.
Must not: CSS @keyframes, `id="root"`, a glass or colour-block card behind the title.
