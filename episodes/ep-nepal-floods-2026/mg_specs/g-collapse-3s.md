# BRIEF — g-collapse-3s · A1 full · four stamped stills (0/1/2/3 s), then full-speed replay

## 0. Claim
The viral clip breaks into four one-second beats (0/1/2/3 s), each stamped as the narrator counts it,
then the clip replays once at full speed as the payoff. Stills are PLACEHOLDERS (media not sourced yet).

## 1. SOURCE
factcheck-A row 1 (3-second collapse, CONFIRMED) + script A1 paragraph. UPDATE (orchestrator, this session):
stills are now REAL — `media/collapse-f0..f3.jpg`, 1920x1080, pulled at 17.0/18.0/19.0/20.0 s of the source
WION clip and composited (a centred content strip over a blurred cover-fit copy of the same frame). The
on-screen stamps stay 0.0/1.0/2.0/3.0 s (exact, relative to the collapse's own start, per the orchestrator).
Checked (ffprobe): all four are 1920x1080. Content fills most of the frame width with modest blur margins
on the sides (not a narrow phone-style strip), so the lower-third-left time chip (x96-340) and the top-left
replay chip (x96-500) both sit clear of the centred content in every frame — no reposition needed.

## 2. DATUM, SCALE, ORIENTATION
- Full-frame comp, 1920x1080. Each still fills the frame (cover-fit), stamped with a lower-third time chip.
- Time chip: x 96-340, y 906-984 (lower-third-left, clear of the presenter circle at x>=1600,y>=680).

## 3. GEOMETRY (px)
- Still layer: `<img>` or `<video>` cover-fit 1920x1080 per still, swapped by crossfade (autoAlpha) at each cue.
- Time chip: glass card rect (96,906)-(340,984), r16; mono readout Courier New 700 34px #f2f5f8, e.g. "0.0 S".
- Replay flag: after the fourth still, a full-frame crossfade to a "REPLAY · FULL SPEED" chip (top zone,
  x96-500,y96-150, same glass treatment) that then clears for the clip to replay (the replay itself is the
  underlying hook footage reused, `data-callback="frame-by-frame payoff"` per the script's own note — this
  comp only carries the chip + the still stamps, the video track is index.html's job).

## 4. MUST BE TRUE
1. Exactly four stills appear in order (f0, f1, f2, f3), each crossfading to the next, never two visible at full opacity simultaneously mid-comp.
2. Each still's time chip reads the matching second ("0.0 S", "1.0 S", "2.0 S", "3.0 S") and updates exactly when that still becomes visible.
3. The time chip never overlaps the presenter-circle corner (x>=1600, y>=680) or the frame's lower-third centre text zone.
4. "REPLAY · FULL SPEED" only appears after the fourth still (3.0 S) has been shown, then the comp clears (autoAlpha 0) to let the reused clip play under it.
5. Something moves for the whole window even on a still frame (a slow Ken Burns drift per still, `kb()` helper pattern, so no still reads as a frozen poster).

## 5. PANEL TEXT (exact) and CUES
Time chips: "0.0 S", "1.0 S", "2.0 S", "3.0 S". Payoff chip: "REPLAY · FULL SPEED".
Cues (s, local @175wpm from the A1 "video that spread" paragraph):
- still f0 mounts + "0.0 S" chip @0.0 (`/* CUE "The video that spread that weekend" @est 0.0 */`), slow Ken Burns begins
- still f1 crossfades + "1.0 S" @6.17 (`/* CUE "In the first second" @est 6.17 */`)
- still f2 crossfades + "2.0 S" @12.34 (`/* CUE "By the second" @est 12.34 */`)
- still f3 crossfades + "3.0 S" @16.80 (`/* CUE "By the third" @est 16.80 */`)
- "REPLAY · FULL SPEED" chip lands @21.5, holds 2 s
- comp clears (autoAlpha 0 on everything) @23.5 so index.html's reused hook clip plays through @23.5-26.5
Declared duration 26.5 s (narration ~22.63 s + chip beat + ~2.5 s cleared window for the replay cut).
