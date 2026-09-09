# edit_script.md — ms-krakatoa-1883 · "Krakatoa Just Erupted. In 1883 It Killed 36,000 People. Here Is What Is Different Now."

> mini-storms #3 (owner go 2026-09-09). Same segment format as ms-elnino-texas. Numbers spelled out for TTS;
> every fact carries `[src: N]`. Delivered pace ≈ 158 wpm. Target 9:20, ~1,370 narration words + 16 s CTA.

## Spec
- Slug `ms-krakatoa-1883`. Voice: pocket-TTS Pharaoh, native pace. CTA: `config.yaml channel.cta` (v5), after C4, 1.0 s dips.
- Visual grammar: FORMAT.md; popfig with local scrim; news bug; no chapter cards; presenter circle phase 2 (talk gated
  on narration spans, hidden in hook / CTA / close). Data-feed holds: BMKG/CIRA satellite ash loop (C1),
  MAGMA Indonesia seismogram or tiltmeter plot (C6).
- Pool: `library/mini-storms/krakatau-2026/` (new; provenance.csv rows travel with the files).
- Interaction beats (cap 3 incl. END CTA): I1-S2 where-are-you-watching (verbatim, TTS "reed"); C5-S1 think-it-yourself
  guess; Z1-S1 END CTA spine.

## Sources
1. PVMBG / MAGMA Indonesia via Antara, "PVMBG continues monitoring Anak Krakatau after eruption ends" (continuous
   eruption 4 Sep 23:07 → 6 Sep 00:04 WIB, 25 h; Level III; 3 km; tiltmeter at Tanjung rising since early August;
   quote from PVMBG head Siti Sumilah Rita Susilawati; 209 flights cancelled at Soekarno-Hatta).
   https://en.antaranews.com/news/430144/pvmbg-continues-monitoring-anak-krakatau-after-eruption-ends
2. Databoks / MAGMA Indonesia daily eruption bulletins 8–9 Sep 2026 (eruptions 8 Sep morning and afternoon, 9 Sep
   00:47 WIB seismic-only, amplitude 51 mm, 28 s, sixth in a week; Level III since 2 July 2026).
   https://databoks.katadata.co.id/en/demographics/statistics/21e7c960349ba0f/mount-anak-krakatau-erupts-again-tonight-wednesday-9-september-2026
3. BMKG SIGMET and satellite notes via nine145 verified update 7–8 Sep (ash surface to 15,000 ft moving west 15 kt;
   39 SIGMETs; eight airports temporarily affected; no sea-level anomaly through 6 Sep 07:30; no confirmed deaths).
   https://nine145.com/2026/09/08/anak-krakatau-eruption-september-2026-verified-update/
4. USGS / Smithsonian GVP, Krakatau 1883 (26–27 Aug 1883; ~36,000 dead, official Dutch count 36,417; explosion heard
   ~4,800 km away at Rodrigues; pressure wave recorded circling the globe seven times on barographs; ~20 km³ ejected;
   global temperatures down ~0.4 °C the following year). https://volcano.si.edu/volcano.cfm?vn=262000
5. Royal Society, "The Eruption of Krakatoa and Subsequent Phenomena" (1888) — barometric traces, sunsets.
   https://archive.org/details/eruptionofkrakat00roya
6. Science Advances 2020, Grilli et al., "The 22 December 2018 tsunami from flank collapse of Anak Krakatau volcano
   during eruption" (landslide <0.2 km³; no strong short-period seismic waves, so no precursory warning; 437 dead;
   coastal wave heights 3.75–6.6 m, run-ups to 13 m; summit 338 m → 110 m). https://www.science.org/doi/10.1126/sciadv.aaz1377
7. Walter et al. 2019, Nature Communications, "Complex hazard cascade culminating in the Anak Krakatau sector collapse"
   (collapse ~21:03 local, waves at the coasts within about half an hour, at night). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6773710/
8. Smithsonian GVP, Anak Krakatau history (emerged 1927, island above the sea by 1930; PVMBG four-level alert scale:
   Level I Normal, II Waspada, III Siaga, IV Awas). https://volcano.si.edu/volcano.cfm?vn=262000
9. British Airways Flight 9, 24 June 1982, Galunggung ash cloud: all four engines flamed out, restarted after descent.
   (ICAO / NASA case study.) https://www.nasa.gov/wp-content/uploads/2020/04/1982-galunggung-eruption.pdf
10. Tambora 1815 = the "year without a summer" (1816), not Krakatoa. NOAA Climate.gov. https://www.climate.gov/news-features/blogs/enso/year-without-summer

---

## HOOK (0:00–0:08)

### H1-S1 — narration
> The volcano that killed thirty six thousand people in a single morning has erupted six times this week, and eight airports have already lost flights.

Visual: Sep 2026 plume (PVMBG/BNPB still, push in); popfig "36,000 DEAD" then "6 ERUPTIONS · 1 WEEK". [src: 2, 3, 4]

