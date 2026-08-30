#!/usr/bin/env python3
"""Derive the emergency-management and insurance-regulator columns for all 51 rows.

Two federal-or-national directories carry these fields for every state at once, which beats
fifty-one hand lookups and gives one citable source per column:

  em_url      usa.gov's state emergency management directory. Each entry is the state's own
              emergency management agency, maintained by GSA as part of usa.gov.
  em_agency   read from the agency site's own <title>, not guessed from the state name. A
              title that does not actually name an agency leaves the field empty.
  doi_agency  the NAIC state insurance department directory. Each state has a detail page
  doi_phone   carrying the department's official name and its published primary number.
  doi_url     the NAIC index also lists each state's consumer-complaint page, which is the
              page a reader with a denied claim actually needs.
  alerts_url  discovered on the emergency management page itself: the link whose own text names
  alerts_note alert or notification enrolment. No national list of these exists because
              enrolment is county-level, and the agency's own page is the only authority that
              stays current. The link's visible text becomes the note, so the note is quoted
              from the agency rather than written by us.

Every URL is checked before it is published, through verify_urls.check: fetched directly, then
re-tried in headless Chrome. A page the host refuses us (403, TLS failure, timeout) is still
published, because the citation is the maintained federal or national directory that lists it
and our own blocked request is not evidence the page is gone. Only a target that answers 404 or
410 is dropped. Every run prints how much of the output was confirmed live versus taken on the
directory's word.

Raw pages are cached under .agency-cache/ so a re-run costs nothing and the extraction stays
reproducible offline.

Usage:
    python3 derive_agencies.py                # fetch (or reuse cache), verify, write agencies.csv
    python3 derive_agencies.py --no-verify    # skip URL verification, for offline iteration
    python3 derive_agencies.py --refresh      # ignore the cache and re-fetch every page
"""

import argparse
import csv
import html
import re
import urllib.parse
from pathlib import Path

import verify_urls
from verify_urls import BLOCKED, DEAD

HERE = Path(__file__).parent
CACHE = HERE / ".agency-cache"
OUT = HERE / "agencies.csv"

EM_SOURCE = "https://www.usa.gov/state-emergency-management"
DOI_SOURCE = "https://content.naic.org/state-insurance-departments"

# The fifty states plus DC, in the order the packets are generated.
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

# A <title> only names an agency if it contains one of these. Anything else ("Home",
# "Welcome", a slogan) is not an agency name and the field stays empty.
AGENCY_WORDS = ("emergency management", "emergency services", "homeland security",
                "emergency preparedness", "public safety", "emergency agency",
                "emergency division", "office of emergency")

# NAIC omits the department name from the address block for six states, so for those the name
# comes from the department's own complaint page instead — a primary source either way.
DOI_WORDS = ("insurance", "state auditor", "department of commerce", "financial regulation",
             "financial services", "financial institutions", "regulatory agencies")

PHONE_RE = re.compile(r"(?:1[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b")

# A link is an alert-enrolment link only if its own visible text says so. Matching on the href
# alone pulls in news feeds and RSS; matching on text keeps the agency as the one making the
# claim, which is also what makes the text usable verbatim as alerts_note.
ALERT_WORDS = ("alert", "notification", "notify", "warning system", "emergency notification",
               "sign up for alerts", "text alerts", "weather alerts")

# Words that mean the link is about broadcasting news, not enrolling a resident.
ALERT_EXCLUDE = ("rss", "news release", "press release", "twitter", "facebook", "newsletter",
                 "current alerts", "active alerts", "road conditions")


def cached(name, url, refresh=False, timeout=60):
    """Fetch a page once and keep it. Returns text, or None if it could not be fetched."""
    CACHE.mkdir(exist_ok=True)
    path = CACHE / name
    if path.exists() and not refresh:
        return path.read_text(encoding="utf-8", errors="replace")
    try:
        text = verify_urls.fetch(url, timeout=timeout).decode("utf-8", "replace")
    except OSError as exc:
        print(f"  fetch failed {url}: {exc}")
        return None
    path.write_text(text, encoding="utf-8")
    return text


def to_https(url):
    url = (url or "").strip()
    if not url or url.startswith("mailto:"):
        return ""
    return re.sub(r"^http://", "https://", url)


