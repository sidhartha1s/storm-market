#!/usr/bin/env python3
"""Timeline lint for storm-market hyperframes compositions (DESIGN.md: the only
deterministic gate; taste stays with the model).

Checks episodes/<slug>/index.html:
  1. every media src (video/img/audio/script) resolves to an existing file
  2. every data-start / data-start+data-duration window sits inside the composition duration
  3. audio elements: narration wavs must not overlap each other or any insert audio
     and no audio src may match a hash in assets/sfx/BANNED.md5 (owner-banned sounds)
  4. NO-REPEAT (owner, ep1 v2 RCA): a visual file may appear in ONE timed window only.
     Reuse requires data-callback="<reason>" on the element — max 3 total uses (owner 2026-07-28).
     Elements inside the last 90s (summary/outro zone) are exempt (owner: recap reuse is fine).
  5. CADENCE REPORT (owner 2026-07-23: pacing = AI judgment, NEVER code-enforced): shots over
     baseline (stills >7s, videos >12s) are PRINTED as a report for the editor-agent to reason
     over — they never fail the lint. Graphics sections (id containing -clip) exempt.

Usage: python3 scripts/lint_timeline.py episodes/<slug>
Exit 0 clean, 1 findings (loud).
"""
import hashlib
import re
import subprocess
import sys
from pathlib import Path

import yaml

# owner-banned audio by content hash (a rename cannot dodge it): "<md5>  <name>  <why>" per line
_banned = Path(__file__).resolve().parent.parent / "assets/sfx/BANNED.md5"
if not _banned.exists():
    sys.exit(f"[lint_timeline] FAIL: {_banned} is missing; the banned-audio check cannot run (restore it from git, never skip it)")
