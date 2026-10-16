---
name: storm-episode
description: >-
  Use the MOMENT the user asks to make, plan or continue a storm-market (The Warning Hour) YouTube documentary episode, or touches the storm-market repo, BEFORE reading any repo doc. Runs the freshness preflight; repo docs are stale until it passes.
---

# storm-episode — kickoff preflight + phase map

This file is tracked in `storm-market/skills/storm-episode/` and junctioned into `~/.claude/skills/` (owner 2026-09-08); the preflight below still guards against a stale checkout: a repo checkout can be stale (wrong branch,
behind origin/main, another session's uncommitted edits), and then its CLAUDE.md/DESIGN.md/
learnings/ are outdated rules that LOOK authoritative, and new contracts merged on main
are invisible from a stale checkout. The preflight is the fix. Everything else here is a pointer — the repo docs on FRESH main
are the source of truth, and this skill never duplicates their content, so it cannot drift.

Repo: `C:\Users\Sidhartha\Automation Projects\storm-market`

## Phase 0 — freshness preflight (run FIRST, before reading any doc or writing any file)

1. **Sync check:** `git fetch origin` then `git rev-list --count HEAD..origin/main`.
   Non-zero (or HEAD not on main) ⇒ every doc in this working tree is suspect. Also run
   `git status -sb` + `git worktree list` — the main checkout is shared by parallel sessions;
   uncommitted changes there are someone else's work. Touch nothing in it.
2. **Worktree BEFORE first write (hard rule, repo CLAUDE.md):**
   `git worktree add .worktrees/<ep-slug> -b <branch> origin/main`
   All episode work happens in that worktree. Full absolute paths in every message to the
   owner (worktrees make relative paths un-openable for him).
3. **Read the rulebook FROM THE WORKTREE** (fresh main, in this order):
   - `CLAUDE.md` — pipeline steps, QC gates, render + deliverables recipes
   - `DESIGN.md` — editing architecture, hook contract, CTA contract, chapter blackouts
   - `references/mg-quickref.md` — every motion-graphics rule; it goes into every MG builder's brief
   - `learnings/` — gotchas by topic, newest first (`learnings/README.md` routes by job); read at least every
     entry newer than the last episode you know about
   - `config.yaml` — pins and paths
4. **Pin current before the first render:** `python3 scripts/pin_ritual.py --check-only`; exit 3 (stale) ⇒ run `python3 scripts/pin_ritual.py` (hidden schtasks) and PR the bump now, never mid-episode; exit 4 (npm unreachable) ⇒ proceed on the current pin and note it in the kickoff summary (repo CLAUDE.md "HARD RULE: the pin stays current").
5. **Rule-change sweep:** `gh pr list --state merged --limit 5` — any PR merged since the
   last episode may have changed the rulebook; skim its description before planning.
6. **Generator tripwire:**
   `grep -rlE 'index\.html|compositions/g-' scripts/ --include='*.py'` — any script that
   WRITES or INJECTS episode HTML (index.html or compositions/*.html) is forbidden: delete
   it before any other work and tell the owner. Episode HTML is HAND-AUTHORED by the session
   via Edit/Write, per cut, with judgment — generated HTML has never passed the owner's
   quality bar. Checkers that only READ episode HTML are fine.
7. **Voice tool present:** `python3 scripts/voice_tool.py`; exit 1 ⇒ fix the piece it names (venv, clone
   script, voice reference, model login) before scripting toward TTS, and tell the owner if it is the login.
   A FAIL that ends "the next narration run downloads them" needs nothing.

Only after 1–7: plan the episode.

## Phase map (each phase's substance lives in the repo docs — follow the pointer)

| Phase | Do | Source of truth |
|---|---|---|
| 1. Research | Reference teardowns (yt-dlp info+comments+srt+contact sheets), each reference video's comments analysed into `references/comment-bank.md`, primary-source fact pass (never trust competitor "facts"), claim-safe footage inventory | CLAUDE.md "The formula", `references/comment-bank.md`, learnings/ teardown entries |
| 1b. ANGLE LOCK (OWNER GATE, before any packaging or script) | Find and test the candidate angles, show the owner all of them with one recommendation, park until he locks one in words, then write `episodes/<slug>/angle.md`. No title, thumbnail, hook or script line exists before that file does | `references/angle.md` (method, tests and the block's format) |
| 2. Design (only after the angle is locked; packaging per `references/packaging-rules.md`: title ≤52 chars with Name+Year in the first 40, thumb school A/B/C by video type) | `edit_script.md` — typed segments, per-beat visual intent + NAMED clip source, blackout-dip placement, **CTA hinge named (segment before / after, DESIGN.md "CTA contract", position from the `config.yaml channel.cta` window)**, word budget via `scripts/word_budget.py` (probe-TTS 2 segs at the shipping tempo, CLAUDE.md Voice), AI-image gap list for owner. **Brief the writer with the locked Angle block (`episodes/<slug>/angle.md`, pasted inline) + `references/script-quickref.md` + `references/flag-words.md` + the episode research pasted inline; the writer opens no other rule file.** Script work runs one agent per act in parallel, never one agent over the whole script (owner 16 Oct 26): each writer, grader and fact-checker owns one act and edits only that act's segments, and every round fans out at once. The writer only TAGS unconfirmed facts `[verify: ...]` inline and hands off hook+intro first — it never self-verifies or reads the six rule docs (script-scaling.md "Script fact-QC layer"). | `references/script-quickref.md` (the one binding rule set); `script-os.md`, `script-framework.md`, `humanise-rules.md`, `script-scaling.md`, DESIGN.md are its sources, not the writer's reading list |
| 3. OWNER GATE + fact-check fan-out (parallel, not serial) | The moment hook+intro is written, two things start on that SAME draft at once, not one after the other: (a) owner sign-off in chat — story/register, paid-spend/bulk-sourcing approval, park until chat approval, never infer, silence is never approval; (b) a fact-check fan-out — several subagents, each owning a slice of the open `[verify]` markers, resolving CONFIRMED/CORRECTED/UNVERIFIED against `research/`. Neither reviewer is the writer. A separate skeptic-reviewer agent also grades the hook/script before the owner sees it. **A section LOCKS only per the one definition in `references/script-scaling.md` "Section lock — the ONE definition"** — it moves to TTS/compose immediately once locked, without waiting for later acts still in fan-out. | `references/script-scaling.md` "Section lock — the ONE definition" (the lock rule lives there, not here); `learnings/script-process.md` "independent grade on every script" (grader bar) |
| 4. TTS + timing | `python3 scripts/tts_episode.py episodes/<slug> --only <locked segment ids>` runs per LOCKED section as it clears (hook+intro first), not once for the whole script — `tts_episode.py` hard-fails any selected segment whose text still carries an open `[verify]` marker; per-segment TTS, lane tempo, words.json in one pass | CLAUDE.md step 2 + Voice, config.yaml external.* + channel.tempo |
| 5. Sourcing | Agent-downloaded, 2–3 candidates/beat, provenance.csv row per file, per-cut frame verification, inserts owner-gated individually | DESIGN.md sourcing + Content ID protocol |
| 6. Compose | **Bespoke diagrams: brief first on `references/mg-brief-template.md` (source figure, datum, px geometry, must-be-true list), scaffold-first build (boxes + real text + cue tweens → 4-frame read → style → motion), meaning reviewed before layout, one frame read by the orchestrator (owner 2026-09-12). Builders build from the brief in parallel: Opus 5.5 for the deep top 5 to 15, Sonnet 5.5 at high effort for the rest (CLAUDE.md "Chain of command for motion graphics"); the builder never verifies itself (roles: CLAUDE.md "Chain of command for motion graphics"). A builder starts only once its section's VO is final (order: CLAUDE.md "Voice"); a graphic built before the VO gets retimed (ep-nepal: 5 retimes). No fixed cap on builders (owner 13 Oct 26: "5 builders is a wrong cap ... please spin up more agents"): agents run on the API, not on local cores, so start one builder per graphic that can be built independently and say the number in the plan. Readers start as soon as the first graphic is built. Captures, gates and renders run on the ZBook.** **Library-first (owner 2026-08-27):** search `library/catalog-index.json` + `npx hyperframes catalog --query "<intent>"` BEFORE hand-authoring; copy the closest in-house exemplar / official block and HAND-RETUNE per cut (scratch allowed with a one-line reason in edit_script.md). Then HAND-AUTHOR index.html + `compositions/g-*.html` (Edit/Write, per-cut judgment — NEVER a script that emits HTML) per `references/mg-quickref.md`; 2–3 versions of each big-concept graphic; act-boundary blackouts hand-placed; **CTA mounted from `config.yaml channel.cta` (staged `media/cta/`, own audio, dips per config)**; GSAP/WAAPI only | `references/mg-quickref.md` + DESIGN.md "CTA contract" + repo `library/` gallery + `references/editing-patterns/` (never edit a shipped episode) |
| 7. Static QC | ALL green before any render: `python3 scripts/run_gates.py episodes/<slug>` (stops on the first failing gate); then the settle-frame pass in `references/mg-quickref.md` "Verify" (new/changed comps only, one subagent reader, two fix rounds max) | CLAUDE.md "render is the LAST step" + step 6c, learnings/mg.md "ep6 draft v2 review" |
| 8. Render | `scripts\render.cmd <slug> draft` first; owner reviews draft; full only after approval. EVERY scheduled/background command runs hidden via `scripts/run_hidden.vbs` (schtasks action = `wscript run_hidden.vbs cmd /c ...`) — a run that opens a visible window is killed (stop the TASK, kill its process TREE from the root pid — never kill by command-line substring) and reported | CLAUDE.md steps 5–6 + "No visible windows", learnings/render.md |
| 9. Deliverables | `master_deliverables.py` (−14 LUFS master + SRT; then finals to main, other renders deleted, worktree removed), metadata.md (**first URL = `channel.cta.first_link`, "📘 The book mentioned at" line, no chapter at the CTA**), private upload + Checks soak | CLAUDE.md step 7, DESIGN.md claims protocol + "CTA contract" |

## Standing owner rules that gate every phase (details in repo docs)
- Timeline is master; the model is the editor; scripts = deterministic checks only.
- Chaser/streamer footage NEVER without license; non-PD pulls 3–4s narrated-over; no
  provenance disguise. Repeats allowed only well-spaced (≥3–4 min, never obvious).
- The ebook CTA is must-keep (owner 2026-08-30): every episode, in-timeline, inside the `config.yaml channel.cta`
  window (placement rule: DESIGN.md "CTA contract"); `sweep_episode.py` fails without it. Never skipped, shortened, or moved to the outro.
- An owner correction lands in its single home the same session (`references/mg-quickref.md`, a gate, or the right `learnings/` file). Docs sweep in the same PR.
- Every review cut = draft render; owner previews park the pipeline until chat approval.
- Render monitoring: poll with `/loop` every 2–3 min, never a detached background watcher and
  never ScheduleWakeup (its turns are invisible to the owner). Never resume a render from another
  session or a compaction summary: re-derive scene/render state from the run dir, manifests, and
  output files first.
- Per-render image QC, every render, on actual frames (subagent eyeballs, never Read into main
  context): hand/finger anatomy (6–7 fingers, 3 hands), broken eyeglasses, deformed faces,
  burned-in caption/subtitle text.
