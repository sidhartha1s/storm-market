# BRIEF — g-rain-bars · section A2, "The wrong end of the season" (3:43) · RHS panel over News18 Bihar footage

## 0. What this graphic claims
Northern India got about 2.6 in of rain over Sept 26-28, roughly nine times the 0.3 in normal for those days. One
fact: the multiplier.

## 1. SOURCE
Script A2: "Al Jazeera reported about two and a half inches of rain that weekend. The normal for those days is
under a third of an inch, so it was close to nine times as much." factcheck material (episode research corpus,
Al Jazeera-sourced): 66.5mm storm vs 7.6mm normal, ratio 8.75 (python-checked) — script rounds to "nine times",
card shows "2.6 IN" and "0.3 IN" (US units first per mg-quickref) with the multiplier tag reading "9X".

## 2. DATUM, SCALE, ORIENTATION
RHS panel, right:0 top:0 bottom:0 width:820px, padding 90px 96px 0 170px. Small eyebrow "NORTHERN INDIA" above two
vertical bars sharing one baseline. Scale: 260px = 2.6 in -> 100 px/in (python-checked). Bars at x 170 (normal) and
x 400 (storm), each 100px wide, baseline y 780.

## 3. GEOMETRY (px; hit within +/-10px)
- Eyebrow top 130: "NORTHERN INDIA" 22px #93a3b2 tracking 6.
- Headline top 170: "Nine times the rain." Arial Black 52px #f2f5f8.
- Baseline at y 780, x 150-620, 2px #2a3644.
- Normal bar: x 170-270, bottom y 780, height 30px (top y 750). Label above bar: "0.3 IN" Courier 26px #93a3b2
  at (170, 710); sub-label under baseline "NORMAL" 19px #93a3b2 at (170, 796).
- Storm bar: x 400-500, bottom y 780, height 260px (top y 520). Label above bar: "2.6 IN" Courier 30px #e74c3c at
  (400, 480); sub-label under baseline "SEPT 26-28" 19px #93a3b2 at (400, 796).
- Multiplier tag "9X" Arial Black 84px #d0121f popfig-style at (170, 570), appears after both bars settle, to the
  left of the storm bar (never on top of it).

## 4. MUST BE TRUE IN THE PICTURE
1. Storm bar height is exactly 260px, normal bar exactly 30px (ratio 8.67, matching 2.6/0.3), both sharing the
   same baseline y=780.
2. Storm bar carries "2.6 IN" and "SEPT 26-28"; normal bar carries "0.3 IN" and "NORMAL" — never swapped.
3. "9X" tag never overlaps either bar or its labels (overlap_check text-collision threshold).
4. US units (inches) are the primary label; no metric shown (mg-quickref "US units first... metric only as a
   small secondary if at all" — this card omits metric entirely, which is allowed).
5. No text inside the presenter keep-out (x>=1600 y>=680) — panel content is x<=720, clear.

## 5. PANEL TEXT (exact) and CUES (175 wpm from beat start; beat = "Just across the border...")
"NORTHERN INDIA" · "Nine times the rain." · "0.3 IN" / "NORMAL" · "2.6 IN" / "SEPT 26-28" · "9X".
Cues (s): panel in 0.0 · eyebrow+headline 0.3 · baseline 1.2 · storm bar grows 2.0, labels land
/* CUE "two and a half inches of rain" @est 3.77 — the storm figure is spoken first, so the storm bar reveals
first even though it sits visually right of the normal bar */ · normal bar grows 7.5, labels land
/* CUE "under a third of an inch" @est 8.91 */ · "9X" tag 11.0 /* CUE "nine times as much" @est 12.69 */ · hold to
13.5 · exit 13.9-14.5. Duration 14.5s declared.

## 6. CONTRACT
Standard contract. `data-composition-id="g-rain-bars"`, timeline at `window.__timelines["g-rain-bars"]`.
Prefix ids `rb-`.

## 7. TOOLS
Standard gate commands.

## 8. RECEIPT
See builder's final message.
