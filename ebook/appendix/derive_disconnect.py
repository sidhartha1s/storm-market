#!/usr/bin/env python3
"""Derive winter_disconnect and summer_disconnect for the states with a verifiable rule.

No working national table exists for this one. The LIHEAP Clearinghouse held exactly this table
and both its domains (liheapch.acf.gov, liheapch.acf.hhs.gov) time out entirely — the site
appears gone rather than blocked (documented in README.md). NCLC's own shutoff-protections page
404s. The National Governors Association's 2021 memo and its downloadable PDF describe only how
many states *had* a COVID-era moratorium in aggregate ("32 states and DC"), not which states or
what the rule actually is — not usable as a citation for any specific state.

So, as with pharmacy_refill_law, this is state-by-state: each row below is sourced to the state
utility commission's own page or rule, not an aggregator. That is also why the fill count is 15
of 51 — every other state was searched and either has no *statewide regulatory* rule (several
states leave this to individual utility tariffs, which is not the same as a commission rule) or
none was found in the time available.

Two things worth being explicit about, because they change what the note can honestly claim:

  - **Most winter rules protect a narrower group than "everyone."** Many condition protection on
    low income, a hardship declaration, or a payment plan being kept current — Minnesota's Cold
    Weather Rule and Michigan's Winter Protection Plan are not a blanket ban on winter shutoffs.
    The note says who is protected, not just the date range, so the packet doesn't over-promise.
  - **The Ohio and Arizona/California/Texas entries are recurring administrative orders or a
    program with dates set annually, not a fixed statutory date.** The dates given are the
    current cycle at time of writing (Ohio's SRO, Arizona's ACC-announced summer moratorium
    window, California's CPUC heat-index threshold); a reader should still confirm the current
    year's dates with the linked page.

Usage:
    python3 derive_disconnect.py                # verify the sourced URLs, write disconnect.csv
    python3 derive_disconnect.py --no-verify      # skip live verification, for offline iteration
"""

import argparse
import csv
from pathlib import Path

import verify_urls
from verify_urls import DEAD

HERE = Path(__file__).parent
OUT = HERE / "disconnect.csv"

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

