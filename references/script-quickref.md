# script-quickref.md — the script writer's brief (owner rules to 27 Sep 26)

A script writer reads this file, `references/flag-words.md` and the episode research, nothing else. It condenses
the source file named in each section header; if a rule here and its source disagree, fix the source in the same
PR and say which one won.

## The hook (owner 27 Sep 26 — supersedes any looser hook rule below)
- **One sentence, 3–5 s.** Promise first: the payoff the title/thumbnail already made.
- **Never pause on a fact that contradicts the title/thumbnail.** Bad: "The weather service called it EF3." then a
  pause. Good (owner-approved): "The weather service changed it to EF5, four months after they called it EF3." The
  promised fact leads; the contradiction rides inside the same sentence.
- No fluff before it: sentence one IS the payoff (numbers first, then the specific image, then the question).
  Delete-test: cut sentence one — if the hook still works, it was fluff.
- No roadmap phrases ("one more thing before", "in the next twenty minutes") — they read as delay.
- Cold open (DESIGN.md): frame one is mid-action, never black. Narrator's first line starts at 0:00 — no broadcast,
  radio or archive audio in the hook (bad audio quality loses viewers before the hook finishes). Date/place popfig
  inside the first second. Every cut lands ON an audio event, never mid-sentence.

## Hook tail, intro, chapters (owner 27 Sep 26)
- **Tail, 5–15 s:** context plus ONE open curiosity gap — not the answer, not a list of what's coming.
- Then **INTRO** (~to 1:10 on a mini, longer on a doc): the full WHAT — stakes, roster, claim — delivered as
  information. Everything after the intro is WHY/HOW, which is what the viewer stays for.
- Then **CHAPTERS**: stakes order, not chronology. Every chapter changes what the viewer already understood; a
  chapter that only adds a subject ("Chapter 5: 1883") gets cut or rewritten.
- Channel post-mortem (27 Sep 26): toll and twist inside 20 s; no black hold, title card or disclaimer before 1:00;
  the line after the hook stays in the hook's scene; a hook claim holds for at least 60 s.

## Refill the cup — loop discipline (owner 27 Sep 26)
- When a loop pays off, open the next loop in the same breath. Never let the viewer's cup run empty.
- Tag every loop: `[loop L1 open]` when planted, `[loop L1 closes]` when paid. Every loop table row needs both.
- One episode loop (hook → final act), one loop per act (paid within 1–2 acts), one `cta-hinge` loop (see CTA
  hinge). Loops close honestly — a dropped loop is the #1 tell of stretched runtime. (`script-scaling.md`)

## Connect two points, don't merge them (owner 27 Sep 26)
- Build curiosity by holding two things next to each other without collapsing them into one claim — e.g. El Reno
  EF3 vs Enderlin EF5: state both, let the gap between them pull the viewer, never flatten into "they're the same."
- No dread or hate framing. Fear only as a sourced fact, never a narrator adjective (terrible, cruel, mercifully).

## The retention engine (every script) — `script-os.md`
Every 20–60 s: question → information → payoff → new question, chained with but/because/which means, never a list.
- Every beat in `edit_script.md` is an AV unit: what is said, what moves on screen, what the sound does, one row,
  one judgment. MGs get dedicated slots for information. (`script-framework.md` §1)
- One dominant question the whole script serves ("the viewer keeps watching to find out ___"), riding on one
  script concept: the one claim the film proves, strongest when it overturns a belief ("physics hid the iceberg",
  not "the Titanic"). The hook confirms it; every act proves part of it.
- Consequence before mechanism ("426 died, and the wave wasn't an earthquake" beats "a landslide tsunami occurs when…").
- Never spend curiosity early — one open question at a time.
- Escalating revelations: interesting → surprising → disturbing → enormous → personal → present-day → unresolved.
- 6–10 retention spikes per 15 min, each with a dedicated visual event (`[RS]` tag).
- Answer the dominant question in the last 30–60 s, then the CTA spine once. Never answer → like → subscribe → bye.
- Live-hazard videos carry a 60–90 s sourced debunk block at 60–75 % ("The problem with that story is…", then the
  measurement).
