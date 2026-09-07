# Breaking-Disaster-News Teardown — 10 reference videos, 2026-09-08

Method: `yt-dlp` metadata+comments+auto-subs, ffmpeg contact sheets (whole-video 5x5 grids
sampled at 100 frames/duration, plus a first-60s hook sheet at 1fps/6x10), ffmpeg scene-cut
detection (`select='gt(scene,0.3)'`), and direct visual inspection of every contact sheet.
Video files were deleted after analysis; sheets/srt/json/logs remain in each video's subfolder.
Batch 2 (9ws0qN4hFtY, hf7xCeEWeOE, YHjdguvoksw, 3r5HgsfWtRQ) additionally records channel
subscriber count and upload cadence (from `channel_follower_count` in info.json plus a live
`yt-dlp --flat-playlist`/per-video date pull against each channel's `/videos` tab) and a
title-to-hook carryover note.

## Comparison table

| id | channel | subs | title | dur | views | upload | cuts total | median shot | hook median shot | wpm | stills vs video | 9:16 embeds | credits shown | CTA/ask timing |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| z_vo0DCEKAE | The Space Desk | not gathered | What Just Happened In Nepal Reveals A Terrifying Truth You Aren't Ready To Hear | 19:14 | 1,241,519 | 2026-08-29 | 238 | 4.2s | 8.0s | ~200 | ~60% real news/drone/CCTV clips, ~40% AI-generated "war room"/office stills+graphics | yes (portrait phone clips pillarboxed) | yes, "SOURCE: USGS" tag on maps | not visible in sampled frames |
| n_41Jzj3KPU | S zone | not gathered | M7+ Earthquakes Are Striking South America — The Nazca Plate Is Under Pressure | 19:49 | 116,650 | 2026-08-27 | 21 | 44.6s | 13.8s | ~174 | ~90% AI-generated painterly stills (webcam presenter over static/slow-pan art) | no | none | not visible in sampled frames |
| qLun3DQLu5s | Global Vlad | not gathered | 6 VOLCANOES ERUPT – 150,000 AFFECTED Across Indonesia (Latest Updates) | 13:09 | 79,684 | 2026-09-07 | 55 | 11.8s | 6.6s | ~66 | ~95% real user-submitted/CCTV phone footage, near-zero stills | yes, dominant format (portrait clips pillarboxed black) | fake "GNN Global Weather Network" bug only, no real handles | not visible in sampled frames |
| 28UP8fh-sCU | Disaster Pulse | not gathered | ASIA'S DEADLIEST VOLCANO ERUPTS! Anak Krakatau Sends Ash 50,000 Feet High | 19:27 | 386,166 (1 day) | 2026-09-06 | 283 | 4.5s | 4.2s | ~166 | ~70% real licensed broadcaster/CCTV clips (VOA, AP, BBC One, PVMBG), ~30% stock cutaways | no | yes — VOA/AP/BBC/Newsflare/Mirror Now logos burned in | not visible in sampled frames |
| iexrMZYDTNw | The Field Report | not gathered | Krakatoa Is Alive Again — And That's Not The Worst Part | 18:41 | 4,210 | 2026-09-07 | 228 | 3.7s | 3.5s | ~192 | ~50% credited real social/satellite clips, ~50% premium AI-generated cinematic stills+diagrams | yes (boat-deck vertical clips) | yes — small "©HANDLE" watermarks + "©CSU/CIRA & JMA/JAXA" satellite credit | not visible in sampled frames |
| Reg_TypDDRQ | (source clip only, metadata not pulled per brief) | n/a | TikTok clip, "Geophysicist Stefan Burns" (@stefanbur) | first 90s only | — | — | — | — | — | 100% real talking-head TikTok clip (face-cam + inset lava footage) | this IS the vertical source | "TikTok @stefanbur" watermark + on-screen name card "Geophysicist Stefan Burns" | n/a |
| 9ws0qN4hFtY | Stefan Burns | 798,000 | If the Sky Goes Dark and it's Suddenly Freezing, This is Why... | 8:27 | 564,046 | 2026-09-02 | 7 | 38.9s | 60.0s (0 cuts in first 60s) | ~159 | ~5% real satellite/data stills, ~95% talking-head-to-camera holds | no | full name card "Geophysicist Stefan Burns", real NASA/NOAA data citations | not visible in sampled frames |
| hf7xCeEWeOE | Stefan Burns | 798,000 | Something Big Has Changed for the World's Largest Ocean... | 18:24 | 476,444 | 2026-09-04 | 33 | 20.1s | 60.0s (0 cuts in first 60s) | ~178 | ~10% real live NOAA/NASA dashboard captures, ~90% talking-head holds | no | full name card, real GOES-19/NOAA dashboard captures | not visible in sampled frames |
| YHjdguvoksw | Stefan Burns | 798,000 | We're Not Ready For What's Coming Next... | 24:33 | 556,336 | 2026-09-07 | 18 | 60.2s | 60.0s (0 cuts in first 60s) | ~162 | ~15% real NASA solar/cosmic-ray data, ~85% talking-head holds | no | full name card, real solar-cycle/Oulu neutron monitor data | not visible in sampled frames |
| 3r5HgsfWtRQ | Hidden Constructions | 1,150 | America's Deadliest Volcano Is Doing Something It Shouldn't | 10:05 | 148,278 | 2026-09-02 | 141 | 3.6s | 2.7s | ~176 | ~55% real archival/scientific footage, ~45% premium AI-generated cinematic B-roll | no | real archival (David Johnston photo, 1980 newsreel), no AI credit given | not visible in sampled frames |

VPH (views-per-hour) note: only 28UP8fh-sCU has enough of a fresh-upload signal to compute — 386,166
views in roughly 24h ≈ 16,000 VPH, by far the fastest of the ten. The others are 2-10 days old with
no timestamp precision finer than upload date, so VPH is not meaningful for them. That said, the
view-to-subscriber RATIO is informative for the batch-2 small/mid channels: Stefan Burns (798,000
subs) runs roughly 0.6-0.7x subs per video (564k/476k/556k views on ~800k subs — a normal, healthy
ratio for an established channel), while Hidden Constructions (1,150 subs) hit 148,278 views on this
video — a ~129x subscriber multiple. That is the clearest "high-demand/low-supply topic" outlier
signal in the whole set: a near-zero-subscriber channel picking an under-covered angle (infrastructure
disasters: dams, sinking towers, sea walls) outperforming its own subscriber base by two orders of
magnitude, the same pattern storm-market's own strategy is betting on.

## Channel upload cadence (batch 2 only, per brief)

- **Stefan Burns** (`UCGutiiMqD6jEy6J9hNdNniA`, 798,000 subscribers): last 5 uploads landed
  2026-08-31, 09-02, 09-04, 09-05, 09-07 — roughly **one video every 1.6 days**. This is a
  breaking-news-speed cadence from an established, credentialed-presenter channel: he ships on
  whatever hazard is live that week (volcano, hurricane trio, solar cycle, earthquake fault) rather
  than batching a single disaster into one deep-dive.
- **Hidden Constructions** (`UCYGYA9PuXei_niErotRU_LA`, 1,150 subscribers): last 8 uploads landed
  2026-08-07, 08-09, 08-14, 08-16, 08-22, 08-27, 08-29, 09-02 — roughly **one video every 3.7 days**,
  closer to twice a week. Each video covers a different structural/engineering disaster (Millennium
  Tower, Hoover Dam, Three Gorges Dam, Venice flood barriers, Vajont Dam, Salton Sea) — a much
  narrower, less time-sensitive niche than Stefan Burns' live-hazard beat, produced at documentary
  pacing (3.6s median shot) rather than talking-head pacing.

wpm in the table is verified: for each srt cue, the running transcript is stitched by matching the
longest overlap between the previous cue's tail and the new cue's head (rolling-caption cues repeat
most of the prior line and append 1-3 new words), counting only the non-overlapping new words —
`scripts` note: see `wpm_check.py` in this folder. This replaced an earlier draft column that
naively halved total raw word count (which overstated every value by ~1.4-1.6x; e.g. z_vo0DCEKAE
read 295 wpm naive vs 200 wpm stitched — confirmed correct by eyeballing the stitched transcript
against the audio's actual pace). qLun3DQLu5s's 66 wpm is real — that video is carried by on-screen
news-ticker text and raw ambient/phone audio, not continuous narration, unlike the rest of the set.

## Per-video notes

### z_vo0DCEKAE — "What Just Happened In Nepal…" (The Space Desk)
**Hook (first 45s):** "489 people are confirmed dead and more than 2,000 are still missing. That is
the toll so far from a disaster that began when a mountain in the Himalaya simply let go with no
warning at all. But the death count is not the part you're not ready to hear. The terrifying part is
why it happened and the fact that the very same thing is now taking shape in valleys far from Nepal.
By the end of this, you will understand the threat quietly forming above millions of people..."
Title promises "a terrifying truth" — the hook pays it off in the first two sentences by naming the
death toll, then immediately pivots to the actual thesis (this can happen elsewhere), which is a real
carry-over, not clickbait.

**Top comments:** sympathy/prayer for Nepal; a comment alleging Western media blackout on Chinese
rescue efforts (11 likes-equivalent range, all low-single-digit likes — this video's comment
engagement is thin relative to its 1.2M views); one comment noting a school principal's early warning
saved 900 students — a fact-check angle the video itself may have missed.

**Visuals:** Real aerial/drone landslide and flood footage, CCTV-style hotel/bus-yard shots, crowd/
evacuation footage, intercut with a large volume of AI-generated "disaster-response war room" stills
(officials at monitors, glowing terrain relief tables, boardroom briefings) that repeat across the
episode. Heavy use of official-style graphics: USGS "SOURCE: USGS" tagged satellite/community-
intensity maps, a custom "2026 Nepal Debris Avalanche and Flash Flood" route map, comparison diagrams
("Normal flood vs Debris flow", "Engineered Dam vs Real Chaotic Rubble Barrier"), and stat cards
("River rose ~9m in 30 min", "3 STORIES IN 30 MINUTES", "+35% GLOF risk increase 1990-2023",
"388+ documented events"). Bold white-caps section-title cards on black ("A MOUNTAIN FELL WITHOUT
WARNING", "WHAT PEOPLE ARE GETTING WRONG ONLINE", "WHAT HAPPENS NEXT") mark chapter breaks. A news-
chyron-style banner appears mid-frame for the death toll ("NEPAL-CHINA BORDER REGION: Nearly 500
confirmed dead / More than 2,000 still missing"). Portrait-orientation phone clips are pillarboxed on
black. The hotel-building aerial and one glacier shot repeat several times across the sample.

### n_41Jzj3KPU — "M7+ Earthquakes Are Striking South America…" (S zone)
**Hook:** "Three major earthquakes, three different countries, 57 days. That is not a coincidence.
That is a continent under siege. And right now, scientists are saying the worst has not happened yet.
The plate underneath South America is not done. It is loaded. It is locked. And it is ready to snap..."
Strong cold-open thesis statement, but the visual behind it never changes (same webcam shot), which
is the format's core weakness.

**Top comments:** heavy end-times/religious commentary (multiple top comments quoting scripture),
plus a technical aside ("sounds like a number of plates are almost ready to unlock, globally") and
one about nuclear testing — audience skews toward doom/prophecy framing rather than science literacy.

**Visuals:** Structurally the odd one out — a small talking-head presenter (red webcam-record icon,
YouTube-recording-style inset bottom-right) narrates over full-screen AI-generated oil-painting-style
disaster illustrations (mountains, lava rivers, cracked earth, tectonic cutaway diagrams) with slow
zoom/pan, plus occasional real graphics (seismograph readouts, a phone earthquake-alert app mockup,
red-dot South America risk maps, Earth-from-space). Word-by-word yellow-highlight burned-in captions,
all caps, bottom-third. No lower-thirds, no source credits, no maps sourced from a real agency (the
red-dot maps read as generic vector graphics, not USGS). This is the cheapest-to-produce format of
the six and explains its low cut count (21 cuts / 20-min video) — ffmpeg scene-detect barely fires
because the underlying art barely changes frame to frame.

### qLun3DQLu5s — "6 VOLCANOES ERUPT…" (Global Vlad)
**Hook:** "What you are looking at is one of six Indonesian volcanoes that erupted inside the same
day. The sound from the one in the Sunda Strait carried 700 km according to Indonesia's geology
agency. But the question people started asking was whether six volcanoes going at once means
something is happening underneath." Short, fact-first hook; no scripted narration continues much past
this — the video is largely carried by raw clip audio and on-screen text after the open.

**Top comments:** several practical/local eyewitness reports (ash on windowsills, air quality
complaints), religious/rapture commentary, and one commenter directly requesting a map ("Is it so
difficult to map them out") — a genuine content gap this format doesn't fill.

**Visuals:** Almost entirely real, raw, vertically-shot phone/CCTV footage of eruptions (pillarboxed
on black/blurred background) — the highest real-footage ratio of the six. Overlaid with a fabricated
"GNN — Global Weather Network" news package: a small red "BREAKING NEWS" badge plus a blue ticker bar
carrying a fact-per-shot headline that updates every 5-15s ("6 VOLCANOES ERUPT SAME DAY ACROSS
INDONESIA" → "JAKARTA AIRPORT GRINDS TO HALT AMID ASH" → "712 FLIGHTS HIT AS ASH GROUNDS AIRPORT" →
"150,000 PASSENGERS CAUGHT AS 8 AIRPORTS CLOSE" → "NO DEATHS REPORTED FROM ANAK KRAKATAU ERUPTION" →
"1883 KRAKATOA ERUPTION KILLED 36,000 PEOPLE" → "SINABUNG ERUPTS AFTER 4 YEARS OF QUIET"). A tiled
diagonal "GNN" watermark appears across several clips. One clip carries a real CCTV timestamp burn-in
("CCTV Lava93 04/09/2026 23:20:23"), confirming at least some feeds are pulled from live volcano
observation cams, not just social video. Clip repetition is heavy — the same eruption footage recurs
under different ticker headlines. No CTA visible in sampled frames.

### 28UP8fh-sCU — "ASIA'S DEADLIEST VOLCANO ERUPTS!" (Disaster Pulse, 386k views in ~1 day)
**Hook:** "Asia is facing one of its scariest volcano stories in years, and this one comes from a
mountain with a very dark past, Anak Krakatoa, the young volcano that grew out of the wreckage of a
much bigger disaster has exploded again, and this time it sent a wall of ash soaring 50,000 ft into
the sky. That is higher than almost every airplane in the world ever flies. Loud booms shook the air
and were heard more than 400 miles away..." Title-to-hook payoff is direct and immediate — the title's
"50,000 Feet" claim is the second sentence spoken.

**Top comments:** dominated by religious/end-times commentary (this is the pattern across nearly every
video in this set — the audience for this niche skews heavily toward prophecy framing), one direct
skepticism comment ("I couldn't find it on the USGS website yet either... 10% suspicious"), and one
first-person eyewitness account (ash on car, 100km from the volcano).

**Visuals:** The most "traditional documentary aggregator" of the six — real licensed broadcaster and
wire footage (VOA drone shots, AP news package, a BBC One clip, PVMBG official CCTV, Newsflare,
ActuVideo, Mirror Now — logos burned into the source clips and kept, not cropped out) plus stock
cutaways (ash macro shots, jet-engine close-up, airport terminal, old B&W archival street footage for
the historical 1883 section, tsunami-wave data visualizations, seismograph readouts). Distinctive
convention: small rounded data-callout chips bottom-left ("50,000 feet", "400+ miles", "50 mph",
"2 countries", "36,000+ deaths", "6 airports", "300+ flights", "90 miles", "1°C") appear in sync with
each number as it's spoken — this is the cleanest "numbers get their own micro-graphic" pattern in the
set. Word-highlighted burned-in captions bottom-center throughout. Highest cut count and highest
hook-cut density (15 cuts in the first 60s) of the whole set — this is the most aggressively edited
video, consistent with it being the single fastest-growing (~16,000 views/hour).

**Clip-lift confirmed (step 7):** the video's opening (~9-15s in) cuts to a TikTok-style talking-head
clip — face-cam with an inset shot of glowing lava — captioned "the wreckage of a much bigger
disaster has..." This is frame-for-frame the same clip as `Reg_TypDDRQ`, credited on-screen there as
"Geophysicist Stefan Burns" (TikTok handle `@stefanbur`). Same face, same expression sequence, same
lava-footage crop and camera framing in both. Confirmed: 28UP8fh-sCU's opener is a direct re-cut of
Reg_TypDDRQ's TikTok source clip, likely obtained without the original creator's on-screen credit
being retained in 28UP8fh-sCU's edit — the "Geophysicist Stefan Burns" name card visible in Reg_TypDDRQ
does not appear in the corresponding 28UP8fh-sCU frames.

### iexrMZYDTNw — "Krakatoa Is Alive Again…" (The Field Report)
**Hook:** "More than 400 people died here in 2018, and almost none of them ever knew it was coming.
Anak Krakatoa in the narrow strait between Java and Sumatra has roared back into its most vigorous
phase in a year. Ash punched 50,000 ft into the stratosphere. Six airports shut down. Asia is on
alert. But the eruption everyone is watching is not the thing that makes this volcano one of the
deadliest on the planet. The real threat is underwater..." Best "curiosity gap" hook of the six — it
deliberately withholds the real threat (submarine flank collapse / tsunami) until after establishing
the surface-level story everyone already knows.

**Top comments:** more religious/prophecy framing, a personal-safety comment from a Jakarta resident
worried about tsunami risk, and a direct eyewitness account (car covered in ash, 100km out) — same
pattern of thin fact-checking/high emotional engagement seen across the set.

**Visuals:** The most premium production of the six — credited real clips (small "©HANDLE" watermarks,
e.g. "©AGUNG DINANJAR", "©DESTINACI OCY"), a real airline departure/delay board, and satellite imagery
explicitly credited "©CSU/CIRA & JMA/JAXA". These are blended with very high-quality AI-generated
cinematic stills (dramatic night-time volcano-with-reflection shots, glowing "ASIA ON ALERT" control-
room renders) and a large library of custom explainer diagrams: volcano cross-sections, a "2018 Anak
Krakatau Tsunami: A Lesson on Non-Tectonic Triggers" flank-collapse diagram, an "Anak Krakatau: Life
Cycle 1919-2023" evolution graphic, a Sunda Strait shipping-lane economic-impact map, a stratospheric-
aerosol-forcing mechanism diagram, and a temperature-anomaly chart. Section breaks use the same
convention as z_vo0DCEKAE — a glitch-transition into a bold white-caps title card on black ("THE
MOUNTAIN IS AWAKE AGAIN", later "WHAT HAPPENS NEXT") — suggesting this is a shared convention across
multiple channels in the niche, not one channel's house style. 9:16 clips are pillarboxed (boat-deck/
railing shots). Real location captions ("KRAKATAU WATERS, BANTEN PROVINCE, INDONESIA") sit as a
documentary-style lower-third.

### Reg_TypDDRQ — source clip (first 90s only, per brief)
100% real single-shot TikTok content: a man ("Geophysicist Stefan Burns", handle `@stefanbur`,
watermark "TikTok @stefanbur" bottom-left throughout) talking directly to camera with a picture-in-
picture inset of glowing lava/eruption footage. An on-screen name card ("Geophysicist Stefan Burns")
appears a few seconds in and persists. Toward the end of the 90s window a red "Eruption of Anak
Krakatua September 4-5th 2026" banner appears over a dark satellite/map view. This is the raw source
that 28UP8fh-sCU re-cut into its own opener (see confirmation above) — direct evidence that at least
one video in this niche builds its cold-open from an uncredited lift of a smaller creator's clip.

**Note:** this same "Geophysicist Stefan Burns" is not a small creator at all — he runs his own
798,000-subscriber YouTube channel (`Stefan Burns`, see 9ws0qN4hFtY / hf7xCeEWeOE / YHjdguvoksw
below). His TikTok clips are being lifted into other channels' videos in addition to his own
full-length YouTube uploads — the same face and lava footage crop appears as a 5-15s uncredited
insert in at least one other channel's cold-open while he separately publishes full 8-25 minute
videos on his own channel under his own name.

### 9ws0qN4hFtY — "If the Sky Goes Dark and it's Suddenly Freezing, This is Why..." (Stefan Burns, 798,000 subs)
**Hook (first 45s):** "Hey everyone, geophysicist Stefan Burns here. A huge pulse of volcanic
activity has hit Aoba volcano in Vanuatu. This really started up on the 25th of August. So there
have been some eruptions ongoing at this volcano for all of 2026. There are some big pulses of
activity that occurred back in 2017, 2018, back in 2011, 2012, 1995. This may yet be the biggest
pulse of volcanic activity from Aoba volcano. They had to evacuate that island on Bay Island in
2017/2018 as a result of the eruptions there..." **Title-to-hook carryover:** the title's "sky goes
dark / suddenly freezing" premise (stratospheric ash/aerosol cooling) is NOT stated until well after
this 45s window — the hook instead opens on the specific volcano and its eruption history. This is
a deliberate curiosity-gap structure: title promises a mechanism, the video spends the first act
establishing the specific event before generalizing to the mechanism the title named.

**Top comments:** a technical aside praising the video's Starlink-reentry/ozone point, several
birthday well-wishes for Stefan personally (parasocial channel relationship), and one comment
explicitly reassuring other viewers that "Stefan is... just a messenger, not a doom-gloomer" —
audience is aware of and pushing back on the doom-framing themselves.

**Visuals:** Near-static talking-head format — Stefan Burns full-frame to camera (not a small PiP
inset; this is his own channel), background alternates between real satellite/cloud imagery of
Vanuatu (labeled "Ambae Island, Vanuatu"), a real volcanic-aerosol-injection cross-section diagram
(stratosphere/troposphere, SO2/H2SO4 chemistry), and a real historical comparison clip ("1991
eruption of Mount Pinatubo, Philippines"). His own live-data pulls: a Suomi NPP-OMPS/TROPOMI SO2
mass timeseries plot and a satellite SO2-plume heatmap sequence, both dated with real recent
timestamps and visibly the actual NASA/NOAA tool UI (captured live, not designed graphics). Only 7
scene-detected cuts in 8.5 minutes; 0 cuts in the first 60 seconds — he holds each graphic for
20-60+ seconds while explaining it rather than cutting on a rhythm. This is the lowest cut-rate
format in the entire set, the opposite pole from the raw-clip-compilation channels.

### hf7xCeEWeOE — "Something Big Has Changed for the World's Largest Ocean..." (Stefan Burns, 798,000 subs)
**Hook:** "Aloha everyone. Geophysicist Stefan Burns here reporting for you live from Hawaii right
now in the middle of the Pacific where we have three major cyclones that are rampaging across the
waters. We have Hurricane Lao currently a category 4 expected to become category 5... We have
hurricane Karina here and also Hurricane Marie, which we were concerned about in terms of its track
guidance going up into SoCal..." **Title-to-hook carryover:** strong — "world's largest ocean" (the
Pacific) and "something big has changed" (three simultaneous major cyclones) are both paid off in
the first two sentences, plus a novel personal detail (reporting live from Hawaii, in the storm's
path) that the title doesn't even need.

**Top comments:** dominated by birthday messages (96-like top comment is Stefan's own pinned
promo/birthday-sale comment for his merch store, `earthevolution.com`) — this is a monetization
channel with a direct product tie-in, distinct from the ad-only compilation channels.

**Visuals:** Same low-cut talking-head format (33 cuts / 18 min, 0 cuts in first 60s). Backgrounds:
real NOAA hurricane-track satellite loops (color-coded storm paths over cloud imagery), real GOES-19
SUVI solar composite imagery and X-ray flux plots (space-weather segment), and a real LASCO-style
blue coronagraph CME sequence with genuine UTC timestamps. 100% real live public-agency data feeds,
zero AI-generated stills, zero stock footage — the entire visual budget goes to holding and pointing
at authentic real-time dashboards.

### YHjdguvoksw — "We're Not Ready For What's Coming Next..." (Stefan Burns, 798,000 subs — his highest-viewed of the three)
**Hook:** "Hey everyone, geophysicist Stefan Burns here. The sun is weakening, and this is a cause
for concern. Now, when most people think of the sun, they think of this limitless supply of light
and energy... But we are seeing some unusual changes right now occurring with the sun. And I'm not
just talking about this solar cycle, solar cycle 25, because the peak of this solar cycle, solar
maximum was back in 2024..." **Title-to-hook carryover:** the weakest of the three Stefan Burns
videos — the title ("We're Not Ready For What's Coming Next") names no subject at all, and the hook
takes the full 45s to even state the topic is the Sun. This is pure curiosity-gap clickbait title
paired with an honest, slow-building scientific hook — a different contract with the viewer than his
other two videos, which both name their subject directly in the title.

**Top comments:** the highest-engagement comment (236 likes) is a genuinely substantive scientific
discussion (Svensmark cosmic-ray/cloud-formation theory), followed immediately by a long thread of
climate-change-skepticism arguments — this specific video's framing ("the sun is weakening") pulls
in a different, more argumentative audience segment than his disaster-specific videos.

**Visuals:** Same format again (18 cuts / 24.5 min, 0 cuts in first 60s, the lowest cut density of
the whole 10-video set). Real graphics: GOES-19 SUVI sun composite, a solar-cycle sunspot-number
progression chart (with a highlighted comparison window drawn on top), a stylized but data-labeled
polar-magnetic-field-lines illustration, a real "Solar Polar Field Strength 1976-2026" timeseries
chart, real Oulu neutron monitor cosmic-ray data, and a real NOAA "C/M/X-class flares per year" bar
chart. Every graphic in this video is either a live public data feed or a clearly-labeled real chart
— no AI-generated imagery detected anywhere in the sample.

### 3r5HgsfWtRQ — "America's Deadliest Volcano Is Doing Something It Shouldn't" (Hidden Constructions, 1,150 subs, 148,278 views — a ~129x subscriber outlier)
**Hook:** "Under a mountain in Washington state, the ground is moving in two directions at once.
Since February, hundreds of earthquakes have shaken the rock beneath Mount St. Helens. By summer,
they were coming 38 times a week. All of them small. All of them deep. When a volcano shakes like
this, it almost always means one thing. Magma is climbing toward the surface. The magma here is not
climbing. The earthquakes are getting deeper, and the mountain itself is sinking..." **Title-to-hook
carryover:** excellent — "doing something it shouldn't" is the literal thesis of the hook (a volcano
that should be swelling is instead settling), stated as a mystery rather than a stat, then resolved
with the real payoff (Mount St. Helens, 57 dead in 1980) by the end of the first 45 seconds.

**Top comments:** two comments flag AI-generated content directly — "I like how that map has a
circle drawn around Mt. Rainier. Damn AI" and "8:38, that 'scientist' is Ai. Being that close to
sulphur emissions even amateurs would be wearing a mask" — a real, specific audience callout of
AI-generated inserts even at this channel's small subscriber count. Other top comments are informed
local/eyewitness pushback ("Mt. St. Helens is a live volcano that will do what it wants... it never
went to sleep so it can't be 'waking up'") and a fact-check-adjacent critique of the danger-zone map
shape versus where the 1980 fatalities actually occurred.

**Visuals:** The most cinematically "documentary" of the whole set and the fastest-cut (141 cuts in
just over 10 minutes, 2.7s hook median — denser than every other video in this teardown). Real
archival material: black-and-white 1980 eruption newsreel-style footage, a real photo of volcanologist
David Johnston with tripod-mounted equipment, real seismograph rolls, and a real 3D wireframe
ground-deformation visualization. This is blended with clearly AI-generated cinematic B-roll (glowing
lava fissures shot as macro "veins," a mirror-still reflection-lake mountain shot, a close-up of a
"scientist" near a fumarole that a commenter correctly flagged as synthetic) and minimalist white-
background explainer cards on grid paper (black sans-serif stat callouts: "All of them small," "All
of them deep," "5 FEETS it moves a day," "450 FEET," "In under 10 minutes") — a distinct, cleaner
infographic style than any of the burned-in-caption formats elsewhere in this set. Bold red all-caps
dramatic text drops ("REFILLING", "WHEN IT STOPS?") mark act breaks instead of a title card.

## Format rules extracted

1. **Hook must name the number in the title within the first two sentences.** Every video that
   ranked well (28UP8fh-sCU, z_vo0DCEKAE, iexrMZYDTNw) states its headline stat (death toll, altitude,
   airport count) in the first 10-15 seconds, spoken, not just shown.
2. **Withhold the real angle for one beat.** The best hook (iexrMZYDTNw) states the obvious surface
   story first, then pivots to "but that's not the real threat" — a curiosity gap earns the next 30s.
3. **Shot length band for aggregated real-footage compilations: 3.5-4.5s median**, with the hook
   segment even tighter (3.5-4.2s in the two best-performing videos). The AI-art/talking-head format
   (n_41Jzj3KPU) runs 13-45s median and is the weakest-performing video in the set by ratio of views
   to duration — faster cutting correlates with this niche's top performers.
4. **Numbers get their own on-screen chip, synced to the spoken word**, not just captions. 28UP8fh-sCU's
   bottom-left data-callout convention ("50,000 feet", "6 airports", "36,000+ deaths") is the cleanest
   version of this and belongs in this format.
5. **Burned-in word-highlight captions are near-universal** (5 of 6 videos): white all-caps text,
   bottom-third or bottom-center, with the current word or key term highlighted in yellow. Auto-caption
   tool aesthetic, not hand-typed lower-thirds.
6. **A fabricated or genuine "BREAKING NEWS" ticker bug is a legitimate convention**, not just ours —
   qLun3DQLu5s runs an entirely invented "GNN — Global Weather Network" badge + rotating blue-bar
   headline, updated every 5-15s with a new fact, over otherwise uncredited raw phone/CCTV clips.
7. **Section breaks = a 1-2s glitch or hard cut into a bold white-caps title card on black.** Two
   unrelated channels (z_vo0DCEKAE, iexrMZYDTNw) use the identical device ("WHAT HAPPENS NEXT" as a
   chapter marker) — this reads as a genre convention, safe to copy.
8. **9:16 source clips get pillarboxed on black (or blurred/side-extended background), never cropped
   to fill 16:9.** True in every video that used vertical phone footage (4 of 6).
9. **Source credit is optional and inconsistent — real broadcaster logos (VOA/AP/BBC) are kept
   burned-in rather than cropped; small creator credits appear as a tiny watermark or are dropped
   entirely** (see the 28UP8fh-sCU / Reg_TypDDRQ clip-lift). Do not assume a small creator's video is
   safe to lift without credit just because bigger channels do it — that is a real Content-ID/ethics
   risk this teardown surfaces, not a rule to copy.
10. **Real official-source maps/graphics (USGS, satellite agency crops) are used sparingly but
    explicitly labeled** ("SOURCE: USGS", "©CSU/CIRA & JMA/JAXA") — this reads as a credibility signal
    worth keeping even in a fast-turnaround format.
11. **AI-generated stills are acceptable filler between real clips but should not carry the whole
    video.** n_41Jzj3KPU (the AI-art-only format) has both the lowest view count relative to age among
    the earthquake videos and the thinnest visual variety — real footage every 45-60s (echoing the
    storm-market channel's own existing rule) is what separates the top performers from it.
12. **Custom explainer diagrams (cross-sections, comparison charts, timelines) are a major share of
    screen time in the two most information-dense videos** (z_vo0DCEKAE, iexrMZYDTNw) — a spatial or
    mechanism claim ("underwater flank collapse", "GLOF risk +35%") consistently gets a purpose-built
    graphic, not just B-roll with text over it.
13. **wpm runs 160-200 for fully-narrated videos** (recomputed 2026-09-08 by de-duplicating rolling
    auto-caption cues: 28UP8fh-sCU 165, iexrMZYDTNw 191, z_vo0DCEKAE 200, Stefan Burns 159-178,
    3r5HgsfWtRQ 176; the table's 248-295 column overstates by ~1.5x) — faster than storm-market's
    own 129-148 wpm documentary pace, because this format is built for speed/urgency.
14. **Comment sections skew heavily toward religious/end-times framing regardless of channel or
    production quality** — this is an audience-level pattern across the whole niche, not a single
    channel's draw, and a content gap (fact-checking, "is this exaggerated") shows up in nearly every
    video's top comments without being addressed on-screen.
15. **A single uncredited clip can carry an entire cold-open to 386k views in a day** (28UP8fh-sCU) —
    the fastest-growing video in this set is also the most aggressively cut (283 cuts, 4.2s hook
    median) and opens on someone else's TikTok content. Speed of cutting and hook payoff correlate with
    growth more than originality does in this niche.
16. **A second, entirely different format wins in this niche: the credentialed live-data explainer.**
    Stefan Burns' three videos (798,000 subs) run 7-33 total cuts across 8-25 minutes, 0 cuts in the
    first 60 seconds, and hold a single real public data feed (NASA/NOAA satellite loops, seismograph
    plots, solar X-ray flux) on screen for 20-60+ seconds while he talks over it, full-frame,
    uninterrupted. This is the polar opposite of the fast-cut compilation format and still nets
    500k+ views per video — credibility and information density substitute for pacing.
17. **Publishing speed can BE the moat.** Stefan Burns ships once every 1.6 days, covering whatever
    hazard is live that week (a different volcano, hurricane trio, solar cycle, or fault each time)
    rather than depth on one story — this is the literal mechanism behind "high-demand/low-supply":
    he is first with credentialed real-data coverage before slower channels finish editing.
18. **A near-zero-subscriber channel can still out-perform its subscriber base by two orders of
    magnitude by picking an uncontested angle.** Hidden Constructions (1,150 subs) hit 148,278 views
    (~129x subs) on a Mount St. Helens video by using unrest-mystery framing ("doing something it
    shouldn't") rather than a stat-blast hook, at a slower ~2x/week cadence — proof that topic
    selection and hook framing matter more than channel size or speed alone.
19. **Even a small-channel audience catches AI-generated inserts and calls them out by timestamp**
    ("8:38, that 'scientist' is Ai," "Damn AI" re: a map). Mixing real archival/data footage with
    AI-generated cinematic B-roll is common in this niche, but it is not undetected — a channel
    building trust on real data (the Stefan Burns model) forgoes this risk entirely by using only
    live public-agency feeds and archival material, never synthetic "documentary" inserts.
20. **A title that withholds its subject entirely ("We're Not Ready For What's Coming Next...") still
    works when the channel already has trust and subscriber momentum**, but it is a materially weaker
    contract than a title that names the specific hazard — of Stefan Burns' three videos, the
    vaguest title pulled the most argumentative, lowest-signal comment section (climate-skepticism
    tangents) rather than on-topic engagement.
