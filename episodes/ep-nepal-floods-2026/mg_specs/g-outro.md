# BRIEF, g-outro · Z close, outro tail (12:32 + narration end)

## 0. What this graphic claims
No factual claim; the channel signature card. "The Warning Hour" wordmark, the standing sign-off.

## 1. SOURCE
Copied from episodes/ep-enderlin-2025/compositions/g-outro.html (the shipped wordmark idiom, itself built from
library/inhouse/outro-brand.html's brand lockup) per the task instruction: "copy g-outro.html and
outro-brand.html, retune ids to g-outro for this episode, keep the channel signature." Script Z:
"*(outro tail 4 s, g-outro, bed out)*" after "This was The Warning Hour." is spoken, ahead of it in the Z picture
line ("...g-outro.").

## 2. DATUM, SCALE, ORIENTATION
Full-frame title card, centred wordmark stage, same layout as Enderlin's g-outro (grid, glow, wordmark, rule,
light sweep). RETUNED DURATION: Enderlin's g-outro carries its own 12.864s spoken signature line plus a 4s tail
(16.864s total). Nepal's script instead speaks "This was The Warning Hour." inside the Z narration BEFORE this
card starts (per the picture line ordering and the separate "(outro tail 4 s...)" note), and the tail plays with
"bed out" (music fading, no narration under this card). So g-outro here is a short non-narrated tail card: match
cut in as the Z narration ends, hold with ambient motion, fade to black by the end of a 4.5s window (4s tail +
0.5s settle, per DESIGN.md "graphics exits need ~1s land time" balanced against the script's explicit 4s figure).

## 3. GEOMETRY (px)
Identical to episodes/ep-enderlin-2025/compositions/g-outro.html: wordmark "The Warning Hour" centred at
left:0 right:0 top:462px, Arial Black 900 120px tracking 6, amber "Warning"; glow ellipse 1200x600 at (360,240);
grid drift background; light sweep box 1400x160 at (260,452); amber rule 600x4 at (660,630).

## 4. MUST BE TRUE IN THE PICTURE
1. Wordmark reads "The Warning Hour" with "Warning" in amber, matching every other episode's outro exactly (the
   channel signature is not reinterpreted per episode).
2. No episode-specific text is added to this card (no episode number, no CTA tag) per the task instruction
   "keep the channel signature" (bare wordmark, not the outro-brand.html episode-number variant).
3. Card is fully visible (wordmark settled) well before the fade begins, never a hard cut to black.
4. Something drifts for the whole window (grid, glow, or the sweep), never a static hold.
5. Fades fully to black by the end of the declared duration (bed out, no lingering visible frame).

## 5. PANEL TEXT (exact) and CUES
"The Warning Hour" (no other text). No spoken cues (bed out, no narration under this card per script). Cues (s,
from card start = the moment Z narration ends): match-cut wordmark settle 0.0-0.4 · rule draws 0.3-1.2 · light
sweep 0.5-2.1 · ambient push/drift continuous 0-4.5 · fade to black 3.5-4.42 (autoAlpha 0, power1.in). Duration
4.5s declared (down from Enderlin's 16.864s, since no VO plays under this card here).

## 6. CONTRACT
Standard contract, copied and retuned. `data-composition-id="g-outro"`, timeline at
`window.__timelines["g-outro"]`. Ids kept as `ou-*` (already episode-agnostic in the source file, no prefix
collision risk since this episode has no other `ou-*` ids).

## 7. TOOLS
Standard gate commands.

## 8. RECEIPT
See builder's final message.
