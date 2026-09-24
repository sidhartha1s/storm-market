# LEARNINGS.md — storm-market

Every owner correction / measured surprise lands here same session. Newest first: add new entries directly under the Promoted rules index, never at the bottom.

## Promoted rules index

Standing rules still governing episode quality, compacted from the journal below. Each
line is a pointer, not a copy — find the full context by searching the journal for the
quoted section header.

- The ebook CTA is a must-keep contract, positioned by the `config.yaml channel.cta` window: late, 85-95 % since 23 Sep 26. → §"the ebook CTA is a channel asset + a must-keep contract"
- (superseded 2026-09-09: the upload file is the 1080p master, no upscale step; the owner upscales by hand.) The 1440p HEVC file was the YouTube upload artifact; re-run the master gain/limiter step on any owner-supplied cut before the 2K upscale, never bit-copy its audio. → §"1440p upload file is HEVC now"
- mp4 surgery on a finished render uses h264_nvenc first, never libx264 — the quality gap doesn't survive YouTube's transcode at consumer-master bitrates. → §"1440p upload tier + NVENC-first for mp4 surgery"
- Convert GIFs before mounting (single-frame → PNG, animated → mp4); every mounted video needs an audio stream — mux silence into mute clips. → §"ep6 render-failure ledger"
- Audio slots longer than their file are silently truncated (WARN, not FAIL) — read the WARNs of a failed render; clip windows must never exceed the real clip length. → §"ep6 render-failure ledger"
- Batch every owner approval ask into ONE message, as early as possible — scattered mid-run checkpoints don't reliably land. → §"ep6 owner rules + broadcast-geometry gotchas"
- The hook must contain zero muted/mediocre elements — every beat is mid-action with its own audio. → §"ep6 owner rules + broadcast-geometry gotchas"
- Video-range black is Y=16, not 0 — threshold pillarbox/blanking detectors at ≤17, or use cropdetect. → §"ep6 owner rules + broadcast-geometry gotchas"
- Broadcast compilation reels have per-segment geometry — run cropdetect per cut window, never one blanket crop per reel. → §"ep6 owner rules + broadcast-geometry gotchas"
- Budget scripts on the previous episode's manifest wpm, then verify against the new manifest after the first full TTS run — probe-TTS only catches gross errors. → §"ep6 TTS + sourcing"
- Scene picking from long reels goes through contact sheets first — never per-frame agent probing. → §"ep6 TTS + sourcing"
- Scripts are written on the retention lattice (`references/script-scaling.md`) — read it before writing any script. → §"ep5 kickoff: the retention lattice + script fact-QC layer"
- Script fact-QC closes every `[verify]` marker before TTS runs; a conditional fact that fails verification gets cut, never softened. → §"ep5 kickoff: the retention lattice + script fact-QC layer"
- Every audio-carrying insert is transcribed in full before cut selection; the cut lands on the transcript's action/emotion peak. → §"ep5 kickoff: the retention lattice + script fact-QC layer"
- The hook has no black start — frame one is already mid-action, anchor audio already mid-transmission. → §"ep5 kickoff: the retention lattice + script fact-QC layer"
- The generator tripwire: any script that authors episode HTML (chooses cuts, holds, graphics, timings) is forbidden — delete it on sight. → §"CHECKPOINT: revert to the ep2 method"
- The full hook contract lives in DESIGN.md — apply it from episode scene one, don't rediscover it. → §"ep2 hook rebuild + ship"
- `--workers` must be pinned on every full render, never left on "auto". → §"ep2 hook rebuild + ship"
- Shipping while another session holds `.git/index.lock`: work from a `git worktree add`, never touch the main checkout. → §"ep2 hook rebuild + ship"
- Insert/AV cuts land on sentence boundaries via transcript, always — never mid-sentence. → §"ep2 v1 owner review"
- Verify each CUT, not just the source video — extract a frame from the cut itself and check chyrons/landmarks against the claimed event. → §"ep2 v1 owner review"
- The draft-proxy render (`--quality draft --crf 32 --fps 15 --workers 3`) is the mandatory review path; full-quality renders only after the owner approves the draft. → §"draft-proxy render validated"
- Cadence is reasoned per clip, never defaulted — any hold over ~8s needs a written reason; no visual repeats within an episode outside a flagged callback. → §"owner review of ep1 v1"
- The sync rule: the frame on screen must never contradict the narration (named entity / time-of-day / timestamp ⇒ a matching or neutral visual). → §"owner review of ep1 v1"
- Never claim an editorial rule "fixed" from memory — re-run the lint/checks on the actual final file before claiming it. → §"RCA: "repeats fixed" claim was FALSE"
- Exhaust every static gate, then render once — a render is the last step, never a diagnostic tool. → §"ep3 v3 — stop rendering to find things a script can find"
- Run blackdetect on every render — the picture track can be empty while every static gate (lint, graphics_qc, hyperframes check) still passes. → §"ep3 v3 — the defects no code gate was looking for"
- `grep -o ' id="[^"]*"' index.html | sort | uniq -d` must print nothing before every render — duplicate element ids render black with no gate catching it. → §"Duplicate element ids render BLACK"
- `optimize_clips.py` must preserve audio and mux silence for mute clips; ffprobe every insert clip for an audio stream before rendering. → §"optimize_clips.py strips audio and ignores bitrate"
- Long renders launch via schtasks (or `run_hidden.vbs`), never harness background Bash — the reaped child tree dies silently mid-capture. → §"Harness background tasks get reaped"
- Stills run 3–6s max, always with motion; video beats may run up to 12–15s when the clip genuinely matches the narration. → §"Owner pivot 2026-08-12"
- The doctor rule: a known-below-spec deliverable means STOP before the render, state exactly what's broken, and wait — never render on a known defect. → §"The doctor rule"
- Count SOURCES, not cuts, when sourcing — assertion assets (broadcast pulls, official audio, survivor clips) beat another angle of the same b-roll. → §"Sourcing doctrine for future episodes"
- The full audio-mixdown scan (volumedetect on 30s windows) is a mandatory pre-render gate, not optional. → §"Audio mixdown as a pre-render gate"
- `scripts/audio_levels.py` is the gate for insert/narration/bed levels — run it before every mixdown build. → §"Audio levels + media budget hardening"
- No visible windows, ever — every scheduled/background command runs through `scripts/run_hidden.vbs`. → §"No visible windows, ever"
- The on-screen text rules (zone occupancy, one fact one instance, no decorative eyebrows, glass under text over footage) live in DESIGN.md — `overlap_check.mjs` v2 enforces them. → §"ep6 draft v2 review — text collisions were a CHECKER false negative"
- hyperframes 0.8.6–0.8.10 opened visible console windows on this box; 0.8.41 does not and is the pin since 16 Sep 26 (its mixer is a flat ~1.5 dB quieter, corrected by the master step). → §"ep6 ship", §"16 Sep 26 — pin bumped to 0.8.41"
- Search `library/catalog-index.json` / `npx hyperframes catalog --query` before hand-authoring any graphic — MG library-first. → §"ep6 ship"

## 2026-09-23 - CTA moves late by default; hooks carry zero fluff; the owner edits scripts in a review loop
- CTA: the owner judged the 30-40 % placement was not converting and only annoyed viewers. The documentary default is
  now 85-95 % (`config.yaml channel.cta.window`), placed where it does not interrupt a reveal. He may move it again.
- Hooks: straight to the point, no fluff, and matched to the title and thumbnail more than to anything else. He was
  editing fluff out of shipped hooks by hand.
- Numbers that are a feat, not the point (a rail car's weight, the distance it flew), are said roughly ("about seventy
  thousand pounds", "nearly five hundred feet"). Do not build the hook on a spectacle the viewer cannot relate to; the
  hook needs a stake or a contradiction the viewer feels.
- Script loop: angle is agreed in a short brainstorm first, then the script is shared as a file. The owner edits it in
  place over a couple of sessions. Each round, `git diff` his edits against the committed draft, name the pattern
  behind each edit, and add it to `references/script-framework.md` so the next script starts with it.

## 2026-09-22 - ep-1974 shipped 17:30 against a 22:00 target: three guesses stacked

- **Measured:** script 3,027 words; raw TTS 18.4 min (165 wpm native, not the 152 assumed); atempo 1.10 made it
  16.7 min of voice (181 wpm is script words over voice minutes; words.json over the wav measures 176.0 wpm); non-voice time 48 s, not the 2.2 min constant. 22:00 became 17:40, then
  17:30 after the owner's cuts. Owner: "you under delivered the minutes of last video."
- **Why:** the budget line in edit_script.md multiplied a guessed pace by a guessed overhead, and the probes the
  plan asked for were made but never fed back into the count. wordcount.py's own footer printed 20.3 min and the
  script was locked anyway.
- **Fix:** `scripts/word_budget.py` measures pace from probe wavs at the shipping tempo and takes the real
  non-voice seconds; it FAILS outside target +/- 1 min. Nothing goes to full TTS while it fails. Checked against
  ep-1974's own audio: it predicts 16:53 for the shipped script (actual 17:30; the two probes ran 4 % faster than
  the episode average, so probe with two segments of different sentence length).
- **Rule of thumb at this voice and tempo:** about 180 words per delivered minute; a 25:00 documentary needs
  about 4,400 narration words.

## 2026-09-22 - ep-1974 draft 2 review: narrator opens the video, banned audio is gated by hash, holds need a reason

- **No broadcast, radio or archive audio in the hook.** Owner: "these broadcast stuff at the hook is a nono. because of bad
  audio quality. no point if the narrators hook being 10/10 if only 40% people wait till it starts at 10secs." The narrator's
  first line is 0:00. DESIGN.md "Cold-open hook contract" is rewritten; the old "anchor line by 2.5 s" rule is gone. The date
  popfig sits inside the first second and clears before the first designed graphic (here 0.15 to 1.65 s).
- **A banned sound came back under its other filename.** `wind-loop.mp3` was marked banned in `assets/sfx/provenance.md` on
  16 Aug 26; the builder mounted its source file `02_wind_ominous_steady.mp3` three times (4:00, 4:58, 10:06). A ban written
  as prose on one filename is a suggestion. Fix: `assets/sfx/BANNED.md5` lists banned audio by content hash and
  `lint_timeline.py` fails on a match, so a rename or a copy cannot dodge it. Proven: the old timeline fails with three
  findings, the new one passes. A future ban is one line in that file.
- **A `hold` whose only content is a bed reads as a mute stretch.** Owner at 5:03 to 5:08: "its mute, with only bgm. why?"
  It was an authored 4 s hold on a lone still with the banned wind under it. A hold earns its place only with diegetic sound
  that belongs to the picture (a siren over the siren, the tape over the tape). Otherwise close it to a 0.3 s breath.
  Two more holds remain (3.0 s at 237.09 s and 3.5 s at 599.71 s in the new cut); both sit under a moving map and were not named.
- **Why the plane graphic failed in draft 1 and passed in draft 2.** An SVG element carried a static `transform="translate()"`
  attribute AND a GSAP x/y tween. GSAP takes over the transform and discards the attribute, so the icon flew from 0,0 while
  its trail drew in the right place. Same family: `transformOrigin` in CSS px on a nested SVG line pushed it outside the
  viewBox (use `svgOrigin` in user units). No gate checks that a mover follows its path, and a still frame looks plausible
  unless you know where the icon should be. Rule for every "A follows B" animation: position the mover with GSAP only, and
  assert in the DOM that the mover sits on the path head at three times before calling it done.
- **The draft rendered before ten graphics were finished.** I found text behind the presenter circle by looking at the draft,
  then fixed it. The builders never had the circle's box in their brief. The box (x 1632 to 1888, y 700 to 956) now goes in
  every builder brief, and no render starts while a builder is still editing (CLAUDE.md "the render is the LAST step").

## 21 Sep 26 — owner review of the ep-1974 draft: "shippable after these small iterations"

