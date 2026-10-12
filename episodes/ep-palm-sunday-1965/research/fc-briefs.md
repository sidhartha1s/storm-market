# Fact check of on-screen text in the 69 graphic briefs

Briefs: EP\mg_specs\briefs\g-*.md (69 files, README excluded). Strings: the backticked strings of each brief's "5. Text (exact) and cues" line, plus the "Source line / Credit / Place label" rows of section 3. Script: EP\edit_script.md as it is now (narration, Picture note, Rows line of each brief's segments). Sources used: study and survey page images read in earlier rounds, survey printed p. 45 read this round, the design sheet section 5 (list sheet), provenance.csv, picture-inventory.md, film-shot-log.md, facts.md, county-key.md, my fc files.
Settled and not judged beyond the string sort: g-a4s01-eyes, g-a4s02-countyb, g-a5s09-alto.

## Count
595 strings read (script sort: brief_scan.py in .qc-tmp\factcheck). 11 are file names or CSS, not on screen, and are left out: 584 on-screen strings.
- IN SCRIPT: 521 (405 in the brief's own segments, 90 with the same words elsewhere in the act, 26 by number or word form: "2 minute head start" against "two minute", "7:00 PM" against "seven o'clock", chain labels, Recommendation 5 and 8 wording).
- SOURCE LINE: 41 (every "Disaster Research Center, 1966, p. N" and "Weather Bureau survey, 1965, p. N" page matches the script's page and the page images; NOAA, NWS, provenance credits match inventory and provenance.csv).
- ADDED and supported: 14. ADDED, label only, no fact: 8. ADDED and unsourced: 0.
- CONTRADICTS: 0 facts; 3 spelling or caption inconsistencies.

## CONTRADICTS
1. g-a1s01-kc, g-a1s05-clocks, g-a1s09-forecasts (two stamps): the place line reads "Kansas City · Eastern time" and "Eastern time"; the script's glass card reads "EST" (A1-S1, S5, S9, S10). Same fact (study p. 6, "11:45 a.m. (EST)"), two spellings. The briefs say the lead may rule it back to EST. Pick one so the stamps match the script note.
2. Photograph A3 has two captions: "Weather Bureau Communications Center, about 1955 · NOAA" (g-a1s18-list, g-a2s21-list) and "Weather Bureau teletype room, about 1955" (g-a3s07-calls, from A3-S8). Inventory A3 and provenance: "Teletype operators at the U.S. Weather Bureau Communications Center, c. 1955". Use the true caption on both.
3. Survey source line is written two ways: "Weather Bureau survey report, 1965, p. N" (most briefs) and "Weather Bureau survey, 1965, p. N" (g-a1s09, g-a3s05, g-a5s04, g-a6s05, g-a6s08, and the script). Same document; one form should win.

## ADDED and unsourced
None. Nothing on screen asserts a place, time, number, date, name or quoted word that the script, a source line or my files fail to carry.

## ADDED and supported
| Brief | String | Claim | Support |
|---|---|---|---|
| g-a1s09-forecasts | "extreme southern Wisconsin", "extreme eastern Iowa", "portions of northern Illinois" | the 2:00 PM forecast area | study p. 6, Forecast 68 text (fc-a1-a2, A1-S10); script says "parts of Wisconsin, Iowa and Illinois" |
| g-a1s09-forecasts | "Severe Weather Forecast 68 · issued 1:00 PM CST (2:00 PM EST)"; "... 69 · issued 4:20 PM CST (5:20 PM EST)" | issue times in both zones | study p. 6 and p. 7; provenance a9 rows |
| g-a1s18, g-a2s21, g-a3s10, g-a4s13 (and the sheet in g-a5s21, g-a6s03, g-z1s02) | eyebrow "SOUTH BEND WEATHER BUREAU · BY TELEPHONE" and title "Organizations notified included:" (8 strings) | who South Bend telephoned | study p. 14, "also telephoned several organizations ... Those organizations notified included ..." (design sheet section 5 read on the page image; fc-a1-a2, A1-S20). Said of the warnings in general, not of the 5:43 one; "included" keeps it from reading as the whole list |
| g-a5s07-marion | label "HOWARD" | the tornado left Howard County for Grant County at 7:50 PM | survey printed p. 45, read: "The tornado left Howard county and entered Grant county at 7:50 PM." In the script only on the Rows line (A5-S7), not in the Picture note or the voice. **Scope flag:** county-key.md grades County C (the study's county west of County B) as Howard. A viewer who sees Howard west of Marion on this map, and the 8:07 county-seat hit in Act 4, can place County B. Strike the label (the map works with Marion and Linn Grove only) |
| g-a6s07-power | "asked for: a repeater scope" | the survey team asked for a screen showing another office's radar | survey printed p. 2, Recommendation 5 (facts G). The team asked, not South Bend: next to the label "South Bend" it reads as South Bend's own request. Wording: "the team asked for: a repeater scope" |

## ADDED, label only (no new fact)
g-a1s06 "our sketch · not to scale"; g-a1s07 "schematic: not a real track"; g-a3s05 "a home in the town"; g-a3s09 "line busy"; g-a3s15 "an office in the path"; g-a4s01 "by the study's account"; g-a5s07 "places the survey names · path schematic"; g-a6s02 "schematic · not any one station's building". Each is a disclaimer or a drawn-thing label; none adds a fact.

## Checks that came out clean
- Every quoted string was set against its page: study pp. 6, 7, 9, 10, 12, 13, 14, 15, 19-25, 29-31, 33, 34; survey pp. 37-45 (the OCR page map was used for pp. 16, 29, 30, 31, 33, 34).
- Film briefs (g-a1s15, g-a2s03, g-a3s07, g-a4s01, g-a5s10, g-a6s11) carry only "Civil defense training film, 1967".
- No brief shows a county the script hides apart from the HOWARD label above.
