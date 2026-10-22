# Act builder: common brief (ep-mayfield-2021, compose round 2, 22 Oct 26)

Project: `C:\Users\Sidhartha\Automation Projects\storm-market\.claude\worktrees\ep-mayfield-2021-a6d084` (storm-market worktree, branch
`claude/ep-mayfield-2021-a6d084`; a narrated US tornado documentary built as a hyperframes HTML composition). Rules: that folder's
`CLAUDE.md`, `DESIGN.md`, `references/mg-quickref.md` (read in full), `learnings/mg.md`, `library/inhouse/snippets/tokens.md`.
Episode dir below = `episodes/ep-mayfield-2021` inside that worktree. Use absolute paths; never `cd`; `python3`, never `python`.

Goal: take your act from locked narration to a composed, gate-clean stretch of `index.html` for the owner's draft preview.

## Inputs (all exist; a missing one = stop and report)
- Script with each segment's Picture line: `edit_script.md` (your act's section).
- Your graphics' briefs: `briefs/mg/g-<id>.md` (on `references/mg-brief-template.md`) and the plan table `briefs/mg/plan.md`.
- Narration timings: `audio/<seg>.words.json` (word times inside each wav) and `briefs/compose/timeline.md` (each segment's
  EPISODE start). Episode time of a word = segment start in timeline.md + the word's `start` in words.json.
- Sourced footage: `media/candidates/<act>/` with `picks.tsv` (the sourcer's pick, in/out, risk) and `provenance.csv`. Read the
  provenance row before wiring a file. Radar replots already made: `media/radar/` (g-a1-6, g-a3-6 folders, `replot.py`).
- Finished examples to copy from (same episode, already verified): `compositions/g-*.html` for the intro (map family g-t1-1,
  building g-i1-5, radar g-h1-3, doc page g-i1-2, quote card g-i1-7, chips g-h1-2 / g-i1-6, claim card g-i1-8, Edwardsville map
  g-i1-9) and the intro's still mounts + `punch()` / `push()` helpers in `index.html`.

## What you build
1. Every graphic your brief list names: one `compositions/g-<id>.html` each, per its brief and `references/mg-quickref.md`
   "File contract". Hand-authored with Write/Edit. Library first, copy the intro's family bases. No script may write HTML.
   Briefs say `npx hyperframes@0.8.149`: the pin is now **0.8.185** (`config.yaml hyperframes_version`).
2. Your act's stretch of `index.html`, ONLY between your markers `<!-- ==== <ACT> (builder) ==== -->` / `<!-- ==== /<ACT> ==== -->`
   (elements) and `// ==== <ACT> (builder) ====` / `// ==== /<ACT> ====` (the script block: `punch()`/`push()` calls). Other
   builders edit the same file concurrently in their own markers: Edit with a unique old_string, and if an Edit fails because the
   file changed, re-read and retry. Never touch lines outside your markers.
   - One `<audio id="nx-<seg>" src="audio/<seg>.wav" data-start=<timeline.md start> data-duration=<timeline.md dur> data-volume="1">`
     per segment, EXCEPT the Paul slots (a1-s13, a2-s10, a3-s9, a4-s6, z1-s7), which the orchestrator already mounted.
   - Picture on every second of your act's narration: stills (`<section class="clip still-wrap" id="v-..."><img id="v-...-img">`,
     track 1, 3 to 6 s each, each with a `punch()` or `push()` line), muted footage (`<video ... muted data-track-index="1">`, cut at the
     sourcer's in/out with `data-media-start`), full-frame comps on track 2, overlay chips/cards on track 4 over footage beneath.
     Picture ends exactly at your act's blackout / Paul slot boundaries; Paul slots are covered by the orchestrator's card.
   - Every mount's times come from words.json cues, with the cue in a comment (episode seconds), as the intro does.
   - Graphic host windows: duration = max(declared, last cue + ~1 s land + 0.6 s exit), comp timeline >= host window.
3. Media you mount: copy (never move, never overwrite) the pick into `media/stills/` or `media/clips/` with a `<act>-...` name; trim
   video with ffmpeg to the pick's in/out, scaled to at most 1920x1080, video only (`-an`). Stills larger than 1920x1080 get scaled
   down. Blurry small stills (under ~1000 px wide) may be upscaled with `realesrgan-ncnn-vulkan` if on PATH, else mount as is and list it.
   Every mounted video carries `muted`. No clip with its own audio (no inserts) in this round.
4. Footage rules: never chaser/streamer footage, never the FOX 2 aerial, the SA cover image or anything the picks file marks NEVER.
   A news pull is muted, a few seconds, narrated over. A still or comp naming a place sits only over footage of that place
   (provenance row).

## Not yours (the orchestrator does these)
Sound (beds, swells), blackouts, the CTA, Paul slots and their placeholder cards, the presenter circle, the end ask, the close card
mount, runtime changes. Do not change any segment's start time: timeline.md is fixed. A beat that cannot be built as written:
build the honest neutral alternative (a designed card or a neutral still) and list it under "calls made".

## Checks you run (your files only; never a render, never `scripts/render.cmd`, never on the ZBook)
- `node scripts/graphics_qc.mjs episodes/ep-mayfield-2021` : 0 errors on your comps.
- `python3 scripts/lint_timeline.py episodes/ep-mayfield-2021` and `python3 scripts/sweep_episode.py episodes/ep-mayfield-2021`: no
  finding that names your ids or your time range (other acts may still be unbuilt: ignore findings outside your range).
- `node scripts/overlap_check.mjs episodes/ep-mayfield-2021`, `node scripts/blank_scan.mjs <absolute episode dir>`,
  `python3 scripts/beat_density.py episodes/ep-mayfield-2021`: nothing in your range.
- Frames: `npx hyperframes@0.8.185 snapshot episodes/ep-mayfield-2021 --at <t1>,<t2>,... --no-end --describe false -o
  episodes/ep-mayfield-2021/.qc-tmp/<act>-frames` at a settled moment of each new graphic over its real picture. Look at them.
  Fix what you see (cut-off text, a label over the wrong thing, empty frame). The orchestrator re-reads frames independently.
  Snapshot is heavy: one at a time, batch your `--at` times into a few calls.

## Never
- rm, rmdir, `git rm`, delete files; list strays in your final message. Never `git commit`, `git stash`, `git checkout`, `git reset`.
- overwrite media (write `<name>-v2.<ext>`); edit other acts' markers, other builders' comps, CLAUDE.md, skills, hooks, settings.
- add decorative elements or remove things to pass a check; a fix changes a value, row or word.
- claim owner approval; pull facts from outside `research/`, the briefs and edit_script.md. On-screen quotes are verbatim.
A denied call is final: report it. Decide small judgment calls yourself and list them under "calls made".

Stop at the done check, at the first blocker, or after 150 min. Report what is finished and what is not.
Done = every graphic in your list exists and passes graphics_qc; your act's narration is fully covered by picture with no gap;
lint/sweep/overlap/blank show nothing in your range; you looked at a settled frame of each graphic.

Return: final message is the result, text, at most 2,000 characters, to the orchestrator only (you never address the owner):
result first; files written with byte sizes; each check's exact command and quoted exit line; graphics built vs not; beats you
changed from the Picture line ("calls made"); open items. Verdict PASS / PARTIAL (open items) / FAIL. Blockers as `[BLOCKED: reason]`.
No report .md files.
