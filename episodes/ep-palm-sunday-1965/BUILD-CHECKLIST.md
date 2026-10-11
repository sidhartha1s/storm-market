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
- [ ] Open check on the angle: the Tornado Autopsy video and the 1966 State Police film heard from their audio (helper p65-teardown). If either follows the warning desk to desk, the structure goes back to the owner.
- [ ] Title and thumbnail options (`references/packaging-rules.md`). Round 1 (11 Oct 26, 6 titles written to the reading-ease floor): the owner saved the page at 21:16 with no title ticked and said in chat "the titles suck actually ... maybe because u are trying to achieve the readability rating thing, maybe remove that. keep them punchy still." Round 2, same page `p65-pack.html`: 7 titles with no reading-ease gate. Rule change for the repo: PR #161, merge waits for his OK.
- [ ] Thumbnails. His saved note, 21:16: "gen all and show me. also, a version similar to critical latitude (idk if this is what u are referring to field notes thing)". One ChatGPT take each of `thumbs/t1-onground-poles-prompt.txt`, `thumbs/t2-fieldnotes-chain-prompt.txt` and `thumbs/t4-critlat-layout-prompt.txt` (Critical Latitude's own layout: presenter centred, line across the frame, words at the bottom); `thumbs/t3-noface-poles.jpg` is the no-face partner. Open until he picks one on the page.
- [ ] Hook and intro, graded by an independent reader, then the owner's sign-off.
- [ ] Paul's on-camera lines; the book ad hinge inside the config window.
- [ ] `edit_script.md` section by section, fact-check fan-out beside the owner's read.

## Build (not started)
- [ ] Narration per locked section. [ ] Sourcing with a provenance row per file. [ ] Graphics from briefs carrying section 7a. [ ] Gates green. [ ] Draft render. [ ] Owner review. [ ] Full render, master, subtitles, metadata.
