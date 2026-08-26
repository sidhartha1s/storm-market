#!/usr/bin/env python3
"""Generate landing/states/<slug>/index.html for every row in state_data.csv,
plus landing/states/index.html (menu). Deterministic transform only — every
fact comes from the CSV; nothing about a specific state is invented here.
Run from anywhere: python3 landing/tools/gen_states.py
"""
import csv
import html
import os
import re
import urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
LANDING = os.path.dirname(HERE)
CSV_PATH = os.path.join(HERE, "state_data.csv")
STATES_DIR = os.path.join(LANDING, "states")

SITE = "https://paulraymond.online"

# ---------------------------------------------------------------- helpers --

def esc(s):
    return html.escape((s or "").strip(), quote=True)


def slug_for(state):
    if state == "District of Columbia":
        return "washington-dc"
    return re.sub(r"[^a-z0-9]+", "-", state.lower()).strip("-")


def gumroad_url(state):
    variant = urllib.parse.quote(state)
    return f"https://paulraymond.gumroad.com/l/packet?wanted=true&variant={variant}"


def fit_title(state):
    candidates = [
        f"{state} Storm Preparedness — Shelter Rebates, Alerts, Checklist",
        f"{state} Storm Preparedness — Shelter & Alerts Checklist",
        f"{state} Storm-Ready Checklist — Shelter & Alerts",
        f"{state}: The Storm-Ready Checklist",
    ]
    for c in candidates:
        if len(c) <= 60:
            return c
    return candidates[-1][:60]


def fit_description(state, hazards):
    named = ", ".join(hazards) if hazards else "severe weather"
    candidates = [
        f"{state} storm prep: shelter rebates, {named}, emergency alerts, and who to call — verified sources, no fluff.",
        f"{state} storm prep: {named} risks, shelter money, and who to call — verified sources.",
        f"{state} storm preparedness — {named}, shelter money, who to call.",
        f"{state} storm preparedness checklist — hazards, shelter money, who to call.",
    ]
    for c in candidates:
        if len(c) <= 155:
            return c
    return candidates[-1][:155]


# ---------------------------------------------------------- hazard prose --
# One generic, factual paragraph per hazard TYPE, written once and reused
# across every state that lists it. Never state-specific.
HAZARD_COPY = {
    "Tornado": "Tornadoes form fast, and even a well-run warning system only buys "
        "minutes. The National Weather Service's after-action reports on the "
        "deadliest US tornadoes trace back to the same pattern: people heard a "
        "warning, stepped outside to look for the funnel, and lost the time a "
        "sheltered household would have had. A named safe room — the lowest "
        "floor, smallest interior room, most walls between you and outside — "
        "and a rehearsed trigger point close most of that gap.",
    "Hail and derecho": "Hail and derecho winds arrive inside the same "
        "thunderstorm complex, often with less lead time than a tornado warning "
        "because the threat is the whole storm line, not a single funnel. Large "
        "hail totals more property-damage claims nationally than any other "
        "severe-storm hazard, and derecho wind gusts can match hurricane-force "
        "winds hundreds of miles from open water. Vehicles under cover and "
        "loose yard items secured before the line arrives are the cheap fix.",
    "Lightning": "Lightning is the most common severe-weather hazard by "
        "frequency, and most strikes happen well before or after the heaviest "
        "rain — the 30-30 rule (shelter if under 30 seconds between flash and "
        "bang, wait 30 minutes after the last one) still holds. It is also the "
        "hazard households prepare for least, because it rarely triggers a "
        "county-level warning of its own.",
    "Hurricane and storm surge": "Storm surge, not wind, is the deadliest part "
        "of a hurricane for most coastal households — it can arrive hours "
        "before landfall and reach well inland of any beachfront. Evacuation "
        "zones are set by surge modeling, not by category number, which is why "
        "a weaker storm on a bad track can flood a zone a stronger storm on a "
        "better track never touches. Knowing your zone before the season, not "
        "during the warning, is the single highest-leverage step.",
    "Extreme heat": "Extreme heat kills more people in an average US year than "
        "any other weather hazard, and most of those deaths are preventable — "
        "the risk concentrates in the first heat wave of the season, before "
        "bodies acclimate, and in households without reliable cooling. Checking "
        "on elderly or isolated neighbors during a heat advisory does more than "
        "any single piece of equipment.",
    "Extreme cold": "Extreme cold turns ordinary failures — a stalled car, a "
        "lost power connection, a wet coat — into emergencies far faster than "
        "people expect, and hypothermia risk starts well above freezing once "
        "wind and moisture are factored in. Frozen and burst pipes are the "
        "most common property-damage claim tied to cold snaps, and they are "
        "largely preventable with basic insulation and a known shutoff valve.",
    "Blizzard and ice storm": "Ice storms cause more prolonged power outages "
        "than almost any other winter hazard, because ice loads snap tree "
        "limbs and power lines that snow alone would not touch — outages can "
        "run days in rural areas. Blizzards add near-zero visibility and "
        "windchill to the mix. A household's real blizzard plan is a heat "
        "source that doesn't depend on grid power and a stocked pantry that "
        "doesn't need refrigeration.",
    "Wildfire": "Wildfire risk to a home is decided mostly in the first five "
        "feet around the structure — the \"home ignition zone\" — where embers "
        "carried well ahead of the flame front land on roofs, gutters, and "
        "anything flammable pressed against the wall. A go-bag and a named "
        "evacuation trigger matter because wildfire evacuation orders can "
        "arrive with far less notice than a hurricane or even a tornado watch.",
    "Extreme rainfall and flash flood": "Flash flooding is the deadliest "
        "hazard tied to rainfall, and most of those deaths are people driving "
        "into water they underestimated — six inches of moving water can stall "
        "a car, twelve can float one. Rainfall intensity, not just total "
        "inches, is what overwhelms storm drains and low-lying roads in a "
        "window of an hour or less.",
    "Riverine and coastal flooding": "Riverine and coastal flooding move on a "
        "slower clock than flash flooding — hours to days instead of minutes "
        "— which is exactly why households underprepare for it. Flood damage "
        "is excluded from standard homeowners' policies almost everywhere, "
        "so the financial exposure is separate from the physical one, and it "
        "is worth checking before, not after, the water rises.",
}


