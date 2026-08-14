# Ep6 Katrina — Fact Verification Round 1

Verifier notes: worked WebSearch + WebFetch + curl/pdftotext directly (context-mode plugin unavailable in this session). Each item has a verdict, the supporting evidence, and exact quoted language where available.

---

## 1. LP&V completion estimate — ~13 years

**VERDICT: CONFIRMED.**

GAO-06-244T ("Army Corps of Engineers: History of the Lake Pontchartrain and Vicinity Hurricane Protection Project"), https://www.gao.gov/products/gao-06-244t (full text mirror: https://www.gao.gov/assets/a112581.html):

> "Congress first authorized the Lake Pontchartrain and Vicinity, Louisiana Hurricane Protection Project in the Flood Control Act of 1965."
>
> "The project, when designed, was expected to take about 13 years to complete and cost about $85 million."
>
> "The cost estimate for the original project was $85 million (in 1961 dollars) and the estimated completion date was 1978."

Script line "originally expected to take about thirteen years" is directly supported. Note: authorized 1965, expected completion 1978 — that's 13 years, consistent.

---

## 2. Rapid intensification driver — Loop Current / warm water

**VERDICT: CORRECTED / SOFTEN SOURCING — the NHC Tropical Cyclone Report itself does NOT mention the Loop Current. Use a NASA source instead, or soften TCR-attributed language to "warm Gulf waters."**

Checked the actual NHC Tropical Cyclone Report AL122005 (https://www.nhc.noaa.gov/data/tcr/AL122005_Katrina.pdf) via pdftotext — its intensification discussion (p.2) attributes Katrina's two rapid-intensification bursts (26-28 Aug) to "a very large upper-level anticyclone that dominated the entire Gulf of Mexico... resulting in very weak wind shear and efficient upper-level outflow." No mention of "Loop Current," "eddy," or ocean heat content anywhere in the document (grepped full extracted text for "loop current," "warm," "intensifi," "eddy" — only wind-shear/outflow language appears).

However, NASA/JPL's own primary page **does** state this explicitly — "Hurricane Katrina Heats up in the Gulf" (NASA/JPL Ocean Surface Topography / sea level science page), https://sealevel.jpl.nasa.gov/images/socbenefits/Hurricane-Katrina-Heats-up-in-the-Gulf.pdf:

> "Maximum wind speeds of Hurricane Katrina increased dramatically as that storm passed over the warm waters of the Loop Current in the Gulf of Mexico in late August 2005. The storm evolved quickly from a category 3 to category 5 event in a matter of 9 hours as it drew heat from the Loop Current and a large warm core eddy evident in the sea surface height..." (credited to R. Leben, G. Born, Univ. of Colorado CCAR).

**Recommendation:** if the script attributes this claim to "the National Hurricane Center," that's not defensible — the TCR doesn't say it. Either (a) cite NASA/JPL for the Loop Current claim, or (b) soften the line to something like "fed by unusually deep, warm Gulf water" without naming a specific NHC attribution.

---

## 3. KLIX radar silence during eyewall passage (~0854 CDT / 1354 UTC)

**VERDICT: CONFIRMED** — "at eight fifty-four in the morning, the radar near the city went silent" is defensible, with a precise caveat: the radar stopped *transmitting/updating* at that time; it did not necessarily go fully offline for the rest of the storm.

Two independent sources converge on 1354 UTC = 8:54 AM CDT:

1. Peer-reviewed AMS conference paper (Blackwell et al., analyzing KLIX NEXRAD data through Katrina landfall), https://ams.confex.com/ams/pdfpapers/108456.pdf — extracted via pdftotext. Its data table of KLIX-derived wind measurements runs in 5-6 minute increments and terminates precisely at **1354 UTC** (row: "1354  64.5  55  41.56" — distance 41.56 km from radar), with no further rows after that time, even though landfall/eyewall passage continued for hours afterward.
2. Lee, Bond & Feltz (2008), "Supercells and mesocyclones in outer rainbands of Hurricane Katrina," *Geophysical Research Letters*, https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2008GL034724 (page blocked by Cloudflare on direct fetch, but indexed search snippet from the article itself reads): "Figure 3 shows KLIX reflectivity at 1354, **the last sweep transmitted by the 88D** (although the radar did continue to operate)."

1354 UTC on Aug 29, 2005 converts to 8:54 AM CDT (UTC−5). This matches the script's claimed time exactly.

**Caveat for the writer:** source #2 explicitly notes the radar "continued to operate" — so "went silent" should be understood/phrased as the data feed/transmission stopping, not physical destruction. If the script implies total silence for the rest of the day, soften to "stopped transmitting" or "went dark" rather than implying permanent loss. I could not independently confirm from a primary NWS/NCEI archive-listing page whether/when transmission resumed (that would need NCEI's radar archive UI, which wasn't reachable in this pass) — flag as a minor residual gap.

---

## 4. London Avenue Canal east breach — "before seven that morning"

**VERDICT: SOFTEN.** Timing is genuinely imprecise/disputed across sources; "before seven" is at the edge of defensibility but not solid as a flat claim.

Wikipedia's London Avenue Canal article (citing the 2007 ASCE report "The New Orleans Hurricane Protection System: What Went Wrong and Why," Anderson/Battjes et al.) states: "The east breach occurred around 6 to 7 a.m." and "The west breach occurred around 7 or 8 a.m." — this is the most specific citation-backed timing I could locate in this pass. Other tertiary sources (New Orleans Historical) cite differing times (~9:30 a.m. for related events), and I did not manage to pull the IPET Vol. V or ILIT final-report primary timeline tables directly (paywalled/binary-heavy PDFs; time-boxed out of this pass).

**Recommended defensible phrasing:** "sometime between six and seven that morning" (east breach) — this stays inside the ASCE-cited range without overclaiming precision. A flat "before seven" is defensible for the east breach specifically (6-7am bracket) but should not be extended to "before seven" for the canal system as a whole, since the west breach range (7-8am) falls after 7.

---

## 5. E-99 sheet-pile load test misinterpretation

**VERDICT: CONFIRMED** — the qualitative claim ("a test whose results, read correctly, said the steel needed to go far deeper") is defensible.

Confirmed test identity and history: the E-99 test was a 1985 field load test on a 200-ft floodwall section on the landside berm of the "Item E-99" East Atchafalaya Basin Protection Levee, Avoca Island, near Morgan City, LA, run by USACE's Lower Mississippi Valley Division — full primary test report: "E-99 Sheet Pile Wall Field Load Test Report" (June 1988), https://biotech.law.lsu.edu/katrina/hpdc/docs/19880600_E-99_Sheet_Pile_Wall_Field_Load_Test_Report.pdf (report exists and is hosted; not fully OCR'd in this pass but its existence/title/date is verified).

