#!/usr/bin/env python3
"""Timeline lint for storm-market hyperframes compositions (DESIGN.md: the only
deterministic gate; taste stays with the model).

Checks episodes/<slug>/index.html:
  1. every media src (video/img/audio/script) resolves to an existing file
  2. every data-start / data-start+data-duration window sits inside the composition duration
  3. audio elements: narration wavs must not overlap each other or any insert audio
  4. NO-REPEAT (owner, ep1 v2 RCA): a visual file may appear in ONE timed window only.
     Reuse requires data-callback="<reason>" on the element — max 3 total uses (owner 2026-07-28).
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
        # narration window must be at least as long as its wav (15 Sep 26: a retime moved starts, kept old lengths, cut six tails)
        if kind == "audio" and src and 'id="nx-' in ("<" + kind + attrs) and d is not None and (ep / src.group(1)).exists():
            import subprocess
            wav_d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                          str(ep / src.group(1))], capture_output=True, text=True).stdout or 0)
            if wav_d > d + 0.05:
                findings.append(f"narration window shorter than its wav: {src.group(1)} window {d}s, wav {wav_d:.2f}s (last words cut)")
        # b-roll is muted by default; a clip with its own sound declares data-has-audio (owner 15 Sep 26)
        if kind == "video" and 'data-track-index="1"' in attrs and "muted" not in attrs and "data-has-audio" not in attrs:
            findings.append(f"unmuted b-roll without data-has-audio: {src.group(1) if src else '?'}")

    audio_windows.sort()
    for (s1, e1, f1), (s2, e2, f2) in zip(audio_windows, audio_windows[1:]):
        if s2 < e1 - 0.05:
            findings.append(f"audio overlap: {f1} ({s1}-{e1:.1f}) vs {f2} ({s2}-{e2:.1f})")

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
