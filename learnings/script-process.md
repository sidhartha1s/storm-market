# learnings/script-process.md: script and process: hooks, CTA, script loop, owner gates, agent and session process

Newest first. New entries go at the top, under this line. Superseded lines point at their current home.

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

## 2026-09-22 - ep-1974 draft 2 review: narrator opens the video, banned audio is gated by hash, holds need a reason
- **No broadcast, radio or archive audio in the hook.** Owner: "these broadcast stuff at the hook is a nono. because of bad
  audio quality. no point if the narrators hook being 10/10 if only 40% people wait till it starts at 10secs." The narrator's
  first line is 0:00. DESIGN.md "Cold-open hook contract" is rewritten; the old "anchor line by 2.5 s" rule is gone. The date
  popfig sits inside the first second and clears before the first designed graphic (here 0.15 to 1.65 s).

## 21 Sep 26 — owner review of the ep-1974 draft: "shippable after these small iterations"
3. **CTA at 85 to 90 % on this doc**, not 30 to 40 %: owner 21 Sep 26 "keep around 85-90 % timeline in a fitting
   manner", fallback "reduce the end ask, then the video, one more sentence, close". ep-1974 sits at 88 % after the
   16-dead-then/4-now payoff. `config.yaml channel.cta.window_by_slug` carries per-episode placements; the deep-lane
   window stays until the owner moves it for the lane (one-orange rule). The 30-40 % rule dates from 30 Aug 26.

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
   owner. Revised 27 Sep 26 (`references/script-scaling.md` "Section lock — the ONE definition"): the grade applies
   PER SECTION, before that section locks, not once on the whole finished script — the hook section needs a grader
   hook score of at least 8, and no chapter axis on a locking section may be under 3.
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
2. **(Superseded 27 Sep 26: hook is 3–5 s, then a 5–15 s tail.) The hook is 45 to 60 words, 20 to 25 s including the insert.** Anything the viewer does not need to decide
   to stay is cut. Test: delete the first sentence; if the hook still works, the sentence was fluff.
