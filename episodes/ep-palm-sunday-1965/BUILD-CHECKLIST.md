# Palm Sunday 1965: build checklist

Status is read from this file. A box is ticked only with the check that proved it.

## Kickoff, 11 Oct 26
- [x] Angle locked by the owner on the review page, 16:29: Candidate 1, note "c1+2+ a bit of 3? or 4? i mean there will be subarcs u will write. go ahead". Lock file: `angle.md`.
- [x] Worktree `.worktrees/ep-palm-sunday-1965` from origin/main at 15c15a29; main checkout not touched.
- [x] Voice tool: `python3 scripts/voice_tool.py` exit 0 (venv, clone script, voice reference, cloning weights all PASS).
- [ ] Pin: `python3 scripts/pin_ritual.py --check-only` says 0.8.143 is stale, npm latest is 0.8.147. Run the ritual and PR the bump before the first render, when no other heavy job is running.
- [x] El Reno learnings on main (PR #160: graphics done line, verify reads, logo rule): merged 11 Oct 26, origin/main 18252a35, tree identical to the reviewed head eace5ef7 (`git diff --stat` empty). Main merged into this branch; `git grep "7a. DONE LINE" -- references/mg-brief-template.md` finds it here.
- [x] Length: 20 to 25 minutes, ticked by the owner on the review page `p65-structure.html`, saved 11 Oct 26 17:24.

## Research (three helpers, started 16:39 to 16:42)
- [x] `research/facts.md`: the warning chain message by message (23 rows), the tornadoes in order, where the chain stopped (22 sentences), the numbers the sources disagree on.
- [x] `research/teardowns.md`: four existing videos (two transcripts read, two had none), what all of them tell and what none tells, viewer comments. None follows a warning to its receiver.
- [x] `research/picture-inventory.md`: 65 items, verdicts Free 22, Ask 37, No 6. No free picture of an office, a police radio room, a studio or a siren.
- [ ] Every quoted line in `facts.md` looked up again by the orchestrator in its source. State 11 Oct 26: 88 found exactly, 37 found with scan-broken letters, 0 not found, 19 sit on the image-only survey scan. Of those 19, one read on its page image so far (Fort Wayne, printed p. 44, word for word). Each line that reaches the script is read on its page image before it is voiced.

## Design (not started; nothing here is written before the research is read)
- [x] Structure: `structure.md` (six acts on a clock, three open questions, candidate 3 as the small arc in Act 5, candidate 4 as two short beats, book ad after Act 3). The owner ticked "Go as shown" on the review page `p65-structure.html`, saved 11 Oct 26 17:24, with the open check on the angle shown at the top of that page.
- [x] Twin funnel photograph (picture inventory row C1): owner on the same page, in his words: "use it." This picture only. Used on the Wikimedia Commons public-domain claim; credit "Paul Huffman / The Elkhart Truth" in the description.
- [x] Open check on the angle: the Tornado Autopsy video and the 1966 State Police film heard from their audio (helper p65-teardown, machine transcripts; `research/teardowns.md` sections 2 and 3). Neither follows one warning desk to desk; neither says police or civil defense held a warning. Orchestrator spot check, 11 Oct 26: `grep -i police` on the film transcript gives 8 lines, all reports to the Bureau, rescue or planning; `grep -i panic` gives 0. The structure stands. Tornado Autopsy does use the 6:50 PM South Bend telephones message.
- [x] Title: **Who Stopped the Palm Sunday 1965 Tornado Warning?** Ticked by the owner on the review page `p65-pack.html` (round 2, 7 titles with no reading-ease gate), saved 11 Oct 26 22:40. Round 1 (6 titles written to the reading-ease floor) was rejected at 21:16: "the titles suck actually ... maybe because u are trying to achieve the readability rating thing, maybe remove that. keep them punchy still." Rule change for the repo: PR #161, merge waits for his OK.
- [x] Thumbnails: the owner in chat, 11 Oct 26 22:40: "all thumbs are good." No single one ticked on the page, so all three Paul takes stand (`thumbs/t1-onground-poles-gen.jpg`, `thumbs/t2-fieldnotes-chain-gen.jpg`, `thumbs/t4-critlat-layout-gen.jpg`, made on his note of 21:16 "gen all and show me. also, a version similar to critical latitude") beside the no-face partner `thumbs/t3-noface-poles.jpg`. Which runs is settled in YouTube's Test and Compare at upload.
- [ ] Thumbnail publish build, at upload time, not before: (a) thumbnail 1 is rebuilt as Paul and the words laid over the untouched photograph, because the ChatGPT take repainted the twin funnel into one; (b) each headline shares one word with the picked title (1: WARNING, 2: STOPPED, 4: STOPPED) and `references/packaging-rules.md` says the headline is never the title's words, so one word changes in each; the changed words go to the owner as inputs before any new ChatGPT take.
- [ ] Hook and intro, graded by an independent reader, then the owner's sign-off. State 11 Oct 26 23:07: `hook-intro-draft.md` holds three versions after fix pass 1 (first grade: v2 6, v3 5.5, v1 4 of 10, bar 8; fact check 33 confirmed, 3 corrected, 0 unverified; check round on the fixed text: 28 of 29 fixes landed, v3 8, v2 7.5, v1 6.5). Shown to the owner on the review page `p65-hook.html` for his pick. The check round's open lines are fixed in the version he picks, before it locks.
  - 12 Oct 26: he found all of those hard to picture ("hard to visualize this as the hook or the intro"). An independent critique (`hook-critique.md`) named the defect (no line gave the viewer a picture) and offered three rebuilt hooks as storyboards (review page `p65-hookfix.html`).
  - Owner's pick, saved 12 Oct 26 02:50: **Rebuild 2, the telephone list.** His note, verbatim: "dont use the first frame as u suggested. use the white shirt paul like el reno. go ahead with 2. show me preview v1. let me know is zbook needs to stay alive."
  - Reading, the agent's: "preview v1" is a draft render of the hook and intro. Paul's first frame is El Reno's desk frame (white linen shirt), `episodes/ep4-el-reno/media/paul/inputs/paul-desk-frame.jpg` in the El Reno worktree, never a thumbnail image.
  - [ ] `edit_script.md` sections H1, T1, I1 written with a picture per line; the six picked hook lines fact-checked on page images before Paul's clip is made.
  - [ ] Preview v1 rendered (draft) and shown to the owner.
- [ ] Paul's on-camera lines; the book ad hinge inside the config window.
- [ ] `edit_script.md` section by section, fact-check fan-out beside the owner's read.

## Build (not started)
- [ ] Narration per locked section. [ ] Sourcing with a provenance row per file. [ ] Graphics from briefs carrying section 7a. [ ] Gates green. [ ] Draft render. [ ] Owner review. [ ] Full render, master, subtitles, metadata.
