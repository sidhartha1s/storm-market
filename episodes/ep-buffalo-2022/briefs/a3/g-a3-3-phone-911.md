# g-a3-3-phone-911 · A3-S2 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`. Template: `references/mg-brief-template.md`.
Start from: chip + source pill in `compositions/g-intro-2-toll-chips.html`. No phone exemplar exists in the library: build the phone from the geometry below (plain SVG/HTML, no device photo).

## 0. What this graphic claims
She called 911 and stayed with her car; around 3 that afternoon she sent a video to a group chat with her sisters. Nothing from her phone is shown: the thumbnail is a blank frame.

## 1. SOURCE
- Called 911, stayed with her car, crews could not reach her: `research/deaths.md` section 4 (CBS/CNN, SECONDARY).
- "Taylor sent a video to a group chat with her sisters at around 3 p.m. on Friday.": `factcheck/a3-r1.md` "New evidence" (CBS/CNN quote).
- URL: https://www.cbsnews.com/miami/news/woman-in-buffalo-found-dead-in-her-car-after-getting-trapped-by-snow-family-says/
- Only one timestamp is sourced (about 3 PM Fri). Show ONE thumbnail; no other times (`_list.md` open item 4).

## 2. DATUM, SCALE, ORIENTATION
Full-frame designed ground (channel radial gradient, layer `ph-ground`, on from frame 0). Light snow particles drift over the ground (behind the phone). Corner x >= 1600, y >= 680 empty.

## 3. GEOMETRY (px)
- Phone `ph-body`: rounded rect x 760-1160 (400 wide), y 120-940 (820 tall), radius 56, fill `#0b1016`, 3 px stroke `#93a3b2`. Screen `ph-screen`: inset 18 px (x 778-1142, y 138-922), radius 40, fill `#04070a`.
- Call state (layer `ph-call`, centred on x 960):
  - "CALLING" Arial 700 22 px `#93a3b2` tracking 6, top 260.
  - "911" Arial Black 900 120 px `#f2f5f8`, top 310 (box y 310-430).
  - Red end-call disc: circle r 44 at (960, 800), fill `#c0392b`, white handset glyph (SVG, no text).
  - Ring pulse around "911": two circles r 90 -> 170 at (960, 370), stroke `#7fb2e5` 3 px, opacity 0.6 -> 0.
- Chat state (layer `ph-chat`):
  - Header bar y 138-218, "SISTERS" Arial 700 26 px `#dfe7ee` tracking 4, centred, top 162.
  - Thumbnail `ph-thumb`: rect x 830-1090 (260 wide), y 330-676 (346 tall, 3:4), radius 18, fill `#15202b`, 1 px `rgba(255,255,255,.14)`; centred play triangle 54 px `#dfe7ee` at 70 % opacity. No image inside, ever.
  - Under it, timestamp "FRI · ABOUT 3 PM" Arial 700 26 px `#e8c56a` tracking 2, centred x 960, top 700.
- Chip "CALLED 911": glass chip, `left:110px; bottom:110px`, Arial Black 900 52 px `#f2f5f8` (x about 110-500, y about 862-970). Clear of the phone (phone left edge x 760).
- Source pill "CNN via CBS News": `left:110px; bottom:54px`, as g-intro-2 `tc-src`.
- Type tiers: 120/52 big, 26 mid, 22/19 small.

## 4. MUST BE TRUE IN THE PICTURE
1. The thumbnail is blank: no face, no snow image, no frame grab, no waveform.
2. Exactly one timestamp on screen, "FRI · ABOUT 3 PM", appearing on the spoken "3".
3. "911" and the chip "CALLED 911" never both carry the moment as two separate readings at the same instant: chip lands 0.4 s after the screen number.
4. The phone is never in anyone's hand (no hand, no desk, no Paul).
5. Nothing at x >= 1600, y >= 680; text 96/54 px inside the frame.

## 5. PANEL TEXT (exact) and CUES (seconds from A3-S2 start, `audio/a3-s2.words.json`)
Strings: `CALLING` · `911` · `SISTERS` · `FRI · ABOUT 3 PM` · `CALLED 911` · `CNN via CBS News`
| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "On a normal day" @0.00 | ground + snow on from frame 0; phone body `fromTo(y:80 -> 0, autoAlpha 0 -> 1, 0.7, power3.out)` at 0.10, screen dark |
| 0.00-4.70 | "...think about, so she did what you'd do." | phone floats y 0 -> -6, sine.inOut, yoyo; snow drift |
| 4.76 | "called" @4.76 | screen lights: call layer in 0.3 s; "CALLING" shows |
| 4.94 | "911" @4.94 | "911" `fromTo(scale 0.8 -> 1, autoAlpha 0 -> 1, 0.4, back.out(1.6))`; ring pulses every 1.0 s until 8.9 |
| 5.34 | (after "911") | chip "CALLED 911" in `fromTo(x:-60 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)`; source pill in |
| 6.22 | "stayed with her car" @6.22 | end-call disc dims to 50 % (call still open, no hang-up animation) |
| 7.76 | "Around" @7.76 | chip out `to(x:-80, autoAlpha 0, 0.45, power3.in)` |
| 7.84 | "3" @7.84 | screen swaps: call layer out 0.3 s, chat layer in 0.3 s (header "SISTERS" at 7.84) |
| 8.18 | "that afternoon" @8.18 | "FRI · ABOUT 3 PM" `fromTo(autoAlpha 0, y:10 -> 0, 0.35, power3.out)` |
| 9.76 | "video" @9.76 | thumbnail `fromTo(y:40 -> 0, autoAlpha 0 -> 1, 0.45, power3.out)` (a sent message rising) |
| 11.04 | "group chat" @11.04 | header "SISTERS" brightens to `#ffffff` 0.25 s |
| 13.10 | "Crews couldn't get to her." @13.10 | whole screen dims to 55 % over 0.8 s |
| 13.48-14.08 | after "her." @13.94 | phone and pill out `to(y:60, autoAlpha 0, 0.6, power3.in)`; ground stays (cut to g-a3-4's matching ground) |
Comp duration 14.08 s.

## 6. CONTRACT
One file `compositions/g-a3-3-phone-911.html`, root `id="g-a3-3-phone-911-root"`, `data-composition-id="g-a3-3-phone-911"`, PAUSED timeline `window.__timelines["g-a3-3-phone-911"]`. Prefix `ph-`. Both screen states pre-authored, toggled by autoAlpha. Snow: finite repeats, never `repeat:-1`. Rest: `references/mg-quickref.md`.
Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a3-3-phone-911`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a3-3-phone-911`.

## 7a. DONE LINE
All seven items of the template 7a. Item 2: the phone covers about 16 % of the frame; the ground and snow fill the rest by design (state it).

## 8. RECEIPT
As the template.
