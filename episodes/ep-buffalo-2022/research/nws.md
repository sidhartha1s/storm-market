# NWS / meteorology fact file: Buffalo blizzard, 23-27 Dec 2022
Compiled 26 Oct 2026. All times US Eastern (EST) unless noted. P = PRIMARY (NWS product text or ASOS obs as archived by Iowa Environmental Mesonet, IEM), S = SECONDARY.

Fetch notes:
- weather.gov/buf event page and the NWS Eastern Region After Action Review PDF (Apr 2023) were NOT fetchable (404 at www.weather.gov paths I guessed; preview-idp.weather.gov host did not resolve). Search listing only: https://preview-idp.weather.gov/media/publications/assessments/ER%20AAR%20Buffalo%20Blizzard%20and%20NE%20Coastal%20Flooding.pdf (UNCONFIRMED content; table of contents only seen in search snippet).
- WPC storm summary page: not found (404 on guessed URL). No WPC primary for pressure.
- IEM archive endpoints worked (raw NWS text products). Base: https://mesonet.agron.iastate.edu/cgi-bin/afos/retrieve.py?pil=<PIL>&sdate=<UTC>&edate=<UTC>&fmt=text&limit=200 (PILs used: WSWBUF, AFDBUF, PNSBUF). ASOS: https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?station=BUF&data=tmpf&data=sknt&data=gust&data=vsby&data=mslp&data=wxcodes&data=feel&year1=2022&month1=12&day1=22&year2=2022&month2=12&day2=27&tz=America%2FNew_York&format=onlycomma&latlon=no&missing=M&trace=T&direct=no&report_type=3&report_type=4
- Gust/wind values in the IEM ASOS feed are knots; mph = kt x 1.15078. Visibility in statute miles.

## Q1. Watch / Warning timeline for Erie County (zones NYZ010 Northern Erie, NYZ085 Southern Erie)

KEY FINDING: NWS Buffalo issued NO "Blizzard Watch" for Erie County. It issued a Winter Storm Watch first, then upgraded straight to a Blizzard Warning. Verified from the VTEC codes in the products.

