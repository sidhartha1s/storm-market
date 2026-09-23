# script-os.md — the retention engine + three narrative architectures (owner + GPT pass, 2026-09-11)

> Read order for any script: this file → `script-framework.md` (hook doctrine, AV one-product rule) →
> `humanise-rules.md` (the owner's 17 anti-AI narration rules + house additions; the pre-TTS humanise pass) →
> `script-scaling.md` (cadence math, loop table, fact-QC) → DESIGN.md (binding AV contract) →
> `mini-storms/FORMAT.md` "Retention architecture" (the 11 rules from Krakatau #4). This file is the layer above them:
> ONE engine every video runs on, THREE architectures a video picks from. It exists because our hooks and chapter
> exits were losing to GPT's on Krakatau #4: we announced structure, spent curiosity early, and chaptered by subject.

## Layer 1 — the retention engine (every video)
The loop, every 20–60 s: **question → information → payoff → new question.** Never spoken as a list; chained with
but / because / which means.

Seven non-negotiables:
1. **One dominant question.** Write it as "the viewer keeps watching to find out ______." Everything serves it.
   Krakatau #5: *could the mechanism that killed 426 people happen again, and would anyone see it coming?*
2. **Consequence before mechanism.** "426 died, and the wave was not caused by an earthquake" beats "a landslide
   tsunami occurs when…".
3. **Never spend curiosity early.** No "in the next 14 minutes…"; one open question at a time ("But where did the
   mountain go?").
4. **Every chapter changes the viewer's understanding** of what they already saw. A chapter that only adds a
   subject ("Chapter 5: 1883") is cut or rewritten ("this was not the first time this mountain turned a collapse
   into a wave").
5. **Escalating revelations:** interesting → surprising → disturbing → enormous → personal → present-day →
   unresolved. Information stakes climb; the biggest reveal completes in the final act.
6. **Retention spikes**, 6–10 per 15 min: one high-density fact each ("338 m to 110 m in one night"), every one with
   a dedicated visual event.
7. **Answer the dominant question in the last 30–60 s, then the CTA spine.** Never answer → like → subscribe →
   ebook → next → bye.

## Layer 2 — three architectures (pick one primary, optionally 30 % of a second)
- **A · Detective** (mysteries, missing evidence, "scientists found…"): hook (something does not add up) → setup →
  question → clue 1 → clue 2 → reconstruction → analogue → modern evidence → return to the mystery → verdict → action.
- **B · Countdown** (fast events: tsunami, hurricane landfall, dam failure): chronological clock; the question is
  "what happens next"; system failure and prevention come after impact.
- **C · Explanation with a twist** (misconceptions, "why does X happen"): common belief → real mechanism →
  complication → example → escalation → twist ("the thing you feared is not the dangerous part") → implication.
Hybrids are normal: Krakatau #5 = 70 % Detective + 30 % Countdown (the 9:03 → 9:33 clock inside the reconstruction).

## Chapter card (five fields, written before any prose)
**Purpose · Question · Reveal · Visual event · Exit hook.** Exit hooks come from eight types: question,
contradiction, escalation, reveal, time shift, location shift, consequence, present-day return.

## Pacing targets
20 / 40 / 90: by 0:20 why care, by 0:40 what exactly is the mystery, by 1:30 why you cannot leave. After that something
materially changes every 60–90 s (new evidence, place, number, person, mechanism, period, implication).

## Gates before TTS
- **Humanise pass** (`humanise-rules.md`, rules 2–14 line by line; diff kept in the episode folder). Owner's read (2026-09-13):
  distribution scans transcripts; strong packaging with an AI-scanning script gets few impressions.
- **Retention scorecard**, per minute, 1–5 on: new information · curiosity · stakes · visual change · payoff · exit
  hook. Rule: no two consecutive low minutes.
- **Cut filter**, per sentence: A story-critical · B curiosity-building · C context · D decoration. Cut D, compress C.
- **Visual audit**: every retention spike has a `[VE]`. Tags in the script: `[VE]` visual event, `[RS]` retention
  spike, `[Q]` question, `[PAY]` payoff, `[HOOK]` exit hook, `[HUMAN]` human consequence.
- **AVD pass**: at 0:30, 1:30 … 13:30 ask "why would a viewer here stay another 60 s?" Weak answer = rewrite.

## Voice rules for the 45–75 US viewer (audience audit 2026-09-14; evidence in references/teardowns/2026-09-14-audience-audit/)
1. **Pace is measured, never assumed** (CLAUDE.md Voice, `scripts/word_budget.py`). Slow only for numbers; pause after a death count, never before a reveal.
2. **Rhythm.** Median sentence 12–18 words; 10–15 % of sentences run 25–35 words as fact-chains joined by and / then /
   which; one kicker of ≤4 words per 150 words, never a flip. The 24-word cap is a TTS constraint, not a writing rule:
   write the long sentence, let the TTS layer split it at commas without changing a word (pocket-TTS mangles long
   single chunks, measured on Krakatau #4).
3. **Opening.** Sentence one is a number or a date. Inside 45 s one direct-address fact promise ("Inside twenty minutes
   you will know what a very strong El Niño did to your state the last two times"). No teaser, no "will history
   repeat", no comment ask before the closing CTA.
4. **Address.** "You" = promise or stake only, ≤3 per 1,000 words after minute one; "we" = Americans / the country 2–3×
   per script; replace half of "people" with the named group (retirees in mobile homes, night-shift nurses); never "I".
5. **Authority.** One named researcher + institution + venue per mechanism chapter ("X said, and this is a direct
   quote"); agencies named on screen (CPC, NWS, USGS, EIA); "nobody knows" always in a source's mouth; fear only as a
   sourced fact, never a narrator adjective (terrible, cruel, mercifully).
6. **Certainty split.** Flat declaratives for record and mechanism; the future in three paths ("If A, X. If B, Y. If C,
   Z. [Source] has not said which."). Hedge words only on numbers.
7. **Time anchoring.** Live videos say "as of this morning", stamp the weekday, and close on a dated watch-for ("The
   next CPC update lands Thursday; the number to look for is Niño-3.4"). "Still / already" ≤1.5 per 1,000 words.
8. **Place anchoring.** A US state or region in the first 60 s of every script (supersedes FORMAT rule 8's "second
   minute"); every foreign distance / height restated in a US landmark and in feet, miles, °F, dollars; ≤3 unfamiliar
   foreign place names per script. Ray: "Lituya is the one time you gave me feet, and that's the one part I remember."
9. **Transitions.** Seams are time-stamps or place-stamps ("At half past two that afternoon, in Mississippi"), never
   "to understand X you have to understand Y". Chapter-exit questions only when the answer is an open fact, ≤3 per
   documentary, ≤2 per mini; the engine's "question" is usually implied by a stamp or an unresolved fact.
10. **Debunk block.** Live-hazard videos carry a 60–90 s sourced debunk at 60–75 % ("The problem with that story
    is…", then the measurement).
11. **Vocabulary.** Keep the term, define it in ≤12 words, reuse it 3+ times; one plain-terms translation per
    number-dense minute; every superlative with comparator and unit ("1,720 feet, higher than the Empire State
    Building with its antenna").
12. **One object per segment**, never stacked; one named victim with age, job and a sourced quote per tragedy.
13. **Close.** Fact + dated forward window, then the CTA spine once. No aphorism, no mirrored callback, no sign-off line.
Owner decision 2026-09-14: humanise-rules.md stays as written. No thesis opener, no chapter-exit questions (rule 9
above is read as: seams are stamps; the open fact is stated, not asked). Ep2's hook at 1.5k views is not evidence.
## The philosophical change
Optimise for "what information does the viewer want right now, and when do we give it," not for "how do we make this
more engaging." Narration and visual event are written together, never narration first.

## News-lane pace: tempo BEFORE timing (owner order 2026-09-14)
Every lane runs Paul's clone at its tempo from `config.yaml channel.tempo` (pitch-preserving atempo). Order of
operations is fixed: (1) TTS the segment; (2) ffmpeg atempo on the wav; (3) transcribe the SPED wav to words.json;
(4) only then resolve cues, cards, popfigs and cuts against it. Never render at the slow pace and speed the video
afterwards; never time graphics against the pre-tempo words.json. `scripts/tts_episode.py` runs steps 1-3 in one pass. Above
1.13 the clone sounds rushed; write denser instead.