- Pre-TTS checks: per-minute scorecard 1–5 on new info · curiosity · stakes · visual change · payoff · exit hook,
  no two low minutes in a row; per-sentence cut filter (A story-critical, B curiosity, C context, D decoration: cut
  D, compress C); visual audit (every `[RS]` has a `[VE]`; tags `[VE] [RS] [Q] [PAY] [HOOK] [HUMAN]`); AVD pass at
  0:30, 1:30 … ("why would a viewer here stay another 60 s?" weak answer = rewrite).
- Pick ONE architecture (Detective / Countdown / Explanation-with-a-twist), hybrids normal; chapter card = Purpose ·
  Question · Reveal · Visual event · Exit hook, written before prose.

## Cadence lattice (per-minute invariants, hold at any runtime) — `script-scaling.md`
| Cadence | Rule |
|---|---|
| Rehook | real beat about every 45–60 s, an aim not a gate (CLAUDE.md "REAL clip", owner 4 Oct 26) |
| Micro-loop | curiosity gap every 30–45 s, phrasing varied |
| Info beat | every 6–10 s of narration |
| Pacing wave | alternate fast/slow, never >90 s one tempo |
| Act size | 3–6 min, self-similar (hook-in → escalate → payoff → hold/blackout) |
| Language | 4th-grader readable: short words, one idea per sentence |
| Spice | one clarifying footnote/analogy per beat that needs it, never filler |
Scale runtime by ADDING acts, never stretching beats. Each new act needs new material (a vignette + a
mechanism/analysis pair) and plants+pays a loop.

## Voice (45–75 US viewer) — `script-os.md` Voice rules + CLAUDE.md Voice
- Median sentence 12–18 words; 10–15% run 25–35 words as fact-chains (and/then/which); one ≤4-word kicker per 150
  words. Write the long sentence — TTS splits it at commas, don't pre-shorten for that reason.
- Sentence one of the SCRIPT is a number or date, unless the 27 Sep 26 hook rule above needs another opener (the hook rule wins).
- "You" = promise/stake only, ≤3 per 1,000 words after minute one. "We" = Americans, 2–3× per script. Never "I".
- One named researcher + institution per mechanism chapter; agencies named on screen; "nobody knows" in a source's mouth.
- Flat declaratives for record/mechanism; the future in three sourced paths, never the narrator's guess.
- A US state/region in the first 60 s; every foreign distance restated in feet/miles/°F/dollars + a US landmark.
- Seams are time-stamps or place-stamps, never "to understand X you have to understand Y."
- Keep technical terms, define in ≤12 words, reuse 3+ times. Every superlative gets a comparator and unit.
- One object per segment; one named victim (age, job, sourced quote) per tragedy.
- Close: fact + dated forward window, then the one signature line (DESIGN.md "Signature closing footnote", owner 4 Oct 26). No other aphorism, no mirrored callback.
- TTS-safe: spell out ALL dates/times/numbers in narration (except years, dollars), no paired dashes, sentences
  under 24 words per TTS chunk (write the long fact-chain; the TTS layer splits it at commas), probe homographs
  before respelling (`references/homographs.md`).

## Humanise pass — zero AI tells (run rules 2–14 line by line before TTS) — `humanise-rules.md`
- No painting the picture ("picture this", personified mountains/companies). No borrowed metaphors (icebergs,
  dominoes, perfect storms). No announcing the move ("here's the thing", "let's dive in", "make no mistake").
- Banned words: delve, furthermore, moreover, additionally, comprehensive, crucial/critical/essential as filler,
  robust, unprecedented, leverage, foster, seamless, elevate, navigate (figurative), game-changer, paradigm, tapestry,
  landscape (figurative), realm, testament, underscore (verb), pivotal, groundbreaking, transformative, multifaceted,
  intricate, nuanced, myriad, plethora, embark, journey (figurative), unlock, harness, empower, resonate, vibrant,
  bustling, nestled, meticulous, utilize, facilitate, implement (when "do" works).
