#!/usr/bin/env python3
"""
fix_fences.py

Fixes broken fenced code blocks where the language tag got separated:
    ```            →    ```python
                
    python
    code...            code...
    ```                ```

Run from repo root: python3 fix_fences.py
"""

import os, re

DIRS = ["_posts", "_pages"]

# Matches: opening ``` alone on a line, optional blank lines, then a word (language tag)
BROKEN_FENCE = re.compile(r'```\s*\n+(\w+)\n', re.MULTILINE)

def fix_file(filepath):
    with open(filepath) as f:
        content = f.read()
    fixed = BROKEN_FENCE.sub(r'```\1\n', content)
    if fixed != content:
        with open(filepath, "w") as f:
            f.write(fixed)
        return True
    return False

def main():
    total = 0
    for d in DIRS:
        if not os.path.isdir(d):
            continue
        for filename in sorted(os.listdir(d)):
            if not (filename.endswith(".md") or filename.endswith(".html")):
                continue
            filepath = os.path.join(d, filename)
            if fix_file(filepath):
                print(f"Fixed: {filepath}")
                total += 1
    print(f"\nFixed {total} files.")

if __name__ == "__main__":
    main()
