#!/usr/bin/env python3
"""Derive pharmacy_refill_law for the states with a verifiable emergency-refill provision.

No single national body maintains a citable, machine-readable table of these laws for all 51
jurisdictions. NCSL holds one and sits behind a Cloudflare bot check headless Chrome does not
clear (documented in README.md). Healthcare Ready's 2022 review ("A Review of State Emergency
Prescription Protocols") is the best *survey* found, but it groups states into three buckets
(public-health-emergency-specific law, general emergency law, no law) without giving a citable
statute or days-supply figure for most of the "general emergency law" states — so it is used here
only as a map of where to look, never as the citation itself.

Every row below was instead traced to the state's own statute or administrative rule, or (where
the provision lives in agency practice rather than codified law) the board's own published
guidance — one lookup per state, which the brief calls out as expected for this column. That is
also why the fill count is 15 of 51 rather than higher: every other state was searched and no
citable standing provision was found, or (Tennessee) the only citation a search surfaced pointed
at a definitions statute that says nothing about pharmacy refills — a dead end worth recording so
nobody re-walks it and mistakes a wrong citation for a real one.

Dead ends worth recording:
  - Tennessee: search results repeatedly surfaced "TCA § 58-2-101, 20-day supply for disaster
    evacuees" as the state's provision. § 58-2-101 is the Emergency Management Act's *definitions*
    section and says nothing about pharmacy refills at all — the figure could not be traced to
    any actual statute, so Tennessee is left blank rather than publish a citation that does not
    hold up.
  - Mississippi: the only "governor declaration" refill rule found was a one-time COVID-era Board
    of Pharmacy waiver, not a standing law — left blank rather than publish an emergency practice
    as if it were codified.

Usage:
    python3 derive_pharmacy.py                # verify the sourced URLs, write pharmacy.csv
    python3 derive_pharmacy.py --no-verify      # skip live verification, for offline iteration
"""

import argparse
import csv
from pathlib import Path

import verify_urls
from verify_urls import DEAD

HERE = Path(__file__).parent
OUT = HERE / "pharmacy.csv"

STATES = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas", "CA": "California",
    "CO": "Colorado", "CT": "Connecticut", "DE": "Delaware", "DC": "District of Columbia",
    "FL": "Florida", "GA": "Georgia", "HI": "Hawaii", "ID": "Idaho", "IL": "Illinois",
    "IN": "Indiana", "IA": "Iowa", "KS": "Kansas", "KY": "Kentucky", "LA": "Louisiana",
    "ME": "Maine", "MD": "Maryland", "MA": "Massachusetts", "MI": "Michigan",
    "MN": "Minnesota", "MS": "Mississippi", "MO": "Missouri", "MT": "Montana",
    "NE": "Nebraska", "NV": "Nevada", "NH": "New Hampshire", "NJ": "New Jersey",
    "NM": "New Mexico", "NY": "New York", "NC": "North Carolina", "ND": "North Dakota",
    "OH": "Ohio", "OK": "Oklahoma", "OR": "Oregon", "PA": "Pennsylvania",
    "RI": "Rhode Island", "SC": "South Carolina", "SD": "South Dakota", "TN": "Tennessee",
    "TX": "Texas", "UT": "Utah", "VT": "Vermont", "VA": "Virginia", "WA": "Washington",
    "WV": "West Virginia", "WI": "Wisconsin", "WY": "Wyoming",
}