# ---------------------------------------------------------------- styles --
STYLE = """
:root{
  --paper:#f4eee1; --paper2:#ece4d2; --card:#faf6ec; --line:#d8cdb4; --rule:#b9ac8e;
  --ink:#211d16; --ink-soft:#4a4335; --faded:#6b6249;
  --sky:#151a1d; --sky2:#1e2629; --sky-line:#323d41; --sky-text:#ede7d8; --sky-dim:#a8b0ac;
  --red:#a92c1e; --red-bright:#c0392b; --amber:#c9871c; --amber-deep:#8a5a0c;
  --display:"Fraunces",Georgia,serif;
  --body:"Source Serif 4","Iowan Old Style",Georgia,serif;
  --mono:"IBM Plex Mono",ui-monospace,monospace;
  --wrap:1140px; --col:760px;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--body);
  font-size:19px;line-height:1.65;-webkit-font-smoothing:antialiased;overflow-x:hidden}
img{max-width:100%;display:block;height:auto}
a{color:var(--red)}
.wrap{max-width:var(--wrap);margin:0 auto;padding:0 24px}
.col{max-width:var(--col);margin:0 auto;padding:0 24px}
h1,h2,h3{font-family:var(--display);font-weight:700;margin:0;line-height:1.1;letter-spacing:-.015em}
p{margin:0 0 18px}
table{width:100%}
.kicker{font-family:var(--mono);font-size:13px;font-weight:600;letter-spacing:.22em;
  text-transform:uppercase;color:var(--red);margin-bottom:16px}
.kicker::before{content:"";display:inline-block;width:26px;height:2px;background:var(--red);
  vertical-align:middle;margin-right:12px}

body::after{content:"";position:fixed;inset:0;pointer-events:none;z-index:1;opacity:.5;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='140' height='140'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2'/%3E%3CfeColorMatrix values='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .035 0'/%3E%3C/filter%3E%3Crect width='140' height='140' filter='url(%23n)'/%3E%3C/svg%3E")}

.topnav{background:var(--sky);border-bottom:1px solid var(--sky-line);position:relative;z-index:3}
.topnav .wrap{display:flex;align-items:center;gap:28px;padding:14px 24px;flex-wrap:wrap}
.brand{font-family:var(--display);font-weight:900;font-size:19px;color:var(--sky-text);
  text-decoration:none;letter-spacing:-.01em}
.brand em{font-style:italic;color:var(--amber)}
.topnav nav{margin-left:auto;display:flex;gap:24px;align-items:center;flex-wrap:wrap}
.topnav nav a{font-family:var(--mono);font-size:12.5px;font-weight:500;letter-spacing:.14em;
  text-transform:uppercase;color:var(--sky-dim);text-decoration:none}
.topnav nav a:hover{color:var(--sky-text)}
.topnav nav a.on{color:var(--amber)}
.topnav .yt{display:inline-flex;align-items:center;gap:8px;border:1px solid var(--sky-line);
  padding:7px 14px;border-radius:2px;color:var(--sky-text)!important;background:var(--red);
  border-color:var(--red)}
.topnav .yt:hover{border-color:var(--red-bright);background:var(--red-bright);color:#fff!important}
.topnav .yt svg{width:16px;height:16px;fill:currentColor}

.masthead{position:relative;background:var(--sky);color:var(--sky-text);overflow:hidden;z-index:2}
.masthead::before{content:"";position:absolute;inset:-40% -20%;pointer-events:none;
  background:
    radial-gradient(60% 45% at 22% 18%,rgba(94,116,110,.34),transparent 62%),
    radial-gradient(55% 40% at 80% 8%,rgba(70,86,96,.4),transparent 60%),
    radial-gradient(70% 55% at 55% 90%,rgba(30,38,41,.9),transparent 70%),
    radial-gradient(40% 30% at 68% 34%,rgba(201,135,28,.10),transparent 65%);
  animation:drift 26s ease-in-out infinite alternate}
@keyframes drift{from{transform:translate3d(-2%,0,0) scale(1)}to{transform:translate3d(2%,1.5%,0) scale(1.04)}}
@media (prefers-reduced-motion:reduce){.masthead::before{animation:none}}
.masthead .col{position:relative;z-index:2;padding-top:64px;padding-bottom:56px}
.dispatch-no{font-family:var(--mono);font-size:13px;font-weight:600;letter-spacing:.22em;
  text-transform:uppercase;color:var(--amber);margin-bottom:18px}
.dispatch-no::before{content:"";display:inline-block;width:26px;height:2px;background:var(--amber);
  vertical-align:middle;margin-right:12px}
.masthead h1{font-size:clamp(34px,5vw,54px);font-weight:900;color:#f6f1e3;max-width:16em}
.standfirst{font-size:clamp(18px,2vw,21px);color:var(--sky-dim);line-height:1.55;
  max-width:38em;margin-top:20px}
.tagrow{margin-top:22px;display:flex;gap:8px;flex-wrap:wrap}
.tag{font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;
  color:var(--sky-text);border:1px solid var(--sky-line);padding:5px 10px;border-radius:2px}

article{position:relative;z-index:2;padding:56px 0 20px}
article h2{font-size:clamp(26px,3.2vw,32px);margin:0 0 18px}
article section{margin:0 0 56px}
article p{color:var(--ink)}

.calltable{border-collapse:collapse;margin:18px 0 0;font-size:17px}
.calltable th,.calltable td{text-align:left;padding:14px 16px;border-bottom:1px solid var(--rule);
  vertical-align:top}
.calltable th{font-family:var(--mono);font-size:12px;letter-spacing:.12em;text-transform:uppercase;
  color:var(--faded);font-weight:600;border-bottom:2px solid var(--ink)}
.calltable td b{font-family:var(--display);font-weight:700}
.calltable .ph{font-family:var(--mono);font-size:14.5px;color:var(--ink-soft)}
@media(max-width:640px){.calltable,.calltable tbody,.calltable tr,.calltable td{display:block}
  .calltable thead{display:none}
  .calltable tr{padding:14px 0;border-bottom:1px solid var(--rule)}
  .calltable td{border:0;padding:4px 0}}

.hazardlist{list-style:none;margin:0;padding:0;border-top:2px solid var(--ink)}
.hazardlist li{padding:22px 0;border-bottom:1px solid var(--rule)}
.hazardlist h3{font-size:20px;margin-bottom:6px}
.hazardlist .when{font-family:var(--mono);font-size:12.5px;letter-spacing:.1em;text-transform:uppercase;
  color:var(--red);margin-bottom:10px;display:block}
.hazardlist p{font-size:17px;color:var(--ink-soft);margin:0}

.rules{margin:0;padding:0;list-style:none}
.rules li{padding:12px 0 12px 26px;border-bottom:1px solid var(--rule);position:relative;font-size:17px}
.rules li::before{content:"—";position:absolute;left:0;color:var(--red)}

.bookcta{display:grid;grid-template-columns:150px 1fr;gap:30px;align-items:center;
  background:var(--card);border:1px solid var(--line);border-top:4px solid var(--red);
  padding:32px;margin:0;box-shadow:0 14px 30px rgba(60,48,20,.12)}
.bookcta .cover{background:linear-gradient(160deg,#232a2e,#141a1d);aspect-ratio:2/3;
  box-shadow:0 18px 34px rgba(0,0,0,.4);transform:rotate(-1.6deg);
  display:grid;place-items:center;text-align:center;padding:12px}
.bookcta .cover span{font-family:var(--display);font-weight:900;color:#f6f1e3;font-size:15px;line-height:1.25}
.bookcta .cover em{color:var(--amber);font-style:italic}
.bookcta h3{font-size:23px;margin-bottom:10px}
.bookcta p{font-size:17px;color:var(--ink-soft);margin-bottom:16px}
.btn{display:inline-block;background:var(--red);color:#fff;text-decoration:none;
  font-family:var(--display);font-weight:700;font-size:18px;padding:14px 30px;border-radius:2px;
  box-shadow:0 10px 24px rgba(169,44,30,.35)}
.btn:hover{background:var(--red-bright)}
.btn-sub{font-family:var(--mono);font-size:12.5px;color:var(--faded);margin-top:10px;letter-spacing:.04em}
@media(max-width:640px){.bookcta{grid-template-columns:1fr}.bookcta .cover{max-width:150px}}

.packetcta{background:var(--paper2);border:1px solid var(--line);border-top:4px solid var(--amber);
  padding:30px 32px;margin:0;text-align:center}
.packetcta h3{font-size:22px;margin-bottom:10px}
.packetcta p{font-size:16.5px;color:var(--ink-soft);margin-bottom:18px}
.btn.amber{background:var(--amber-deep)}
.btn.amber:hover{background:var(--amber)}

.faq{margin:0}
.faq details{border-bottom:1px solid var(--rule);padding:18px 0}
.faq summary{font-family:var(--display);font-weight:700;font-size:18.5px;cursor:pointer;
  list-style:none}
.faq summary::-webkit-details-marker{display:none}
.faq summary::before{content:"+";color:var(--red);margin-right:12px;font-family:var(--mono)}
.faq details[open] summary::before{content:"–"}
.faq p{margin:12px 0 0;font-size:16.5px;color:var(--ink-soft)}

.verified{font-family:var(--mono);font-size:12.5px;color:var(--faded);letter-spacing:.03em;
  margin-top:8px}

footer{background:var(--sky);color:var(--sky-dim);padding:36px 0;position:relative;z-index:2}
footer .wrap{max-width:var(--wrap)}
footer p{margin:0 0 10px;font-size:13px;line-height:1.6}
footer a{color:var(--sky-text)}
footer strong{color:var(--sky-text)}

.menugrid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin:0 0 48px}
.menugrid a{display:block;background:var(--card);border:1px solid var(--line);color:var(--ink);
  text-decoration:none;padding:18px 20px}
.menugrid a:hover{box-shadow:0 12px 24px rgba(60,48,20,.14);transform:translateY(-2px)}
.menugrid h3{font-size:17.5px;margin-bottom:6px}
.menugrid p{font-size:14.5px;color:var(--ink-soft);margin:0}
.regionhead{font-family:var(--mono);font-size:13px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--faded);border-top:2px solid var(--ink);padding-top:10px;margin:40px 0 20px}
@media(max-width:860px){.menugrid{grid-template-columns:1fr}}
"""

