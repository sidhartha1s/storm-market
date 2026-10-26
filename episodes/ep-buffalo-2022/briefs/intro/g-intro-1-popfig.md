# g-intro-1-popfig · H1-S1 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
PROVISIONAL hook: if the owner picks another hook shape, this graphic is redone.

## 0. What this graphic claims
Where and when: Buffalo, New York, on 23 December 2022, the day the blizzard began. It is the only graphic on Paul (owner: no graphic on him beyond the date/place popfig).

## 1. SOURCE
- Date: the Blizzard Warning for Erie County was in effect from 7 AM Fri 23 Dec 2022 (`research/nws.md` row 1.2, product WWUS41 KBUF 220854, IEM archive). Fact check: `factcheck/intro-r3.md` row 3 ("Picture/popfig 'BUFFALO, NY · DEC 23, 2022' ... CONFIRMED").
- Place: Buffalo, Erie County, New York (`edit_script.md` title line; `research/deaths.md`).

## 2. DATUM, SCALE, ORIENTATION
Canvas 1920 x 1080. No scale. Horizontal centre x = 960 unless Paul's framing puts his face there (see section 3). Text-safe box: x 96 to 1824, y 54 to 1026.

## 3. GEOMETRY (px at 1920 x 1080)
- Popfig block, centred on x = 960, no colour-block card behind it (popfig rule). Two lines:
  - `pf-sub` (top line): "BUFFALO, NY", Arial Black, `font-weight:900`, 38 px, colour `#f4f0e8` (Beige stamp text), letter-spacing 0.06em, top edge y = 640, height about 44.
  - `pf-big` (second line): "DEC 23, 2022", 'AbrilFig' (Abril Fatface, vendored `fonts/AbrilFatface-Regular.ttf` per tokens.md), 150 px, colour `#d0121f` (Popfig red), letter-spacing 0.04em, text-shadow as `.popfig .pf-big` in `library/inhouse/snippets/cards.css`. Top edge y = 696, glyph box about 696 to 846. Width about 1000 px, so x about 460 to 1460.
  - Local scrim only as `.popfig::before` in `episodes/ep-enderlin-2025/index.html` line 36 (soft radial dark, no hard edge), never a block card.
- Default placement is the lower-middle band (chest height), not mid-face. The clip does not exist yet. When it does, read one frame at 0.8 s: if the popfig covers his face, mouth or the hat brim, move the whole block down or into the empty side (centre x on the empty half), keeping it inside the text-safe box. Report the final x/y.
- Bottom-right: Flow's watermark star is covered by the channel logo at (1740, 900), 96 px (`references/mg-quickref.md` "Logo on every full-frame clip"). Nothing of the popfig enters x 1680 to 1800, y 840 to 960.
- No presenter circle in this segment (Paul is full frame).

## 4. MUST BE TRUE IN THE PICTURE
1. Exactly two strings on screen: "BUFFALO, NY" and "DEC 23, 2022". Nothing else is written on Paul.
2. The red line is 16 characters or fewer (it is 12) and 3 words or fewer (it is 3).
3. No part of the popfig covers Paul's eyes, mouth or hat brim in any frame from 0.2 s to its exit.
4. The popfig is fully landed (opacity 1, final scale) by 0.80 s, inside the first second.
5. It is gone (autoAlpha 0) before "some" at 5.16 s, so "some of those calls never got an answer" plays on his face alone.

## 5. PANEL TEXT (exact) and CUES (seconds from H1-S1 start, `audio/h1-s1.words.json`)
Text: `BUFFALO, NY` (sub) and `DEC 23, 2022` (big). Proper case rule does not apply: popfig caps are the channel style.
| t (s) | spoken word | action |
|---|---|---|
| 0.20 | "call" @0.14 | sub "BUFFALO, NY" in: `fromTo(autoAlpha 0, y:18 -> 0, 0.35, power3.out)` |
| 0.34 | "911" @0.34 | big "DEC 23, 2022" in: `fromTo(autoAlpha 0, scale 1.35 -> 1, 0.45, power4.out)` (the Abril punch), landed 0.79 |
| 0.79 to 5.00 | through "Christmas," @4.28 | hold with a slow push `to(scale 1 -> 1.04, 4.2 s, ease none)` on the block (continuous motion) |
| 3.68 | "Buffalo" @3.68 | sub line brightens `to(color #ffffff, 0.3)` and a 2 px beige underline draws under it `scaleX 0 -> 1, 0.4, power2.out` (the voice names the place) |
| 4.95 to 5.10 | after "Christmas," (next word "some" @5.16) | exit: `to(autoAlpha 0, y:-30, 0.35, power3.in)`, ends 5.10 |
Comp duration 5.4 s (last beat 5.10 + land). Spoken time in a comment at each tween (`/* 911 @0.34 */`).
TIMING CAVEAT: these cues are the TTS wav's. Paul's clip will be his own take: when `ins-paul-1` exists, re-cue every row to its own words.json (same words), keeping the rules in section 4.

## 6. CONTRACT
One file `compositions/g-intro-1-popfig.html`: `<template>` + `<style>` + root `<div id="g-intro-1-popfig-root" data-composition-id="g-intro-1-popfig" data-width="1920" data-height="1080">` (never `id="root"`) + script building a PAUSED gsap timeline at `window.__timelines["g-intro-1-popfig"]` (`window.__timelines = window.__timelines || {}` first). Root transparent. Element ids prefixed `p1-`. Do not reuse index.html class names: name classes `p1-sub`, `p1-big`, not `.popfig`. Start-hidden elements hidden in CSS too. Two tiers by design (popfig): put `data-type-ok="date/place popfig: two lines by design"` on the root. Wrap the block in one timed element so overlap_check sees it. No other rules restated here: `references/mg-quickref.md`.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-intro-1-popfig`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-intro-1-popfig`.

## 7a. DONE LINE
All seven items of `references/mg-brief-template.md` 7a. Item 7 (overlay over the real picture) waits for `ins-paul-1`: until then say "not verified over footage, clip missing".

## 8. RECEIPT
As the template: start/end times, loops, section 4 failures and fixes, gate line, PNG folder, final popfig x/y.