# abbr -> (law text, source URL). Citations are to the state's own statute/rule text, or (LA, GA)
# the licensing board's own published guidance where the rule lives in board policy.
LAWS = {
    "AZ": ("Up to a 30-day emergency refill (non-controlled) when the governor declares a state "
           "of emergency under A.R.S. § 32-1910(A)/(B); a second 30-day refill is allowed if the "
           "emergency continues 21+ days. Ends when the declaration is terminated.",
           "https://www.azleg.gov/ars/32/01910.htm"),
    "AL": ("Standing emergency refill is a 72-hour supply; a governor's emergency proclamation "
           "can extend it to a 30-day supply. Not for Schedule I/II drugs.",
           "https://law.justia.com/codes/alabama/title-34/chapter-23/article-3/section-34-23-75/"),
    "CA": ("During a proclaimed state of emergency, a pharmacist may refill a prescription "
           "without the prescriber's authorization if the prescriber is unavailable after a "
           "reasonable effort to contact them; the statute sets no fixed days-supply cap for "
           "this provision specifically (Bus. & Prof. Code § 4064).",
           "https://law.justia.com/codes/california/code-bpc/division-2/chapter-9/article-3/section-4064/"),
    "FL": ("Up to a 30-day supply once a county is under an NWS hurricane warning or a "
           "gubernatorial state-of-emergency order (Fla. Stat. § 465.0275, pharmacist side); "
           "insurers must also waive refill-too-soon restrictions and cover the 30 days "
           "(Fla. Stat. § 252.358).",
           "https://www.flsenate.gov/Laws/Statutes/2024/465.0275"),
    "GA": ("Up to a 30-day supply once the governor declares a state of emergency or the NWS "
           "issues a hurricane warning for the area, per O.C.G.A. § 26-4-80(j) and the Board of "
           "Pharmacy's standing Policy #14; not for Schedule II. Prescriber notified within 48 "
           "hours.",
           "https://gbp.georgia.gov/document/document/bop-policy-14-statement-hurricanes-helene-milton-full/download"),
    "KY": ("Up to a 30-day supply (non-controlled) when the governor issues an executive order "
           "under KRS 39A.100 activating pharmacists' emergency authority under KRS 315.500, per "
           "KRS 217.215(3).",
           "https://pharmacy.ky.gov/statutesandregulations/Pages/default.aspx"),
    "LA": ("Up to a 30-day supply once the governor declares or renews a state of emergency, "
           "under Louisiana Board of Pharmacy Rule §519 ('State of Emergency'), automatically "
           "activated by the declaration.",
           "https://www.pharmacy.la.gov/assets/docs/EmergencyCommunications/2021-2_Ida/2021-0903_BoardGuidance.pdf"),
    "MD": ("Up to a 30-day supply during a federal or state emergency declaration when the "
           "prescriber cannot be reached (versus 14 days normally); prescriber notified within "
           "7 days. Not for controlled substances. Health Occ. § 12-506.",
           "https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gho&section=12-506&enactments=false"),
    "NH": ("Only a 72-hour supply, triggered when a natural or man-made disaster itself prevents "
           "the pharmacist from contacting the prescriber (Admin. Code Ph 703.10 / RSA 318:47-f) "
           "— New Hampshire does not extend this to 30 days the way most PHE-specific states do.",
           "https://gc.nh.gov/rules/State_Agencies/ph100-2200.html"),
    "NC": ("Insurers must allow and cover an early refill for up to 29 days after the Dept. of "
           "Insurance issues a bulletin following an emergency declaration (N.C.G.S. § 58-3-228) "
           "— an insurance-coverage guarantee alongside the separate pharmacist-side refill rule.",
           "https://www.ncleg.net/enactedlegislation/statutes/html/bysection/chapter_58/gs_58-3-228.html"),
    "OK": ("Up to a 30-day supply of a non-controlled medication when the prescriber cannot be "
           "reached and the pharmacist judges it essential to health/safety; controlled "
           "substances capped at 10 days (63 O.S. § 2-309 and Board rule).",
           "https://law.justia.com/codes/oklahoma/title-63/section-63-2-309/"),
    "OR": ("Up to a 30-day supply during a declared emergency when the drug is essential to "
           "health or continuing therapy (versus 72 hours outside a declared emergency) — "
           "OAR 855-041-1120 / 855-007-0090.",
           "https://oregon.public.law/rules/oar_855-041-1120"),
    "SC": ("A one-time emergency refill of up to a 30-day supply during a declared State of "
           "Emergency, marked 'Emergency Refill' and the prescriber notified within 15 days. "
           "Not for controlled substances. S.C. Code § 40-43-170.",
           "https://llr.sc.gov/bop/emergencyalert.aspx"),
    "TX": ("Up to a 30-day supply (non-Schedule-II) when a natural/man-made disaster prevents "
           "contacting the prescriber, the governor has declared a state of disaster under Govt. "
           "Code Ch. 418, and the Board has issued its own notification. Tex. Occ. Code § 562.054.",
           "https://law.justia.com/codes/texas/occupations-code/title-3/subtitle-j/chapter-562/subchapter-b/section-562-054/"),
    "WA": ("Up to a 30-day supply of legend (non-controlled) drugs, or 7 days for Schedule "
           "III-V, once the governor issues an emergency proclamation preventing continuity of "
           "care. WAC 246-945-332.",
           "https://app.leg.wa.gov/wac/default.aspx?cite=246-945-332"),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-verify", action="store_true", help="skip URL verification")
    args = parser.parse_args()

    rows, dropped, blocked, checks = [], [], [], []
    for abbr, state in STATES.items():
        row = {"state": state, "abbr": abbr, "pharmacy_refill_law": "", "pharmacy_refill_law_src": ""}
        if abbr in LAWS:
            law, url = LAWS[abbr]
            row["pharmacy_refill_law"], row["pharmacy_refill_law_src"] = law, url
            if not args.no_verify:
                verdict, _, why = verify_urls.check(url)
                checks.append(verdict)
                if verdict == DEAD:
                    dropped.append((state, url, why))
                    row["pharmacy_refill_law"] = row["pharmacy_refill_law_src"] = ""
                elif verdict == "blocked":
                    blocked.append((state, url, why))
        rows.append(row)

    with OUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    filled = sum(1 for r in rows if r["pharmacy_refill_law"])
    print(f"wrote {OUT}  ({len(rows)} rows, {filled} with a sourced provision)")
    if checks:
        print(f"  checks: {verify_urls.summarise(checks)}")
    if blocked:
        print(f"\n{len(blocked)} URL(s) published on our own research "
              "(the host refused us, but never said the page is gone):")
        for state, url, why in blocked:
            print(f"  {state}: {url}  [{why}]")
    if dropped:
        print(f"\n{len(dropped)} URL(s) dropped as gone:")
        for state, url, why in dropped:
            print(f"  {state}: {url}  [{why}]")
    missing = sorted(set(STATES.values()) - {LAWS.get(a) and s for a, s in STATES.items() if a in LAWS})
    print("\nSee the module docstring for the Tennessee and Mississippi dead ends, and note that "
          "every state not listed in LAWS was searched and no citable standing provision was found.")


if __name__ == "__main__":
    main()
