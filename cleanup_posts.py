#!/usr/bin/env python3
"""
cleanup_posts.py

Run from the root of your Jekyll repo:
    python3 cleanup_posts.py              # full run (fetches images)
    python3 cleanup_posts.py --no-images  # skip image fetching

Requirements:
    pip3 install requests beautifulsoup4 markdownify
"""

import os
import re
import sys
import time
import html
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

REQUEST_DELAY = 0.5
SKIP_IMAGES = "--no-images" in sys.argv

# Directory defaults to _posts, override with e.g. python3 cleanup_posts.py _pages
args = [a for a in sys.argv[1:] if not a.startswith("--")]
POSTS_DIR = args[0] if args else "_posts"

# Matches fenced code blocks (``` with or without language)
FENCED_BLOCK = re.compile(r'(```[^\n]*\n[\s\S]*?```)', re.MULTILINE)


def convert_wp_code_blocks(body):
    """Convert <pre class='wp-block-code'> to fenced markdown."""
    soup = BeautifulSoup(body, "html.parser")
    changed = False
    for pre in soup.find_all("pre", class_=re.compile(r"wp-block-code")):
        code_tag = pre.find("code")
        if not code_tag:
            continue
        lang = code_tag.get("lang", "")
        if not lang:
            for cls in code_tag.get("class", []):
                m = re.match(r"language-(\w+)", cls)
                if m:
                    lang = m.group(1)
                    break
        code = html.unescape(code_tag.get_text()).strip("\n")
        pre.replace_with(f"\n```{lang}\n{code}\n```\n")
        changed = True
    return str(soup) if changed else body


def html_to_markdown(segment):
    """Convert an HTML segment to markdown, skipping if it has no HTML."""
    if not re.search(r'<[a-zA-Z]', segment):
        return segment
    return md(segment, heading_style="ATX", bullets="-", strip=["script", "style"])


def clean_body(body):
    # Step 1: convert any remaining wp-block-code pre tags
    body = convert_wp_code_blocks(body)

    # Step 2: split on fenced code blocks — even indices are HTML, odd are code
    parts = FENCED_BLOCK.split(body)

    result = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            # Fenced code block — keep exactly as-is
            result.append(part)
        else:
            # HTML segment — convert to markdown
            result.append(html_to_markdown(part))

    body = ''.join(result)

    # Step 3: ensure blank lines before and after fenced code blocks
    body = re.sub(r'([^\n])(```)', r'\1\n\n```', body)      # text immediately before opening fence
    body = re.sub(r'```([^\n`])', r'```\n\n\1', body)       # text on same line as closing fence
    body = re.sub(r'```\n([^\n`])', r'```\n\n\1', body)     # text on next line after closing fence, no blank

    # Step 4: collapse excessive blank lines
    body = re.sub(r'\n{3,}', '\n\n', body)
    return body.strip()


def fetch_og_image(url):
    try:
        resp = requests.get(url, timeout=10,
                            headers={"User-Agent": "Jekyll-cleanup-script/1.0"})
        if resp.status_code != 200:
            return None
        soup = BeautifulSoup(resp.text, "html.parser")
        tag = soup.find("meta", property="og:image")
        if tag and tag.get("content"):
            img = tag["content"]
            if "blank.jpg" in img or not img.strip():
                return None
            return img
    except Exception as e:
        print(f"  WARNING: could not fetch {url}: {e}")
    return None


def parse_post(content):
    if not content.startswith("---"):
        return None, content
    end = content.find("\n---", 3)
    if end == -1:
        return None, content
    fm = content[3:end].strip()
    body = content[end+4:].strip()
    return fm, body


def has_real_image(fm):
    m = re.search(r'^image\s*:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
    if not m:
        return False
    val = m.group(1).strip().strip('"\'')
    return bool(val) and "blank.jpg" not in val


def get_permalink(fm):
    m = re.search(r'^permalink\s*:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return None


def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    fm, body = parse_post(content)
    if fm is None:
        print(f"  SKIP (no front matter): {filepath}")
        return

    changed = False

    # 1. Image fetching
    if not SKIP_IMAGES and not has_real_image(fm):
        permalink = get_permalink(fm)
        if permalink:
            base = "https://nerdian.ca"
            url = base + permalink if permalink.startswith("/") else permalink
            print(f"  Fetching og:image from {url}")
            og_image = fetch_og_image(url)
            time.sleep(REQUEST_DELAY)
            if og_image:
                fm = re.sub(r'\nimage:.*', '', fm)
                fm = fm + f'\nimage: "{og_image}"'
                print(f"  Found image: {og_image}")
                changed = True
            else:
                print(f"  No og:image found")

    # 2. Convert body to clean markdown
    cleaned_body = clean_body(body)
    if cleaned_body != body:
        changed = True
        print(f"  Body converted to markdown")

    if changed:
        new_content = f"---\n{fm}\n---\n\n{cleaned_body}\n"
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  Updated.")
    else:
        print(f"  No changes needed.")


def main():
    if not os.path.isdir(POSTS_DIR):
        print(f"ERROR: '{POSTS_DIR}' directory not found. Run from your Jekyll repo root.")
        return

    posts = sorted([f for f in os.listdir(POSTS_DIR) if f.endswith(".md") or f.endswith(".html")])
    print(f"Found {len(posts)} posts in {POSTS_DIR}/")
    print(f"Image fetching: {'DISABLED' if SKIP_IMAGES else 'ENABLED'}\n")

    for i, filename in enumerate(posts, 1):
        filepath = os.path.join(POSTS_DIR, filename)
        print(f"[{i}/{len(posts)}] {filename}")
        process_file(filepath)
        print()

    print("Done.")


if __name__ == "__main__":
    main()
