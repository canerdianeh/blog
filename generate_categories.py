#!/usr/bin/env python3
"""
generate_categories.py

Scans _posts/ for all categories and generates a page for each one
in category/<slug>/index.md

Run from repo root: python3 generate_categories.py
"""

import os, re, yaml

POSTS_DIR = "_posts"
CATEGORY_DIR = "category"


def get_categories(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        return []
    end = content.find("\n---", 3)
    if end == -1:
        return []
    fm = yaml.safe_load(content[3:end])
    return fm.get("categories", []) or []


def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')


def main():
    # Collect all categories
    categories = set()
    for filename in os.listdir(POSTS_DIR):
        if filename.endswith(".md"):
            for cat in get_categories(os.path.join(POSTS_DIR, filename)):
                categories.add(cat)

    print(f"Found {len(categories)} categories: {sorted(categories)}\n")

    os.makedirs(CATEGORY_DIR, exist_ok=True)

    for cat in sorted(categories):
        slug = slugify(cat)
        cat_dir = os.path.join(CATEGORY_DIR, slug)
        os.makedirs(cat_dir, exist_ok=True)
        filepath = os.path.join(cat_dir, "index.md")
        content = f"""---
layout: category
title: "Category: {cat}"
category: "{cat}"
permalink: /category/{slug}/
---
"""
        with open(filepath, "w") as f:
            f.write(content)
        print(f"  Created: {filepath}")

    print("\nDone. Commit the category/ directory.")

if __name__ == "__main__":
    main()
