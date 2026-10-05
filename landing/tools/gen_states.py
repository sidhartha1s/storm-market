#!/usr/bin/env python3
"""Generate landing/states/<slug>/index.html for every row in state_data.csv,
plus landing/states/index.html (menu), rendered in the shared Binder chrome
(landing/tools/chrome.py). Deterministic transform only: every fact comes
from the CSV; nothing about a specific state is invented here.
Run from anywhere: python3 landing/tools/gen_states.py
"""
import csv
import html
import json
import os
import re
import urllib.parse

import chrome

HERE = os.path.dirname(os.path.abspath(__file__))
LANDING = os.path.dirname(HERE)
CSV_PATH = os.path.join(HERE, "state_data.csv")
STATES_DIR = os.path.join(LANDING, "states")

SITE = "https://paulraymond.online"

# ---------------------------------------------------------------- helpers --

def esc(s):
    """HTML-escape a stripped field. Also swaps a stray em dash for a colon
    (Binder copy carries none) — a mechanical, meaning-preserving glyph swap,
    not a rewording; the source CSV itself is left untouched."""
    s = (s or "").strip()
    s = s.replace(" — ", ": ").replace("—", ": ")
    return html.escape(s, quote=True)


def denash(s):
    """Same swap as esc(), for the title/description candidates below, which
    are plain strings (not yet html-escaped) at the point they need it."""
    return s.replace(" — ", ": ")


def slug_for(state):
    if state == "District of Columbia":
        return "washington-dc"
    return re.sub(r"[^a-z0-9]+", "-", state.lower()).strip("-")


def gumroad_url(state):
    variant = urllib.parse.quote(state)
    return f"https://paulraymond.gumroad.com/l/packet?wanted=true&variant={variant}"


def fit_title(state):
    # Candidates keep the original em dash so the <=60 selection below picks
    # the same candidate per state as before; denash() runs only on the winner.
    candidates = [
        f"{state} Storm Preparedness — Shelter Rebates, Alerts, Checklist",
        f"{state} Storm Preparedness — Shelter & Alerts Checklist",
        f"{state} Storm-Ready Checklist — Shelter & Alerts",
        f"{state}: The Storm-Ready Checklist",
    ]
    for c in candidates:
        if len(c) <= 60:
            return denash(c)
    return denash(candidates[-1][:60])


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
            return denash(c)
    return denash(candidates[-1][:155])


# ---------------------------------------------------------- hazard prose --
# One generic, factual paragraph per hazard TYPE, written once and reused
# across every state that lists it. Never state-specific.
HAZARD_COPY = {
    "Tornado": "Tornadoes form fast, and even a well-run warning system only buys "
        "minutes. The National Weather Service's after-action reports on the "
        "deadliest US tornadoes trace back to the same pattern: people heard a "
        "warning, stepped outside to look for the funnel, and lost the time a "
        "sheltered household would have had. A named safe room (the lowest "
        "floor, smallest interior room, most walls between you and outside) "
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
        "rain: the 30-30 rule (shelter if under 30 seconds between flash and "
        "bang, wait 30 minutes after the last one) still holds. It is also the "
        "hazard households prepare for least, because it rarely triggers a "
        "county-level warning of its own.",
    "Hurricane and storm surge": "Storm surge, not wind, is the deadliest part "
        "of a hurricane for most coastal households: it can arrive hours "
        "before landfall and reach well inland of any beachfront. Evacuation "
        "zones are set by surge modeling, not by category number, which is why "
        "a weaker storm on a bad track can flood a zone a stronger storm on a "
        "better track never touches. Knowing your zone before the season, not "
        "during the warning, is the single highest-leverage step.",
    "Extreme heat": "Extreme heat kills more people in an average US year than "
        "any other weather hazard, and most of those deaths are preventable: "
        "the risk concentrates in the first heat wave of the season, before "
        "bodies acclimate, and in households without reliable cooling. Checking "
        "on elderly or isolated neighbors during a heat advisory does more than "
        "any single piece of equipment.",
    "Extreme cold": "Extreme cold turns ordinary failures (a stalled car, a "
        "lost power connection, a wet coat) into emergencies far faster than "
        "people expect, and hypothermia risk starts well above freezing once "
        "wind and moisture are factored in. Frozen and burst pipes are the "
        "most common property-damage claim tied to cold snaps, and they are "
        "largely preventable with basic insulation and a known shutoff valve.",
    "Blizzard and ice storm": "Ice storms cause more prolonged power outages "
        "than almost any other winter hazard, because ice loads snap tree "
        "limbs and power lines that snow alone would not touch: outages can "
        "run days in rural areas. Blizzards add near-zero visibility and "
        "windchill to the mix. A household's real blizzard plan is a heat "
        "source that doesn't depend on grid power and a stocked pantry that "
        "doesn't need refrigeration.",
    "Wildfire": "Wildfire risk to a home is decided mostly in the first five "
        "feet around the structure (the \"home ignition zone\") where embers "
        "carried well ahead of the flame front land on roofs, gutters, and "
        "anything flammable pressed against the wall. A go-bag and a named "
        "evacuation trigger matter because wildfire evacuation orders can "
        "arrive with far less notice than a hurricane or even a tornado watch.",
    "Extreme rainfall and flash flood": "Flash flooding is the deadliest "
        "hazard tied to rainfall, and most of those deaths are people driving "
        "into water they underestimated: six inches of moving water can stall "
        "a car, twelve can float one. Rainfall intensity, not just total "
        "inches, is what overwhelms storm drains and low-lying roads in a "
        "window of an hour or less.",
    "Riverine and coastal flooding": "Riverine and coastal flooding move on a "
        "slower clock than flash flooding (hours to days instead of minutes), "
        "which is exactly why households underprepare for it. Flood damage "
        "is excluded from standard homeowners' policies almost everywhere, "
        "so the financial exposure is separate from the physical one, and it "
        "is worth checking before, not after, the water rises.",
}


