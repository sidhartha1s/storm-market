#!/usr/bin/env python3
"""Generate documentary-style AI b-roll stills via DeAPI (Z-Image-Turbo INT8).

  python3 scripts/gen_ai_stills.py [--dry-run] [--max-api-calls N] [--only id,id]

DeAPI txt2img/poll pattern: async submit ->
poll request-status -> download presigned result_url PNG. Prompts are hardcoded
below (STILLS list) — this is a one-off episode still-gen script, not a
per-episode-data engine.

Cost railguards (per CLAUDE.md):
- --max-api-calls hard cap (default 16), pre-incremented BEFORE each HTTP call.
- 1 retry max per image (2 attempts total).
- Running call count printed before every attempt.
- Crash-safe resume: skips an id whose PNG already exists (use --force to redo).
"""
import argparse
import json
import os
import random
import sys
import time
from pathlib import Path

import httpx
from dotenv import load_dotenv

REPO = Path(__file__).resolve().parent.parent
OUT_DIR = REPO / "episodes" / "ep2-2011-super-outbreak" / "media" / "ai"

DEAPI_BASE_URL = "https://api.deapi.ai/api/v1"
DEAPI_MODEL = "ZImageTurbo_INT8"
# 2048x1152 = 16:9, both divisible by 16 (Z-Image-Turbo step-16 grid); larger than
# the requested 1920x1080 floor per the brief ("1920x1080 or larger, 16:9").
DEAPI_IMAGE_WIDTH = 2048
DEAPI_IMAGE_HEIGHT = 1152
DEAPI_STEPS = 12
COST_PER_IMAGE_USD = 0.002
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"

STYLE = (
    ", documentary photograph, dark cinematic color grade, moody atmospheric "
    "storm light, photorealistic, sharp realistic detail, gentle film grain, "
    "no text, no captions, no logos, no watermark, 16:9 composition"
)
NEGATIVE = (
    "people, person, human, man, woman, child, face, silhouette of a person, crowd, "
    "text, caption, subtitle, watermark, logo, signature, readable sign lettering, "
    "garbled text, illegible writing, "
    "cartoon, anime, illustration, painting, digital art, cgi, 3d render, "
    "deformed, disfigured, blurry, low quality, extra limbs, "
    "tropical, palm trees, jungle, rainforest, smoke, wildfire"
)

STILLS = [
    ("ai-lake-martin-dusk",
     "lakeside wooden cabins on a dark Alabama lake at dusk, violent storm sky "
     "overhead, last grey-green light on the water, trees whipping, no people, "
     "cinematic documentary still"),
    ("ai-ms-farmland-wedge",
     "a massive dark wedge tornado over empty Mississippi farmland, late "
     "afternoon storm light, wide flat fields, distant funnel touching down"),
    ("ai-rural-road-storm",
     "an empty rural two-lane asphalt road in Alabama, violent green-black "
     "storm sky overhead, trees bending sideways in high wind, no vehicles"),
    ("ai-town-street-dark",
     "a small southern American town main street under a near-black storm "
     "sky, a traffic light swinging violently in the wind, empty brick "
     "storefronts with blank unlettered signage, no readable words anywhere"),
    ("ai-night-wedge-lightning",
     "an enormous tornado silhouette at night, illuminated by a bright "
     "lightning flash against black sky, dramatic scale, rain streaks"),
    ("ai-house-splinters-closeup",
     "extreme closeup of splintered house framing lumber and broken wood "
     "beams after a tornado, overcast daylight, debris texture, nails and "
     "shattered wood"),
    ("ai-field-scar-aerial",
     "aerial drone view of a long straight tornado damage swath of snapped "
     "and flattened trees cutting through temperate deciduous forest and "
     "green Midwest American farm fields, brown scar of splintered timber "
     "and debris, overcast daylight, flat American countryside, no smoke, "
     "no dirt road, no tropical or jungle vegetation"),
    ("ai-storm-horizon-dusk",
     "a massive supercell thunderstorm mothership cloud structure at dusk "
     "over flat plains, dramatic layered clouds, wide horizon, no tornado"),
    ("ai-radio-tower-storm",
     "a visibly damaged broadcast radio tower, its lattice mast bent sharply "
     "and buckled partway up, leaning at a broken angle against dark storm "
     "clouds, twisted collapsed metal struts, dramatic stormy sky"),
]


def read_keys() -> list[str]:
    load_dotenv(REPO / ".env")
    keys = [v.strip() for k, v in sorted(os.environ.items())
            if k.startswith("DEAPI_API_KEY") and v.strip()]
    seen, out = set(), []
    for k in keys:
        if k not in seen:
            seen.add(k); out.append(k)
    if not out:
        sys.exit("DEAPI_API_KEY not found in env or ./.env")
    return out


def _validate_png(data: bytes | None, source: str) -> bytes | None:
    if not data:
        return None
    if not data.startswith(PNG_MAGIC):
        print(f"    {source} returned non-PNG payload ({len(data)} bytes); discarding", file=sys.stderr)
        return None
    return data