| # | Fact | Value | Quote (<25 words) | URL | Date | Type |
|---|---|---|---|---|---|---|
| 1.1 | First headline for Erie County: Winter Storm Watch (VTEC WS.A.0016), covering Niagara, Orleans, Erie, Genesee, Wyoming, Chautauqua, Cattaraugus | Issued 2:22 PM EST Tue 20 Dec 2022 (1922Z). Valid Fri morning 23 Dec to Mon morning 26 Dec | "Localized blizzard conditions are possible." Watch text: "Winds could gust as high as 65 mph Friday into Friday night." | https://mesonet.agron.iastate.edu/cgi-bin/afos/retrieve.py?pil=WSWBUF&sdate=2022-12-17T00:00Z&edate=2022-12-22T08:00Z&fmt=text&limit=200 (product WWUS41 KBUF 201922) | 20 Dec 2022 | P |
| 1.2 | Blizzard Warning first issued for Erie County (VTEC BZ.W.0001, NEW; WS watch upgraded to it) | Issued 3:54 AM EST Thu 22 Dec 2022 (0854Z). In effect 7 AM Fri 23 Dec to 7 AM Sun 25 Dec | "BLIZZARD WARNING IN EFFECT FROM 7 AM FRIDAY TO 7 AM EST SUNDAY" | https://mesonet.agron.iastate.edu/cgi-bin/afos/retrieve.py?pil=WSWBUF&sdate=2022-12-19T00:00Z&edate=2022-12-27T00:00Z&fmt=text&limit=200 (product WWUS41 KBUF 220854) | 22 Dec 2022 | P |
| 1.3 | Warning lead time before effective time | 27 hours 06 min (3:54 AM Thu to 7 AM Fri). Computed from 1.2 | n/a | same as 1.2 | 22-23 Dec | P (computed) |
| 1.4 | Watch lead time before blizzard start | Watch 2:22 PM Tue 20 Dec; warning effective 7 AM Fri 23 Dec = about 2 days 17 hours. Computed | n/a | same as 1.1/1.2 | 20-23 Dec | P (computed) |
| 1.5 | Warning expected snow/wind at issue | "Total snow accumulations of 1 to 3 feet", gusts "as high as 70 mph Friday and Friday night" | "Blizzard conditions will develop Friday afternoon lasting into Saturday night." | same as 1.2 | 22 Dec | P |
| 1.6 | Forecast raised by 6:48 PM Thu 22 Dec | "2 to 3 feet with locally higher", gusts "65 to 70 mph", wind chills "10 to 20 below zero" | "frequently reducing visibilities to zero. Travel is strongly discouraged." | WSWBUF product WWUS41 KBUF 222348 (same IEM wsw query as 1.2) | 22 Dec | P |
| 1.7 | Warning for Erie ended early | Blizzard Warning cancelled, replaced by Winter Storm Warning, 5:45 AM EST Sun 25 Dec (Northern/Southern Erie, Genesee). Original end was 7 AM Sun | "BLIZZARD WARNING IS REPLACED BY A WINTER STORM WARNING WHICH IS IN EFFECT UNTIL 4 AM EST MONDAY" | WSWBUF product WWUS41 KBUF 251045 (same IEM wsw query as 1.2) | 25 Dec | P |
| 1.8 | First Area Forecast Discussion flagging a big storm for the region | 4:10 AM EST Sun 18 Dec 2022: AFD says a "very large and powerful storm system will impact the bulk of the eastern half of the country later in the week." About 5 days before the 23 Dec blizzard onset | quoted as shown | https://mesonet.agron.iastate.edu/cgi-bin/afos/retrieve.py?pil=AFDBUF&sdate=2022-12-15T00:00Z&edate=2022-12-20T00:00Z&fmt=text&limit=100 (product FXUS61 KBUF 180910) | 18 Dec | P |
| 1.9 | First AFD to say blizzard/once-in-a-generation | 4:51 AM EST Tue 20 Dec 2022: "One could certainly describe this storm system as a once in a generation type of event." Also "Headlines (watches) will likely be issued within the next few forecast cycles." | quoted as shown | https://mesonet.agron.iastate.edu/cgi-bin/afos/retrieve.py?pil=AFDBUF&sdate=2022-12-18T12:00Z&edate=2022-12-22T12:00Z&fmt=text&limit=60 (product FXUS61 KBUF 200951) | 20 Dec | P |
| 1.10 | Days ahead summary | Storm signalled ~5 days ahead (18 Dec AFD), "once in a generation" wording 3 days ahead (20 Dec), watch ~2.7 days ahead, warning ~27 h ahead of effective time | n/a | see 1.1, 1.2, 1.8, 1.9 | | P (computed) |

## Q2. Start / end at Buffalo; hours of blizzard and zero visibility at BUF

Derived by me from the IEM ASOS feed for BUF (Buffalo Niagara Intl, station BUF), local-time column. NWS official blizzard criterion: visibility <= 1/4 mile with wind/frequent gusts >= 35 mph for 3+ hours (standard NWS definition, not fetched this run; UNCONFIRMED).

