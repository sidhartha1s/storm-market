# g-a5-10-close · A5-S9 · standard · Sonnet 5.5, high effort

Read first: `references/mg-quickref.md` (whole file), `library/inhouse/snippets/tokens.md`, `learnings/mg.md`, `DESIGN.md` "Signature closing footnote" and "Outro" (match-cut the channel title to the closing line; the card does not sit). Template: `references/mg-brief-template.md`.
Start from: `episodes/ep-enderlin-2025/compositions/g-outro.html` (the closest shipped close: same signature beat, wordmark only, slow push, glow and grid drift, two light sweeps, fade to black). Copy it and retime to this segment; `library/inhouse/outro-brand.html` is the older base.

## 0. What this graphic claims
Nothing factual: the channel's close card. The Warning Hour wordmark carries the signature line ("Blizzards don't ask permission. But this one sent word days early. Learn what a warning sounds like, so when it comes, you're settled before the roads close. This was The Warning Hour."). No recap, no CTA text, no episode title.

## 1. SOURCE
- Signature line shape: `DESIGN.md` "Signature closing footnote" (canonical shape, tweaked per episode). The spoken claim "sent word days early" is sourced in `edit_script.md` A5-S9 rows (`research/nws.md` 1.8 and 1.2; `factcheck/a5-r1.md` row 31); nothing of it is printed.
- Wordmark: "The Warning Hour", "Warning" in amber, exactly as Enderlin's `g-outro`.

## 2. DATUM, SCALE, ORIENTATION
Full-frame ground (radial gradient `#0b1016 -> #030507 78%`) from frame 0, layer `cl-wrap`. Wordmark centred on x 960. The presenter circle is off under the close card (`references/mg-quickref.md` "Corner circle"), but keep the corner x >= 1600, y >= 680 free of text anyway. No scale.

## 3. GEOMETRY (px) — as Enderlin `g-outro`, renamed
- Grid: `left:-240px; top:-60px; width:2400px; height:1200px`, 1 px lines `rgba(147,163,178,0.04)` every 120 px.
- Glow: ellipse `left:360px; top:240px; 1200 x 600`, `radial-gradient(ellipse, rgba(216,161,58,0.12), rgba(216,161,58,0) 70%)`.
- Wordmark: "The" / "Warning" / "Hour", three spans, Arial Black `font-weight:900` 120 px, line-height 140, letter-spacing 6, `#f2f5f8`, "Warning" `#d8a13a`; one centred line, top 462 (box about x 360-1560, y 462-602).
- Light sweep box `left:260px; top:452px; 1400 x 160`, overflow hidden, `mix-blend-mode:screen`; sweep 220 x 240 white-amber gradient.
- Rule: 600 x 4, radius 2, `#d8a13a`, left 660, top 630, `scaleX` from centre.
- One text tier only (the wordmark): declare `data-type-ok="wordmark close card"` on the root (flat-type exemption, `references/mg-quickref.md` "Gate-readable authoring"), as Enderlin's outro shipped.

## 4. MUST BE TRUE IN THE PICTURE
1. The wordmark is on the first frame (match cut from the ground g-a5-9 ends on), settled within 0.4 s; never a fade up from black.
2. Only the wordmark and its rule: no episode title, no date, no CTA, no subscribe text, no Paul.
3. Something moves for the whole window (push, glow and grid drift; no 4 s still gap).
4. Fades to black by host end - 0.08 s.

## 5. PANEL TEXT (exact) and CUES (seconds from A5-S9 start, `audio/a5-s9.words.json`)
Strings: `The` · `Warning` · `Hour`

| t (s) | spoken word | action |
|---|---|---|
| 0.00 | "Blizzards" @0.00 | stage push `scale 1 -> 1.08` over the whole window, linear; glow `x -160 -> 160` and grid `x 0 -> 150`, linear, whole window; words settle `fromTo(y:10 -> 0, 0.4, power3.out)` stagger 0.05 |
| 0.30 | "don't ask permission," @0.44-1.44 | rule draws `scaleX 0 -> 1`, 0.9 s, power3.out; first sweep `x -240 -> 1420`, 1.6 s, power1.inOut, at 0.50 |
| 2.62 | "sent word days early." @2.36-3.62 | glow breathes `opacity 1 -> 0.55`, 1.2 s, sine.inOut, yoyo, 1 repeat |
| 4.46 | "a warning" @4.34-4.68 | "Warning" pulses `scale 1 -> 1.06`, 0.35 s, power2.out, yoyo, 1 repeat |
| 7.06 | "settled before the roads close." @7.06-8.46 | rule stretches `scaleX 1 -> 1.35`, 1.4 s, power2.inOut; back to 1 at 8.46, 1.2 s |
| 9.06 | "This was the Warning Hour." @9.06-10.18 | second sweep `x -240 -> 1420`, 1.4 s, at 9.30; words lift `y 0 -> -8`, 0.3 s, yoyo, 1 repeat, stagger 0.12, from 9.70 ("Warning" @9.70) |
| 13.31 to 14.31 | 4 s tail after "Hour." @10.18 | stage, glow and grid `to(autoAlpha 0, 1.0, power1.in)`, done by 14.31 (host end - 0.08) |

Comp duration 14.39 s (wav 10.39 + 4.0 s tail, as Enderlin's close). If the orchestrator sets a different tail, keep the fade's end at host end - 0.08.

## 6. CONTRACT
One file `compositions/g-a5-10-close.html`, root `id="g-a5-10-close-root"`, `data-composition-id="g-a5-10-close"`, PAUSED timeline `window.__timelines["g-a5-10-close"]`. Prefix `cl-` (Enderlin's `ou-` ids and classes renamed). If an episode-level close comp already exists in this episode, do not build this; tell the orchestrator (`_list.md` open item 8). Rest: `references/mg-quickref.md`. Footage: none.

## 7. TOOLS
`node scripts/freeze_scan.mjs episodes/ep-buffalo-2022 --comp g-a5-10-close`; `node scripts/graphics_qc.mjs episodes/ep-buffalo-2022 g-a5-10-close`.

## 7a. DONE LINE
All seven items of the template 7a. Frame 0 shows the settled-or-settling wordmark on the ground; a frame at host end - 0.04 is black.

## 8. RECEIPT
As the template.
