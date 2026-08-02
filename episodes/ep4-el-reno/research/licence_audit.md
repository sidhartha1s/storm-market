# Licence audit — every file wired into index.html (2026-08-03)

Scope: extracted every `src=`/`data-media-src=` path actually referenced in `index.html`, plus
walked all 13 mounted `data-composition-src` files (`compositions/g-*.html`) — none of the 13
compositions reference `media/` directly, so the audit scope is exactly what `index.html`
references: **148 unique files**. Files sitting on disk but not wired are out of scope.

Method: fetched the licence at the source for every file that had not already been individually
verified in a prior pass this session (Wikimedia file pages, the live NWS Norman event page,
DVIDS pages, archive.org item pages, a Commons audio file page) — `provenance.csv` itself was
treated as the thing being audited, never as evidence. Two Bash/curl calls and one NARA API
attempt were blocked or returned a JS-shell page instead of data; those are called out inline
rather than silently marked verified.

## Bucket counts (148 total)

| Bucket | Count |
|---|---|
| SAFE-PD | 84 |
| SAFE-ATTRIBUTION | 39 |
| SHARE-ALIKE | 0 (already pulled by team-lead before this audit) |
| NON-COMMERCIAL / NO-DERIVATIVES | 0 |
| BROADCAST-CLAIMS | 8 |
| **FLAGGED (see below — was mislabeled SAFE-PD in provenance.csv)** | **9** |

The 9 flagged rows split as: 1 disputed-licence Commons file (RaXPol) and 8 third-party
"photo courtesy" images on the NWS Norman event page that are NOT government-authored despite
living on a `.gov` URL. All 9 are corrected in `provenance.csv` as of this pass — none carry a
license.

---

## FLAGGED — act on these (9 files)

### 1. Commons file with an active deletion dispute
| File | Finding |
|---|---|
| `media/wikimedia/wikimedia-raxpol-radar-2324z.png` | Source: `commons.wikimedia.org/wiki/File:2013_El_Reno_tornado_RaXPol_2013-05-31_2324Z.png`. The file page itself carries a **pending deletion nomination**: "Data shown in the file is from the University of Oklahoma's (OU) Rapid X-band Polarimetric Radar (RaXPol), which does not have licensed or public domain works," and OU "encourages RaXPol data usage only through formal publications... with acknowledgement." RaXPol is a university research instrument, not a federal agency — NWS using the data operationally does not make OU's data federal-employee PD. The Commons "PD" template on this file is disputed by Commons' own community, not settled. **Recommend: pull, same treatment as the Nolte photo.** |

### 2. Third-party "photo courtesy" images on the NWS Norman page (8 files)
None of these are NWS staff work. The live page (`weather.gov/oun/events-20130531`) captions
each one with an individual photographer's name and the word "courtesy" — a display credit,
not a licence grant. Hosting on a `.gov` domain does not convert a viewer submission into
federal public domain; PD under 17 U.S.C. §105 only covers works made by a federal employee in
the course of duty.

| File | Live-page caption found |
|---|---|
| `media/weathergov/wxgov-storm-photo-brennan-jontz.jpg` | "El Reno, OK Supercell - **Photo courtesy Brennan Joseph**" |
| `media/weathergov/wxgov-supercell-photo-magnuson.jpg` | "El Reno, OK Supercell from Above - **Photo courtesy Tom Magnuson**" |
| `media/weathergov/wxgov-storm-photo-elreno-1.jpg` | "El Reno, OK Tornado: **Photos Courtesy of Jeff Snyder**" (one caption covers all 6 in the series) |
| `media/weathergov/wxgov-storm-photo-elreno-2.jpg` | same Jeff Snyder series |
| `media/weathergov/wxgov-storm-photo-elreno-3.jpg` | same Jeff Snyder series |
| `media/weathergov/wxgov-storm-photo-elreno-4.jpg` | same Jeff Snyder series |
| `media/weathergov/wxgov-storm-photo-elreno-5.jpg` | same Jeff Snyder series |
| `media/weathergov/wxgov-storm-photo-elreno-6.jpg` | same Jeff Snyder series |

No CC licence, no reuse grant, no contact/permission trail found for any of the three named
photographers (Brennan Joseph, Tom Magnuson, Jeff Snyder). **Recommend: pull all 8**, per the
channel's own "credit ≠ license" rule — this is functionally identical to unlicensed
storm-photographer content, just routed through a `.gov` display page instead of YouTube.

By contrast, the REMAINING 20 wired `weathergov/` files (damage-survey photos, maps, hydro
graphics, the two safety-graphic PNGs, the satellite-loop mp4) carry **no** photographer credit
on the live page — consistent with NWS-staff-authored survey/analysis product, kept as SAFE-PD.

---

