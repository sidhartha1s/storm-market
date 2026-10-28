# Buffalo ins-paul-3/-5 (29 Oct 26): a second CDP client that attached and detached mid-run sent the clip to Chrome's
# default folder and save_as wrote 0 B. This replays that on a throwaway headless Chrome (own profile, own port, no
# window) and checks the old path loses the file while flowdl.save_download keeps it.
import http.server, json, os, socket, subprocess, sys, tempfile, threading, time, urllib.request
from playwright.sync_api import sync_playwright
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from flowdl import save_download

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BODY = os.urandom(2 * 1024 * 1024)
NOWIN = getattr(subprocess, "CREATE_NO_WINDOW", 0)


class Clip(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/clip.mp4":
            self.send_response(200)
            self.send_header("Content-Type", "video/mp4")
            self.send_header("Content-Disposition", 'attachment; filename="clip.mp4"')
            self.send_header("Content-Length", str(len(BODY)))
            self.end_headers()
            self.wfile.write(BODY)
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b'<a id="dl" href="/clip.mp4">720p</a>')

    def log_message(self, *a):
        pass


def free_port():
    s = socket.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close()
    return port


def other_client(cdp_url):
    # what the screenshot loop did: attach with Playwright, then detach
    subprocess.run([sys.executable, "-c", "import sys; from playwright.sync_api import sync_playwright as s\n"
                    "with s() as p: p.chromium.connect_over_cdp(sys.argv[1]).contexts[0].pages[0].title()", cdp_url],
                   check=True, timeout=60, creationflags=NOWIN)


root = tempfile.mkdtemp(prefix="flowdl-test-")
default_dir = os.path.join(root, "chrome-default-downloads")
os.makedirs(os.path.join(root, "profile", "Default"))
os.makedirs(default_dir)
json.dump({"download": {"default_directory": default_dir, "prompt_for_download": False}},
          open(os.path.join(root, "profile", "Default", "Preferences"), "w"))
srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Clip)
threading.Thread(target=srv.serve_forever, daemon=True).start()
site = f"http://127.0.0.1:{srv.server_port}/"
port = free_port()
chrome = subprocess.Popen([CHROME, "--headless=new", f"--remote-debugging-port={port}", f"--user-data-dir={os.path.join(root, 'profile')}",
                           "--no-first-run", "--no-default-browser-check", site], creationflags=NOWIN)
cdp_url = f"http://127.0.0.1:{port}"
try:
    for _ in range(60):
        try:
            urllib.request.urlopen(cdp_url + "/json/version", timeout=2); break
        except Exception:
            time.sleep(0.5)
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(cdp_url)
        page = browser.contexts[0].pages[0]
        page.wait_for_selector("#dl")

        other_client(cdp_url)
        with page.expect_download() as dl:  # the old path
            page.click("#dl")
        old = os.path.join(root, "old.mp4")
        try:
            dl.value.save_as(old)
        except Exception as e:
            print("old path save_as raised:", repr(e)[:120])
        old_size = os.path.getsize(old) if os.path.exists(old) else -1
        in_default = os.path.exists(os.path.join(default_dir, "clip.mp4"))
        print("old path:", old_size, "B saved; Chrome's default folder got the clip:", in_default)
        assert old_size != len(BODY) and in_default, "old path kept the clip: the detaching client no longer resets Chrome"

        other_client(cdp_url)
        new = save_download(browser, page, lambda: page.click("#dl"), os.path.join(root, "new.mp4"))
        print("save_download:", os.path.getsize(new), "B")
        assert open(new, "rb").read() == BODY, "save_download lost the clip"
    print("test_flowdl OK")
finally:
    chrome.kill()
    srv.shutdown()
