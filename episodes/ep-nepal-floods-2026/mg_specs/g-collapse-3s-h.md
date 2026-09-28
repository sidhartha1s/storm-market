# BRIEF — g-collapse-3s-h · Hook overlay · thin timer bar, 0.0 s -> 3.0 s, lands on "3 seconds"

## 0. Claim
The viral collapse clip took about three seconds start to finish; a thin timer bar over the footage
counts that out live, landing on "3 seconds" as the narrator says it.

## 1. SOURCE
factcheck-A row 1 (CONFIRMED): Asianet Newsable "Vanished In 3 Seconds," LatestLY, 28 Sep 2026 — the
Kali Gandaki mountainside collapse took about three seconds. Note (factcheck-A "other issues" #3):
PressAdda describes "just six seconds" for one framing — the script's own `[verify: frame-check]` tag
in A1 flags this is still open; this hook comp uses the 3-second figure the script currently carries,
and the exact seconds may change to match the clip per the orchestrator's retime note.

## 2. DATUM, SCALE, ORIENTATION
- Overlay only, mounted over the hook clip (track 3+, never covering the falling slope's centre).
- Timer bar sits in the TOP safe zone: x 96-824 (728 px wide), y 96-150 (never lower-third, never centre).

## 3. GEOMETRY (px)
- Glass-card chip background behind the bar: rect (86,86)-(834,160), r18, glass surface (rgba(10,16,24,.55), blur 18px, border rgba(255,255,255,.14)).
- Timer track: rect (110,118)-(800,138), r10, fill rgba(147,163,178,.28).
- Timer fill: rect (110,118)-(110,138) growing width 0->690 (scaleX 0->1, transformOrigin left), fill popfig red #d0121f.
- Time readout text (mono, "0.0 S" -> "3.0 S"), Courier New 700 30px #f2f5f8, at (110,96), counting up via onUpdate.
- "3 SECONDS" landing label: Abril-style, red #d0121f, 52px (headline tier, not full 150px popfig display, to
  respect the "never over the falling slope's centre" rule and stay a top-zone chip), appears at (110,168) once the timer lands.

## 4. MUST BE TRUE
1. The entire comp (chip, bar, readout, landing label) stays within y 86-220 — the TOP zone — and never enters the frame's centre (y 400-680) or the presenter-circle corner (x>=1600,y>=680).
2. The timer fill's width only increases (0->690 px), monotonic, finishing exactly at the "3.0 S" readout.
3. The readout text always matches the fill's current fraction (e.g., fill at 50% width shows "1.5 S"), no mismatch frame.
4. "3 SECONDS" only appears AFTER the readout reaches "3.0 S", never before.
5. Something moves for the whole window (the fill itself, or a subtle pulse on the landing label after it lands).

## 5. PANEL TEXT (exact) and CUES
Readout: "0.0 S" counting to "3.0 S". Landing label: "3 SECONDS".
Cues (s, from hook clip start, H · 0:00):
- chip + track fade in @0.15
- fill begins growing, readout starts counting @0.3
- fill completes, readout hits "3.0 S" @3.3 (`/* CUE "In three seconds" @est 0.0 (matches the clip's own 3 s, not the narration cue) */`)
- "3 SECONDS" label lands @3.35, small pulse @3.6
- comp exits (chip slides up, autoAlpha 0) @4.0
Declared duration 4.2 s. The exact seconds retime with the shot log per the task's note; this brief
documents the 3.0 s figure currently in the script.
