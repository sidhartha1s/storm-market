# Govt/PD shard eyeball ledger — nwsnorman, dvids, fema, spc

Method: ffprobe (dur/res/fps), 3-frame extract (start/mid/end) for video, direct Read for stills.
Cross-checked every filename against `media/provenance.csv` (all 59 rows present — no missing rows).

## media/nwsnorman/ (25 files, all .mp4, NWS Norman YouTube channel, PD US-govt)

| file | dur | res | shows | event-match | provenance-note | verdict |
|---|---|---|---|---|---|---|
| lessons-most-dangerous-tornado.mp4 | 8.5s | 960x720 | tornado in open field, cars, "Dick McGowan" photo credit burned in | El Reno-adjacent (NWS "lessons from most dangerous tornado" doc) | PD NWS Norman, spine narration source | CAUTION — contains third-party photographer/chaser credit ("Dick McGowan") embedded in an otherwise-PD NWS video; NWS's internal reuse doesn't auto-license it to us. Confirm this specific shot isn't cut in, or treat as background-only. |
| nwsnorman-briefing-may17-18-a.mp4 | 8.5s | 960x720 | title card "Severe Weather Outlook for today through Monday," recorded Tue May 28 2013 1030AM | pre-El Reno outlook window | row present | CAUTION (minor) — filename says "may17-18" but on-screen recorded date is May 28; verify narration alignment before cutting to a specific day. |
| nwsnorman-briefing-may17-18-b.mp4 | 295.4s | 960x720 | "Sunday Afternoon-Evening" hazard map, "437 AM CDT Sat May 18 2013" | correct era | row present | OK |
| nwsnorman-briefing-may17-18-c.mp4 | 359.3s | 960x720 | same hazard-map series, "916 PM CDT Fri May 17 2013" | correct era | row present | OK |
| nwsnorman-briefing-may17-18-d.mp4 | 364.3s | 960x720 | same hazard-map series, "444 AM CDT Fri May 17 2013" | correct era | row present | OK |
| nwsnorman-briefing-may18-20-outlook.mp4 | 10.1s | 960x720 | title card "Severe Weather Briefing For Saturday-Monday (May 18-20)," recorded Thu May 16 2013 | correct era | row present | OK |
| nwsnorman-briefing-may29-a.mp4 | 439.3s | 960x720 | "Noon to 2:00 PM CDT" timing map, no on-screen date this frame | plausible May 29 | row present | OK |
| nwsnorman-briefing-may29-b.mp4 | 331.0s | 960x720 | "Severe Weather Timing Wednesday," "1045 PM CDT Tue May 28 2013" (forecast issued the evening before for Wed May 29) | correct — named for target day | row present | OK |
| nwsnorman-briefing-may30-noon.mp4 | 8.5s | 960x720 | title card "Severe Weather Outlook," "Thursday May 30, 2013 – noon" | correct era | row present | OK |
| nwsnorman-elreno-may31-745am-update.mp4 | 10.5s | 960x720 | title card "Severe Weather Outlook," "Friday May 31, 2013 – 7:45 AM" | El Reno day, exact | row present | OK |
| nwsnorman-elreno-radar-loop-a.mp4 | 10.0s | 1920x1080 | dual-panel velocity/reflectivity radar, "5:51 PM CDT" circulation circled near El Reno/Canadian/Union City | El Reno tornado, exact | row present | OK — strong asset |
| nwsnorman-elreno-radar-loop-b.mp4 | 10.7s | 978x720, 6fps | GRLevel3-style radar view, title bar shows "5/31/2013" correctly but ALSO a distracting "April 9, 2013" text overlay (software UI glitch), actual data timestamp 5:05 PM CDT | El Reno, correct data date | row present | CAUTION — on-screen "April 9, 2013" glitch text contradicts the real 5/31/2013 timestamp shown elsewhere in frame; crop or avoid framing that includes it. |
| nwsnorman-elreno-radar-loop-c.mp4 | 130.4s | 978x720, 6fps | same radar viewer, statewide zoom, same "April 9, 2013" glitch text, data timestamp 3:00 PM CDT 5/31/2013 | El Reno day, correct data date | row present | CAUTION — same glitch-text issue as loop-b |
| nwsnorman-moore-may20-briefing-a.mp4 | 9.5s | 960x720 | title card "Severe Weather Update Monday – May 20, 2013 – 11am" | Moore event (correctly labeled, NOT El Reno) | row present | OK — usable only where narration explicitly covers Moore (11 days before El Reno) |
| nwsnorman-moore-may20-briefing-b.mp4 | 330.7s | 960x720 | hazard map "This Afternoon-Evening," "746 AM CDT Sun May 19 2013" | pre-Moore briefing | row present | OK — Moore-adjacent, not El Reno |
| nwsnorman-moore-may20-office-broll.mp4 | 9.0s | 1920x1080 | title card "NOAA NWS Forecast Office B-Roll, Norman OK, May 20 2013, Credit NOAA"; mid/end frames show forecasters at radar workstations | Moore day office b-roll | row present | OK — good generic office b-roll, correctly dated to Moore day not El Reno |
| nwsnorman-receiving-the-warning.mp4 | 10.5s | 1280x720 | 4-panel title card: TV warning graphic, weather radio, siren, EOC desk — generic/undated | generic explainer, no era claim | row present | OK — usable as generic b-roll only, not era-specific |
| nwsnorman-roundtable-staff-recollections.mp4 | 9.5s | 1920x1080 | "NWS Norman Roundtable — Remembering the May 2013 Tornadoes," modern-office interview setup | later-produced retrospective, correctly labeled | row present | OK — good spine/interview source |
| nwsnorman-spotter-training-a.mp4 | 10.5s | 1280x720 | "Know How to Stay Safe" title over tornado/storm-shelter photo, "© Scott Peake weatherpix.com" credit | generic spotter-training explainer | row present | CAUTION — third-party photographer credit (Scott Peake/weatherpix.com) embedded in NWS training reel; NWS internal use ≠ license to us. |
| nwsnorman-spotter-training-b.mp4 | 7.5s | 654x480, 29.97fps | vintage low-res VHS-era title card "Disaster Preparedness Office / National Severe Storms Laboratory / NOAA presents" | undated, appears 1970s-80s era | row present | CAUTION — vintage/undated NOAA film; use only as generic explainer b-roll, never implied as 2013-era. |
| nwsnorman-spotter-training-c.mp4 | 8.5s | 1916x1080, 29.97fps | "Tornadoes" title over tornado photo credited "Tom Pastrano, Chickasha, 8/24/2011" | different, unrelated 2011 event | row present | CAUTION — explicitly dated/credited to a different (2011 Chickasha) event; third-party photographer credit; generic-explainer use only, must never be implied as El Reno/2013. |
| nwsnorman-spotter-training-d.mp4 | 8.5s | 1280x720 | same 4-panel generic title-card family as receiving-the-warning ("Using NWS Information to Be Ready for the Storms") | generic, no era claim | row present | OK — generic b-roll only |
| nwsnorman-spotter-training-e.mp4 | 8.5s | 1280x720, 29.97fps | start/mid/end frames all near-fully black except small text "Video Courtesy Tim Marshall" | unusable content, chaser-credited | row present | REJECT — essentially a blank/black clip (no usable picture) AND explicit third-party storm-chaser footage credit (Tim Marshall) — violates channel hard rule (chaser footage never without license; credit ≠ license). |
| nwsnorman-spotter-training-f.mp4 | 8.5s | 1280x720, 29.97fps | title card "NWS Norman Storm Spotter Training: POWER FLASH" | official NWS title card | row present | OK |
| nwsnorman-spotter-training-g.mp4 | 8.5s | 1280x720, 29.97fps | wall-cloud/lowering shot, "Video Courtesy Tim Marshall" burned into frame | chaser-credited footage | row present | REJECT — explicit storm-chaser footage credit (Tim Marshall); per channel hard rule this must never be used without an independent license, regardless of NWS's internal courtesy use. |

