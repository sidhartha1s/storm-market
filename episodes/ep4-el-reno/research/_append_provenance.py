import csv
from pathlib import Path

EP = Path("C:/Users/Sidhartha/Automation Projects/storm-market/.worktrees/ep4-el-reno-v3/episodes/ep4-el-reno")
CSV = EP / "media" / "provenance.csv"

FETCHED = "2026-08-30"

rows = []

# --- Raw sources (4) ---
rows.append([
    "broadcast/abc-families-fleeing-highways.mp4",
    "https://www.youtube.com/watch?v=Jf5zF0RG5us",
    "Claims-budgeted broadcast (ABC News, channel_id=UCBi2mrWuNuyYy4gbM6fU18Q verified)",
    FETCHED,
    "GAP A (2013 OKC interstate gridlock) source. \"Families Fleeing Storm Trapped on Okla. Highways\", uploaded 2013-06-02, 164s, 640x360 (yt-dlp android client, format 18). ABC's own aerial storm-chopper + ground gridlock b-roll (Beverly Lam interview, I-40 standstill), narrated by Alex Perez, El Reno. No third-party/chaser credit visible in the cut windows used."
])
rows.append([
    "broadcast/abc-tornadoes-rush-hour-trucks.mp4",
    "https://www.youtube.com/watch?v=eo2ncG0e2C4",
    "Claims-budgeted broadcast (ABC News, channel_id=UCBi2mrWuNuyYy4gbM6fU18Q verified)",
    FETCHED,
    "GAP A (2013 OKC interstate gridlock) source. \"Tornadoes Strike During Rush Hour, Overturn Trucks\", uploaded 2013-06-01, 169s, 640x360 (yt-dlp android client, format 18). Photojournalist Mike Betcher stand-up at El Reno + re-aired KWTV/News9-credited (official station, on the allowed list) night gridlock/traffic b-roll. First 13s of this file carries a StormChasingVideo.com dashcam credit (visible on frame-check) -- AVOIDED, not used in any cut window."
])
rows.append([
    "broadcast/kfor-chopper4-flooding-aerials.mp4",
    "https://www.youtube.com/watch?v=4tGbqM8nGi0",
    "Claims-budgeted broadcast (KFOR Oklahoma's News 4, channel_id=UCEUYiWFyzpEBMZ3aG7ud7xg verified)",
    FETCHED,
    "GAP B (May 31-June 1 2013 OKC flash-flood night) source. \"Raw: Chopper 4 aerials flooding in OKC\", uploaded 2013-06-02, 38.6s, 640x360. Silent aerial b-roll of a whole neighborhood inundated by muddy floodwater (houses/trees submerged), one continuous shot (scenedetect: 0-38.6s single scene)."
])
rows.append([
    "broadcast/kfor-flooded-streets-metro.mp4",
    "https://www.youtube.com/watch?v=t7CJnbABCH8",
    "Claims-budgeted broadcast (KFOR Oklahoma's News 4, channel_id=UCEUYiWFyzpEBMZ3aG7ud7xg verified)",
    FETCHED,
    "GAP B (May 31-June 1 2013 OKC flash-flood night) source. \"Power lines down and flooded streets throughout the metro\", uploaded 2013-06-02 (description states \"May 31\"), 170.2s, 640x360. KFOR live reporter Sarah Sellers at SW 89th & May: wind/apartment damage plus a flooded-street segment (~120-131s) with cars driving through standing water at night, headlights reflecting off floodwater, an emergency vehicle."
])

