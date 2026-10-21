# factcheck-B: storm, rain, mechanism (I1-S1, S2, S3, S4, S5, S6, S7, S9, S10)

Checked 21 Oct 2026 against edit_script.md (HEAD 3c3799dc working tree). Verifier only: script and facts-*.md untouched.
How read: PDFs downloaded to a scratch dir and read through the text layer (pdftotext). OFR 70-51 Table 1 row (trash barrel) also read as a rendered page image (the text layer scrambles the table columns). HTML pages by curl, tags stripped. Printed page numbers unless "pdf p." is given.
Verdict key: CONFIRMED = spoken wording holds. CORRECTED = replacement line given. UNVERIFIED = cut.

## Summary
| Item | Verdict |
|---|---|
| I1-S1 landfall "just before midnight", Aug 17 | CONFIRMED, soften time (11 PM CDT is an hour before midnight) |
| I1-S1 "about 175 mph" | CONFIRMED (reanalysis, label it) |
| I1-S1 "143 on the Gulf Coast" | CONFIRMED to NWS Jackson only (single source, keep "Weather Service" on screen) |
| I1-S2 "wasn't even calling it a hurricane anymore" | CONFIRMED (marker can drop) |
| I1-S2 "nearly half" (113 of 256) | CORRECTED: 44 percent is "more than four in ten" |
| I1-S3 rain, 7 p.m., 8 hours, 27 inches | CONFIRMED |
| I1-S4 trash barrel | CONFIRMED as a fact; "one of the best measurements" is NOT in the source: CORRECTED |
| I1-S5 1956 probable maximum, 28 in 6 h | CONFIRMED sentence; CORRECTED wording ("the most rain it figured could ever fall" overstates; also the graphic must not equate 27 in 8 h with 28 in 6 h) |
| I1-S6 "whole hillsides came down ... asleep" | CORRECTED: scars are strips; "asleep" is a single NWS generalization |
| I1-S7 PP 804 abstract sentence | CONFIRMED exact; "geologists" CORRECTED to "USGS scientists" |
| I1-S9 Davis Creek 2 of 25, 27 dead, 22 missing | CONFIRMED figures; "by that fall" CORRECTED (sentence is undated) |
| I1-S10 113 dead and 39 missing, 13 Nov 1969 | CONFIRMED |

## 1. I1-S2 status over Virginia, 19 Aug 1969 (evening)
Verdict: CONFIRMED for "wasn't even calling it a hurricane anymore". Official status: tropical depression (best track), "remnants" in the contemporary text.

