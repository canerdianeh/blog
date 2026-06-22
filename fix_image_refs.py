#!/usr/bin/env python3
"""
fix_image_refs.py

One-time fix: for posts/pages with remote image URLs, check if the image
was already downloaded to assets/images/ and update the reference to the
local path. If not downloaded yet, download it now.

Run from repo root: python3 fix_image_refs.py
"""

import os, re, requests
from urllib.parse import urlparse

DIRS = ["_posts", "_pages"]
ASSETS_DIR = "assets/images"


def url_to_local_path(url):
    """Convert a remote image URL to expected local path."""
    parsed = urlparse(url)
    parts = parsed.path.lstrip("/").split("/")
    # Drop non-date leading components (e.g. 'files')
    if parts and not re.match(r'^\d{4}$', parts[0]):
        parts = parts[1:]
    return os.path.join(ASSETS_DIR, *parts)


def download_image(url, local_path):
    try:
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        resp = requests.get(url, timeout=15, headers={"User-Agent": "Jekyll-cleanup/1.0"})
        if resp.status_code == 200:
            with open(local_path, "wb") as f:
                f.write(resp.content)
            return True
    except Exception as e:
        print(f"  ERROR downloading: {e}")
    return False


def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find image: field with a remote URL
    m = re.search(r'^(image:\s*["\']?)(https?://[^\s"\']+)(["\']?\s*)$', content, re.MULTILINE)
    if not m:
        return

    remote_url = m.group(2)
    local_path = url_to_local_path(remote_url)

    if not os.path.exists(local_path):
        print(f"  Downloading: {remote_url}")
        if not download_image(remote_url, local_path):
            print(f"  FAILED - keeping remote URL")
            return
        print(f"  Saved to: {local_path}")
    else:
        print(f"  Already downloaded: {local_path}")

    # Update the reference
    local_ref = "/" + local_path
    new_content = re.sub(
        r'^image:\s*["\']?https?://[^\s"\']+["\']?\s*$',
        f'image: "{local_ref}"',
        content,
        flags=re.MULTILINE
    )
    if new_content != content:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  Reference updated to: {local_ref}")


def main():
    for d in DIRS:
        if not os.path.isdir(d):
            continue
        files = [f for f in os.listdir(d) if f.endswith(".md") or f.endswith(".html")]
        print(f"\nProcessing {d}/ ({len(files)} files)")
        for filename in sorted(files):
            filepath = os.path.join(d, filename)
            with open(filepath) as f:
                content = f.read()
            if "image:" in content and "http" in content:
                print(f"\n{filename}")
                process_file(filepath)

    print("\nDone.")

if __name__ == "__main__":
    main()
