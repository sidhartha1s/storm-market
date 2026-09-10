# edit_script.md — ms-krakatau-sirens · "Krakatoa 2026: Why the Sirens Will Not Save Anyone"

> mini-storms #4 (owner go 2026-09-10 23:45, plan self-approved). Same segment format as ms-krakatoa-1883. Numbers spelled
> out for TTS; every fact carries `[src: N]`; sentences under 24 words. Delivered pace ≈ 158 wpm. Target 13:50, ~2,130 words + 16 s CTA.

## Spec
- Slug `ms-krakatau-sirens`. Voice: pocket-TTS Pharaoh, native pace. CTA: `config.yaml channel.cta` (v5), after C4, dips 1.0 / 0.5 s.
- Visual grammar: FORMAT.md; popfig with local scrim; news bug; no chapter cards; presenter circle phase 2; every overlay
  anchored to words.json cues. Data-feed holds: BMKG/CIRA satellite (C1), the InaTEWS chain diagram (C2), USGS Barry Arm
  monitoring imagery (C7), Landsat before/after (C4).
- Pool: `library/mini-storms/krakatau-2026/` (+ warning-system/, tsunami-2018-more/, alaska-hawaii/, 1883-more/, broadcast-2026/).
- Interaction beats (cap 3): I1-S2 where-are-you-watching (verbatim, TTS "reed"); C6-S1 guess-the-height; Z1-S1 END CTA spine.

## Sources
1. PVMBG / MAGMA Indonesia via Antara + Databoks, 4–9 Sep 2026 (25-h eruption 4 Sep 23:07 → 6 Sep 00:04; Level III since 2 Jul; 3 km;
   tiltmeter at Tanjung rising since early August; 9 Sep 00:47 sixth eruption; PVMBG head quote).
   https://en.antaranews.com/news/430144/pvmbg-continues-monitoring-anak-krakatau-after-eruption-ends
2. BMKG SIGMET / nine145 verified update 7–8 Sep 2026 (39 SIGMETs; 8 airports; no sea-level anomaly through 6 Sep).
   https://nine145.com/2026/09/08/anak-krakatau-eruption-september-2026-verified-update/
3. AFP via Inquirer, 23 Dec 2018: BNPB spokesman Sutopo Purwo Nugroho, "Indonesia did not yet have any early warning system for
   tsunamis caused by underwater landslides or volcanoes in the sea." https://newsinfo.inquirer.net/1065822/
4. ABC News Australia, 1 Oct 2018: all 22 tsunami buoys inoperative since 2012 (vandalism, theft, fishermen mooring, funding);
   backup = 134 tide gauges, land seismographs, sirens in about 55 locations, SMS. https://www.abc.net.au/news/2018-10-01/indonesia-tsunami-early-detection-buoys-broken-for-six-years/10324200
5. 2018 Sunda Strait tsunami digest (BNPB/BMKG figures): 21:03 collapse, 21:27 BMKG detection, 21:30–21:38 waves on the beaches;
   423 eruptions that day; Carita ≥2 m, Tanjung Lesung >5 m, survey run-ups to 13.4 m; 426 dead, 14,059 injured, 2,752 houses,
   510 boats; Seventeen band, six of the party killed; PLN outing 43 of 199; BMKG first called it high tide.
   https://en.wikipedia.org/wiki/2018_Sunda_Strait_tsunami
6. Grilli et al., Science Advances 2020 (landslide <0.2 km³; no strong short-period seismic waves; summit 338 → 110 m).
   https://www.science.org/doi/10.1126/sciadv.aaz1377
7. GFZ / BMKG post-2018: 533 seismographs by 2024; TsunamiRisk project 2021–24 (22 Indonesian + 7 German institutions); BMKG:
   detection incomplete without underwater sensors. https://www.gfz.de/en/press/news/details/ein-verbessertes-tsunami-fruehwarnsystem-fuer-indonesien ; https://voi.id/en/news/432666
8. Earth magazine / USGS, Lituya Bay 9 Jul 1958: M7.5 Fairweather fault; 30 million m³ rock; 524 m run-up; 180 km/h; minutes between
   quake and wave; Ulrich + son on the Edrie survived, Swansons on the Badger lifted over the trees, Orville and Mickey Wagner died.
   https://www.earthmagazine.org/article/benchmarks-july-9-1958-megatsunami-drowns-lituya-bay-alaska
