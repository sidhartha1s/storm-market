# El Reno 2013: fact check for the locked angle (9 Oct 26)

Pulled for the angle the owner locked on 9 Oct 26 (`../angle.md`). Each item is marked CONFIRMED, CORRECTED or NOT CONFIRMED with its source. `facts.md` (audited 2 Aug 26) stays the base sheet; where the two disagree, this file wins and says why.

Sources read directly on 9 Oct 26:
- **SA** NWS Service Assessment, "May 2013 Oklahoma Tornadoes and Flash Flooding" (`13oklahoma_tornadoes.pdf`, https://www.weather.gov/media/publications/assessments/13oklahoma_tornadoes.pdf), text extracted with `pdftotext -layout`.
- **OUN** NWS Norman event page, https://www.weather.gov/oun/events-20130531 (times on it are CST; add one hour for CDT).
- **W14** Wurman, Kosiba, Robinson, Marshall 2014, "The Role of Multiple-Vortex Tornado Structure in Causing Storm Researcher Fatalities", Bulletin of the American Meteorological Society 95(1), 31 to 45, doi 10.1175/BAMS-D-13-00221.1 (times UTC; subtract five hours for CDT).
- **FOX** Fox News (AP photo), "Oklahoma Storms Kill 9 Guatemalans; Family Swept Away", 4 Jun 2013.
- **N9** News 9, Karl Torp, "Search Continues In OKC For Several Victims Swept Away By Floods", 3 Jun 2013.
- **GAZ** Oklahoma Gazette, Tim Farley, "In cars", 4 Jun 2013.

Every unit conversion below was made by script (m/s x 2.23694; m x 1.09361 for yards).

## 1. The spine: nobody lost their life indoors. CONFIRMED, with a scope

SA Appendix C, the fatality table for May 31, counted row by row by script:

| Rows | Circumstance column |
|---|---|
| 8 | tornado: 1 "Vehicle, driving from El Reno to Chickasha" (M 67), 4 "Vehicle, storm chasing" (M 35, M 55, M 24, M 45), 2 "Vehicle, parked along I-40" (F 26, M 17 days), 1 "Vehicle" (M 32) |
| 12 | "Sheltering in drainage ditch, flash flood": M 8, M 4, M 33, F 34, M 4, F 7, F 34, M 21, F 3, F 4, M 3, F 5 months |
| 1 | "Vehicle, flash flood" (M 65) |

- 21 rows, 0 of them name a building. Of the 12 in drainage ditches, 8 were aged eight or under.
- SA, section text: "All eight of the direct tornado fatalities on May 31, 2013, were in vehicles, four of whom were involved in storm chasing."
- OUN tornado table: 19 tornadoes that day, 8 deaths in total, all 8 from tornado 3 (El Reno). No other tornado that day took a life.
- **Scope the script must keep:** the 21 are the night of May 31. OUN counts a fourteenth flash-flood death in Okfuskee County "during the mid morning hours of June 1, 2013"; it is not in Appendix C and its circumstance was not pulled. Say "that night" or "on May 31", never "in the whole event".
- **What the claim is not:** OUN says "The tornado damaged numerous homes along with a few businesses near El Reno." No source pulled says whether people were inside those homes. The claim is that no one lost their life in a building, not that people rode out direct hits at home.

## 2. Wind and rating. CONFIRMED (295), CORRECTED (296 and 302 are out)

- OUN: "The RaXPol radar data shows winds of at least 295 mph very close to the surface. These intense winds were present in very small sub-vortices within the larger tornado circulation."
- OUN: "none of these intense sub-vortices impacted any structures in rural Canadian County. So despite the measured wind speeds, surveyors could not find any damage that would support a rating higher than EF-3".
- The survey paper in `facts.md` gives "in excess of 130 m/s" (290.8 mph). Speak "about 295" with NWS as the source, or "near 300". "296" and "302" are in no primary source pulled.
- OUN: maximum width 2.6 miles; path 16 miles; tornado 3 ran 1703 to 1744 CST (6:03 to 6:44 PM CDT) in the table, and the text says it "dissipated at 5:42 PM CST" (6:42 PM CDT). The two differ by two minutes: say "about 6:42".
- **The upgrade to EF5: CONFIRMED.** NWS Norman Public Information Statement, 12:06 PM CDT Tue 4 Jun 2013 (product PNSOUN, Iowa Environmental Mesonet text archive): "THE TORNADO HAS BEEN UPGRADED TO AN EF5 TORNADO BASED ON VELOCITY DATA FROM THE RESEARCH MOBILE RADAR DATA FROM THE UNIVERSITY OF OKLAHOMA RAXPOL RADAR AND THE DOPPLER ON WHEELS RADARS". The same statement: width 2.6 miles "BELIEVED TO BE THE WIDEST TORNADO ON RECORD IN THE UNITED STATES", path 16.2 miles, start 6:03 PM CDT, end 6:43 PM CDT near Interstate 40 and Banner Road.
- **The return to EF3: date NOT CONFIRMED.** News coverage gives 30 Aug 2013. No PNSOUN statement exists in the archive between 25 Aug and 10 Sep 2013, so it was announced some other way. The reason is confirmed (OUN, quoted above); the date needs its source before it is spoken.

## 3. The science arc: the tornado inside the tornado. CONFIRMED (W14)

- Sub-vortex forward speed: "Vp as high as 79 m/s" (176.7 mph). This confirms the "about 175 mph" that `facts.md` listed as unverified.
- Size of the sub-vortex that reached the research car: 90 to 230 m across (295 to 755 ft).
- The whole circulation was about 2 km across (1.24 miles) at its core flow where the cars entered it.
- W14: both vehicles "penetrated the weak side of the MVMC/tornado, so they may have been unaware that they were inside."
- The wide circulation itself nearly stopped: W14 has it moving less than 500 m in 300 s near Interstate 40 from 6:29 to 6:35 PM CDT; OUN has the loop north of the interstate from 6:27 to 6:35 PM CDT at less than 10 mph.

## 4. The middle: two vehicles. CONFIRMED, with one CORRECTION

**CORRECTED: they were not on the same road.** The research car was eastbound on Reuter Road; the TV crew was southbound on US-81. They were inside the same tornado, minutes apart.

The TV crew (W14, plus `facts.md` for the people):
- "A Weather Channel vehicle driving southward on US-81 penetrated into the tornado/MVMC in an attempt to traverse to the southern side".
- Hit by "the small central subvortex" as the centre crossed US-81 "moving rapidly east-northeastward, with Vp ~ 25 m/s" (55.9 mph). "Westerly winds on the southern side of the central vortex exceeded 83 m/s at 120 m AGL" (185.7 mph at 394 ft) "and transported the vehicle to the east side of US-81, injuring the occupants."
- OUN puts the tornado crossing US-81 near Reno Road at 6:19 PM CDT.
- Distance about 200 yards, three aboard, all survived: `facts.md` (weather.com).

The research car (W14):
- Entered the core flow eastbound on Reuter Road just behind Dan Robinson at about 6:21 to 6:22 PM CDT. Robinson was doing about 20 m/s (44.7 mph); the research car fell behind. Its headlights are last seen at 6:22:15 PM CDT.
- A sub-vortex intensified about 500 m to the south-southeast, moved north-northwest and became "nearly stationary over Reuters Road from 2323:35 to 2323:57 UTC" (6:23:35 to 6:23:57 PM CDT), "centered just to the east of the inferred starting position of the Samaras vehicle". Peak winds in it exceeded 81 m/s (181.2 mph).
- The car was about 530 m (580 yards) west of the Reuter and Radio roads intersection when struck, and was found 50 to 100 m north-east of that intersection: carried about 600 m (656 yards) in about 20 s.
- W14: "With only 30-s potential warning, possibly low visibility ... and the anomalous and rapidly changing direction of movement of the subvortex, it is likely that no clear direction to safety was apparent."
- W14: the car "was not especially heavy or armored, likely adding to its vulnerability".
- **Two sources disagree on the clock.** SA quotes Robinson's own account: "At this point at 6:19:25 p.m., the white Chevy Cobalt ... was immediately behind me." W14, timed against radar, has the same sighting at about 6:22. Speak "a little after 6:20" or use W14 and name it.
- SA: "It does not appear that traffic was a factor in the deaths of the TWISTEX storm chasers."

**One sub-vortex, not two (added after the intro fact check, `../fact_check.md`).** W14 reads as a single interior sub-vortex at both vehicles: "a large tornado/MVMC with a single (at this time) embedded subvortex" crosses US-81 with the large circulation at about 25 m/s; "after 2320 UTC; the interior subvortex ... is displaced" and loops, "becoming stationary over Reuters road and the vehicle"; Figure 9 has both vehicles "transported by winds in the embedded subvortex"; the conclusions say "it was an interior subvortex that impacted both the Samaras and Weather Channel teams". The paper never says "the same vortex" in one sentence, so the script tags it. Never write two different vortices.

**Why one crew lived: the sources describe, they do not conclude.** W14 says the TV crew "was impacted by a very rapidly moving interior subvortex", and that over the research car it sat nearly still for about 20 s. The script may lay those two facts side by side. It may not say "this is why they survived": no source says it.

## 5. The twelve in the drains. Two groups; the tie to the table is OUR INFERENCE

- **A family of seven (FOX):** "believed to have left their Oklahoma City home when the storms rolled through the area and then walked to a nearby drainage ditch where they thought they would be safe. While the family was not affected by the high winds, a surge of powerful water from the accompanying rains hurled them through the dark, concrete tunnel where they were taking shelter." Deputy Fire Chief Marc Woodard: carried five miles downstream. FOX, citing La Prensa Libre, names Yolanda Santos Solís (37) and her children Brandon (8), Leslie (6) and Christopher (4), and Samuel Cifuentes, Floridalma Santos Cucúm and Alexander Cifuentes Santos.
- **A group of eleven (N9):** "A group of 11, including mostly young children, huddled together inside a storm drain under S.W. 15th near the Dell plant to escape the tornadoes. When the water level got to about two feet, the group tried to get out, but could not. The raging water swept all 11 into the Oklahoma River a quarter of a mile away." One three-year-old was pronounced dead that night; on 3 Jun four were still missing, aged 21, six months, 3 and 4.
- **Inference, by script:** 7 + 5 = 12, the number of ditch rows in Appendix C, and the ages match within a year except one (press 37, table 34). 18 people went into the two drains; 12 did not survive; 6 from the second group did. The table names no one, so this pairing is ours.
- **Conflict:** FOX says the three Cifuentes family members "were killed when the vehicle they were driving in through the storm crashed". Appendix C has only one flood death in a vehicle (M 65), which fits the later local reporting that all seven were in the ditch. **CONFIRMED all seven were in the ditch** by News 9, Deanne Stein, "OKC Family Mourns Adults, Kids Killed After Taking Shelter In Drainage Ditch" (Wayback Machine snapshot of 8 Jun 2013, read directly): "when the tornado sirens blared in Oklahoma City on Friday, Samuel Cifuentes left his home near N.W. 26th Street and Meridian with his wife, Florinda Santos and their son, Alex as well as her cousin, Yolanda Santos and her three children, Cristofer, Brandon and Lesly. The seven went only a few feet away into a drainage ditch, only to be washed away by floodwaters." Family member Enma Aguilar: "They were in the ditch because they thought it was the safest spot because they just thought it was going to be a tornado, not a flooding. They didn't imagine that." And: "The family says they took a table from the home and hid under it in the ditch." Florinda Santos was recovered along Deep Fork Creek, "four miles from where the family took shelter". The FOX vehicle account is the early, wrong one. Still not read: the 9 Jun report of the last recovery.
- **What came near them:** OUN tornado 10 was an EF1 from 4 SE Yukon to "W OKC (SW 15th/Meridian)", 6:51 to 7:09 PM CDT, no deaths, no injuries. Tornadoes 13, 14 and 15 in the city were EF1, EF0 and EF1. Every tornado that entered the city that evening was EF0 or EF1 and none took a life. The distance from tornado 10's end point to either drain was not measured.

## 6. The warning and Spanish speakers. CONFIRMED as a gap, NOT CONFIRMED as a cause

- SA: "Among those killed during the May 31 tornado and ensuing flooding was a Guatemalan family whose primary language was Spanish. In interviews with EMs and broadcast meteorologists, they acknowledged that there are insufficient forecast and warning resources for those who do not speak English."
- SA: "Only a few radio and television stations broadcast in Spanish".
- **The assessment does not say the language gap caused this family's decision**, and FOX says they left "when the storms rolled through". The script can say the assessment raised the gap in the same paragraph as this family. It cannot say the warning never reached them.

## 7. The fairness twist. CONFIRMED (the tweet), PARTLY CONFIRMED (the broadcast wording)

- SA: "Fact: At 1 p.m. on May 31, WFO Norman tweeted, 'TORNADO SAFETY: If you choose to flee in your car, plan for and anticipate traffic jams and blocked roads, hail, heavy rain and flooding.'"
- SA: "People followed atypical media advice to immediately drive south as storms were bearing down on Oklahoma City." And: "The atypical response of many residents evacuating from the tornadoes rather than following shelter plans led to the traffic jams and accidents on May 31." And: "Some weather warning professionals heightened public anxiety by telling listeners they would be unable to survive if not underground".
- GAZ quotes the KFOR chief meteorologist: "leave south Oklahoma City and go south. Do it right now." and, a little later, "get in your car and drive south." GAZ also quotes Gary England of KWTV calling the advice "dangerous".
- **The exact words were not checked against the broadcast recording**, and an NBC transcript of the feed reads slightly differently. Narrate with the assessment's sentence. A quoted line on screen waits for the recording.

## Still open after this pass
- The date and source of the return to EF3 (the 4 Jun 2013 upgrade statement is now in section 2).
- The News 9 report of 9 Jun 2013 on the last recovery (the main report on the family is now read and quoted in section 5).
- Richard Henderson's age: Appendix C has a 35-year-old "Vehicle, storm chasing" row, no name.
- The circumstance of the June 1 Okfuskee County flood death.
- The broadcast recording for the exact words.