| # | Fact | Value | URL | Type |
|---|---|---|---|---|
| 2.1 | Rain/precip before the front | Rain on the night of 22-23 Dec; temp 37-39F at midnight to 6 AM Fri 23 Dec | ASOS URL in Fetch notes | P |
| 2.2 | Front arrival / wind jump | 7:24 AM Fri 23 Dec: wind 16 kt gust 21 kt, temp 38F. By 8:06 AM: gust 52 kt, snow, vis 1/2 mi | ASOS URL | P |
| 2.3 | Visibility first at/below 1/4 mile (blizzard criterion) | 8:39 AM EST Fri 23 Dec (vis 1/4 mi, heavy snow + blowing snow, gust 58 kt) | ASOS URL | P (derived) |
| 2.4 | Visibility returned above 1/4 mile | First obs above 1/4 mi: 1:06 AM EST Sun 25 Dec (vis 1.5 mi; last obs <=1/4 mi was 12:54 AM). Continuous span about 40.5 hours | ASOS URL | P (derived) |
| 2.5 | Second low-vis spell | 5:54 AM to about 7:17 AM Mon 26 Dec, vis <=1/4 mi (1.4 hours) | ASOS URL | P (derived) |
| 2.6 | Visibility reported 0 (zero) | Several runs between 12:05 PM Fri 23 Dec and 3:54 AM Sat 24 Dec; longest unbroken: 8:25 PM Fri to 1:54 AM Sat (about 6 hours) and 1:34 PM to 5:54 PM Fri (about 5 hours). Total of 0.00 vis obs over 23-24 Dec: 12:05 PM Fri to 4:04 AM Sat with small gaps (about 16 hours of 0 vis reports by my count of the spans) | ASOS URL | P (derived; hourly+special obs only) |
| 2.7 | Third-party blizzard-duration figure | "37.5 consecutive hours of blizzard conditions"; Wikipedia attributes it to CNN/Axios. Differs from my 40.5 h of vis <=1/4 mi (blizzard needs wind too). Use NWS 37 h only if the NWS storm summary confirms it | https://en.wikipedia.org/wiki/December_2022_North_American_blizzard | S, UNCONFIRMED vs NWS |
| 2.8 | Blizzard "longest in Buffalo's recorded history" | Wikipedia cites CNN/Axios. Not confirmed from NWS page. Tried: weather.gov/buf event page (404) | https://en.wikipedia.org/wiki/December_2022_North_American_blizzard | S, UNCONFIRMED |
| 2.9 | Lake effect snow continued after the blizzard | Warning replaced by Winter Storm Warning 5:45 AM Sun 25 Dec for "lake effect snow and blowing snow"; Erie airport total reached its final 51.9 in by 9:08 PM 27 Dec | https://mesonet.agron.iastate.edu/cgi-bin/afos/retrieve.py?pil=PNSBUF&sdate=2022-12-23T00:00Z&edate=2023-01-05T00:00Z&fmt=text&limit=60 | P |

## Q3. Wind gusts, temperature drop, wind chill (BUF ASOS, derived)

| # | Fact | Value | URL | Type |
|---|---|---|---|---|
| 3.1 | Peak gust in the hourly/special obs feed | 60 kt = about 69 mph at 12:54 PM EST Fri 23 Dec. Many 56-58 kt (64-67 mph) gusts from 8:39 AM to 10:30 PM that day | ASOS URL | P (derived) |
| 3.2 | Peak gust claimed in news | 72 mph at Buffalo airport (Spectrum News 1); 74 mph at Niagara Falls airport; 79 mph Lackawanna (Yahoo citing NWS; Wikipedia citing WPC) | https://spectrumlocalnews.com/nys/buffalo/weather/2022/12/28/buffalo-blizzard-through-the-eyes-of-a-meteorologist ; https://en.wikipedia.org/wiki/December_2022_North_American_blizzard | S, UNCONFIRMED vs NWS peak-wind list (my feed tops at 69 mph; 1-min/5-min peaks can be higher) |
| 3.3 | Peak sustained wind | 39 kt = about 45 mph at 9:54 AM Fri 23 Dec | ASOS URL | P (derived) |
| 3.4 | Temperature fall at BUF | 38F at 7:24 AM Fri 23 Dec to 12F at 12:54 PM = 26F in about 5.5 hours. Down to 4F at 3:05 AM Sat 24 Dec (earlier high of 40F on 22 Dec 5:54 PM, so 36F lower than that). The NWS forecast called this a "flash freeze" | ASOS URL ; forecast quote in product 220854 (IEM WSWBUF link in 1.2): "A rapid switch from rain to snow with sharply falling temperatures" | P (derived) |
| 3.5 | Coldest wind chill in feed (ASOS "feel") | about -24F at 5:18 AM Sat 24 Dec (temp 4F, wind 33 kt). Wind chill below -10F from about 11:43 AM Fri to about 3 PM Sat | ASOS URL | P (derived) |
| 3.6 | Forecast wind chill | "Wind chills as cold as 10 to 20 below zero" | WSWBUF 222348 (IEM link in 1.2) | P |
| 3.7 | Forecast storm winds, first look | AFD 20 Dec: system "will have the potential to generate at least storm force winds over the Lower Great lakes." | AFDBUF 200951 (IEM link in 1.9) | P |

## Q4. Snow totals; comparison with 1977

