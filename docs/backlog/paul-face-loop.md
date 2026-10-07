# Backlog — Paul face loop (picture-in-picture presenter, narration-gated)

Owner ask 2026-09-08: put a small circular Paul in a corner of every video so viewers meet the face
early instead of first seeing him at the CTA. Phase 1 is a muted loop; phase 2 gates the loop on the
narrator's audible beats so the mouth moves only while there is speech (not lip-sync, "talk-sync").

## Reference
- Source frame: `assets/cta/paul-storm-ready-v5-sep6.mp4` (left the tree 7 Oct 26, in git history; Paul on camera, 2560x1440 master → 1080p asset).
  Still references: `landing/assets/paul-binder.jpg`, `paul-plywood.jpg`, `paul-stage.jpg`,
  `paul-tornado-selfie.jpg`, `ebook/build/art/cover-v2-paul.png`.
- Placement: bottom-RIGHT circle, 200 px, 40 px inset, above the bug strip line (the bug occupies the
  bottom 92 px full-width; the chip/checklist live bottom-LEFT, so right is the free corner). Hidden during
  the CTA window (Paul is full-frame there), during the hook (0–8 s, nothing competes with the number), and
  under the close card.

## Phase 1 — the loop asset (1 h, no code in the pipeline)
1. Cut a **10–12 s "listening + talking" loop** from the v5 CTA master: pick a stretch where Paul's head
   stays inside a stable crop, trim to a mouth-closed frame at both ends so it loops without a pop,
   crop to a centred square around the face, 400x400, `-r 30`, muted. Optionally colour-match to the
   channel grade (soft-light steel) so it sits with the b-roll.
2. Mask: CSS `border-radius:50%` on a 200 px wrapper + a 3 px `#d0121f` ring and a 12 px shadow; a 6 %
   slow breathing scale (`sine.inOut`, yoyo) so the circle is never a still.
3. Mount as a track-4 `<video ... muted data-callback="presenter loop">` per chapter window (max-2-uses rule:
   lint counts distinct windows, so register the loop file as an allowed always-on asset in lint_timeline
   — one line exemption by filename, same as the CTA).
4. Template in `library/mini-storms/presenter-pip.html` (CSS + the mount pattern), used by both lanes.

## Phase 2 — talk-sync (2–3 h, one deterministic script, no editorial judgment)
The narrator's per-segment `audio/<id>.words.json` already has word start/end times. Derive **speech spans**:
merge consecutive words with gaps < 0.35 s; anything ≥ 0.35 s between spans is a pause.
- Build two loop assets from the CTA master: **`paul-talk.mp4`** (mouth moving, 6–8 s, seamless) and
  **`paul-idle.mp4`** (mouth closed, slight blink/nod, 6–8 s, seamless).
- In `index.html`, the presenter circle holds BOTH videos stacked; a GSAP timeline toggles `autoAlpha`
  between them on every span edge (0.12 s crossfade). hyperframes keeps both playing in lockstep, so the
  visible one is always mid-loop and never restarts — that is what sells it as "listening vs talking".
- `scripts/talk_sync.py episodes/<slug>` (mechanical, allowed under the code rule: it reads words.json +
  the narration `data-start`s and PRINTS the span list as GSAP lines to paste into index.html; it never
  writes episode HTML). ~40 lines.
- Quality bar: the swap must land within ±0.1 s of the first/last word; test on 3 segments by eye (frame
  at span start, span end, mid-pause).

## Phase 3 (later, optional) — real lip-sync
LTX / SadTalker-class lip-sync per segment is possible (the JP channel's storm-insert recipe already does a
tight-crop LTX lip-sync), but it costs GPU minutes per minute of narration and adds a QC surface (teeth,
jitter). Only worth it if the PiP is held large (≥ 320 px) or used full-frame. Not for the 200 px circle.

## Suggested "talk" loop content (what the mouth does on mute)
- 6–8 s of natural conversational cadence: two short phrases, a beat, one longer phrase; eyebrows lift once;
  one small nod. Avoid a laugh, a hard "O" or a long pause inside the talk loop (they read as mismatched
  when the narration is mid-sentence).
- Idle loop: closed mouth, one blink at ~2 s, one at ~5 s, a 1° head tilt and back. That is enough motion to
  survive beat_density and still read as "listening".
- Both loops must start and end on the same frame pose (closed mouth, neutral) so the crossfade is invisible.

## Open questions for the owner
1. Left or right corner? (Proposal: right; left is taken by the data chip and the checklist card.)
2. Circle size 200 px on 1080p — ok, or larger for TV viewers?
3. Show from the intro (0:08) or from chapter 1 (~1:05)?