def title_of(page, words=AGENCY_WORDS):
    match = re.search(r"(?is)<title[^>]*>(.*?)</title>", page or "")
    if not match:
        return ""
    text = html.unescape(re.sub(r"\s+", " ", match.group(1))).strip()
    # Titles are usually "Home | Agency Name" or "Agency Name - Slogan". Keep the segment
    # that actually names an agency; a title with no such segment names nothing usable.
    for part in re.split(r"\s*[|\u2013\u2014-]\s*", text):
        if any(word in part.lower() for word in words):
            return part.strip()
    return ""


def alerts_link(page, base):
    """Find the alert-enrolment link on an agency page. Returns (url, link text) or ("", "").

    Deliberately conservative, because inventing an enrolment URL is exactly what the appendix
    rule forbids. A candidate has to clear all of these:

      - its own visible text names alerts, and reads as a label rather than a sentence;
      - it is not a news, social or "current alerts" feed, which broadcast rather than enrol;
      - it points at a page, not a document — an "Ash Alert" PDF press release is not a signup
        form, and its raw spaces used to crash the fetcher outright;
      - either the label says sign up, or the target path itself is alert-related.

    A page with nothing that qualifies yields nothing, which is the correct outcome.
    """
    best = ("", "", 0)
    for href, text in re.findall(r'(?is)<a[^>]+href="([^"#]+)"[^>]*>(.*?)</a>', page or ""):
        label = html.unescape(re.sub(r"(?s)<[^>]+>", " ", text))
        label = re.sub(r"\s+", " ", label).strip()
        if not 3 <= len(label) <= 60:
            continue
        low = label.lower()
        if any(word in low for word in ALERT_EXCLUDE):
            continue
        if not any(word in low for word in ALERT_WORDS):
            continue

        url = urllib.parse.urljoin(base, html.unescape(href.strip()))
        if not url.startswith("https://") or re.search(r"[\s\x00-\x1f]", url):
            continue
        if re.search(r"(?i)\.(pdf|docx?|xlsx?|pptx?|jpe?g|png)$", urllib.parse.urlparse(url).path):
            continue

        signup = any(word in low for word in
                     ("sign up", "signup", "subscribe", "enroll", "enrol", "register"))
        path_is_alerts = bool(re.search(r"(?i)alert|notif|warn", urllib.parse.urlparse(url).path))
        if not (signup or path_is_alerts):
            continue

        rank = 2 if signup else 1
        if rank > best[2]:
            best = (url, label, rank)
    return best[0], best[1]


def em_urls(refresh):
    page = cached("usa_state_em.html", EM_SOURCE, refresh)
    if not page:
        raise SystemExit(f"FAIL: could not fetch {EM_SOURCE}")
    found = dict(re.findall(r'<a class="url" id="([A-Z]{2})" href="([^"]+)"', page))
    missing = sorted(set(STATES) - set(found))
    if missing:
        raise SystemExit(f"FAIL: usa.gov listing has no entry for {missing} — layout changed.")
    return found


def doi_index(refresh):
    """Return {state name: (detail_page_url, complaint_url)} from the NAIC index."""
    page = cached("naic_index.html", DOI_SOURCE, refresh)
    if not page:
        raise SystemExit(f"FAIL: could not fetch {DOI_SOURCE}")
    selects = re.findall(r"(?s)<select[^>]*>(.*?)</select>", page)
    detail, complaint = {}, {}
    for block in selects:
        options = re.findall(r'<option value="([^"]*)"[^>]*>([^<]*)</option>', block)
        for value, label in options:
            name = html.unescape(label).strip()
            if "field_contact_state_department_target_id=" in value:
                detail[name] = urllib.parse.urljoin(DOI_SOURCE, html.unescape(value))
            elif value.startswith(("http", "mailto:")) and "naic.org" not in value:
                complaint.setdefault(name, html.unescape(value))
    # NAIC writes "District Of Columbia"; the book writes "District of Columbia".
    for table in (detail, complaint):
        for key in list(table):
            if key.lower() == "district of columbia":
                table["District of Columbia"] = table[key]
    missing = [s for s in STATES.values() if s not in detail]
    if missing:
        raise SystemExit(f"FAIL: NAIC index has no detail page for {missing} — layout changed.")
    return detail, complaint