| # | Fact | Value | Quote | URL | Date | Type |
|---|---|---|---|---|---|---|
| 4.1 | Buffalo Airport storm total (5-day lake effect storm total) | 51.9 in, observed by 9:08 PM 27 Dec (Official NWS Obs) | "Buffalo Airport 51.9 in 0908 PM 12/27 Official NWS Obs" | https://mesonet.agron.iastate.edu/cgi-bin/afos/retrieve.py?pil=PNSBUF&sdate=2022-12-23T00:00Z&edate=2023-01-05T00:00Z&fmt=text&limit=60 (PNS NOUS41 KBUF 281646, 11:46 AM 28 Dec) | 28 Dec 2022 | P |
| 4.2 | Erie County next highest (volunteer/co-op) | Lake View 1NE 44.6 in (COOP); Elma 2.7 WSW 44.5; Hamburg 2.0 N 43.5; Williamsville 3.8 E 37.6; Orchard Park 37.0 | same PNS | 28 Dec | P |
| 4.3 | Caveat | The PNS title says "5 DAY STORM TOTAL SNOWFALL REPORTS FROM THE LAKE EFFECT SNOWSTORM" so totals span 23-27 Dec, and the airport figure is flagged SNOW_24 in the machine-readable section (label oddity) | same PNS | P |
| 4.4 | Snow forecast ahead | Warning 22 Dec: 1 to 3 feet, then 2 to 3 feet. Observed airport 51.9 in is above that range | WSWBUF links in 1.2 | P |
| 4.5 | Blizzard of 1977 (Jan-Feb 1977) | Not confirmed from NWS. A secondary summary of an NWS presentation (via search) says 20+ fatalities, 69 mph winds, "only 12" of snow" new, mostly ground blizzard. UNCONFIRMED. Tried: weather.gov/buf pages (404), search | https://blog.ametsoc.org/tag/blizzard ; https://en.wikipedia.org/wiki/Blizzard_of_1977 | | S, UNCONFIRMED |
| 4.6 | 2022 death toll vs 1977 | WIVB: "death toll ... equaling Blizzard of '77" at 29; later 47 total | https://digital-release.wivb.com/weather-news/buffalo-blizzard-2022/death-toll-from-blizzard-rises-to-at-least-29-equaling-blizzard-of-77/amp/ ; https://www.wivb.com/weather-news/buffalo-blizzard-2022/erie-county-medical-examiner-confirms-three-more-blizzard-related-deaths-bringing-total-to-47/amp/ | Dec 2022 | S |

## Q5. Bomb cyclone pressure numbers

| # | Fact | Value | Quote | URL | Date | Type |
|---|---|---|---|---|---|---|
| 5.1 | NWS Buffalo forecast, 20 Dec | "The low will deepen from roughly 1000mb Thursday evening to roughly 968mb by Friday evening" = 32 mb in about 24 h | "easily meeting the definition of bombogenesis (24mb/24hrs)" | https://mesonet.agron.iastate.edu/cgi-bin/afos/retrieve.py?pil=AFDBUF&sdate=2022-12-18T12:00Z&edate=2022-12-22T12:00Z&fmt=text&limit=60 (FXUS61 KBUF 200951) | 20 Dec 2022 | P (forecast) |
| 5.2 | NWS Buffalo forecast, 21 Dec | "roughly 990mb ... late Thursday night ... 982mb over southernmost Ontario Friday morning ... about 968mb ... by Friday evening" | "setting low pressure records once it passes north of the border" | same IEM AFDBUF link (FXUS61 KBUF 211824, 1:24 PM 21 Dec) | 21 Dec | P (forecast) |
| 5.3 | NWS Buffalo forecast, 22 Dec | "Surface pressure drops rapidly (about 20 mb in only 12 hours) to around 970mb" | quoted as shown | same IEM AFDBUF link (FXUS61 KBUF 221008, 5:08 AM 22 Dec) | 22 Dec | P (forecast) |
| 5.4 | Observed pressure at BUF | Lowest sea-level pressure in METARs: 981.4 hPa (about 28.98 inHg) at 7:54 AM Fri 23 Dec, right as the front hit; rose to 995.9 by midnight 24 Dec | ASOS URL | P (derived; MSLP from hourly METAR) |
| 5.5 | Observed storm minimum | 963 mb (28.44 inHg), Wikipedia citing WPC surface analysis archive; Washington Post 35 mb fall in 24 h. NOT confirmed from a WPC page (guess URL 404) | https://en.wikipedia.org/wiki/December_2022_North_American_blizzard | S, UNCONFIRMED |