NAV = """
<div class="topnav">
  <div class="wrap">
    <a class="brand" href="/">Paul <em>Raymond</em></a>
    <nav>
      <a href="/field-notes/">Field Notes</a>
      <a href="/resources/">Free Checklists</a>
      <a class="on" href="/states/">State Guides</a>
      <a class="ytl" href="https://www.youtube.com/@PaulRaymond-s9v" rel="noopener">&#9654; The Warning Hour</a>
      <a class="buy" href="/#offer">Get the Book &mdash; $47</a>
    </nav>
  </div>
</div>
"""

FOOTER = """
<footer>
  <div class="wrap">
    <div class="bookrow">
      <img src="/assets/cover-mini.webp" alt="The Storm-Ready Home by Paul Raymond &mdash; book cover" width="96" height="144" loading="lazy">
      <div>
        <h3>The Storm-Ready Home</h3>
        <p>486 pages &middot; 130 numbered protections &middot; 23 hazard playbooks &middot; the 60-day sequence &middot; the 61-page printable binder. $47, instant PDF, 7-day money-back guarantee.</p>
      </div>
      <a class="btn" href="/#offer">Get the Book &mdash; $47 &rarr;</a>
    </div>
    <p class="small">General preparedness information for households. Not medical, legal,
      engineering or insurance advice, and not a substitute for the instructions of your local
      emergency officials. In an emergency, call 911 and follow the direction of authorities.</p>
    <p class="small">Figures cited to their issuing documents. Public-domain material reproduced under
      17 U.S.C. &sect; 105. <strong>No agency of the United States Government has endorsed, reviewed, or is
      affiliated with this book.</strong></p>
    <p class="small"><a href="/#offer">Get the book</a> &middot; <a href="/">Home</a> &middot; <a href="/field-notes/">Field Notes</a> &middot;
      <a href="/resources/">Free checklists</a> &middot; <a href="/states/">State guides</a> &middot;
      <a href="/about/">About</a> &middot; <a href="/privacy.html">Privacy</a> &middot; <a href="/terms.html">Terms</a> &middot;
      <a href="https://www.youtube.com/@PaulRaymond-s9v" rel="noopener">&#9654; The Warning Hour on YouTube</a></p>
  </div>
</footer>
"""


