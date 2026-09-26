# learnings/mg.md: motion graphics: composition bugs, gate behaviour, MG owner reviews

Newest first. New entries go at the top, under this line. Superseded lines point at their current home.

## 2026-09-26 - MG eval 2 (El Reno "widest tornado", Three.js, Opus builders): the small brief won, house docs lost
- **The owner's ranking:**
  1. B, small brief only (~21 min build).
  2. C, quick-ref + move library + style frames (29.5 min).
  3. A, full house docs (35 min). Owner: "when the camera moves up, it sucks".
  More documentation made the output slower AND worse.
- **The blind Opus judge and the gates both disagreed with the owner.** The judge ranked C 38 > A 34 > B 33 (/50). The gates passed B only 1/4. So the owner picks; a judge score is a note, never a gate (eval use only).
- **The gates misread WebGL.** B failed:
  - graphics_qc `undesigned`, because it reads a Three.js canvas as a flat background with too few type tiers;
  - overlap_check, which stages comps without `<base href>`, so every Three.js comp fails "timeline not registered";
  - beat_density.
  None of these is a build defect. Fix them in the gates before the next WebGL build.
- **Stillness is about drift, not new information** (owner). A hold that waits for the narrator's impact point is fine if the elements float slightly; see `references/mg-quickref.md` "Motion and exits".
- **Builder slip:** all three El Reno builds put the MG host on `data-track-index="1"`, which sweep treats as the media track ("media files exist" and "still over 6 s" failures). MG hosts go on track 2 or higher.

## 2026-09-22 - ep-1974 draft 2 review: narrator opens the video, banned audio is gated by hash, holds need a reason
- **Why the plane graphic failed in draft 1 and passed in draft 2.** An SVG element carried a static `transform="translate()"`
  attribute AND a GSAP x/y tween. GSAP takes over the transform and discards the attribute, so the icon flew from 0,0 while
  its trail drew in the right place. Same family: `transformOrigin` in CSS px on a nested SVG line pushed it outside the
  viewBox (use `svgOrigin` in user units). No gate checks that a mover follows its path, and a still frame looks plausible
  unless you know where the icon should be. Rule for every "A follows B" animation: position the mover with GSAP only, and
  assert in the DOM that the mover sits on the path head at three times before calling it done.
- Presenter-circle box x 1632-1888, y 700-956 in every builder brief: superseded by references/mg-quickref.md "Frame and safe zones" (26 Sep 26). No render while a builder edits: CLAUDE.md "the render is the LAST step".

## 21 Sep 26 — owner review of the ep-1974 draft: "shippable after these small iterations"

