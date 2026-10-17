# g-a2-paul-chip · STANDARD (Sonnet 5.5, high) · act a2, segment a2-s9

**Open numbers:** none.

**Under it:** Paul full frame, the a2-s9 `ins-paul-<n>` clip (his own voice, no narration). Text over him is allowed;
he is never composited over a graphic, so this is a chip only. The Warning Hour logo sits at (1740, 900): keep clear.
**Host:** starts on "four" (its first mark), ends on his last word, where the cut lands into the a2-s10 clip.
**Cue clock:** `clip offset + word start`; offset = the ins-paul clip's `data-start` minus host `data-start` (his words
are timed by `audio/a2-s9.words.json`; if the mounted clip is trimmed or slowed to 0.85, re-time from its own transcript).

## 0. What this graphic claims
The second siren came four minutes after the tornado touched down.

## 1. SOURCE (confirmed rows, quoted)
- E15 (NIST Finding 35): "the siren system was sounded again, 4 minutes after the tornado touched down and almost exactly when the tornado entered the City of Joplin."
- E14 (NWS Table 1): "538 pm CDT - Second 3 minute siren alert sounded".

## 2. DATUM, SCALE, ORIENTATION
No scale. One glass card, lower-third anchor left 110, bottom 110.

## 3. GEOMETRY
- Glass card, padding 20 x 30: line 1 "4 MIN AFTER TOUCHDOWN" Arial Black 900 52 px #f2f5f8 tracking 2; line 2 "NIST Finding 35" Arial 700 20 px #c8d3e0 tracking 3.
- In: x -40 to 0 + autoAlpha 0.4 s power3.out; line 2 follows 0.3 s later. Hold: card floats y 0 to -5 (sine, finite repeat). Exit: x 0 to -980 + autoAlpha 0, 0.6 s power3.in, ending on the host end.

## 4. MUST BE TRUE IN THE PICTURE
1. The chip says 4 minutes after touchdown, never "after the warning" (E15).
2. The card covers no part of Paul's face (frame read on the real clip) and stays left of x 1600 and clear of the logo.
3. The card is gone by the cut (check host end minus 0.1 s).

## 5. PANEL TEXT (exact) and CUES
| cue (segment · word · start s) | what happens |
|---|---|
| a2-s9 · "four" · 3.28 | card in, line 1 |
| a2-s9 · "minutes." · 3.52 | line 2 "NIST Finding 35" (0.3 s after line 1 begins) |
| a2-s9 · "again." · 7.66 | exit fills the host's last 0.6 s; host ends at the cut |

The host runs about 4.4 s from "four" to the end of "again.", so a gap of 4 s or more with nothing moving never fits; the float keeps it moving anyway.

## 6 to 8
As `references/mg-brief-template.md` §6, §7, §7a (item 7: one frame over Paul's clip), §8. File
`compositions/g-a2-paul-chip.html`, timeline `window.__timelines["g-a2-paul-chip"]`, root id `a2pc-root`.
