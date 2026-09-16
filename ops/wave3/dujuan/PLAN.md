# Dujuan series plan (owner 16 Sep 26: 3 videos/day, in order, starting today)

## Storm state used for this plan (JMA 16 Sep 19:10 JST, JTWC warning 04)
Unnamed TD near the Marianas, 998 hPa, 30 kt. JMA: TS in 12 h, STS from +45 h (Ogasawara), +93 h (20 Sep 15:00 JST) 31.1N 139.2E "south of Japan" 975 hPa 30 m/s, +117 h (21 Sep 15:00) 37.0N 143.1E "east of Japan". JTWC peak 65 kt (75 mph) 19-21 Sep, 21/06Z at 35.7N 142.7E (~270 km east of Tokyo). Central case = close offshore pass of Kanto 20-21 Sep during Silver Week (19-23 Sep). Branch A = curves in and hits; branch B = grazes.

## The model we copy
소박사TV (Dr Soh TV, 677k subs): one ~8-min video per day per storm, title = "Typhoon No. 25 Dujuan" + the ONE development of the day ("The North Pacific High holds the key", "Imminent", "A tropical depression emerges"), 300-800k views each, map-and-model driven. umbrellaman (5.7k subs): 3:20 model-track video, 190k views. Owner's read: viewers want the specific update (expected mph, "25th typhoon"), a moving coloured track map with projections, and glassmorphic stat pushes in the first minutes.

## Cadence: every day = 1 SPINE update + 1 ANGLE + 1 EVERGREEN/FLEX
| Day | Spine (daily update, title = No. 25 Dujuan + today's development) | Angle (from the top-10) | Evergreen / flex |
|---|---|---|---|
| Tue 16 Sep | U1 "Typhoon No. 25 Dujuan Is Forming, Aimed at Japan's Biggest Holiday in 11 Years" (= #1 Silver Week Collision) | #5 JMA vs NHC: how Japan and America rank the same storm | #3 Japan's five-level evacuation alerts, explained for Americans |
| Wed 17 Sep | U2 "Dujuan Has a Name: Two Tracks, One Storm" (= #2) | #4 What American travelers in Japan should do now | #6 Why Japan's worst typhoons keep landing on holiday weeks |
| Thu 18 Sep | U3 "Dujuan Turns Toward the Ogasawara Islands at 60 mph" | #7 How Dujuan stacks up against the last decade | flex: storm surge (only if JMA issues a surge warning) |
| Fri 19 Sep | U4 "Silver Week Begins Under a Typhoon Watch" (Games open in Nagoya) | Silver Week transport: what JR/ANA/JAL have cut | flex: Ogasawara passage report |
| Sat 20 Sep | U5 "Dujuan South of Japan at 975 hPa: the 24 Hours That Decide Tokyo" | #8 prep: Kanto on the edge of the circle | flex |
| Sun 21 Sep | U6 = #8 "Dujuan's Closest Pass to Kanto" (anchor day) | live-day extra if it hits (branch A) | #10 near-miss (branch B) |
| Mon 22 Sep | U7 = #9 "After Dujuan: the first real numbers" | Silver Week wrecked: cancellations count | wrap / next storm |

Kill rule holds: a spine update ships only when an official number moved (pressure, wind, category, circle, warning level). Evergreens carry the day if the storm stalls.

## Per-video build (Format C, 8+ min, atempo 1.10, Paul corner circle, no chapter cards)
- Open 0-60 s = the stat push: glassmorphic cards over the moving track map: "TYPHOON No. 25 · 998 → 975 hPa · 35 → 63 mph (JMA) / 75 mph (US Navy)" with count-ups; every wind on screen in mph, with km/h and m/s small.
- The track map is OUR composition: Japan/western Pacific plate, JMA forecast circles and JTWC track drawn from the official JSON/text coordinates of that day, animated point to point; branch A/B drawn as two labelled tracks when the forecast is open.
- One named official quote on screen per video (JMA forecaster, JTWC bulletin, Cabinet Office, JR East, airline).
- Close on the unresolved tracking line + soft comment/subscribe.
- Footage stack: NOAA/CIRA Himawari loops, NASA Worldview, JMA graphics (credited), JTWC/US Navy graphics, DVIDS (Yokosuka/Yokota typhoon prep, PD), short narrated broadcaster pulls (NHK/TBS/ANN/FNN/Reuters), Pexels/Pixabay Tokyo/rain/shinkansen/airport b-roll.
- Pool: library/mini-storms/dujuan-2026/ (built once, in the MAIN checkout, reused by every video).

## Capacity
Each video ≈ 2.5 h of work; renders ≈ 25 min each, one at a time on the GTX 1650. 3/day = scripts and sourcing fan out to Sonnet agents while the director composes; renders queue back to back.
