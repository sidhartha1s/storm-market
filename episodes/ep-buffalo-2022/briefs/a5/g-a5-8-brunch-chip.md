# g-a5-8-brunch-chip · A5-S7 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: the built `compositions/g-a4-3-day-chip.html` (same chip family: glass chip, source pill, float, exits). Copy it; change strings, cues and the credit swap.

## 0. What this graphic claims
The brunch photo was taken on Christmas Day 2022 in a Cold Spring apartment while the blizzard ran outside. The chip names that date, so it is a claim about that photo and may only sit over it. After the cut, the DVIDS photo (30 Dec 2022) carries only its credit.

## 1. SOURCE
- Brunch photo: Commons "2022 Christmas brunch, Buffalo, New York - 20221225.jpg", Andre Carrotflower, own work, CC BY-SA 4.0, taken Sun 25 Dec 2022, 12:43 PM, file page "while the historic Blizzard of 2022 rages outside": `research/cc-clips-r2.md` row S7; `factcheck/a5-r1.md` row 26. NOT on disk yet (`media/candidates/a5/picks.md`: fetch saved an error page; licence call is the orchestrator's).
- DVIDS 7578226, 105th MP Company soldier hands donated Christmas toys to children during welfare checks, Fri 30 Dec 2022, public domain ("Courtesy Photo"): `research/cc-clips-r2.md` row D6; file `media/a5/A5-S7_c1_dvids-toys-welfare-check.jpg`. DVIDS terms UNCONFIRMED (`research/response.md` section 7).

## 2. DATUM, SCALE, ORIENTATION
Canvas 1920 x 1080, overlay on two stills (root transparent). Lower-third anchor `left:110px; bottom:110px`. Credit pill top-right. Presenter circle may be on: nothing in x >= 1600, y >= 680. Picture cut (index) at S7 +9.74 ("Across the same city"). No scale.

## 3. GEOMETRY (px)
- Chip: glass as g-a4-3 (`rgba(10,16,24,.55)`, blur 18 px saturate 1.15, 1 px `rgba(255,255,255,.14)`, radius 28, padding 22 px 34 px), `left:110px; bottom:110px`. One baseline: "CHRISTMAS DAY" Arial Black `font-weight:900` 52 px `#f2f5f8`, " · " 38 px `#93a3b2`, "2022" Arial Black 900 38 px `#e8c56a`. About x 110 to 720, y 860 to 970.
- Credit pills (glass, radius 14, padding 5 px 12 px, Arial 400 19 px `#c8d3e0`), `right:96px; top:54px` (top-right corner, clear of the presenter corner), two pre-authored pills, one visible at a time:
  - C1 "Photo: Andre Carrotflower / Wikimedia Commons / CC BY-SA 4.0" (over the brunch photo).
  - C2 "New York National Guard, DVIDS" (over the DVIDS photo).
- Type tiers: 52 (big), 38 (mid), 19 (small).

## 4. MUST BE TRUE IN THE PICTURE
1. The chip reads exactly "CHRISTMAS DAY · 2022" and is fully gone (autoAlpha 0) before the cut at 9.74: it never sits over the DVIDS photo (30 Dec).
2. C1 shows only over the brunch photo (0 to 9.74), C2 only over the DVIDS photo (9.74 to end); the swap happens on the cut frame.
3. No place name on screen ("COLD SPRING" is spoken, not shown).
4. The chip never covers the table's centre (the orchestrator checks a settled frame at 6.5 s; if the table sits lower-left, move the chip to `left:auto; right:400px`, still clear of the corner).
5. Nothing in x >= 1600, y >= 680.

## 5. PANEL TEXT (exact) and CUES (seconds from A5-S7 start, `audio/a5-s7.words.json`)
Strings: `CHRISTMAS DAY` · ` · ` · `2022` · `Photo: Andre Carrotflower / Wikimedia Commons / CC BY-SA 4.0` · `New York National Guard, DVIDS`

| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "Four years ago this week," | C1 `fromTo(autoAlpha 0, y:-10 -> 0, 0.4, power2.out)` at 0.10 |
| 5.44 | "Christmas brunch table." @5.44-6.56 | chip in `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.4, power3.out)`; "2022" `fromTo(scale 1.25 -> 1, 0.35, power4.out)` at 5.60 |
| 7.86 | "blizzard ran outside." @7.86-8.92 | chip floats; "CHRISTMAS DAY" brightens `#f2f5f8 -> #ffffff` |
| 0.00 to 9.74 | | chip and C1 float `y: 0 -> -4`, `sine.inOut`, yoyo, finite repeats |
| 8.96 to 9.56 | after "outside." @8.92 | chip out `to(x:-80, autoAlpha 0, 0.6, power3.in)` (gone 0.18 s before the cut) |
| 9.74 | "Across the same city," @9.74 (picture cut) | C1 `set(autoAlpha 0)` and C2 `set(autoAlpha 1)` on the cut frame (a hard swap with the picture cut, not a fade) |
| 9.74 to end | | C2 floats as C1 did |
| 13.44 to 14.04 | after "loved." @13.84 (host end - 0.6) | C2 out `to(autoAlpha 0, y:-10, 0.6, power3.in)` |

Comp duration 14.04 s (wav length). The orchestrator mounts the cut at exactly S7 +9.74; if it moves, move the swap with it.

## 6. CONTRACT
One file `compositions/g-a5-8-brunch-chip.html`, root `id="g-a5-8-brunch-chip-root"`, `data-composition-id="g-a5-8-brunch-chip"`, PAUSED timeline `window.__timelines["g-a5-8-brunch-chip"]`. Ids prefixed `bc-`; classes `bc-chip`, `bc-src` (never `.lt`, `.glasscard`, `.srclab`). Root transparent. Start-hidden in CSS too. The two stills, their pushes, the face blur on the DVIDS still and the CC credit in the description are index/orchestrator work.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a5-8-brunch-chip`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a5-8-brunch-chip`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 7: one frame at 6.5 s over the brunch photo (if it is still not on disk, say so in the receipt and composite over the DVIDS still only for layout, labelled as such) and one at 11.5 s over `media/a5/A5-S7_c1_dvids-toys-welfare-check.jpg`.

## 8. RECEIPT
As the template.