# --- GAP A cuts (3) ---
rows.append([
    "broadcast/cuts/graded/abc-families-fleeing-highways__0008.60-0013.10.mp4",
    "https://www.youtube.com/watch?v=Jf5zF0RG5us",
    "Claims-budgeted broadcast (ABC News, channel_id=UCBi2mrWuNuyYy4gbM6fU18Q verified)",
    FETCHED,
    "Derived trim of broadcast/abc-families-fleeing-highways.mp4 (4.50s); GAP A gridlock cut. Transcript: \"...traffic coming to a standstill on major highways with that storm brewing. Closer the gridlock proving deadly.\" Visual: aerial night highway light-trail shot (scenedetect scene 8.575-23.290s), ABC's own footage, no third-party credit."
])
rows.append([
    "broadcast/cuts/graded/abc-families-fleeing-highways__0024.20-0030.28.mp4",
    "https://www.youtube.com/watch?v=Jf5zF0RG5us",
    "Claims-budgeted broadcast (ABC News, channel_id=UCBi2mrWuNuyYy4gbM6fU18Q verified)",
    FETCHED,
    "Derived trim of broadcast/abc-families-fleeing-highways.mp4 (6.08s); GAP A gridlock cut. Transcript: \"With the deadly tornado looming above, a driver's nightmare was unfolding below. Complete gridlock.\" Visual: ABC aerial storm-chopper shot over the metro under a green stormy sky, cutting to nighttime cars stuck under an overpass with headlights on."
])
rows.append([
    "broadcast/cuts/graded/abc-tornadoes-rush-hour-trucks__0050.04-0056.40.mp4",
    "https://www.youtube.com/watch?v=eo2ncG0e2C4",
    "Claims-budgeted broadcast (ABC News, channel_id=UCBi2mrWuNuyYy4gbM6fU18Q verified; re-aired KWTV/News9-credited b-roll, KWTV channel_id also on the official-station allowlist)",
    FETCHED,
    "Derived trim of broadcast/abc-tornadoes-rush-hour-trucks.mp4 (6.36s); GAP A gridlock cut, the strongest of the pool. Transcript: \"Thousands of central Oklahomans, with last week's Moore tornado freshened their minds, clogged Interstate 40.\" Visual: night highway light-trail aerial (KWTV/KOTV credit) cutting to close bumper-to-bumper gridlock with an emergency vehicle's lights among stopped traffic. Frame-checked to confirm no chaser/streamer credit in this window (the file's 0-13s StormChasingVideo.com-credited segment was NOT used)."
])

# --- GAP B cuts (4) ---
rows.append([
    "broadcast/cuts/graded/kfor-chopper4-flooding-aerials__0008.00-0014.00.mp4",
    "https://www.youtube.com/watch?v=4tGbqM8nGi0",
    "Claims-budgeted broadcast (KFOR Oklahoma's News 4, channel_id=UCEUYiWFyzpEBMZ3aG7ud7xg verified)",
    FETCHED,
    "Derived trim of broadcast/kfor-chopper4-flooding-aerials.mp4 (6.00s); GAP B flood cut. Silent aerial b-roll, muddy floodwater inundating a residential neighborhood, houses and trees partly submerged -- intended to run narrated-over/with SFX, no dialogue in source."
])
rows.append([
    "broadcast/cuts/graded/kfor-chopper4-flooding-aerials__0022.00-0028.00.mp4",
    "https://www.youtube.com/watch?v=4tGbqM8nGi0",
    "Claims-budgeted broadcast (KFOR Oklahoma's News 4, channel_id=UCEUYiWFyzpEBMZ3aG7ud7xg verified)",
    FETCHED,
    "Derived trim of broadcast/kfor-chopper4-flooding-aerials.mp4 (6.00s); GAP B flood cut, second window of the same continuous aerial pass (different framing of the flooded neighborhood than the 8.00-14.00s cut) for cutaway variety."
])
rows.append([
    "broadcast/cuts/graded/kfor-flooded-streets-metro__0120.10-0125.32.mp4",
    "https://www.youtube.com/watch?v=t7CJnbABCH8",
    "Claims-budgeted broadcast (KFOR Oklahoma's News 4, channel_id=UCEUYiWFyzpEBMZ3aG7ud7xg verified)",
    FETCHED,
    "Derived trim of broadcast/kfor-flooded-streets-metro.mp4 (5.22s); GAP B flood cut. Transcript: \"...the road out here while you were sitting out here was completely flooded.\" Visual: flooded street at night, car headlights reflecting off standing water."
])
rows.append([
    "broadcast/cuts/graded/kfor-flooded-streets-metro__0125.32-0130.58.mp4",
    "https://www.youtube.com/watch?v=t7CJnbABCH8",
    "Claims-budgeted broadcast (KFOR Oklahoma's News 4, channel_id=UCEUYiWFyzpEBMZ3aG7ud7xg verified)",
    FETCHED,
    "Derived trim of broadcast/kfor-flooded-streets-metro.mp4 (5.26s); GAP B flood cut, continuation. Transcript: \"...it was several inches, almost a foot, maybe a foot and a half deep, full of water.\" Same flooded-street-at-night visual as the preceding cut."
])