## Q6. Did NWS frame danger as wind/visibility rather than snow depth?

Yes in the products. Quotes (all PRIMARY, NWS Buffalo, IEM archive links as noted):
| # | Quote | Where | Date |
|---|---|---|---|
| 6.1 | "True blizzard conditions are rare in Western NY, and it's unusual to even consider blizzard headlines this far in advance of a storm." | AFD 5:08 AM 22 Dec (FXUS61 KBUF 221008); AFDBUF IEM link in 1.9 | 22 Dec |
| 6.2 | "Expect the combination of lake effect snow and very strong winds to produce Blizzard conditions across the Niagara Frontier" | same AFD | 22 Dec |
| 6.3 | "Strong winds will cause significant blowing and drifting snow, frequently reducing visibilities to zero. Travel is strongly discouraged." | Blizzard Warning text, 3:54 AM 22 Dec (WSWBUF 220854) | 22 Dec |
| 6.4 | "Areas of blowing snow could significantly reduce visibility with whiteouts and localized blizzard conditions possible." | Winter Storm Watch text 2:22 PM 20 Dec (WSWBUF 201922) | 20 Dec |
| 6.5 | "An extraordinary 70-75 kt low level jet" and "damage producing winds" lead the 20 Dec AFD; snow is mentioned after ("As if the very real threat for damage producing winds were not enough") | AFD 4:51 AM 20 Dec (FXUS61 KBUF 200951) | 20 Dec |
| 6.6 | Warning impacts list: "Widespread blowing snow will significantly reduce visibility" and frostbite in "as little as 30 minutes" | WSWBUF 222348 | 22 Dec |
| 6.7 | Instruction for stranded travellers: "If you get stranded, stay with your vehicle." | WSWBUF 221909 (2:09 PM 22 Dec), Jefferson zone text; the Erie zone text in that product was cut off in my read, so for Erie this is UNCONFIRMED | 22 Dec |
| 6.8 | Warning headline wording for Erie never used snow total as the trigger: top line is "Blizzard conditions expected", snow totals second | WSWBUF 220854 | 22 Dec |

## Angle check: "most of the dead were found outdoors" (S, county executive figures via WIVB)
| # | Fact | Value | URL | Type |
|---|---|---|---|---|
| 7.1 | Erie County 46 deaths by circumstance (Poloncarz): 18 found outdoors in snow; 12 no power/heat; 7 delayed EMS (cardiac); 4 in vehicles; 4 snow-blowing/shoveling; 1 drowned in hotel pool. Plus one Niagara County CO death = 47 overall | https://www.wivb.com/weather-news/buffalo-blizzard-2022/erie-county-medical-examiner-confirms-three-more-blizzard-related-deaths-bringing-total-to-47/amp/ | S |
| 7.2 | Check on the angle: "outdoors" 18 of 46 = 39% (22 of 46 = 48% if vehicles added). That is the largest single category but NOT a majority. Wording "most" is UNCONFIRMED against 18/46. Use "the largest group" or "more than any other cause" unless a later official count shows a majority | computed from 7.1 | S (computed) |
| 7.3 | Earlier Tuesday count: 17 outdoors, 3 vehicles, 3 clearing snow, 7 no heat (via search summary; page not opened) | https://abc7news.com/amp/post/buffalo-ny-snow-storm-death-toll-weather-snowfall-totals-houses-encased-in-ice/12623686/ | S, UNCONFIRMED |

## Not obtained
- weather.gov/buf event review page and NWS Eastern Region After Action Review text (404 / host unreachable). Tried: guessed www.weather.gov/buf paths, www.weather.gov/media/publications/assessments path, preview-idp host.
- NCEI Storm Events, NWS Public Information Statement with official peak gusts (PNS fetched only snow reports in first 60 products; no wind-gust PNS read), WPC storm summary, GOES imagery pages, 1977 totals from NWS: not fetched in the 40-minute window.
- AMS spotlight https://headlines.ametsoc.org/2023/10/12/once-in-a-generation-the-2022-buffalo-blizzard/ returned 403; search snippet only (47 dead, >100,000 power out).