## INTRO (0:08–1:05)

> TTS note: the owner's phrase is "Comment down where you are watching this from. I read all the comments." — spelled "reed" in the narration line only.

### I1-S1 — narration
> Krakatoa. In August eighteen eighty three, this mountain blew twenty cubic kilometres of rock into the sky. The sound was heard three thousand miles away. The pressure wave went around the planet seven times. And the sea it threw at the coast of Java and Sumatra killed more than thirty six thousand people before breakfast.

Visual: 1883 lithograph (Parker & Coward) slow push; Sunda Strait map; popfigs "20 KM³", "HEARD 3,000 MI", "7 TIMES AROUND". [src: 4, 5]

### I1-S2 — narration
> Its child, Anak Krakatau, has been erupting since the fourth of September. And here is the thing almost every clip you have seen this week gets wrong. The eruption everyone is filming is not the danger. The danger is the one nobody filmed, on a December night in twenty eighteen. Stay with this, because by the end you will know what the mountain is doing right now, what twenty eighteen proved, and exactly what to watch for this week. Comment down where you are watching this from. I reed all the comments.

Visual: bystander plume clips credited, then black-night ocean; chip "THE ONE NOBODY FILMED"; popfig "DEC 22, 2018". [src: 1, 6]

## CH1 — THIS WEEK (1:05–1:55)

### C1-S1 — narration
> The facts on the record first. At seven minutes past eleven on the night of September fourth, Anak Krakatau began an eruption that did not stop for twenty five hours. Indonesia's volcano agency, PVMBG, holds it at Level Three, the second highest alert, where it has sat since July. Nobody is allowed within three kilometres of the crater. Since the long eruption ended there have been more. Two on Monday. Another just after midnight on Wednesday, picked up only on the seismographs, twenty eight seconds long. Six eruptions in one week. The head of the agency put it plainly: volcanic activity remains high, and another eruption in the near future remains possible.

Visual: DATA-FEED HOLD, BMKG/CIRA satellite ash loop labelled; timeline chip Sep 4 → Sep 9; popfigs "25 HOURS", "LEVEL III", "3 KM", "6 ERUPTIONS"; glass quote card for the PVMBG line. [src: 1, 2]

## CH2 — WHY FLIGHTS STOP (1:55–2:45)

### C2-S1 — narration
> So why do airports close for a cloud? Because volcanic ash is not smoke. It is pulverised glass. In nineteen eighty two a British Airways jumbo flew into an ash cloud over Java at night, and all four engines flamed out. The crew glided for thirteen minutes before the engines relit. Aviation has never forgotten it. This week Indonesia's weather agency issued thirty nine ash warnings to pilots, with ash reported from the surface up to fifteen thousand feet drifting west. Eight airports were affected, and Jakarta's main airport alone cancelled more than two hundred flights. Which raises the question that actually matters: how bad can this get?

Visual: departure board stock, jet engine cutaway still, BA009 route map; popfigs "PULVERISED GLASS", "4 ENGINES OUT", "39 WARNINGS", "8 AIRPORTS", "209 CANCELLED". [src: 3, 9, 1]

## CH3 — 1883 (2:45–3:45)

### C3-S1 — narration
> To answer that, go back to the morning of August twenty seventh, eighteen eighty three. Four explosions. The biggest, at two minutes past ten, tore the island apart. On the island of Rodrigues, three thousand miles across the Indian Ocean, a police chief wrote down that he heard the roar of heavy guns. Barometers in Britain twitched as the pressure wave passed over them, and kept twitching every thirty six hours as it went around the world again. The sky glowed red at sunset for months. The planet cooled by about half a degree for a year. But the killer was not the ash, and it was not the sound. It was the sea. Walls of water thirty metres high hit the coasts of the strait and erased one hundred and sixty five villages.

Visual: 1883 lithographs (Parker & Coward), Royal Society barograph trace push, red-sunset painting, Sunda Strait map with wave rings; popfigs "AUG 27, 1883", "10:02 AM", "HEARD 3,000 MI", "−0.4 °C", "30 M WAVES", "165 VILLAGES". [src: 4, 5]

## CH4 — THE CHILD (3:45–4:30)

### C4-S1 — narration
> The mountain did not stay dead. In nineteen twenty seven, fishermen saw steam rising from the sea where the old island had been. By nineteen thirty a new cone stood above the waves. They called it Anak Krakatau, the child of Krakatoa. And the child grew fast, a few metres a year, until by twenty eighteen it stood three hundred and thirty eight metres tall. That number matters. Because on the twenty second of December twenty eighteen, most of it fell into the sea.

Visual: NASA/USGS satellite time series of Anak growth, before/after 2018; popfigs "1927", "338 M", "DEC 22, 2018". Connective into the CTA dip. [src: 6, 8]

