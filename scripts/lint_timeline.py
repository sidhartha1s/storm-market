#!/usr/bin/env python3
"""Timeline lint for storm-market hyperframes compositions (DESIGN.md: the only
deterministic gate; taste stays with the model).

Checks episodes/<slug>/index.html:
  1. every media src (video/img/audio/script) resolves to an existing file
  2. every data-start / data-start+data-duration window sits inside the composition duration
  3. audio elements: narration wavs must not overlap each other or any insert audio
  4. NO-REPEAT (owner, ep1 v2 RCA): a visual file may appear in ONE timed window only.
     Reuse requires data-callback="<reason>" on the element — and even then max 2 total uses.
     Elements inside the last 90s (summary/outro zone) are exempt (owner: recap reuse is fine).
  5. CADENCE REPORT (owner 2026-07-23: pacing = AI judgment, NEVER code-enforced): shots over
     baseline (stills >7s, videos >12s) are PRINTED as a report for the editor-agent to reason
     over — they never fail the lint. Graphics sections (id containing -clip) exempt.

Usage: python3 scripts/lint_timeline.py episodes/<slug>
Exit 0 clean, 1 findings (loud).
"""
import re
import sys
from pathlib import Path


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

    for src in re.findall(r'<script[^>]*src="([^"]+)"', html):
        if not src.startswith("http") and not (ep / src).exists():
            findings.append(f"missing script: {src}")

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
        if len(timed) > 2:
            findings.append(f"repeat: {src} used {len(timed)}x — max 2 (one + one flagged callback)")
        elif len(timed) == 2 and not any(cb for _, _, cb in timed):
            findings.append(f"repeat: {src} used 2x with no data-callback=\"reason\" on the reuse")

    if findings:
        print("[lint_timeline] FAIL")
        for f in findings:
            print("  -", f)
        sys.exit(1)
    print(f"[lint_timeline] PASS — {len(tags)} media/script tags, comp {comp_dur}s, "
          f"{len(audio_windows)} timed voice/insert audio windows non-overlapping")


if __name__ == "__main__":
    main()