Owner watched the whole 17:39 draft ("overall really well put video", the motion graphics "a significant better look
this time", 14:05 the combed-trees card "interesting bit"). Corrections, each persisted here:
1. **Motion graphics go static after the story beat lands.** `beat_density.py` said 0/39 because a 100 px grid drift
   over 78 s counts as a tween; to the eye 1.3 px/s is a freeze, and blackdetect read four dark cards as black for
   6 to 11 s. Rule: every comp carries a VISIBLE ambient element for its whole window (a scan line at 6 px/s or more,
   staggered dot blips at least every 1.5 s, a sweep rotating), finite repeats, never `repeat:-1`. Verify by pixel
   diff of two frames 2 s apart at three points in the window, not by tween coverage.
2. Presenter circle on docs, keep-out x >= 1600, y >= 680: superseded by references/mg-quickref.md "Frame and safe zones" (26 Sep 26).
4. Beige glass for every card over a dark map: superseded by references/mg-quickref.md "Palette and surfaces" (26 Sep 26): beige only for quoted sources over dark maps.
5. **A person card without a real photo does not keep the photo slot** (owner: "don't leave the card with photo's
   space in"); monograms are out, text-only layout for the nine people with no PD photo (a sourcer checks first).
6. **Red popfigs**: owner is fine with the light use here ("its good. i mean it"); no retrofit, weigh them per episode.
7. **The g-plane icon rode a different coordinate space than its trail** (owner: "a moving house fly on the top
   left"): position markers must be verified by measuring the icon against the path head, never by eye.
8. **The F6 card's strike missed the glyph and the F5 hung outside the card**: a strike goes through the glyph body,
   every child stays inside the card box; screenshot the card at the last cue before shipping.

## 21 Sep 26 — ep-1974 assembly: the static gates could not read cue-positioned comps, and four rules got a home

Findings from the first hand-authored 39-comp timeline (17.6 min, hook anchored on the WHAS air-check):

1. **Comps place tweens at `CUES.six`, `DUR - 0.6`, `CUES.dark + 1.5`; the gates only parsed numeric literals.**
   `sweep_episode.py` check 7 reported 14 false "holds" and `beat_density.py` hard-exited on every batch built from
   words.json cues. Fix: `scripts/comp_consts.py` `fold(src)` replaces `const NAME = num`, `const NAME = {k: v}`
   members and `num op num` arithmetic with literals before the regexes run (dates like `2026-09` stay text via the
   leading-zero guard). Both gates import it. Unknown identifiers stay as they were, so a real hole still reports.
2. **A declared hold is an empty `<section class="clip hold">` on its own track** (DESIGN.md "hold-marker line").
   `lint_timeline.py` sanctions narration gaps only inside a blackout, a hold or the CTA dips; every other gap over
   0.8 s still fails. Holds and blackouts never stack at one seam (owner 20 Sep 26).
3. **Overlay hosts on tracks 3 and 4 are mounted comps.** `sweep_episode.py` read them as unmounted because it only
   looked at tracks 1 and 2; "mounted" is now any host on any track. Coverage still counts tracks 1 and 2 only, so
   blackouts must sit on track 1.
4. **The CTA gate slug regex is `(ep\d*-|ms-)`.** `ep-1974-…` (no digit after `ep`) silently SKIPPED the CTA gate;
   a skipped gate reads as green in the summary line. Check the SKIPPED lines, not the exit code.
5. **A cutaway still over a map comp is a "sandwich" to `overlap_check.mjs`** (index element covering comp text).
   Escape per element with `data-overlap-ok="cutaway over the map"` only when the still is full-frame and meant to
   cover the map; popfigs never sit over a map comp (state labels collide), the map's own rail carries the number.
6. **`repeat:-1` on a comp's main timeline makes `tl.duration()` infinite (1e10).** Two batch-4 comps did it for
   ambient drift. Measure every comp with a bare page + `window.__timelines[id].duration()` before mounting; the
   staging pages a measurer writes into `compositions/_dur_*.html` count as unmounted comps in sweep until deleted.
7. **Builders leave `_shot_*.html` staging pages in `compositions/`.** sweep and graphics_qc both scan them
   (23 "unmounted" comps, phantom collisions). Delete every `_shot_*`, `_dur_*`, `_debug_*` page before the gate
   run, and the one-shot scripts under `scripts/_*` that this branch added before the PR.

## 16 Sep 26 — shorts demo v3: tracked pin on the wrong object, text outside the 9:16 safe zone (owner RCA order)
Owner on sh-hawaii-lowell-1 v3: "the circle is off … an overcook", "texts mangled/overlapping/out of viewport",
"you missed on both cases today". Both pins and their labels were removed for v4; the video never ships a pin.
The RCA is training for the next pin.
- **Pin 1 (lineman): the ring tracked foliage because the seed box was a guess.** The tracker (OpenCV MIL, then
  5-frame smoothing, keyframes every 3rd frame baked into gsap) did exactly its job on the box it was given.
  The box came from a subagent reading a gridded frame and *estimating* pixel coordinates (380,470,230,380); the
  lineman was at about (782,718). No step compared the box to the picture before 30 s of keyframes were baked.
  Rule: **a tracking seed is verified visually before tracking** — crop the ROI out of frame 0, and draw the
  ring on frame 0 AND the last tracked frame of the source, then a subagent answers one yes/no question per
  image: "is the ring on the <named object>?" Only a yes on both starts the bake. For people and vehicles,
  seed from a detector (YOLO/HOG person box), not from a coordinate estimate.
- **Pin 2 (truck): MIL lags on real motion.** On the moving vehicle the ring trailed the object by roughly a third
  of its width. MIL is a template tracker; it is fine for a slow pan, not a moving subject. For anything that
  moves, use per-frame detection or a stronger tracker (CSRT/KCF at least), and still run the two-image check.
- **The labels went off-frame because `overlap_check.mjs` reads static layout.** The label was placed with a
  gsap `x` tween that carried it past 1080 px at runtime; the static rect was inside. Captions and the close
  card also sat in the Shorts UI zone (title, buttons, right rail), which no gate modelled.
  Fix shipped: `scripts/shorts_lint.mjs` (see references/shorts/PLAN.md step 5) measures every visible text
  element at runtime, 0.25 s steps, against the frame, the safe zone and each other. Proof: on the v3 index.html
  it reports 18 findings (the off-frame label, 7 captions, the head, the close card); on v4 it passes.
- **Layout that passed for 9:16:** head at y 250, captions at y 1220, close card at y 1190, quote card at y 560,
  chips at y 960 sliding in from x −60 (was −500, which the lint flagged as off-frame mid-tween), all with
  right 180 px so the right rail stays clear.
- **Preflight trap:** the ffprobe spawn probe measured 0.94 s (gate 0.4 s) on the first launch right after a
  Chromium-heavy lint run; the same shared binary spawns at 0.14 s warm. Re-measure once on the idle box
  before touching anything.

## 15 Sep 26 — first two Format C (rolling update) builds, ms-indonesia-four-volcanoes + ms-hawaii-lowell-outages
- **Frame reviewers misjudge edges and coastlines.** "Pin in the water" / "touches the right edge" were wrong twice; a PIL pixel check
  on the snapshot (or the source map's land/sea mask) settles it in seconds. Use the mask to place pins in the first place.
- **shot_comp.mjs staging copies** (`compositions/_shot_*.html`) get graded by graphics_qc; delete them right after snapshots.
- Overlap checker sees only `p-` overlays: superseded by scripts/overlap_check.mjs:38 (every timed index overlay except bo-/nx-/sx-/clip-/v- ids, 17 Sep 26).

## 2026-09-12 · MG eval: a tidy diagram with the island underwater scored 21/25
- Three Sonnets and a blind reader built and ranked g-slope from a brief that described a LOOK (tall cone 338 m → shorter
  cone 110 m, 27° → 16°) with no datum, no orientation, no source figure. Winner had the post-collapse island submerged;
  the numbers themselves were wrong (27° is the pre-collapse slope ABOVE water, now ~7°; the underwater slope went
  24° → 16°, Meredew 2026). Every check in the chain (scaffold read, blind reader, graphics_qc) measured layout.
- Fix, durable: `references/mg-brief-template.md`. Brief = SOURCE figure + DATUM/SCALE/ORIENTATION + geometry in px +
  MUST-BE-TRUE list with ratios, all numbers confirmed first. Review order: meaning → layout → motion → code gate.
  For bespoke diagrams the orchestrator reads one final frame itself against the truths.
- With the complete brief both Sonnets (polish-first and scaffold-first) produced physically correct diagrams in 2–3 loops,
  ~11–15 min, ~310k tokens each; one caught a contradiction inside the brief and reported it. Scaffold-first still finds
  layout defects cheaper; the brief is what makes the picture true.
- GSAP gotcha: an un-positioned `tl.set()` lands at the END of the timeline as built so far; inserting positioned tweens
  above it silently shifts it (panel vanished at 5.5 s). Add late fixes at the end of the timeline, always with positions.
- The blind reader reported the NE label present when it was hidden under a rock fill; the orchestrator's own frame read
  caught it. Vision-agent verdicts get one spot-check by the orchestrator, every time.

## 2026-09-11 · Krakatau #4 mistake ledger: which gate should have caught what
- Catchable and now gated: nowrap text off the frame (overlap_check `off-frame`, measures scrollWidth and the
  viewport), an overlay stacked on a card (overlap_check `overlay-on-comp`; the builder now sends such overlays to
  the right half), glass cards flagged "undesigned" (the detector only knew gradients; backdrop blur now counts).
  That last one was a true positive I had filed as a known false alarm: a red gate is never noise until the current
  artifact was opened, and real noise gets the detector fixed the same day.

## 2026-09-11 · Krakatau #4 slice QC: text that runs off the frame, and blind clip picks
- Slice renders (5 windows, 10 fps, ~2 min each) caught what the static suite cannot see: a 25-char popfig
  cut at both frame edges, three bug headlines (63–84 chars) truncated mid-word, and a popfig stacked on the
  siren-chain card. Root cause: no width gate on nowrap text. Fix: character caps in FORMAT.md (popfig ≤16,
  chip ≤52, bug ≤60) asserted by the builder; long thoughts become chips.
- graphics_qc "undesigned" on glass cards as a known false alarm: superseded by scripts/graphics_qc.mjs:190 (backdrop blur counts as designed, 11 Sep 26).

## 2026-09-08 — breaking lane v1 (br-elnino-california, /mini-storms first run)
- **Static gates vs the fast format:** `graphics_qc.mjs` reports "0 elements · flat background"
  on 1.6 s chapter cards — its sample grid never lands inside the window (false negative,
  verified by `_shot_comps` screenshots at 0.05/0.3/1.2 s). `sweep_episode.py` counts only
  track-2 hosts as "mounted" (superseded 21 Sep 26: any host on any track), so a whole-video lower-third bug cannot be a sub-comp on track 3
  (flagged unmounted) or on track 2 (same-track overlap with cards) → the bug is inline markup
  in index.html. `_shot_comps` staging files (`compositions/_shot_*.html`) must be deleted
  before sweep or they read as unmounted comps.

## 2026-09-08 — breaking lane, first video (br-elnino-california): owner corrections + measured facts
- **Owner rules added after the v2/v3 previews (2026-09-08):** narration always above every bed (score 0.13,
  ambience ≤0.20, rumble 0.16; ebur128 per-15 s momentary spread ≤3 LU across the narration span); eyebrow
  under a red popfig = local radial scrim + 38 px Arial Black with a stroke (no glass); film layer (vignette,
  grade, grain, dust) OFF during the CTA window so the QR reads. "Breaking" renamed **mini-storms**; both
  channel skills now live in `skills/` and are junctioned into `~/.claude/skills/`.
- **Whisper writes digits, cue phrases must too (2026-09-11):** "twenty four minutes" never matches; the transcript
  says "24 minutes", "36 ,417" (merged to "36417" by the cue tokenizer), "9th of july", "5 to 10". Run the cue check
  (every overlay + card cue resolves) before the timeline build; 30 of 62 cues failed the first pass on Krakatau #4.
- **Overlay sync RCA (owner 2026-09-10, Krakatau v1 draft: "MGs not syncing, some early, some late"):** every
  popfig/chip time in the scratch builder was an estimate at 2.6 words/s from the script; measured against words.json
  they were 2–4 s off in both directions ("25 HOURS" 3.5 s early, "437 DEAD" 3 s early, "PULVERISED GLASS" 2.8 s early).
  The card rows, which used `word_at()` cues, were right. Root fix: every overlay carries a cue phrase resolved from
  `audio/<seg>.words.json`; unmatched cue = build failure. Also found while reading the transcripts: pocket-TTS split
  two >24-word sentences and repeated/mangled fragments ("drifting west, drifting west", "affected"→"lifted", "not a
  wave"→"not if if"); the owner did not hear them, the transcript showed them. Read every transcript before the timeline.

## ep6 ship (2026-08-23) — hyperframes 0.8.x, the hidden-console chain, and a preflight bug
- **overlap_check v2 must `page.close()` the index page before staging comps** — the episode page
  holds ~80 videos; keeping it open while staging 14 comps crashed the renderer ("Target
  crashed"). Fixed in `scripts/overlap_check.mjs`.
- **MG library built (2026-08-27, owner-ordered).** `library/` = catalog-index.json (195
  storm-relevant official HyperFrames items triaged by 12 vision agents from 286 candidates;
  82 top-scored with full local source in `library/official/`) + 8 in-house exemplars +
  15 overlay-snippet groups extracted from shipped eps (`library/inhouse/`), + localhost
  gallery (`library/gallery/`, serve from `library/`). Extraction gotcha worth remembering:
  **sub-comps inherit color/font from the EPISODE index.html body styles** — an extracted
  g-*.html is NOT self-contained until those inherited rules are baked into its own <style>
  (first extraction pass rendered black-on-black). Official catalog metadata lives cached at
  `~/.hyperframes/cache/` (374 registry JSONs, zero network to enumerate); each docs page
  `.md` ships the item's full HTML source; `npx hyperframes catalog --query` is built-in
  semantic search — never build a custom one.

## ep6 draft v2 review — text collisions were a CHECKER false negative (owner 2026-08-22)
- **overlap_check v1 checked the wrong slices.** It sampled one instant per card/comp pair and
  never looked at comp-INTERNAL text or mid-tween positions; every owner screenshot (AUG 23 over
  the DEPRESSION chip, FLORIDA LANDFALL mangle, 80% twice) was in a class it did not sample.
  v2: stage each comp (template → bare gsap page — loading the raw `<template>` file renders
  NOTHING and silently PASSes), step 0.5s through the host window, post-transform bboxes of all
  visible leaf text, pair intersection >25% of the smaller box, dup-fact strings, card zones vs
  comp text. Two real bugs it then caught in its own first runs: the template staging (above) and
  a card whose only line held an `<em>` had NO leaf → full-frame zone → "collided with everything".
- **Rules now in references/mg-quickref.md "Text doctrine" (DESIGN.md "On-screen text rules" until 26 Sep 26)**: zone occupancy, one fact one instance, no
  decorative eyebrows, narration order/wording, glass under any text over footage, small text
  never alone (BFMG). Encoded because the same four habits shipped in v1 AND v2.
- **Pre-render frame composites without a render:** a one-shot playwright script can hide every
  `[data-start]` element outside T, seek videos (`currentTime`), inject the comp template into
  its host div and seek both timelines — ~5s per frame, faithful enough for layout QC at every
  owner-flagged timestamp. Scratch-space only (tripwire: it reads, never authors).

## Owner pivot 2026-08-12 — cadence, sourcing, SFX, durable references
- **Graphics exits need ~1s land time** after the last beat — v2 cut scenes one or two frames
  after motion ended, repeatedly ("one time is okay... three and four and five times?").

## ep3 v3 — stop rendering to find things a script can find (2026-07-29)
- **You do not need a render to blackdetect.** `blank_scan.mjs` inlines each composition into
  a bare page with gsap, seeks its timeline at 0.25s, and sums the on-screen area of every
  element with computed opacity >= 0.06. A comp that goes empty shows up in seconds. It found
  a real 0.75s hole in g-close between the closing lines and the title card. Exclude the
  background texture (`.drift`) from the ink sum — it is present in every frame by
  construction and would mask exactly the failure being looked for.
- **An SVG `stroke-dasharray` shorter than the line it hides paints the overhang as a second
  dash, from frame one.** A route polyline measured 1377.6px and I wrote 1360: a 17.6px red
  mark sat in Indiana for the first eleven seconds, an hour of story before the storm gets
  there. Same bug again on the strikethrough line at 1040 vs 1041.4. Compute the length,
  then `ceil() + 1`. Never type a dash length.
- **`MotionPathPlugin` is not in the bundled `gsap.min.js`.** Move a marker along a route with
  per-leg `attr:{cx,cy}` tweens timed to each leg's own length, or the speed jumps at corners.
- **Chromium will not parse a staged page saved as `.html.tmp`.** MIME sniffing is by
  extension; every composition reported "no timeline" until the file was renamed `.html`.
  Keep it out of version control with `.gitignore`, not a clever extension.
- **Retiring a graphic means retiring its generator entry, its `_durations.json` key and the
  file.** Dropping only the mount left `g-panel-lone` authored-but-unmounted, which the
  sweep caught immediately.
- **A gate that only counts the first cycle of a repeating tween reports moving frames as
  dead.** `beat_density.py` scored `repeat:3` as one cycle; eight compositions carried
  inflated max-still numbers. Total motion is `duration + repeat * (duration + repeatDelay)`,
  and `yoyo` does not change it.
- **The episode should end when the closing card's content ends.** Two bugs stacked: the
  card's background drift ran 0.6s past its own credit fade, and the timeline's total ran
  past the card, so `close_picture_gaps` stretched the host to reach it — 3.69s of frozen
  black after the last visible frame. ep2, the shipped reference, ends at 0.00s of tail.
  Trimming the ending then exposed a second defect: the leftover hold cut from the credits
  to a 1925 damage photograph for 1.54s. The last segment in `ORDER` takes no tail.

## ep3 v3 - second audit round (2026-07-29)
- **Check for authored-but-unmounted compositions every build.** Three graphics passed every QC
  gate while being mounted nowhere - including the stat panel for the episode's longest segment,
  which therefore ran 48s with no graphic at all. `authored_ids - mounted_ids` must be empty.
- **A counter must open on its first tick's value.** The path maps shipped the END toll in the DOM
  (490 dead, 4:00 PM) and then animated backwards to 5 dead at 1:14 PM.
- **Narration-cued means EVERY graphic, not just the ones with a cue helper.** The met map fired
  its five labelled blocks in diagram order - four were 5-18s off their spoken word, one directly
  contradicted the voiceover. Hand-authored compositions need the same words.json alignment the
  generated panels get.

## ep3 v3 (2026-07-29) — the "check the code, not the frames" rebuild
- **Never tween a layout/text-reflow property.** `gsap_non_transform_motion`: `letterSpacing`,
  `width`, `height` snap to integer device pixels under the seek-by-frame capture engine and
  stutter on any slow/ease-out move. Use transforms — `scaleX`/`scaleY` with an explicit
  `transformOrigin`, or `x`/`y`. A growing bar is `scaleY:0→1`, never `height:0→900`.
- **Never set an initial transform in CSS when GSAP will tween any transform on that element.**
  `gsap_css_transform_conflict`: GSAP rewrites the whole transform matrix, silently discarding
  a CSS `scaleX(0)` or a `translateX(-50%)` centering. Set the initial state with `tl.set(...)`
  at t=0 instead.
- **Sub-composition asset paths are resolved against the PROJECT ROOT, not the comp's own
  directory.** `../media/x.jpg` renders but 404s in Studio preview. Always `media/x.jpg`.
- **A graphic's duration must be DERIVED from its resolved narration cues, never hand-estimated.**
  Panels whose rows are cued off `words.json` slid off screen at the hand-guessed duration while
  later rows were still firing on an off-screen card, and the host window sat empty for the rest
  of the segment. `dur = max(declared, last_cue + tail)`.
- **Idle warnings on an overlay panel are not the same defect as idle on a full-frame graphic** —
  the panel sits over a moving photo. But the card's own content still must not sit dead: one
  continuous transform tween spanning the window fixes it and costs nothing.

## ep3 v2 (2026-07-28)
- **StaticGuard boundary rule**: any GSAP fade that ends exactly at a clip-window boundary needs a `tl.set(..., {autoAlpha:0})` hard kill right after the fade, or validate flags stale-visibility risk.

## 2026-07-26 — ep2 v1 owner review (9/10; every item below is a standing rule now)
**Composition contract:**
- **Exit animations must end fully gone** (autoAlpha:0 + overshoot the slide). `x:660` on an
  820px panel left a stuck sliver for ~1s until the host window closed — owner caught it at
  three timestamps. Snapshot host-end−0.5s to verify every panel exit.
- Panel gradients: `box-sizing:border-box`, text inside the SOLID zone (live, references/mg-quickref.md). The dark backing chip under text over media: superseded by the glass card (26 Sep 26).

## 2026-07-26 — ep2 overnight build (tooling gotchas, all reproduced)
- `.lt-loc` text-shadow alone was unreadable over white map graphics; the dark backing chip fix is superseded by the glass card (references/mg-quickref.md, 26 Sep 26).

## 2026-07-23 — v3 pre-render multi-agent QC sweep (owner-ordered; caught what 2 shipped versions missed)
3. **CDN GSAP caused 10s navigation timeouts** in validate/snapshot — vendor `gsap.min.js` into
   the episode dir and reference it relatively. Deterministic + faster.
5. Namecards need scrim bars (`display: table; margin: auto` per line — inline-block puts
   name+sub on ONE row; transform-centering fights GSAP y-tweens).

## 2026-07-22 — owner review of ep1 v1 (9/10, "best one till date"; ~80% of issues = cadence + repetition)
4. **Graphics never idle**: ≤3s from graphic-on-screen to first payoff element (v1 polygon sat
   ~10s). Reveal ON the word (match cut) — owner loved the UNSURVIVABLE match cut, flagged
   CATASTROPHIC landing 5s before its word.
5. **Number reveals**: never pre-reveal in an eyebrow/fine-print (v1 spoiled 161); counter rolls
   fast then dramatically slows into the final number; secondary stat (158) appears AFTER.
6. **Lower-third sub-line readability**: dark-amber italic serif fails on busy ground — bump
   contrast/weight or give it a backing bar.

## 2026-07-22 — demo-joplin-90 (first E2E, owner: "incredible")
- Grain/vignette/dust as a timeline-driven seeded canvas = deterministic and cheap; reseed ~12/s.
