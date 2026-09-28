# BRIEF — g-toll-counter-a4 · section A4, "Settled, disputed, open" (8:24) · full-frame 3-column ledger

## 0. What this graphic claims
Three outlets counted the same storm differently in the same 48 hours: Nepal's disaster agency (12/7 missing),
ANI (21/5 missing), NewsBytes (24/14 missing). The scopes and hours differ; the point is the spread, not a "true"
number.

## 1. SOURCE
Script A4: "On the twenty seventh, Nepal's disaster agency counted twelve lives lost and seven missing... That
weekend, the Indian news agency ANI put Nepal at twenty one, with five missing. The outlet NewsBytes reached
twenty four..." factcheck-A #4 confirms NewsBytes 24/14 (nationwide); "other issues" note confirms this is a
genuinely contested, unreconciled number across outlets — the card's job is to show the spread honestly.

## 2. DATUM, SCALE, ORIENTATION
Full-frame (not a footage overlay — this beat cuts to the CNBC TV18 anchor/map shot separately per script, so the
card can own the full frame briefly before that cut). Three equal columns, each 560px wide, gaps 60px, centered:
column left edges at x 96, 696, 1296 (three 560px columns + 2x60px gaps = 1880px within the 96-1824 safe zone).

## 3. GEOMETRY (px)
- Masthead: eyebrow "THE SAME STORM, THREE COUNTS" at (96,74) 22px #93a3b2; headline "The toll depends on who's
  counting." at (96,108) Arial Black 52px, wraps within 1728px.
  NOTE: masthead sits ABOVE the columns (top 74-176); columns start at top 260, so no collision.
- Each column: glass card 560x680, top 260, radius 28, glass surface per tokens.md.
  - Outlet name (row header) top 30 inside card, Arial Black 30px #f2f5f8.
  - Date line top 74, 19px #93a3b2.
  - Counter "lives lost" top 160, Courier 84px #e74c3c, label below 20px #c8d3e0.
  - Counter "missing" top 380, Courier 84px #e74c3c (dimmer, 0.85 opacity), label below.
  - Column 3 (NewsBytes) also carries "24" as its main number since that is the figure the narration names last.
- Footer line under the three cards, top 980: "Same storm, different hours, different places." Georgia italic 28px
  #d8a13a.

## 4. MUST BE TRUE IN THE PICTURE
1. Three distinct cards, each with its own outlet name AND date, never merged into one ledger row.
2. Nepal disaster agency card shows 12 / 7; ANI shows 21 / 5; NewsBytes shows 24 / 14 — exact figures, no rounding.
3. Cards land left-to-right in narration order (agency, then ANI, then NewsBytes) matching the script's order.
4. No card claims to be the final/correct count; footer reads as a caveat, not a verdict.
5. No text inside the presenter keep-out (x>=1600 y>=680) — rightmost card's right edge is x=1856, so its counter
   text (centered, well inside the card) must stay left of x=1600; verify at build time.

## 5. PANEL TEXT (exact) and CUES (175 wpm from beat start; beat = "The toll is the first thing...")
Masthead: eyebrow "THE SAME STORM, THREE COUNTS" · headline "The toll depends on who's counting."
Card 1: "NEPAL DISASTER AGENCY" · "Sept 27" · counters 12 "LIVES LOST", 7 "MISSING".
Card 2: "ANI" · "That weekend" · counters 21 "LIVES LOST", 5 "MISSING".
Card 3: "NEWSBYTES" · "Sept 28" · counter 24 "LIVES LOST" (headline number), 14 "MISSING".
Footer: "Same storm, different hours, different places."
Cues (s): masthead 0.2 · card 1 in 2.4 /* CUE "Nepal's disaster agency counted twelve" @est 4.80 */, counters run
4.8-6.3 /* CUE "seven missing" @est 7.54 */ · card 2 in 11.0 /* CUE "ANI put Nepal at twenty one" @est 13.71 */,
counters run 13.7-15.2 /* CUE "five missing" @est 16.11 */ · card 3 in 15.0 /* CUE "NewsBytes reached twenty four"
@est 17.49 */, counters run 17.5-19.0, missing counter (14) follows at 19.5 · footer 22.0 /* CUE "about seventy"
@est 22.97 (the CNBC combined figure is spoken but not shown here — it belongs to the anchor cutaway, not this
card, per mg-quickref "one fact, one instance per frame") */. Exit 24.0-24.6 (all three cards y:-30 autoAlpha:0
stagger 0.08, power3.in). Duration 25.0s declared.

## 6. CONTRACT
Standard contract. Root `#root` transparent, `data-composition-id="g-toll-counter-a4"`, PAUSED timeline at
`window.__timelines["g-toll-counter-a4"]`. Prefix ids `t4-`.

## 7. TOOLS
Same gate commands as g-toll-counter, run once across the whole episode after all comps draft.

## 8. RECEIPT
See builder's final message.