Peer-reviewed source directly discussing the failure logic — Sills, Vroman, Wahl & Schwanz (2008), "Overview of New Orleans Levee Failures: Lessons Learned and Their Impact on National Levee Design and Assessment," ASCE *Journal of Geotechnical and Geoenvironmental Engineering* (mirrored PDF at Tulane, https://www2.tulane.edu/~sanelson/New_Orleans_and_Hurricanes/overviewofleveefailures.pdf), extracted via pdftotext:

> "The E-99 full-scale field load test provided a false sense of security for I-type floodwalls... For example, in 1985, the E-99 test section, a field load test of a sheet-pile wall similar in design to those of the I-wall canal failures, was performed by the Lower Mississippi Valley Division (LMVD) of the USACE... The purpose of the field load test was to obtain full-scale performance data to validate the design methods used for optimizing the depth of sheet-pile penetration... The data showed significant wall deflections. Back-analysis showed that the observed wall deflections did not match those predicted using the design methods."

The specific "17 ft actual vs. 31-46 ft needed" figure — cited by a secondary (non-primary but citation-attributed) source, New Orleans Historical, https://neworleanshistorical.org/items/show/275:

> "At a savings of $100,000,000, the Corps wrongly concluded it could short-sheet the steel pilings of the 17th Street Canal driving them to depths of not more than 17 feet instead of between 31 and 46."

**Note:** this source frames it as reliance on "a poorly executed and misinterpreted study... conducted near Morgan City in 1988" — which is the E-99 test (Morgan City location confirmed above), so this is the same event, just imprecisely dated (test performed/reported 1985-88, spanning the LMVD field test through the 1988 report). The qualitative claim in the script is solid; the specific "31-46 ft" figure is sourced to a non-primary summary site rather than ILIT/Seed-Bea directly, so treat the exact numbers as "commonly cited" rather than ironclad-primary. Recommend keeping the qualitative sentence as scripted and, if exact footage numbers are spoken on-camera, hedge with "as much as" language.

---

## 6. Charity Hospital doctors in the 60 Minutes "Katrina" segment (Sept 4, 2005)

**VERDICT: CORRECTED — names identified.**

- **"Dr. Peter W."** = **Dr. Peter DeBlieux**, Charity Hospital ER physician/director, who led moving the entire ER (50+ critically ill patients) up one flight of stairs during the flooding. Corroborated by CBS's own retrospective, "What 60 Minutes witnessed in first Katrina report," https://www.cbsnews.com/news/what-60-minutes-witnessed-in-first-hurricane-katrina-report — and by LSU Health's own first-person account page, https://www.lsuhospitals.org/hurricanes/deBlieux.shtml.
- **"Ben Dewablanc"** = **Dr. Ben deBoisblanc**, LSU/Charity ICU (pulmonary-critical-care) physician, who described a patient dying awaiting helicopter evacuation. Per the CBS retrospective piece:
  > "'She died on the rooftop waiting for a helicopter,' deBoisblanc [said]. 'I haven't spoken to her husband. I don't even know where he is. I don't even know if he knows she's dead.'"

**Caveat:** I could NOT independently confirm the specific detail that the woman died "on the helipad while her husband fanned her" — the CBS retrospective account has her dying "on the rooftop" awaiting a helicopter, and deBoisblanc explicitly says he hasn't spoken to the husband and doesn't know where he is (implying the husband was not present with deBoisblanc at time of death, or at least deBoisblanc has no account of him fanning her). This detail may exist in the original broadcast audio/video (which I did not have access to review directly) but is not corroborated in the written record I found. **Recommend either finding/reviewing the original broadcast footage to confirm the fanning detail, or softening the script to omit that specific visual and keep only what's textually corroborated** (elderly woman died awaiting helicopter; deBoisblanc doesn't know if her husband was ever told).

