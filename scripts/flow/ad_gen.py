# Multi-shot Flow agent driver for the book ad, ONE browser window for every shot (owner: no window churn).
# usage: ad_gen.py <jobs.json>
# jobs.json: {"aspect": "16:9", "count": 2, "credits_per_video": 15, "budget": 120,
#             "jobs": [{"name": "s1", "frame": "C:/.../key1.png", "ingredients": ["C:/.../paul-style-sheet.png", ...], "prompt": "..."}]}
# Railguard: a shot is approved only when Flow's own confirmation quotes exactly count*credits_per_video credits
# and the running total stays within budget; anything else is rejected-by-silence (left unapproved) and logged.
import json, os, re, sys, time
from playwright.sync_api import sync_playwright

D = os.path.dirname(os.path.abspath(__file__))
PROFILE = r"C:\Users\Sidhartha\AppData\Local\ffroliva\gflow-cli\profile_sidclashes2much"
PROJECT = "https://flow.google.com/project/d8c62548-9b03-4a66-a99b-cfff268d9996"
CFG = json.load(open(sys.argv[1], encoding="utf8"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jobcheck import errors as _job_errors, ram_refusal, assert_responsive
if _job_errors(CFG):
    sys.exit("refused, nothing spent:\n" + "\n".join(_job_errors(CFG)))
if ram_refusal():
    sys.exit(ram_refusal())
OUT = os.path.dirname(os.path.abspath(sys.argv[1]))


def log(*a):
    line = " ".join(str(x) for x in a)
    print(line, flush=True)
    open(os.path.join(D, "log.txt"), "a", encoding="utf8").write(line + "\n")


def shot(page, name):
    # Evidence only, never a gate: the spend decision reads the quote from the page text. Chrome stops painting a
    # covered window, and page.screenshot then hung 30 s and aborted a run after its prompt was sent (12 Oct 26).
    try:
        page.screenshot(path=os.path.join(OUT, f"drv-{name}.png"), timeout=8000)
    except Exception as e:
        log("screenshot skipped", name, repr(e)[:80])


def set_defaults(page, aspect, count, model=None):
    page.locator('button[aria-label="Settings"]').last.click()
    page.wait_for_timeout(2000)
    page.get_by_text(aspect, exact=True).last.click()
    page.get_by_text(f"x{count}", exact=True).last.click()
    page.wait_for_timeout(500)
    if model:
        page.locator('[aria-label="Video generation default model"]').first.click()
        page.wait_for_timeout(1500)
        page.locator(f'[role=option]:has-text("{model}"), [role=menuitem]:has-text("{model}"), [role=menuitemradio]:has-text("{model}")').first.click()
        page.wait_for_timeout(1000)
        shown = page.locator('[aria-label="Video generation default model"]').first.inner_text()
        if model not in shown:  # never generate on a model the run did not ask for
            raise RuntimeError(f"model pick failed: wanted {model!r}, Settings shows {shown!r}; nothing spent")
        log("model set", shown.strip())
    page.get_by_role("button", name="Save").click()
    page.wait_for_timeout(1500)


def add_ingredient(page, path):
    page.locator('button[aria-label="Add ingredients to the prompt box"]').click()
    page.wait_for_timeout(2500)
    name = os.path.basename(path)
    if not page.locator(f'text="{name}" >> visible=true').count():
        with page.expect_file_chooser() as fc:
            page.get_by_role("button", name="Upload media").click()
        fc.value.set_files(path)
        page.locator(f'text="{name}" >> visible=true').last.wait_for(timeout=90000)  # upload lands in the list when processed
        page.wait_for_timeout(2000)
    page.locator(f'text="{name}" >> visible=true').last.click()
    page.wait_for_timeout(1000)
    add = page.get_by_role("button", name="Add to prompt")
    if add.count() and add.is_visible():
        add.click()
    page.wait_for_timeout(3000)


def enabled_approves(page):
    # used chips stay in the chat with a disabled class; stale unanswered requests stay enabled, so callers
    # compare against the count taken before their own send and only ever click a chip that appeared after it
    chips = page.locator('text="Approve" >> visible=true')
    return [chips.nth(i) for i in range(chips.count()) if "disabled" not in (chips.nth(i).get_attribute("class") or "")]


def video_tiles(page):
    # [x, y, clip id] per clip tile in the Videos grid, newest first (new clips land on top). Never count tiles: the
    # grid keeps only about 8 in the DOM and a failed card takes a slot (9 Oct 26: a landed clip sat at "tiles 9
    # target 10"). Never compare whole addresses: Flow swaps a tile's thumbnail from .../image/<id> to .../video/<id>
    # (same day: an old clip was taken for a new one). The id inside the address is what stays.
    # width > 300 drops the chat thumbnails.
    vids = page.get_by_text("Videos", exact=True).first
    box = vids.bounding_box() if vids.is_visible() else None
    if box and box["x"] >= 0:  # the nav rail collapses when the agent panel widens; the Videos filter stays applied
        vids.click()
        page.wait_for_timeout(3000)
    raw = page.evaluate("""() => [...document.querySelectorAll('img,video')].map(e => { const r = e.getBoundingClientRect();
        return [Math.round(r.left + r.width / 2), Math.round(r.top + r.height / 2), (e.currentSrc || e.src || '').split('?')[0], r.left, r.right, r.width]; })""")
    return grid_tiles(raw)


def grid_tiles(raw):
    # [x, y, clip id] of the Videos-grid tiles, newest first, from every <img>/<video> rect [cx, cy, src, left, right, width].
    # Keep tiles that start on screen, end before the agent panel (left 1330+ on the 1920 px driver window) and are wider
    # than a chat thumbnail. Row-major sort: on a wide window the grid is 2 columns and "newest first" runs across each
    # row; a right edge < 1080 dropped column 2 and hid a landed clip's anchor for 2 h (23 Oct 26).
    tiles = sorted((t for t in raw if t[3] >= 0 and t[4] < 1320 and t[5] > 300), key=lambda t: (t[1], t[0]))
    return [[x, y, (re.search(r"[0-9a-f]{8}-[0-9a-f-]{27}", src) or re.search(r"[^/]+$", src)).group(0)] for x, y, src, *_ in tiles]


def to_grid(page):
    # The project grid, where tiles are read. Clicking a tile now opens the clip in the scene editor
    # (<project>/edit/<id>), which Escape does not leave; every later job then read 0 tiles (23 Oct 26, 10 jobs in a row).
    if not page.url.startswith(PROJECT) or "/edit/" in page.url:
        page.goto(PROJECT, wait_until="domcontentloaded")
        page.wait_for_timeout(10000)


def clips_above(tiles, anchor):
    # the tiles above the anchor clip (the top clip before the send) are the new ones; none when the anchor is out of view
    ids = [t[2] for t in tiles]
    return tiles[:ids.index(anchor)] if anchor in ids else []


def verdict(path):
    from jobcheck import clip_verdict
    return clip_verdict(path, CFG, sys.argv[1])


def quoted_price(quote, expect):
    # the exact price only: "130 credits?" must not pass for 30 (review of PR 213, 23 Oct 26)
    return re.search(rf"(?<![\d.,]){expect} credits\b", quote) is not None


def main_checkout():
    # The lock and the STOP file live in the MAIN checkout's scripts/flow: every worktree drives the same Chrome on
    # port 9333, so a per-checkout lock let two drivers share one tab. A worktree's .git is a file "gitdir: <main>/.git/worktrees/<name>".
    root = os.path.dirname(os.path.dirname(D))
    dotgit = os.path.join(root, ".git")
    if os.path.isfile(dotgit):
        gitdir = open(dotgit).read().split(":", 1)[1].strip()
        root = os.path.dirname(os.path.dirname(os.path.dirname(gitdir)))
    return root


RUN = os.path.join(main_checkout(), "scripts", "flow")
os.makedirs(RUN, exist_ok=True)
STOP = os.path.join(RUN, "STOP")
DONE = os.path.join(OUT, "approved.done")  # crash-safe resume: a rerun of the same jobs.json skips these job names


def take_lock():
    # One driver on the Flow tab at a time. 9 Oct 26: two drivers stopped with TaskStop lived on (only their shell
    # died), woke when the next clip landed and overwrote a finished clip with an empty file.
    import subprocess
    lock = os.path.join(RUN, "driver.lock")
    if os.path.exists(lock):
        pid = open(lock).read().strip()
        if pid and f'"{pid}"' in subprocess.run(["tasklist", "/FI", f"PID eq {pid}", "/FO", "CSV", "/NH"], capture_output=True, text=True).stdout:
            sys.exit(f"another Flow driver is running (pid {pid}); not starting, nothing spent")
    open(lock, "w").write(str(os.getpid()))
    return lock


def failed_cards(page):
    # a refused or errored generation shows a "Failed" card (grid and chat) and never becomes a tile; Flow refunds it
    return [l.strip() for l in page.evaluate("() => document.body.innerText").splitlines()].count("Failed")


LOCK = take_lock()
with sync_playwright() as p:
    # attach to the ONE long-lived Flow Chrome (port 9333) and reuse its tab: every fresh launch or new tab of this
    # profile came up on Flow's public page (5 Oct 26), so the browser is never launched or closed from here
    # Is the port alive? Ask over plain HTTP first. A 3 s CDP attach timed out on a loaded laptop (12 Oct 26, 2 GB free)
    # while Chrome was up, and the except branch then launched a second window on the same profile.
    import urllib.request
    def port_alive():
        try:
            return urllib.request.urlopen("http://127.0.0.1:9333/json/version", timeout=10).status == 200
        except Exception:
            return False
    if port_alive():
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9333", timeout=60000)
    else:
        # No Flow Chrome is running: start it ONCE, detached, and leave it running for every later run. Never closed from here.
        import subprocess
        log("no Flow Chrome on port 9333: starting it once, it stays open")
        subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe", f"--user-data-dir={PROFILE}", "--remote-debugging-port=9333",
                          "--no-first-run", "--no-default-browser-check", PROJECT],
                         creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP)
        time.sleep(12)
        browser = p.chromium.connect_over_cdp("http://127.0.0.1:9333")
    ctx = browser.contexts[0]
    page = next((pg for pg in ctx.pages if "flow.google.com" in pg.url), None) or ctx.pages[0]
    # never page.bring_to_front(): it pulled the Flow window over the owner's work on every job (owner 23 Oct 26,
    # "disable tab focussing for chrome"). Screenshots are evidence only and may skip on an unpainted background tab.
    assert_responsive(page, 60000)
    spent = 0
    approved = 0
    try:
        to_grid(page)
        enter = page.get_by_text("Create with Google Flow", exact=True)
        if enter.count() and enter.first.is_visible():  # public page: enter the app in this same tab, as the owner does
            log("public page: entering Flow")
            enter.first.click()
            page.wait_for_url(lambda u: "/about" not in u, timeout=60000)
            page.wait_for_timeout(8000)
            if not page.url.startswith(PROJECT):
                page.goto(PROJECT, wait_until="domcontentloaded")
                page.wait_for_timeout(10000)
        # a "what's new" dialog covers the editor after a sign-in. exact=True: on an empty session the chat panel offers a
        # "How do I get started?" card, and a substring match clicked it and sent that question to the agent (12 Oct 26)
        news = page.get_by_role("button", name="Get started", exact=True)
        if news.count() and news.first.is_visible():
            log("dismissing the what's-new dialog")
            news.first.click()
            page.wait_for_timeout(3000)
        shot(page, "entry")
        if not page.locator('button[aria-label="Start generation"]').count():
            raise RuntimeError(f"not in the Flow editor ({page.url}); nothing spent")
        # no send, no spend: `--download-top N` fetches the top N clips now; `--after <clip id>` waits for one clip to
        # land above that clip (a shot approved by an earlier run), then fetches it
        mode = sys.argv[2] if len(sys.argv) > 3 else ""
        TOP = int(sys.argv[3]) if mode == "--download-top" else 0
        anchor = sys.argv[3] if mode == "--after" else video_tiles(page)[0][2]
        log("top clip before", anchor, "mode", mode or "send")
        fails_before = failed_cards(page)
        expect = CFG["count"] * CFG["credits_per_video"]
        done = set(open(DONE, encoding="utf8").read().split()) if os.path.exists(DONE) else set()
        todo = [j for j in CFG["jobs"] if j["name"] not in done] if not mode else []
        log(f"plan: {len(todo)} jobs x {expect} credits = {len(todo) * expect}, budget {CFG['budget']}, already approved {sorted(done)}")
        refused = 0
        for job in todo:
            if os.path.exists(STOP):  # kill switch: `touch STOP` (main checkout scripts/flow) halts before the next spend
                log("STOP file, halting before", job["name"], "spent", spent)
                break
            if spent + expect > CFG["budget"]:
                log("budget stop before", job["name"], "spent", spent)
                break
            # a fresh agent session per job: the old thread carried a refused shot's line into the next take (20 Oct 26)
            page.keyboard.press("Escape")  # a clip preview overlay blocks the panel
            page.wait_for_timeout(1000)
            page.locator('button[aria-label="Start new session"]').click(timeout=15000)
            page.wait_for_timeout(3000)
            clear = page.locator('button[aria-label="Clear prompt"]')
            if clear.count():  # the input keeps the last job's attachments across sessions
                clear.first.click()
                page.wait_for_timeout(1000)
            # the model is always set: Flow keeps the last pick as its default, and a Veo test left it on Veo 3.1 Lite,
            # so the next Omni job was quoted 10 credits and refused by the price check (23 Oct 26, Moore retake 3)
            set_defaults(page, CFG["aspect"], CFG["count"], CFG.get("model", "Omni 1.1 Flash"))
            shot(page, f"{job['name']}-newsession")
            for ing in [job["frame"]] + job.get("ingredients", []):
                add_ingredient(page, ing)
            n_before = len(enabled_approves(page))
            box = page.locator("textarea:visible, [contenteditable=true]:visible").last
            box.click()
            page.keyboard.insert_text(job["prompt"])
            page.wait_for_timeout(800)
            page.locator('button[aria-label="Start generation"]').click()
            log("sent", job["name"])
            quote = None
            for _ in range(36):  # up to 3 min for the agent's plan
                page.wait_for_timeout(5000)
                txt = page.evaluate("() => document.body.innerText")
                qs = [l for l in txt.splitlines() if "credits" in l and "?" in l]
                if qs and len(enabled_approves(page)) > n_before:
                    quote = qs[-1]
                    break
            shot(page, f"{job['name']}-confirm")
            log("quote", job["name"], quote)
            if not quote or not quoted_price(quote, expect):
                log("NOT approved", job["name"], "expected", expect)
                refused += 1
                if refused >= 2:  # circuit breaker: two refusals in a row mean the page or the price changed, not the job
                    log("two NOT approved in a row, halting")
                    break
                continue
            refused = 0
            enabled_approves(page)[-1].click()
            spent += expect
            approved += 1
            open(DONE, "a", encoding="utf8").write(job["name"] + "\n")
            log("approved", job["name"], "spent", spent)
            page.wait_for_timeout(8000)

        # wait for the approved videos to land, then download the newest ones at 720p original
        target = TOP or (1 if mode == "--after" else approved * CFG["count"])
        end = time.time() + 1500
        new = []
        # poll the open page; reloading every minute got the profile logged out (5 Oct 26)
        while time.time() < end:
            tiles = video_tiles(page)
            new = tiles[:TOP] if TOP else clips_above(tiles, anchor)
            log("new clips", len(new), "target", target)
            if len(new) >= target:
                break
            if failed_cards(page) > fails_before:  # stop waiting: nothing will land for this shot
                why = [l.strip() for l in page.evaluate("() => document.body.innerText").splitlines() if l.strip().startswith("Unable")]
                log("FAILED in Flow, refunded by Flow:", (why or ["no reason shown"])[0][:200])
                break
            page.wait_for_timeout(60000)
        shot(page, "grid")
        for i, (x, y, clip) in enumerate(new[:target]):
            log("opening", clip)
            # find the tile again by its clip id and scroll it into view: the positions taken before the loop go stale
            # once a tile has been opened and closed, and the second download then clicked beside its tile (12 Oct 26)
            pos = page.evaluate("""(id) => { const e = [...document.querySelectorAll('img,video')].find(e => (e.currentSrc || e.src || '').includes(id) && e.getBoundingClientRect().width > 300);
                if (!e) return null; e.scrollIntoView({block: 'center'}); const r = e.getBoundingClientRect();
                return [Math.round(r.left + r.width / 2), Math.round(r.top + r.height / 2)]; }""", clip)
            if not pos:
                log("tile not in the grid, skipped", clip)
                continue
            page.wait_for_timeout(1500)
            x, y = page.evaluate("""(id) => { const r = [...document.querySelectorAll('img,video')].find(e => (e.currentSrc || e.src || '').includes(id) && e.getBoundingClientRect().width > 300).getBoundingClientRect();
                return [Math.round(r.left + r.width / 2), Math.round(r.top + r.height / 2)]; }""", clip)
            page.mouse.click(x, y)
            page.wait_for_timeout(4000)
            title = page.evaluate("() => document.title")
            page.locator('button[aria-label="Download media"]').first.click()
            page.wait_for_timeout(1500)
            with page.expect_download(timeout=120000) as dl:
                page.locator('[role=menuitem]:has-text("720p")').first.click()
            path = os.path.join(OUT, f"raw-{i + 1:02d}.mp4")
            if os.path.exists(path) and os.path.getsize(path):  # never write over a clip already on disk
                path = path.replace(".mp4", f"-{time.strftime('%H%M%S')}.mp4")
            dl.value.save_as(path)
            shot(page, f"dl-{i + 1:02d}")
            log("saved", path, os.path.getsize(path), title)
            log(*verdict(path))
            page.keyboard.press("Escape")
            page.wait_for_timeout(3000)
            to_grid(page)
    except Exception as e:
        shot(page, "error")
        log("ERROR", repr(e)[:400])
    finally:
        os.remove(LOCK)
        log("done spent", spent)  # browser stays open and signed in
