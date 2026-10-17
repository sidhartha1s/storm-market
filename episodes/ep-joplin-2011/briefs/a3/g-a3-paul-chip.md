# BRIEF g-a3-paul-chip · A3-S8 · STANDARD (Sonnet 5.5, high effort) · overlay over Paul full frame

Read first: `references/mg-quickref.md` (incl. "Paul on screen": text over his full-frame clip is allowed; the logo sits at 1692–1788 × 852–948), `learnings/mg.md`, `library/inhouse/snippets/tokens.md`. Exemplars: snippets `popup-chip` and `source-label`.
Under it (whole host): Paul's full-frame clip `ins-paul-<n>` for A3-S8.

**Cue caveat:** the cues below come from `audio/a3-s8.words.json` (the TTS wav). If Paul's Flow clip carries its own audio, re-time "71" and "three." from that clip's transcript; the timings will differ. The transcript reads "can get to" where the text says "could get to": a Whisper slip, no cue rides on it.

## 0. What this graphic claims
Of the 71 people lost at home, only three had a basement they could reach, and the tornado took all three (H22).

## 1. SOURCE
- H22, Sec. 4.6.2.2 footnote 176: "Only three of the 71 individuals who died in residences in the Joplin tornado had access to basements."
- 71 = 59 houses + 12 apartments, Table 4-3 (H26), base 154.

## 2. DATUM, SCALE, ORIENTATION
Overlay, transparent, 1920 × 1080. No scale.

## 3. GEOMETRY
- Chip (glass popup-chip): left 96, bottom 150, "71 LOST AT HOME", Arial Black 900, 52 px.
- Source chip (glass source-label): left 96, bottom 54, 20 px: "NIST Sec. 4.6.2.2".
- Both stay left of x 900 so they never cross Paul's face; nothing in x ≥ 1600, y ≥ 680 (the logo).

## 4. MUST BE TRUE IN THE PICTURE
1. "71" is the only number on screen. The chip never says "3".
2. Neither chip covers Paul's face, mouth or the logo, at any frame (read a frame over the real clip).
3. Paul's face is alone on screen after the chips exit (the Picture line's hold).

## 5. PANEL TEXT (exact) and CUES (a3-s8.words.json, see caveat)
Text: "71 LOST AT HOME" · "NIST Sec. 4.6.2.2".
Host: a3-s8 "71" @1.10 → "three." @6.04 + 0.4.
- 1.10 "71": chip in (popup-chip entrance, 0.45 s, power3.out); source chip in at 1.4.
- 1.6 → 5.8: both float (y ±3 px, finite repeats).
- 5.84 → 6.44: both slide out (x −40, autoAlpha 0, power3.in). Paul holds alone after.

## 6–8. CONTRACT, TOOLS, DONE LINE, RECEIPT
`references/mg-brief-template.md` §6, §7, §7a and §8 unchanged, COMPID = `g-a3-paul-chip`, root id `g-a3-paul-chip-root`.