Owner watched the whole 17:39 draft ("overall really well put video", the motion graphics "a significant better look
this time", 14:05 the combed-trees card "interesting bit"). Corrections, each persisted here:
1. **Motion graphics go static after the story beat lands.** `beat_density.py` said 0/39 because a 100 px grid drift
   over 78 s counts as a tween; to the eye 1.3 px/s is a freeze, and blackdetect read four dark cards as black for
   6 to 11 s. Rule: every comp carries a VISIBLE ambient element for its whole window (a scan line at 6 px/s or more,
   staggered dot blips at least every 1.5 s, a sweep rotating), finite repeats, never `repeat:-1`. Verify by pixel
   diff of two frames 2 s apart at three points in the window, not by tween coverage.
2. **Paul's presenter circle belongs on docs too** (bottom-right 240 px, FORMAT.md "Presenter circle"): from the end
   of the hook to the CTA dip and from the CTA out-dip to the close card, hidden in the hook, the CTA and the close.
   Every RHS rail, cite card and person card stays out of x >= 1600, y >= 680.
3. **CTA at 85 to 90 % on this doc**, not 30 to 40 %: owner 21 Sep 26 "keep around 85-90 % timeline in a fitting
   manner", fallback "reduce the end ask, then the video, one more sentence, close". ep-1974 sits at 88 % after the
   16-dead-then/4-now payoff. `config.yaml channel.cta.window_by_slug` carries per-episode placements; the deep-lane
   window stays until the owner moves it for the lane (one-orange rule). The 30-40 % rule dates from 30 Aug 26.
4. **Glass cards over a dark map read better beige** (owner frames at 08:08 and 15:15): cite cards go to
   rgba(232,222,200,0.90) with dark text; other glass panels over dark gradients are the builder's call, reported.
5. **A person card without a real photo does not keep the photo slot** (owner: "don't leave the card with photo's
   space in"); monograms are out, text-only layout for the nine people with no PD photo (a sourcer checks first).
6. **Red popfigs**: owner is fine with the light use here ("its good. i mean it"); no retrofit, weigh them per episode.
7. **The g-plane icon rode a different coordinate space than its trail** (owner: "a moving house fly on the top
   left"): position markers must be verified by measuring the icon against the path head, never by eye.
8. **The F6 card's strike missed the glyph and the F5 hung outside the card**: a strike goes through the glyph body,
   every child stays inside the card box; screenshot the card at the last cue before shipping.

## 21 Sep 26 — first long render on 0.8.41: streaming needs two env vars, and the harness reaps renders

1. **0.8.41 streams captured frames into ffmpeg only for comps up to 240 s.** Anything longer takes the disk
   capture path and asks for ~8.3 MB per frame of temp space: 131 GB for a 17.6-min draft at 15 fps on a C: with
   22 GB free, so the render dies at "Starting frame capture" with `Disk capture may need ~131756 MB`. The shorts
   final and the pin-ritual demo (29 s, 84 s) never met this. `render.cmd` now sets
   `PRODUCER_STREAMING_ENCODE_MAX_DURATION_SECONDS=7200` and `HF_CAPTURE_PARALLEL_STREAM=true`; the second one
   is required with `--workers` above 1 (`shouldStreamParallelCapture` in cli.js), without it the log still says
   `streaming-encode gate enabled:false`. Read that gate line in every render log: `enabled:true` or the render
   will not finish on this disk.
2. **Harness background Bash is not a render launcher** (already in this file's index line, ignored under
   deadline pressure). The harness kills background tasks when free RAM drops near 2 GB, and the kill takes the
   whole cmd/npx/chrome tree: the 05:28 attempt died 35 min in with the log frozen at 25 % and nine orphan
   chromes. `schtasks /create ... /tr "wscript.exe <abs>\scripts\run_hidden.vbs cmd.exe /c <abs>\scripts\<task>.cmd"`
   plus `/run` (with `MSYS2_ARG_CONV_EXCL='*'` under Git Bash) is the only launcher; the `/tr` string has a
   261-char cap, so the per-episode wrapper `.cmd` (workers, overrides) keeps it short. Delete the task after.
3. **Draft timing on this box at 0.8.41, streaming, 2 workers:** 15 885 frames in about 13 min (frame 600 at
   06:08, complete 06:21), 186 MB at crf 32 / 15 fps. Two workers, not three, when free RAM is under 5 GB.
4. **A render preflight refusal for `ffprobe spawns in 0.40s` is a load reading, not a binary problem**, when
   the env already names the shared build: three whisper transcribers and two ffmpeg cutters from sourcing
   agents pushed a 0.17 s spawn to 0.40 s. Quiet the box (agents' jobs killed by their owners), re-measure.

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

## 2026-09-20 (later) — write sentences people say; one score; a hold replaces the blackout; fillers on probe
Owner on v4 Tanner passage ("Same town. One mile to the west. One hour later. Ninety eight miles long."): "your average
sentence is three to four words long, nobody speaks like this"; "in the dark" is filler; scores with a percentage
beside them are confusing; a 3.5 s hold followed by a blackout is 5 to 7 s of nothing.
1. **Fragments are banned.** The CLAUDE.md voice rule already says "flowing connective sentences, not chopped
   fragments"; the writer over-corrected the third-grader rule into trailer-speak. Sentences run 10 to 22 words,
   joined with and / but / because / so; one idea each, but a whole sentence. A fragment is allowed only as a spoken
   quote from a real person.
2. **Decoration words are cut** ("in the dark" when the clock already said 7:30 PM; "head on"; "by the way" unless it
   is a deliberate filler). Delete test per phrase, not just per sentence.
3. **One score per script, out of 10, from the independent grader, with one line on what would move it.** No
   confidence percentage in the owner-facing report (it lives in the grader file only).
4. **A hold replaces the blackout at that seam, never both.** Hold 3 to 4 s after a payoff over a moving picture
   with a bed; the act blackout stays only where there is no hold.
5. **Spoken fillers are an experiment, not a rule:** uh / um / you know / look / I mean / so / well / right? / by the
   way / actually, plus spoken grammar (repeat the subject: "the man who ran the office, he knew"; contractions;
   a trailing "right?"). One or two per 30 s at most. Probe both versions through pocket-TTS before deciding;
   probes for ep-1974 live in `episodes/ep-1974-super-outbreak/audio/probe/`.

## 2026-09-20 — plain American, literal clock times, atempo 1.10 on docs, and an independent grade on every script
Owner on the 1974 hook: "quarter to five" is confusing, say "4:45 PM"; "the day is only half over" is a riddle; "why did
knowing not save them" is Oxford English; "talk in a way a third grader can make sense of, talk like a human, you are
overstressing the documentary persona". Also: docs get atempo 1.10 like the minis (probe the hook first).
Rules:
1. Clock times are literal digits with AM/PM in the on-screen popfig and spoken as "four forty five PM". No "quarter
   to", "half past", "the day is only half over".
2. Register test per sentence: would a third grader follow it aloud? Short words, one idea, no inversion, no riddle
   phrasing. The documentary voice is a person telling a story, not a narrator performing one.
3. F5 vs EF5: 1974 and every tornado before 2007 is F-scale (F5); 2007 on is EF5. The owner read "F5" as a typo; the
   script now carries a one-line note so nobody "fixes" it.
4. **Every hook and every script (shorts, minis, docs) gets an independent grade before the owner sees it**: a
   separate skeptic-reviewer agent that has not seen the writer's reasoning rates the hook 0 to 10 with a confidence
   percentage, every chapter on the six script-os axes, draws the stakes curve, lists open-loop gaps, register
   violations and fluff sentences, and ranks the fixes. The writer fixes, re-grades, and reports both grades to the
   owner. A script ships to TTS only when the grader's hook score is at least 8 and no chapter axis is under 3.
5. Tension system, not taste: the loop table carries plant and pay TIMES; at any timestamp at least one loop must be
   open and unpaid; no 90-second window without a retention spike; stakes score per chapter never drops more than one
   point and ends higher than it started. Checked by the grader, and by `scripts/script_scorecard.py` once it exists.

## 2026-09-20 — hooks and CTAs carry fluff; the owner is cutting 30 to 40 s out of shipped videos by hand
Owner, 20 Sep 26: "your hook, maybe the very first sentence, maybe the second or third, it's just fluff. It doesn't get
to the point. At least give them the ROI." He trimmed Joplin and Tri-State on YouTube himself. Studio data: Tri-State
21 % watched, Joplin 25 %, Carr Fire 5.8 % after day one; the losses sit in the first 10 to 15 s.
Rules, every script from ep-1974 on:
1. **Sentence one is the payoff the title promised.** Numbers first ("Seven F5 tornadoes in one afternoon. Three
   hundred and thirty dead."), the specific image second, the question third. No scene-setting before the ROI.
2. **The hook is 45 to 60 words, 20 to 25 s including the insert.** Anything the viewer does not need to decide
   to stay is cut. Test: delete the first sentence; if the hook still works, the sentence was fluff.
3. **No roadmap phrases anywhere** ("one more thing before", "here is what that day would become", "in the next
   twenty minutes"). They read as delay. Fold the numbers into a sentence that already carries stakes.
4. **The CTA hinge is one tease sentence, not a paragraph.** The segment before the CTA ends on the loop in ≤ 25
   words; the segment after opens with the payoff in its first three words ("He wrote a six.").
5. **Owner-cut SRT diff is the retention gate for the next script:** before writing a new hook, diff the shipped
   SRT of the last video against what is live on YouTube and list what the owner removed; do not write those
   shapes again. (20 Sep 26: the live durations of Joplin, Tri-State and Super Outbreak still match the shipped
   SRTs to within seconds, so the trims may still be processing; re-check before the next script.)

## 20 Sep 26 — El Reno v3 post-mortem: stock footage was audible and no gate saw it
- Owner rejected v3 partly for "a lot of audio for the stock footages". Root cause: `<video>` elements
  mounted with neither `muted` nor `data-volume`. hyperframes plays such a track at 1.0, but
  `audio_levels.py` treated "no data-volume" as muted by convention and skipped them, so the levels gate
  passed a mix with unlevelled clip audio under narration.
- Fix (this PR): `audio_levels.py` now skips a video only when it carries `muted` (or data-volume 0) and
  levels every other video at its data-volume, default 1.0; `sweep_episode.py` check 5e fails any `<video>`
  that declares neither. Verified: ep6 trips on `kb-radarloop` (silence-muxed, harmless, but undeclared);
  ms-krakatau-sirens passes both gates with the same 19 audible elements as before.
- Rule: every `<video>` says what its audio is. `muted` for b-roll, `data-volume` for inserts and the CTA.

## 16 Sep 26 — pin bumped to 0.8.41 on owner order; the ritual's RMS drift is a flat mixer offset
- `pin_ritual.py` against 0.8.41: duration 84.000/84.000 s, black map 2/2 identical, RMS −16.91 → −18.04 dB,
  exit 3 (no bump, human decides). Evidence for the decision came from the shorts final, which exists on disk
  at both versions: 0.7.109 draft −12.9 LUFS, 0.8.41 final −14.5 LUFS. Windowed volumedetect on the same cut:
  narration windows −1.3 / −1.7 / −1.8 dB, the bed-only window −1.6 dB; narration-to-bed spacing 30.8 vs
  31.1 dB. Every stem moved together, the balance did not: a flat output-gain change in the 0.8 mixer, and
  `master_deliverables.py` measures and corrects the master to −14 LUFS regardless. Owner: "bump the pin".
- Bumped with the ritual's own `bump_pins()` (config.yaml + render.cmd) and the baseline record rewritten
  from the 0.8.41 demo render (`scripts/pin_baseline.json`: rms −18.04, peak −1.56); the next ritual run
  compares against 0.8.41, not 0.7.109. The demo mp4 is cached at
  `episodes/demo-joplin-90/renders/pin-baseline-0.8.41.mp4` for SSIM.
- New in 0.8.41 and worth reading in every render log: `audio_volume_tween_overrides_gain` (a gsap `volume`
  tween now REPLACES `data-volume`, it does not scale it; demo-joplin-90's bgm trips it) and
  `audio_src_not_found` blocks the render instead of shipping a silent track.
- Ritual gotcha: it prechecked only `media/`, but `audio/` is gitignored too; two launches were wasted in a
  fresh worktree before the narration wavs were copied. The precheck now covers both.

## 16 Sep 26 — hyperframes 0.8.41 full render on this box: no visible windows, clean
Owner asked for the latest hyperframes on the shorts final instead of the 0.7.109 pin. Same flags as
render.cmd, `npx hyperframes@0.8.41`, sh-hawaii-lowell-1 (29.4 s, 1080×1920, 5 clips, 3 workers): rendered in
1m 18.7s, GPU probe NVIDIA, 0 black / 0 silent stretches, 4-frame subagent read identical to the 0.7.109 draft,
master -14.01 LUFS. Owner watched it: "didnt start opening 200 CMD windows … its smooth", so the 0.8.x
visible-terminal-tab problem that froze the pin is gone on this box at 0.8.41. Not a pin bump by itself: run
`scripts/pin_ritual.py` against 0.8.41 (the demo A/B on a 48-clip comp is the test that matters, a 5-clip
short is not) and bump on identical metrics.

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

## 2026-09-15 — Renders were on the Intel iGPU; pin headless Chrome to the GTX 1650
- **Every render up to 15 Sep captured on the Intel UHD iGPU.** `--browser-gpu` only asks Chrome for
  hardware D3D11; Windows hands an unpinned headless exe the integrated adapter. Measured on
  ms-elnino-cpc-today full (7:47, 2 workers): 26 min, CPU 100 %, render RSS peak 5.7 GB (the iGPU's
  frame buffers live in system RAM), GTX 1650 at 0 %. The owner could not multitask.
- **Fix is a per-user registry pin, no package patch:** `HKCU\Software\Microsoft\DirectX\UserGpuPreferences`,
  value = full exe path, data `GpuPreference=2;`. Chromium reads it; `--force_high_performance_gpu` adds
  nothing on top (probed both). Trap: hyperframes launches its OWN Chrome from
  `~/.cache/hyperframes/chrome/chrome-headless-shell/<ver>/…`, not the Playwright one, and every new
  build is a new exe path. `render_busy.py --launch` now pins every chrome-headless-shell.exe under
  both trees on every launch; `verify_render.sh` fails (exit 2) unless the log's
  `browserGpuMode probe →` line names NVIDIA.
- Still CPU by design in 0.7.109: ffmpeg frame extraction (~70 s for 48 clips) and audio; no hw-decode switch exists.
- RAM floor stays 4 GB: the GPU run's capture RSS is ~4 GB vs ~5–6 GB on the iGPU (k2 logs in the 15 Sep session).

## 15 Sep 26 — first two Format C (rolling update) builds, ms-indonesia-four-volcanoes + ms-hawaii-lowell-outages
- **Pronunciation gate before timing.** Read every proper noun back from the whisper words.json after TTS (Arupadhatu came out
  "Aeropoda 2-1", KIUC as "Kaiyo Sea", Haena as "Hina"). Respell phonetically in the narration blockquote only, re-synthesise, then
  time. Doing it after the timeline existed cost a full mechanical retime (~40 min). Probe-TTS the name list first next time.
- **words.json must be younger than its wav.** transcribe ran on one native wav before atempo in a crashed chain; the tell is
  words end > wav duration. Check before cueing anything.
- **Frame reviewers misjudge edges and coastlines.** "Pin in the water" / "touches the right edge" were wrong twice; a PIL pixel check
  on the snapshot (or the source map's land/sea mask) settles it in seconds. Use the mask to place pins in the first place.
- **shot_comp.mjs staging copies** (`compositions/_shot_*.html`) get graded by graphics_qc; delete them right after snapshots.
- **Two-worker draft render + Firefox = 0.8 GB free.** render_busy's floor is right; nothing else launches during a render.
- **Overlap checker only sees overlays with a `p-` id and a timed wrapper**; bare popfig divs are invisible to it (0 overlays,
  false PASS). Wrap every overlay in `<section class="clip" id="p-…" data-start data-duration data-track-index>`; chips and
  source labels on track 4, popfigs and quote cards on track 5.

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
- Auto-mode classifier refuses most new Agent spawns from command-heavy prompts ("Auto-Mode Bypass"); resuming an existing
  agent via SendMessage passes. Owner adds `Agent` to permissions.allow; the session cannot (Self-Modification).

## 2026-09-11 · Krakatau #4 mistake ledger: which gate should have caught what
- Catchable and now gated: nowrap text off the frame (overlap_check `off-frame`, measures scrollWidth and the
  viewport), an overlay stacked on a card (overlap_check `overlay-on-comp`; the builder now sends such overlays to
  the right half), glass cards flagged "undesigned" (the detector only knew gradients; backdrop blur now counts).
  That last one was a true positive I had filed as a known false alarm: a red gate is never noise until the current
  artifact was opened, and real noise gets the detector fixed the same day.
- Not catchable by code: what a clip shows. provenance.csv now carries a `shot` column (what is visible, including
  burned-in chyrons) for every broadcast cutter, written from one labelled contact grid read by a subagent; the
  builder refuses a cutter without one. Pick pictures from `shot`, never from a file name.
- Quote cards: the attribution era must match the cut underneath (Ulrich 1958 sat on an 1883 print); `shot`
  starts with an era/category token so the check is a glance.
- Process: list every violation in one pass before iterating (three gate cycles burned on one bug line at a
  time); write Windows-path scripts with the Write tool, never bash heredocs (the backslash-U escape trap, three
  times this session, once while writing this very rule).

## 2026-09-11 · OOM: the gate suite ran on top of a live draft render
- Draft (2 capture workers ≈ 2 Chromiums + node) + blank_scan + graphics_qc (2 more headless Chromiums) +
  optimize_clips (ffmpeg batch) + the owner's browser = 16 GB gone; the owner saw the OOM before I did.
- render_preflight only guards the render's own start, and direct launches skip it. New guard
  `scripts/render_busy.py` (exit 3 while any `hyperframes … render` node is alive; RENDER_BUSY_OK=1 override)
  is called from playwright_env.mjs (covers both Chromium gates), optimize_clips --apply, and the slice/draft
  launchers. Rule: one heavy job at a time; gates BEFORE the render, verify_render AFTER it, never beside it.

## 2026-09-11 · Krakatau #4 slice QC: text that runs off the frame, and blind clip picks
- Slice renders (5 windows, 10 fps, ~2 min each) caught what the static suite cannot see: a 25-char popfig
  cut at both frame edges, three bug headlines (63–84 chars) truncated mid-word, and a popfig stacked on the
  siren-chain card. Root cause: no width gate on nowrap text. Fix: character caps in FORMAT.md (popfig ≤16,
  chip ≤52, bug ≤60) asserted by the builder; long thoughts become chips.
- Picking broadcast cutters by file name ("f24_005 = 2026 plume") put an airport departure board under "same
  mountain, same mechanism, then where?" and a terminal corridor under the siren explainer. Rule: every clip is
  eyeballed (labelled contact grid, one subagent read) before it is wired; provenance.csv carries the source,
  not the picture.
- graphics_qc "undesigned" on glass cards is still the known false alarm; beat_density is the motion gate.

## 2026-09-10 — Krakatau packaging pass: owner corrections on title length and thumbnail plates

- **Titles aim under 60 characters.** Not a hard cap ("55 is not an upper limit"); low-value stretchers at the tail are fine, but an 87-char title was rejected on sight. Owner's own rewrite: "It Killed 36,000 First. Now It's Happening Again." (49).
- **Thumbnail plates are bright and detailed.** A night plate (deep shadows, moonless) was rejected: too dark, details not visible at phone size. The owner supplied a sunset eruption plate (`thumbs/owner-plate-sunset.png`, ChatGPT) as the reference look: golden light, vivid colour, sharp everywhere.
- **This episode's text: one red word, huge, at the top** (DEADLY / UNSURVIVABLE), no kicker. Instance decision for Krakatau, not a rewrite of the mini-storms ≤4-word + BREAKING kicker rule; propose generalising only if the owner repeats it.
- **ChatGPT renders thumbnail text in-image, and better than Pillow.** Owner: "it does most of my thumbnails itself." On the same plate the model's DEADLY beat the Impact composite. Prompt recipe (word in caps, position and width in percent, font by reference + hex, outline + shadow, "keep the photograph exactly as it is", negatives) lives in the `yt-packaging` skill, `references/thumbnail-production.md`. Driver: `~/Automation Projects/webgen/genimg.mjs edit|gen chatgpt-simplotel`.
- The `yt-packaging` skill (installed 2026-09-10 in `~/.claude/skills/`) now runs before any title/thumbnail work on this channel; its cover-one and redundancy tests are what caught the IT'S BACK / "Just Erupted" triple restatement.

## 2026-09-08 — breaking lane v1 (br-elnino-california, /mini-storms first run)

- **Structure vocabulary (owner correction):** HOOK is 3–10 s, one sentence paying off the title.
  Then INTRO to ~1:10 (stakes, open loops, promise). Then chapters. A 45 s "hook" was rejected.
  Size every section in words at the delivered wpm before TTS (packaging.md table).
- **Pharaoh pace on short news sentences = 158 wpm native** (1,426 words → 9:01). atempo 1.15
  pushed it to 182 wpm / 7:50 and was reverted. Measure before applying any atempo.
- **Static gates vs the fast format:** `graphics_qc.mjs` reports "0 elements · flat background"
  on 1.6 s chapter cards — its sample grid never lands inside the window (false negative,
  verified by `_shot_comps` screenshots at 0.05/0.3/1.2 s). `sweep_episode.py` counts only
  track-2 hosts as "mounted", so a whole-video lower-third bug cannot be a sub-comp on track 3
  (flagged unmounted) or on track 2 (same-track overlap with cards) → the bug is inline markup
  in index.html. `_shot_comps` staging files (`compositions/_shot_*.html`) must be deleted
  before sweep or they read as unmounted comps.
- **Scene-cut broadcast pulls:** ffmpeg `select='gt(scene,0.35)'` on 6 news reels gave 51
  usable 3–7 s cuts in one pass; windows must be clamped to the cut's real length (several
  were 1–2 s short → sweep "frame extraction failed" is the symptom).
- **Long map holds:** a 12 s NOAA outlook still fails the 6 s still rule; render it as a 13 s
  zoompan mp4 (`ffmpeg -loop 1 ... zoompan`) — passes as video and still moves.
- **Pexels API key in ~/.claude/.env returns 403 (dead); Pixabay key works.** Wikimedia Commons
  API rate-limits after ~10 file fetches (429) — batch with a pause.
- Reuse pool for the whole El Niño series: `library/mini-storms/el-nino-2026/` (+ provenance.csv).

## 2026-09-08 — breaking lane, first video (br-elnino-california): owner corrections + measured facts

- **Hook is 3–10 s, then INTRO (open loops, stakes, promise) to ~1:10, then chapters.** Owner rejected a
  plan that called the first 45 s "the hook". Size every section in words at delivered wpm before TTS.
- **Pharaoh voice ran 158 wpm native on short news sentences** (1,426 words → 9.0 min). No atempo needed
  in this lane; the 129 wpm figure is a documentary-sentence number. Measure, then decide.
- **No chapter cards in the breaking lane** (owner, after the v1 preview): chapters butt-cut with a 0.45 s
  narration gap; the script's connective sentences carry the transition. Removing 8 cards = one-shot
  mechanical retime (events list: point, delta; starts shift for points ≤ start, ends for points < end).
  Gotcha: a narration window whose end sits 0.01 s past a removed span gets shortened by the rule —
  restore every nx-* duration from audio/manifest.json after any retime, then re-check gaps.
- **CTA v5 (owner "newest paul CTA sep 6", 2560x1440 source) is transcoded to 1080p30 as the versioned
  asset** `assets/cta/paul-storm-ready-v5-sep6.mp4` (md5 in config.yaml); media_budget refuses 1440p
  sources. hyperframes validator wants `data-has-audio="true"` on the audible CTA video.
- **Sweep's CTA gate skips `br-` slugs** (epN-only). Breaking episodes mount the CTA by hand; the
  30–40 % window is a documentary rule — this one sits at 43 % (after chapter 3) by story logic.
- **graphics_qc cannot sample a 1.6 s composition** (reports 0 elements / flat background); proved the
  cards with `_shot_comps` screenshots instead. Moot now that cards are gone.
- **Pixabay "mudslide" search returned an Amalfi-coast town clip.** Every stock pick gets a contact-sheet
  eyeball before wiring; the owner spotted it in the preview. Pexels API keys (all 3) are dead (403).
- **Instagram via `yt-dlp --cookies-from-browser chrome` fails while Chrome is open** (cookie DB locked).
  Use a cookies.txt export or close Chrome first. No social clips in this cut.
- **Render waiters get killed by the harness under memory pressure** (3 headless workers ≈ 3.8 GB);
  use one `Monitor` until-loop on the done marker, never several polling shells.
- Draft render of a 9:45 cut: 13 min wall-clock at 3 workers (frames ~9 fps at 15 fps draft).
- Runtime log for the 3 h SLA lives in `episodes/br-elnino-california/runtime.md`.

- **Owner rules added after the v2/v3 previews (2026-09-08):** narration always above every bed (score 0.13,
  ambience ≤0.20, rumble 0.16; ebur128 per-15 s momentary spread ≤3 LU across the narration span); eyebrow
  under a red popfig = local radial scrim + 38 px Arial Black with a stroke (no glass); film layer (vignette,
  grade, grain, dust) OFF during the CTA window so the QR reads. "Breaking" renamed **mini-storms**; both
  channel skills now live in `skills/` and are junctioned into `~/.claude/skills/`.
- **Video #2 (ms-elnino-texas) build recipe that worked:** cut lists hand-authored per narration segment as
  (kind, src, dur, id, callback); a scratch helper (never committed) computes butt-cut starts from the
  narration schedule and fills the last slot; overlays hand-authored as (kind, id, at, hold, big, sub).
  Total authoring ~25 min. Media probes in `sweep_episode.py` report "frame extraction failed" while a full
  render is running on the box — re-run the sweep on a quiet box before believing it.
- **Full renders refuse (exit 2) while a TTS run or a sourcing agent's ffmpeg is alive** (heavy-process
  limit 2). Sequence: TTS → sourcing → gates → render; never overlap them on this 16 GB box.
- **Gemini (nanobanana) free tier is exhausted** → thumbnail candidates come from real render frames
  (`thumbs/frame-cand-*.png`) until a paid key exists.

- **Homographs are a TTS trap (owner 2026-09-09, "AI-slop radar"):** pocket-TTS read "I read all the comments" as
  "I red" (past tense). Before TTS, scan every interaction line for read / lead / live / wind / tear / bass /
  close / present / record and respell the narration copy phonetically ("reed") while the script keeps the
  owner's exact wording. Listen to every interaction beat once after TTS; a wrong-tense homograph reads as AI
  slop to the audience. Owner's phrases are verbatim — never paraphrase a line he wrote.
- **Script retention pass (owner 2026-09-11, Krakatau #4 v1 → v2):** the v1 draft scored 5.5/10 on stakes per
  90 s: chronology order put the peaks (Lituya, the arithmetic) at 6:51 and 10:17 and the dips (1883, fix list, the
  not-happening list) after the CTA and in the last third; three macro-loops opened in the first minute and none was
  touched again for 6–10 min; the intro was a table of contents; the voice read out "December twenty second, twenty
  eighteen, three minutes past nine" while the MG could carry it. Owner: "just say two days before Christmas, show
  DEC 22, 2018 · 9:03 PM in MG; that's the engagement manipulation you are missing." Full rule set now in FORMAT.md
  "Retention architecture" and the mini-storms skill; the v2 hook is the owner's line verbatim.
- **A worktree's clip pool dies with the worktree (2026-09-11, Krakatau #4):** `library/mini-storms/<event>/` media
  is gitignored, so `git worktree remove` deleted the 72-asset Krakatau pool the moment #3 shipped; only the clips
  already staged into `episodes/ms-krakatoa-1883/media/` (bc + _orig + stills) survived, and the #4 builder had to
  fall back to them. Rule: before removing an episode worktree, copy `library/mini-storms/<event>/` into the main
  checkout (`robocopy /E`), then remove. Pools are cross-angle assets; the worktree is not their home.
- **Whisper writes digits, cue phrases must too (2026-09-11):** "twenty four minutes" never matches; the transcript
  says "24 minutes", "36 ,417" (merged to "36417" by the cue tokenizer), "9th of july", "5 to 10". Run the cue check
  (every overlay + card cue resolves) before the timeline build; 30 of 62 cues failed the first pass on Krakatau #4.
- **The TTS driver skips a segment whose wav exists** (`tts_episode.py --only` reuses the old file silently): delete
  the wav AND its words.json before any re-synthesis, or the "fix" never happens (Krakatau v2 c2/c7, 2026-09-10).
- **Overlay sync RCA (owner 2026-09-10, Krakatau v1 draft: "MGs not syncing, some early, some late"):** every
  popfig/chip time in the scratch builder was an estimate at 2.6 words/s from the script; measured against words.json
  they were 2–4 s off in both directions ("25 HOURS" 3.5 s early, "437 DEAD" 3 s early, "PULVERISED GLASS" 2.8 s early).
  The card rows, which used `word_at()` cues, were right. Root fix: every overlay carries a cue phrase resolved from
  `audio/<seg>.words.json`; unmatched cue = build failure. Also found while reading the transcripts: pocket-TTS split
  two >24-word sentences and repeated/mangled fragments ("drifting west, drifting west", "affected"→"lifted", "not a
  wave"→"not if if"); the owner did not hear them, the transcript showed them. Read every transcript before the timeline.
- **CTA first syllable clipped + post-CTA black too long (owner 2026-09-10):** CTA start was off the 30 fps grid and
  the blackout sat on the same track ending at the same instant. Fix: blackouts on their own track, CTA audio starts
  0.1 s under the black, all starts ceil-aligned to 1/30 s, dip-out 0.5 s. z1 hiss/long pauses: TTS gaps > 0.55 s
  replaced with 0.4 s digital silence via a words.json-driven ffmpeg concat, then re-transcribed.
- **A sleeping laptop kills TTS and sourcing agents silently (2026-09-09→10):** pocket-TTS hung at 4/13 segments for
  12 h with 6 orphan python processes; the sourcing agent's report never landed. After any overnight gap: check
  `audio/*.wav` count and the pool's provenance.csv before trusting either. Also: a `> TTS note` blockquote placed
  between a `##` heading and the next `###` is parsed as narration of the PREVIOUS segment by tts_episode.py — notes
  are plain lines, never blockquotes.
- **A full render is never a test (owner 2026-09-09, three wasted Texas full renders):** a mount/layout change is
  verified in this order and no other: read the renderer's runtime path in the pinned package → draft-render a
  20–30 s slice of the REAL index.html (`T0` window, ~1 min) and read one contact strip → re-run the static gate
  suite on the final file → post a one-message plan and wait for "go" → ONE full render. "The previous render
  looked fine" is void once the file changed; never launch a second full render to find out what the first did.
- **Check free disk before every full render, and delete a killed render's spool (2026-09-09, Texas):** the capture
  spool lives in `%LOCALAPPDATA%\Temp\hf-render-*` and reaches ~9–10 GB for a 10-min 30 fps full. Render #1 captured
  all 18690 frames and then died in the encode with ffmpeg exit 4294967268 (= -28, ENOSPC) at 98 % disk; hyperframes
  deletes its own spool on failure, so the frames are gone too and the whole render reruns. Three stale spools from
  killed renders (14.6 GB) plus the extract cache had eaten the headroom. Rule: `df` ≥ 30 GB free before a full;
  killing a render includes deleting its `hf-render-*` dir the same minute; a failure report says what was LOST first.
- **Capture rate on this box is 9–12 fps at 2 workers, content-independent (measured 2026-09-09 from the log
  checkpoints):** a 623 s / 18690-frame timeline takes ~31 min capture + ~4 min encode. The presenter-circle layers
  cost nothing measurable. ETAs come from the log checkpoint fps, never from a window that includes the 4-min extract
  phase (that mistake produced a 58-min ETA for a 35-min render).

## 2026-08-30 — the ebook CTA is a channel asset + a must-keep contract (owner order, ep4 rewire kickoff)

1. **The CTA was never in the pipeline.** ep2's Paul CTA was spliced into the finished mp4 by the
   owner outside the repo (LEARNINGS 08-29: located by cross-correlation), ep5/ep6 shipped with
   none, and the clip itself lived only in `Videos\storm-insert-work` — unfindable from the repo.
   Now: `assets/cta/paul-storm-ready-v4c.mp4` (tracked; `.gitignore` negation — the only mp4 in
   git), transcript + README beside it, `config.yaml channel.cta` as the single source of truth.
2. **Placement is a contract, not taste:** hook > CTA > payoff, start inside 30–40% of runtime,
   scripted tease before / payoff first-sentence after, 1.0s dips, own audio, no chapter boundary,
   first link in the description = the ebook. DESIGN.md "CTA contract"; `sweep_episode.py` fails a
   missing or misplaced CTA; `script-scaling.md` requires a `cta-hinge` loop-table row.
3. **`build_srt.py` only saw `<audio id="ins…">` inserts** — ep6-style `<video id="ins…"
   data-volume="1">` inserts (and the CTA) got no SRT cue. Fixed: video inserts with
   `data-volume="1"` are cued from their `data-srt-label` too.
4. ep4 (El Reno) is the first in-timeline use; the contract is "verified" only once ep4's draft
   shows the CTA landing on the hinge and the sweep passes on it.

## 2026-08-29 — 1440p upload file is HEVC now (owner order, ep2 CTA re-cut session)

1. **`-master-1440p.mp4` is hevc_nvenc p7 cq22 by default** (the `--hevc` recipe + the lanczos
   2560×1440 scale). The h264 cq19/24M upscale shipped ~5 GB for a 28-min episode (ep2 v2:
   4.8 GB, 5m18s at 5.3× realtime); the owner asked why the 2K file was not compressed.
   Measured HEVC 1440p on the same master: 3.5 GB, 16 Mbps, 8m05s at 3.5× realtime.
   Hyperframes capture stays 1080p — nothing upstream changes, only the upscale codec.
2. **Owner-recut episodes arrive with hot audio.** Ep2 v2 from the external editor measured
   −14.24 LUFS but **+0.30 dBTP** (the July master was −1.0). Always re-run the master step
   (gain + alimiter, video copy) on an owner-supplied cut before the 2K upscale, never
   bit-copy its audio.
3. **Locating edits in an owner re-cut: audio cross-correlation, not frame diffs.** A
   re-export changes grain/grading enough that 32×18 frame hashes disagree (~15–18 mean
   diff) even on identical content; 4 s narration windows cross-correlated at 8 kHz gave
   corr ≥0.98 and pinned every cut to 0.1 s (ep2 v2: trims 2.4 s @0:21, 3.2 s @5:45,
   CTA +15.0 s @8:26, trim 2.2 s after). Map SRT + chapters piecewise through that table and
   split any cue that straddles the inserted segment.

## 2026-08-24 — 1440p upload tier + NVENC-first for mp4 surgery (owner orders, ep1 insert session)

1. **1440p is the upload resolution from now on (owner order).** YouTube assigns bitrate tiers
   by resolution: a 1080p upload gets the ~2.5–4 Mbps VP9 tier, the SAME content uploaded at
   2560×1440 gets ~9–20 Mbps — and viewers watching "1080p" on a 1440p upload are served the
   better-fed stream. `master_deliverables.py` now emits `-master-1440p.mp4` by default
   (h264_nvenc p5 cq19 24M, lanczos upscale from the finished master, audio bit-copied;
   `--no-2k` skips). Hyperframes capture stays 1080p — comps are authored in 1080 coordinates,
   sources are 1080p, and native 1440p capture would ~2.25x the render time for zero real detail.
2. **mp4 surgery on finished renders = h264_nvenc FIRST, never libx264 (measured 2026-08-24).**
   Ep1 15s-insert job on the 17-min master: h264_nvenc p5 cq19 ≈ 7 min; libx264 preset slow
   crf16 was on pace for ~90 min (killed at 0.2x realtime). At 14–16 Mbps consumer-master
   bitrates the quality difference does not survive YouTube's transcode. The PATH ffmpeg
   (Gyan 8.1.1) has working NVENC on this box — same build caveat as the `--hevc` step.
3. **Frame-accurate insert/splice recipe (proven on ep1):** find the true cut with
   `select='gt(scene,0.25)',showinfo` + eyeball extracted frames; single-pass filter_complex
   trim/concat from the ORIGINALS (never a second generation from an intermediate); verify
   splice frames + duration on the output; shift SRT cues and chapter timestamps by the net
   insert-minus-removed delta.

## ep6 ship (2026-08-23) — hyperframes 0.8.x, the hidden-console chain, and a preflight bug
- **hyperframes 0.8.x opens a visible Windows Terminal tab per ffprobe/ffmpeg spawn on this
  box; 0.7.109 does not.** Measured with a process watcher during a hidden demo render: every
  `ffprobe.exe`/`ffmpeg.exe` child of the 0.8.10 render node got its own `conhost.exe` (a new
  console) and `OpenConsole.exe` (a Windows Terminal tab) appeared at the same instants — with
  the render launched through `run_hidden.vbs` exactly like the 0.7.109 renders that show
  nothing. Owner saw "lots of CMDs, 4 at a time". 0.8.10 spawns its ffmpeg/ffprobe children with
  different flags than 0.7.109 (eight `windowsHide:true` sites vs two, new stdio shapes) and
  under node 24's libuv those allocate a fresh console. The telemetry opt-out
  (`HYPERFRAMES_NO_TELEMETRY=1` / `DO_NOT_TRACK=1`) was a red herring — one detached `node -e
  fetch` per run, not the tab source; the env stays set (harmless) but is not the fix.
  **Decision (owner):** ep6 full render on 0.7.109 with the explicit, logged override
  `RENDER_PIN_STALE_OK=1` (render_preflight.py prints `[OVERRIDE]`); pin stays 0.7.109 until an
  upstream version spawns ffmpeg hidden. The 0.8.10 demo render itself PASSED (4m08s, mp4 on
  disk) — the blocker is the windows, not the output. Kill rule: stop the TASK and kill its
  process TREE from the task's root pid; `*hyperframes*`/`*pin_ritual*` command-line matches also
  hit this session's own bash tool shells (and other sessions') — done twice, never again.
- **render.cmd ran preflight BEFORE its own `set HYPERFRAMES_FF*_PATH` lines** → media_budget.py
  measured the slow PATH ffprobe and refused the full render (marker 3). Reordered 2026-08-23:
  env first, then preflight. The draft path had passed only because the PATH spawn happened to be
  under the threshold that day.
- **16 GB is not "room for everything".** frame composites (80 videos in one page) +
  overlap_check + a demo render + faster-whisper concurrently → `mkl_malloc`, `uv_spawn EAGAIN`,
  "Unable to capture screenshot" at frame 390. One browser-heavy job at a time; check
  `FreePhysicalMemory` before launching (2.5 GB free → `RENDER_WORKERS=2`, 7.5 GB → 3).
  Separately: the faster-whisper `small.en` cache on this box is corrupt (`mkl_malloc` regardless
  of RAM) — use `base.en` int8.
- **Subagent briefs must forbid `cd`.** Two Explore agents issued `cd`-prefixed Bash and produced
  8+ permission prompts on the owner's screen in auto mode. Prefer Grep/Read in the main session;
  any subagent with Bash gets "never cd; absolute paths only" in the brief.
- **overlap_check v2 must `page.close()` the index page before staging comps** — the episode page
  holds ~80 videos; keeping it open while staging 14 comps crashed the renderer ("Target
  crashed"). Fixed in `scripts/overlap_check.mjs`.
- **Gate noise to expect on a finished episode:** `sweep_episode.py` FAILs on src-less `<section>`
  gradients (`?` rows: same-track overlap, adjacent duplicate, asset reuse, media exists) and on
  stills >6s that the lint pacing report already lists; lint is the hard gate. `verify_render`
  exempts black and freeze only inside declared blackout sections and the CTA dips (silence also in
  holds and the CTA body); a dark card that sits still anywhere else, holds included, is a real defect.
- **Credits need provenance rows for EVERY still.** The seven owner-supplied Wikimedia stills
  (charity-web-c*, hsdrrs-web-c*) had no provenance row; licence/author were pulled from the
  Commons API and the files matched to the Commons thumbnails by a subagent before writing the
  CC-BY attribution block (`media/provenance-wikimedia-stills.csv`). Four of the six used are
  CC BY / CC BY-SA — attribution is mandatory, not courtesy.

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
- **Rules now in DESIGN.md "On-screen text rules"**: zone occupancy, one fact one instance, no
  decorative eyebrows, narration order/wording, glass under any text over footage, small text
  never alone (BFMG). Encoded because the same four habits shipped in v1 AND v2.
- **Pre-render frame composites without a render:** a one-shot playwright script can hide every
  `[data-start]` element outside T, seek videos (`currentTime`), inject the comp template into
  its host div and seek both timelines — ~5s per frame, faithful enough for layout QC at every
  owner-flagged timestamp. Scratch-space only (tripwire: it reads, never authors).
- **"Source ends early" — check what the SOURCE is before saying so (corrected 2026-08-23):**
  ins-hodges "cut before finishing" was first answered "the C-SPAN pull ends at 7.44s, nothing to
  extend". Wrong: the 7.44s file was OUR pull; the source is the local 39-minute C-SPAN hearing
  (`media/audio-assert/ins06_house_testimony.mp4`, transcript alongside). Re-cut to the sentence
  end (8.85s) and retimed everything after it by +1.55s. Never call a pull "the source".

## No visible windows, ever (owner 2026-08-21)
- schtasks interactive tasks pop a cmd window on the desktop. ALL scheduled/background
  commands run through `scripts/run_hidden.vbs` (wscript, window style 0 — no flash):
  `/tr "wscript.exe <abs>\scripts\run_hidden.vbs cmd.exe /c <abs>\scripts\render.cmd <slug> <mode>"`.
  Never a bare `cmd /c` task action, never foreground `cmd //c` runs of render.cmd either.
- render.cmd preflight also refuses when ≥3 heavy processes (e.g. leftover headless chrome
  from QC runs) are alive — exit 2 with marker written but log untouched; kill QC browsers
  first, then relaunch.

## Audio levels + media budget hardening (ep6, 2026-08-17)
- **Insert audibility is a FILE problem, not an attr problem.** NPR hook insert sat at
  data-volume 1.0 and was still 6.8 dB under narration — the source wav was quiet.
  Gain-normalize insert FILES to the narration median (measure with volumedetect) before the
  mixdown gate. `alimiter` boosts by default (`level=1`); pass `level=0` or check the result —
  it overshot two inserts +5 dB before correction.
- **`scripts/audio_levels.py` is the gate for this** (run before every mixdown build):
  effective dB = file mean_volume + 20·log10(data-volume); narration median is the reference;
  inserts must land ±2.5 dB of it; music beds fail if >30 dB under; beds warn when competing
  with voice. Catches the ep6 NPR defect and the ep6-v1 "score at 0.08 = silent" defect.
- **`optimize_clips.py` now escalates crf (23→27→31) until under the 150 MB media budget and
  PRESERVES audio** (aac copy-encode; silent track muxed for mute clips). The old `-an` pass
  forced a 15-clip re-mux ritual + 36-clip silent-track patch every optimize run — retired.
  Measured ep6: 51 clips crf23 = 194 MB, crf27 = 143 MB; crf27 invisible under archival grain.
  CAVEAT (ep1 session, 2026-08-24 merge): optimize_clips re-encodes from `media/_orig/`
  backups, so a rerun reverts any per-file gain fix applied after a previous pass —
  audio_levels.py catches this.

## 2026-08-16 — ep6 render-failure ledger (3 compile failures, each root-caused)

A. **Animated GIFs kill the compile — never mount a .gif.** hyperframes transcodes every
   GIF at compile with a hardcoded 300s timeout; a 1.6 MB 24-frame radar GIF blew it
   (fail #1). Convert before wiring: single-frame GIF → PNG (`-frames:v 1`), animated GIF
   → mp4. Two of ep6's three "animated" GIFs were actually single-frame — probe
   `nb_frames` first.

B. **Every mounted video needs an audio stream in hyperframes ≥0.7.109 — even muted
   b-roll can be registered as an audio slot.** Fail #3 was `kb-radarloop-audio`: a
   `-an` mp4 I created got an audio reference and compile threw
   `ASSET_MEDIA_TYPE_MISMATCH (expected: audio)`. The CLI does NOT name the culprit —
   found it by temporarily instrumenting `mismatches.push` in the npx-cached cli.js
   (revert after). Fix: mux silence — `-f lavfi -i anullsrc=r=48000:cl=stereo -shortest
   -c:v copy -c:a aac`. (SUPERSEDED 2026-08-17: `optimize_clips.py` no longer strips
   audio — it preserves the source track and muxes silence into mute clips itself. The
   re-mux ritual is retired; the anullsrc recipe stays useful for one-off assets.)

C. **Audio slots longer than their file are silently truncated (compile WARN, not fail)
   — read the WARNs of a FAILED render, they're real defects.** Fail #2's log exposed 5
   beds shorter than their wired windows (worst: 33.5s drone on a 345.4s slot = 5min of
   missing bed that lint/sweep never see). Fix: loop-extend the file to the wired length
   (`-stream_loop N -t <dur>` + 2.5s afade out), or correct data-duration to the true
   file length when the shortfall is a natural tail.

D. **schtasks tasks do NOT start on battery by default** — a /run leaves them "Queued"
   forever. After /create, always:
   `Set-ScheduledTask -Settings (New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries
   -DontStopIfGoingOnBatteries)`. Battery also power-throttles extract/encode — plug in
   for renders.

E. **Clip windows must never exceed real clip length** (draft-blocking freeze class):
   7 ep6 clips were wired longer than their footage (worst +4.8s). Detector: ffprobe
   every `<video>` src vs its data-duration. Fixes by size: big overshoot → re-extract
   longer from the source reel (per-segment cropdetect again); small (<1s) → setpts
   speed-stretch ≤10% (+ atempo on audible clips).

## 2026-08-15 — ep6 owner rules + broadcast-geometry gotchas (later same day)

A. **Owner-gate style change (owner 2026-08-15, supersedes per-insert one-message-each):
   batch ALL owner approval asks into ONE message, as EARLY as possible.** Scattered
   mid-run checkpoints buried in summaries don't reliably reach him and become "probable
   failure or escalation later." A true blocker = STOP and ask plainly; everything else gets
   decided by the editor and reported. Asking twice for something already confirmed is a
   defect. (He flagged the ep6 insert slate "go ahead" under this rule.)
B. **The hook must contain ZERO muted/mediocre elements (owner 2026-08-15).** Every hook
   beat is mid-action WITH audio — natural wind/water, reporter, 911/dispatch, or narrator.
   A silent still in the hook is a bug (ep6's breach still at 9.0-14.1s was replaced with
   surge-water video carrying its own live audio). A designed dead-silence void beat remains
   allowed — that's an audio EVENT, not a mute.
C. **Video-range black is Y=16, not 0.** A pillarbox/blanking detector thresholded at
   "luma < 4" passes limited-range black bars. This exact miss made two sessions measure the
   same WWL reels and reach opposite conclusions (pillarboxed vs clean). Threshold ≤17, or
   use cropdetect.
D. **Broadcast compilation reels have PER-SEGMENT geometry — run cropdetect per cut window,
   never one blanket crop per reel.** The WWL aug28-31 reels are 1280x720 progressive
   carriers with 4:3 content whose active rect varies segment to segment (w 938-974,
   x 152-174, some with top blanking). One measured crop applied reel-wide leaves 10-20px
   black slivers on other segments. Recipe: cropdetect on the exact source window → inset
   ~6px → crop to 16:9 inside the active rect (house style, matches the DVIDS recipe) →
   scale 1920x1080. Then verify numerically with 12px edge strips (Y>17) AND one eyeball
   frame.

## 2026-08-15 — ep6 TTS + sourcing (measured surprises)

1. **Probe-TTS can undershoot the delivered pace by 10+ wpm.** ep6 probes measured a 137.5
   blend; the 46-segment manifest ground truth came out 149.1 wpm (ep1's 153.5 was the better
   prior). The probe segments were unrepresentatively slow-styled. Budget scripts on the
   manifest wpm of the PREVIOUS episode, then verify against the new manifest after the first
   full TTS run and expand/trim THEN — the probe only catches gross errors.
2. **QC gate that caught a real gap: diff whisper-heard words.json against the source .txt per
   segment** (normalize digits + number-words + homophones like Corps/core; flag <0.90
   similarity or >8% word-count drift). BUT verify a flag before re-synthesizing: whisper
   small.en deterministically swallowed a whole mid-file sentence (a5-s4, 6s of clean audio
   heard as one token) while the AUDIO was complete — chunk-level transcription of
   `audio/_segments/*.wav` + the concat.txt order proves which side is broken. Fix for a bad
   words.json: re-transcribe per chunk and offset by cumulative ffprobe durations
   (deterministic, exact) — do NOT re-run TTS for a whisper mishearing.
3. **tts_clone.py caches sentence chunks in `audio/_segments/` ("exists, skip").** Sidelining a
   segment's output wav does NOT force re-synthesis — the concat rebuilds byte-identical audio
   from cached chunks. To truly regenerate, clear that segment's chunk wavs too. (Also means
   text edits within a segment re-synthesize only changed sentences — cheap.)
4. **pocket-TTS intermittently dies at CUDA init/clone with a native crash** (no traceback,
   ~1 in 8 segments on the GTX 1650, same input passes on rerun). `tts_episode.py` now does one
   loud `[FALLBACK]`-logged retry per segment and hard-fails on a second consecutive failure.
5. **DVIDS image IDs are a single global sequential counter** — numerically adjacent IDs are
   unrelated uploads; always verify each image's title page. DVIDS search/NARA REST are
   JS/auth-gated for scripts; the direct CDN pattern
   `d1ldvf68ux039x.cloudfront.net/thumbs/photos/{bucket}/{id}/2000w_q95.jpg` works headless.
6. **schtasks under Git Bash needs `MSYS2_ARG_CONV_EXCL='*'`** or `/Create`/`/Run` get mangled
   into paths.
7. **Scene picking from long reels: contact sheets FIRST, never per-frame agent probing (owner
   correction 2026-08-15).** An agent "watching" a reel by extracting one frame at a time is a
   blind person borrowing eyes one glance at a time. The pipeline is: PySceneDetect CSV (already
   the standing rule) → deterministic script renders labeled contact-sheet grids (~30 scene
   thumbnails per image, scene number + timestamp burned in) → judgment reads the SHEETS and
   tags scene numbers per beat → one ffmpeg batch extracts the tags. Code does everything
   deterministic; eyes only choose.

## Full-render stability on this box (ep5 v5c, two attempts, 2026-08-14)
- **Close studios/headless browsers before a full render.** Attempt 1 died at frame 29553
  (capture page hung 4+ min, then Page.captureScreenshot protocol error) with 2 studio servers +
  8 chrome-headless shells resident. Attempt 2, same comp, clean box: completed. Free-RAM dipped
  to 0.4GB mid-render and survived — contention, not the comp, is the killer.
- **No resume exists** (0.7.81): captured frames stream to the encoder and are deleted; a crashed
  run leaves nothing reusable. Budget a full restart into any crash.
- **Baseline speed: ~600-900 frames/min at 1080p30, 2 workers** (0.3-0.5x realtime) — matches
  ep2's 75-min/28-min history. 3000fpm/1.1x-realtime expectations don't hold on this box.
- **Delete `render_*_done.marker` BEFORE relaunching a same-name render** — a stale marker from
  the failed attempt made the watcher report the new run dead (false "exit=1").
- **schtasks wrappers: never bare `python3`** — cmd resolves it to the Microsoft Store stub
  (exit 9009). Use the full `...\Python312\python.exe` path.
- **Harness reaping applies to ALL long background jobs, not just renders** — a 10-min master
  build got killed mid-measure. Anything over ~2 min goes schtasks + done-marker + Monitor.

## HF studio (`hyperframes preview`) — capabilities and traps (ep5 v5c, 2026-08-14)
- **Studio cannot preview a full media-heavy episode.** Opening the 32-min comp fired 2,200+
  media requests at once — canvas stays black, audio never starts, node server crawls. For an
  audio/hook check, build a trimmed scaffold comp instead (junction media/audio, subtree-filter
  index to the window, clamp root data-duration).
- **Runtime comp length = max(element windows, LAST GSAP TWEEN POSITION)** — data-duration alone
  doesn't clamp playback. Trimming a comp means trimming the script's tween/kb positions too.
- **`data-composition-id` is a contract with the timeline JS** — renaming it breaks the runtime
  (`StaticGuard: Timeline registered as X but no element has data-composition-id=X`).
- **Studio MUTATES index.html** (stamps `data-hf-id` on every element). Harmless to renders, but
  any script matching tag shapes must not assume attribute order (build_srt.py fixed 2026-08-14).
  Diff index.html after any studio session before trusting downstream tooling.
- **Studio realtime playback jitters video under a transform tween** (per-tick video seeks) —
  looks like violent shake; the seek-by-frame RENDER is clean. Verify motion complaints against
  render frames (tblend diff series: shake = sawtooth; smooth = flat bands) before "fixing".

## Owner answer standards (transcript sweep, 2026-08-13)
- A "what's your math / on what basis" question gets the actual logic and data, answered FIRST,
  before any pivot to fixes. Padded defensive estimates read as lying — quote compute-real time.
- Anything that went wrong twice gets a process RCA (what gate should have caught it, why it
  didn't), and the fix lands in the durable docs the same session — corrections that live only
  in chat evaporate.
- "News" (or any single named source) is one of ten thousand — never over-index on a source
  because the owner mentioned it once.
- Same-cut reuse: a specific short cut never repeats in a tight window; different in/out points
  of a longer reel are different cuts. The sweep family gate encodes this — keep it calibrated.

## Audio mixdown as a pre-render gate (ep5 v5, 2026-08-13)
Build the full audio mix from index.html (atrim+adelay+volume+amix, normalize=0) and scan 30s
windows with volumedetect BEFORE rendering. Caught: kick hit (vol 0.6) stacking with narration
start at an act boundary = 0dB clip. Hits under speech need ~0.4. Target: mix mean ≈ -19,
window peaks ≤ -1.5. Also: sparse-keyframe warnings in the render log (dvbhawk-helipov,
calfire-itf-willhappenagain) cause freezes — re-encode with -g 30 before the next full render.

## Music policy update (owner order 2026-08-13, supersedes "never downloaded music")
Owner-provided Pixabay downloads (assets/sfx/owner-2026-08-13/) and DeAPI-generated tracks are
ALLOWED as music/SFX. Still forbidden: anything ripped from YouTube/unlicensed. DeAPI recipe:
POST /api/v2/audio/music (multipart; model AceStep_1_5_Turbo, guidance_scale exactly 1,
inference_steps exactly 8, lyrics "[Instrumental]", format mp3, max 300s) — poll
GET /api/v2/jobs/{request_id} (NOT /requests/ — that 404s). ~$0.0009 per 60s. Generated tracks
pad ~3s of tail silence — trim/fade before mounting. Keys in repo-root .env (gitignored).

## Sourcing doctrine for future episodes (owner, ep5 review, 2026-08-13)
ep5 mounted 142 cuts that traced to only ~30 real source acquisitions — 5-6 reels re-sliced.
Owner: "30 sources should be 60. The clips are there." Count SOURCES, not cuts; and count
ASSERTION assets specifically (broadcast pulls, day-after newspapers, official audio, presser
clips, survivor clips, before/after stills) — third-party proof that the thing happened beats
another angle of the same b-roll. Re-slicing a reel is editing, not sourcing.

## The doctor rule — known-below-spec = STOP, never render (owner, ep5 v4 RCA, 2026-08-13)
v4 shipped a music layer I knew was below the ordered spec ("Hybrid C") — flagged it in my own
park summary and rendered anyway. Owner burned a review cycle discovering what I already knew.
Standing rule: the moment a deliverable is known below spec, STOP before the render, state
exactly what is broken, give options, wait. A render on a known defect wastes GPU hours AND the
owner's review hours. Corollary: verification gates check STRUCTURE; before any render also do
an EXPERIENCE pass — listen to the full audio mixdown, watch the hook, spot-watch 3 random
minutes. A green suite on an unwatchable artifact is a failed QC.

## Owner pivot 2026-08-12 — cadence, sourcing, SFX, durable references

- **Cadence anxiety retired:** video beats up to 12-15s when genuinely matched; stills 3-6s MAX
  with motion (sweep now enforces 6s, was 12s); prefer video everywhere. Claim-risk pulls >12-15s
  need narration over them; transcribe news clips before cutting.
- **SFX is default-ON now** (base tone + peak swells, library/ffmpeg-synth only) — ep5 v2 shipped
  with a single wind bed the owner heard as "buzzing"; a low-volume steady loop under silence
  reads as a defect, not atmosphere. Design per scene, verify post-render.
- **Docs must not cite episode paths** — episode folders get deleted after publish. Shipped
  patterns get COPIED into `references/editing-patterns/` the same session ("you want it to be
  gone with the wind?").
- **Docs drift is a real defect class:** "still ≤12s" survived two owner cadence corrections
  ("will your grandfather come and revise this?"). Any editorial rule change sweeps CLAUDE.md,
  DESIGN.md, LEARNINGS.md AND the gate scripts in the same session.
- **Graphics exits need ~1s land time** after the last beat — v2 cut scenes one or two frames
  after motion ended, repeatedly ("one time is okay... three and four and five times?").
- **PySceneDetect** (scenedetect.com) approved for splitting long sources into scene cuts —
  validate on this box before first use; cheaper than agent OCR passes.

## Harness background tasks get reaped — long renders need schtasks (measured ep5, 2026-08-06)

Two draft renders launched via the harness's background Bash died mid-capture (41% and 33%)
when the harness killed the task — the CHILD TREE dies too, a few minutes later (the log
keeps heartbeating briefly, which reads as "survived" and isn't). `Start-Process` was already
known-fatal (ep3 attempt 11). The reliable launcher on this box is a one-shot **Windows
scheduled task**: `schtasks /create /tn ep5draft /tr "cmd /c cd /d <worktree> &&
scripts\render.cmd <slug> draft" /sc once /st 23:59 /f && schtasks /run /tn ep5draft` —
fully detached, survives the session. Watch it with a log-mtime stall monitor (>10 min
silent = dead), never with a process-name count (MCP daemons match loose filters).

## optimize_clips.py strips audio and ignores bitrate (measured ep5, 2026-08-06)

Two silent failure modes in one script, both hit on ep5:
- **`-an` is unconditional** — it stripped the audio track from all 4 owner-gated INSERT
  clips (the whole point of an insert is its audio). Nothing warned. Restored from
  `media/_orig/` with `-c:a aac`. Rule: after ANY optimize pass, ffprobe the insert clips
  for an audio stream before rendering. (2026-08-17: optimize_clips.py itself now preserves
  audio + muxes silence for mute clips — see "Audio levels + media budget hardening". The
  ffprobe-before-render rule stands for any ad-hoc batch.)
  **RECURRED on ep5 v3 (2026-08-12):** an ad-hoc media-budget crf pass re-encoded every
  mounted mp4 >900KB with `-an` and stripped ins-mckay again; render failed loud at
  `audio_processing_failed` (hyperframes' extractAudioFromVideo, stage "extract", found no
  audio stream — that error code means AN AUDIBLE VIDEO ELEMENT, not a corrupt file). The
  rule is not about optimize_clips.py — it is about `-an` in ANY batch: exclude every
  element mounted un-muted / data-has-audio from the batch, and ffprobe all audible
  elements for an audio stream as the last step before any render.
  (2026-08-17: optimize_clips.py itself now preserves audio + muxes silence for mute
  clips — see "Audio levels + media budget hardening". The any-ad-hoc-batch rule stands.)
  **Corollary (ep5 v4, 2026-08-12): a "lost" source is probably in `media/_orig/`.**
  Two audio-stripped sources triggered a re-download hunt (Wayback CDX + Brightcove id
  spelunking for a Gannett CDN mp4) while byte-identical audio-bearing originals sat in
  `media/_orig/` the whole time — optimize passes MOVE originals there. Check `_orig/`
  (and `_orig_media/`) before any re-download. Bonus fact recovered anyway: the dozer-911
  mp4 URL is `media.gannett-cdn.com/28911775001/28911775001_5851158634001_5851141890001.mp4`
  (still live; provenance.csv row elided it with `...`— never elide URLs in provenance).
- **It only checks resolution and window-length, not bitrate.** ffmpeg scene cuts made with
  stream-copy keep the source's 15-19 Mbps, so 78 within-spec clips still totalled 645 MB
  against the 150 MB decode budget. Fix: re-encode cuts at libx264 crf 23-27 when cutting
  (~0.5 MB/s lands the budget); crf 27-32 passes cost little on graded b-roll.

## Duplicate element ids render BLACK — and no gate caught it (measured ep5, 2026-08-06)

Two `<video>` windows shared `id="vx-carrwaterb2"` (a copy-paste slip during the retention
re-cut). hyperframes keys frame placement by element id, so the FIRST window (581.9s, 8s)
rendered **pure black** while every static gate passed — sweep, lint, blank_scan and
graphics_qc all read attributes, none checks id uniqueness. Found only by post-render
`verify_render.sh` blackdetect + eyeballing the frame. **Check before every render:**
`grep -o ' id="[^"]*"' index.html | sort | uniq -d` must print nothing. (Candidate for a
sweep_episode.py check — mechanical, must-never-forget.)

## 2026-08-05 — ep5 kickoff: the retention lattice + script fact-QC layer (owner orders, all standing from ep5 on)

**New standing process (each has its full text where noted):**
1. **Retention lattice — `references/script-scaling.md` (NEW, read before writing any script).**
   A 10/10 short script scores on its *cadences*, not length; runtime scales by ADDING 3–6 min
   self-similar acts, never by stretching beats. Per-minute invariants (rehook 45–60s, micro-loop
   30–45s, info beat 2–3s on graphics, pacing wave, loop-table plant/pay). Owner: keep it
   **text-only — no JSON, no schema, zero code complexity**; "spice" = the clarifying footnote/
   relatable example (salt, not filler; 70–80% info at 35 min). Orchestrator mode for very long
   scripts: orchestrator writes ALL act briefs + loop table first, one writer agent per act,
   orchestrator re-walks the seams itself.
2. **Script fact-QC layer (pre-TTS, zero cost — owner order).** Pass 1: in-session eyeball of
   every number/name/date/distance INCLUDING arithmetic (ep5 pass 1 caught 9 bugs — among them a
   106→105 day-gap math error and a wrong 100-mi distance). Pass 2: verification agents close
   every `[verify]` marker → CONFIRMED / CORRECTED / CUT (conditional-fact rule: drop, never
   soften). TTS does not run with open markers.
3. **Insert-transcription rule (owner order):** every audio-carrying insert is transcribed in
   full (faster-whisper) BEFORE cut selection; the cut is chosen at the transcript's
   action/emotion peak; excerpt + transcript logged in edit_script + provenance.
4. **Hook: NO black start (owner order).** Frame one is mid-action — the episode's defining shot
   already moving, anchor audio already mid-transmission. The 2–3s VOID survives only as the
   hook's END punctuation. (DESIGN.md hook contract amended.)
5. **Language: 4th-grader readable (owner).** Short words, concrete pictures; emotion from facts
   and rhythm, never vocabulary. Matches the shipped eps' register; TTS syncs cleaner.
6. **Real human portraits (owner):** show the real faces briefly — per-person licensing verdicts
   first; ≤4–5s dwell, once, then symbolic; never a child victim's likeness.

**Measured / sourced this session:**
7. **Probe-TTS: punchy prose runs SLOWER.** Long-sentence segment 158 wpm, short-sentence segment
   139 wpm, blended ≈145. Budget words at the measured blend of the episode's actual style —
   the single planning figure (158) over-budgets a punchy script by ~9%.
8. **Licensing (Carr/Camp):** CAL FIRE firenado heli clip = USE-WITH-CREDIT (CA state-works PD
   doctrine; AB 2880 died 2016; source Storyful's CAL FIRE-credited copy, not network versions).
   911/dispatch recordings CPRA-released = CLEAR-TO-USE from the original holder. Raw
   Broadcastify scanner rips = HELD (no license path). Camp Fire bystander evacuation clips +
   sheriff bodycam = strike-class (chaser-equivalent), network-aired re-cuts only.
9. **When an aggregate stat is uncited, compute it from primary records ourselves** (ep5: the widely-cited
   "70 of 84 died at home" figure isn't stated anywhere in the DA report — our own tally of its
   84 per-victim narratives, agent read, judgment not regex: 71 at/just outside home, 10 fleeing,
   15 mobility-limited). Verification + net-info-gain in one.
10. **Subagent gotcha:** general-purpose research agents that spawn their OWN sub-agents return
    placeholder "waiting for reports" results (nested subagents never report back). Brief
    workers to do the work THEMSELVES; a status-shaped final message = re-dispatch immediately.

## 2026-08-02 — CHECKPOINT: revert to the ep2 method (owner order)

**What happened:** ep1 (9/10) and ep2 (9/10) were hand-authored — the model read word
timestamps and made every cut as an editorial judgment, typed directly into index.html.
ep3 sessions replaced that with generators (`build_ep3.py` 942 lines, `gen_misc_comps.py`,
`gen_panel_comps.py`, `gen_track_comps.py` — ~2,700 lines emitting episode HTML from shot
tables/templates). Output rhythm went metronomic → owner rated ep3 v2 2/10, ep4 (which
inherited the branch + an injection pattern, `build_picture.py`/`inject_audio_hook.py`)
worse. Quality curve tracked generator adoption exactly.

**Why the existing rule failed:** (1) "AI-first, code-second" rule was written 2026-07-29 —
mid-drift, same days build_ep3.py was written — and the generators stayed in the tree as
precedent; (2) one ep3 session read docs from a stale checkout and never saw the rule;
(3) the storm-episode skill carried no authorship rule at all.

**The fix (this PR):** generators + per-episode .cmd forks deleted; TRIPWIRE added to
CLAUDE.md HARD RULE and to the storm-episode skill's preflight; committed junk purged
(.qc-tmp, .consumed, logs, __pycache__, SESSION_LEDGER, plan docs) + .gitignore extended.
ep2 content verified byte-identical between origin/claude/ep2-ship (ff4cac5) and main —
no content revert needed; the revert unit was the PROCESS, not the shipped episodes.

**Kept from the ep3/ep4 era (explicitly, owner-approved):** research learnings
(competitor-plagiarism rule, PD-by-age sourcing, per-cut frame verification), all READ-only
QC checkers (sweep_episode, blank_scan, beat_density, graphics_qc, lint_timeline,
media_budget, render_preflight), render-ops knowledge (workers pin, protocol timeouts,
render-is-last-step), DESIGN.md graphics anatomy + hook contract + chapter blackouts,
master_deliverables/render.cmd infra. ep1–ep3 shipped videos untouched; ep4 will be REDONE
hand-authored from this base, reusing its research + assets.

## Render size + HEVC compression (measured ep3 v5, 2026-07-30)

A full render at `--crf 16 --fps 30` is ~20 Mbps → **5.08 GB for 34m56s**. That is near-lossless
overkill for graphics/stills content. Two ways to ship smaller **without visible quality loss**:

- **Single-pass (no extra step) — the "compress during render" answer:** hyperframes emits
  **H.264 only** for mp4 (vp9 for webm); there is **no HEVC output flag**. But `--crf`, `--fps`,
  and `--video-bitrate` are all render-time flags. Render the final at `--crf 19-20` and author
  at **24 fps** (most YouTube docs) → ~1.5-2 GB H.264 in one pass, no transcode. The slow part is
  frame *capture* (~1.2x realtime, ~98 min here); the encode target is nearly free to change.
- **HEVC (extra shrink) needs a transcode** — hyperframes can't emit it. But the transcode only
  decodes+encodes, it does NOT re-capture frames, so on GPU it is a ~6-min add-on, not a second render.

**NVENC driver gotcha (cost an hour to spot):** the pinned **Gyan.FFmpeg.Shared 8.1.2** build's
`hevc_nvenc` fails with `Driver does not support the required nvenc API version. Required: 13.1
Found: 13.0` (exit -40) — its NVENC needs Nvidia driver 610+. The older **Gyan.FFmpeg.Essentials
8.1.1** build on PATH has a compatible NVENC and works. Use 8.1.1 for NVENC, or update the driver.

Measured HEVC transcode of the −14 LUFS master (5097 MB, `-c:a copy`, audio untouched):

| encoder | speed on this box (GTX 1650) | wall time (35 min vid) | output |
|---|---|---|---|
| `libx265 -preset slow -crf 22` | **0.15x** | **~4 hours** | ~1.2 GB |
| `hevc_nvenc -preset p7 -cq 22` (ffmpeg 8.1.1) | **5.96x** | **~6 min** | **2.19 GB** |

**Takeaway:** software x265 `preset slow` is a non-starter for a review loop (0.15x). GPU
`hevc_nvenc p7 cq22` gives a 2.3x shrink in 6 minutes, visually lossless, audio bit-copied. For
future episodes the cleanest is to render at a higher CRF + 24 fps so the small file falls out of
the render itself; reach for the GPU-HEVC pass only when you want the extra shrink.

## ep3 v3 — stop rendering to find things a script can find (2026-07-29)

- **Owner correction, and the sharpest one of this episode: renders 7, 8 and 9 all died to
  defects I could have found before starting them.** I rendered, thought of a new check,
  killed the render, rendered again. Every check I invented reactively is now a script that
  runs in seconds — `scripts/sweep_episode.py`, `beat_density.py`, `blank_scan.mjs`,
  `clip_report.py`. The rule: **exhaust every static gate, THEN render once.** A render is
  the last step, not a diagnostic tool.
- **You do not need a render to blackdetect.** `blank_scan.mjs` inlines each composition into
  a bare page with gsap, seeks its timeline at 0.25s, and sums the on-screen area of every
  element with computed opacity >= 0.06. A comp that goes empty shows up in seconds. It found
  a real 0.75s hole in g-close between the closing lines and the title card. Exclude the
  background texture (`.drift`) from the ink sum — it is present in every frame by
  construction and would mask exactly the failure being looked for.
- **When the owner gives timestamps against an old cut, MAP THEM YOURSELF.** I asked him to
  re-point 5:48 and 28:04 because the v3 timeline had shifted. That was my job: the v2 draft
  was built from a commit still in the tree, so `git show <sha>:episodes/<slug>/index.html`
  into a temp dir plus the window ledger answers it in one command. Doing that showed his
  5:16 and 5:48 notes were the SAME defect — one 33.4s stock cloud clip covering a whole
  four-minute-mark passage — and that 28:04 was a 0.904-aspect portrait stretched full-frame
  for 163 seconds.
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
- **A blanket `fit="contain"` pillarboxes photos that were already the right shape.** Four
  stills at 1.58-1.75 aspect were running inside blurred bars for nothing. Letterbox on the
  IMAGE's aspect, not the segment's hint — with papers exempt, since cropping a front page
  cuts the text.
- **Retiring a graphic means retiring its generator entry, its `_durations.json` key and the
  file.** Dropping only the mount left `g-panel-lone` authored-but-unmounted, which the
  sweep caught immediately.
- **The `ffprobe deadline with code 0` failure was never a bad asset — the deadline is 120s,
  hardcoded.** hyperframes 0.7.64 wraps its probes in `deadlineAtMs: Date.now() + 12e4` with
  no env override, and the probe it runs at `video_extract` is not the cheap duration read —
  it is `-count_packets`, which walks every packet. Measured on an idle box with the exact
  arguments: worst clip 3.05s, whole 16-clip pass 29.9s. The
  failed render spent 274s inside `video_extract` before a single probe blew 120s, i.e. the
  box was running roughly 40x slower than idle. Cost does NOT track file size — the 57 MB
  transcode probes in 2.0s while a 10 MB lightning clip takes 3.05s — so the "4K asset"
  theory was wrong twice over. The fix is `render_preflight.py` plus an otherwise-idle box.
- **Coverage tools must name their picture tracks.** `clip_report.py` counted every track,
  so nine overlay windows (date card, source chip, quote cards, lower-thirds) papered over
  the black underneath them; the date card alone hid 0.30-14.3s. Whitelist the picture
  tracks, then prove the check can still fail by deleting one still from a scratch copy.
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
- **A substitution pool with no geography will contradict the narration.** Past the reuse
  ceiling, `pick()` drew from a flat spare list and put the Heinz plant in Princeton,
  Indiana under a sentence about Annapolis, Missouri — the far end of the track, three hours
  later. Act-scoped pools first, global spares second. The narration/picture gate found it;
  no human review had.
- **Word-level timings turn "does the picture contradict the voice" into a script.**
  `narration_picture_check.py` reads `audio/<seg>.words.json` and tests what is on screen at
  the instant a year or a town is spoken. Build the place vocabulary from the archive's
  filename convention (`1925_-_<Town>_-_`), not from every capitalised token — the loose
  version called "Where", "Morning" and "Building" towns and buried three real findings in
  thirteen false ones.
**Render (2026-07-27, ep2 full render):**
- Full-quality render died at 74% with `Protocol error: Target closed` after a burst of
  `net::ERR_NETWORK_CHANGED` on the localhost media server — a host network-interface change
  (Wi-Fi/VPN flip) mid-capture kills the Puppeteer browser's media fetches. Environmental, not
  a comp defect (same comp draft-rendered clean). Fix: relaunch with
  `PRODUCER_PUPPETEER_PROTOCOL_TIMEOUT_MS=900000` alongside the nav-timeout var; avoid network
  changes during long renders. A ~28-min comp at standard/30fps ≈ 75+ min capture on this box —
  budget 2h wall-clock when the machine is also running other sessions.
- **Check the hyperframes version before production starts, and read what changed.** Bumped
  0.7.64 -> 0.7.81 on 2026-07-29 (owner order). The upgrade **shortens the ffprobe deadline
  from 120s to 30s** (`Date.now() + 12e4` became `+ 3e4`) — the exact deadline twelve ep3 v3
  renders died on. A newer version can be STRICTER, not just better, so every timing measured
  against the old pin has a 4x smaller margin. `npm view hyperframes version` is one command
  and belongs at the top of a production run, not after a failure. Bumped 0.7.81 -> 0.7.107 on
  2026-08-14 after the ritual: changelog audit (827 commits; relevant = extraction memory
  bounding, hidden-audio excluded from render mix, WebGPU capture fixes; ffprobe 30s deadline
  UNCHANGED, verified in dist) + A/B render of demo-joplin-90 at full quality — identical
  duration/blackdetect, RMS delta 0.006 dB, SSIM 0.997, spot frames clean. No behavior change
  observed; the hidden-audio mix change did not alter loudness on a comp using visible audio tags.
  **Ritual scripted 2026-08-14 (owner: manual refresh was "stupid" — pin rotted 26 versions in
  2 weeks while the warn-only banner fired unheard):** `scripts/pin_ritual.py` runs the whole
  thing (npm view, candidate render of demo-joplin-90, metric diff vs committed
  `pin_baseline.json`, auto-bump on identical metrics, exit 3 + no bump on drift), and
  `render_preflight.py` — now actually invoked by `render.cmd` — hard-blocks FULL renders on a
  stale pin (exit 6) while drafts only warn. npm unreachable never blocks. Baseline mp4 is an
  on-disk cache (`episodes/demo-joplin-90/renders/pin-baseline-<ver>.mp4`); when absent, the
  ritual re-renders the baseline too (metrics-only compare if that ever fails to keep SSIM).
  **Gotcha that cost 40 min:** `npx hyperframes@<uncached-version>` prompts "Ok to proceed?"
  and a detached run hangs on stdin until the timeout — every scripted npx call needs `-y`
  AND `stdin=DEVNULL`. (The schtasks cmd wrappers dodged this by accident; python
  subprocess did not.)
- **A rule with no gate is a suggestion (owner, 2026-07-29).** "Cap every source asset at the
  composition's resolution" was written in CLAUDE.md and violated by seven clips through twelve
  failed renders, because nothing checked it. The counter-question for any rule that keeps
  getting broken is not "say it louder" — it is "what reads the number before the expensive
  step?" `media_budget.py` reads three numbers in three seconds; the renders it replaces cost
  forty minutes each.
- **Keep code headache low (owner, 2026-07-29): if reasoning can do it, do not write a script.**
  Code earns its place when the check is mechanical, repeated, and must never be forgotten —
  deterministic gates, batch transforms, anything guarding money or a long render. Reasoning
  owns taste and context. **The tell for a script that should have been a docs line: it needs a
  hand-tuned stoplist to stop being wrong — that is judgement wearing a regex.** Applied the same
  day to this repo's own new code: `probe_timing.py` deleted (a one-shot diagnostic whose answer
  now lives here — a number already measured is not a tool), and `narration_picture_check.py`
  lost its place check (thirteen false positives to three real ones, propped up by a stoplist of
  words that are not towns) while keeping the era check, which is genuinely mechanical.
- **THE ep3 v3 render RCA, after thirteen failures: process-spawn scanning, not media.**
  Security software on this box scans every process creation, and the cost tracks
  BINARY SIZE, not work done:

  | binary | size | spawn |
  |---|---|---|
  | `cmd /c echo` | tiny, system | 0.063s |
  | `where.exe` | small, signed | 0.172s |
  | `python.exe` | medium | 0.251s |
  | `ffprobe.exe` (Gyan essentials, static) | **97 MB** | **1.165s** |
  | `ffprobe.exe` (Gyan **shared**) | **224 KB** | **0.102s** |

  A render fires roughly 200 ffprobe spawns (21 video windows x ~3 probe types, ~70 audio
  files x 2). At 1.2s each that is ~200s of pure scanning — and the observed `video_extract`
  stage durations were 193s and 204s. When spawns collide the scanner serialises them and one
  probe waits past its deadline, which is the `ffprobe deadline with code 0` failure.
  **Fix: `winget install Gyan.FFmpeg.Shared` and point hyperframes at it with
  `HYPERFRAMES_FFPROBE_PATH` / `HYPERFRAMES_FFMPEG_PATH`** (both render scripts now do).
  Measured on the real probe over all 16 clips: 1.32s each -> 0.40s each, ~263s -> ~80s
  projected per render.

  **Why it took thirteen renders:** every earlier theory was about the MEDIA (a 4K asset,
  contention, worker count, the deadline value). Cutting media 72%, halving workers, and
  changing the deadline 120s->30s each changed NOTHING, and that was the signal — a
  performance fix that moves the needle zero means the model of the problem is wrong. The
  question that cracked it was "how long does ffprobe take when it opens no file at all?"
  (1.4s, versus 0.06s for `cmd`). **When three independent fixes change nothing, stop fixing
  and go measure the thing every attempt has in common.**

## ep3 v3 — the defects no code gate was looking for (2026-07-29)

- **Run `blackdetect` on every render. The picture track can be empty and every static gate will
  still pass.** ep3's segment scheduler advanced by `seg_dur + GAP` but only covered `seg_dur`
  with picture windows, so the 0.75s breath between narration segments had nothing on tracks 1/2.
  `ffmpeg -vf blackdetect=d=0.1:pix_th=0.10` on the draft found **81 black spans, 63 at segment
  boundaries**; sampled frames were pure black. lint_timeline PASSED, graphics_qc PASSED,
  hyperframes check found nothing — because none of them ask "is anything on screen at time t".
  The gate that catches it is a union-coverage sweep of every element carrying
  `data-start`+`data-duration`+`data-track-index`, compared against the comp duration.
  Reference floor: ep2 (shipped) has 2 uncovered gaps, ep1 has 6. Anything in the dozens is a bug.
- **Corollary: a coverage report must read the ELEMENT, not the animation array.** My first pass
  parsed only the ken-burns `KB` array and the sub-composition hosts, and reported 63 gaps *plus*
  16s phantom holes — because `<video>` clips carry their timing on the element itself and never
  appear in KB. Same-shaped bug, opposite direction: it invented gaps that did not exist while
  missing 32 real windows. Enumerate by attribute, never by animation bookkeeping.
- **`blackdetect` false-positives on dark graphics.** Half the flagged spans were title cards on a
  near-black background, correctly rendering. Verdict requires eyeballing a frame from each span
  (dispatch a subagent — never Read frames into the main context). File size is a decent triage
  signal: the truly-black JPEGs were 13KB, the content ones 38–47KB.
- **"ffprobe deadline with code 0" is a size problem, not a corruption problem.** Render #7 died at
  10% of `video_extract` after 141s. All 18 video assets probed clean. The cause was one 365MB
  3840x2160 stock clip feeding 12.9s of a 1080p comp — 10x every other asset. Transcoding it to
  1080p (365MB -> 54MB) is the durable fix; retrying the render is not. Cap source assets at the
  composition's own resolution before wiring them.
- **`hyperframes check` reports `data-end without data-duration` for every `<audio>`/`<video>` in
  a composition whose source contains zero `data-end`.** It is validating a normalized DOM, not the
  source. Verified pre-existing by running `check` against the git-HEAD index.html. It does not
  block `render`. Don't burn a cycle chasing it — but do re-verify it is pre-existing rather than
  assuming, by checking out the prior file and re-running.

## ep3 v3 - second audit round (2026-07-29)
- **Cut rate is an asset-budget decision, not just a taste one.** ep2 (shipped, 7.5/10) holds an
  11.0s median across 136 windows in 28 min. Driving ep3 to a 5.5s median needed ~260 windows in
  35 min - roughly double the assets per minute - and the photo library could not feed it, so
  frames silently repeated 5-12 times. Pick the median from `distinct_assets * 3 / minutes`, then
  design the rhythm inside that budget. Landing at a 6.5s median with 216 windows fit 106 assets
  with zero over the 3-use ceiling.
- **Identify assets by content hash, never by path.** Six newspaper front pages existed
  byte-identical under `media/newspapers/` and `media/photos/`; the reuse lint counted each path
  separately, so one page reached nine on-screen uses under a ceiling of three.
- **Count uses per WINDOW, not per `<img>` tag.** The letterbox treatment emits the same src twice
  (blurred backdrop + foreground), which inflates a naive `grep src=` count by 2x and produces
  false reuse findings. Two of my own audit agents were fooled by exactly this.
- **A "credited" archival face is still a misattribution if no credit renders.** The Signal Corps
  commander who shut Finley down sat under a panel headlined JOHN PARK FINLEY for 32 seconds; the
  edit script said "credited" but no attribution element existed anywhere in the window. If a real
  person's face is on screen under someone else's name, that is a factual error, not a design nit.
- **Check for authored-but-unmounted compositions every build.** Three graphics passed every QC
  gate while being mounted nowhere - including the stat panel for the episode's longest segment,
  which therefore ran 48s with no graphic at all. `authored_ids - mounted_ids` must be empty.
- **A counter must open on its first tick's value.** The path maps shipped the END toll in the DOM
  (490 dead, 4:00 PM) and then animated backwards to 5 dead at 1:14 PM.
- **Narration-cued means EVERY graphic, not just the ones with a cue helper.** The met map fired
  its five labelled blocks in diagram order - four were 5-18s off their spoken word, one directly
  contradicted the voiceover. Hand-authored compositions need the same words.json alignment the
  generated panels get.
- **`ffprobe` on a still image reports ~0.04s.** Any clamp that treats that as a clip duration will
  cut a window into single-frame slivers. Guard duration probes by file extension and fail loud
  when a non-video is typed as a clip.
- **Audit findings need adversarial verification before you act on them.** 81 raw findings became
  54 confirmed - a third were wrong, including several that would have sent me editing correct code.

## ep3 v3 (2026-07-29) — the "check the code, not the frames" rebuild
- **`hyperframes check` (not the deprecated `validate`) is the real static gate.** It caught 19
  errors a frame sweep never would. Run it before every render, not after.
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
- **Quantize the timeline to the decimal grid you print at.** Accumulating `ct += w` in float
  while emitting `{ct:.2f}` makes a window's printed end land 0.01s past the next window's
  printed start — 44 same-track overlap errors. Round every start and duration to 2dp and
  accumulate the rounded values, so end == next start bit-for-bit.
- **A graphic's duration must be DERIVED from its resolved narration cues, never hand-estimated.**
  Panels whose rows are cued off `words.json` slid off screen at the hand-guessed duration while
  later rows were still firing on an off-screen card, and the host window sat empty for the rest
  of the segment. `dur = max(declared, last_cue + tail)`.
- **Clamp every clip window to the clip's own length at BUILD time** (`ffprobe`, cached). This is
  the ep3-v2 frame-coverage failure caught one stage earlier, deterministically, instead of 20
  minutes into a render.
- **Hand-declared beat weights bypass the pacing clamps.** `mixed` segments rescale their weights
  to fill the narration window, which pushed stills to 7.2s and a single clip to 16.4s while
  `MAX_STILL` was 6.5. Any path that produces windows must go through the same splitter.
- **Idle warnings on an overlay panel are not the same defect as idle on a full-frame graphic** —
  the panel sits over a moving photo. But the card's own content still must not sit dead: one
  continuous transform tween spanning the window fixes it and costs nothing.
- **Tooling gotcha:** the Bash tool consumes backslashes in heredoc'd Python even inside a
  quoted `<< 'EOF'`. `"\n"` arrives as a real newline, which silently corrupts source-generating
  scripts. Build literal backslashes with `chr(92)`, and always `ast.parse` the result.
- **Windows CRLF breaks naive line-joining repairs** — read/normalize with explicit
  `.replace(chr(13)+chr(10), chr(10))` before any line-level surgery, and write back as bytes.

## ep3 v2 (2026-07-28)
- **`loop` attribute does NOT survive render**: hyperframes 0.7.64 video extraction ignores `loop`; a looped clip window longer than the source fails the 95% frame-coverage gate ("captured N of expected M frames"). Fix at the asset level: pre-loop the file with `ffmpeg -stream_loop N -i src -t <maxwin+2> -g 30 -keyint_min 30` and keep the filename. Never set `HF_VIDEO_COVERAGE_THRESHOLD=0` — the gate is right, the encode would freeze/blank.
- **Don't run whisper transcription concurrently with a render**: CPU starvation made hyperframes' ffprobe miss its deadline ("[FFmpeg] ffprobe deadline with code 0") during video_extract. Sequence them.
- **tts_ep3v2.cmd chained transcribe stage died silently after TTS DONE** (no marker, no log lines) — give each detached stage its OWN log + exit marker; a chained `goto`-loop .cmd hides which stage failed.
- **StaticGuard boundary rule**: any GSAP fade that ends exactly at a clip-window boundary needs a `tl.set(..., {autoAlpha:0})` hard kill right after the fade, or validate flags stale-visibility risk.
- **`hyperframes snapshot` accepts only one `--at`** — repeated flags silently collapse (and add a stray extra frame); loop one invocation per timestamp for fixchecks.

## 2026-07-27 — ep2 hook rebuild + ship (hook contract now in DESIGN.md)

**Editorial:**
1. **The hook contract (owner rated old hook 0.6/10, demanded 9.8+ "unskipable").** What made
   it 0.6: four undifferentiated clips in 12s, no intelligible speech until 0:22, one silent
   clip, mid-sentence commentary fragments, an orphan audio tail after the emotional line, no
   sonic build. What fixed it: an intelligible ANCHOR line (Spann's live "tornado emergency")
   starting by ~2.5s; every cut lands ON an audio event; a siren spine that builds start→duck→
   swell→die; the insert trimmed to end on its complete emotional statement ("we knew something
   was coming" — nothing after); date/place card in the first second; a dead-silent VOID
   before the narrator enters (2-3s then; **1.5s since the 2026-08-16 blackout table**). Full contract in DESIGN.md — apply from ep3 scene one, don't
   rediscover it.
2. **Dual-scope statistics must be self-disambiguating in publish copy.** 324 (outbreak) vs 316
   (Apr 27 alone) are both correct, but a reviewer read them as a contradiction — a viewer will
   too. Any copy using a scoped figure names the scope in the same sentence.

**Pipeline / tooling (all reproduced):**
3. **`--workers` must be pinned on full renders** — omitted, hyperframes "auto" resolved to 1
   worker on a loaded box (2× slower than the 3-worker draft). Recipe in CLAUDE.md/DESIGN.md
   now pins `--workers 3`.
4. **`render . <file.html>` entry arg is IGNORED by hyperframes 0.7.64** — it silently renders
   the default composition. There is no partial/preview render via entry file; use duration
   overrides or sub-comp renders instead.
5. **Start-Process ArgumentList quoting:** a .cmd path containing spaces must carry embedded
   escaped quotes (`'\"C:\...path with spaces...\.cmd\"'`) — unquoted, cmd.exe silently no-ops
   and no log ever appears.
6. **Harness kills long-running background Bash watchers between turns** — completion watches
   on renders must use the Monitor tool (poll a done-marker every ~120s), and the filter must
   emit on ALL terminal states (complete AND error/fail lines), not just success.
7. **Master pass numbers (ep2):** full-comp mix landed −13.13 LUFS / TP +0.05 (hot). Master =
   `-c:v copy -af volume=-1.05dB -c:a aac -b:a 256k` → −14.19 LUFS / TP −1.01, verified with a
   second loudnorm read. Plain gain beats dynamic loudnorm when input LRA is already tight (3.4).
8. **Shipping while another session holds `.git/index.lock`:** `git worktree add <dir> -b
   <branch> origin/main` succeeds despite the lock (index.lock only guards the main checkout's
   index). Copy changed files in, commit/push/PR/merge from the worktree — the other session's
   checkout and branch are never touched. Note: the auto-commit hook fires inside worktrees too
   (an Edit there self-commits); `git worktree remove` can hit Windows Permission-denied — `mv`
   the dir to trash + `git worktree prune` works.

## 2026-07-26 — ep2 v1 owner review (9/10; every item below is a standing rule now)

**Editorial (owner corrections):**
- **Broadcast variety:** TV/broadcast pulls stay short and MEANINGFUL — never a 12-24s single
  pull; length itself is editor judgment ("4,4,4" was an owner example, not a formula — don't
  hardwire it). Different sources, different cuts, different chapters; never reuse the same
  broadcast cut twice. Grade every broadcast/private-rec clip (unified grade = transformational
  + look-glue); stock/PD exempt.
- **SFX beds must be diegetically motivated and SHORT.** A 136s wind loop over analysis
  narration read to the owner as inexplicable "steady wind"; crickets running under a blackout
  read as "grey sound." Bed enters with the storm beat, leaves when the beat does.
- **Bare static stills >10s = retention risk.** Motion video tolerates 12-15s; a bare still
  doesn't. Split with another visual or overlay an info beat — but never force filler.
- **Insert/AV cuts on sentence boundaries via transcript, always.** 8-14s, complete meaningful
  statement (emotional or informational), never mid-sentence. "80% is the cut; the last 20% is
  knowing what to leave out."
- **Every act's episode outro carries the episode number** (match ep1: "Episode N — Title").
- **Cold-open clips need per-beat volumedetect** — one silent source beat (towercam) muted the
  opening 3.6s of a cuts-on-audio montage.

**Composition contract:**
- **Exit animations must end fully gone** (autoAlpha:0 + overshoot the slide). `x:660` on an
  820px panel left a stuck sliver for ~1s until the host window closed — owner caught it at
  three timestamps. Snapshot host-end−0.5s to verify every panel exit.
- Panel gradients: `box-sizing:border-box`, text starts inside the SOLID zone; every
  text-over-media element gets a dark backing chip.

**Process:**
- **Verify each CUT, not just the source video.** An official CBS upload titled for the April 2011
  Alabama outbreak contained Henryville, IN (March 2012) footage inside its montage — caught only
  because a chyron was legible in a snapshot frame. Rule: before wiring any broadcast cut, extract
  a frame FROM THE CUT and check chyrons/landmarks against the event; title + official channel are
  not provenance for individual shots.

- **Provenance notes are load-bearing at COMPOSE time.** cullman-aftermath.mp4 carried a
  "2017-era footage" warning in provenance.csv and still got wired into a 2011 documentary
  (twice). Rule: before wiring any clip, re-read its provenance row; a "backup only"/era
  mismatch note disqualifies it.
- **Owner meta-principle (from 6 channels):** do NOT pre-constrain the editor-AI with scripts
  and hard-coded rules before it sees the problem. Scripts = deterministic checks only (lint);
  pacing/grading/placement stay AI judgment per-case. "Do not draw lines before AI even sees
  the problem."
- **QC density:** 18 frames on a 28-min video is not a review. Dense sweep ≈ 1 frame / 15-20s
  plus targeted checks on every region you changed.

## 2026-07-26 — ep2 overnight build (tooling gotchas, all reproduced)

- **Snapshot `--timeout` covers ONLY runtime init; page navigation is a separate 10s default**
  that kills media-heavy comps with "Navigation timeout of 10000 ms exceeded". Fix: env var
  `PRODUCER_PAGE_NAVIGATION_TIMEOUT_MS=120000` (found in cli.js `resolveDiagnosticNavigationTimeoutMs`).
  Applies to snapshot AND render — set it on every invocation for big comps.
- **Harness background Bash tasks die at the 120s default timeout / on compaction** — long
  snapshot/render jobs go DETACHED: `Start-Process cmd.exe '/c <ABSOLUTE path>.cmd'` writing a
  log + `done.marker`, polled via wakeups. Relative .cmd path silently no-ops (process spawns,
  script never runs). One npx call per .cmd — a second `call npx` after the first never ran.
- **Snapshot's video-frame extraction can fail per-frame** ("could not be extracted — will appear
  black/stale") while the composition is fine — the RENDER captures live playback and is unaffected.
  Verify suspects by ffmpeg-extracting frames from the source media at the mapped offsets
  (data-start/trim math), not by rerunning snapshot.
- `scripts/tts_episode.py --only` REWRITES manifest.json with only those segments — re-run a full
  pass (existing wavs skip fast) after any `--only` patch. `transcribe_episode.py` skips existing
  words.json — delete stale ones after re-TTS or timings go stale.
- yt-dlp `--print` implies `--simulate` — subtitle downloads silently skip; run without `--print`.
- Subagents can go idle without reporting (2 of 6 tonight) — poll with SendMessage pings; if still
  silent, verify their on-disk output yourself and take over the reporting step.
- `.lt-loc` lower-third relied on text-shadow alone — unreadable over white map graphics; all
  text-over-media cards get a dark backing chip (`background: rgba(5,8,12,0.78)`) from ep2 on.

## 2026-07-26 — draft-proxy render validated (timed on ep1 v3d, 17:17 comp)

`--quality draft --crf 32 --fps 15 --workers 3`: **21m 16s vs 39m 32s** standard (46% faster),
258 MB vs 1775 MB. 1080p at 15fps — quote/graphic text fully readable in extracted frames;
review-quality confirmed by eyeball. Capture dominates render time (fps halving ≈ halves capture;
encode/pipeline overhead is the floor), so don't expect draft to scale below ~half. This is THE
review path per CLAUDE.md; full-quality render only after owner approves the draft.
Monitor gotcha: "render finished" check via `tasklist ... node.exe` is too broad — other node
processes keep it true forever; watch for the log's "Render complete" line instead.

## 2026-07-26 — ep2 design review (owner corrections, all wired into CLAUDE.md/DESIGN.md same session)

1. **Broadcast-clip rehook cadence**: core audience 40–70+ watched these disasters on live TV —
   real broadcast/news/PD/survivor clips every 45–60s as rehooks; stock fills BETWEEN real clips,
   never the reverse. Network clips 3–4s, narrated-over, credited (credit ≠ license, ≠ claim immunity).
2. **Claims-vs-strikes ruling (Oldshue)**: network material = revenue claims (budgeted OK);
   independent chaser/streamer footage = manual strikes (channel-fatal) → NEVER-without-license
   covers streamers too. Disguising a source (grain/crops/short cuts) to dodge Content ID is
   prohibited — structural immunity, not obfuscation. The story can be narrated over our radar
   re-plots + network tower-cam instead of the streamer's frames.
3. **Burned-in radar timestamps: map to narration OR crop out of frame** — cropping now an
   approved alternative to honest-labeling when the clock isn't the story. UTC-vs-local trap stands.
4. **Cold-open montage grammar**: clips enter MID-ACTION (the hit, not wind-up/aftermath), cuts
   land ON the audio event (scream/crash/dispatch line), 911 audio as one scene in the chain.
   Never re-rip clips from competitor videos — trace to original sources (their edit carries
   their Content ID fingerprint + VO bleed); refs are a shot list only.
5. **Conditional-fact rule**: a proposed distinctive fact ships ONLY if verification confirms it
   (e.g. "Wrangler plant never reopened") — drop entirely on failure, never soften into "reportedly".
6. **Runtime**: 13–23 min band is a default, not a cap — owner explicitly ordered 30 min for ep2
   (high-demand topic). Word formula scales: minutes × 0.9 × wpm (see 7).
7. **The "137 wpm" planning figure was WRONG** (caught by ep2 probe): ep1's own audio manifest
   says 2,519 words / 16.4 min = **153.5 wpm delivered**; ep2 probe segments ran 159–168 wpm.
   Plan at ~158 and ALWAYS probe 2 segments before locking script length — provenance ladder in
   action: disk manifest > LEARNINGS claim. (How "137" got recorded is unresolved; possibly an
   earlier script revision's word count divided by a later duration.)

## 2026-07-23 — v3 pre-render multi-agent QC sweep (owner-ordered; caught what 2 shipped versions missed)

A 4-agent Workflow sweep (media-contract / timeline-contract / sync-audit / snapshot-eyeball)
before the v3 render found 10 issues, 3 blockers — **keep this sweep as a standing pre-render
step for every episode**:
1. **`rain-wall-parked-cars.mp4` showed a MALAYSIAN license plate** — shipped in v1 AND v2
   unnoticed. Lesson: vision-verify every inherited/act-dir clip too, not just newly sourced
   ones; foreign tells (plates, signage, architecture) are the #1 stock hazard. Replaced with
   `rain-wall-downpour-generic.mp4` (anonymous pavement closeup). Tainted file kept on disk for
   v2 provenance but must never be re-used.
2. **`data-media-start` on a clip broke snapshot frame extraction** (funnel beat rendered black
   in snapshots though the file was healthy). Robust pattern: pre-trim the segment into its own
   file (`tornado-funnel-hold-4s.mp4`) and drop data-media-start when a beat uses a mid-file window.
3. **CDN GSAP caused 10s navigation timeouts** in validate/snapshot — vendor `gsap.min.js` into
   the episode dir and reference it relatively. Deterministic + faster.
4. Honest-label rule reconfirmed: watch-beat popup must narrate the radar's burned-in clocks
   ("watch 1:30 PM → by 5 PM this appears"), never caption footage with a time it contradicts.
5. Namecards need scrim bars (`display: table; margin: auto` per line — inline-block puts
   name+sub on ONE row; transform-centering fights GSAP y-tweens).
6. Every intentional dead-frame beat gets an explicit track-4 blackout section — an undocumented
   coverage gap is indistinguishable from a bug in review.
7. **SFX bed volumes must compensate for source loudness — never copy the music-bed ducking
   numbers.** First v3 render shipped a completely inaudible SFX layer: sources (rain −29.7dB,
   wind −30.4dB mean) are ~15dB quieter than the ACE music beds (~−14dB), so `volume 0.05-0.14`
   buried them ~-40dB under the mix. Caught only by a differential band-energy check against the
   v2 render (same section, no SFX) — identical spectra = layer silent. Rule: `volumedetect`
   every audio source, set element volume from (target mix level − source mean), and VERIFY the
   layer post-render by differential comparison, not by assuming the keyframes worked.

## 2026-07-23 — RCA: "repeats fixed" claim was FALSE (owner caught it on v2, rated 8.5/10)

**What I claimed:** "repeats gone, cadence fixed." **Reality (deterministic audit of shipped
index.html):** 10 files used 2-3x, 21 non-graphic shots >12s, and the night-rain-lamp SUBJECT
appeared 6 times across 5 *different* files (156s, 180s, 215s, 235s, 528s + window-rain 80s).

**Root causes (all three, compounding):**
1. **Audited by construction, not verification** — I trusted my shot-map ledger, which drifted
   from the actual HTML through later edits. Never re-checked the final file.
2. **Wrong dedup key** — I enforced file-level uniqueness; the viewer perceives subject-level
   identity. Different Pexels files of "street lamp in night rain" are the same shot to a human.
3. **Localized the cadence fix** — applied faster cuts only to beats the owner named, never ran
   a global max-hold pass. One-still-per-beat authoring means every long beat = a long hold.

**Fixes shipped (session-independent — no owner re-teaching needed):**
- `scripts/lint_timeline.py` now FAILS on: file reuse without `data-callback` (max 2 uses),
  any non-graphic visual >12s without `data-hold-ok`, both exempt in the last 90s (summary).
  Ran against v2: 31 findings — it would have blocked the false claim. HARD pre-render gate
  (repo CLAUDE.md step 6).
- DESIGN.md: subject-family dedup rule (dedup what the frame shows, not the filename).
- Meta-rule in CLAUDE.md: never claim an editorial rule fixed from memory — re-run the lint.

**Owner clarifications captured:** recap/outro reuse is fine (exempt zone); more stock/NOAA
variety encouraged; goal = learnings compound so video N needs fewer revisions than video N-1.

## 2026-07-22 — owner review of ep1 v1 (9/10, "best one till date"; ~80% of issues = cadence + repetition)

1. **Cadence is REASONED per clip, never defaulted**: the editor-agent must justify each hold —
   "1.5s stinger or 12s land-the-beat" is an editorial decision per beat; anything >8s needs a
   reason written in the edit script. Overlong offenders in v1: hook porch-swing, cloud shots,
   siren still at 11:05 (14.6s), outro title dwell.
2. **No visual repeats within an episode** (owner caught all three: lamp-post rain ×2,
   rain-window ×2 within 2 min, St John's facade ×2). One reuse allowed ONLY as an intentional
   callback: different crop/grade, >5 min apart, flagged in the edit script.
3. **Sync rule — the frame must not contradict the narration**: "died in the dark" over a
   daylight photo; "Walmart" over a Walgreens aerial; "1:30 PM watch" over a 22:43 UTC radar
   stamp. Named entity / time-of-day / timestamp in VO ⇒ matching visual or a neutral one.
4. **Graphics never idle**: ≤3s from graphic-on-screen to first payoff element (v1 polygon sat
   ~10s). Reveal ON the word (match cut) — owner loved the UNSURVIVABLE match cut, flagged
   CATASTROPHIC landing 5s before its word.
5. **Number reveals**: never pre-reveal in an eyebrow/fine-print (v1 spoiled 161); counter rolls
   fast then dramatically slows into the final number; secondary stat (158) appears AFTER.
6. **Lower-third sub-line readability**: dark-amber italic serif fails on busy ground — bump
   contrast/weight or give it a backing bar.
7. **Script length planning: words = target_total_minutes × 0.9 × 137** (pocket-TTS Pharaoh
   delivered rate). 20-min ask ⇒ ~2,450 narration words.
8. **Detached render (Start-Process + log poll) is the render path** — harness background tasks
   were killed by RAM pressure from orphan chromes; kill orphans before rendering. Chunked
   rendering (JP machinery) stays out until a single render of a 20-min episode actually fails.

9. **[LOCAL PATCH] hyperframes 0.7.64 hardcodes a 30s ffprobe deadline** (`deadlineAtMs:
   Date.now() + 3e4` in dist/cli.js) — on this box ffprobe spawns take 1.4-4.5s each (suspected
   Defender per-spawn scanning) and a 33-video composition blows it ("ffprobe deadline with
   code 0"; killed 3 v2 render attempts at compile/extract). Patched to 12e4 in the npx cache
   (`_npx/*/node_modules/hyperframes/dist/cli.js`, both 0.7.64 dirs — hardlinked). Re-apply
   after any npx-cache clear: `grep -c "Date.now() + 3e4" dist/cli.js` must be 0. DURABLE fix =
   Defender exclusion for ffmpeg/ffprobe (owner/admin decision, pending).

## 2026-07-22 — ep1-joplin full-episode build (overnight ship-it)

- **Word-count annotations in edit_script overestimate ~30%**: planned ~2,460 words / "20.4 min";
  delivered TTS = 13.2 min narration → 14.0 min episode. Pharaoh pocket-TTS runs ~137 wpm
  delivered on long segments (not 129). Next episode: target word count = minutes × 137, and
  TTS a 2-segment probe before annotating the whole script.
- **TTS driver header regex must match ALL segment types carrying a blockquote** — `— narration`
  matching missed graphic-with-VO segments (a1-s2, a3-s3). Fixed: match on the segment ID.
- **120s ACE beds loop cleanly with ffmpeg `acrossfade=d=3` self-concat** — build per-act loop
  files (media/music/*-loop.mp3); no audible seam at documentary duck levels.
- **Real-radar frames carry burned-in scan times (UTC)** — any popup naming a different clock
  time contradicts the frame. Label honestly (fine-print provenance line) or match the scan.
- **NASA ASTER false-color reads as alarming red** — always add a one-line false-color
  explainer popup; the gray scar IS the story.
- **NEXRAD via GCP mirror, not AWS**: `gcp-public-data-nexrad-l2` allows anonymous listing
  (AWS bucket is GetObject-only); pyart `plot_ppi_map` creates a NEW GeoAxes (style
  `fig.axes[-1]`); velocity lives on sweep 1 (split-cut VCP), not sweep 0.
  Render script kept at `C:/nexrad-t/render_radar.py`.
- **Compaction summaries lie about artifacts** (rule 12 confirmed): "words.json exists" was
  false — always `ls` the actual files on resume before building on them.

## 2026-07-22 — owner feedback on demo-joplin-90 (overall: "incredible")

1. **Memorial/character beats: prefer a REAL photo where one publicly exists** (news/memorial
   coverage — an editorial-respect judgment per case); else make the STAT carry the emotion —
   e.g. the death toll as a rising red counter (Joplin = 161, NWS-verified; owner recalled 178 —
   always verify the number). Symbolic stock (grad cap) reads weakest of the three options.
2. **Radar/graphic beats: REAL data beats stylized animation.** Owner loved the sweep but wants
   the actual storm: render real NEXRAD Level-II archive data (AWS open data, free) for the event,
   or use NWS archived radar imagery (PD) — stylized radar only when no real data exists.
3. **Cold-open pacing: slow is fine, silence is not.** 4s to first audible dispatch sound read as
   dead air. Fix = loudness-normalize the insert to narration level (ffmpeg loudnorm, ≈ -15dB
   mean) and bring first sound in by ~1s. Keep the cinematic visual pace — owner explicitly liked
   it; tighten the AUDIO attack, not the edit.
4. **Music is a LIBRARY, not per-episode**: assets/music/ holds owned ACE-generated beds
   (5 moods); reuse/loop/duck across episodes. Generate new moods only when the library lacks one.

## 2026-07-22 — demo-joplin-90 (first E2E, owner: "incredible")

**Hyperframes 0.7.64 gotchas (cost a lint/fix cycle each — pre-empt next time):**
- Every `<audio>`/`<video>` with `data-start` NEEDS an `id` — silently SILENT/FROZEN in render without it.
- `window.__timelines = window.__timelines || {}` before assignment (lint error otherwise).
- Root composition div needs `data-start="0"`.
- No layout-property tweens (letterSpacing) — transforms/opacity only.
- Same-track time overlap = lint error; give crossfade/blackout elements their own track.
- StaticGuard "uses data-end without data-duration" on validate = **false positive** in 0.7.64
  (reproduced on JP-market's known-good probe fixture) — ignore, don't chase.
- `hyperframes transcribe` silently produced nothing on this box — use faster-whisper via
  JP-market `.venv` with `HF_HUB_OFFLINE=1` (models cached: small.en, medium.en).

**Editorial/pipeline:**
- Word-timestamp cuts work exactly as designed: transcribe each TTS segment, cut on the word.
- Stock tonal mismatch is real: sunny clips need a static CSS `filter` grade (brightness/saturate)
  to sit in a documentary cut — grade at composition, not ffmpeg.
- Insert audio needs loudness normalization before compositing — dispatch tone-out sat at
  −26dB mean vs narration −15; normalize inserts to ≈ narration level (ffmpeg loudnorm) next time.
- Music: **DeAPI ACE-Step 1.5 XL Turbo works** (endpoint + request ids in the episode's
  media/music/provenance.txt). Prompt for "no drums" may still return beat-driven takes —
  generate 2, spectrogram-check, keep the drone.
- Grain/vignette/dust as a timeline-driven seeded canvas = deterministic and cheap; reseed ~12/s.
- Sourcing workflow pattern (5 parallel download agents + vision-verify stage) delivered 100%
  usable assets in ~14 min — keep for episodes; scale agents per act.
- Owner delegation note: insert selection was owner-delegated for the demo; REAL episodes keep
  the owner gate (frames + transcript + source, yes/no).

**QC:**
- xstack contact sheets pad undefined regions GREEN — padding, not video content; don't panic.
- Snapshot pre-render QC caught both grade issues before paying for a render — keep snapshot
  sweep (≈13 frames) as the mandatory pre-render gate; post-render frame sweep stays too.
