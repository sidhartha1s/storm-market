# Save one Flow download to a path through the driver's own CDP session, never through Chrome's default behaviour.
# Why (Buffalo ins-paul-3 and -5, 29 Oct 26): Browser.setDownloadBehavior is one setting per browser context, shared by
# every CDP client. A second client that attaches and detaches mid-run (a 3-minute screenshot loop over
# connect_over_cdp) overrides the driver's setting, and its detach puts Chrome back on its default: the clip goes to
# ~/Downloads/<suggested name> and Playwright's save_as writes 0 B. So the setting is re-asserted right before each click.
import os, shutil, tempfile


def save_download(browser, page, click, path, timeout=120000):
    # click: the call that starts the download. Returns the saved path; raises if Chrome did not write the file here.
    folder = tempfile.mkdtemp(prefix="flowdl-")
    cdp = browser.new_browser_cdp_session()
    try:
        cdp.send("Browser.setDownloadBehavior", {"behavior": "allowAndName", "downloadPath": folder, "eventsEnabled": True})
        with page.expect_download(timeout=timeout) as dl:
            click()
        guid = os.path.basename(dl.value.path())  # path() returns once Chrome reports the download completed
        shutil.move(os.path.join(folder, guid), path)
        return path
    finally:
        cdp.detach()
        shutil.rmtree(folder, ignore_errors=True)
