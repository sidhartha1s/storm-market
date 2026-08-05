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
| Info beat | something NEW lands every 2–3s on graphics; every 6–10s in narration | info density IS the retention; fluff is seasoning (≤20–30%) |
| Pacing wave | alternate fast (2–4s cuts) and slow (holds 3–10s); never >90s of one tempo | monotony reads as length |
| Act size | 3–6 min. An act = a mini-episode: hook-in (≤15s) → escalate → payoff → hold/blackout | the self-similar unit that scaling adds |
| Blackout | 2–3s black between acts (hard cut in/out) | the documentary breath |
| Emotion | stats mid-act; emotion banked at act ends; the heaviest vignette at the episode's final third | teardown-verified pattern |
| TTS breath | holds/voids are WRITTEN pauses — a `hold` segment is a scripted breath, not dead air; full stops = hard breaks | pacing lives in the script, not post |
| Graphic trigger | spatial claim → map · mechanism → animated diagram · number cluster → stat card · reveal/correction → dedicated graphic | "show, don't make the viewer look at stuff" |

## The open-loop registry (the spine of scaling)

Every episode keeps a LOOP TABLE in its edit_script:
- **1 episode loop**: planted in the hook, paid in the final act. (ep5: "fire is not supposed to do this" → "the warnings were there.")
- **1 loop per act**: planted in that act, paid within 1–2 acts. Each act ALSO pays off one earlier loop — an act that only plants is a tease; an act that only pays is a dead end.
- Loops close honestly. A dropped loop is the #1 tell of stretched runtime (competitor teardown: the "radar could warn us someday" tease that never resolves).

## The scaling recipe (x → 2x → 3x…)

1. **Never lengthen an act past 6 min.** More runtime = more acts.
2. Each added act needs its own **new material**: a vignette + a mechanism/analysis pair (info first, spice second). No new material → don't add the act → the honest runtime is shorter.
3. Re-run the loop table: every new act plants one, pays one.
4. Cadences unchanged. A 500x script is just more 3–6 min mini-episodes on the same lattice,
   arranged so stakes DESCEND into the close (no recap, no outro summary).
5. Info:fluff at 35 min ≈ 70–80% info. Fluff = sensory texture, dwell, foreshadow — earns its
   seat only where a beat needs air. Never force it.

## Act-planner template (fill per act, per episode — JSON for planning, prose for writing)

```json
{
  "act": "A2-pyrotornadogenesis",
  "minutes": 5.5,
  "words": 800,
  "job": "the science wedge — fire builds its own storm, then a tornado",
  "hook_in": "the air itself had changed",
  "plants_loop": "no warning existed for this",
  "pays_loop": "what crossed the river (A1)",
  "rehooks": ["CAL FIRE vortex reprise @~2min", "radar triangulation graphic @~4min"],
  "emotion_bank": "low — this act is info; emotion is A3's job",
  "tempo": "slow-build -> fast reveal -> slow hold",
  "graphics": ["g-pyrocb", "g-vortex"],
  "exit": "hold 3s on the ice-topped plume, blackout"
}
```

## Insert-transcription rule (owner order 2026-08-05)

Every `insert` (audio-carrying clip) is **transcribed in full (faster-whisper) BEFORE cut
selection**. The cut is chosen from the transcript at the action/emotion peak; the chosen
excerpt (~10 words) + full transcript path are logged in the edit script AND provenance.csv.
Never cut an insert by eyeballing the waveform.
