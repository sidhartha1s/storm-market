# BRIEF g-a3-shelter-chip · A3-S7 · STANDARD (Sonnet 5.5, high effort) · overlay

Read first: `references/mg-quickref.md`, `learnings/mg.md`, `library/inhouse/snippets/tokens.md`. Exemplars: snippets `popup-chip` and `source-label` (`library/inhouse/snippets/usage-examples.html`, `cards.css`), `references/editing-patterns/ep6-glasscard-popfig-bfmg.html`.
Under it (whole host): the NIST ground photograph of an in-home shelter standing in a destroyed house, or the clip of the same if sourced. Transparent root; the orchestrator mounts the picture on a lower track for the full window. A still over 6 s fails sweep check 9: the photo gets its own slow push at mount.

**Note for the orchestrator:** a3-s7.words.json transcribes the first word as "Partly"; the script and `a3-s7.txt` say "Hardly". Listen to `audio/a3-s7.wav` before mounting: if the voice says "partly", the line means the opposite and needs a TTS redo (cues below then shift).

## 0. What this graphic claims
The few in-home shelters NIST saw held, and the people in them survived (H16, H18).

## 1. SOURCE
- H16, Finding 23: "Based on a few instances observed in this tornado, in-home shelters did perform well and provided life-safety protection to the home owners."
- H18, Sec. 1.2: "Very few residents had in-home shelters. Those who did and were in the storm's path survived in these pre-manufactured shelters while their wood-framed homes were destroyed around them."

## 2. DATUM, SCALE, ORIENTATION
Overlay, 1920 × 1080, transparent. No map, no scale.

## 3. GEOMETRY
- Chip (glass popup-chip, lower-third zone): left 96, bottom 150, "IN-HOME SHELTERS HELD", Arial Black 900, 52 px `#f2f5f8`.
- Source line (glass source-label): left 96, bottom 54 (baseline ≤ 1026), 20 px `#c8d3e0`: "NIST Finding 23 · a few instances observed · Sec. 1.2".
- Keep x ≥ 1600, y ≥ 680 empty (presenter circle).
- Nothing over the shelter in the picture: once the photo is picked, the orchestrator names its box; if the chip covers it, the chip moves to the top-left zone (left 96, top 96).

## 4. MUST BE TRUE IN THE PICTURE
1. The chip says "HELD", never "survived every time" or a count; the source line keeps "a few instances observed".
2. No number on screen except the finding number.
3. The chip and source line never cover the shelter in the photo (frame read over the real picture).

## 5. PANEL TEXT (exact) and CUES (a3-s7.words.json)
Text: "IN-HOME SHELTERS HELD" · "NIST Finding 23 · a few instances observed · Sec. 1.2".
Host: a3-s7 "shelter" @1.82 → "it." @5.82 + 0.8.
- 1.82 "shelter": source line in (fromTo autoAlpha 0, y 24 → 0, 0.4 s).
- 4.98 "came": chip in (popup-chip entrance, x −40 → 0, power3.out, 0.5 s), one gloss sweep 5.3–5.9.
- Hold: both float (y ±3 px, finite repeats) so no span of 4 s is still. Exit: chip and source slide out in the last 0.6 s per quickref "Motion and exits".

## 6–8. CONTRACT, TOOLS, DONE LINE, RECEIPT
`references/mg-brief-template.md` §6, §7, §7a and §8 unchanged, COMPID = `g-a3-shelter-chip`, root id `g-a3-shelter-chip-root`.
