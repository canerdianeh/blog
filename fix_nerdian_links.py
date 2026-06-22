#!/usr/bin/env python3
"""
fix_nerdian_links.py

Scans _posts/ and _pages/ for links and images pointing to nerdian.ca,
downloads them locally, and updates the references.

Run from repo root: python3 fix_nerdian_links.py
"""

import os, re, requests
from urllib.parse import urlparse
from pathlib import Path

DIRS = ["_posts", "_pages"]
ASSETS_DIR = "assets"
REQUEST_DELAY = 0.3

# Match markdown links and images pointing to nerdian.ca or blog.ianbeyer.com
NERDIAN_URL = re.compile(
    r'(!\[([^\]]*)\]\()(https?://(?:nerdian\.ca|blog\.ianbeyer\.com)/files/([^\)]+))(\))',
    re.IGNORECASE
)
NERDIAN_LINK = re.compile(
    r'(\[([^\]]+)\]\()(https?://(?:nerdian\.ca|blog\.ianbeyer\.com)/files/([^\)]+))(\))',
    re.IGNORECASE
)


def url_to_local(url):
    parsed = urlparse(url)
    # files/2020/06/img.png → assets/2020/06/img.png
    path_parts = parsed.path.lstrip('/').split('/')
    if path_parts and path_parts[0] == 'files':
        path_parts = path_parts[1:]
    return os.path.join(ASSETS_DIR, *path_parts)


def download_file(url, local_path):
    if os.path.exists(local_path):
        print(f"    Already exists: {local_path}")
        return True
    try:
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        resp = requests.get(url, timeout=20, headers={"User-Agent": "Jekyll-cleanup/1.0"})
        if resp.status_code == 200:
            with open(local_path, 'wb') as f:
                f.write(resp.content)
            print(f"    Downloaded: {local_path}")
            return True
        else:
            print(f"    FAILED ({resp.status_code}): {url}")
            return False
    except Exception as e:
        print(f"    ERROR: {e}")
        return False


def process_file(filepath):
    with open(filepath) as f:
        content = f.read()

    changed = False

    # Fix image src pointing to nerdian.ca
    def replace_image(m):
        nonlocal changed
        url = m.group(3)
        local_path = url_to_local(url)
        if download_file(url, local_path):
            changed = True
            return f"{m.group(1)}{{{{site.baseurl}}}}/{local_path}{m.group(5)}"
        return m.group(0)

    # Fix href links pointing to nerdian.ca files
    def replace_link(m):
        nonlocal changed
        url = m.group(3)
        local_path = url_to_local(url)
        if download_file(url, local_path):
            changed = True
            return f"{m.group(1)}{{{{site.baseurl}}}}/{local_path}{m.group(5)}"
        return m.group(0)

    content = NERDIAN_URL.sub(replace_image, content)
    content = NERDIAN_LINK.sub(replace_link, content)

    if changed:
        with open(filepath, 'w') as f:
            f.write(content)
        print(f"  Updated: {filepath}")


def main():
    for d in DIRS:
        if not os.path.isdir(d):
            continue
        files = sorted([f for f in os.listdir(d) if f.endswith('.md') or f.endswith('.html')])
        print(f"\nScanning {d}/ ({len(files)} files)...")
        for filename in files:
            filepath = os.path.join(d, filename)
            with open(filepath) as f:
                content = f.read()
            if 'nerdian.ca' in content or 'blog.ianbeyer.com' in content:
                print(f"\n{filename}")
                process_file(filepath)
    print("\nDone.")

if __name__ == "__main__":
    main()