## UNVERIFIABLE — tool access notes (not a separate bucket; folded into the counts above)
- `catalog.archives.gov` (FEMA/NARA source for the 5 `fema/` files) returned an empty React-SPA
  shell to both WebFetch and a direct `curl` hit on `/api/v2/records/search` — the real API
  needs a different base path/key this pass didn't have. Classified the 5 FEMA files as
  SAFE-PD on domain + agency-level confidence (Andrea Booher is FEMA Public Affairs staff, and
  17 U.S.C. §105 covers FEMA the same as NWS) rather than a live per-file confirmation — saying
  so rather than silently marking it fully verified.
- Two `weather.gov` binary fetches (a satellite gif, one damage jpg) hit the fetch tool's
  10 MB content-length cap; both errors confirmed *live, real* content at the URL (one image
  did come through at 932 KB), so treated as domain-confirmed, not as a failure to reach the
  source.

## Broadcast channel spot-check
Re-verified 2 of the 8 unique broadcast source videos directly via `yt-dlp -j` (not from
provenance.csv): CNN (`UCupvZG-5ko_eiXAupbDfxWw`) and KFOR Oklahoma's News 4
(`UCEUYiWFyzpEBMZ3aG7ud7xg`) — both channel_ids matched what provenance.csv already recorded.
Did not re-run this for all 8 (KOCO, The Weather Channel entries) — those already carry
recorded channel_ids from the original sourcing pass and OWNER-APPROVED status from
2026-08-02; flagging that this was a spot-check, not exhaustive, per the audit's own standard.

---

## Full file list by category

### SAFE-PD (84)

**ai/ — self-made AI stills, no third-party rights (9)**
ai-multi-vortex-tornado-v1.png, ai-multi-vortex-tornado-v2.png, ai-night-city-flooding-v1.png,
ai-night-city-flooding-v2.png, ai-rain-wrapped-tornado-v2.png, ai-rural-section-road-v1.png,
ai-rural-section-road-v2.png, ai-supercell-structure-v1.png, ai-supercell-structure-v2.png
— DeAPI-generated per provenance.csv, consistent across the repo's other episodes.

**dvids/ — DoD/National Guard, PD (7)**
dvids-guardsman-firefighter-rubble-search-9148500.jpg, dvids-moore-137th-arw-938052.jpg,
dvids-moore-137th-arw-938056.jpg, dvids-moore-137th-arw-938060.jpg,
dvids-oknatlguard-response-940434.jpg, dvids-oknatlguard-response-940441.jpg,
dvids-oknatlguard-response-940448.jpg — 3 of 7 individually re-verified live on dvidshub.net
this pass (explicit "PUBLIC DOMAIN" banner + named military photographer on each); remaining 4
share the identical dvidshub.net PD pattern.

**fema/ — FEMA/NARA, PD (5, domain-confidence — see note above)**
fema-booher-elreno-damage-03.jpg, -04.jpg, -09.jpg, -10.jpg, -11.jpg — Andrea Booher, FEMA
Public Affairs, NARA record group 311.

