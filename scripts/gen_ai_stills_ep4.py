#!/usr/bin/env python3
"""Generate documentary-style AI gap-fill stills via DeAPI (Z-Image-Turbo INT8)
for episodes/ep4-el-reno. 2 variants per subject; pick best in media/ai, note
provenance for kept files.

  python3 scripts/gen_ai_stills_ep4.py [--dry-run] [--max-api-calls N] [--only id,id]

Same DeAPI txt2img/poll pattern as gen_ai_stills_ep3.py.

Cost railguards (per CLAUDE.md):
- --max-api-calls hard cap (default 14), pre-incremented BEFORE each HTTP call.
- 1 retry max per image (2 attempts total).
- Stop on 3 consecutive failures.
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
OUT_DIR = REPO / "episodes" / "ep4-el-reno" / "media" / "ai"
ENV_PATH = Path("C:/Users/Sidhartha/Automation Projects/storm-market/.env")

DEAPI_BASE_URL = "https://api.deapi.ai/api/v1"
DEAPI_MODEL = "ZImageTurbo_INT8"
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

SUBJECTS = [
    ("rain-wrapped-tornado",
     "a massive rain-wrapped tornado, dark gray-green wall of rain over two miles "
     "wide over flat Oklahoma farmland, evening storm light, a wedge barely "
     "discernible inside the rain curtains, telephone poles in the foreground for scale"),
    ("multi-vortex-tornado",
     "a multi-vortex tornado, several thin violent subvortex funnels snaking beneath "
     "an enormous low black cloud base over open green fields"),
    ("night-city-flooding",
     "night city street flooding, rising black water at a highway underpass, heavy "
     "rain streaks lit by headlight beams, an abandoned car silhouette, no people"),
    ("rural-section-road",
     "an empty rural section road in storm light, wet gravel road running toward a "
     "darkening horizon, wheat fields on either side, distant lightning, ominous "
     "green-gray sky"),
    ("supercell-structure",
     "a wide shot of a sculpted rotating supercell storm structure over open plains "
     "at dusk"),
]


def read_keys() -> list[str]:
    load_dotenv(ENV_PATH)
    keys = [v.strip() for k, v in sorted(os.environ.items())
            if k.startswith("DEAPI_API_KEY") and v.strip()]
    seen, out = set(), []
    for k in keys:
        if k not in seen:
            seen.add(k); out.append(k)
    if not out:
        sys.exit(f"DEAPI_API_KEY not found in {ENV_PATH}")
    return out


def _validate_png(data: bytes | None, source: str) -> bytes | None:
    if not data:
        return None
    if not data.startswith(PNG_MAGIC):
        print(f"    {source} returned non-PNG payload ({len(data)} bytes); discarding", file=sys.stderr)
        return None
    return data


def _download_result(url: str, source: str, attempts: int = 3) -> bytes | None:
    last_err = None
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
    ap.add_argument("--max-api-calls", type=int, default=14)
    ap.add_argument("--only", help="comma-separated subject ids to limit to")
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    subjects = SUBJECTS
    if args.only:
        keep = set(args.only.split(","))
        subjects = [s for s in subjects if s[0] in keep]

    # 2 variants per subject
    stills = [(f"ai-{sid}-v{n}", prompt) for sid, prompt in subjects for n in (1, 2)]

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
    consecutive_fail = 0
    for sid, prompt in todo:
        if consecutive_fail >= 3:
            print("3 consecutive failures; stopping.", file=sys.stderr)
            break
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
            consecutive_fail += 1
            print(f"  FAILED {sid}", file=sys.stderr)
            continue
        consecutive_fail = 0
        (OUT_DIR / f"{sid}.png").write_bytes(png)
        ok += 1
        print(f"  saved {sid}.png ({len(png)} bytes)")
        if calls >= args.max_api_calls:
            print("Budget cap reached; stopping.", file=sys.stderr)
            break

    print(f"stats: {ok} ok, {fail} failed, {calls} API calls")


if __name__ == "__main__":
    main()
