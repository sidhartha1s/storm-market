# The Warning Hour — 14-Day Programme (2026-09-15 → 2026-09-28)

Director's note 2026-09-14: slate generated from the four-channel data, then corrected by hand: weekend documentary slots are the
BANKED TORNADO DOCS (owner decision), not new foreign docs; the CPC signal is an El Niño advisory (>90 % odds), not La Niña;
every row fixes bucket + angle + named source only, the literal title/number is locked by the 06:00 radar scan that day.
Slot titles below are placeholders for shape, not facts.

Nepal-flood bucket is already dead by the kill rule: last toll update in the data is Sep 6 20:59 ("1,400+ dead & 5,500 missing"); zero fresh numbers since, 8 days silent as of program start. It is dropped from this slate entirely. Krakatau/Indonesia and Japan (Sakurajima) are the two live foreign buckets still moving (PVMBG/JMA issue alerts on a rolling basis), so they carry the "foreign live-event" slot most days, per the format's own performance data (foreign avg ~$3.9\times$ domestic per-video views). Exact tolls/place-names/numbers in each title get locked by the 06:00 radar scan same day — the slate below fixes bucket + angle + source, not the literal future number.

## Slate
Slugs: the first cards match `ops/tracker.json`; later rows keep date-coded placeholders until the radar locks the story, at which
point the card is created with a descriptive `ms-<story>` slug and the row here is updated.

date | slug | bucket | working title | named source | why
2026-09-15 | ms-indonesia-four-volcanoes | krakatau | Anak Krakatau Erupts Again, PVMBG Holds Alert 3 | PVMBG | proper noun + live, EarthDesk pool best 225k
2026-09-15 | ms-hawaii-lowell-outages | hawaii-lowell | Hawaii Still Counting Lowell's Power Outages | Hawaii EMA / Hawaiian Electric | number (outages) + US-stake, GWN 818k tail
2026-09-16 | ms-sakurajima-ash | japan | Sakurajima Ash Cloud Grounds Kagoshima Flights | JMA / VAAC Tokyo | live + number, GWN 1.6M format
2026-09-16 | ms-0916-usf-b | us-flood | Flash Flood Watch Issued for Gulf Coast Today | NWS | live + US-stake, us-flood pool
2026-09-17 | ms-0917-krak-a | krakatau | Indonesia: Three More Volcanoes On Watch | PVMBG | proper noun + live, EarthDesk 175-225k
2026-09-17 | ms-0917-haw-b | hawaii-lowell | Lowell Cleanup: Hawaii's Final Outage Count | Hawaii EMA | closing number; kill after today, no new figure
2026-09-18 | ms-0918-jpn-a | japan | Sakurajima: JMA Says Alert Level Unchanged | JMA | live agency quote, GWN format
2026-09-18 | ms-elnino-cpc-today | elnino | NOAA's Climate Center Updates El Niño Watch | NOAA / CPC | forecast = "what the agency said today"
2026-09-19 SAT | ep-0919-doc-a | documentary (bank) | 1925 Tri-State Tornado (repackaged, School A thumb) | NWS / Tri-State assessment | banked tornado doc, weekend slot
2026-09-19 SAT | ms-0919-krak-b | krakatau | Krakatau's Lava Still Glows, PVMBG Update | PVMBG | live + number (ash height)
2026-09-20 SUN | ep-0920-doc-a | documentary (bank) | banked tornado doc #2 (repackaged) | NWS service assessment | weekend slot
2026-09-20 SUN | ms-0920-jpn-b | japan | Japan: JMA's Latest Sakurajima Advisory | JMA | live agency update
2026-09-21 | ms-0921-krak-a | krakatau | PVMBG: Anak Krakatau Ash Reaches New Height | PVMBG | number + live
2026-09-21 | ms-0921-tor-b | us-tornado-evergreen | Tornado Alley Is Still Moving, NWS Confirms | NWS | evergreen + US-stake, SpaceDesk 390k
2026-09-22 | ms-0922-jpn-a | japan | Sakurajima Ashfall Hits Kagoshima Streets | JMA | live + place
2026-09-22 | ms-0922-usf-b | us-flood | Gulf Coast Flash Flood Sets NWS Record | NWS | number + US-stake
2026-09-23 | ms-0923-krak-a | krakatau | Darwin VAAC Raises Krakatau Ash Warning | Darwin VAAC | live + agency
2026-09-23 | ms-0923-eln-b | elnino | CPC's Newest El Niño Outlook, Explained | NOAA / CPC | forecast framing
2026-09-24 | ms-0924-jpn-a | japan | Sakurajima: Japan's Volcano Won't Stand Down | JMA | live, evergreen tension line
2026-09-24 | ms-0924-tor-b | us-tornado-evergreen | NWS: Tornado Alley's New Shape This Season | NWS | evergreen + US-stake
2026-09-25 | ms-0925-krak-a | krakatau | PVMBG's Latest Count: Krakatau Eruptions Rise | PVMBG | number + live
2026-09-25 | ms-0925-usf-b | us-flood | River Flood Stage Escalates, NWS Watch Up | NWS | number + US-stake
2026-09-26 SAT | ep-0926-doc-a | documentary (bank) | banked tornado doc #3 (repackaged) | NWS service assessment | weekend slot
2026-09-26 SAT | ms-0926-jpn-b | japan | JMA Holds Sakurajima at Alert Level 3 Again | JMA | live consistency
2026-09-27 SUN | ep-0927-doc-a | documentary (bank) | banked tornado doc #4 (repackaged) | NWS service assessment | weekend slot
2026-09-27 SUN | ms-0927-usf-b | us-flood | NWS Flash Flood Emergency Hits Gulf Coast | NWS | live + US-stake
2026-09-28 | ms-0928-krak-a | krakatau | PVMBG: Krakatau Ash Column Grows Again | PVMBG | number + live
2026-09-28 | ms-0928-eln-b | elnino | NOAA's CPC: What Today's El Niño Data Shows | NOAA / CPC | forecast framing