## CTA — `assets/cta/paul-storm-ready-v5-sep6.mp4`, dips 1.0 s (4:30–4:46). Presenter circle hidden.

## CH5 — DECEMBER 22, 2018 (4:46–5:50)

### C5-S1 — narration
> It was a Saturday night, two days before Christmas. Anak Krakatau had been erupting for months, and nobody on the beaches was worried, because the tsunami warning system in Indonesia listens for earthquakes. A collapsing volcano does not make one. Just after nine in the evening, the south west flank of the mountain slid into the strait. Less than a fifth of a cubic kilometre of rock. That was enough. Before I tell you what the tide gauges did, guess how long the coast had between the collapse and the first wave. An hour? Two? The answer is under half an hour, in the dark, with no siren. Waves between four and seven metres, running up to thirteen in places, hit beach resorts and a concert in full swing. Four hundred and thirty seven people died. The mountain itself lost two thirds of its height overnight, from three hundred and thirty eight metres to one hundred and ten.

Visual: BNPB/BMKG aftermath stills, tide-gauge plot from the Science Advances paper (credited), night ocean, before/after summit graphic; popfigs "NO EARTHQUAKE", "0.2 KM³", "UNDER 30 MIN", "437 DEAD", "338 → 110 M". [src: 6, 7]

## CH6 — WHAT THEY WATCH NOW (5:50–6:45)

### C6-S1 — narration
> So what are the scientists actually watching this week? Not the plume. Three things. First, the shape of the mountain, because the collapse of twenty eighteen came from a cone that had grown too steep too fast, and the child has been rebuilding ever since. Second, the tremor, the continuous shaking that tells them how much magma is moving. Third, the tilt. The observatory has a tiltmeter on the flank, and its readings at the Tanjung station have been rising since the start of August. Rising tilt means the mountain is inflating. It does not mean a collapse is coming, but it is exactly the signal they did not have eyes on in twenty eighteen. All of this is public. The MAGMA Indonesia page posts every eruption within minutes.

Visual: DATA-FEED HOLD, MAGMA Indonesia seismogram or tiltmeter plot labelled; collapse-geometry diagram; popfigs "SHAPE", "TREMOR", "TILT ↑ SINCE AUGUST". [src: 1, 6]

## CH7 — WHO IS AT RISK (6:45–7:40)

### C7-S1 — narration
> Who is actually at risk. The coasts of the Sunda Strait first: Banten on the Java side, Lampung on the Sumatra side. Those are the beaches twenty eighteen hit, and they are the only places where a Krakatau tsunami can reach. Jakarta and the cities of West Java get the ash, which is a breathing and a flight problem, not a tsunami problem. And then there are the travellers. Bali has been fine, but flights route through Jakarta, and eight airports have already had ash closures this week. If you are flying into Java in the next two weeks, your risk is a cancelled connection, not a wave.

Visual: Sunda Strait map with the two coasts lit in narration order, then Jakarta ash shading, then a Java/Bali flight-route map; popfigs "BANTEN", "LAMPUNG", "JAKARTA · ASH", "BALI · FLIGHTS". [src: 3, 6]

## CH8 — WHAT IS NOT HAPPENING (7:40–8:50)

### C8-S1 — narration
> Now the honest part. Nobody is forecasting an eighteen eighty three. That eruption came from a mountain twenty times the size of the child, and the child does not hold that much magma. The ash is not a health emergency for anyone outside Indonesia; it is not crossing an ocean. The tsunami risk is real but local, a few hundred kilometres of coast, and the weather agency has seen no sea-level anomaly this week. And the year without a summer that people keep quoting was Tambora in eighteen fifteen, a different volcano, a different island, thirty times bigger.

Visual: split NOT / YES card; Tambora vs Krakatoa size comparison graphic; popfigs "NOT 1883", "NOT A GLOBAL EVENT", "TSUNAMI RISK · LOCAL", "TAMBORA, NOT KRAKATOA". [src: 3, 4, 10]

### C8-S2 — narration
> So what should you actually do. If you are on the Sunda Strait coast: know that the warning for this mountain will not be a siren, it will be the sea pulling back or the sound of the collapse, and you move uphill on your own. If you are booked to Jakarta this month: check your airline the night before, not at the gate. And if you are anywhere else, watch the tilt, not the plume. The mountain will tell the instruments before it tells the cameras.

Visual: 3-row checklist card over footage; popfigs "1 UPHILL, NO SIREN", "2 CHECK THE NIGHT BEFORE", "3 WATCH THE TILT". [src: 1, 6]

## CLOSE (8:50–9:20)

### Z1-S1 — narration
> The child of Krakatoa is awake, and the instruments are watching it more closely than any mountain on Earth. If you enjoyed this video, like and subscribe for more. I truly appreciate it. Comment the one thing you would want to know if you were on that coast tonight, and I will answer it in the next one.

Visual: outro brand card; end screen pointer to the El Niño videos. Presenter circle hidden.
