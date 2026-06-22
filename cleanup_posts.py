#!/usr/bin/env python3
"""
cleanup_posts.py - Run from Jekyll repo root to clean _posts/
    python3 cleanup_posts.py              # includes image fetching
    python3 cleanup_posts.py --no-images  # skip image fetching

Requirements: pip3 install requests beautifulsoup4 markdownify
"""

import os, re, sys, time, html, requests
from urllib.parse import urlparse
from pathlib import Path
from bs4 import BeautifulSoup
from markdownify import markdownify as md

TARGET_DIR = "_posts"
ASSETS_DIR = "assets/images"
REQUEST_DELAY = 0.5
SKIP_IMAGES = "--no-images" in sys.argv
FENCED_BLOCK = re.compile(r'(```[^\n]*\n[\s\S]*?```)', re.MULTILINE)


def download_image(url):
    """Download image to assets/images/, return local path or None."""
    try:
        parsed = urlparse(url)
        # Preserve the path structure from the URL
        url_path = parsed.path.lstrip("/")
        # Strip domain-specific prefix (e.g. files/2022/11/img.jpg -> 2022/11/img.jpg)
        parts = url_path.split("/")
        # Drop the first path component if it's 'files' or similar non-date prefix
        if parts and not re.match(r'^\d{4}$', parts[0]):
            parts = parts[1:]
        local_path = os.path.join(ASSETS_DIR, *parts)
        if os.path.exists(local_path):
            return "/" + local_path
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        resp = requests.get(url, timeout=15, headers={"User-Agent": "Jekyll-cleanup/1.0"})
        if resp.status_code != 200:
            return None
        with open(local_path, "wb") as f:
            f.write(resp.content)
        print(f"  Downloaded: {local_path}")
        return "/" + local_path
    except Exception as e:
        print(f"  WARNING: could not download {url}: {e}")
        return None


def fetch_og_image(url):
    """Fetch og:image URL from a page."""
    try:
        resp = requests.get(url, timeout=10, headers={"User-Agent": "Jekyll-cleanup/1.0"})
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
        print(f"  WARNING: {e}")
    return None


# SyntaxHighlighter shortcode language mapping
SHORTCODE_LANGS = {
    'js': 'javascript', 'javascript': 'javascript',
    'python': 'python', 'py': 'python',
    'php': 'php', 'bash': 'bash', 'shell': 'bash', 'sh': 'bash',
    'xml': 'xml', 'html': 'html', 'css': 'css',
    'perl': 'perl', 'java': 'java', 'ruby': 'ruby',
    'c': 'c', 'cpp': 'cpp', 'sql': 'sql', 'plain': '',
}

def convert_shortcode_blocks(body):
    """Convert [js]...[/js] style SyntaxHighlighter shortcodes to fenced code blocks."""
    langs = '|'.join(SHORTCODE_LANGS.keys())
    pattern = re.compile(
        rf'\[({langs})(?:\s[^\]]*)?\](.*?)\[/(?:{langs})\]',
        re.DOTALL | re.IGNORECASE
    )
    def replacer(m):
        lang = SHORTCODE_LANGS.get(m.group(1).lower(), m.group(1).lower())
        code = m.group(2).strip('\n')
        return f"\n```{lang}\n{code}\n```\n"
    return pattern.sub(replacer, body)


def convert_wp_code_blocks(body):
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
    if not re.search(r'<[a-zA-Z]', segment):
        return segment
    return md(segment, heading_style="ATX", bullets="-", strip=["script", "style"])


def clean_body(body):
    body = convert_shortcode_blocks(body)
    body = convert_wp_code_blocks(body)
    parts = FENCED_BLOCK.split(body)
    result = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            result.append(part)
        else:
            result.append(html_to_markdown(part))
    body = ''.join(result)
    body = re.sub(r'([^\n])(```)', r'\1\n\n```', body)        # blank line before opening fence
    body = re.sub(r'```([^\n`\w])', r'```\n\n\1', body)       # blank line after closing fence (same line, non-word)
    body = re.sub(r'```\n([^\n`])', r'```\n\n\1', body)       # blank line after closing fence (next line)
    body = re.sub(r'\n{3,}', '\n\n', body)
    return body.strip()


def parse_post(content):
    if not content.startswith("---"):
        return None, content
    end = content.find("\n---", 3)
    if end == -1:
        return None, content
    return content[3:end].strip(), content[end+4:].strip()


def has_real_image(fm):
    m = re.search(r'^image\s*:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
    if not m:
        return False
    val = m.group(1).strip().strip('"\'')
    # Already a local path
    if val.startswith("/assets/"):
        return True
    return bool(val) and "blank.jpg" not in val


def get_permalink(fm):
    m = re.search(r'^permalink\s*:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
    return m.group(1).strip() if m else None


def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    fm, body = parse_post(content)
    if fm is None:
        print(f"  SKIP (no front matter)")
        return
    changed = False

    if not SKIP_IMAGES:
        # Check if image exists and is already local
        m = re.search(r'^image\s*:\s*["\']?(.*?)["\']?\s*$', fm, re.MULTILINE)
        current_image = m.group(1).strip().strip('"\'') if m else ""

        if current_image.startswith("/assets/"):
            print(f"  Image already local, skipping")
        elif current_image and "blank.jpg" not in current_image:
            # Remote URL — download it
            local_path = download_image(current_image)
            if local_path:
                fm = re.sub(r'\nimage:.*', '', fm)
                fm += f'\nimage: "{local_path}"'
                changed = True
        else:
            # No image or blank — fetch from WP site
            permalink = get_permalink(fm)
            if permalink:
                url = "https://nerdian.ca" + permalink if permalink.startswith("/") else permalink
                print(f"  Fetching og:image...")
                og_url = fetch_og_image(url)
                time.sleep(REQUEST_DELAY)
                if og_url:
                    local_path = download_image(og_url)
                    if local_path:
                        fm = re.sub(r'\nimage:.*', '', fm)
                        fm += f'\nimage: "{local_path}"'
                        changed = True
                    else:
                        print(f"  Could not download image")
                else:
                    print(f"  No og:image found")

    cleaned_body = clean_body(body)
    if cleaned_body != body:
        changed = True
        print(f"  Body converted")

    if changed:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"---\n{fm}\n---\n\n{cleaned_body}\n")
        print(f"  Updated.")
    else:
        print(f"  No changes.")


def main():
    if not os.path.isdir(TARGET_DIR):
        print(f"ERROR: '{TARGET_DIR}' not found. Run from repo root.")
        return
    files = sorted([f for f in os.listdir(TARGET_DIR) if f.endswith(".md") or f.endswith(".html")])
    print(f"Found {len(files)} files in {TARGET_DIR}/")
    print(f"Image fetching: {'DISABLED' if SKIP_IMAGES else 'ENABLED (downloading locally)'}\n")
    for i, filename in enumerate(files, 1):
        print(f"[{i}/{len(files)}] {filename}")
        process_file(os.path.join(TARGET_DIR, filename))
        print()
    print("Done.")

if __name__ == "__main__":
    main()
