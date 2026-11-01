# Maps, forecast, mechanism: Great Appalachian Storm, 24-26 Nov 1950
Researched 26 Oct 26. "fetch summary" = WebFetch gave a summary, not raw text. PRIMARY = 1950-era or the author's own record; SECONDARY = later text.

## 1. Daily weather maps
1. NWS Jackson KY hosts surface charts for 24, 25, 26, 27 Nov 1950 (each URL returned HTTP 200 by curl, 26 Oct 26; image contents NOT read, WebFetch cannot view JPEG). Page text says the charts are for 1:30 a.m. each day (fetch summary). SECONDARY host, likely a scan of the Weather Bureau chart; original series not confirmed.
   - 24 Nov: https://www.weather.gov/images/jkl/PastEvents/19501124Surface.JPG
   - 25 Nov: https://www.weather.gov/images/jkl/PastEvents/19501125Surface.JPG
   - 26 Nov: https://www.weather.gov/images/jkl/PastEvents/19501126Surface.JPG
   - 27 Nov: https://www.weather.gov/images/jkl/PastEvents/19501127Surface.JPG
   - Snow map: https://www.weather.gov/images/jkl/PastEvents/1950SnowStorm.jpg (200 OK)
   - Page: https://www.weather.gov/jkl/appalachianstorm1950
2. NWS Charleston WV lists 12Z upper-air and surface maps for 24-29 Nov, filenames 19501124_12z.gif and 19501124_12z_surf.png (same pattern for 25, 26, 27), base https://www.weather.gov/images/rlx/SnowClimo/Storms/ (base path from fetch summary, NOT curl-tested). Page: https://www.weather.gov/rlx/snow
3. NOAA Central Library "U.S. Daily Weather Maps" covers April 1871 to April 1968 as DjVu/PDF named yyyymmdd (fetch summary): https://library.noaa.gov/weather-climate/daily-weather-maps . The search form is dynamic; per-date direct URLs for 19501124-27 NOT confirmed. The old direct path docs.lib.noaa.gov/rescue/dwm/1950/19501125.djvu failed (DNS ENOTFOUND). Related library "Daily Synoptic Weather Maps" (Northern Hemisphere, 1899 to 31 Mar 1971): https://library.noaa.gov/weather-climate/synoptic-map ; guessed image pattern DSM_1950_1125.jpg returned 403, unconfirmed.
4. Public-domain status: no statement on either library page (fetch summary). US federal work, so public domain by law is expected, but NOT stated on the page. Ask a Librarian: https://answers.library.noaa.gov/form?queue_id=7867
5. WeatherNation reprints two NOAA charts (25 Nov, 28 Nov): https://media.weathernationtv.com/app/uploads/2017/11/Capture-8.png and https://media.weathernationtv.com/app/uploads/2017/11/Capture2.png (SECONDARY, via https://www.weathernationtv.com/news/the-great-appalachian-storm-of-1950-in-historical-context). Wikimedia file for the 25/26 Nov analysis: https://en.wikipedia.org/wiki/File:Great_Appalachian_Storm_1950-11-26_weather_map.gif (not opened).
6. What the maps show: no pressure or position was read off any image; see section 3 for text descriptions.

## 2. Forecasting and numerical prediction
- Phillips, N. A., 1958: Geostrophic errors in predicting the Appalachian storm of November 1950. Geophysica, 6, 389-405. Citation source: AMS Kistler et al. reference list (SECONDARY). Full text/abstract NOT reached; no URL for the paper itself found. Cited at https://ams.confex.com/ams/84Annual/webprogram/Paper73168.html
- Kistler, Uccellini, Kocin, "Thanksgiving Weekend Storm of 1950", Norm Phillips Symposium, 84th AMS Annual Meeting, 15 Jan 2004. https://ams.confex.com/ams/84Annual/techprogram/paper_73168.htm (SECONDARY, fetch summary + snippets)
  - "the manually derived forecasts of the day were unable to anticipate this extreme event."
  - "extend the lead time predictability beyond the 3.5 days established with the first attempt to simulate this storm."
  - "The initial conditions depict a weak cyclonic wave over Minnesota" ahead of "a very cold air mass over southwestern Canada" (second quote partial).
  - Storm "chosen the first test case for Charney's 2 Level model"; results "less successful than hoped" but led to the meetings that produced the Joint Numerical Weather Prediction Unit in 1954 (fetch summary; cites Phillips 2000).
  - Phillips 1958 is cited there as an early NWP case study of this storm.
