# Palm Sunday 1965: build checklist

Status is read from this file. A box is ticked only with the check that proved it.

## Kickoff, 11 Oct 26
- [x] Angle locked by the owner on the review page, 16:29: Candidate 1, note "c1+2+ a bit of 3? or 4? i mean there will be subarcs u will write. go ahead". Lock file: `angle.md`.
- [x] Worktree `.worktrees/ep-palm-sunday-1965` from origin/main at 15c15a29; main checkout not touched.
- [x] Voice tool: `python3 scripts/voice_tool.py` exit 0 (venv, clone script, voice reference, cloning weights all PASS).
- [ ] Pin: `python3 scripts/pin_ritual.py --check-only` says 0.8.143 is stale, npm latest is 0.8.147. Run the ritual and PR the bump before the first render, when no other heavy job is running.
- [x] El Reno learnings on main (PR #160: graphics done line, verify reads, logo rule): merged 11 Oct 26, origin/main 18252a35, tree identical to the reviewed head eace5ef7 (`git diff --stat` empty). Main merged into this branch; `git grep "7a. DONE LINE" -- references/mg-brief-template.md` finds it here.
- [ ] Length: the slate says 20 to 25 minutes. Not yet confirmed by the owner for this episode.

## Research (three helpers, started 16:39 to 16:42)
- [ ] `research/facts.md`: the warning chain message by message, the tornadoes in order, where the chain stopped, the numbers the sources disagree on.
- [ ] `research/teardowns.md`: four existing videos, what all of them tell and what none tells, viewer comments.
- [ ] `research/picture-inventory.md`: real pictures, film and sound, each with its rights line and a verdict.
- [ ] Every quoted line in `facts.md` looked up again by the orchestrator in its source.

## Design (not started; nothing here is written before the research is read)
- [ ] Structure: acts, the three open questions, which of candidates 3 and 4 is the small arc. Shown to the owner.
- [ ] Title and thumbnail options (`references/packaging-rules.md`). Owner picks.
- [ ] Hook and intro, graded by an independent reader, then the owner's sign-off.
- [ ] Paul's on-camera lines; the book ad hinge inside the config window.
- [ ] `edit_script.md` section by section, fact-check fan-out beside the owner's read.

## Build (not started)
- [ ] Narration per locked section. [ ] Sourcing with a provenance row per file. [ ] Graphics from briefs carrying section 7a. [ ] Gates green. [ ] Draft render. [ ] Owner review. [ ] Full render, master, subtitles, metadata.
