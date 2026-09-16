# edit_script.md — ms-dujuan-silver-week · "Typhoon No. 25 Dujuan Is Forming, Aimed at Japan's Biggest Holiday in 11 Years" (Format C, 16 Sep 26)

> Wave 3 U1, first video of the Dujuan daily series (ops/wave3/dujuan/PLAN.md). Angle = ideas-r3.md #1, Silver Week
> Collision, built to be honest under both open branches: the storm curving into Kanto, or sliding past offshore.
> Present-tense rolling update as of JMA 16 Sep 19:10 JST (TC2630, still an unnamed tropical depression) and JTWC
> warning 04, 16/09Z. Every number sourced to facts-16sep.md / fact-pack-16sep.md; nothing carries a [verify] tag.
> Numbers spelled out for TTS except years and dollar figures (humanise-rules.md); sentences under 24 words;
> wind spoken in mph, shown in km/h on screen; `[src]` per fact group. Target ≥1,350 words at 1.10 tempo (8-min
> floor); measured at 1,374 words / ≈8:41 at the ms-kauai-lowell-day2 blended rate (158 wpm). Paul's CTA mounted
> at the end of B3, ≈3:07 (36% in), the natural pause right after the quote card.

## Spec
- Slug `ms-dujuan-silver-week`. Voice: pocket-TTS Pharaoh → atempo 1.10 → transcribe the sped wav → cues from that
  words.json. Probe-TTS "Dujuan" before final synthesis; if pocket-TTS doesn't land near "doo-jwan," respell the
  narration token phonetically and re-probe (storm-market homograph rule).
- Spoken names: Guam, Mariana Islands, Japan, Tokyo, Kanto, Nagoya, Yokosuka, Yokota, Dujuan.
  On screen only (not spoken): Ogasawara, Nozomi, Costa Serena.
- Pool: `library/mini-storms/dujuan-2026/` (built once in the main checkout, reused by every video in the series,
  per ops/wave3/dujuan/PLAN.md). Footage: NOAA/CIRA Himawari loops, JTWC/US Navy graphics, JMA bulletin graphics
  (credited), DVIDS Yokosuka/Yokota b-roll if available, short narrated broadcaster pulls (NHK/TBS/Reuters),
  Pexels/Pixabay Tokyo/Shinkansen/airport b-roll. No storm-chaser footage.
- MG: opening glassmorphic stat-card push + track map draw-on (B1/B2); meteorology explainer chip row (B2);
  four-checkpoint forecast track map (B3); quote card (B3); JTWC overlay + two labelled branch tracks (B4);
  Silver Week calendar + Nozomi/Asian Games chips (B5); US-bases Kanto map (B6); JMA-vs-NHC scale ladder graphic
  (B7); tracking/benchmark card (B8).
- Close: B8 ends on both open threads (track, strength) still unresolved; B9 is the single soft comment +
  subscribe line, tied to the real trigger event (Japan naming the storm), not an invented clock time.
- CTA: Paul's ebook CTA mounts at the end of B3 (≈3:07, 36% in), right after the "East of Japan" quote card lands
  — the first natural pause in the meteorology block, ahead of the Silver Week pivot. 0.5 s dip in/out, film
  layer off, Paul circle hidden during the quote card per the presenter-circle spec.

## Sources
- f1 JMA live feed, TC2630 (targetTc.json → specifications.json), fetched 16 Sep 2026, issue time 16 Sep 19:10
  JST: position, category (still TD), current intensity, and the four-point forecast track (+12h/+45h/+93h/+117h).
  https://www.jma.go.jp/bosai/typhoon/data/targetTc.json — facts-16sep.md §6.
- f2 JMA typhoon intensity scale (Strong / Very Strong / Violent Typhoon, Severe Tropical Storm band) and the
  10-minute-vs-1-minute sustained-wind conversion note, via Wikipedia "Tropical cyclone scales" citing RSMC
  Tokyo, fetched 16 Sep 2026 — facts-16sep.md §4.
- f3 Silver Week 2026 dates (19–23 Sep), first full 5-day Silver Week in 11 years (prior 2015, next 2032), 2026
  national-holiday count (16→17), Nozomi Shinkansen fully reserved-seat 18–23 Sep, peak congestion windows:
  Metropolis Japan, "Silver Week 2026 in Japan," 10 Sep 2026 — facts-16sep.md §2.
- f4 US Forces Japan: Fleet Activities Yokosuka (7th Fleet HQ) and Yokota Air Base (USFJ HQ) as established Kanto
  installations; ~55,000 active-duty servicemembers at 15 bases Japan-wide; TCCOR readiness system (mechanism,
  not Dujuan-specific — no TCCOR declared yet, storm still unnamed): Wikipedia "United States Forces Japan";
  Stripes Japan TCCOR precedent — facts-16sep.md §3.
- f5 Kanto typhoon benchmarks: Typhoon Hagibis 2019 (139 dead, 3 missing, US$17.3B damage); Typhoon Faxai 2019
  (934,000 households without power, 390,000+ evacuation calls); Typhoon Ampil 2024 (4 injured Kanto-wide,
  minimal Tokyo damage): Wikipedia "Typhoon Hagibis" / "Typhoon Faxai" / "Typhoon Ampil (2024)" — facts-16sep.md §5.
- f6 Japan drew 42.7 million international visitors in 2025, its highest total on record: nippon.com, 23 Jan
  2026 — facts-16sep.md §3.
- f7 2026 Asian Games Aichi-Nagoya: opens 19 Sep, 46 nations, athletes' village includes the cruise ship Costa
  Serena docked in Nagoya housing at least 4,000 participants: Wikipedia "2026 Asian Games"; Marine Insight,
  16 Sep 2026 — facts-16sep.md §1.
- g1 JTWC TD 24W warning 04, 16/0900Z: position (277 nm ENE of Guam), current intensity (30 kt, gusts 40 kt),
  12/24/36h forecast (40/50/50 kt) with the turn toward Japan, peak forecast (65 kt, 19–21 Sep), closest pass
  ~270 km (168 mi) east of Tokyo on 21 Sep, SST 29–30°C, low shear, dry-air brake to the NW, 14 ft seas, GDACS
  green: fact-pack-16sep.md.