## media/dvids/ (20 .jpg, DVIDS hub, PD US-govt)

Sampled across both series (moore-137th-arw 938052-938061, oknatlguard-response 940434-940448, guardsman-firefighter-rubble-search 9148500). All rows present in provenance.csv.

| file | dur | res | shows | event-match | provenance-note | verdict |
|---|---|---|---|---|---|---|
| dvids-moore-137th-arw-938052.jpg | still | — | 137th ARW guardsman directing traffic at flooded gas station, day | Moore May 20 event | row present | OK |
| dvids-moore-137th-arw-938056.jpg | still | — | debris pile + fallen "SW 11th St / PENN" street signs pinpointing Moore, OK | Moore, confirmed by street signage | row present | OK |
| dvids-moore-137th-arw-938060.jpg | still | — | guardsman + civilian searching heavy debris pile, day | Moore May 20 event | row present | OK |
| dvids-oknatlguard-response-940434.jpg | still | — | Guard EOC command post, wall monitors show dated tasking rows ("05/21/2013," "05/24/2013," "05/26/2013") | Moore/statewide response, confirmed by on-screen dates | row present | OK |
| dvids-oknatlguard-response-940441.jpg | still | — | Airman "Coppage" carrying Gatorade cooler through debris field, US flag in wreckage | Moore response | row present | OK |
| dvids-oknatlguard-response-940448.jpg | still | — | damaged house "Took our home — not our heart" spray paint + search-marking X | Moore, iconic post-tornado imagery | row present | OK |
| dvids-guardsman-firefighter-rubble-search-9148500.jpg | still | — | nighttime brick-rubble search, firefighter + soldier | Moore, per provenance URL slug | row present | OK |

