# BRIEF — g-social-mock · A4 · phone-frame social post mock, blurred text, red "?" stamp

## 0. Claim
The story online moved faster than the confirmed count: posts sharing the collapse video called it
another glacier collapse, echoing Langtang. This is a generic, unattributed mock, not a real post.

## 1. SOURCE
factcheck-A "Other issues" + A4 script text (no [verify] tag on this beat; the claim is about online
framing in general, not one named post). No real handle, no real username, no real avatar photo — the
phone mock is illustrative only, per the picture line's own instruction ("no real handle, no real username").

## 2. DATUM, SCALE, ORIENTATION
- Stage 1920x1080. Phone frame centred, x 760-1160 (400 px wide), y 140-940 (800 px tall), rounded rect.
- "?" stamp overlays the frame's lower-right corner at (1040,760), rotated -12deg.

## 3. GEOMETRY (px)
- Phone body: rounded rect (760,140)-(1160,940), r28, fill #15202b, stroke #93a3b2 2px; a notch bar top-centre.
- Post card inside the phone (screen area 784,180 - 1136,900): avatar circle placeholder (no photo, just a
  flat #2a3644 disc, r28) top-left, two grey bars for username/handle (blurred: heavy box-blur filter, fill
  #4a5560 at reduced opacity, never legible text), body text lines as blurred grey bars EXCEPT one bar of
  real crisp text "glacier collapse" (mid-block, un-blurred, #f2f5f8, 26px) — every other line stays a
  blurred bar. A thumbnail video placeholder rect below the text, flat #0b1016.
- Red "?" stamp: circle r70 #8e2020 (crimson token) with white "?" glyph 84px Abril-style, rotated -12deg,
  drop shadow.

## 4. MUST BE TRUE
1. Every text line in the mock post is a blurred/illegible bar EXCEPT the single phrase "glacier collapse," which is the only crisp legible text.
2. No avatar photo, no handle text, no username text is ever legible (all blurred bars or flat placeholders) — matches "no real handle, no real username."
3. The red "?" stamp is fully inside the frame (no glyph clipped by the phone's rounded rect) and legible.
4. The phone frame and its contents sit inside the 96/54 px text-safe margin.
5. Something moves for the whole window (a subtle scroll drift on the post content, or the stamp's slight rotation settle).

## 5. PANEL TEXT (exact) and CUES
Only on-screen text: "glacier collapse" (the one crisp phrase) and the "?" glyph.
Cues (s, local @175wpm; this beat opens the shared A4 picture line before g-rock-ice-vs-rain takes over):
- phone frame slides up @0.3
- blurred post lines stagger in @1.2
- "glacier collapse" phrase turns crisp (unblurs) @2.74 (`/* CUE "called it another glacier collapse" @est 2.74 */`)
- red "?" stamp slams in @5.5 (`/* CUE "a repeat of Langtang" @est 5.5 */`)
- exit @7.6 (phone frame + stamp slide out together, power3.in)
Declared duration 9.0 s (covers the beat's first two sentences, ~7.2 s narration local, + 1.8 s tail before g-rock-ice-vs-rain mounts).