9. Alaska DGGS / USGS, Barry Arm: ~500 million m³; flagged 2020; 48 km from Whittier; 2020 worst case 300 m at source, 30 m
   regionally; 2021 USGS reassessment ~0.6 m offshore Whittier, >200 m in the fjord; instruments (NTWC water level, seismic,
   infrasound, ground radar, deformation camera, InSAR); status 4 Sep 2026 "no signs of large-scale active deformation".
   https://dggs.alaska.gov/hazards/barry-arm-landslide.html
10. 1883 digest (Verbeek / Royal Society): 27 Aug explosions 05:30, 06:44, 10:02; Merak wave 46 m; 24 m south Sumatra, 42 m west
    Java; official toll 36,417 (Banten 21,565, Lampung 12,466, Batavia 2,350); heard at Perth 3,110 km and Rodrigues 4,800 km;
    barographs recorded the wave seven times. https://en.wikipedia.org/wiki/1883_eruption_of_Krakatoa
11. NOAA Climate.gov: the year without a summer (1816) was Tambora 1815. https://www.climate.gov/news-features/blogs/enso/year-without-summer
12. USGS FAQ: tsunami triggers (earthquakes, eruptions, submarine and onshore landslides) all occur in the United States; Pacific
    states most exposed. https://www.usgs.gov/faqs/could-a-large-tsunami-happen-united-states

---

## HOOK (0:00–0:10)

### H1-S1 — narration
> The sirens along the Sunda Strait have never once sounded for Krakatoa. Not in twenty eighteen, when the wave killed four hundred and twenty six people. And they will not sound next time either.

Visual: 2018 aftermath aerial (BBC/Al Jazeera), then a siren tower still; popfigs "426 DEAD", "NO SIREN". [src: 5]

## INTRO (0:10–1:15)

TTS note (not narration): the owner's phrase is "Comment down where you are watching this from. I read all the comments." — spelled "reed" in the narration line only.

### I1-S1 — narration
> December twenty second, twenty eighteen. Three minutes past nine in the evening, a Saturday, two days before Christmas. A piece of Anak Krakatau, the child of Krakatoa, slides into the sea. Twenty four minutes later the weather agency's instruments notice. By then the wave is already breaking over a beach concert at Tanjung Lesung, and the band is still playing. No earthquake. No alert. No siren. The next morning the disaster agency said the sentence this whole video is about. Indonesia did not yet have any early warning system for tsunamis caused by underwater landslides or volcanoes in the sea.

Visual: night ocean, then the concert-stage aftermath still, BNPB presser; chip "SATURDAY · TWO DAYS BEFORE CHRISTMAS"; popfigs "9:03 PM", "24 MINUTES"; glass quote card for the BNPB line. [src: 3, 5]

### I1-S2 — narration
> That mountain has erupted six times in the last week, and it is taller again. Everyone online is watching one number, the height of the plume. It is the wrong number. So this is not a history video. In the next fourteen minutes you will see exactly how a tsunami siren works, and why a collapsing volcano defeats it. You will see what was fixed since twenty eighteen, and what was not. And then something most people watching this do not know: the tallest wave ever recorded on Earth was not in Asia. It was in Alaska, and America is watching a slope right now for the same reason. Comment down where you are watching this from. I reed all the comments.

Visual: 2026 plume satellite, then a Lituya Bay teaser aerial (USGS) for 2 s, then Barry Arm radar still; chip "SIX ERUPTIONS · ONE WEEK"; popfig "ALASKA"; chip "COMMENT: WHERE ARE YOU WATCHING FROM?". [src: 1, 8, 9]

## C1 — THIS WEEK, ON THE RECORD (1:15–2:10)

### C1-S1 — narration
> The record first. At seven minutes past eleven on the night of September fourth, Anak Krakatau began an eruption that ran for twenty five hours. Indonesia's volcano agency, PVMBG, holds it at Level Three, the second highest alert, where it has been since July. Nobody within three kilometres of the crater. Then two more eruptions on Monday, and a sixth just after midnight on Wednesday, twenty eight seconds long, seen only by the seismographs. The observatory's tiltmeter on the flank has been rising since the start of August, which means the mountain is inflating. The head of the agency said it plainly: activity remains high, and another eruption in the near future remains possible.

