# BRIEF — g-ledger · A4 spine (Established / Disputed / Unknown board), full act, 100 s

## 0. What this graphic claims
Three things are settled, one is disputed (the toll), three are still unknown as of Sept 29. Each claim slides into
its column on the voice and stays for the rest of the act — the board IS act A4's spine graphic.

## 1. SOURCE (verbatim claim text, owner-assigned, fact-file backed)
Established: wall fell Sept 27 after rain (factcheck-C#1); video from that day, Lete/Mustang (factcheck-C#2);
avalanche hit the camp (factcheck-C#3). Disputed: toll 12/21/24 (factcheck-C#4,#5,#6). Unknown: how long the river
was blocked (factcheck-A#13: duration/lake-size "had not been reported by the twenty ninth" — note factcheck-C#12
confirms a blockage DID happen, but its DURATION stays unreported, so this Unknown entry is accurate as scoped);
12 crew still missing (factcheck-D#3); no radar/sensor reading published from either slope before it moved
(factcheck-B#22).

## 2. DATUM, SCALE, ORIENTATION
Three columns, full frame: ESTABLISHED x 96-660, DISPUTED x 700-1280 (centred), UNKNOWN x 1320-1824. Header row
y=140. Claim chips stack downward per column, first chip top=220, each next chip top += 130.

## 3. GEOMETRY (px)
- Column header cards: "ESTABLISHED" (96,140) green accent #3fa15a underline, "DISPUTED" (700,140) amber accent
  #d8a13a underline, "UNKNOWN" (1320,140) blue-grey accent #5a768f underline. 26px tracking8 section-header tier.
- Claim chips: glass card, width matches column (Established/Unknown 528px, Disputed 500px), padding 20 28,
  radius 16, text 24px #dfe7ee (row-value-ish tier, wraps to 2 lines max).
- Established chips at (96,220), (96,350), (96,480).
- Disputed chip at (700,220) — one wide chip, big red Abril 60px "12 · 21 · 24" plus sub "REPORTS DISAGREE".
- Unknown chips at (1320,220), (1320,350), (1320,480).
- Background sweep: full-width diagonal light band (like dtl-sweep), continuous loop across the whole 100 s window.

## 4. MUST BE TRUE
1. Exactly 3 chips in ESTABLISHED, 1 in DISPUTED, 3 in UNKNOWN, matching the assigned claim list verbatim (short form).
2. The disputed chip shows all three contested numbers (12, 21, 24), never picks one as "the" toll.
3. Every chip that has landed by a given time STAYS visible (no chip exits early — "stays for the rest of the act").
4. Column headers are legible for the entire 100 s (never covered by a chip).
5. Something moves continuously (sweep band or header glow) across every 4 s window of the whole comp.

## 5. PANEL TEXT (exact, diagram-label length) and CUES
Established: "WALL FELL · SEPT 27, AFTER RAIN" / "VIDEO FROM THAT DAY · LETE, MUSTANG" / "AVALANCHE HIT THE CAMP".
Disputed: "12 · 21 · 24" (big) / "THE TOLL: REPORTS DISAGREE" (sub).
Unknown: "HOW LONG THE RIVER WAS BLOCKED" / "12 CREW STILL MISSING" / "ANY READING OF EITHER SLOPE BEFORE IT MOVED".
Cues (s, from "Three things about this week are settled." sentence start, A4 open, 175 wpm est):
/* CUE "Three things about this week are settled" @est 0.3 */ headers reveal (all 3 at once), sweep starts (continuous, whole comp).
/* CUE "The wall fell into the Kali Gandaki on September twenty seventh, after days of rain" @est 7.2 */ Established chip 1 slides in (x:-40->0, autoAlpha).
/* CUE "filmed near the village of Lete in Mustang district" @est 12.3 */ Established chip 2 slides in.
/* CUE "the avalanche hit the Himlung camp" @est 18.5 */ Established chip 3 slides in.
/* CUE "the reports disagree on" @est 22.0 */ Disputed chip slams in (power4.in, scale 1.2->1), numbers "12 · 21 · 24" stagger-reveal.
/* CUE "Some of it is still open" @est 80.9 */ Unknown header pulses (scale 1.04 yoyo).
/* CUE "how long the debris held the river back" @est 87.5 */ Unknown chip 1 slides in.
/* CUE "twelve of the crew still missing" @est 93.3 */ Unknown chip 2 slides in.
/* CUE "no agency has published a radar or sensor reading from either slope before it moved" @est 98.4 */ Unknown chip 3 slides in, hold to exit.
Duration 102 s (whole board exits x:660->1400 autoAlpha 0 at 101.4, 0.6 s power3.in — chapter blackout follows).