Quotes (raw):
- HURDAT2 (NHC current best track, file hurdat2-1851-2025-092326.txt, https://www.nhc.noaa.gov/data/hurdat/), storm AL091969 CAMILLE:
  `19690819, 0600, TD, 36.0N, 89.3W, 30` / `19690819, 1200, TD, 37.0N, 88.0W, 30` / `19690819, 1800, TD, 37.6N, 86.0W, 25` / `19690820, 0000, TD, 37.6N, 84.0W, 25` / `19690820, 0600, TD, 37.4N, 80.6W, 25` / `19690820, 1200, TD, 37.2N, 77.3W, 30` / `19690820, 1800, TS, 37.0N, 75.3W, 45`.
  Hurricane status ends at 19690818 1200 UTC (HU, 75 kt); TS 18 Aug 1800 UTC; TD from 19 Aug 0600 UTC. 20 Aug 0000 UTC = 8 PM EDT on the 19th (center over Kentucky, 84.0W); 0600 UTC = 2 AM EDT on the 20th (southwest Virginia, 80.6W); 1200 UTC near Richmond (77.3W).
- Kieper, Landsea, Beven 2016, BAMS 97(3) 367-384, https://repository.library.noaa.gov/view/noaa/15209/noaa_15209_DS1.pdf, p. 368: "...when Camille was inland as a tropical depression over Kentucky." Table 1 (p. 380) lists "Tropical depression" for the 19 and 20 Aug rows (the text-layer table is scrambled; HURDAT2 is the clean copy).
- Camp and Miller 1970, USGS OFR 70-51 (https://pubs.usgs.gov/of/1970/0051/report.pdf), Abstract p. 1: "Hurricane Camille became a tropical depression and soaked central Virginia with up to 28 inches of rain during the night of August 19th and morning of the 20th." p. 5 (ESSA-Weather Bureau Staff chapter "The Storm"): "During the evening of the 19th and early morning of the 20th, the remnants of Camille intensified rapidly as she crossed the Appalachian Mountain ridges." and "Near midnight, the low pressure center began to intensify as it moved eastward into Virginia along a track south of Roanoke and Lynchburg."
- Contemporary Weather Bureau advisory table, reproduced in US Army Engineer District Mobile, "Report on Hurricane Camille 14-22 August 1969" (May 1970), Table 1, "Summary of Weather Bureau advisories and bulletins": row "11 a.m. 18 ... 33.0 90.1 Warnings discontinued"; row "2 p.m. 18 ... 33.5 90.1 Heavy rains and flash flooding"; next row is "5 a.m. 21 ... Gaining strength in Atlantic". No advisory rows for 19 and 20 Aug. Same report, section 6 "Overland": "the storm weakened rapidly and was a tropical depression before reaching the northern Mississippi border. As a depression, Camille moved north-northeastward through western Tennessee, east-northeastward through central Kentucky, and eastward through extreme southern West Virginia and southern Virginia. Late Tuesday evening, 19 August, the remnants of the storm produced torrential rainfall..." URL: https://biotech.law.lsu.edu/blog/H_CAMILLE.pdf (LSU-hosted scan, OCR text layer; a Corps document quoting Weather Bureau text, so SECONDARY for agency wording but contemporary).
- NWS Jackson (https://www.weather.gov/jan/1969_08_17_hurricane_camille): "Camille weakened to a tropical depression as it crossed Mississippi into western Tennessee and Kentucky, then it turned eastward across West Virginia and Virginia."
Finding: by the evening of 19 Aug it was a tropical depression, the Weather Bureau had ended hurricane warnings on the morning of the 18th and had no advisories until it regained tropical-storm strength offshore on the 20th/21st. "Wasn't even calling it a hurricane anymore" holds. Marker can be dropped. Optional stronger true line: "...and it had not been a hurricane for more than a day." (hurricane to 1200 UTC 18 Aug; the evening of the 19th is about 40 hours later).
Caveat: the center was still over Kentucky at 8 PM EDT and crossed into Virginia near midnight; "was crossing Virginia" is right for the night, not the early evening. The rain was already falling in Virginia by about 7 p.m. (OFR p. 7).

### "Nearly half" (113 of 256)
Verdict: CORRECTED.
- Raw, NWS Jackson: "The combination of winds, surges, and rainfalls caused 256 deaths (143 on the Gulf Coast and 113 in the Virginia floods) and $1.421 billion in damage. Three deaths were reported in Cuba." (page re-read raw 21 Oct 2026, curl, tags stripped.)
- 143 + 113 = 256 holds. 113 / 256 = 0.4414 = 44 percent. "Nearly half" stretches 44 percent; "more than four in ten" is exact.
- The 113 is the Virginia state-wide total (not only the mountains); Nelson County alone was 114+ to 126 in other counts (P rows). Do not say "Virginia mountains" and "113" as one tight pair without "the Weather Service's count" on screen. Also note the same NWS page says "local totals of up to 31 inches. Most of this rain occurred in 3 to 5 hours" which conflicts with OFR 70-51 (27-28 in, about 8 h); do not cite this page for rain.
Replacement line: "Yet more than four in every ten of the deaths the Weather Service counts for Camille happened right there, in the Virginia mountains." Chip text "NEARLY HALF" -> "OVER 4 IN 10" (or "44 PERCENT").

## 2. I1-S7 PP 804 abstract
Verdict: CONFIRMED (exact sentence, three reads agree). "Geologists": CORRECTED.
Raw, abstract, PP 804 p. 1 (pdf p. 9), https://pubs.usgs.gov/pp/0804/report.pdf, also https://pubs.usgs.gov/publication/pp804: "Most of the 150 people whom the flood killed in this mountainous area died from broken bones and other blunt-force injuries, rather than by drowning. The transport of sediment and other debris by the water therefore was very significant in loss of life and in property damage."
Basis inside the paper (p. 16): "Dr. J. H. Gamble of Lovingston, who was in charge of identifying and examining the flood victims, found that almost none of the dead showed evidence of drowning. 'The vast majority were just multiple fractures ... Most died from massive blunt force injuries.' (Simpson and Simpson, 1970, p. 270)." So the finding rests on the bodies examined; the missing were never examined. "Most of the people the flood took" is the abstract's own sweep, fine for the line, but "the dead" is more exact than "the people it took" (the taken include the never found).
Authors: Garnett P. Williams and Harold P. Guy (title page). Affiliation printed: "Geological Survey Professional Paper". The paper gives no job titles; OFR 70-51 (Camp and Miller) is stamped "Geological Survey, Water Resources Division" and Williams and Guy wrote its sediment chapter. The study is of erosion and sediment (geomorphology). "Geologists" is not supported as a title. Safe noun: "USGS scientists" or "federal scientists". (Title "hydrologist" not found on any page read, so not used.)
Replacement line: "When federal scientists studied it afterward, they found most of the dead hadn't drowned. They had broken bones and blunt-force injuries." Card text unchanged (exact quote shortened with the source's own words; "USGS Professional Paper 804, 1973" correct).
Side finding (for I1-S8, not in my slice): PP 804 p. 16 says "There is no way to determine how many of the 125 people who lost their lives in Nelson County were killed by debris avalanches." (125 is a PP 804 number for Nelson.)

## 3. OFR 70-51 re-read raw
URL: https://pubs.usgs.gov/of/1970/0051/report.pdf (136 pdf pages; printed page = pdf page minus 12). Title: Camp, J.D., and Miller, E.M., "Flood of August 1969 in Virginia", Open-file report, Richmond, Virginia, 1970.
- 1956 probable maximum, p. 7 (pdf p. 19): "A study made by the Weather Bureau in 1956 for the Corps of Engineers concluded that the probable maximum rainfall possible in this area was 28 inches in 6 hours and 31 inches in 12 hours." CONFIRMED verbatim. (The sentence preceding it, same page: "The 27-28 inch rainfall within about 8 hours in Nelson County, Virginia, represents one of the all-time meteorological anomalies in the United States". The report does not itself compare the 27-28 in to the probable maximum; it lists other rainfall records "approaches the following records".)
- Table 1 trash barrel, printed p. 11 (pdf p. 23), read from the page image: row "Nelson | 37 deg 49' | 79 deg 00' | 27" | Trash barrel | Good | Barrel had been emptied afternoon before rain began". CONFIRMED. Column head is "24-hour total (inches)". Other Nelson rows: 25 Barrel Good; 23 street trash container Good (p. 12); 20.4+ plastic garbage container Good; WB Recorder 11+ "Gage overflowed". Accuracy "Good" is also given to many gauges, so "one of the best measurements" is the writer's ranking, not the source's. 27 is the highest figure in Table 1 (31 in at Tye River unverified, p. 7).
- "Most of the rain fell during the 8-hour period beginning about 7 p.m. on the 19th.", p. 7 (pdf p. 19), CONFIRMED verbatim; followed by "Wide publicity was given to a report of 31 inches near Tye River, Va. Attempts to verify this measurement were unsuccessful." A Nelson gauge remark on p. 11: "Hard rain from 8 p.m. to 4 a.m."
- "reliable indications of 27-28 inches in the central part of Nelson County", p. 5-6 (the paragraph runs across the page break; sits on printed p. 6).
- Davis Creek, p. 22 (pdf p. 34), CONFIRMED: "In the Davis Creek community in Nelson County, only two of 25 houses remained. Twenty-seven persons were known dead and 22 were missing from this one hollow."
- p. 1 abstract (pdf p. 13), CONFIRMED: "As of Nov. 13, 1969, the State had counted 113 dead and 102 injured with 39 persons still missing. The total damage amounted to over $116 million." Same sentence repeated p. 22.
Replacement lines:
- I1-S4: "One of the biggest measurements came from a trash barrel somebody had emptied that afternoon, and the survey rated it good." (Card unchanged; it quotes the row's own words.)
- I1-S5: "Thirteen years earlier, the Weather Bureau had worked out, for the Army Corps of Engineers, the probable maximum rainfall for that area. Twenty-eight inches in six hours." Graphic: label the 6-hour limit as 6 hours and the observed bar as "27 to 28 in, about 8 hours"; do not draw 27 under 28 as if same duration (the 12-hour limit is 31 in).
- I1-S9: "In one hollow along Davis Creek, two of twenty-five houses were left, and the federal flood report counted twenty-seven known dead and twenty-two still missing there." (The Davis Creek sentence has no date; "by that fall" is an inference, drop it.)
- I1-S10 holds as written.

## 4. I1-S1 landfall, winds, Gulf Coast toll
- Time, CONFIRMED with softening. HURDAT2: `19690818, 0400, L, HU, 30.3N, 89.4W, 150, 900`. 0400 UTC 18 Aug = 11 PM CDT 17 Aug (Sunday). NWS Lake Charles, https://www.weather.gov/lch/1969Camille: "made landfall near Waveland, Mississippi at 11 PM CDT with maximum sustained winds of 175 mph (150 knots) and a minimum central pressure of 900 millibars (26.58 inches)". BAMS 2016 p. 368: "the eye making landfall near midnight Sunday local time (0400 UTC 18 August)". Contemporary Corps report (quoting 1969 data): "about 11:30 PM CDT on 17 August 1969". "Just before midnight" is fair against the 1969 11:30 value but an hour loose against the reanalysis. Safer: "late on the night of August seventeenth" or "around eleven o'clock that Sunday night". Popfig "Aug 17, 1969 . 11 PM" is right for the reanalysis.
- 175 mph, CONFIRMED: NHC press release 1 Apr 2014, https://www.nhc.noaa.gov/news/20140401_pa_reanalysisCamille.pdf: "peak sustained winds of 175 mph and a central pressure of 900 mb ... reduced from 190 mph". Keep "about" and the on-screen "reanalysis 2014" label; the 1970 and NWS Jackson texts say about 200 mph or 190 mph gusts/old value, so a viewer who knows the older number needs the label.
- 143, CONFIRMED to NWS Jackson only: "256 deaths (143 on the Gulf Coast and 113 in the Virginia floods)". The 1970 Corps report (Red Cross figures) lists Mississippi 137, Louisiana 9, Virginia 114, West Virginia 2 = 262, so the Gulf Coast number differs by source (146 there). Keep "per the Weather Service" in the spoken or on-screen source.

## 5. I1-S6 "whole hillsides came down into the hollows where people were asleep"
Verdict: CORRECTED.
- "Whole hillsides": PP 804 p. 17 (pdf p. 25): "Typical avalanche scars range from about 200-800 feet in horizontal length, 25 to 75 feet in width and 1 to 3 feet in depth. Some scars are as short as 20 feet or as long as 1,000 feet, as wide as 200 feet, and as deep as 15 or 20 feet." The slides are strips of soil, not whole hillsides. PP 804 abstract p. 1: "they usually followed pre-existing depressions on hillsides and occurred on slopes greater than 35 percent".
- Hollows, supported: PP 804 p. 16: "A number of missing houses, particularly in the Davis Creek basin, originally stood in small hollows which were scoured by avalanches."
- In the dark, supported: PP 804 p. 15: "Observations during the present storm were obscured because of the darkness." Slides ran to "about 0400 hours on August 20" (p. 16).
- Asleep: only NWS Sterling, https://www.weather.gov/lwx/hurricane_history (raw 21 Oct 2026): "Most residents were asleep during the storm, which had been unpredicted. There was no way to warn anyone of the impending catastrophe, because phone lines were obliterated along with everything else..." It is an uncited agency generalization on a page that also says "Camille dumped 31 inches of rain in six hours" (contradicts OFR 70-51's unverified-31 and 8 hours). USGS says nothing about sleeping. Rain began about 7 p.m. (OFR p. 7), so many were awake for hours. Treat "asleep" as unverified as a flat statement.
Replacement line: "On the steep slopes above the creeks, the soaked ground let go in the dark, long strips of hillside sliding down into the hollows where people lived." If the owner wants "asleep", it needs a named survivor or the attributed form "the Weather Service says most residents were asleep" (not recommended).
Also: PP 804 does not support "whole hillsides"; do not show a picture of a whole mountainside sliding. The cross-section should show a narrow tongue of soil.

## Open items
- Operational 1969 Weather Bureau advisory text for 19 Aug not found (no advisories were issued; the Corps report table shows none). MWR Simpson et al. 1970 (98(4): 293-306) returned 403 at AMS; not read. HURDAT2 + BAMS + OFR 70-51 + Corps table suffice for the line.
- Neither author's job title found; do not use "hydrologist" or "geologist".
