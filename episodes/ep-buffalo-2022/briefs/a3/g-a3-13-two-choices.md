# g-a3-13-two-choices · A3-S11 2.90-8.60 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: the chip in `compositions/g-intro-2-toll-chips.html` (glass chip at the lower-third anchor). Copy, prefix `tw-`, two chips.

## 0. What this graphic claims
Anyone stuck out there had two choices, each with a limit: stay, and the drifts bury the car; walk, and frostbite can start in as little as 30 minutes.

## 1. SOURCE
- Drifts: `research/nws.md` Q6 row 6.3 (Blizzard Warning: "Strong winds will cause significant blowing and drifting snow", PRIMARY); `factcheck/a3-r1.md` row 58 CONFIRMED (and her message that the snow would reach her waist).
- Frostbite 30 minutes: WSWBUF 221909 (`factcheck/a3-r1.md` row 37, PRIMARY), as g-a3-7.
- Footage: Andre Carrotflower, "Laurel Street during December 2022 Buffalo, New York blizzard - 20221224 - 03 (night)", Sat 24 Dec 2022 8:55 PM, CC BY-SA 4.0 (`research/cc-clips-r2.md` S2). Not confirmed to show a single car under a streetlight (`_list.md` open item 6).

## 2. DATUM, SCALE, ORIENTATION
Overlay on footage (slow push on the still, done in index.html), root transparent. Corner x >= 1600, y >= 680 empty.

## 3. GEOMETRY (px)
- Chip `tw-c1` and `tw-c2`, one at a time, glass surface (radius 28), `left:110px; bottom:110px`, padding 22 px 34 px, hugs text, one line baseline-aligned:
  - Verb span Arial Black 900 52 px `#e8c56a`: "STAY:" / "WALK:"; 16 px gap; rest span Arial Black 900 52 px `#f2f5f8`.
  - C1 "STAY:" + "THE CAR GETS BURIED" (about 26 characters, x about 110-1100).
  - C2 "WALK:" + "FROSTBITE IN AS LITTLE AS 30 MIN" (about 38 characters at about 37 px = 1400 px: too wide). C2 is two lines instead: line 1 "WALK:" + "FROSTBITE IN AS" ; line 2 "LITTLE AS 30 MIN" (left-aligned with "FROSTBITE"), line-height 60. Box about x 110-830, y about 790-970.
- Credit, Arial 400 19 px `#c8d3e0` on a glass pill, `right:96px; top:54px`: "Photo: Andre Carrotflower / Wikimedia Commons / CC BY-SA 4.0" (whole window).
- Source pill `left:110px; bottom:54px`: "NWS Buffalo Blizzard Warning, 22 Dec 2022" (on with C2 only; C1 is the act's own summary of row 58).
- Type tiers: 52 big (the chips carry one reading each); credit and source 19 small. Only 3-4 text nodes: state the count; if graphics_qc flat-type fires, add nothing, declare the two-tier exemption per `references/mg-quickref.md` "Gate-readable authoring".

## 4. MUST BE TRUE IN THE PICTURE
1. One chip at a time, in voice order: STAY, then WALK.
2. Chip strings exactly as §3 (the Picture line's text, C2 wrapped on two lines without changing a word).
3. Nothing over the car in the settled frame (orchestrator read over the still; if the car is lower-left, move the chips to `right:` side, ending left of x 1600, and above y 680).
4. The CC credit is on screen for the whole window.
5. No graphic after 8.60: the closing question plays over the clean picture.

## 5. PANEL TEXT (exact) and CUES (segment seconds, `audio/a3-s11.words.json`; host starts at 2.90, comp-local = t - 2.90)
Strings: `STAY:` · `THE CAR GETS BURIED` · `WALK:` · `FROSTBITE IN AS` · `LITTLE AS 30 MIN` · `Photo: Andre Carrotflower / Wikimedia Commons / CC BY-SA 4.0` · `NWS Buffalo Blizzard Warning, 22 Dec 2022`
| t (s) | spoken word | action |
|---|---|---|
| 2.90 | (before "Stay" @2.96) | credit visible from frame 0 |
| 2.96 | "Stay" @2.96 | C1 in `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)`, verb span first, rest at 3.36 |
| 4.28 | "burying" @4.28 | C1 sinks a little: `to(y:8, 0.6, power2.inOut)` (the car going under), then floats |
| 4.74-5.10 | "or" @4.74 | C1 out `to(x:-80, autoAlpha 0, 0.36, power3.in)` |
| 5.24 | "walk" @5.24 | C2 in (as C1); source pill in |
| 6.14 | "cold" @6.14 | "LITTLE AS 30 MIN" line brightens to `#ffffff` 0.25 s |
| 7.24 | "door," @7.24 | C2 holds, float y 0 -> -4 |
| 8.00-8.60 | "whichever way" @8.00 | C2, pill and credit out `to(x:-80, autoAlpha 0, 0.6, power3.in)` |
Comp duration 5.70 s.

## 6. CONTRACT
One file `compositions/g-a3-13-two-choices.html`, root `id="g-a3-13-two-choices-root"`, `data-composition-id="g-a3-13-two-choices"`, PAUSED timeline `window.__timelines["g-a3-13-two-choices"]`. Prefix `tw-`. Rest: `references/mg-quickref.md`.
Footage under it: Carrotflower S2 night still (or V3 per `_list.md` item 6), mounted for the whole host window and the rest of A3-S11. Its credit must stay on screen while the still is up after 8.60 too: that is the orchestrator's index overlay.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a3-13-two-choices`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a3-13-two-choices`. Repeat: "30 MIN" repeats g-a3-7's chip about 40 s earlier (callback, not the same frame).

## 7a. DONE LINE
All seven items of the template 7a. Item 7: one frame per chip over the still.

## 8. RECEIPT
As the template.
