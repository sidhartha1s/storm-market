# script-scaling.md — the retention lattice (owner-ordered 2026-08-05, ep5)

> The problem this solves: a solid short script scores 10/10 because of its *cadences*, not its
> length. Stretch the beats and it dies. The fix: runtime scales by ADDING self-similar units
> (acts), never by stretching any beat. All cadences below are **per-minute invariants** — they
> hold identically at 15, 35, or 90 minutes. This is a prompt/note for the writing session, not
> an enforcement script (CLAUDE.md: judgment stays with the model).

## The invariants (constant at ANY runtime)

| Cadence | Rule | Why |
|---|---|---|
| Rehook | a REAL beat every 45–60s: broadcast/PD clip, audio insert, stat spike, or a loop opening | audience 40–70+ came for the real thing |
| Micro-loop | a curiosity gap every 30–45s of narration ("what crossed the river that night was not the fire anyone had been fighting") — phrasing varied, never formulaic | keeps the next 30s pre-sold |
| Info beat | every 6–10s in narration; graphics reveal on the spoken word and drift while they wait (`references/mg-quickref.md` "Motion and exits") | info density IS the retention; fluff is seasoning (≤20–30%) |
| Pacing wave | alternate fast (2–4s cuts) and slow (holds 3–10s); never >90s of one tempo | monotony reads as length |
| Act size | 3–6 min. An act = a mini-episode: hook-in (≤15s) → escalate → payoff → hold/blackout | the self-similar unit that scaling adds |
| Blackout | 2–3s black between acts (hard cut in/out) | the documentary breath |
| Emotion | stats mid-act; emotion banked at act ends; the heaviest vignette at the episode's final third | teardown-verified pattern |
| TTS breath | holds/voids are WRITTEN pauses — a `hold` segment is a scripted breath, not dead air; full stops = hard breaks | pacing lives in the script, not post |
| Language | **4th-grader readable** (owner 2026-08-05): short words, concrete pictures, one idea per sentence; emotion comes from facts and rhythm, never from vocabulary | TTS syncs clean; the shipped eps' register |
| Graphic trigger | spatial claim → map · mechanism → animated diagram · number cluster → stat card · reveal/correction → dedicated graphic | "show, don't make the viewer look at stuff" |

## The open-loop registry (the spine of scaling)

Every episode keeps a LOOP TABLE in its edit_script:
- **1 episode loop**: planted in the hook, paid in the final act. (ep5: "fire is not supposed to do this" → "the warnings were there.")
- **1 loop per act**: planted in that act, paid within 1–2 acts. Each act ALSO pays off one earlier loop — an act that only plants is a tease; an act that only pays is a dead end.
- **1 CTA hinge (REQUIRED, owner 2026-08-30 — DESIGN.md "CTA contract")**: a tease→payoff pair
  whose tease ends the segment inside the `config.yaml channel.cta` window (85–95%, owner 23 Sep 26) and whose payoff opens the next segment's first
  sentence; the 15.1s CTA sits between them. Listed in the loop table as `cta-hinge` with the two
  segment ids. If no honest payoff falls in that band, restructure the acts — the CTA never moves.
- Loops close honestly. A dropped loop is the #1 tell of stretched runtime (competitor teardown: the "radar could warn us someday" tease that never resolves).

## The scaling recipe (x → 2x → 3x…)

1. **Never lengthen an act past 6 min.** More runtime = more acts. Runtime arithmetic = narration + blackouts + the 15.1s CTA + its two 1.0s dips.
2. Each added act needs its own **new material**: a vignette + a mechanism/analysis pair (info first, spice second). No new material → don't add the act → the honest runtime is shorter.
3. Re-run the loop table: every new act plants one, pays one.
4. Cadences unchanged. A 500x script is just more 3–6 min mini-episodes on the same lattice,
   arranged so stakes DESCEND into the close (no recap, no outro summary).
5. **Spice ≠ fluff (owner definition, 2026-08-05):** spice is the clarifying footnote — the one
   example that makes a number felt ("a football field per second"), the one analogy that makes a
   mechanism click ("a skater pulling in her arms"), the one sensory detail that makes a place
   real ("a sunrise behind the hospital at ten PM"). Salt on the food: adds clarity or relatability,
   never length for its own sake. At 35 min: 70–80% info, spice where a beat needs it. Don't force it.

## Act brief (text-only — one short block per act, written before the act's prose)

No JSON, no schema, nothing parseable — a brief is six plain lines a writer reads and follows.
Format-proof by construction: there is nothing to fail midrun.

> **ACT — [name] · [minutes] min · ~[words] words**
> **Job:** the one thing this act must accomplish.
> **In / out:** the hook-in line idea → the exit beat (hold/blackout).
> **Loops:** plants [x] · pays [y].
> **CTA hinge:** (only in the act that carries it) tease = last line of [seg] → CTA → payoff = first line of [seg].
> **Rehooks:** the 2–3 real beats (insert / graphic reveal / stat spike) and roughly where.
> **Tempo + emotion:** the pacing wave shape, and how much emotion this act banks (info acts bank little — that's the next act's job).

## Scaling by agents (orchestrator mode — for very long scripts)

When one sitting can't hold the whole script (fatigue is how structure gets missed):
1. The ORCHESTRATOR (main session) writes ALL act briefs first — the full loop table, word
   allotments, and cadence sheet. Structure is decided once, globally, before any prose.
2. One writer agent per act (or per arc of 2–3 acts). Each gets: this file + its act brief +
   the loop table + the previous act's closing lines (for the seam). It writes prose only.
3. The orchestrator splices, then re-walks the seams itself: every loop planted got paid,
   rehook cadence unbroken across seams, no phrase or image repeated across acts, transitions
   rewritten by hand where two agents' voices meet.
4. All of it is text briefs and judgment — no code, no schema, nothing that can break midrun.
   A missing brief line degrades to "writer uses judgment," never to a crash.

## Script fact-QC layer (owner order 2026-08-05 — runs BEFORE TTS, zero cost)

Two passes, both pre-TTS, both free:
1. **In-session eyeball:** re-walk every number, name, date, distance, and death count in the
   draft against the research reports. Arithmetic too (day gaps, per-count divisions). Fix on
   the spot; anything unsourced gets `[verify]` or gets cut.
2. **Verification agents' verdicts applied:** every `[verify]`-gated line resolves to
   CONFIRMED (marker removed) / CORRECTED (line rewritten) / UNVERIFIED (line CUT — the
   conditional-fact rule: drop entirely, never soften into "reportedly").
Standing sub-rules: dual-scope stats name their scope in the same sentence; quotes carry their
attribution; TTS does not run until the script has zero open `[verify]` markers.

## Insert-transcription rule (owner order 2026-08-05)

Every `insert` (audio-carrying clip) is **transcribed in full (faster-whisper) BEFORE cut
selection**. The cut is chosen from the transcript at the action/emotion peak; the chosen
excerpt (~10 words) + full transcript path are logged in the edit script AND provenance.csv.
Never cut an insert by eyeballing the waveform.