## Daily clock (1 person + Sonnet agents, IST)
06:00 radar scan (agent 1): wire/agency feeds + GWN/EarthDesk/Szone/SpaceDesk new uploads + JMA/PVMBG/NOAA/NWS bulletins → locks real bucket, number, source for both slots.
07:00 source lock: named agency + one wire/one local outlet per slot, live-blog URL if one exists.
08:00-09:00 script draft, 8-beat skeleton, 165 wpm target, humanise gate (no rhetorical Qs, no em dashes, no reveal-flips).
09:30 TTS, atempo 1.10, re-transcribe against script.
10:00-12:00 sourcing/B-roll pulled in parallel (agent 2 = slot A, agent 3 = slot B) while assembly starts on slot A.
12:00-14:00 assemble both, run gates (humanise, thumb spell-check, description-first-line-is-URL, Content ID check on raw clips).
14:00 render, announce to owner.
Publish: slot A (foreign live) into GWN's heaviest window, 8pm-2am ET; slot B (US-stake) into the secondary 2-7pm ET block — matches the upload-hour histogram, not the event clock.

## Kill rule
Drop a bucket the moment either holds: (1) two straight days with no new agency number/statement — nepal-flood already meets this (silent since Sep 6) and is excluded above; (2) a bucket with no proper noun beyond a US city/state tracks under the flop line (domestic wildfire/earthquake-swarm, <20k, per the 9-video/6-video flop data) — pull on the first flat day, redirect that agent to the next radar hit, don't wait for a third video to confirm.

## 5 things a beginner misses
1. A changed official number gets a new upload (new slug, new thumb), never an edit to the old video — Nepal's 11-video serial off one event is the proof.
2. Thumbnail text and place-name spelling (Kagoshima, Sakurajima, Anak Krakatau) get checked before render, not just the script.
3. Raw phone/interview clip audio (the `>>` cutaways that are the actual hit-amplifier) needs Content ID clearance before render, not after a claim lands.
4. Description's first line is the source URL, not a hashtag block — GWN's own live-blog convention, and how both the crawler and viewers find sourcing.
5. End screens cross-link the day's other slot (A→B, B→A), not a generic subscribe card — mirrors GWN's chapter-driven self-cross-promo since it never credits footage per-clip.