def _download_result(url: str, source: str, attempts: int = 3) -> bytes | None:
    for _ in range(attempts):
        try:
            with httpx.Client(timeout=httpx.Timeout(60.0, connect=20.0), follow_redirects=True) as client:
                resp = client.get(url)
            if resp.status_code != 200:
                print(f"    {source}: download HTTP {resp.status_code}", file=sys.stderr)
                return None
            return _validate_png(resp.content, source)
        except httpx.HTTPError as e:
            last_err = e
            time.sleep(2)
    print(f"    {source}: download failed: {last_err}", file=sys.stderr)
    return None


def poll_job_result(request_id: str, api_key: str, max_wait: int = 180) -> bytes | None:
    headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}
    start_time = time.time()
    with httpx.Client(timeout=30) as client:
        while time.time() - start_time < max_wait:
            response = client.get(f"{DEAPI_BASE_URL}/client/request-status/{request_id}", headers=headers)
            if response.status_code != 200:
                print(f"Poll error {response.status_code}: {response.text[:200]}", file=sys.stderr)
                return None
            data = response.json().get("data") or {}
            status = data.get("status", "")
            if status == "done":
                result_url = data.get("result_url")
                if not result_url:
                    print(f"Job {request_id} done but no result_url", file=sys.stderr)
                    return None
                return _download_result(result_url, f"request {request_id}")
            if status == "error":
                print(f"Job {request_id} failed: {json.dumps(data)[:300]}", file=sys.stderr)
                return None
            print(f"  Job {request_id}: {status or 'unknown'}...")
            time.sleep(3)
    print(f"Job {request_id} timed out after {max_wait}s", file=sys.stderr)
    return None


def generate_image(prompt: str, api_key: str) -> bytes | None:
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    seed = random.randint(0, 2**32 - 1)
    payload = {
        "prompt": prompt + STYLE,
        "model": DEAPI_MODEL,
        "width": DEAPI_IMAGE_WIDTH,
        "height": DEAPI_IMAGE_HEIGHT,
        "seed": seed,
        "steps": DEAPI_STEPS,
        "negative_prompt": NEGATIVE,
    }
    print(f"    Seed: {seed}")
    try:
        with httpx.Client(timeout=120) as client:
            response = None
            for rl_wait in (0, 20, 45, 90):
                if rl_wait:
                    time.sleep(rl_wait)
                response = client.post(f"{DEAPI_BASE_URL}/client/txt2img", headers=headers, json=payload)
                if response.status_code != 429:
                    break
                print("  429 rate-limited; backing off before retry", file=sys.stderr)
            if response.status_code != 200:
                print(f"API error: {response.status_code} - {response.text}", file=sys.stderr)
                return None
            result = response.json()
            request_id = (result.get("data") or {}).get("request_id")
            if not request_id:
                print(f"txt2img: no request_id: {json.dumps(result)[:400]}", file=sys.stderr)
                return None
            return poll_job_result(request_id, api_key)
    except (httpx.HTTPError, ValueError) as e:
        print(f"Request error: {type(e).__name__}: {e}", file=sys.stderr)
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--max-api-calls", type=int, default=16)
    ap.add_argument("--only", help="comma-separated ids to limit to")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    stills = STILLS
    if args.only:
        keep = set(args.only.split(","))
        stills = [s for s in stills if s[0] in keep]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    todo = [(sid, p) for sid, p in stills if args.force or not (OUT_DIR / f"{sid}.png").exists()]

    print(f"Plan: {len(todo)} images @ ~${COST_PER_IMAGE_USD:.4f} = ~${len(todo)*COST_PER_IMAGE_USD:.4f}. "
          f"cap={args.max_api_calls} model={DEAPI_MODEL} {DEAPI_IMAGE_WIDTH}x{DEAPI_IMAGE_HEIGHT}")
    for sid, p in stills:
        if (sid, p) not in todo:
            print(f"  [skip] {sid} already generated (0 API)")
    if args.dry_run:
        for sid, p in todo:
            print(f"  DRY {sid}: {p[:90]}...")
        return

    keys = read_keys()
    key = keys[0]
    calls = 0
    ok = 0
    fail = 0
    for sid, prompt in todo:
        png = None
        for attempt in range(2):  # 1 try + 1 retry
            if calls >= args.max_api_calls:
                print(f"  [budget] skip {sid} (cap {args.max_api_calls} reached)", file=sys.stderr)
                break
            calls += 1
            print(f"[{calls}/{args.max_api_calls}] {sid} attempt{attempt+1} ...")
            png = generate_image(prompt, key)
            if png:
                break
            print(f"  attempt {attempt+1} failed for {sid}", file=sys.stderr)
            time.sleep(5)
        if not png:
            fail += 1
            print(f"  FAILED {sid}", file=sys.stderr)
            continue
        (OUT_DIR / f"{sid}.png").write_bytes(png)
        ok += 1
        print(f"  saved {sid}.png ({len(png)} bytes)")
        if calls >= args.max_api_calls:
            print("Budget cap reached; stopping.", file=sys.stderr)
            break

    print(f"stats: {ok} ok, {fail} failed, {calls} API calls")
    if fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
