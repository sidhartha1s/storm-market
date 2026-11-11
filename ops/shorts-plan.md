# Shorts lane and devq picks of 11 Nov 26: scope and checklist

Owner, 11 Nov 26: "figure out atleast 3-5 shorts or 1-2 high qualoty shorts per episode ... could be a big PR.
scope it and drive it e2e. run tests for the stuff on devq and this, as they are being merged. not words,
actual tests". Devq answers: `~/.claude/scratch/devq-retention/answers-storm-nov11.json` (saved 20:44).

Status is read from this file. A box is ticked only with the check that proved it.

## Done
- [x] PR #251 and #252 merged (merge commit: the branch held 7 merge commits, so it could not be rebased).
      `e2e.py` at 9c47ede52c before the merge: E2E PASS, 0 FAIL.
- [x] Research, 4 workers, sources dated: `~/.claude/scratch/shorts-research/{youtube,instagram,facebook,craft}.md`.
- [x] Inventory of what the repo already has for shorts (PLAN.md of 15 Sep, `shorts_lint.mjs`, `sh-hawaii-lowell-1`, PR #179).
- [x] 36 concepts with full narration, 4 per episode (1 flagship 60-90 s, 3 quick 20-40 s), every fact with an
      `edit_script.md` line: `~/.claude/scratch/shorts-research/concepts/E0*.md`. Not yet fact-read by me.

## What the research changes (against PLAN.md v1 of 15 Sep 26)
| Point | v1 | v2 | Source |
|---|---|---|---|
| Length | 14-40 s only | 20-40 s quick plus one 60-90 s flagship per film | Instagram median views by length, 9.77M reels, Jan-Jun 2026 (Socialinsider): 4,700 at 1-30 s, 10,374 at 45-60 s, 9,790 at 60-90 s |
| YouTube money | "earns nothing directly" | same, and from 1 Feb 2027 Shorts revenue share needs 10M Shorts views per 90 days | Team YouTube, 11 Aug 2026 |
| YouTube cadence | several a day | about 5 a month on the documentary channel | Metricool, 29 Jul 2026 (correlation): 8,789 views per long video at ~5 Shorts a month, 4,364 with none, back near that at 35+ |
| Cover | frame 1 is the thumbnail | same on YouTube (custom Shorts thumbnails are Partner Program, desktop only); Instagram cover is the centre 3:4 crop, so the cover line sits inside it | ppc.land 26 Jul 2026; hopperhq |
| Paul on screen | no Paul CTA | no Paul at all in shorts | Emplifi 19 Mar 2026: a visible person, reach -7.4 %; Instagram "AI-generated profile" label, 31 Aug 2026 |
| Loop close | required | dropped for anything over 7 s | Emplifi 19 Mar 2026 |
| Facebook | second platform | register interest in Content Monetization now (invite-only); views under 5 s and videos under 10 s do not pay | Meta newsroom 18 Mar 2026; Meta Creators blog 30 Mar 2026 |
| AI voice | not covered | tick Meta's "AI info" label on every reel (realistic AI voiceover is listed) | Meta Help, undated |
| Originality | PD footage rule | own narration and own graphics on every short; never a bare clip | YouTube Help post 1 Oct 2026; Meta 14 Jul 2025 |

Not supported by any data found: that cut-downs lose to purpose-written shorts, a words-per-minute target, a
"part 2" penalty. They stay as our own test, measured on the first ten posts.

## To do, in order
### PR `shorts-lane` (this branch)
- [ ] Fact-read the 36 concepts against the scripts; fix or drop; move to `episodes/<slug>/shorts/concepts.md`.
- [ ] `references/shorts/PLAN.md` v2: the table above, the two shapes, the word budgets, the safe zones.
- [ ] The seven gates that hardcode 1920x1080 read the composition size (`blank_scan`, `overlap_check`,
      `occlusion_check`, `graphics_qc`, `freeze_scan`, `beat_probe`, `stage_comp`); one test per gate that fails
      on a 1080x1920 fixture today.
- [ ] `shorts_lint.mjs` joins `run_gates.py` for `sh-` slugs; test.
- [ ] Phrase-caption builder from `words.json` (2-4 words, one highlight); test.
- [ ] Pilot: E04 "Two words, 25 minutes" voiced, built at 1080x1920, gates green, rendered, `stream_gate.py check`,
      frames opened by me. Then the owner watches it. No batch before his yes.
- [ ] After the yes: the other 35, in waves, between renders.
- [ ] Instagram account and Facebook monetization interest: owner steps (login).

### PR `devq-rules` (docs and records)
- [ ] Titles: E08 option 1, E09 option 2 recorded; E04 waits (devq says option 4, chat said option 1);
      E05 and E06 rechecked against the niche study.
- [ ] Script rules: under 24 words; open question allowed, with the retention rule the owner asked for
      (every section ends on an open loop); first sentence rule rechecked.
- [ ] Title and thumbnail block only the upload, in writing.

### PR `devq-gates`
- [ ] File-only gates may run beside a render; a memory-headroom test first (owner: "dont let it OOM").
- [ ] A render refuses to start unless the gates passed on that exact timeline; test.

### PR `devq-flow`
- [ ] Acts drafted while the hook waits; every hook option, title and thumbnail fact-checked and graded before the owner sees it.
- [ ] Captions, description, thumbnails and upload folder prepared while a draft waits.
- [ ] One standing page: every open pick for every episode, plus the content calendar (upload queue E04-E09,
      shorts queue, next films).

### PR `simplify-sweep`
- [ ] The 8 reuse findings of the simplify pass on #252.
