#!/usr/bin/env python3
"""Tell IndexNow search engines (Bing and partners) which pages changed.

Runs in CI after a successful deploy. Usage:
  indexnow.py             submit pages changed since $BEFORE (all pages if unknown)
  indexnow.py --all       submit every page in the live sitemap
  indexnow.py --dry-run   print what would be sent and send nothing
"""
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime

HOST = "raveeshmayya.com"
BASE = f"https://{HOST}"
KEY = "c465a9e2dee3914a2bbe9afbcd6d8e61"
ENDPOINT = "https://api.indexnow.org/IndexNow"
SITEMAP = f"{BASE}/sitemap.xml"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
UA = "raveeshmayya-indexnow/1.0"
# A change to any of these can alter many pages, so everything is resubmitted.
SITEWIDE = ("layouts/", "themes/", "data/", "hugo.yaml")


def git(*args):
    out = subprocess.run(["git", *args], capture_output=True, text=True)
    return out.stdout.strip() if out.returncode == 0 else ""


def sitemap_pages():
    # The query string bypasses the Pages CDN cache so a fresh deploy is visible.
    req = urllib.request.Request(f"{SITEMAP}?t={int(time.time())}", headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as resp:
        root = ET.fromstring(resp.read())
    pages = []
    for url in root.findall("sm:url", NS):
        loc = url.find("sm:loc", NS).text.strip()
        lastmod = url.find("sm:lastmod", NS)
        pages.append((loc, lastmod.text.strip() if lastmod is not None else None))
    return pages


def select_urls(pages, submit_all):
    before = os.environ.get("BEFORE", "").strip()
    if submit_all or not before or set(before) == {"0"} or git("cat-file", "-t", before) != "commit":
        return [loc for loc, _ in pages]
    changed = git("diff", "--name-only", before, "HEAD").splitlines()
    if any(path.startswith(SITEWIDE) for path in changed):
        return [loc for loc, _ in pages]
    # Hugo takes lastmod from the Git author date, so compare against the same kind of date.
    cutoff = datetime.fromisoformat(git("show", "-s", "--format=%aI", before))
    return [
        loc for loc, lastmod in pages
        if lastmod and datetime.fromisoformat(lastmod) > cutoff
    ]


def main():
    dry_run = "--dry-run" in sys.argv
    urls = select_urls(sitemap_pages(), "--all" in sys.argv)
    if not urls:
        print("No changed pages to submit.")
        return 0
    payload = {
        "host": HOST,
        "key": KEY,
        "keyLocation": f"{BASE}/{KEY}.txt",
        "urlList": urls,
    }
    print(f"{len(urls)} URL(s):")
    for url in urls:
        print("  ", url)
    if dry_run:
        print("Dry run: nothing sent.")
        return 0
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json; charset=utf-8", "User-Agent": UA},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print("IndexNow response:", resp.status)
            return 0 if resp.status in (200, 202) else 1
    except urllib.error.HTTPError as err:
        print("IndexNow response:", err.code, err.reason)
        return 1


if __name__ == "__main__":
    sys.exit(main())
