Ignoring 10 permissions.allow entries from .claude/settings.json: this workspace has not been trusted. Run Claude Code interactively here once and accept the trust dialog, or set projects["C:/Users/Sidhartha"].hasTrustDialogAccepted: true in C:\Users\Sidhartha\.claude-accounts\claude7\.claude.json.
## Channel checks

| Metric | Critical Latitude | Forecast Files |
|---|---|---|
| Subs | 5,010 | 1,300 |
| Videos | 3 | 11 |
| Channel age | Joined Apr 1 2016 (dormant, pivoted to this format ~Jul 2026) | Joined Jun 28 2026 (brand new) |
| Total views | 116,728 | 97,208 |
| Avg views/video | 38,909 | 8,837 |
| Avg video length | 26.3 min | 11.9 min |
| Top video | "America's Most Dangerous Fault..." — 189K views | "Scientists Monitoring 9.0 West Coast Earthquake" — 79K views |
| jWfHJ5pc1f4 (source video) | 18K views (30:38) — *not* actually the top performer on the channel | — |
| Category/format | Weather, news-doc, faceless | Weather, news-doc, faceless |
| RPM estimate | $6.37 | $5.24 |
| Monetized | No | No |

Note: Critical Latitude's channel-outliers/faceless-classifier calls hit the free-tier daily cap (10/24h, already exhausted) — metrics above come from `youtube_channel_videos` (popular sort) + `get_batch_channel_metrics_v2` instead, which cover everything needed since both channels only have 3 and 11 videos respectively (easy to eyeball manually).

## Teardown per video

Full a–g breakdown for all 4 videos (SkyWhisper "Joplin", Dark Horizon "Katrina", Critical Latitude "Cascadia", Forecast Files "9.0 West Coast") — verbatim hooks, retention lines, survivor quotes, and outros — is in the subagent's report above. Key numbers it measured directly from transcript: Joplin 2,646 words/~142 wpm; Katrina 2,582 words/~136 wpm; Critical Latitude 5,529 words/~180 wpm; Forecast Files 2,830 words/~186 wpm.

## Cross-video formula (weighted toward Joplin/Katrina)

All four share: (1) hook within 10–15s — either a found-footage/audio cold-open or a present-tense "this is happening to you" stat; (2) a thesis/foreshadow line in the first 60–90s that the whole video pays off later; (3) short declarative "breath mark" sentences ending nearly every beat; (4) stats always translated into human-scale comparisons (Formula 1 speed, "longer than California"); (5) a recurring honesty/credibility signal ("no hype," "the honest truth is"). The two proven outliers both bank emotional payoff at the *end* (Joplin's 5 hero vignettes, Katrina's Superdome material) rather than spreading it evenly (observation only; placement rule: script-scaling.md "Emotion", owner 4 Oct 26).

## Differences worth stealing

- **SkyWhisper**: location-by-location "march" structure (new building + death count every ~60-90s) turns stats into a serialized mini-cliffhanger anthology; skips subscribe CTA entirely, closes on pure aphorism.
- **Dark Horizon**: plants the full thesis/twist in the cold open (institutional-negligence angle deepens dread rather than spoiling it).
- **Critical Latitude**: puts the engagement CTA *inside* the hook (~55s) rather than only at the outro; runs an explicit myth-correction segment naming a competing wrong narrative.
- **Forecast Files**: contrarian thesis ("not terrifying") on the same subject as competitors; explicit callback structure (hook anecdote replayed verbatim as the emotional climax); named-scientist attribution throughout instead of anonymous "one scientist said."

Ran the analysis to fit the ~45-call budget (used ~13 nexlev calls total); the `youtube_channel_outliers` tool was already rate-limited before I started, so I substituted direct video-list inspection for the outlier detection on both small channels.
