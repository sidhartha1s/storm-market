# track-map.html — re-pointing to a new advisory

1. Fetch fresh data (from repo root, or anywhere — these are plain `curl`s):
   `https://www.jma.go.jp/bosai/typhoon/data/targetTc.json` to get the live `tropicalCyclone` id
   (TC2630 today; use whatever id is current), then that id's `specifications.json` and
   `forecast.json` under `https://www.jma.go.jp/bosai/typhoon/data/<ID>/`, plus JTWC's warning
   text at `https://www.metoc.navy.mil/jtwc/products/wp<basin><number>web.txt` (find today's
   filename via `https://www.metoc.navy.mil/jtwc/jtwc.html` if `wp2426web.txt` has rolled over).
   Save the three JMA files into `data/` as `jma-<UTCstamp>-{specifications,forecast,targetTc}.json`
   and the JTWC text as `data/jtwc-warning<NN>-<date><time>z.txt`.
2. Run `python3 data/build_track.py` (picks up the newest `jma-*-specifications.json` /
   `jma-*-forecast.json` glob match automatically — delete or archive old dated files if you
   don't want them picked up) — writes `data/track.json`.
3. Run `python3 data/build_js_embed.py > data/_embed.js` — prints two `const COASTLINE = ...;`
   / `const TRACK = ...;` lines.
4. Open `data/_embed.js`, copy both lines, and paste them over the two `const COASTLINE = ...;`
   / `const TRACK = ...;` lines inside `track-map.html`'s `<script>` block (search for
   `/* ---------- DATA` to find the spot). Delete `data/_embed.js` again afterward — it's a
   paste buffer, not a checked-in artifact.
5. Re-run the screenshot check before trusting it: extract the `<template>` body into a bare
   page with `../gsap.min.js` loaded, seek the `track-map` timeline to a few points, and look
   at the PNGs (see CLAUDE.md's per-composition snapshot rule). `data/build_coastline.py` only
   needs re-running if the map's geographic bounds (`LON0/LON1/LAT0/LAT1` in both the script and
   the composition) ever change — the coastline itself doesn't move day to day.

The coastline (`data/coastline.json`, from Natural Earth 110m `ne110m.geojson`, public domain)
does not need to be regenerated per advisory — only `TRACK` changes.
