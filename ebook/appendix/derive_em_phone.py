#!/usr/bin/env python3
"""Derive the em_phone column from EMAC's state emergency-management directory.

usa.gov's state emergency management listing (the em_url source in derive_agencies.py) carries
no phone number, and scraping a number off each of the 51 agencies' own sites one at a time is
exactly the "inferred phone" the hard rule warns against — a phone pulled off a page by pattern
match with no human check that it is the *main* line rather than a regional office or a program
extension. What is needed instead is a second maintained directory that already did that
verification, the same way usa.gov already did it for URLs.

EMAC — the Emergency Management Assistance Compact, the interstate mutual-aid compact that every
state and territory belongs to, administered under NEMA (the National Emergency Management
Association) — publishes exactly that: one page, one phone number per state, kept current because
member states use it themselves to reach each other during a real deployment. That operational
purpose is why it is trustworthy in a way a marketing directory would not be: a wrong number on
this page breaks EMAC's own mutual-aid calls, not just a book's appendix.

    em_phone   the first non-fax phone number listed in the state's own paragraph on EMAC's
               contact page. Where a paragraph lists two numbers (a toll-free line and a direct
               line), the first one is taken, matching the order EMAC itself lists them in.

Usage:
    python3 derive_em_phone.py                # fetch (or reuse cache), verify, write em_phone.csv
    python3 derive_em_phone.py --refresh       # re-fetch the EMAC page
"""

import argparse
import csv
import re
from pathlib import Path

import verify_urls
from verify_urls import DEAD

HERE = Path(__file__).parent
CACHE = HERE / ".agency-cache"
OUT = HERE / "em_phone.csv"

SOURCE = "https://www.emacweb.org/index.php/contact/contact-your-state-ema"

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

PHONE_RE = re.compile(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")

# An address line (a street number or a PO Box) marks the end of the agency-name header. Some
# paragraphs put a military JFHQ designation before the agency name (Montana) or an "of" prefix
# on it (Washington), so the state name is looked for anywhere in the header, not just word one —
# but never past this boundary, because several *other* states' street addresses contain the word
# "Washington" (New York's own "1220 Washington Avenue", Indiana's "West Washington Street") and
# matching those would silently hand Washington State a New York phone number.
ADDRESS_LINE = re.compile(r"^\s*(\d|P\.?\s*O\.?\s*Box)", re.I)


def cached(refresh=False):
    CACHE.mkdir(exist_ok=True)
    path = CACHE / "emac_agencies.html"
    if not path.exists() or refresh:
        data = verify_urls.fetch(SOURCE, timeout=60)
        path.write_bytes(data)
    return path.read_text(encoding="utf-8", errors="replace")


def header_of(para):
    """The lines of a paragraph up to (not including) the first address line."""
    text = re.sub(r"(?s)<a[^>]*>.*?</a>", " ", para)  # drop the trailing link/URL
    header = []
    for line in re.split(r"(?i)<br\s*/?>", text):
        if ADDRESS_LINE.match(line):
            break
        header.append(line)
    return header


def phones_by_state(page):
    """Split the page into its per-agency <p> blocks, find the one whose header names each
    state, and pull the first non-fax phone out of that paragraph."""
    found = {}
    paragraphs = re.findall(r"(?is)<p(?:\s[^>]*)?>(.*?)</p>", page)
    headers = [" ".join(header_of(p)) for p in paragraphs]
    for state in STATES.values():
        pattern = re.compile(rf"\b{re.escape(state)}\b")
        for para, header in zip(paragraphs, headers):
            if not pattern.search(header):
                continue
            lines = re.split(r"(?i)<br\s*/?>", re.sub(r"(?s)<a[^>]*>.*?</a>", " ", para))
            for line in lines:
                if "fax" in line.lower():
                    continue
                match = PHONE_RE.search(line)
                if match:
                    found[state] = match.group(0).strip()
                    break
            if state in found:
                break
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true", help="re-fetch the EMAC page")
    args = parser.parse_args()

    page = cached(args.refresh)
    phones = phones_by_state(page)

    verdict, _, why = verify_urls.check(SOURCE)
    print(f"source check: {verdict} ({why})")
    if verdict == DEAD:
        raise SystemExit("FAIL: the EMAC contact page itself now answers dead — find a replacement source.")

    rows = []
    missing = []
    for abbr, state in STATES.items():
        phone = phones.get(state, "")
        if not phone:
            missing.append(state)
        rows.append({
            "state": state, "abbr": abbr,
            "em_phone": phone,
            "em_phone_src": SOURCE if phone else "",
        })

    with OUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {OUT}  ({len(rows)} rows)")
    print(f"  em_phone: {sum(1 for r in rows if r['em_phone'])}/{len(rows)}")
    if missing:
        print(f"\nno paragraph matched on EMAC's page for: {', '.join(missing)}")


if __name__ == "__main__":
    main()