---

## 7. HSDRRS vs. Katrina return period — "rated for a storm smaller than Katrina"

**VERDICT: CONFIRMED**, with precise phrasing recommended.

- HSDRRS is explicitly designed to a **100-year level of risk reduction** (1% annual-exceedance-probability storm surge) — per USACE New Orleans District's own HSDRRS pages, https://www.mvn.usace.army.mil/Missions/HSDRRS/Risk-Reduction-Plan/100-Year-Level-Protection/, and corroborated across multiple secondary sources (Munich Re, IWA Water Policy journal).
- Katrina's surge is estimated by IPET (Volume VII, 2008 final report) at roughly a **400-year return-period event** at New Orleans — i.e., Katrina's surge was a rarer/larger event than the 100-year design standard the new system is built to. (I could not pull the exact IPET Vol. VII sentence directly in this pass — the IPET final report PDF wasn't reachable/parseable — but the ~400-year figure is consistently reported in secondary engineering literature summarizing IPET's own numbers.)

**Recommended defensible phrasing:** "The new walls are built to withstand a hundred-year storm — Katrina's surge was closer to a four-hundred-year event." This is more precise and more defensible than the vaguer "a storm smaller than Katrina," and it's directly checkable against public USACE (100-year) and IPET-derived (~400-year) figures. Flag: I was not able to independently re-verify the "~400-year" figure against the raw IPET PDF itself in this pass (secondary-sourced only) — recommend one more direct check of IPET Vol. VII before final broadcast if time allows.

---

## 8. New Orleans elevation — "as much as ten feet below sea level"

**VERDICT: CONFIRMED**, and actually could go further/more dramatic if desired.