# abbr -> {"winter": (note, url) | None, "summer": (note, url) | None}
RULES = {
    "MN": {"winter": ("Cold Weather Rule, Oct 1 - Apr 30: a utility cannot disconnect a "
                       "customer's primary heat source if the household is below 50% of state "
                       "median income and keeps an agreed payment plan (Minnesota PUC).",
                       "https://mn.gov/puc/consumers/shut-off-protection")},
    "KS": {"winter": ("Cold Weather Rule, Nov 1 - Mar 31: no disconnection when temperatures are "
                       "forecast below 35°F in the next 48 hours; a 12-month payment plan must be "
                       "offered (Kansas Corporation Commission).",
                       "https://www.kcc.ks.gov/consumer-information/cold-weather-rule")},
    "NY": {"winter": ("HEFPA winter rule, Nov 1 - Apr 15: utilities must make special contact "
                       "efforts before terminating heat-related service, plus a mandatory "
                       "holiday-period moratorium around Christmas/New Year (NY Dept. of Public "
                       "Service).",
                       "https://dps.ny.gov/winter")},
    "MA": {"winter": ("Winter moratorium, standard dates Nov 15 - Mar 15 (temporarily expanded to "
                       "Oct 27 - Apr 1 for the 2025-26 season): no shutoff of heat-related service "
                       "for a household that files a financial-hardship form (Mass. Dept. of "
                       "Public Utilities).",
                       "https://www.mass.gov/info-details/when-am-i-protected-from-having-my-utilities-shut-off")},
    "CT": {"winter": ("Winter moratorium, Nov 1 - May 1: no disconnection of gas/electric hardship "
                       "accounts lacking funds to pay in full; life-threatening loss-of-service "
                       "cases are protected year-round (PURA).",
                       "https://portal.ct.gov/heatinghelp/Winter-Protection-Program")},
    "IL": {"winter": ("Winter disconnection rule, Dec 1 - Mar 31, for customers using electric or "
                       "gas as their primary heat source (Illinois Commerce Commission).",
                       "https://icc.illinois.gov/consumers/rules-applicable-to-utilities")},
    "MI": {"winter": ("Winter Protection Plan, Nov 1 - Mar 31: shields seniors (65+) from shutoff "
                       "outright, and low-income customers who pay 7% of estimated annual usage "
                       "monthly and apply for heating assistance (Michigan PSC).",
                       "https://www.michigan.gov/-/media/Project/Websites/mpsc/consumer/info/tips/senior_protections.pdf")},
    "OH": {"winter": ("PUCO's annually-renewed Winter Reconnect/Special Reconnect Order (current "
                       "cycle Oct 13, 2025 - Apr 15, 2026) lets any residential customer "
                       "reconnect or avoid shutoff by paying a capped amount ($175) regardless of "
                       "the full balance owed; PIPP Plus caps ongoing payments at a share of "
                       "income for eligible low-income customers.",
                       "https://puco.ohio.gov/utilities/electricity/resources/utility-assistance-programs")},
    "PA": {"winter": ("Winter termination moratorium, Dec 1 - Mar 31, for households at or below "
                       "250% of the Federal Poverty Level, under the Responsible Utility Customer "
                       "Protection Act (Act 201) (Pennsylvania PUC).",
                       "https://www.puc.pa.gov/media/2761/24_act-201.pdf")},
    "WI": {"winter": ("Statewide winter disconnection moratorium, Nov 1 - Apr 15, for "
                       "heat-related residential service; a utility must file and get PSC "
                       "approval before disconnecting during the moratorium (Wis. Admin. Code "
                       "PSC 113.0304).",
                       "https://docs.legis.wisconsin.gov/code/admin_code/psc/113/iii/0304")},
    "IA": {"winter": ("Winter disconnection moratorium, Nov 1 - Apr 1, for customers certified "
                       "eligible for LIHEAP or the Weatherization Assistance Program (Iowa "
                       "Utilities Commission).",
                       "https://iuc.iowa.gov/press-release/2025-03-31/utility-shutoff-moratorium-ends")},
    "ID": {"winter": ("Winter Payment Plan, Nov 1 - Mar 31: regulated gas/electric utilities "
                       "cannot shut off service in Dec/Jan/Feb to a household with a child, a "
                       "senior (62+) or a seriously ill member that cannot pay, if enrolled in "
                       "the plan (Idaho PUC).",
                       "https://puc.idaho.gov/Fileroom/PublicFiles/Consumer/winter%20payment%20plan.pdf")},
    "AZ": {"summer": ("Summer disconnection moratorium, Jun 1 - Oct 15 (current cycle 2026); "
                       "utilities may instead choose a temperature-based rule barring shutoff "
                       "when 95°F+ or below 32°F is forecast (Arizona Corporation Commission).",
                       "https://www.azcc.gov/news/home/2026/06/02/acc-reminds-ratepayers-of-summer-utility-disconnection-moratorium--utility-bill-assistance-programs")},
    "CA": {"summer": ("CPUC bars electric disconnection for nonpayment when the CalHeatScore "
                       "heat-index forecast crosses a set threshold (lowered in 2026 from 100°F "
                       "to 90°F-equivalent), with utilities required to consult the index before "
                       "any shutoff (California PUC).",
                       "https://docs.cpuc.ca.gov/PublishedDocs/Efile/G000/M607/K785/607785658.PDF")},
    "TX": {"summer": ("No shutoff during an NWS Heat Advisory for the customer's county, plus 2 "
                       "additional days after the advisory ends; providers must also offer a "
                       "deferred payment plan for bills due during extreme weather (PUC of "
                       "Texas).",
                       "https://ftp.puc.texas.gov/public/puct-info/agency/resources/pubs/news/2024/PUCT_Emphasizes_Consumer_Protection_Rules_as_Summer_Heat_Sets_In.pdf")},
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-verify", action="store_true", help="skip URL verification")
    args = parser.parse_args()

    rows, dropped, blocked, checks = [], [], [], []
    for abbr, state in STATES.items():
        row = {"state": state, "abbr": abbr, "winter_disconnect": "", "summer_disconnect": ""}
        rule = RULES.get(abbr, {})
        for season, column in (("winter", "winter_disconnect"), ("summer", "summer_disconnect")):
            if season not in rule:
                continue
            note, url = rule[season]
            row[column] = note
            if not args.no_verify:
                verdict, _, why = verify_urls.check(url)
                checks.append(verdict)
                if verdict == DEAD:
                    dropped.append((state, column, url, why))
                    row[column] = ""
                elif verdict == "blocked":
                    blocked.append((state, column, url, why))
        rows.append(row)

    with OUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    winter_n = sum(1 for r in rows if r["winter_disconnect"])
    summer_n = sum(1 for r in rows if r["summer_disconnect"])
    print(f"wrote {OUT}  ({len(rows)} rows, {winter_n} with winter_disconnect, "
          f"{summer_n} with summer_disconnect)")
    if checks:
        print(f"  checks: {verify_urls.summarise(checks)}")
    if blocked:
        print(f"\n{len(blocked)} URL(s) published on our own research "
              "(the host refused us, but never said the page is gone):")
        for state, column, url, why in blocked:
            print(f"  {state} {column}: {url}  [{why}]")
    if dropped:
        print(f"\n{len(dropped)} URL(s) dropped as gone:")
        for state, column, url, why in dropped:
            print(f"  {state} {column}: {url}  [{why}]")
    print("\nEvery state not listed in RULES was searched and no citable statewide commission "
          "rule was found in the time available — see the module docstring.")


if __name__ == "__main__":
    main()