Visual: DATA-FEED HOLD BMKG/CIRA satellite, timeline chip Sep 4 → 9; popfigs "25 HOURS", "LEVEL III", "3 KM", "28 SECONDS", "TILT ↑ SINCE AUGUST"; quote card. [src: 1]

## C2 — HOW A SIREN ACTUALLY WORKS (2:10–3:05)

### C2-S1 — narration
> Here is how a tsunami warning works, in Indonesia and almost everywhere else. The ground shakes. Seismographs on land measure the earthquake within a minute or two. A computer compares it to a library of pre-run scenarios and decides if the sea floor moved enough. Then the warning goes out: sirens in about fifty five coastal locations, text messages, television. Indonesia can do that in under five minutes, and it has done it. But look at the first word in that chain. The ground shakes. Every part of the system waits for an earthquake. The twenty two buoys that were supposed to feel the wave itself had all been dead since twenty twelve. Vandalised, used by fishermen as anchor points, some simply stolen. So in twenty eighteen the country had a fast siren, and nothing to pull the trigger.

Visual: InaTEWS chain diagram built as a card (seismograph → computer → siren), siren tower and SMS screen stock, buoy photo with a red X; popfigs "55 SIRENS", "UNDER 5 MINUTES", "22 BUOYS", "DEAD SINCE 2012". [src: 4]

## C3 — DECEMBER 22, 2018, MINUTE BY MINUTE (3:05–4:20)

### C3-S1 — narration
> Now put the two together. That Saturday the volcano had already erupted four hundred and twenty three times since noon. Nobody on the beaches was alarmed, because it had been doing that for months. At three minutes past nine, the south west flank gave way. Less than a fifth of a cubic kilometre of rock, sliding into the strait. It did not shake the ground the way an earthquake does, so the seismographs saw nothing worth a warning. At twenty seven minutes past nine, a tide gauge finally registered a wave on the Banten coast. Between half past nine and twenty two minutes to ten, the water arrived. At least two metres at Carita. More than five at Tanjung Lesung, where the band Seventeen was on stage in front of a company party. Six of the band's party died. Of one hundred and ninety nine employees at that party, forty three did not go home. The weather agency's first public statement called it a high tide. The final count was four hundred and twenty six dead, more than fourteen thousand injured, two thousand seven hundred houses gone. The tallest run-up the survey teams found later was thirteen point four metres.

Visual: night eruption CCTV, collapse before/after Landsat, tide-gauge trace card, concert-stage aftermath still, BBC "struck at night without warning", Tanjung Lesung resort aftermath, BNPB presser; popfigs "423 ERUPTIONS", "9:03 PM", "0.2 KM³", "9:27 PM", "5 M", "43 OF 199", "426 DEAD", "13.4 M". [src: 5, 6]

## C4 — WHY NOBODY SAW IT COMING (4:20–5:10)

### C4-S1 — narration
> Why did nothing see it? Because a collapse is not an earthquake. The child of Krakatoa had grown three hundred and thirty eight metres tall on a cone that was too steep, too fast. When it let go, the signal it sent was long and slow, the kind of rumble seismographs are built to ignore. It happened at night, on a holiday weekend, at the one hour a beach is full of people who cannot see the horizon. And the water in the Sunda Strait is shallow, so the wave crossed to the coast in under half an hour. The mountain lost two thirds of its height that night. The people on the beach lost twenty four minutes they never knew they had.

Visual: collapse diagram, before/after summit graphic 338 → 110, night beach stock, strait map with the wave timing; popfigs "338 M", "NOT AN EARTHQUAKE", "UNDER 30 MIN", "338 → 110 M". Connective into the CTA dip. [src: 6]

## CTA — `assets/cta/paul-storm-ready-v5-sep6.mp4`, dips 1.0 s in / 0.5 s out (5:10–5:26). Presenter circle hidden.

## C5 — 1883, THE SAME WAVE (5:26–6:30)