USGS-sourced data (via Greater New Orleans Community Data Center's neighborhood elevation mapping, drawing on USGS National Elevation Dataset): "Lakeview, Gentilly, and Metairie... now sit at 6 feet to 8 feet below sea level, while certain subdivisions in eastern New Orleans lie at 12 to 14 feet below sea level." USGS's own state-level lowest-point figure: the lowest point in Louisiana is in New Orleans, cited at 8 ft below sea level (MR-GO basin) in one USGS-sourced summary; the GNOCDC/USGS neighborhood data (above) shows some eastern subdivisions considerably lower, at 12-14 ft.

**Verdict on scripting "as much as ten feet below":** solidly defensible — it's actually a conservative/safe middle figure between the commonly-cited 6-8 ft (Lakeview/Gentilly/Metairie) and the max cited 12-14 ft (eastern New Orleans subdivisions). No correction needed.

---

## 9. 80% flooded — by when?

**VERDICT: CONFIRMED**, dated to August 30, 2005 (not the 31st).

NASA Science/Earth Observatory (science.nasa.gov, NASA's own MODIS/Terra satellite imagery page for Katrina flooding): imagery captured **August 30, 2005, at 11:45 a.m. CDT** by MODIS on NASA's Terra satellite "showed much of New Orleans under water... early news reports indicated that as much as 80 percent of the city was flooded after levees failed to hold Katrina's massive storm surge." A separate QuickBird pass on August 31 documented the levee breaches themselves, and Aqua/MODIS imagery on Aug 31 still showed the city severely flooded (i.e., the 80% figure from Aug 30 had not receded by Aug 31 — flooding was, if anything, still rising as water continued to pour in from Lake Pontchartrain).

**Recommended phrasing:** "By August 30th — the next day — as much as eighty percent of the city was underwater" is defensible and directly NASA-sourced.

---

## 10. "Thirty-five miles from the center"

**VERDICT: CONFIRMED — exact primary-source match, with two figures available depending on which measurement point the script means.**

- **NHC Advisory #27** (10 AM CDT, Aug 29, 2005), https://www.nhc.noaa.gov/archive/2005/pub/al122005.public.027.shtml — direct quote: **"THIS POSITION IS NEAR THE MOUTH OF THE PEARL RIVER...ABOUT 35 MILES EAST-NORTHEAST OF NEW ORLEANS LOUISIANA."** This is an exact match for "thirty-five miles" and is a live public NHC advisory (as close to primary as it gets).
- Separately, the NHC Tropical Cyclone Report AL122005 itself (final post-storm report, https://www.nhc.noaa.gov/data/tcr/AL122005_Katrina.pdf, confirmed via pdftotext) states the storm's **closest approach** was: "the center of the eye made its closest approach (about 20 n mi) to the east of downtown New Orleans" (~23 statute miles).

**Recommendation:** if the script's "thirty-five miles" refers to Advisory #27's landfall-time position near the Pearl River mouth, it's an exact match — cite Advisory #27. If it's meant to describe the storm's closest approach to downtown specifically, the TCR's own figure is smaller (~20 n mi / ~23 statute miles), so "thirty-five miles" would overstate the closest-approach distance. Recommend the writer clarify which moment/reference point the line intends; both are real, sourced, and precise, but they're not interchangeable.

---

## 11. Population: 484,674 → ~230,172

**VERDICT: CONFIRMED.**

The Data Center (GNOCDC successor), "Facts for Features: Katrina Impact," https://www.datacenterresearch.org/data-resources/katrina/facts-for-impact/ (per indexed search snippet, direct fetch was blocked/403'd in this pass but content is corroborated by the same figures appearing consistently across secondary citations of Data Center research):

> "The population of New Orleans fell from 484,674 before Katrina (April 2000) to an estimated 230,172 after Katrina (July 2006) — a decrease of 254,502 people."

484,674 is the U.S. Census Bureau's April 1, 2000 decennial count for the City of New Orleans (Orleans Parish). 230,172 is the Census Bureau's July 1, 2006 population estimate, as cited/used by The Data Center. **Minor gap:** I was blocked (HTTP 403) from directly loading The Data Center's own page to grab the primary-source sentence verbatim — the figures above are well-corroborated via search-indexed snippets of that exact page, but a follow-up direct fetch (perhaps via a different user agent or the Census Bureau's own American FactFinder/vintage-2006 estimate page) would firm this up to fully primary-verified status if time allows.

---

## 12. NPR segment — audio still live?

**VERDICT: YES — confirmed live.**

Fetched https://www.npr.org/2005/08/30/4823849/new-orleans-spared-the-worst-but-still-reeling directly. The page embeds NPR's standard audio module with a "Listen" button (`class="audio-module-listen"`) and a download tool (`class="audio-tool audio-tool-download"`), both pointing to:
`https://ondemand.npr.org/anon.npr-mp3/npr/day/2005/08/20050830_day_02.mp3?e=4823849&t=progseg&seg=2&p=17&sc=site`

I sent a direct HTTP request to that mp3 URL and got **HTTP 200** (live, resolves, serves audio) — confirmed via curl, not just page markup. So: yes, the segment audio is still served, both streamable ("Listen") and downloadable.

---

# Summary Table

| # | Item | Verdict |
|---|------|---------|
| 1 | LP&V ~13 years | CONFIRMED — GAO-06-244T: "expected to take about 13 years to complete and cost about $85 million," est. completion 1978 |
| 2 | Loop Current driver | CORRECTED — NHC TCR does NOT mention Loop Current (attributes intensification to upper-level anticyclone/low shear); use NASA/JPL source instead if naming Loop Current |
| 3 | KLIX radar silent 8:54am | CONFIRMED — AMS paper data + GRL 2008 paper both show last transmitted sweep at 1354 UTC = 8:54 CDT; radar "continued to operate" though, so phrase as "stopped transmitting" not total silence |
| 4 | London Ave breach "before 7am" | SOFTEN — ASCE-cited range is east breach 6-7am, west breach 7-8am; use "between six and seven" for east breach specifically |
| 5 | E-99 test misread | CONFIRMED (qualitative) — E-99 (1985, Morgan City) misinterpreted; "17 ft vs 31-46 ft" figure is secondary-sourced, treat exact numbers as commonly-cited not ironclad-primary |
| 6 | Charity Hospital doctors | CORRECTED — names = Dr. Peter DeBlieux (ER) and Dr. Ben deBoisblanc (ICU); "husband fanning her" detail NOT corroborated in written record, recommend verifying against broadcast footage or cutting that specific visual |
| 7 | HSDRRS vs Katrina | CONFIRMED — 100-year design vs Katrina's ~400-year IPET-estimated surge; recommend precise phrasing over vague "smaller than Katrina" |
| 8 | NOLA elevation ~10ft | CONFIRMED — USGS/GNOCDC data shows 6-14 ft below sea level across neighborhoods; "as much as ten feet" is a safe, defensible middle figure |
| 9 | 80% flooded | CONFIRMED — NASA: Aug 30, 2005, 11:45am CDT MODIS imagery, "as much as 80 percent... flooded" |
| 10 | "35 miles" | CONFIRMED — exact match to NHC Advisory #27 language for landfall-time position; note TCR's closest-approach figure is smaller (~20 n mi/~23 mi) — clarify which reference point is intended |
| 11 | Population 484,674 → 230,172 | CONFIRMED — Data Center figures (April 2000 vs July 2006); primary-page fetch was 403'd, figures corroborated via search snippet only |
| 12 | NPR audio still live | YES — confirmed via direct HTTP 200 on the mp3 URL embedded in the page |

## Residual gaps flagged for a possible round 2
- Item 2: need to confirm the script doesn't misattribute the Loop Current claim to NHC specifically.
- Item 4: IPET Vol. V / ILIT primary timeline PDFs not directly pulled (blocked/time-boxed) — current sourcing is a 2007 ASCE paper via Wikipedia citation, one level removed from IPET/ILIT primary.
- Item 6: the fanning-the-dying-woman visual detail is unconfirmed in text sources — needs a footage/transcript check.
- Item 7: ~400-year IPET figure sourced secondarily; a direct IPET Vol. VII quote would firm this up.
- Item 11: Data Center primary page returned 403; figures are well-corroborated but not pulled verbatim from the primary URL directly.
