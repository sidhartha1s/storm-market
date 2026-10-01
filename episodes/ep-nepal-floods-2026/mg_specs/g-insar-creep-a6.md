# BRIEF — g-insar-creep-a6 · A6 return, small (Langtang counter, then empty strip) · SCHEMATIC swath

## 0. What this graphic claims
Callback: the tool that DID see Langtang moving was satellite radar (already-known 12 in / 30 cm figure), and it
still has nothing for the Kali Gandaki wall this September. Smaller, calmer than the A3 payoff — no suspense, just
the callback plus the still-empty state.

## 1. SOURCE
Same as g-insar-creep (factcheck-B#20, #22). Lower-third-scale card, not the full rail.

## 2. DATUM, SCALE, ORIENTATION
Lower-third anchor per tokens.md: left 110, bottom 110 (top = 1080-110-380 = 590), width 620, height 380.

## 3. GEOMETRY (px, card-local then +110/+590 offset)
- Card bg glass, radius 20, border 1px rgba(255,255,255,.14).
- Local eyebrow (28,26) "SATELLITE RADAR · LANGTANG" 20px grey tracking4.
- Local counter (28,70) Courier 700 70px #e74c3c "12 IN" then sub Courier 400 26px #93a3b2 "30 CM · AUG 2026" at (28,150).
- Local mini colour-ramp bar (28,190) w560 h14, FULL green->amber->red (already resolved, no freeze this time).
- Crossfade target: same card content swaps to "KALI GANDAKI · SEPT" label (28,70) 30px #f2f5f8, empty grey bar
  (no gradient) at (28,190), small "?" mark (28,230) 40px #d0121f.

## 4. MUST BE TRUE
1. "12 IN" is the primary counter (US units first); "30 CM" is the visibly smaller secondary line.
2. The colour ramp bar is shown FULL/resolved on the Langtang state (not climbing) — this is a callback, not a new reveal.
3. The empty Kali Gandaki state carries no colour ramp and a "?" mark, echoing g-insar-creep's empty state exactly.
4. Card stays inside the lower-third zone (left<=110+620=730, bottom<=110+380=490 from bottom, i.e. top>=590) — never enters the presenter corner.

## 5. PANEL TEXT (exact) and CUES
Text: "12 IN" / "30 CM · AUG 2026" / "KALI GANDAKI · SEPT" / "?".
Cues (s, from "The tool that did see Langtang moving..." paragraph start, A6, 175 wpm est):
/* CUE "The tool that did see Langtang moving was satellite radar" @est 0.3 */ card pops in, "12 IN" + ramp bar (already full) reveal together.
/* CUE "measure ground motion from orbit to a fraction of an inch" @est 4.8 */ hold, ramp bar pulses once (scaleX 1->1.02 yoyo).
/* CUE "It only works when someone processes the images in time" @est 8.0 */ crossfade: Langtang content out, KALI GANDAKI + empty bar + "?" in.
/* CUE "someone has to warn the valley when a slope speeds up" @est 12.0 */ hold on the empty state.
Duration 15 s (card exits y:0->40 autoAlpha 0 at 14.3, 0.5 s power3.in).