**nwsnorman/ — NWS Norman YouTube channel, PD (10)**
nwsnorman-briefing-may17-18-b.mp4, nwsnorman-briefing-may18-20-outlook.mp4,
nwsnorman-elreno-may31-745am-update.mp4, nwsnorman-elreno-radar-loop-a.mp4,
nwsnorman-moore-may20-briefing-a.mp4, nwsnorman-moore-may20-office-broll.mp4,
nwsnorman-receiving-the-warning.mp4, nwsnorman-roundtable-staff-recollections.mp4,
nwsnorman-spotter-training-d.mp4, nwsnorman-spotter-training-f.mp4 — official NWSNorman channel
(carried over from the documentary-sourcing pass's channel verification).

**radar/cdt/ — self-made NEXRAD renders from PD federal data (20)**
All 16 `ktlx-ref-*` + 4 `ktlx-vel-*` files — self-rendered (pyart, per
research/footage_sources.md's documented pattern) from raw NEXRAD Level-II data pulled from the
public `gcp-public-data-nexrad-l2` bucket (confirmed reachable, no auth). Self-made graphic
from PD federal data; no third-party rights.

**sfx/ — CC0/PD library assets (6)**
01_rain_street_medium.mp3 (archive.org, CC0 1.0 — verified live), 03_tornado_siren_waver.ogg
(Wikimedia Commons, PD, Techtonic — verified live), 03b_tornado_siren_constant.ogg (same,
verified live), 04_distant_storm_rumble.mp3 (archive.org, CC0 1.0 — verified live),
05_town_evening_crickets.mp3 (archive.org, CC0 1.0 — verified live), rain-loop.mp3 (self-made
loop derived from 01, inherits CC0). **Note:** the shared `assets/sfx/provenance.md` doc
wrongly lists 01/04/05 as "Pixabay" — stale/contradicts the real CC0 archive.org sources
actually used; worth a separate fix outside this episode.

**spc/ — NOAA/SPC, PD (1)**
spc-satellite-tornado-9frame-anim.mp4 — derived mp4 of the SPC-hosted gif at
`spc.noaa.gov/publications/edwards/st-anim.gif`; live-fetched this pass, genuine GIF with
embedded "J. Snyder — jeffrey.snyder@noaa.gov" metadata confirming NOAA-employee authorship.

**weathergov/ — NWS Norman event page, PD, NO photographer credit found (20)**
wxgov-damage-01/03/05/06/07/08/10.jpg (7), wxgov-map-ef-contour-timing.jpg,
wxgov-map-ingredients.png, wxgov-map-overview1.png, wxgov-map-overview2.png,
wxgov-map-pns-damage-path.png, wxgov-map-polygons-okc-metro.jpg, wxgov-map-storm-reports.jpg
(7), wxgov-hydro-24hr-mpe.png, wxgov-hydro-exceedance-probabilities.png,
wxgov-hydro-rainfall-48hr.png (3), wxgov-graphic-car-safety.png, wxgov-graphic-tornado-safety.png
(2), wxgov-satellite-loop-elreno.mp4 (1) — live-page captions checked category-by-category this
pass; none carry a "courtesy"/named-photographer credit, consistent with NWS-staff survey work.

**wikimedia/ — PD (9)**
wikimedia-samaras-car-PDgov.jpg, wikimedia-tim-samaras-portrait-PDgov.jpg,
wikimedia-elreno-radar-2310z.png, wikimedia-ground-scar.jpg,
wikimedia-highest-rated-damage-indicator.jpg, wikimedia-preliminary-ef5-rating-survey.jpg,
wikimedia-preliminary-okc-tornado-tracks-map.png, wikimedia-preliminary-tornado-track-map.png,
wikimedia-phased-array-radar-reflectivity.mp4 — every one individually fetched at the Commons
file page this pass (or a prior pass this session); all confirmed PD-USGov (NOAA/NWS Norman or
NASA).

**music/ — self-made AI, no third-party rights (5)**
m-dread-5x.mp3, m-hopeful-1x.mp3, m-neutral-3x.mp3, m-somber-2x.mp3, m-tense-3x.mp3 — DeAPI
ACE-Step generated per DESIGN.md's music policy. **Gap noted, not a licence problem:** LEARNINGS
says ACE request-ids should live in `media/music/provenance.txt`; no such file exists for this
episode's music pool.

### SAFE-ATTRIBUTION (39) — needs a description credit

**wikimedia/ — CC BY (5)**
wikimedia-carl-young-portrait-CCBY.jpg, wikimedia-twistex-hitpr-probe-CCBY.jpg,
wikimedia-twistex-mesonet-vehicles-CCBY.jpg (all 3: Tony Laubach, CC BY 3.0),
wikimedia-ef5-tornado-CCBY-rodriguez.jpg, wikimedia-ef5-tornado-wedge.jpg (both: Daniel
Rodriguez, CC BY 2.0).

**stock/ — Pexels License (30) + Pixabay License (4)**
Pexels: dashboard-pov-rain-01/03/04/05, dawn-dusk-sky-01/02/04/05,
emergency-lights-rain-03/04, highway-traffic-rain-02/04/06, night-flood-street-01/03/05,
plains-wheat-01/04/05/06, radio-closeup-04, rainwall-pavement-01/03/04/05/06,
supercell-timelapse-02/04/05/06 (30 files — 1 URL spot-checked live this pass, confirmed
genuine Pexels page).
Pixabay: lightning-02, stormsky-timelapse-01/04/05 (4 files, all `pixabay.com/videos/id-*`
URLs per provenance.csv, not individually re-fetched this pass beyond domain pattern).

### BROADCAST-CLAIMS (8) — claims-budgeted per owner-approved policy

**Wired directly (3):** broadcast/kfor-sutton-very-close-call-hookcut.mp4 (KFOR),
broadcast/twc-bettes-describes-direct-hit.mp4 (The Weather Channel),
broadcast/twc-bettes-suv-toss-marquee.mp4 (The Weather Channel).

**Wired as audio-only inserts, derived from an already-approved broadcast source (5):**
inserts/ins-30seconds.m4a ← koco-survivor-testimony-c.mp4 (KOCO),
inserts/ins-bettes-mylife.m4a ← cnn-storm-reporting-dangerous.mp4 (CNN),
inserts/ins-gillig-survived.m4a ← kfor-2019-survivor-testimony.mp4 (KFOR),
inserts/ins-samaras-vehicle.m4a ← cnn-ethics-of-chasing.mp4 (CNN),
inserts/ins-thought-die.m4a ← koco-survivor-testimony-b.mp4 (KOCO).
All 5 source videos are OWNER-APPROVED 2026-08-02 in the existing provenance rows; channel_id
for CNN and KFOR re-verified live via `yt-dlp -j` this pass.
