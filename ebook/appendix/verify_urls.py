#!/usr/bin/env python3
"""Shared URL fetching and liveness checking for the derive_*.py scripts.

The appendix rule is that a field is sourced and dated or it is empty. Applying it to URLs
needs one distinction the first version of these scripts got wrong: **being blocked is not
being dead.** A large share of state agency sites sit behind a WAF that rejects any
non-browser client, so treating a 403 as "gone" blanked live pages that a federal directory
actively maintains — worse data than publishing them.

So a check returns one of three verdicts:

  LIVE      the page was fetched, or rendered in headless Chrome. Publish it.
  BLOCKED   the host refused us (403/429, TLS or connection failure, timeout) but never said
            the page is gone. Publish it: the citation is the directory that lists it, and a
            maintained federal listing is better evidence than our own blocked request.
  DEAD      the target itself answered 404 or 410. Drop it — the directory has gone stale for
            that state. Note that a hostname failing to resolve does **not** count: this
            machine cannot resolve wi.gov at all while wisconsin.gov resolves fine, so a
            resolution failure says something about the resolver, not the page.

Callers log the verdict for every URL they publish, so a run always says how much of the
output was confirmed live versus taken on the directory's word.
"""

import subprocess
import urllib.error
import urllib.request
from pathlib import Path

LIVE, BLOCKED, DEAD = "live", "blocked", "dead"

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126 Safari/537.36"}
CHROME = Path("C:/Program Files/Google/Chrome/Application/chrome.exe")

# Only the target saying "this does not exist" counts as dead.
DEAD_CODES = {404, 410}


def fetch(url, timeout=60):
    """Raw bytes, or raise. Used directly when the caller wants the page, not a verdict."""
    request = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(request, timeout=timeout) as fh:
        return fh.read()


def chrome_dom(url, budget_ms=15000):
    """Render in headless Chrome. Returns the DOM, or None if Chrome could not load it.

    Chrome's own failure interstitial is identified by its ERR_ token, not by loose phrases
    like "page not found" — those appear inside perfectly good pages and were previously
    throwing away live sites.
    """
    if not CHROME.exists():
        return None
    try:
        proc = subprocess.run(
            [str(CHROME), "--headless=new", "--disable-gpu", "--dump-dom",
             f"--virtual-time-budget={budget_ms}", url],
            capture_output=True, text=True, errors="replace", timeout=budget_ms // 1000 + 75,
        )
    except (subprocess.SubprocessError, OSError):
        return None
    dom = proc.stdout
    if len(dom) < 2000:
        return None
    return None if "ERR_" in dom and "chrome-error" in dom.lower() else dom


def check(url, want_page=False):
    """Return (verdict, page_or_None, detail). Publish on LIVE or BLOCKED, drop on DEAD."""
    try:
        page = fetch(url, timeout=45).decode("utf-8", "replace")
        return LIVE, (page if want_page else None), "200"
    except urllib.error.HTTPError as exc:
        code, detail = exc.code, str(exc.code)
    except urllib.error.URLError as exc:
        code, detail = None, type(exc.reason).__name__
        if "getaddrinfo" in str(exc.reason) or "Name or service not known" in str(exc.reason):
            detail = "hostname does not resolve from here"
    except (OSError, ValueError) as exc:
        code, detail = None, type(exc).__name__

    dom = chrome_dom(url)
    if dom:
        return LIVE, (dom if want_page else None), f"{detail} to urllib, rendered in browser"
    if code in DEAD_CODES:
        return DEAD, None, detail
    return BLOCKED, None, detail


def summarise(verdicts):
    """One line per field group: how much was confirmed live vs taken on the directory's word."""
    counts = {LIVE: 0, BLOCKED: 0, DEAD: 0}
    for verdict in verdicts:
        counts[verdict] = counts.get(verdict, 0) + 1
    return (f"{counts[LIVE]} confirmed live, {counts[BLOCKED]} published on the directory's "
            f"word (blocked to us), {counts[DEAD]} dropped as gone")