- Banned phrases: a testament to, the landscape of, in today's world, in the ever-evolving, on the other hand, without
  further ado, it's worth noting, it's important to understand, in conclusion, to summarize, as we've discussed, at the
  end of the day, when it comes to, plays a crucial role, stands as a, serves as a, is a reminder that, the quiet
  [anything], what sounds like, what amounts to, in what can only be described as, some say, many experts believe,
  it's been reported (name the source or cut the claim).
- No em dashes, no rhetorical questions, no hedging/filler intensifiers (arguably, kind of, very, really).
- No banned sentence shapes: reveal-flip ("not X, it's Y"), question-then-answer fragment, anaphora run (3+
  sentences same opener), thesis opener ("this is the story of…"), summary tag ("That's the mechanism.").
- Specifics over abstractions: exact figures, never rounded, unless the number is a feat not the point (a rail
  car's weight) — then say it roughly ("about seventy thousand pounds").
- Strong verbs, active voice. Vary sentence length on purpose (short/medium/short, never 3 same length running).
- No summaries, recaps, soft exits, no "in this video." No fabricated quotes/stats/events — missing source = cut it.
- Rationed spoken devices (rules from ep-1974 probes): banned every script — "uh"/"um", self-corrections, doubled
  negatives, trailer fragments. Rationed devices (openers, asides, check-ins like "right?") max 3 per 20-min script,
  never twice in 3 minutes, never the same one in neighboring acts. New device = probe it in TTS first.

## Flag words — `references/flag-words.md`
Write with its alternatives from the first draft. `python3 scripts/flag_words.py episodes/<slug>` fails the script
on any hard word in narration, on-screen text or metadata.

## `[verify]` gate — writer tags, never resolves (owner order 27 Sep 26) — `script-scaling.md`
- Every fact not already in the pasted research gets `[verify: ...]` inline the moment it's written.
  That is the writer's ENTIRE job on this gate — no in-session eyeball, no resolving markers, no
  opening the six rule docs to double-check a fact. A parallel fact-check fan-out (several
  subagents, one slice each, run by the orchestrator, not the writer) resolves every marker to
  CONFIRMED (marker removed) / CORRECTED (line rewritten) / UNVERIFIED (line CUT — never softened
  to "reportedly") while the owner reads the draft.
- Hand off hook+intro as soon as it's written. Section lock (the 3-condition definition — markers
  resolved, owner's explicit approval, hook also needs the grader's pass) lives in
  `script-scaling.md` "Section lock — the ONE definition"; that section goes to TTS the moment
  IT locks, without waiting for later acts.
- Every audio-carrying insert is transcribed in full before cut selection; cut chosen at the transcript's peak.

## CTA hinge (must-keep every episode from ep4 on) — DESIGN.md "CTA contract"
- Window: CTA starts inside 85–95% of runtime, at a seam that doesn't interrupt a reveal.
- Hinge is scripted: the segment BEFORE the CTA ends on a tease (`cta-hinge` loop, ≤25 words); the segment AFTER
  opens with the payoff in its first sentence (first three words ideally, e.g. "He wrote a six.").
- Shape: hook > story > CTA > close. Never skipped, shortened, or moved to the outro.

## Title/thumbnail match — owner 27 Sep 26; dual-scope rule from `script-scaling.md`
- The hook and intro must say aloud what the title/thumbnail promised — a checkable fact, not an adjective.
- Every claim in the title or thumbnail text must appear in the script with a source.
- Dual-scope stats (episode total vs. one day) name their scope in the same sentence a viewer could misread it.

## Hand-back check
`flag_words.py` exit 0, and `word_budget.py` PASS at the shipping tempo (CLAUDE.md "Voice").
