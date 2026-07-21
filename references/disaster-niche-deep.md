Ignoring 10 permissions.allow entries from .claude/settings.json: this workspace has not been trusted. Run Claude Code interactively here once and accept the trust dialog, or set projects["C:/Users/Sidhartha"].hasTrustDialogAccepted: true in C:\Users\Sidhartha\.claude-accounts\claude7\.claude.json.
## SkyWhisper deep-dive

**SkyWhisper (@geofury_here)** — 17.7K subs, 13 videos, 5.73M total views, ~440.8K avg views/video, joined Oct 2025 (~9 months old).
- Outlier: "The Worst Tornado Ever Recorded – Joplin 2011" — 2.4M views, 18:36, outlier 5.4x
- RPM: $6.69 avg ($4.57–$8.81), ~$16,075 est. earnings on that video — mid-tier, not cheap
- 100% tornado niche, no diversification. Top 10: Joplin 2.4M, El Reno 2013 828K, Deadliest Tornado Year 462K, Plainfield 454K, Jarrell 340K, CA Fire Tornado 271K, Hackleburg 234K, "Destroyed Same City 3x" 227K, Moore 1999 135K, Super Outbreak 117K

## Dark Horizon deep-dive (MoE topic spread confirmed)

**Dark Horizon (@TheDarkHorizonYT)** — 34.4K subs, 23 videos, 6.22M total views, ~270.5K avg, joined May 2025.
- Outlier: "The Storm that Drowned an Entire State – Katrina 2005" — 1.72M views, 18:59, outlier 6.3x
- RPM: $5.59 avg ($2.67–$8.51), ~$9,625 est. — average tier
- **Confirmed multi-disaster MoE**: hurricanes (Katrina, Harvey, Sandy, Andrew, Helene, Hugo, Dorian, Maria, Ivan) + fire tornado (CA 2018, 1.3M views, 4.8x) + toxic/EF-tornadoes (Picher, Smithville, El Reno, Moore, Joplin) + blizzard (NY 1993) + tsunami (Japan 2011). Hurricanes are center of gravity but non-hurricane content (fire tornado, tornado retrospectives) outperforms several hurricane entries — genuine cross-topic expert mix, not single-niche.

## Competitor channels

| Channel | Subs | Outlier video | Views | Multiple | Disaster types |
|---|---|---|---|---|---|
| Disasters Explained | 11.9K | Every BRUTAL Tornado Shape Explained In 8 Min | 986K | 11.2x | Tornado |
| Tornado Autopsy | 6.56K | The Tornado That Destroyed a Town in 8 Minutes | 147K | 11.1x | Tornado |
| StormForge | 14.1K | Hugo: The Storm That Changed the Carolinas Forever | 197K | top | Hurricane/tornado/wildfire |
| Forgotten Disasters | 7.07K | The Tragic Story of the Bath School Disaster of 1927 | 177K | top | Fires, heat waves, industrial, hurricanes |
| CJ Morgan – Florida Man Weather | 8.64K | The Blizzard That Shut Down America (1993) | 184K | top | Hurricane/blizzard/tornado |
| Carly Anna WX | 70.7K | Surviving the Unthinkable: Rainsville EF-5 | 492K | top | Tornado deep-dives |
| Doctor Prowl | 35.6K | Top 10 Scariest Natural Disaster Videos | 300K | top | Tornado/tsunami/wildfire compilations |
| Apocalypse Vision | 1.77K | Lava Tsunami Destroys New York | 55K | top | Speculative/fictional mega-disasters |
| Mother Nature's Wrath | 1.84K | Thwaites "Doomsday" Glacier Crack Doubled | 2.3K | top | Glaciers/avalanches/quakes (low traction) |

*(Rate-limited on `youtube_channel_outliers` after ~10 calls, so several entries are "top video" not a computed multiplier.)*

## Small warning-map channels

No small (<100k) channel using the literal red/yellow/green live-alert-map thumbnail format (Ryan Hall Y'all style) turned up with a strong outlier — that format is saturated by mid/large channels (Ryan Hall Y'all, Reed Timmer, Max Velocity, Nimbus Weather), which were excluded per your brief. Closest adjacent finds:

| Channel | Subs | Outlier video | Views | Published | Note |
|---|---|---|---|---|---|
| Skip Talbot Storm Chasing | 88.2K | 3 Hours of Tornadoes | 6.9M | 2020 | Raw chase footage, not map-thumbnail |
| Oklahoma Weather Couple | 5.2K | 2013 Moore EF5 – Full Live Coverage | 1.7M | 2024 reupload | Closest to live-coverage/alert feel |
| Vertical Velocity | 25.8K | Passenger train hits cars/semi | 4.2M | 2022 | Viral clip, unrelated format |

**Gap flagged:** this niche genuinely needs a dedicated `search_niche_finder_channels`/`find_outlier_faceless_channels` pass filtered to weather-broadcast category — wasn't completed within the call budget used. Worth a follow-up run if this niche matters.

## Observed formulas

- **Titles:** "The [Superlative] [Disaster] Ever Recorded – [Place] [Year]" (SkyWhisper) / "The [Verb] That [Devastating Consequence] – [Event] [Year]" (Dark Horizon) / "[X Minutes] That [Consequence]" compressed-time hook (Tornado Autopsy, Disasters Explained) / ranked-list hooks for compilation channels.
- **Recurring "greatest hits" events** re-covered across nearly every channel: **Joplin 2011** (highest-leverage single topic — hits for SkyWhisper, Tornado Autopsy, Apocalypse Vision, storm-chase reuploads), **Katrina 2005**, and the **2011 Super Outbreak**.
- **Length:** winners cluster at 13–23 min; some longer-form (28–60 min) and compilation/marathon (50–70+ min) formats also perform.
- **Thumbnails:** cinematic AI-generated wide disaster shots (funnel clouds, storm surge, wreckage) + bold all-caps place/year text overlay — consistent across nearly all sampled channels; several disclose AI-generated imagery openly, suggesting this is now standard practice, not a hidden shortcut.

One gap to flag: the warning-map niche (part C) wasn't fully resolved — worth a targeted follow-up if you want it filled in.