def head(title, description, canonical, favicon="data:,"):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta property="og:type" content="website">
<meta property="og:url" content="{esc(canonical)}">
<link rel="canonical" href="{esc(canonical)}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{favicon}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,600;9..144,700;9..144,900&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>{STYLE}</style>
<style id="chrome">
.topnav{{position:sticky;top:0;z-index:40;box-shadow:0 6px 24px rgba(0,0,0,.35)}}
.topnav nav a.buy{{background:var(--red);color:#fff!important;font-family:var(--display);font-weight:700;
  font-size:15px;letter-spacing:0;text-transform:none;padding:9px 18px;border-radius:2px;
  box-shadow:0 8px 20px rgba(169,44,30,.4);border:0}}
.topnav nav a.buy:hover{{background:var(--red-bright)}}
.topnav nav a.ytl{{color:var(--sky-dim)}}
@media(max-width:760px){{.topnav .wrap{{gap:12px;padding:10px 16px}}.topnav nav{{gap:12px}}
  .topnav nav a.buy{{padding:8px 12px;font-size:14px}}.topnav nav a.ytl{{display:none}}}}
footer{{background:var(--sky);color:var(--sky-dim)}}
footer .bookrow{{display:grid;grid-template-columns:96px 1fr auto;gap:26px;align-items:center;
  background:#1e2629;border:1px solid var(--sky-line);padding:22px 26px;margin-bottom:34px}}
footer .bookrow img{{width:96px;height:auto;box-shadow:0 12px 26px rgba(0,0,0,.55);transform:rotate(-1.6deg)}}
footer .bookrow h3{{font-family:var(--display);font-size:22px;color:var(--sky-text);margin:0 0 6px;line-height:1.1}}
footer .bookrow p{{font-size:15px;color:var(--sky-dim);margin:0;line-height:1.5}}
footer .bookrow .btn{{white-space:nowrap}}
footer .small{{font-family:var(--mono);font-size:12px;line-height:1.7;max-width:70em;color:var(--sky-dim)}}
footer a{{color:var(--sky-text)}}
@media(max-width:760px){{footer .bookrow{{grid-template-columns:96px 1fr}}footer .bookrow .btn{{grid-column:1/-1;text-align:center}}}}
.bookcta .cover{{background:none;padding:0;display:block;overflow:hidden}}
.bookcta .cover img{{width:100%;height:100%;object-fit:cover;display:block}}
.samplestrip{{display:flex;align-items:center;gap:18px;background:var(--sky);color:var(--sky-text);
  padding:16px 22px;margin:34px 0 10px;border-left:4px solid var(--amber)}}
.samplestrip img{{width:46px;height:auto;flex:none;box-shadow:0 8px 18px rgba(0,0,0,.5);transform:rotate(-2deg)}}
.samplestrip p{{margin:0;font-size:16px;color:var(--sky-dim);line-height:1.45}}
.samplestrip b{{color:#fff}}
.samplestrip a{{color:var(--amber);font-family:var(--mono);font-size:12.5px;letter-spacing:.12em;
  text-transform:uppercase;white-space:nowrap;margin-left:auto;text-decoration:none}}
.samplestrip a:hover{{color:#fff}}
@media(max-width:640px){{.samplestrip{{flex-wrap:wrap}}.samplestrip a{{margin-left:0}}}}
.gate{{background:var(--card);border:1px solid var(--line);border-top:4px solid var(--amber);
  padding:30px 32px;margin:44px 0 24px;display:grid;grid-template-columns:1fr auto;gap:24px;align-items:center}}
.gate .k{{font-family:var(--mono);font-size:12px;letter-spacing:.2em;text-transform:uppercase;color:var(--amber-deep,#8a5a0c);margin-bottom:8px}}
.gate h3{{font-family:var(--display);font-size:24px;margin:0 0 8px;line-height:1.1}}
.gate p{{margin:0;font-size:16.5px;color:var(--ink-soft)}}
.gate .ghost{{display:inline-block;border:2px solid var(--ink);color:var(--ink);font-family:var(--display);
  font-weight:700;font-size:17px;padding:12px 24px;border-radius:2px;text-decoration:none;white-space:nowrap}}
.gate .ghost:hover{{background:var(--ink);color:var(--paper)}}
.gate .sub{{font-family:var(--mono);font-size:12px;color:var(--faded);margin-top:8px}}
@media(max-width:640px){{.gate{{grid-template-columns:1fr}}}}
@media print{{.topnav,footer,.samplestrip,.gate,.bookcta{{display:none!important}}}}
</style>
</head>
<body>
"""


def call_row(label, agency_or_text, url, phone):
    """One <tr> for the who-to-call table. Skips entirely if nothing to show."""
    if not agency_or_text and not url and not phone:
        return ""
    name = esc(agency_or_text) if agency_or_text else label
    if url:
        name_cell = f'<b><a href="{esc(url)}">{name}</a></b>'
    else:
        name_cell = f"<b>{name}</b>"
    phone_cell = f'<span class="ph">{esc(phone)}</span>' if phone else "—"
    return f"<tr><td>{esc(label)}</td><td>{name_cell}</td><td>{phone_cell}</td></tr>\n"


def build_state_page(row):
    state = row["state"].strip()
    slug = slug_for(state)
    hazards = [row[f"hazard_{i}"].strip() for i in (1, 2, 3) if row[f"hazard_{i}"].strip()]
    seasons = [row[f"season_{i}"].strip() for i in (1, 2, 3)]

    title = fit_title(state)
    description = fit_description(state, hazards)
    canonical = f"{SITE}/states/{slug}/"

    # ---- direct-answer intro ----
    hz_txt = []
    for hz, se in zip(hazards, seasons):
        if se:
            hz_txt.append(f"{hz.lower()} ({se})")
        else:
            hz_txt.append(hz.lower())
    if len(hz_txt) >= 2:
        hz_join = ", ".join(hz_txt[:-1]) + f" and {hz_txt[-1]}"
    else:
        hz_join = hz_txt[0] if hz_txt else "severe weather"
    intro = (f"{state}'s biggest weather risks are {hz_join}. This page collects the state's "
              f"emergency contacts, shelter and mitigation money, and the rules worth knowing "
              f"before the next warning — every fact linked to its source below.")

    tags = []
    for ov in row["region_overlay"].split("|"):
        ov = ov.strip()
        if ov:
            tags.append(f'<span class="tag">{esc(ov)}</span>')

    # ---- shelter & mitigation section ----
    mitigation_html = ""
    mit_program = row["mitigation_program"].strip()
    mit_url = row["mitigation_url"].strip()
    wind_ded = row["wind_deductible_note"].strip()
    roof_acv = row["roof_acv_note"].strip()
    if mit_program or wind_ded or roof_acv:
        parts = []
        if mit_program:
            link = f'<a href="{esc(mit_url)}">{esc(mit_program)}</a>' if mit_url else esc(mit_program)
            parts.append(f"<p>{state} runs {link} — check current eligibility and funding rounds "
                          f"directly on the program page before applying.</p>")
        else:
            parts.append(f"<p>No dedicated state-run storm-shelter rebate or grant program is "
                          f"listed for {esc(state)} in the mitigation data reviewed for this page. "
                          f"Check with the state emergency management agency below for anything new.</p>")
        if wind_ded:
            parts.append(f"<p>{esc(wind_ded)}</p>")
        if roof_acv:
            parts.append(f"<p>{esc(roof_acv)}</p>")
        mitigation_html = f"""<section>
      <h2>Shelter &amp; mitigation money</h2>
      {''.join(parts)}
    </section>
    """

    # ---- who to call table ----
    rows_html = ""
    rows_html += call_row("Emergency management",
                           row["em_agency"].strip() or "State emergency management agency",
                           row["em_url"].strip(), row["em_phone"].strip())
    rows_html += call_row("Insurance regulator",
                           row["doi_agency"].strip() or "State insurance regulator",
                           row["doi_url"].strip(), row["doi_phone"].strip())
    if row["alerts_note"].strip() or row["alerts_url"].strip():
        rows_html += call_row("Weather alerts", row["alerts_note"].strip(),
                               row["alerts_url"].strip(), "")
    rows_html += call_row("Energy bill assistance (LIHEAP)", "",
                           row["energy_assist_url"].strip(), row["energy_assist_phone"].strip())
    rows_html += call_row("Well water testing", row["well_test_contact"].strip(),
                           row["well_test_url"].strip(), "")

    call_section = f"""<section>
      <h2>Who to call, before and after</h2>
      <table class="calltable">
        <thead><tr><th>Purpose</th><th>Contact</th><th>Phone</th></tr></thead>
        <tbody>
        {rows_html}
        </tbody>
      </table>
    </section>
    """

    # ---- hazards section ----
    hz_items = ""
    for hz, se in zip(hazards, seasons):
        copy = HAZARD_COPY.get(hz, "")
        when = f"Peak season: {esc(se)}" if se else ""
        hz_items += f"""<li><h3>{esc(hz)}</h3>{f'<span class="when">{when}</span>' if when else ''}
        <p>{copy}</p></li>
        """
    hazards_section = f"""<section>
      <h2>The hazards {esc(state)} actually faces</h2>
      <ul class="hazardlist">
        {hz_items}
      </ul>
    </section>
    """

    # ---- rules worth knowing ----
    rules = []
    pharm = row["pharmacy_refill_law"].strip()
    winter_d = row["winter_disconnect"].strip()
    summer_d = row["summer_disconnect"].strip()
    if pharm:
        rules.append(f"<li><b>Emergency prescription refills:</b> {esc(pharm)}</li>")
    if winter_d:
        rules.append(f"<li><b>Winter utility shutoff protection:</b> {esc(winter_d)}</li>")
    if summer_d:
        rules.append(f"<li><b>Summer utility shutoff protection:</b> {esc(summer_d)}</li>")
    rules_section = ""
    if rules:
        rules_section = f"""<section>
      <h2>Rules worth knowing</h2>
      <ul class="rules">
        {''.join(rules)}
      </ul>
    </section>
    """

    gumroad = gumroad_url(state)
    top_packet_cta = f"""<div class="packetcta">
      <h3>Get Your Free {esc(state)} Packet</h3>
      <p>Every contact and program on this page, plus a one-page printable checklist for {esc(state)}.</p>
      <a class="btn amber" href="{esc(gumroad)}">Get Your Free {esc(state)} Packet &rarr;</a>
    </div>
    """

    book_cta = f"""<div class="bookcta">
      <div class="cover"><img src="/assets/cover-mini.webp" alt="The Storm-Ready Home by Paul Raymond &mdash; book cover" loading="lazy" width="150" height="225"></div>
      <div>
        <h3>The 130 things you can do before the next one.</h3>
        <p>A 486-page manual built from the post-storm reports. 130 numbered protections,
          23 hazard playbooks, a 60-day sequence, and the printable binder.</p>
        <a class="btn" href="/#offer">Get the Book — $47 &rarr;</a>
        <div class="btn-sub">Instant PDF · Pay once, own it forever · 7-day money-back guarantee</div>
      </div>
    </div>
    """

    # ---- FAQ ----
    if mit_program:
        faq1 = f"{esc(state)} runs {esc(mit_program)}, a state shelter/mitigation program. Check the program page for current funding and eligibility."
    else:
        faq1 = f"No dedicated state-run storm-shelter rebate or grant program is listed for {esc(state)} in the mitigation data reviewed here. The state emergency management agency is the best source for anything new."
    faq2 = f"{esc(state)}'s primary weather hazards are {hz_join}."
    doi_name = row["doi_agency"].strip() or "the state insurance regulator"
    faq3 = f"Insurance in {esc(state)} is regulated by {esc(doi_name)}."

    faq_html = f"""<section>
      <h2>Frequently asked</h2>
      <div class="faq">
        <details><summary>Does {esc(state)} offer storm shelter rebates?</summary><p>{faq1}</p></details>
        <details><summary>What natural disasters does {esc(state)} get?</summary><p>{faq2}</p></details>
        <details><summary>Who regulates insurance in {esc(state)}?</summary><p>{faq3}</p></details>
      </div>
    </section>
    """

    verified = row["verified_on"].strip()
    verified_line = f'<p class="verified">Data verified {esc(verified)}, sources linked inline.</p>' if verified else ""

    faq_ld_items = [
        {"q": f"Does {state} offer storm shelter rebates?", "a": re.sub("<[^>]+>", "", faq1)},
        {"q": f"What natural disasters does {state} get?", "a": re.sub("<[^>]+>", "", faq2)},
        {"q": f"Who regulates insurance in {state}?", "a": re.sub("<[^>]+>", "", faq3)},
    ]
    import json as _json
    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": item["q"],
                "acceptedAnswer": {"@type": "Answer", "text": item["a"]},
            }
            for item in faq_ld_items
        ],
    }

    doc = head(title, description, canonical)
    doc += NAV.format(states_on="on")
    doc += f"""
<header class="masthead">
  <div class="col">
    <div class="dispatch-no">State Guide</div>
    <h1>{esc(state)}: The Storm-Ready Checklist</h1>
    <p class="standfirst">{intro}</p>
    <div class="tagrow">{''.join(tags)}</div>
  </div>
</header>

<article>
  <div class="col">
    {mitigation_html}
    {call_section}
    {hazards_section}
    {rules_section}
    <section>{top_packet_cta}</section>
    <section>{book_cta}</section>
    {faq_html}
    {verified_line}
  </div>
</article>
"""
    doc += FOOTER
    doc += f'\n<script type="application/ld+json">{_json.dumps(faq_ld, ensure_ascii=False)}</script>\n'
    doc += "</body>\n</html>\n"
    return slug, doc


def build_menu(rows):
    groups = {}
    for row in rows:
        primary = row["region_overlay"].split("|")[0].strip() or "Other"
        groups.setdefault(primary, []).append(row)

    order = sorted(groups.keys(), key=lambda k: (-len(groups[k]), k))

    body = ""
    for region in order:
        items = sorted(groups[region], key=lambda r: r["state"])
        cards = ""
        for row in items:
            state = row["state"].strip()
            slug = slug_for(state)
            hazards = [row[f"hazard_{i}"].strip() for i in (1, 2, 3) if row[f"hazard_{i}"].strip()]
            teaser = ", ".join(hazards)
            cards += f"""<a href="/states/{slug}/" data-name="{esc(state.lower())}">
        <h3>{esc(state)}</h3>
        <p>{esc(teaser)}</p>
        <span class="go">Open the {esc(state)} guide &rarr;</span>
      </a>
      """
        body += f"""<div class="regionhead">{esc(region)}</div>
    <div class="menugrid">
      {cards}
    </div>
    """

    title = "State-by-State Storm Guides — Shelter Rebates, Alerts, Contacts"
    if len(title) > 60:
        title = "State Storm Guides — Shelter Rebates & Alerts"
    description = ("Every US state's storm hazards, shelter and mitigation money, "
                    "emergency contacts, and utility rules in one place — verified sources.")
    if len(description) > 155:
        description = description[:155]
    canonical = f"{SITE}/states/"

    doc = head(title, description, canonical)
    doc += MENU_EXTRA_CSS
    doc += NAV.format(states_on="on")
    doc += f"""
<header class="masthead">
  <div class="col" style="max-width:1000px">
    <div class="dispatch-no">State Guides · 50 states + DC</div>
    <h1>Where do you live?</h1>
    <p class="standfirst">Every state has a page: the three hazards it actually faces, the
      shelter rebates and grants on offer, who answers the phone before and after, and the
      rules worth knowing — every fact linked to its source.</p>
    <div class="finder">
      <input id="q" type="search" placeholder="Type your state&hellip;" autocomplete="off" aria-label="Find your state">
      <span class="hint">or scroll and tap any card &darr;</span>
    </div>
  </div>
</header>

<div class="menubook">
  <div class="col" style="max-width:1000px">
    <img src="/assets/cover-mini.webp" alt="" aria-hidden="true" width="64" height="96">
    <p><b>Every state packet is already inside the book.</b> The Storm-Ready Home ships all 51
      state packets with its 130 protections, 23 hazard playbooks and the printable binder.</p>
    <a class="btn" href="/#offer">Get the Book &mdash; $47 &rarr;</a>
  </div>
</div>

<article>
  <div class="col" style="max-width:1000px">
    <p class="nomatch" id="nomatch" hidden>No state matches that &mdash; check the spelling, or scroll.</p>
    {body}
  </div>
</article>
"""
    doc += MENU_EXTRA_JS
    doc += FOOTER
    doc += "</body>\n</html>\n"
    return doc


def main():
    with open(CSV_PATH, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    os.makedirs(STATES_DIR, exist_ok=True)
    count = 0
    for row in rows:
        slug, doc = build_state_page(row)
        out_dir = os.path.join(STATES_DIR, slug)
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(doc)
        count += 1

    menu_doc = build_menu(rows)
    with open(os.path.join(STATES_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(menu_doc)

    print(f"generated {count} state pages + 1 menu page in {STATES_DIR}")


if __name__ == "__main__":
    main()