BANNED = {l.split()[0]: l.split()[1] for l in _banned.read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")}


def main():
    ep = Path(sys.argv[1])
    html = (ep / "index.html").read_text(encoding="utf-8")
    findings = []

    m = re.search(r'data-duration="([\d.]+)"', html)
    if not m:
        sys.exit("no composition data-duration found")
    comp_dur = float(m.group(1))

    tags = re.findall(r"<(video|img|audio|script)\b[^>]*>", html)
    elems = re.finditer(r'<(video|img|audio)\b([^>]*)>', html)
    audio_windows = []
    for e in elems:
        kind, attrs = e.group(1), e.group(2)
        src = re.search(r'src="([^"]+)"', attrs)
        if src and not src.group(1).startswith(("http", "data:")):
            if not (ep / src.group(1)).exists():
                findings.append(f"missing file: {src.group(1)}")
            elif kind == "audio" and hashlib.md5((ep / src.group(1)).read_bytes()).hexdigest() in BANNED:
                findings.append(f"BANNED audio (assets/sfx/BANNED.md5): {src.group(1)} = {BANNED[hashlib.md5((ep / src.group(1)).read_bytes()).hexdigest()]}")
        start = re.search(r'data-start="([\d.]+)"', attrs)
        dur = re.search(r'data-duration="([\d.]+)"', attrs)
        s = float(start.group(1)) if start else 0.0
        d = float(dur.group(1)) if dur else None
        if s > comp_dur:
            findings.append(f"{kind} {src.group(1) if src else '?'} starts at {s}s > comp {comp_dur}s")
        if d is not None and s + d > comp_dur + 0.05:
            findings.append(f"{kind} {src.group(1) if src else '?'} window {s}+{d} exceeds comp {comp_dur}s")
        if kind == "audio" and "data-bed" not in attrs:  # music bed may span everything
            audio_windows.append((s, s + (d if d is not None else comp_dur - s),
                                  src.group(1) if src else "?"))

    audio_windows.sort()
    for (s1, e1, f1), (s2, e2, f2) in zip(audio_windows, audio_windows[1:]):
        if s2 < e1 - 0.05:
            findings.append(f"audio overlap: {f1} ({s1}-{e1:.1f}) vs {f2} ({s2}-{e2:.1f})")

    # NARRATION SEAMS (owner 17 Sep 26, Dujuan U1 review: "awkward gaps ... not intentional"). Voice
    # segments may be apart by at most the blackout length; the sanctioned holes are the CTA, a chapter
    # blackout, and a declared hold (<section class="clip hold" data-start data-duration>, DESIGN.md).
    cta_starts = [float(x) for x in re.findall(r'<video\b[^>]*src="[^"]*cta/[^"]*"[^>]*data-start="([\d.]+)"', html)]
    voice = sorted((s, s + d) for s, d in ((float(a), float(b)) for a, b in
                   re.findall(r'<audio\b[^>]*id="nx-(?!ins)[^"]*"[^>]*data-start="([\d.]+)"[^>]*data-duration="([\d.]+)"', html)))
    structure = [(float(a), float(a) + float(b)) for a, b in re.findall(
        r'<section\b[^>]*class="[^"]*\b(?:blackout|hold)\b[^"]*"[^>]*data-start="([\d.]+)"[^>]*data-duration="([\d.]+)"', html)]
    for (s1, e1), (s2, e2) in zip(voice, voice[1:]):
        gap = s2 - e1
        if gap > 0.8 and not any(e1 - 0.5 <= c <= s2 for c in cta_starts) \
                and not any(bs < s2 and be > e1 for bs, be in structure):
            findings.append(f"narration gap {gap:.1f}s at {e1:.1f}-{s2:.1f}s (max 0.8s outside the CTA)")

    for src in re.findall(r'<script[^>]*src="([^"]+)"', html):
        if not src.startswith("http") and not (ep / src).exists():
            findings.append(f"missing script: {src}")

    # PICTURE COVERAGE (owner 2026-07-29, owed to main): the v3 draft rendered black at
    # segment seams — instants where the picture tracks (1 = base visuals, 2 = graphics)
    # covered nothing. This is a DETERMINISTIC coverage check on the assembled timeline, not
    # a pixel blackdetect: a pixel scan false-positives on dark graphics in motion (three of
    # v3's flagged spans were exactly that), while a coverage gap is a real hole that always
    # renders black. Every instant in (0, comp_dur) must sit inside at least one picture window.
    pic = []
    for e in re.finditer(r'<(video|section|div)\b([^>]*)>', html):
        a = e.group(2)
        tr = re.search(r'data-track-index="(\d+)"', a)
        st = re.search(r'data-start="([\d.]+)"', a)
        du = re.search(r'data-duration="([\d.]+)"', a)
        if tr and st and du and tr.group(1) in ("1", "2"):
            s = float(st.group(1))
            pic.append((s, s + float(du.group(1))))
    pic.sort()
    if pic:
        cursor = 0.0
        for s, e in pic:
            if s > cursor + 0.03:                 # a hole before this window opens
                findings.append(f"picture gap: nothing on tracks 1/2 from {cursor:.2f}s to {s:.2f}s "
                                f"({s - cursor:.2f}s of black)")
            cursor = max(cursor, e)
        if cursor < comp_dur - 0.03:
            findings.append(f"picture gap: nothing on tracks 1/2 from {cursor:.2f}s to end "
                            f"{comp_dur:.2f}s ({comp_dur - cursor:.2f}s of black)")

    # 4+5: no-repeat + cadence on VISUAL windows.
    # Collect (src, start, dur, has_callback, has_holdok) for videos and timed <section><img>.
    visuals = []
    for e in re.finditer(r'<video\b([^>]*)>', html):
        a = e.group(1)
        src = re.search(r'src="([^"]+)"', a)
        st = re.search(r'data-start="([\d.]+)"', a)
        du = re.search(r'data-duration="([\d.]+)"', a)
        if src and st:
            visuals.append((src.group(1), float(st.group(1)),
                            float(du.group(1)) if du else 0.0,
                            "data-callback" in a, "data-hold-ok" in a))
    for e in re.finditer(r'<section\b([^>]*?)>((?:(?!</section>).)*?)</section>', html, re.S):
        a, body = e.group(1), e.group(2)
        st = re.search(r'data-start="([\d.]+)"', a)
        du = re.search(r'data-duration="([\d.]+)"', a)
        img = re.search(r'<img[^>]*src="([^"]+)"', body)
        secid = re.search(r'id="([^"]+)"', a)
        graphic = bool(secid and "-clip" in secid.group(1))
        if st and img:
            visuals.append((img.group(1), float(st.group(1)),
                            float(du.group(1)) if du else 0.0,
                            "data-callback" in a or "data-callback" in body,
                            "data-hold-ok" in a or graphic))
    summary_zone = comp_dur - 90
    by_src = {}
    reports = []
    for src, st, du, cb, hk in visuals:
        by_src.setdefault(src, []).append((st, du, cb))
        is_still = not src.endswith((".mp4", ".webm", ".mov"))
        limit = 7 if is_still else 12
        if du > limit and not hk and st < summary_zone:
            reports.append(f"[pacing report] {'still' if is_still else 'video'} {src} holds {du:.1f}s at {st:.0f}s (baseline {limit}s) — editor: reason about it")
    for src, uses in by_src.items():
        timed = [(st, du, cb) for st, du, cb in uses if st < summary_zone]
        # owner rule 2026-07-28: an image may return up to 3x if each return is justified
        if len(timed) > 3:
            findings.append(f"repeat: {src} used {len(timed)}x — max 3, each reuse data-callback'd")
        elif len(timed) == 3 and sum(1 for _, _, cb in timed if cb) < 2:
            findings.append(f"repeat: {src} used 3x but only {sum(1 for _, _, cb in timed if cb)} reuse(s) carry data-callback")
        elif len(timed) == 2 and not any(cb for _, _, cb in timed):
            findings.append(f"repeat: {src} used 2x with no data-callback=\"reason\" on the reuse")

    for r in reports:
        print(" ", r)
    if findings:
        print("[lint_timeline] FAIL")
        for f in findings:
            print("  -", f)
        sys.exit(1)
    print(f"[lint_timeline] PASS — {len(tags)} media/script tags, comp {comp_dur}s, "
          f"{len(audio_windows)} timed voice/insert audio windows non-overlapping")


if __name__ == "__main__":
    main()
