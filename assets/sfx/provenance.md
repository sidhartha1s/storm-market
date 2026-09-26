# assets/sfx — shared SFX library

Reusable ambience/SFX beds. Optional per episode — the editor decides use, never mandated
(owner 2026-07-26). Gain rule: volumedetect source, compensate to mix target, verify layer
post-render (learnings/audio-tts.md 2026-07-23 item 7 — these sources run ~15dB quieter than the ACE music beds).

| File | Source | License | Notes |
|------|--------|---------|-------|
| 01_rain_street_medium.mp3 | Pixabay | Pixabay license | steady street rain, ep1 acts 1-2 |
| 02_wind_ominous_steady.mp3 | Pixabay | Pixabay license | low ominous wind, ep1 act 2-3 |
| 03_tornado_siren_waver.ogg | Wikimedia Commons | Public domain | civil-defense siren, waver mode |
| 03b_tornado_siren_constant.ogg | Wikimedia Commons | Public domain | siren, constant/alert mode |
| 04_distant_storm_rumble.mp3 | Pixabay | Pixabay license | distant thunder bed |
| 05_town_evening_crickets.mp3 | Pixabay | Pixabay license | quiet-town evening ambience |
| rain-loop.mp3 | self-made (acrossfade self-concat of 01) | derivative | 174s seamless loop |
| wind-loop.mp3 | self-made (acrossfade self-concat of 02) | derivative | 183s seamless loop — **BANNED as a bed (owner 2026-08-16, ep6 10:05: reads as unexplained "steady wind" under narration).** Kept only for transient gusts under on-screen wind. |

Detailed per-file source URLs: `episodes/ep1-joplin/media/provenance.csv` (sfx rows).
- sfx-rumble-bed-long.mp3 / sfx-swell.wav / sfx-boom.wav — ffmpeg-synthesized (anoisesrc brown/pink, sine 48Hz), 2026-08-12, ep5. Claim-free by construction.
- `owner-2026-08-13/` — owner's Pixabay pack (Pixabay license): civil-defense siren (= "siren"
  in owner vocabulary; ep6 hook `sfx-siren-hook.mp3` is its first 14.5s, mounted 0.144),
  risers, percussion hits, ocean waves (ep6 hook water bed), wind variants, industrial-pulse
  drone (freesound_community; ep6 act-6 bed `score-act6-drone-ext.mp3` = this drone
  self-crossfaded to 353s). Weewoo sirens (police/fire) live here too — never the "siren".
- Music scores (DeAPI-generated, claim-free): `deapi/README.md`. Music layer is default-ON
  since ep5/ep6 (one bed per act + swells + a riser into every act boundary, peaking WITH the
  narration line).
