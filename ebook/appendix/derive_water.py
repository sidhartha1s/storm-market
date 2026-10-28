#!/usr/bin/env python3
"""Derive the private-well water-testing columns for all 51 rows from two EPA sources.

Playbook 18 tells a reader on a private well to get the water tested after a flood, and the
appendix has to say who does that in their state. Two EPA pages cover every state at once:

  well_test_url      EPA's "Private Drinking Water Well Programs in Your State" page carries a
                     per-state link in an image map. These are the states' own well-program
                     pages, which is where a well owner starts.
  well_test_contact  EPA's list of state Safe Drinking Water Act laboratory certification
                     programs (40 CFR 142.10(b)(3)(i)) names the office in each state that
                     certifies the labs allowed to test drinking water. That is the office to
                     ask for a certified lab, and naming it is more useful than naming a lab
                     that may not exist next year.

URLs are checked before publishing through verify_urls.check — direct fetch, then a
headless-Chrome retry. A page the host merely refuses us stays published, because the citation
is EPA's maintained listing; only a 404 or an unresolvable hostname is dropped.

Usage:
    python3 derive_water.py                # fetch (or reuse cache), verify, write water.csv
    python3 derive_water.py --no-verify    # skip verification, for offline iteration
    python3 derive_water.py --refresh      # re-fetch both sources
"""

import argparse
import csv
import html
import re
import subprocess
from pathlib import Path

import verify_urls
from verify_urls import BLOCKED, DEAD

HERE = Path(__file__).parent
CACHE = HERE / ".agency-cache"
OUT = HERE / "water.csv"

WELLS_SOURCE = ("https://www.epa.gov/privatewells/"
                "private-drinking-water-well-programs-your-state")
LABS_SOURCE = ("https://www.epa.gov/system/files/documents/2023-03/"
               "state-cert-programs-certify-labs-to-conduct-drinking-water-analyses.pdf")

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


def cached(name, url, refresh=False, binary=False):
    CACHE.mkdir(exist_ok=True)
    path = CACHE / name
    if not path.exists() or refresh:
        data = verify_urls.fetch(url, timeout=120)
        path.write_bytes(data)
    return path.read_bytes() if binary else path.read_text(encoding="utf-8", errors="replace")


def well_urls(refresh):
    """Read the per-state links out of EPA's image map."""
    page = cached("epa_wells.html", WELLS_SOURCE, refresh)
    found = {}
    for name, url in re.findall(r'<area alt="([^"]+)"[^>]*?href="([^"]+)"', page):
        found[html.unescape(name).strip()] = re.sub(r"^http://", "https://",
                                                    html.unescape(url).strip())
    if len(found) < 40:
        raise SystemExit(f"FAIL: EPA image map yielded only {len(found)} links — page changed.")
    return found


def lab_contacts(refresh):
    """Read the certifying office for each state out of EPA's certification-program list."""
    pdf = CACHE / "epa_certlabs.pdf"
    cached("epa_certlabs.pdf", LABS_SOURCE, refresh, binary=True)
    txt = CACHE / "epa_certlabs.txt"
    # -table, not -layout: the plain layout mode folds the far-right column onto the wrong
    # rows, which silently gave Alabama the *lab list* text as its certifying office.
    subprocess.run(["pdftotext", "-table", str(pdf), str(txt)], check=True, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    text = txt.read_text(encoding="utf-8", errors="replace")

    found = {}
    for abbr, state in STATES.items():
        pattern = re.compile(rf"^{abbr}\s{{2,}}{re.escape(state)}\s{{2,}}(.+)$", re.M)
        match = pattern.search(text)
        if not match:
            continue
        # Cut at the start of the next column rather than at any run of spaces: office
        # names contain wide internal gaps ("Licensure &   Certification") that a naive
        # whitespace split truncates.
        office = re.split(r"\s{2,}(?:[A-Z]{2} DW laboratory|not available)",
                          match.group(1).strip())[0]
        office = re.sub(r"\s{2,}", " ", office).strip()
        if len(office) > 8 and not office.startswith(f"{abbr} DW"):
            found[state] = office
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-verify", action="store_true", help="skip URL verification")
    parser.add_argument("--refresh", action="store_true", help="re-fetch both sources")
    args = parser.parse_args()

    wells = well_urls(args.refresh)
    contacts = lab_contacts(args.refresh)

    rows, dropped, no_link, blocked, checks = [], [], [], [], []
    for abbr, state in STATES.items():
        url = wells.get(state, "")
        if url and not args.no_verify:
            verdict, _, why = verify_urls.check(url)
            checks.append(verdict)
            if verdict == DEAD:
                dropped.append((state, url, why))
                url = ""
            elif verdict == BLOCKED:
                blocked.append((state, url, why))
        elif not url:
            no_link.append(state)
        rows.append({
            "state": state, "abbr": abbr,
            "well_test_contact": contacts.get(state, ""),
            "well_test_url": url,
            "well_test_url_src": WELLS_SOURCE if url else "",
            "well_test_contact_src": LABS_SOURCE if contacts.get(state) else "",
        })

    with OUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {OUT}  ({len(rows)} rows)")
    print(f"  well_test_url: {sum(1 for r in rows if r['well_test_url'])}/{len(rows)}")
    print(f"  well_test_contact: {sum(1 for r in rows if r['well_test_contact'])}/{len(rows)}")
    if checks:
        print(f"  checks: {verify_urls.summarise(checks)}")
    if no_link:
        print(f"\nno link in the EPA image map: {', '.join(no_link)}")
    if blocked:
        print(f"\n{len(blocked)} URL(s) published on EPA's word "
              "(the host refused us, but never said the page is gone):")
        for state, url, why in blocked:
            print(f"  {state}: {url}  [{why}]")
    if dropped:
        print(f"\n{len(dropped)} URL(s) dropped as gone:")
        for state, url, why in dropped:
            print(f"  {state}: {url}  [{why}]")


if __name__ == "__main__":
    main()