### C5-S1 — narration
> If you are over sixty, you may have seen the nineteen sixty nine film Krakatoa, East of Java. Good film. The island is west of Java. What the film got right is the sea. On the morning of August twenty seventh, eighteen eighty three, the old mountain went in four explosions. Five thirty, six forty four, and the one at two minutes past ten. That one was heard in Perth, three thousand kilometres away, and on Rodrigues Island, forty eight hundred. The pressure wave crossed barographs around the world seven times. But the killing was done by water. The wave that hit Merak was forty six metres high. Twenty four metres along the south coast of Sumatra, forty two along the west coast of Java. Thirty six thousand four hundred and seventeen dead by the official count. Twenty one thousand of them in Banten, the same coast as twenty eighteen. Same strait, same coast, same mechanism, one hundred and thirty five years apart. And in eighteen eighty three, nobody expected a siren.

Visual: Parker & Coward lithographs, film poster still (fair use, 2 s), Royal Society barograms, 1883 tsunami-reach map, Merak illustration; popfigs "EAST OF JAVA?", "10:02 AM", "HEARD 4,800 KM", "46 M", "36,417 DEAD", "SAME COAST". [src: 10]

## C6 — ALASKA, 1958 (6:30–7:40)

### C6-S1 — narration
> Now the part that is not about Indonesia at all. Before I tell you, guess how tall the tallest wave ever recorded on Earth was. A hundred feet? Three hundred? On the ninth of July, nineteen fifty eight, a magnitude seven point five earthquake hit the Fairweather fault. It shook a fjord in southeast Alaska called Lituya Bay. Thirty million cubic metres of rock fell a thousand metres into the water. The wave that came off that rockfall climbed the far shore to five hundred and twenty four metres. Seventeen hundred and twenty feet. It stripped the forest off the mountainside to that line, and the line is still visible from the air today. Three fishing boats were anchored in the bay. Howard Ulrich and his eight year old son rode the wave on the Edrie and lived. Bill and Vivian Swanson were lifted over the treetops on the Badger and lived. Orville and Mickey Wagner on the Sunmore were never found. Ulrich said afterwards: it was not a wave at first. It was like an explosion. Two minutes, from the shaking to the water. No siren on Earth is that fast.

Visual: USGS Lituya Bay trimline aerial (hold, labelled), Don Miller photos, boats map card, popfigs "GUESS: HOW TALL?", "JULY 9, 1958", "524 M", "1,720 FT", "2 MINUTES"; quote card for Ulrich. [src: 8]

## C7 — BARRY ARM, WATCHED TODAY (7:40–8:45)

### C7-S1 — narration
> That was a rockfall into a fjord. Now here is the one being watched today. In twenty twenty, scientists wrote an open letter about a slope above Barry Arm, in Prince William Sound, Alaska. About five hundred million cubic metres of rock, sixteen times Lituya. It is held up by a glacier that is melting out from under it. The first worst case said three hundred metres of run-up at the source, and thirty metres across the sound. The town of Whittier sits forty eight kilometres away. A second look by the Geological Survey in twenty twenty one brought Whittier's number down to about two feet offshore. The fjord itself could still see more than two hundred metres. So the slope now carries water level gauges from the National Tsunami Warning Center, two seismic stations and an infrasound sensor. Plus ground radar, a camera watching for movement, and satellite radar from orbit. On September fourth this year the status read: no signs of large scale active deformation. Notice what that is. It is the same instrument Krakatau's observatory relies on. Not a siren. A measurement of the mountain moving before it falls.

Visual: DATA-FEED HOLD USGS Barry Arm imagery/radar labelled, Prince William Sound map with Whittier, instrument list card, Whittier town still; popfigs "500 MILLION M³", "48 KM", "2 FT AT WHITTIER", "200 M IN THE FJORD", "SEPT 4, 2026". [src: 9]

## C8 — WHAT WAS FIXED SINCE 2018 (8:45–9:45)

### C8-S1 — narration
> So what did Indonesia fix? Quite a lot, and not the thing that matters most. By twenty twenty four the seismograph network had grown to five hundred and thirty three stations. A three year German and Indonesian project, twenty two Indonesian institutions and seven German ones, rebuilt the warning models and wrote the strategy. New water level stations went in along the strait. They are built to see a disturbance that is not an earthquake, including one caused by a volcano. And the volcano itself now has a tiltmeter that is public, updated within minutes. Then the weather agency's own director said the honest sentence: without sensors under the sea, the calculation can be slow and missed. The buoys are still the missing piece. Everything else got faster. The trigger is still the problem.