- Lead time of the 1950 hand forecasts: NOT found as a number. "3.5 days" is the model-simulation lead, not the hand forecast.
- Smagorinsky use of the storm: NOT found. Charney, Fjortoft and von Neumann 1950 (https://faculty.eas.ualberta.ca/jdwilson/EAS372_13/Charney_etal50.pdf) is the barotropic ENIAC paper, not about this storm (not opened).

## 3. Monthly Weather Review and mechanism
- Smith, C. D., Jr., 1950: The destructive storm of November 25-27, 1950. Mon. Wea. Rev., 78, 204-209. DOI https://doi.org/10.1175/1520-0493(1950)078<0204:tdson>2.0.co;2 (Crossref confirmed, issued Nov 1950). journals.ametsoc.org returned 403; full text NOT read. Archived PDF cited by Wikipedia: web.archive.org/web/20050123112302/http://docs.lib.noaa.gov/rescue/mwr/078/mwr-078-11-0204.pdf (WebFetch blocked archive.org).
- Smith, C. D. and Roe, C. L., 1952: Comparisons between the storms of November 20-22, 1952, and November 25-27, 1950. MWR 80, 227-231. DOI https://doi.org/10.1175/1520-0493(1952)080<0227:cbtson>2.0.co;2 (Crossref; not read).
- Bristor, C. L., 1951: The Great Storm of November 1950. Weatherwise, 4, 10-16 (a magazine, NOT MWR; citation from a search result, not opened).
- Lowest central pressure: no primary value reached. Wikipedia infobox 978 hPa, uncited (https://en.wikipedia.org/wiki/Great_Appalachian_Storm_of_1950); NBC Connecticut "around 980 mb". See Conflicts.

Mechanism facts (value / URL / snippet / grade):
- M1. Arctic cold front crossed E Kentucky near midnight 23-24 Nov; temps fell "from the 40s and 50s just ahead of the front to the teens just behind it." https://www.weather.gov/jkl/appalachianstorm1950 (fetch summary quote) SECONDARY.
- M2. Low formed on the front over the Carolinas on 25 Nov, moved northwest into Ohio by midday 26 Nov, stalled over Lake Erie 27-28 Nov. Same URL, fetch summary, SECONDARY.
- M3. Contrast in one storm: arctic air wrapped around the low while warm Atlantic air was drawn northwest; Pittsburgh 30.5 in snow in single digits, Buffalo 200 mi north in the 40s with no snow. Same URL, fetch summary, SECONDARY. Best single fact for the "two hazards" claim.
- M4. Winds from the gradient: a roughly 1050 mb high near Maine plus a ~980 mb low; "The freakishly strong pressure gradient produced violent southeasterly and easterly winds across New England." https://www.nbcconnecticut.com/news/local/the-great-southeast-of-1950/26557/ (fetch summary quote) SECONDARY.
- M5. Warm-sector air near 60F let turbulence mix the low-level jet to the surface (850 mb winds ~+4 standard deviations; Mt Washington 160 mph). Same NBC URL, fetch summary, SECONDARY.
- M6. Blocking: a strong Omega block over the North Atlantic and a near-stationary high over eastern Canada; low deepened rapidly over eastern North Carolina, near Washington DC by early 25 Nov, then turned northwest. https://oceanweatherservices.com/blog/?p=154 (fetch summary) SECONDARY. Wikipedia says the same (blocking ridge over eastern Canada), no inline cite.
- M7. Cold side: upper low stalled over the central Appalachians, 850 mb temps -15 to -20C, low became vertically stacked and near-stationary; upslope flow kept snow falling to 29 Nov. https://www.weather.gov/rlx/snow (fetch summary) SECONDARY.
- M8. Hand forecasts missed it: see section 2 quote. SECONDARY (2004 NCEP conference abstract).

## 4. NWS/NOAA explainers
- NWS Jackson KY (mechanism, charts): https://www.weather.gov/jkl/appalachianstorm1950
- NWS Charleston WV (upper-air + surface maps, stacked low): https://www.weather.gov/rlx/snow
- NCEI article: https://www.ncei.noaa.gov/news/great-appalachian-snowstorm-november-1950 : snow map and RSI only; no mechanism, pressure or forecast (fetch summary).
- WeatherNation/NOAA retrospective: no mechanism or forecast either (fetch summary).

## Conflicts
- Lowest pressure: 978 hPa (Wikipedia, uncited) vs "around 980 mb" (NBC CT). Neither is the Smith 1950 value.
- Dating: NWS Jackson says the low formed 25 Nov on the front; Wikipedia says morning of 24 Nov in SE North Carolina; Oceanweather says the secondary low formed 24 Nov and was near Washington DC early 25 Nov.
- Snow: Pittsburgh 30.5 in (NWS JKL) vs "nearly 28 in" (Oceanweather). Winds/snow are in nws-facts.md.
- "First storm forecast using NWS numerical model programs" (Oceanweather) vs first test case for Charney's model (Kistler). Use the AMS one.

## Could not confirm
- Direct per-date NOAA Central Library URLs for 24-27 Nov 1950 and their public-domain statement.
- Pressure values or low position read off any map image.
- Full text of Smith 1950 (403 / archive blocked); Phillips 1958 abstract or URL.
- Lead time and content of the 1950 operational hand forecasts; Smagorinsky/JNWP details beyond the AMS abstract; Doolin 2023 (NZ Met Soc) article not read (redirect not followed): https://www.metsoc.org.nz/resources/Documents/weather_and_climate/Vol_43_pdfs/Doolin_2_2023.pdf

## Calls made
- Treated the NWS Jackson charts as the usable "daily map" URLs because the NOAA library path is dynamic and its old direct link is dead.
- Bristor 1951 is Weatherwise, not MWR; listed anyway.
- Used the Crossref DOI record as proof of the MWR citation.
- Graded all mechanism items SECONDARY; no primary text was readable.
