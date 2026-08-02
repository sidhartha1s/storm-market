#!/usr/bin/env python3
"""Derive the mitigation_program columns — hand-researched, not scraped from a national list.

No federal or national body maintains a machine-readable table of state wind/seismic retrofit
grant programmes; IBHS's own FORTIFIED incentives page (fortifiedhome.org/incentives) mixes
insurer discount programmes, tax credits and true state grants without distinguishing them, and
several of the programmes it names moved or relaunched within the last year. So this column is
the handful of states that were confirmed, one at a time, against the *programme's own government
page* — which is exactly the "51 lookups is acceptable and expected for the legal columns"
exception in the brief, and exactly why the fill count here is 7 out of 51 rather than a
suspiciously round 51.

**Blank for most states is the correct answer.** Every state not listed below was searched and
came up with nothing, an insurer-run discount with no state grant behind it, or a programme whose
own funding status is currently too unsettled to cite responsibly (see NOTES).

  FL  My Safe Florida Home           https://mysafeflhome.com/plan-your-storm-ready-home/
  CA  Earthquake Brace + Bolt        https://www.insurance.ca.gov/0400-news/0102-alerts/2025/Earthquake-Brace-Bolt-Grant-Program-Op.cfm
  AL  Strengthen Alabama Homes       https://www.strengthenalabamahomes.com/
  LA  Louisiana Fortify Homes Program https://ldi.la.gov/fortifyhomes
  OK  Strengthen Oklahoma Homes (OKReady) https://www.oid.ok.gov/okready/
  SC  SC Safe Home Mitigation Grant Program https://doi.sc.gov/605/SC-Safe-Home
  KY  Strengthen Kentucky Homes Program https://skh.ky.gov

FL, CA and AL were already researched for Part Five, Chapter Two of the manuscript
(P5-C2-documents-money.md) and are reused here rather than re-derived, per the brief.

NOTES on the states searched and left blank on purpose:

  - **Mississippi** has run a program under two names — the Comprehensive Hurricane Damage
    Mitigation Program and "Strengthen Mississippi Homes" — administered by the Mississippi
    Insurance Department. Its funding was suspended by the legislature in a 2025 special session,
    a 2026 bill to refund and expand it (to $15,000 grants) was reported heading to the governor,
    and neither of the two URLs a web search turns up for it currently resolves: the MID
    preparedness-page URL answers a "Page not found" page (live wrapper, dead content) and the
    apps.mid.ms.gov program page answers 404. A programme that cannot currently be pointed at
    a live official page is not citable yet, even though it plainly exists.
  - **Georgia** and **Mississippi's own MWUA** run FORTIFIED insurance-premium discounts through
    the Georgia Underwriting Association and Mississippi Windstorm Underwriting Association —
    both state-created residual-market insurers, not state agencies, and both are a rate discount
    rather than a grant or credit programme. Left out rather than stretched to fit the column.
  - **North Carolina, Connecticut, New Jersey, New York, Rhode Island, Texas** were named by IBHS
    as offering discounts or credits for FORTIFIED-qualifying upgrades, but on inspection each is
    an *insurer* rate filing responding to a state mandate to offer wind-mitigation discounts
    (comparable to Florida's own Fla. Stat. § 627.0629, already covered in Protection 104), not a
    named grant or credit *programme* a homeowner applies to. Not the same thing as the seven
    above, so left blank here too.
  - Every other state: searched, nothing found.

Usage:
    python3 derive_mitigation.py                # verify the seven URLs, write mitigation.csv
    python3 derive_mitigation.py --no-verify     # skip live verification, for offline iteration
"""

import argparse
import csv
from pathlib import Path

import verify_urls
from verify_urls import DEAD

HERE = Path(__file__).parent
OUT = HERE / "mitigation.csv"

# The fifty states plus DC, same set every other fragment covers — merge.py refuses to merge a
# fragment whose state set does not match the others, so every state gets a row even though
# 44 of them are blank on purpose.
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

# (abbr, program name, url) — url doubles as its own source, there being no secondary citation
# more authoritative than the programme's own government page. Every other state is blank.
PROGRAMS = {
    "FL": ("My Safe Florida Home",
           "https://mysafeflhome.com/plan-your-storm-ready-home/"),
    "CA": ("Earthquake Brace + Bolt",
           "https://www.insurance.ca.gov/0400-news/0102-alerts/2025/Earthquake-Brace-Bolt-Grant-Program-Op.cfm"),
    "AL": ("Strengthen Alabama Homes",
           "https://www.strengthenalabamahomes.com/"),
    "LA": ("Louisiana Fortify Homes Program",
           "https://ldi.la.gov/fortifyhomes"),
    "OK": ("Strengthen Oklahoma Homes Program (OKReady)",
           "https://www.oid.ok.gov/okready/"),
    "SC": ("SC Safe Home Mitigation Grant Program",
           "https://doi.sc.gov/605/SC-Safe-Home"),
    "KY": ("Strengthen Kentucky Homes Program",
           "https://skh.ky.gov"),
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-verify", action="store_true", help="skip URL verification")
    args = parser.parse_args()

    rows, dropped, blocked, checks = [], [], [], []
    for abbr, state in STATES.items():
        row = {"state": state, "abbr": abbr,
               "mitigation_program": "", "mitigation_url": "", "mitigation_url_src": ""}
        if abbr in PROGRAMS:
            program, url = PROGRAMS[abbr]
            row["mitigation_program"], row["mitigation_url"], row["mitigation_url_src"] = program, url, url
            if not args.no_verify:
                verdict, _, why = verify_urls.check(url)
                checks.append(verdict)
                if verdict == DEAD:
                    dropped.append((state, url, why))
                    row["mitigation_program"] = row["mitigation_url"] = row["mitigation_url_src"] = ""
                elif verdict == "blocked":
                    blocked.append((state, url, why))
        rows.append(row)

    with OUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    filled = sum(1 for r in rows if r["mitigation_program"])
    print(f"wrote {OUT}  ({len(rows)} rows researched, {filled} with a confirmed programme)")
    if checks:
        print(f"  checks: {verify_urls.summarise(checks)}")
    if blocked:
        print(f"\n{len(blocked)} URL(s) published on our own prior research "
              "(the host refused us, but never said the page is gone):")
        for state, url, why in blocked:
            print(f"  {state}: {url}  [{why}]")
    if dropped:
        print(f"\n{len(dropped)} URL(s) dropped as gone — programme removed from this run:")
        for state, url, why in dropped:
            print(f"  {state}: {url}  [{why}]")
    print("\nSee the module docstring for the states searched and deliberately left blank, "
          "and why (Mississippi, Georgia, and the insurer-discount-only states).")


if __name__ == "__main__":
    main()