Visual: seismograph network map, BMKG station photos, tiltmeter plot, buoy photo with red X again; popfigs "533 SEISMOGRAPHS", "22 + 7 INSTITUTIONS", "STILL NO BUOYS"; quote card for the BMKG line. [src: 7, 1]

## C9 — THE ARITHMETIC OF A WARNING (9:45–10:45)

### C9-S1 — narration
> Do the arithmetic with me. In twenty eighteen the collapse happened at nine oh three. The first wave reached a beach at about nine thirty. That is twenty seven minutes. A tide gauge cannot see a wave until the wave is passing it. So the earliest any instrument could know was nine twenty seven, and it did. Now add what a warning needs after that: a person to confirm it, a decision to sound the alarm, and the sirens themselves. In the best system on Earth that is five to ten minutes. Which lands the siren at the same moment as the water, or after it. That is not a failure of Indonesia. It is the shape of the problem. For a volcano that sits inside the strait, the wave and the warning arrive together. The only thing that can be faster is a person looking at the sea.

Visual: timeline card 21:03 → 21:27 → 21:30 with the "detect + decide + broadcast" bars overlapping the wave arrival; popfigs "27 MINUTES", "9:27", "+5 TO 10 MIN", "SAME MOMENT". [src: 5]

## C10 — WHO IS AT RISK THIS WEEK (10:45–11:40)

### C10-S1 — narration
> Who is that person, this week. The coasts of the Sunda Strait: Banten on the Java side, Anyer, Carita, Tanjung Lesung, and Lampung on the Sumatra side. The ferries between Merak and Bakauheni cross the strait all day, within sight of the mountain. Jakarta and West Java get the ash, which is a breathing and an airport problem, not a wave. If you have family flying into Java this month, their risk is a cancelled connection. If they are on a beach in Banten, their risk is the thing this mountain has already done once, at night, without a sound.

Visual: strait map lit in narration order, ferry stock, Anyer beach, Jakarta ash; popfigs "BANTEN", "LAMPUNG", "MERAK – BAKAUHENI", "JAKARTA · ASH". [src: 2, 5]

## C11 — WHAT IS NOT HAPPENING (11:40–12:30)

### C11-S1 — narration
> The honest part. Nobody is forecasting an eighteen eighty three; the child holds a fraction of the old mountain's magma. The ash is not crossing an ocean. The year without a summer that people keep quoting was Tambora, in eighteen fifteen, a different volcano thirty times bigger. And no, a Krakatau wave cannot reach America. The strait opens onto the Indian Ocean, and the twenty eighteen wave was spent within a few hundred kilometres of coast. The weather agency has seen no sea level anomaly this week. The risk is local, real, and repeatable. That is the whole point.

Visual: NOT card (three rows), Indian Ocean map with the strait; popfigs "NOT 1883", "TAMBORA, NOT KRAKATOA", "NO WAVE TO AMERICA". [src: 2, 11]

## C12 — THE ONLY SIREN THAT WORKS (12:30–13:25)

### C12-S1 — narration
> So here is the siren that works, and it is the same one on both sides of the Pacific. One: if the sea pulls back from the beach, or the water goes strangely flat and fast, that is the warning. You move uphill, twenty metres or more, and you do it now. Two: if the mountain is erupting and you hear a roar you have not heard before, the same. If the ground shakes near a steep shore, the same. Whittier practises it. The town runs to high ground on a drill, because they know a siren will be late. Three: if you are visiting a coast like this, know the high ground before the sun goes down. Most of the people who died in twenty eighteen were within a few hundred metres of a slope that would have saved them. They did not know it was there.

Visual: 3-row checklist card over beach footage, Whittier drill still, uphill road stock; popfigs "1 SEA PULLS BACK", "2 THE SOUND", "3 KNOW THE HILL". [src: 5, 8, 9]

## CLOSE (13:25–13:50)

### Z1-S1 — narration
> It was not a wave at first, he said. It was like an explosion. The instruments will tell you the mountain is inflating. Only you can tell when the sea has changed. If you enjoyed this video, like and subscribe for more. I truly appreciate it. Comment the one coast you know that has no high ground nearby, or any suggestions for improvements. I love reeding all your comments. Make sure to check out the ebook in the description, and stay tuned for the next video. Good day.

Visual: Lituya Bay aerial slow push, then the outro brand card; end screen pointer to the Krakatau and El Niño videos. Presenter circle hidden.