3. **No roadmap phrases anywhere** ("one more thing before", "here is what that day would become", "in the next
   twenty minutes"). They read as delay. Fold the numbers into a sentence that already carries stakes.
4. **The CTA hinge is one tease sentence, not a paragraph.** The segment before the CTA ends on the loop in ≤ 25
   words; the segment after opens with the payoff in its first three words ("He wrote a six.").
5. **Owner-cut SRT diff is the retention gate for the next script:** before writing a new hook, diff the shipped
   SRT of the last video against what is live on YouTube and list what the owner removed; do not write those
   shapes again. (20 Sep 26: the live durations of Joplin, Tri-State and Super Outbreak still match the shipped
   SRTs to within seconds, so the trims may still be processing; re-check before the next script.)

## 2026-09-12 · MG eval: a tidy diagram with the island underwater scored 21/25
- Auto-mode classifier refuses most new Agent spawns from command-heavy prompts ("Auto-Mode Bypass"); resuming an existing
  agent via SendMessage passes. Owner adds `Agent` to permissions.allow; the session cannot (Self-Modification).

## 2026-09-11 · Krakatau #4 mistake ledger: which gate should have caught what
- Process: list every violation in one pass before iterating (three gate cycles burned on one bug line at a
  time); write Windows-path scripts with the Write tool, never bash heredocs (the backslash-U escape trap, three
  times this session, once while writing this very rule).

## 2026-09-10 — Krakatau packaging pass: owner corrections on title length and thumbnail plates

- **Titles aim under 60 characters.** Not a hard cap ("55 is not an upper limit"); low-value stretchers at the tail are fine, but an 87-char title was rejected on sight. Owner's own rewrite: "It Killed 36,000 First. Now It's Happening Again." (49).
- **Thumbnail plates are bright and detailed.** A night plate (deep shadows, moonless) was rejected: too dark, details not visible at phone size. The owner supplied a sunset eruption plate (`thumbs/owner-plate-sunset.png`, ChatGPT) as the reference look: golden light, vivid colour, sharp everywhere.
- **This episode's text: one red word, huge, at the top** (DEADLY / UNSURVIVABLE), no kicker. Instance decision for Krakatau, not a rewrite of the mini-storms ≤4-word + BREAKING kicker rule; propose generalising only if the owner repeats it.
- **ChatGPT renders thumbnail text in-image, and better than Pillow.** Owner: "it does most of my thumbnails itself." On the same plate the model's DEADLY beat the Impact composite. Prompt recipe (word in caps, position and width in percent, font by reference + hex, outline + shadow, "keep the photograph exactly as it is", negatives) lives in the `yt-packaging` skill, `references/thumbnail-production.md`. Driver: `~/Automation Projects/webgen/genimg.mjs edit|gen chatgpt-simplotel`.
- The `yt-packaging` skill (installed 2026-09-10 in `~/.claude/skills/`) now runs before any title/thumbnail work on this channel; its cover-one and redundancy tests are what caught the IT'S BACK / "Just Erupted" triple restatement.

## 2026-09-08 — breaking lane v1 (br-elnino-california, /mini-storms first run)

- **Structure vocabulary (owner correction):** HOOK is 3–5 s (owner 27 Sep 26, was 3–10 s), one sentence paying off the title.
  Then INTRO to ~1:10 (stakes, open loops, promise). Then chapters. A 45 s "hook" was rejected.
  Size every section in words at the delivered wpm before TTS (packaging.md table).

## 2026-09-08 — breaking lane, first video (br-elnino-california): owner corrections + measured facts
- **No chapter cards in the breaking lane** (owner, after the v1 preview): chapters butt-cut with a 0.45 s
  narration gap; the script's connective sentences carry the transition. Removing 8 cards = one-shot
  mechanical retime (events list: point, delta; starts shift for points ≤ start, ends for points < end).
  Gotcha: a narration window whose end sits 0.01 s past a removed span gets shortened by the rule —
  restore every nx-* duration from audio/manifest.json after any retime, then re-check gaps.
- CTA gate skipped `br-` slugs and the 30-40 % window: superseded by the sweep slug regex `(ep\d*-|ms-)` (21 Sep 26) and the 85-95 % window (23 Sep 26).
- Runtime log for the 3 h SLA lives in `episodes/br-elnino-california/runtime.md`.
- **Video #2 (ms-elnino-texas) build recipe that worked:** cut lists hand-authored per narration segment as
  (kind, src, dur, id, callback); a scratch helper (never committed) computes butt-cut starts from the
  narration schedule and fills the last slot; overlays hand-authored as (kind, id, at, hold, big, sub).
  Total authoring ~25 min. Media probes in `sweep_episode.py` report "frame extraction failed" while a full
  render is running on the box — re-run the sweep on a quiet box before believing it.
- **Script retention pass (owner 2026-09-11, Krakatau #4 v1 → v2):** the v1 draft scored 5.5/10 on stakes per
  90 s: chronology order put the peaks (Lituya, the arithmetic) at 6:51 and 10:17 and the dips (1883, fix list, the
  not-happening list) after the CTA and in the last third; three macro-loops opened in the first minute and none was
  touched again for 6–10 min; the intro was a table of contents; the voice read out "December twenty second, twenty
  eighteen, three minutes past nine" while the MG could carry it. Owner: "just say two days before Christmas, show
  DEC 22, 2018 · 9:03 PM in MG; that's the engagement manipulation you are missing." Full rule set now in FORMAT.md
  "Retention architecture" and the mini-storms skill; the v2 hook is the owner's line verbatim.

## 2026-08-30 — the ebook CTA is a channel asset + a must-keep contract (owner order, ep4 rewire kickoff)

1. **The CTA was never in the pipeline.** ep2's Paul CTA was spliced into the finished mp4 by the
   owner outside the repo (learnings/render.md 2026-08-29: located by cross-correlation), ep5/ep6 shipped with
   none, and the clip itself lived only in `Videos\storm-insert-work` — unfindable from the repo.
   Now: `assets/cta/paul-storm-ready-v4c.mp4` (tracked; `.gitignore` negation — the only mp4 in
   git), transcript + README beside it, `config.yaml channel.cta` as the single source of truth.
2. **Placement is a contract, not taste:** hook > CTA > payoff, start inside 30–40% of runtime (superseded 23 Sep 26: 85–95 %, `config.yaml channel.cta.window`),
   scripted tease before / payoff first-sentence after, 1.0s dips, own audio, no chapter boundary,
   first link in the description = the ebook. DESIGN.md "CTA contract"; `sweep_episode.py` fails a
   missing or misplaced CTA; `script-scaling.md` requires a `cta-hinge` loop-table row.
3. **`build_srt.py` only saw `<audio id="ins…">` inserts** — ep6-style `<video id="ins…"
   data-volume="1">` inserts (and the CTA) got no SRT cue. Fixed: video inserts with
   `data-volume="1"` are cued from their `data-srt-label` too.
4. ep4 (El Reno) is the first in-timeline use; the contract is "verified" only once ep4's draft
   shows the CTA landing on the hinge and the sweep passes on it.

## ep6 ship (2026-08-23) — hyperframes 0.8.x, the hidden-console chain, and a preflight bug
- **Subagent briefs must forbid `cd`.** Two Explore agents issued `cd`-prefixed Bash and produced
  8+ permission prompts on the owner's screen in auto mode. Prefer Grep/Read in the main session;
  any subagent with Bash gets "never cd; absolute paths only" in the brief.

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

## The doctor rule — known-below-spec = STOP, never render (owner, ep5 v4 RCA, 2026-08-13)
v4 shipped a music layer I knew was below the ordered spec ("Hybrid C") — flagged it in my own
park summary and rendered anyway. Owner burned a review cycle discovering what I already knew.
Standing rule: the moment a deliverable is known below spec, STOP before the render, state
exactly what is broken, give options, wait. A render on a known defect wastes GPU hours AND the
owner's review hours. Corollary: verification gates check STRUCTURE; before any render also do
an EXPERIENCE pass — listen to the full audio mixdown, watch the hook, spot-watch 3 random
minutes. A green suite on an unwatchable artifact is a failed QC.

## Owner pivot 2026-08-12 — cadence, sourcing, SFX, durable references
- **Docs must not cite episode paths** — episode folders get deleted after publish. Shipped
  patterns get COPIED into `references/editing-patterns/` the same session ("you want it to be
  gone with the wind?").
- **Docs drift is a real defect class:** "still ≤12s" survived two owner cadence corrections
  ("will your grandfather come and revise this?"). Any editorial rule change sweeps CLAUDE.md,
  DESIGN.md, LEARNINGS.md AND the gate scripts in the same session (homes since 26 Sep 26: CLAUDE.md, DESIGN.md,
  references/mg-quickref.md, learnings/, the gates).

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
   already moving, anchor audio already mid-transmission (anchor audio superseded 22 Sep 26: the narrator opens at 0:00). The 2–3s VOID survives only as the
   hook's END punctuation. (DESIGN.md hook contract amended.)
5. **Language: 4th-grader readable (owner).** Short words, concrete pictures; emotion from facts
   and rhythm, never vocabulary. Matches the shipped eps' register; TTS syncs cleaner.
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

## ep3 v3 — stop rendering to find things a script can find (2026-07-29)
- **When the owner gives timestamps against an old cut, MAP THEM YOURSELF.** I asked him to
  re-point 5:48 and 28:04 because the v3 timeline had shifted. That was my job: the v2 draft
  was built from a commit still in the tree, so `git show <sha>:episodes/<slug>/index.html`
  into a temp dir plus the window ledger answers it in one command. Doing that showed his
  5:16 and 5:48 notes were the SAME defect — one 33.4s stock cloud clip covering a whole
  four-minute-mark passage — and that 28:04 was a 0.904-aspect portrait stretched full-frame
  for 163 seconds.
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

## ep3 v3 - second audit round (2026-07-29)
- **Audit findings need adversarial verification before you act on them.** 81 raw findings became
  54 confirmed - a third were wrong, including several that would have sent me editing correct code.

## ep3 v3 (2026-07-29) — the "check the code, not the frames" rebuild
- **Tooling gotcha:** the Bash tool consumes backslashes in heredoc'd Python even inside a
  quoted `<< 'EOF'`. `"\n"` arrives as a real newline, which silently corrupts source-generating
  scripts. Build literal backslashes with `chr(92)`, and always `ast.parse` the result.
- **Windows CRLF breaks naive line-joining repairs** — read/normalize with explicit
  `.replace(chr(13)+chr(10), chr(10))` before any line-level surgery, and write back as bytes.

## 2026-07-27 — ep2 hook rebuild + ship (hook contract now in DESIGN.md)

**Editorial:**
1. **The hook contract (owner rated old hook 0.6/10, demanded 9.8+ "unskipable").** What made
   it 0.6: four undifferentiated clips in 12s, no intelligible speech until 0:22, one silent
   clip, mid-sentence commentary fragments, an orphan audio tail after the emotional line, no
   sonic build. What fixed it (the anchor-line part is superseded 22 Sep 26: narrator at 0:00, no archive audio in the hook): an intelligible ANCHOR line (Spann's live "tornado emergency")
   starting by ~2.5s; every cut lands ON an audio event; a siren spine that builds start→duck→
   swell→die (superseded 26 Sep 26: the hook's sound is reasoned per episode, see DESIGN.md); the insert trimmed to end on its complete emotional statement ("we knew something
   was coming" — nothing after); date/place card in the first second; a dead-silent VOID
   before the narrator enters (2-3s then; **1.5s since the 2026-08-16 blackout table**). Full contract in DESIGN.md — apply from ep3 scene one, don't
   rediscover it.
2. **Dual-scope statistics must be self-disambiguating in publish copy.** 324 (outbreak) vs 316
   (Apr 27 alone) are both correct, but a reviewer read them as a contradiction — a viewer will
   too. Any copy using a scoped figure names the scope in the same sentence.
8. **Shipping while another session holds `.git/index.lock`:** `git worktree add <dir> -b
   <branch> origin/main` succeeds despite the lock (index.lock only guards the main checkout's
   index). Copy changed files in, commit/push/PR/merge from the worktree — the other session's
   checkout and branch are never touched. Note: the auto-commit hook fires inside worktrees too
   (an Edit there self-commits); `git worktree remove` can hit Windows Permission-denied — `mv`
   the dir to trash + `git worktree prune` works.

## 2026-07-26 — ep2 v1 owner review (9/10; every item below is a standing rule now)
- **Every act's episode outro carries the episode number** (match ep1: "Episode N — Title").
- **Owner meta-principle (from 6 channels):** do NOT pre-constrain the editor-AI with scripts
  and hard-coded rules before it sees the problem. Scripts = deterministic checks only (lint);
  pacing/grading/placement stay AI judgment per-case. "Do not draw lines before AI even sees
  the problem."

## 2026-07-26 — ep2 overnight build (tooling gotchas, all reproduced)
- Subagents can go idle without reporting (2 of 6 tonight) — poll with SendMessage pings; if still
  silent, verify their on-disk output yourself and take over the reporting step.

## 2026-07-26 — ep2 design review (owner corrections, all wired into CLAUDE.md/DESIGN.md same session)
5. **Conditional-fact rule**: a proposed distinctive fact ships ONLY if verification confirms it
   (e.g. "Wrangler plant never reopened") — drop entirely on failure, never soften into "reportedly".
6. **Runtime**: 13–23 min band is a default, not a cap — owner explicitly ordered 30 min for ep2
   (high-demand topic). Word formula scales: minutes × 0.9 × wpm (see 7; superseded by `scripts/word_budget.py`, 22 Sep 26).

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
- (Limits superseded: max 3 uses since owner 2026-07-28, and long holds are a printed report since 2026-07-23; see lint_timeline.py docstring.)
  `scripts/lint_timeline.py` now FAILS on: file reuse without `data-callback` (max 2 uses),
  any non-graphic visual >12s without `data-hold-ok`, both exempt in the last 90s (summary).
  Ran against v2: 31 findings — it would have blocked the false claim. HARD pre-render gate
  (repo CLAUDE.md step 6).
- DESIGN.md: subject-family dedup rule (dedup what the frame shows, not the filename).
- Meta-rule in CLAUDE.md: never claim an editorial rule fixed from memory — re-run the lint.

**Owner clarifications captured:** recap/outro reuse is fine (exempt zone); more stock/NOAA
variety encouraged; goal = learnings compound so video N needs fewer revisions than video N-1.

## 2026-07-22 — ep1-joplin full-episode build (overnight ship-it)
- **Compaction summaries lie about artifacts** (rule 12 confirmed): "words.json exists" was
  false — always `ls` the actual files on resume before building on them.