# --- EXTRA cuts (12) ---
rows.append([
    "broadcast/cuts/graded/cnn-ethics-of-chasing__0055.72-0059.88.mp4",
    "see broadcast/cnn-ethics-of-chasing.mp4 row for source_url (prior session)",
    "Claims-budgeted broadcast (CNN, verified per prior session's provenance row for this parent file)",
    FETCHED,
    "Derived trim of broadcast/cnn-ethics-of-chasing.mp4 (4.16s); EXTRA cut, chasers/ethics beat, previously-unused window. Transcript: \"If you put yourself a hundred yards away from debris flying you put yourself in pretty grave danger.\""
])
rows.append([
    "broadcast/cuts/graded/cnn-ethics-of-chasing__0062.14-0069.88.mp4",
    "see broadcast/cnn-ethics-of-chasing.mp4 row for source_url (prior session)",
    "Claims-budgeted broadcast (CNN, verified per prior session's provenance row for this parent file)",
    FETCHED,
    "Derived trim of broadcast/cnn-ethics-of-chasing.mp4 (7.74s); EXTRA cut, chasers/ethics beat, previously-unused window. Transcript: Mike Eilts (Twister-research-team veteran) -- \"He thinks storm chasing has gone too far. It's no longer pictures of tornadoes that people want.\""
])
rows.append([
    "broadcast/cuts/graded/cnn-ethics-of-chasing__0096.50-0101.02.mp4",
    "see broadcast/cnn-ethics-of-chasing.mp4 row for source_url (prior session)",
    "Claims-budgeted broadcast (CNN, verified per prior session's provenance row for this parent file)",
    FETCHED,
    "Derived trim of broadcast/cnn-ethics-of-chasing.mp4 (4.52s); EXTRA cut, chasers/science beat, previously-unused window. Transcript: \"...so much still needs to be learned when it comes to violent weather. We still don't know everything about tornadoes.\" Visual opens on a KOCO-credited (official-station) tornado funnel wide shot before cutting to the CNN interview desk."
])
rows.append([
    "broadcast/cuts/graded/kfor-sutton-studio-interview__0079.04-0084.96.mp4",
    "see broadcast/kfor-sutton-studio-interview.mp4 row for source_url (prior session)",
    "Claims-budgeted broadcast (KFOR Oklahoma's News 4, channel_id=UCEUYiWFyzpEBMZ3aG7ud7xg verified)",
    FETCHED,
    "Derived trim of broadcast/kfor-sutton-studio-interview.mp4 (5.92s); EXTRA cut, storm-on-air beat, previously-unused window. Transcript: Emily Sutton -- \"...a bird fall from the sky here in a moment and then all of a sudden the wind progressed even higher and higher.\" Visual: KFOR's own \"Live 4\"-bugged chase-vehicle footage of the tornado wedge in the field, replayed under her narration."
])
rows.append([
    "broadcast/cuts/graded/kfor-sutton-studio-interview__0084.96-0091.12.mp4",
    "see broadcast/kfor-sutton-studio-interview.mp4 row for source_url (prior session)",
    "Claims-budgeted broadcast (KFOR Oklahoma's News 4, channel_id=UCEUYiWFyzpEBMZ3aG7ud7xg verified)",
    FETCHED,
    "Derived trim of broadcast/kfor-sutton-studio-interview.mp4 (6.16s); EXTRA cut, storm-on-air beat, continuation. Transcript: \"...I knew this was not good and you'll actually start to see chunks of trees...\" Same KFOR \"Live 4\" chase footage as the preceding cut."
])
rows.append([
    "broadcast/cuts/graded/koco-one-year-ago__0058.56-0063.28.mp4",
    "see broadcast/koco-one-year-ago.mp4 row for source_url (prior session)",
    "Claims-budgeted broadcast (KOCO 5 News, channel_id=UCoIhMkbeDRBImkGiA5mZp5A verified)",
    FETCHED,
    "Derived trim of broadcast/koco-one-year-ago.mp4 (4.72s); EXTRA cut, El Reno aftermath beat, previously-unused window. Transcript: \"We had a lot of loss in El Reno. The mayor of El Reno says the loss of lives forever changed...\" Visual: debris pile, reporter Kim Passoff on-camera with a resident gesturing at damage."
])
rows.append([
    "broadcast/cuts/graded/koco-one-year-ago__0094.58-0100.90.mp4",
    "see broadcast/koco-one-year-ago.mp4 row for source_url (prior session)",
    "Claims-budgeted broadcast (KOCO 5 News, channel_id=UCoIhMkbeDRBImkGiA5mZp5A verified)",
    FETCHED,
    "Derived trim of broadcast/koco-one-year-ago.mp4 (6.32s); EXTRA cut, recovery/aftermath beat, previously-unused window. Transcript: \"Today is a day of anticipation, a day of joy and excitement. One year later, the Health Center is celebrating reopening.\" Visual: El Reno Indian Health Center exterior + reopening-ceremony interior shots."
])
rows.append([
    "broadcast/cuts/graded/kfor-2019-survivor-testimony__0068.16-0073.32.mp4",
    "see broadcast/kfor-2019-survivor-testimony.mp4 row for source_url (prior session)",
    "Claims-budgeted broadcast (KFOR Oklahoma's News 4, channel_id=UCEUYiWFyzpEBMZ3aG7ud7xg verified)",
    FETCHED,
    "Derived trim of broadcast/kfor-2019-survivor-testimony.mp4 (5.16s); EXTRA cut, survivor-testimony beat, previously-unused window. Transcript: J.C. Gillig -- \"...all of a sudden my whole body, I was in pain. I couldn't hardly breathe. I kept gasping for air.\""
])
rows.append([
    "broadcast/cuts/graded/kfor-2019-survivor-testimony__0117.32-0120.40.mp4",
    "see broadcast/kfor-2019-survivor-testimony.mp4 row for source_url (prior session)",
    "Claims-budgeted broadcast (KFOR Oklahoma's News 4, channel_id=UCEUYiWFyzpEBMZ3aG7ud7xg verified)",
    FETCHED,
    "Derived trim of broadcast/kfor-2019-survivor-testimony.mp4 (3.08s); EXTRA cut, survivor-testimony beat, previously-unused window. Transcript: \"I feel God had his hand on us for sure.\""
])
rows.append([
    "broadcast/cuts/graded/koco-survivor-testimony-b__0037.38-0041.38.mp4",
    "see broadcast/koco-survivor-testimony-b.mp4 row for source_url (prior session)",
    "Claims-budgeted broadcast (KOCO 5 News, channel_id=UCoIhMkbeDRBImkGiA5mZp5A verified)",
    FETCHED,
    "Derived trim of broadcast/koco-survivor-testimony-b.mp4 (4.00s); EXTRA cut, survivor-testimony beat, previously-unused window. Transcript: \"I know we lost everything. Everything's gone.\" Visual: house-frame/timber wreckage, on-screen caption matches quote."
])
rows.append([
    "broadcast/cuts/graded/koco-survivor-testimony-c__0027.80-0034.46.mp4",
    "see broadcast/koco-survivor-testimony-c.mp4 row for source_url (prior session)",
    "Claims-budgeted broadcast (KOCO 5 News, channel_id=UCoIhMkbeDRBImkGiA5mZp5A verified)",
    FETCHED,
    "Derived trim of broadcast/koco-survivor-testimony-c.mp4 (6.66s); EXTRA cut, survivor-testimony beat, previously-unused window. Transcript: \"I told the kids, put your shoes on, tie your shoes. We all had tennis shoes tied and that tornado blew our shoes off our feet.\""
])
rows.append([
    "broadcast/cuts/graded/koco-survivor-testimony-c__0054.10-0056.94.mp4",
    "see broadcast/koco-survivor-testimony-c.mp4 row for source_url (prior session)",
    "Claims-budgeted broadcast (KOCO 5 News, channel_id=UCoIhMkbeDRBImkGiA5mZp5A verified)",
    FETCHED,
    "Derived trim of broadcast/koco-survivor-testimony-c.mp4 (2.84s); EXTRA cut, survivor-testimony beat, previously-unused window. Transcript: \"I didn't know if my mom was alive because she wasn't moving.\""
])

with CSV.open("a", newline="", encoding="utf-8") as f:
    w = csv.writer(f, quoting=csv.QUOTE_MINIMAL, lineterminator="\r\n")
    for r in rows:
        w.writerow(r)

print(f"Appended {len(rows)} rows")