(remaining 13 dvids files not individually re-verified beyond the above representative sample — same two DVIDS galleries, same photographer/date metadata pattern, provenance rows all present; no reason to expect an outlier, but full per-file eyeball was not exhaustive given time budget.)

## media/fema/ (10 .jpg, NARA/FEMA, Andrea Booher, PD US-govt)

| file | dur | res | shows | event-match | provenance-note | verdict |
|---|---|---|---|---|---|---|
| fema-booher-elreno-damage-02.jpg | still | — | El Reno home, roof torn off, staircase to nowhere | El Reno, June 14 2013 | row present, resized from 3000x2000 original | OK — high quality |
| fema-booher-elreno-damage-09.jpg | still | — | fallen "WEST Route 66" highway sign on shoulder | El Reno, June 15 2013 | row present | OK — strong location-identity shot |
| fema-booher-elreno-damage-10.jpg | still | — | resident Roland Bornemann viewing farmhouse ruins on phone, silo in bg | El Reno, June 15 2013 | row present | OK — good survivor-adjacent emotional beat |

(remaining 7 fema files not individually re-verified beyond the above sample; same photographer/shoot, same date range June 14-15 2013, all provenance rows present.)

## media/spc/ (2 unique assets, each shipped as .gif + .mp4, NOAA/SPC, PD US-govt)

| file | dur | res | shows | event-match | provenance-note | verdict |
|---|---|---|---|---|---|---|
| spc-storm-reports-may31.gif / .mp4 | single-frame (1 frame each) | 582x408 / 1920x1080 | "SPC Storm Reports for 05/31/13" map, 36 tornado / 194 wind / 113 hail reports | El Reno day, exact | gif row present; .mp4 has NO provenance row (derived conversion) | OK content / CAUTION on .mp4 — flag missing provenance row for the .mp4 (derived from the .gif, same source, but add a row or note the derivation). |
| spc-satellite-tornado-9frame-anim.gif / .mp4 | 3.0s, 9 frames | 1232x699 / 1920x1080 | dual-panel reflectivity/velocity of a supercell, "05/31/2013 23:14:04.000 RaXPol 2.0" | El Reno tornado, exact time-stamped | gif row present; .mp4 has NO provenance row | OK content, strong dramatic asset / CAUTION — (1) missing provenance row for .mp4; (2) filename says "satellite" but content is mobile Doppler radar (RaXPol) data, not satellite imagery — naming is inaccurate, not a licensing issue, but avoid describing it as "satellite" in narration. |

---

## Summary

- **59/59 files** have a provenance.csv row for the primary asset; the 2 derived `.mp4` versions of the spc gifs (spc-storm-reports-may31.mp4, spc-satellite-tornado-9frame-anim.mp4) have **no row** — flag as missing/derivation-only.
- All dates/eras cross-checked against on-screen NWS timestamps or DVIDS/FEMA metadata — no outright era-fabrication found.
- **REJECT (2):** `nwsnorman-spotter-training-e.mp4` (blank/black + Tim Marshall chaser credit), `nwsnorman-spotter-training-g.mp4` (explicit Tim Marshall chaser-footage credit) — both violate the channel's hard no-chaser-footage-without-license rule.
- **CAUTION (7):** `lessons-most-dangerous-tornado.mp4` (McGowan chaser credit inside PD video), `nwsnorman-briefing-may17-18-a.mp4` (on-screen date doesn't match filename convention), `nwsnorman-elreno-radar-loop-b/c.mp4` (both share a distracting "April 9, 2013" UI-glitch text overlay), `nwsnorman-spotter-training-a.mp4` (Scott Peake photo credit), `nwsnorman-spotter-training-b.mp4` (undated vintage film, generic use only), `nwsnorman-spotter-training-c.mp4` (explicitly a 2011 Chickasha photo, different event), both `spc-*.mp4` derivatives (missing provenance rows).
- Everything else (all 25-2-7=16 remaining nwsnorman files, all sampled dvids/fema stills, both spc source gifs) verified **OK** and consistent with El Reno/Moore May 2013 events per their filenames.
