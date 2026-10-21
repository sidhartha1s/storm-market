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
  6. PRESENTER CIRCLE (owner 2026-10-19, Joplin): a <video class="pip"> window holding more than
     4.0 s with no voice (narration or a voiced clip) FAILs: Paul's face sits frozen in silence.
  7. OUTSIDE VOICES (owner 2026-10-20): in an epN documentary every audible non-narrator element
     (radio, 911, broadcast sound) has a data-caption-for host covering its whole window, or
     data-caption-ok="reason" when it has no words. config.yaml channel.voice_captions.exempt lists shipped episodes.
  8. DEAD AIR (owner 2026-10-21): inside a blackout or declared hold of an epN documentary, at most MAX_QUIET (4 s)
     may pass with no narration, Paul line or audible outside sound (check 7's test, words or not); a bed alone
     does not count. Same exempt list.

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
MAX_QUIET = 4.0  # longest stretch with no voice of any kind inside a blackout or hold (DESIGN.md "hold", owner 21 Oct 26)


def _num(tag, attr):
    m = re.search(rf'{attr}="([\d.]+)"', tag)
    return float(m.group(1)) if m else None


def outside_voice(tag):
    """(id, start, end) when an <audio>/<video> tag plays audible sound other than the narrator, Paul, the CTA or a bed;
    else None. The one test for checks 7 and 8."""
    idm = re.search(r'\sid="([^"]+)"', tag)   # \s: hyperframes stamps data-hf-id="hf-..." before the real id
    vid = idm.group(1) if idm else ""
    s, d = _num(tag, "data-start"), _num(tag, "data-duration")
    # narration is nx- but not nx-ins (circle_audio.py, build_srt.py, sweep_episode.py); every sx- bed carries data-bed
    if (re.match(r"nx-(?!ins)", vid) or vid.startswith(("ins-paul", "ins-cta")) or "data-bed" in tag
            or re.search(r'src="[^"]*cta/', tag) or s is None or d is None):
        return None
    # audible as audio_levels.py reads it: data-volume defaults to 1.0; a video is silent only when muted
    vol = _num(tag, "data-volume")
    if (vol is not None and vol <= 0) or (tag.startswith("<video") and re.search(r"\smuted(?=[\s>/=]|$)", tag)):
        return None
    return vid, s, s + d


def longest_gap(spans, ws, we):
    """(length, start) of the longest stretch of [ws, we] that no span in the sorted list covers."""
    cursor, longest = ws, (0.0, ws)
    for vs, ve in spans:
        if ve <= cursor or vs >= we:
            continue
        if vs - cursor > longest[0]:
            longest = (vs - cursor, cursor)
        cursor = max(cursor, ve)
    if we - cursor > longest[0]:
        longest = (we - cursor, cursor)
    return longest


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
        # narration window must be at least as long as its wav (FORMAT.md:59, day-1 bug 15 Sep
        # 26: a retime moved narration starts and kept the old data-duration, cutting the last
        # words of six segments — the render shipped clean-looking and silently truncated).
        if kind == "audio" and src and re.search(r'\sid="nx-', attrs) and d is not None and (ep / src.group(1)).exists():
            wav_d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", str(ep / src.group(1))],
                                         capture_output=True, text=True).stdout.strip() or 0)
            if wav_d > d + 0.05:
                findings.append(f"narration window shorter than its wav: {src.group(1)} window {d}s, wav {wav_d:.2f}s (last words cut)")
        # b-roll is muted by default; a clip with its own sound declares data-has-audio
        # (FORMAT.md:57, owner 15 Sep 26: a stranded-passenger interview played under Paul and
        # a quote card with neither muted nor data-has-audio set).
        if kind == "video" and 'data-track-index="1"' in attrs and "muted" not in attrs and "data-has-audio" not in attrs:
            findings.append(f"unmuted b-roll without data-has-audio: {src.group(1) if src else '?'}")

    audio_windows.sort()
    for (s1, e1, f1), (s2, e2, f2) in zip(audio_windows, audio_windows[1:]):
        if s2 < e1 - 0.05:
            findings.append(f"audio overlap: {f1} ({s1}-{e1:.1f}) vs {f2} ({s2}-{e2:.1f})")

    # NARRATION SEAMS (owner 17 Sep 26, Dujuan U1 review: "awkward gaps ... not intentional"). Voice
    # segments may be apart by at most the blackout length; the sanctioned holes are the CTA, a chapter
    # blackout, and a declared hold (<section class="clip hold" data-start data-duration>, DESIGN.md).
    cta_wins = []
    for cm in re.finditer(r'<video\b[^>]*src="[^"]*cta/[^"]*"[^>]*>', html):
        a = cm.group(0)
        cs, cd = re.search(r'data-start="([\d.]+)"', a), re.search(r'data-duration="([\d.]+)"', a)
        if cs and cd:
            cta_wins.append((float(cs.group(1)), float(cs.group(1)) + float(cd.group(1))))
    cta_starts = [s for s, _ in cta_wins]
    # sanctioned CTA gap is bounded by config.yaml channel.cta.dip_in/dip_out (config.yaml:40-41,
    # DESIGN.md "CTA contract"), not open-ended — a 4s black-plus-silence stretch used to pass
    # every gate as long as SOME CTA start fell in the window (docs-drift-cta-gap-unbounded).
    _cfg = yaml.safe_load((Path(__file__).resolve().parent.parent / "config.yaml").read_text(encoding="utf-8"))
    _cta_cfg = ((_cfg.get("channel") or {}).get("cta")) or {}
    dip_in = float(_cta_cfg.get("dip_in", 0.8))
    dip_out = float(_cta_cfg.get("dip_out", 0.8))
    # Voice is the narrator's segments plus Paul's own on-camera lines (<video id="ins-paul-N" data-volume="1">,
    # mg-quickref "Paul on screen", owner 7 Oct 26): a line he speaks on camera is not a hole in the narration.
    # A silent ins-paul- clip is not voice (same data-volume test as build_srt.py and sweep_episode.py).
    paul_lines = [m.groups() for m in re.finditer(
        r'<video\b[^>]*id="ins-paul-[^"]*"[^>]*data-start="([\d.]+)"[^>]*data-duration="([\d.]+)"[^>]*>', html)
        if re.search(r'data-volume="1(?:\.0+)?"', m.group(0))]
    voice = sorted((s, s + d) for s, d in ((float(a), float(b)) for a, b in paul_lines +
                   re.findall(r'<audio\b[^>]*id="nx-(?!ins)[^"]*"[^>]*data-start="([\d.]+)"[^>]*data-duration="([\d.]+)"', html)))
    structure = [(float(a), float(a) + float(b)) for a, b in re.findall(
        r'<section\b[^>]*class="[^"]*\b(?:blackout|hold)\b[^"]*"[^>]*data-start="([\d.]+)"[^>]*data-duration="([\d.]+)"', html)]

    # OUTSIDE VOICES and DEAD AIR: checks 7 and 8 in the docstring, epN documentaries not yet shipped.
    slug = ep.resolve().name
    voice_rules = bool(re.match(r"ep\d*-", slug)) and slug not in (
        ((_cfg.get("channel") or {}).get("voice_captions") or {}).get("exempt") or [])
    live = re.sub(r"<!--.*?-->", "", html, flags=re.S)   # a commented-out tag is not mounted
    sounds = [(m.group(0), outside_voice(m.group(0))) for m in re.finditer(r"<(?:audio|video)\b[^>]*>", live)]
    outside = sorted((s, e) for _, v in sounds if v for _, s, e in [v])
    if voice_rules:
        caps = [(m.group(1), _num(m.group(0), "data-start"), _num(m.group(0), "data-duration"))
                for m in re.finditer(r'<[a-z]+\b[^>]*\bdata-caption-for="([^"]+)"[^>]*>', live)]
        for tag, v in sounds:
            if not v or "data-caption-ok=" in tag:
                continue
            vid, s, e = v
            if not any(c == vid and cs is not None and cd is not None and cs <= s + 0.05 and cs + cd >= e - 0.05
                       for c, cs, cd in caps):
                findings.append(f"outside voice without a caption over its whole window: {vid or tag[:80]} ({s:.2f}-{e:.2f}s); "
                                f"mount a host with data-caption-for=\"{vid}\" from its first to its last frame "
                                f"(mg-quickref \"Outside voices\"), or data-caption-ok=\"reason\" when it has no words")

    for (s1, e1), (s2, e2) in zip(voice, voice[1:]):
        gap = s2 - e1
        if gap <= 0.8:
            continue
        cta = next((w for w in cta_wins if e1 - 0.5 <= w[0] <= s2), None)
        if cta:
            cs2, ce2 = cta
            if cs2 - e1 > dip_in + 0.1:
                findings.append(f"CTA dip-in {cs2 - e1:.1f}s at {e1:.1f}-{cs2:.1f}s exceeds config dip_in {dip_in}s")
            if s2 - ce2 > dip_out + 0.1:
                findings.append(f"CTA dip-out {s2 - ce2:.1f}s at {ce2:.1f}-{s2:.1f}s exceeds config dip_out {dip_out}s")
            continue
        if any(bs < s2 and be > e1 for bs, be in structure):
            continue
        findings.append(f"narration gap {gap:.1f}s at {e1:.1f}-{s2:.1f}s (max 0.8s outside the CTA)")

    # The presenter circle is Paul's face speaking the narration: with no voice under it the face sits still
    # (owner 19 Oct 26, Joplin draft: "its on mute, paul is frozen"; pip-w16 ran 12.8 s past its last line).
    for m in re.finditer(r'<video\b[^>]*class="[^"]*\bpip\b[^"]*"[^>]*>', html):
        st, du = re.search(r'data-start="([\d.]+)"', m.group(0)), re.search(r'data-duration="([\d.]+)"', m.group(0))
        if not (st and du):
            continue
        ws, we = float(st.group(1)), float(st.group(1)) + float(du.group(1))
        cursor, longest = ws, (0.0, ws)
        for vs, ve in voice:
            if ve <= cursor or vs >= we:
                continue
            if vs - cursor > longest[0]:
                longest = (vs - cursor, cursor)
            cursor = max(cursor, ve)
        if we - cursor > longest[0]:
            longest = (we - cursor, cursor)
        if longest[0] > 4.0:
            findings.append(f"presenter circle on with no voice for {longest[0]:.1f}s from {longest[1]:.1f}s "
                            f"(max 4.0s): end the pip window with the line")

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
        cls = re.search(r'class="([^"]*)"', a)
        if cls and "pip" in cls.group(1).split():
            continue  # the presenter circle is not a picture cut: cadence and no-repeat do not apply to it
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