def call_item(label, name_or_text, url, phone):
    """One <li> for the who-to-call list. Skips entirely if nothing to show."""
    if not name_or_text and not url and not phone:
        return ""
    name = esc(name_or_text) if name_or_text else label
    name_html = f'<a href="{esc(url)}">{name}</a>' if url else name
    phone_html = f" &middot; {esc(phone)}" if phone else ""
    return f"<li><b>{esc(label)}</b><p>{name_html}{phone_html}</p></li>"


def build_state_page(row):
    state = row["state"].strip()
    slug = slug_for(state)
    hazards = [row[f"hazard_{i}"].strip() for i in (1, 2, 3) if row[f"hazard_{i}"].strip()]
    seasons = [row[f"season_{i}"].strip() for i in (1, 2, 3)]

    title = fit_title(state)
    description = fit_description(state, hazards)
    canonical = f"{SITE}/states/{slug}/"
    rel = "../" * 2  # states/<slug>/index.html sits 2 levels below landing/

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
              f"before the next warning: every fact linked to its source below.")

    tags = [ov.strip() for ov in row["region_overlay"].split("|") if ov.strip()]
    tags_block = ""
    if tags:
        tags_html = "".join(f'<span class="tag">{esc(t)}</span>' for t in tags)
        tags_block = f"<p>{tags_html}</p>"

    sheets = []
    tabs = []

    sheets.append(f"""<section class="sheet" id="sheet-overview">
      <p class="kick">State Guide</p>
      <h1>{esc(state)}: The Storm-Ready Checklist</h1>
      <p class="lead">{intro}</p>
      {tags_block}
    </section>""")
    tabs.append(("sheet-overview", "Overview"))

    # ---- shelter & mitigation money (always renders) ----
    mit_program = row["mitigation_program"].strip()
    mit_url = row["mitigation_url"].strip()
    wind_ded = row["wind_deductible_note"].strip()
    roof_acv = row["roof_acv_note"].strip()
    parts = []
    if mit_program:
        link = f'<a href="{esc(mit_url)}">{esc(mit_program)}</a>' if mit_url else esc(mit_program)
        parts.append(f"<p>{esc(state)} runs {link}: check current eligibility and funding rounds "
                      f"directly on the program page before applying.</p>")
    else:
        parts.append(f"<p>No dedicated state-run storm-shelter rebate or grant program is "
                      f"listed for {esc(state)} in the mitigation data reviewed for this page. "
                      f"Check with the state emergency management agency below for anything new.</p>")
    if wind_ded:
        parts.append(f"<p>{esc(wind_ded)}</p>")
    if roof_acv:
        parts.append(f"<p>{esc(roof_acv)}</p>")
    sheets.append(f"""<section class="sheet" id="sheet-shelter">
      <p class="kick">Money</p>
      <h2>Shelter &amp; mitigation money</h2>
      {''.join(parts)}
    </section>""")
    tabs.append(("sheet-shelter", "Shelter & Money"))

    # ---- who to call (always renders) ----
    call_items = ""
    call_items += call_item("Emergency management",
                             row["em_agency"].strip() or "State emergency management agency",
                             row["em_url"].strip(), row["em_phone"].strip())
    call_items += call_item("Insurance regulator",
                             row["doi_agency"].strip() or "State insurance regulator",
                             row["doi_url"].strip(), row["doi_phone"].strip())
    if row["alerts_note"].strip() or row["alerts_url"].strip():
        call_items += call_item("Weather alerts", row["alerts_note"].strip(),
                                 row["alerts_url"].strip(), "")
    call_items += call_item("Energy bill assistance (LIHEAP)", "",
                             row["energy_assist_url"].strip(), row["energy_assist_phone"].strip())
    call_items += call_item("Well water testing", row["well_test_contact"].strip(),
                             row["well_test_url"].strip(), "")
    sheets.append(f"""<section class="sheet" id="sheet-call">
      <p class="kick">Contacts</p>
      <h2>Who to call, before and after</h2>
      <ul class="ruled">
        {call_items}
      </ul>
    </section>""")
    tabs.append(("sheet-call", "Who to Call"))

    # ---- hazards (always renders) ----
    hz_items = ""
    for hz, se in zip(hazards, seasons):
        copy = HAZARD_COPY.get(hz, "")
        lead_in = f"Peak season: {esc(se)}. " if se else ""
        hz_items += f"<li><b>{esc(hz)}</b><p>{lead_in}{copy}</p></li>"
    sheets.append(f"""<section class="sheet" id="sheet-hazards">
      <p class="kick">Hazards</p>
      <h2>The hazards {esc(state)} actually faces</h2>
      <ul class="ruled">
        {hz_items}
      </ul>
    </section>""")
    tabs.append(("sheet-hazards", "Hazards"))

    # ---- rules worth knowing (conditional: only if any rule is present) ----
    pharm = row["pharmacy_refill_law"].strip()
    winter_d = row["winter_disconnect"].strip()
    summer_d = row["summer_disconnect"].strip()
    rule_items = ""
    if pharm:
        rule_items += f"<li><b>Emergency prescription refills</b><p>{esc(pharm)}</p></li>"
    if winter_d:
        rule_items += f"<li><b>Winter utility shutoff protection</b><p>{esc(winter_d)}</p></li>"
    if summer_d:
        rule_items += f"<li><b>Summer utility shutoff protection</b><p>{esc(summer_d)}</p></li>"
    if rule_items:
        sheets.append(f"""<section class="sheet" id="sheet-rules">
      <p class="kick">Know Before You Need It</p>
      <h2>Rules worth knowing</h2>
      <ul class="ruled">
        {rule_items}
      </ul>
    </section>""")
        tabs.append(("sheet-rules", "Rules to Know"))

    # ---- FAQ (always renders) ----
    if mit_program:
        faq1 = f"{esc(state)} runs {esc(mit_program)}, a state shelter/mitigation program. Check the program page for current funding and eligibility."
    else:
        faq1 = f"No dedicated state-run storm-shelter rebate or grant program is listed for {esc(state)} in the mitigation data reviewed here. The state emergency management agency is the best source for anything new."
    faq2 = f"{esc(state)}'s primary weather hazards are {hz_join}."
    doi_name = row["doi_agency"].strip() or "the state insurance regulator"
    faq3 = f"Insurance in {esc(state)} is regulated by {esc(doi_name)}."

    verified = row["verified_on"].strip()
    verified_html = (f'<p class="verified" style="font-family:var(--mono);font-size:12.5px;color:var(--faded);'
                      f'margin-top:22px">Data verified {esc(verified)}, sources linked inline.</p>'
                      if verified else "")

    sheets.append(f"""<section class="sheet" id="sheet-faq">
      <p class="kick">FAQ</p>
      <h2>Frequently asked</h2>
      <dl class="faq">
        <div><dt>Does {esc(state)} offer storm shelter rebates?</dt><dd>{faq1}</dd></div>
        <div><dt>What natural disasters does {esc(state)} get?</dt><dd>{faq2}</dd></div>
        <div><dt>Who regulates insurance in {esc(state)}?</dt><dd>{faq3}</dd></div>
      </dl>
      {verified_html}
    </section>""")
    tabs.append(("sheet-faq", "FAQ"))

    # ---- get the book: fixed final tab, book CTA + state packet CTA ----
    gumroad = gumroad_url(state)
    sheets.append(f"""<section class="sheet" id="sheet-book">
      <p class="kick">Get the Book</p>
      <h2>The 130 things you can do before the next one.</h2>
      <div class="row">
        <div>
          <p class="lead">A 486-page manual built from the post-storm reports. 130 numbered
            protections, 23 hazard playbooks, a 60-day sequence, and the printable binder.</p>
          <p><a class="btn" href="{chrome.BUY}">Get the book, $9.99</a></p>
        </div>
        <figure style="margin:0"><img class="cover" src="{rel}assets/cover-mini.webp" width="150" height="225" alt="The Storm-Ready Home by Paul Raymond, book cover"></figure>
      </div>
      <div style="margin-top:44px;padding-top:36px;border-top:2px dashed var(--rule)">
        <h2>Get your free {esc(state)} packet</h2>
        <p class="lead">Every contact and program on this page, plus a one-page printable checklist for {esc(state)}.</p>
        <p><a class="btn" href="{esc(gumroad)}">Get your free {esc(state)} packet &rarr;</a></p>
      </div>
    </section>""")
    tabs.append(("sheet-book", "Get the Book"))

    # ---- FAQPage JSON-LD (logic unchanged; none of these three facts ever
    #      contain an em dash, so this is byte-for-byte identical to before) ----
    faq_ld_items = [
        {"q": f"Does {state} offer storm shelter rebates?", "a": re.sub("<[^>]+>", "", faq1)},
        {"q": f"What natural disasters does {state} get?", "a": re.sub("<[^>]+>", "", faq2)},
        {"q": f"Who regulates insurance in {state}?", "a": re.sub("<[^>]+>", "", faq3)},
    ]
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

    head_extra = f"""<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta property="og:type" content="website">
<meta property="og:url" content="{esc(canonical)}">
<meta name="twitter:card" content="summary_large_image">
<style>.tag{{font-family:var(--mono);font-size:11.5px;letter-spacing:.1em;text-transform:uppercase;
  color:var(--soft);border:1px solid var(--rule);padding:5px 10px;border-radius:2px;
  display:inline-block;margin:2px 8px 2px 0}}</style>"""

    body_extra = f'<script type="application/ld+json">{json.dumps(faq_ld, ensure_ascii=False)}</script>'

    doc = chrome.render(
        title=esc(title),
        description=esc(description),
        canonical=esc(canonical),
        tabs=tabs,
        sheets="\n".join(sheets),
        depth=2,
        head_extra=head_extra,
        body_extra=body_extra,
    )
    return slug, doc