def doi_details(page):
    """Pull the department's official name and published primary number off a detail page."""
    text = re.sub(r"(?is)<(script|style).*?</\1>", " ", page or "")
    text = re.sub(r"(?s)<[^>]+>", "\n", text).replace("&nbsp;", " ")
    text = "\n".join(line.strip() for line in text.split("\n") if line.strip())

    agency = ""
    # The address block is introduced by a bare "Main" line, then the department name.
    match = re.search(r"\nMain\n([^\n]{6,90})\n", text)
    if match and re.search(r"(?i)insurance|regulat|commerce|financial", match.group(1)):
        agency = match.group(1).strip()

    phone = ""
    match = re.search(r"Primary Phone Number:\s*\n([^\n]{7,40})", text)
    if match:
        found = PHONE_RE.search(match.group(1))
        if found:
            phone = found.group(0).strip()
    return agency, phone


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-verify", action="store_true",
                        help="skip live URL verification (offline iteration only)")
    parser.add_argument("--refresh", action="store_true",
                        help="ignore the cache and re-fetch every page")
    args = parser.parse_args()

    em = em_urls(args.refresh)
    detail_pages, complaint_pages = doi_index(args.refresh)

    rows, dropped, blocked = [], [], []
    checks = {"em_url": [], "alerts_url": [], "doi_url": []}
    for abbr, state in STATES.items():
        print(f"{abbr} {state}")
        row = {"state": state, "abbr": abbr, "em_agency": "", "em_url": "", "em_url_src": "",
               "alerts_note": "", "alerts_url": "", "alerts_url_src": "",
               "doi_agency": "", "doi_url": "", "doi_url_src": "",
               "doi_phone": "", "doi_phone_src": ""}

        url = to_https(em[abbr])
        if url:
            if args.no_verify:
                row["em_url"], row["em_url_src"] = url, EM_SOURCE
            else:
                verdict, page, why = verify_urls.check(url, want_page=True)
                checks["em_url"].append(verdict)
                if verdict == DEAD:
                    dropped.append((state, "em_url", url, why))
                else:
                    row["em_url"], row["em_url_src"] = url, EM_SOURCE
                    if page:
                        row["em_agency"] = title_of(page)
                        found, label = alerts_link(page, url)
                        if found:
                            alert_verdict, _, alert_why = verify_urls.check(found)
                            checks["alerts_url"].append(alert_verdict)
                            if alert_verdict == DEAD:
                                dropped.append((state, "alerts_url", found, alert_why))
                            else:
                                row["alerts_url"] = found
                                row["alerts_url_src"] = url
                                row["alerts_note"] = label
                                if alert_verdict == BLOCKED:
                                    blocked.append((state, "alerts_url", found, alert_why))
                    if verdict == BLOCKED:
                        blocked.append((state, "em_url", url, why))

        page = cached(f"naic_{abbr}.html", detail_pages[state], args.refresh)
        agency, phone = doi_details(page)
        row["doi_agency"] = agency
        if phone:
            row["doi_phone"], row["doi_phone_src"] = phone, DOI_SOURCE

        url = to_https(complaint_pages.get(state, ""))
        if url:
            if args.no_verify:
                row["doi_url"], row["doi_url_src"] = url, DOI_SOURCE
            else:
                verdict, page, why = verify_urls.check(url, want_page=True)
                checks["doi_url"].append(verdict)
                if verdict == DEAD:
                    dropped.append((state, "doi_url", url, why))
                else:
                    row["doi_url"], row["doi_url_src"] = url, DOI_SOURCE
                    if page and not row["doi_agency"]:
                        row["doi_agency"] = title_of(page, DOI_WORDS)
                    if verdict == BLOCKED:
                        blocked.append((state, "doi_url", url, why))
        rows.append(row)

    with OUT.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    filled = {key: sum(1 for r in rows if r[key])
              for key in ("em_url", "em_agency", "alerts_url", "doi_agency", "doi_url",
                          "doi_phone")}
    print(f"\nwrote {OUT}  ({len(rows)} rows)")
    for key, count in filled.items():
        print(f"  {key}: {count}/{len(rows)}")
    for field, verdicts in checks.items():
        if verdicts:
            print(f"  {field} checks: {verify_urls.summarise(verdicts)}")
    if blocked:
        print(f"\n{len(blocked)} URL(s) published on the directory's word "
              "(the host refused us, but never said the page is gone):")
        for state, field, url, why in blocked:
            print(f"  {state} {field}: {url}  [{why}]")
    if dropped:
        print(f"\n{len(dropped)} URL(s) dropped as gone:")
        for state, field, url, why in dropped:
            print(f"  {state} {field}: {url}  [{why}]")


if __name__ == "__main__":
    main()
