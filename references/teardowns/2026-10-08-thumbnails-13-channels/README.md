# Thumbnail study: 13 channels, 8 Oct 26

Owner ask, 7 Oct 26: dissect the top thumbnails of Johnny Harris, Critical Latitude, Elias Yoder and The Japanese
Method, find weather and disaster channels with recent high views, and build a design system for Paul from it.
The systems that came out of it: `references/packaging-rules.md` "Paul on the thumbnail".

Method: `yt-dlp` flat pull of each channel's uploads (up to 600), the 10 latest plus the 10 most viewed of the
rest, each thumbnail logged field by field (text, layout, face, background, graphics).
`<slug>-meta.json` is the pull, `<slug>-dissect.json` the per-thumbnail log and the channel findings; its `by` field
says who read it and at what size. Ten channels were read one thumbnail at a time at 640 px. Three were read by the
orchestrator from contact sheets and are thinner: Critical Latitude at 640 px, Elias Yoder at 400 px with short rows,
The Japanese Method at 400 px with its 20 thumbnails logged in 6 grouped rows. Thumbnail images are not kept in the repo.

| Channel | Subscribers | Host face (thumbnails) | Studied (thumbnails) | Latest 10, median (views) | File |
|---|---|---|---|---|---|
| Johnny Harris | 7,970,000 | 17 | 20 | 3,350,000 | `johnny-dissect.json` |
| Critical Latitude | 67,400 | 13 | 20 | 300,000 | `critlat-dissect.json` |
| The Japanese Method (AI avatar) | 140,000 | 20 | 20 | hidden in the feed | `japmethod-dissect.json` |
| Elias Yoder (AI avatar) | 365,000 | 19 | 20 | 5,900 | `yoder-dissect.json` |
| TornadoTRX (tornado documentaries) | 486,000 | 0 | 19 | 2,750,000 | `trx-dissect.json` |
| Celton Henderson (tornado documentaries) | 210,000 | 0 | 20 | 869,000 | `celton-dissect.json` |
| HIGH RISK Chris (tornado documentaries) | 314,000 | 2 | 20 | 1,300,000 | `highrisk-dissect.json` |
| Pecos Hank (storm chaser) | 1,240,000 | 2 | 20 | 992,000 | `pecos-dissect.json` |
| Freddy McKinney (storm chaser) | 642,000 | 2 | 20 | 414,000 | `freddy-dissect.json` |
| Reed Timmer (storm chaser) | 2,080,000 | 1 | 20 | 128,000 | `reed-dissect.json` |
| Swegle Studios (weather explainers) | 551,000 | 0 | 20 | 236,000 | `swegle-dissect.json` |
| Ryan Hall, Y'all (forecasts) | 3,520,000 | 0 | 20 | 2,350,000 | `ryanhall-dissect.json` |
| Max Velocity (forecasts) | 2,180,000 | 0 | 20 | 783,000 | `maxvel-dissect.json` |

## What each channel does

**Johnny Harris**
- Host cut out on the left third on 9 of 17, face about 22 % of the frame width, eyes on the camera.
- White caps headline of 1 to 4 words with one red accent (10 of 20).
- One object ringed in red. Top 3 (17.0 M, 14.0 M, 14.0 M views) all use host left + caps claim + one ringed object.

**Critical Latitude**
- It changed format. Old: AI disaster scene + fake TV bar, no host: 21,000 to 196,000 views (7 thumbnails).
- New: presenter on cream graph paper + hand-drawn diagram: up to 1,700,000 views; 6 of 11 are above 450,000.
- Headline is 2 lines: black heavy caps, then the payoff word in cream on a red brush box. Her look is quiet and worried, never shouting.

**The Japanese Method (AI avatar)**
- Same man, same red polo on 20 of 20. The outfit is the logo.
- He is generated inside the scene and his hands always do something: point, pinch his nose, hold the object.
- Best 9 with known views are all a numbered grid of tiles. That part only fits list videos.

**Elias Yoder (AI avatar)**
- Same costume on 19 of 20: straw hat, beard, white shirt, suspenders.
- He points at or holds the one object the video is about.
- 8 of the popular 10 show a dollar figure; 1 of the latest 10 does. Popular: 445,000 to 2,200,000 views. Latest: 774 to 26,000.

**TornadoTRX (tornado documentaries)**
- Real storm footage as the whole frame on 18 of 19, dark and desaturated.
- Year in white over the place name in red, centred: 9 of 19, including 16.0 M and 7.6 M views.
- No host, no badge, no border on any thumbnail.

**Celton Henderson (tornado documentaries)**
- Real photograph or footage on 20 of 20.
- White heavy type with one red payoff word on 12 of 12 headline thumbnails. The red word is a rating, a count or a superlative.
- Top: Smithville, 11.0 M views, red STRONGEST over a dark tornado above ordinary houses.

**HIGH RISK Chris (tornado documentaries)**
- White caps with a red key word on 7 of 12 text thumbnails; year and place line above it on 3.
- His top video (8.0 M) is one of only 2 with the host: waist up, holding a camera pole with a CAMERA label and a red arrow, tornado behind.
- 8 of 20 have no text at all: one wide funnel with a house or car for scale.

**Pecos Hank (storm chaser)**
- Real footage on 20 of 20. Three-panel collage with a title across it on 8.
- One red accent per thumbnail on 8 of 20.
- Top 3 (29 M, 26 M, 21 M views) have no host face.

**Freddy McKinney (storm chaser)**
- Top (21 M): no text, tornado wall fills the upper two thirds, one small person in the lower third for scale.
- Red arrow onto one object on 5 of the popular 10.
- Host close-ups only on 2 recent thumbnails.

**Reed Timmer (storm chaser)**
- Real footage with no text on 10 of 20.
- Top 3 (20 M, 11 M, 10 M views): no face, no text, a large readable disaster scene.
- Popular set marks one detail in red (5 of 10); the latest set mostly does not (1 of 10).

**Swegle Studios (weather explainers)**
- Real photograph as the base on 16 of 20; caps on 20 of 20; 1 to 5 words on 16.
- One word plus a yellow arrow onto the object that carries the threat (4 thumbnails).
- No presenter portrait on any thumbnail.

**Ryan Hall, Y'all (forecasts)**
- US map on 19 of 20. No person on any thumbnail.
- 2 words, white caps with a thick black outline, top left, on 16 of 20.
- Top 3 (13.0 M, 7.2 M, 7.0 M): the same words WINTER PREDICTION over a magenta and cyan map.

**Max Velocity (forecasts)**
- Map + two-line white caps top left + one white arrow on 20 of 20. No person.
- Text is a reaction, never the title: NO WAY (5), NOT GOOD (4), GET READY (3).
- Top 3 all use a magenta hazard band on a blue map.

## Read across

- Storm and weather channels (9 studied) almost never show the host: the highest share is 2 of 20 thumbnails, and 5 channels show no host at all.
- Their winners are real storm footage or a real map plus 2 to 4 words with one red word.
- The one disaster channel where a presenter wins is Critical Latitude, after it moved from an AI disaster scene
  with a fake news bar to a presenter on cream paper beside a hand-drawn diagram.
- AI avatar channels lock one outfit and put the avatar inside the scene with his hands doing a job.
- Thumbnail words are never the title.