def build_menu(rows):
    canonical = f"{SITE}/states/"

    title = "State-by-State Storm Guides — Shelter Rebates, Alerts, Contacts"
    if len(title) > 60:
        title = "State Storm Guides — Shelter Rebates & Alerts"
    title = denash(title)

    description = ("Every US state's storm hazards, shelter and mitigation money, "
                    "emergency contacts, and utility rules in one place — verified sources.")
    if len(description) > 155:
        description = description[:155]
    description = denash(description)

    groups = {}
    for row in rows:
        primary = row["region_overlay"].split("|")[0].strip() or "Other"
        groups.setdefault(primary, []).append(row)
    order = sorted(groups.keys(), key=lambda k: (-len(groups[k]), k))

    region_html = ""
    for region in order:
        items = sorted(groups[region], key=lambda r: r["state"].strip())
        grid_items = ""
        for r in items:
            state_r = r["state"].strip()
            hazards_r = [r[f"hazard_{i}"].strip() for i in (1, 2, 3) if r[f"hazard_{i}"].strip()]
            teaser = ", ".join(hazards_r)
            grid_items += (
                f'<li data-name="{esc(state_r.lower())}">'
                f'<a href="{esc(slug_for(state_r))}/">'
                f'<b>{esc(state_r)}</b>'
                f'<span class="hz">{esc(teaser)}</span>'
                f'<span class="go">Open the {esc(state_r)} guide &rarr;</span>'
                f"</a></li>"
            )
        region_html += f"""<div class="regionhead">{esc(region)}</div>
      <ul class="stategrid">
        {grid_items}
      </ul>
      """

    sheets = [f"""<section class="sheet" id="sheet-directory">
      <p class="kick">State Guides &middot; 50 states + DC</p>
      <h1>Where do you live?</h1>
      <p class="lead">Every state has a page: the three hazards it actually faces, the
        shelter rebates and grants on offer, who answers the phone before and after, and the
        rules worth knowing, every fact linked to its source.</p>
      <div class="finder">
        <input id="q" type="search" placeholder="Type your state&hellip;" autocomplete="off" aria-label="Find your state">
        <span class="hint">or scroll and tap any card &darr;</span>
      </div>
      <p class="nomatch" id="nomatch" hidden>No state matches that, check the spelling, or scroll.</p>
      {region_html}
    </section>""", f"""<section class="sheet" id="sheet-book">
      <p class="kick">Get the Book</p>
      <h2>Every state packet is already inside the book.</h2>
      <div class="row">
        <div>
          <p class="lead">The Storm-Ready Home ships all 51 state packets with its 130
            protections, 23 hazard playbooks and the printable binder.</p>
          <p><a class="btn" href="{chrome.BUY}">Get the book, $9.99</a></p>
        </div>
        <figure style="margin:0"><img class="cover" src="../assets/cover-mini.webp" width="150" height="225" alt="The Storm-Ready Home by Paul Raymond, book cover"></figure>
      </div>
    </section>"""]

    tabs = [("sheet-directory", "State Directory"), ("sheet-book", "Get the Book")]

    head_extra = f"""<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:image" content="{SITE}/assets/og.png">
<meta property="og:type" content="website">
<meta property="og:url" content="{esc(canonical)}">
<meta name="twitter:card" content="summary_large_image">
<style>
.finder{{display:flex;align-items:center;gap:18px;flex-wrap:wrap;margin:24px 0 8px}}
.finder input{{flex:1 1 320px;max-width:420px;font-family:var(--body);font-size:20px;padding:12px 16px;
  background:#fff;color:var(--ink);border:2px solid var(--cta);border-radius:6px;outline:none}}
.finder input:focus{{box-shadow:0 0 0 3px rgba(194,87,27,.25)}}
.finder .hint{{font-family:var(--mono);font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:var(--faded)}}
.nomatch{{font-family:var(--mono);font-size:14px;color:var(--faded);padding:12px 0}}
.nomatch[hidden]{{display:none}}
.regionhead{{font-family:var(--mono);font-size:13px;letter-spacing:.18em;text-transform:uppercase;
  color:var(--faded);border-top:2px solid var(--ink);padding-top:10px;margin:34px 0 6px}}
.regionhead[hidden]{{display:none}}
.stategrid{{list-style:none;margin:14px 0 0;padding:0;display:grid;
  grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:6px 20px}}
.stategrid li{{border-bottom:1px solid var(--rule)}}
.stategrid li[hidden]{{display:none}}
.stategrid a{{display:block;padding:10px 2px 12px;text-decoration:none;color:var(--ink)}}
.stategrid a:hover b{{color:var(--cta)}}
.stategrid b{{display:block;font-family:var(--display);font-weight:700;font-size:18px}}
.stategrid .hz{{display:block;font-size:14px;color:var(--soft);margin-top:2px}}
.stategrid .go{{display:block;font-family:var(--mono);font-size:11px;letter-spacing:.08em;
  text-transform:uppercase;color:var(--cta);margin-top:6px}}
@media(max-width:640px){{.stategrid{{grid-template-columns:repeat(auto-fill,minmax(170px,1fr))}}}}
</style>"""

    body_extra = """<script>
(function(){
  var q=document.getElementById('q'), items=[].slice.call(document.querySelectorAll('.stategrid li')),
      heads=[].slice.call(document.querySelectorAll('.regionhead')), none=document.getElementById('nomatch');
  if(!q)return;
  q.addEventListener('input',function(){
    var v=q.value.trim().toLowerCase(), shown=0;
    items.forEach(function(li){var on=!v||li.dataset.name.indexOf(v)>-1;li.hidden=!on;if(on)shown++;});
    heads.forEach(function(h){var grid=h.nextElementSibling;h.hidden=!!v&&!grid.querySelector('li:not([hidden])');});
    none.hidden=shown>0;
  });
  q.addEventListener('keydown',function(e){
    if(e.key==='Enter'){var first=items.filter(function(li){return !li.hidden;})[0];if(first)location.href=first.querySelector('a').href;}
  });
})();
</script>"""

    return chrome.render(
        title=esc(title),
        description=esc(description),
        canonical=esc(canonical),
        tabs=tabs,
        sheets="\n".join(sheets),
        depth=1,
        head_extra=head_extra,
        body_extra=body_extra,
    )


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
