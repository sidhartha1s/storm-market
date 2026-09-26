# DeAPI music assets + generation recipe (owner-approved 2026-08-13)

Reusable AI-generated score tracks (claim-free — generated, not licensed) plus the exact
recipe to make more. First used on ep5 (California 2018). Keys: repo-root `.env`
(`DEAPI_KEY_1` / `DEAPI_KEY_2`, gitignored). Docs: https://docs.deapi.ai · full endpoint
reference: https://deapi.ai/llms.txt

## Tracks in this folder

| File | Prompt character | Duration | Used as |
|---|---|---|---|
| `score-act3-somber.mp3` | somber solo piano, sparse, mournful documentary underscore | 115s | ep5 act 3 (victim aftermath) |
| `score-act5-tension.mp3` | tense cinematic strings ostinato, rising dread, no drums | 270s | ep5 act 5 (the trap) — LOUD source (mean −11.5 dB), mount ~0.08 |
| `score-act6-close.mp3` | melancholic ambient piano + soft strings, grief and quiet hope | 300s | ep5 act 6 (close); `score-act6-ext.mp3` in ep5 media = self-crossfaded to 329.38s |
| `test-dark-ambient-60s.mp3` | dark ambient drone, low strings, wildfire tension | 60s | validation test, usable as a bed |
| `score-act1-darkambient.mp3` | dark ambient, sub-bass, slow dread (ep6 act 1 "the bowl") | 168s | ep6 act 1, mount ~0.2 |
| `score-act2-unease.mp3` | uneasy strings/pad, storm forming (ep6 act 2) | 170s | ep6 act 2 |
| `score-act3-urgent.mp3` | urgent pulsing strings, evacuation (ep6 act 3) | 215s | ep6 act 3 |
| `score-act4-stormhybrid.mp3` | hybrid orchestral/drone, landfall (ep6 act 4) | 195s | ep6 act 4 |

ep6 also reuses `score-act3-somber.mp3` (self-crossfaded to 243.5s as its act-7 bed) and
`score-act6-close.mp3` (close). The ep6 act-6 bed is NOT DeAPI — it is the owner-pack
industrial-pulse drone, loop-extended (see `../provenance.md`).

Total generation cost, all tracks: under **$0.02**.

## Recipe (validated end-to-end 2026-08-13)

```
POST https://api.deapi.ai/api/v2/audio/music        (multipart/form-data)
  caption          <= 300 chars, style prompt
  model            AceStep_1_5_Turbo   (Base variant allows steps 5-100, guidance 3-20)
  lyrics           "[Instrumental]"    (required, must not be empty)
  duration         10-300 (seconds)
  inference_steps  exactly 8 for Turbo (min == max == 8)
  guidance_scale   exactly 1 for Turbo (max_guidance = 1 — anything higher 422s)
  seed             -1
  format           mp3 (only format deployed models accept; wav/flac 422)
Auth: Authorization: Bearer <key>, Accept: application/json
Price check first: same endpoint + /price  (~$0.0009 per 60s)
Poll:  GET /api/v2/jobs/{request_id}   — NOT /requests/{id} (that 404s)
       status "done" -> download data.result_url
```

## Gotchas
- Generated tracks pad **~3s of silence at the tail** — trim or fade before mounting.
- For windows longer than 300s, self-crossfade the track (acrossfade d=4) — see ep5's
  `score-act6-ext.mp3` build in learnings/audio-tts.md.
- Measure `volumedetect` per track before choosing `data-volume`; outputs vary wildly
  (−11.5 to −32.8 dB mean across these four).
- Discover models at runtime: `GET /api/v2/models?filter[inference_types]=txt2music`.
  txt2audio on DeAPI = TTS models only, NOT sound effects — SFX come from the owner
  Pixabay pack (`assets/sfx/owner-2026-08-13/`) or ffmpeg synthesis.
