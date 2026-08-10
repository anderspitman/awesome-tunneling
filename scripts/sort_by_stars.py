#!/usr/bin/env python3
"""Fetch current GitHub star counts for entries in the awesome-tunneling README
and sort the "Open source" section by stars (descending).

Entries without a GitHub repo (or whose repo can't be resolved) have no star
count, so they stay at the top of the section in their original relative order.

Usage:
    python3 scripts/sort_by_stars.py            # fetch counts (cached) and rewrite README.md
    python3 scripts/sort_by_stars.py --refresh  # ignore cache, fetch fresh counts
    python3 scripts/sort_by_stars.py --check    # fetch + print report, don't rewrite

Requires GH_TOKEN (or GITHUB_TOKEN) in the environment for a comfortable API
rate limit. Results are cached in .cache/stars.json to avoid hammering the API.
"""

import json
import os
import re
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(ROOT, "README.md")
CACHE = os.path.join(ROOT, ".cache", "stars.json")
CACHE_MAX_AGE = 6 * 3600  # seconds

SECTION_START = "# Open source (at least with a reasonably permissive license)"
SECTION_END = "# Commercial/Closed source"

ENTRY_RE = re.compile(r"^(\* \[)([^\]]+)(\]\()([^)]+)(\))(.*)$")
GITHUB_REPO_RE = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")


def github_token():
    return os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN") or ""


def fetch_star_count(repo):
    """Return stargazers_count for repo (owner/name), or None on failure."""
    url = f"https://api.github.com/repos/{repo}"
    req = urllib.request.Request(url)
    token = github_token()
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "awesome-tunneling-star-sorter")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.load(resp)
            return data.get("stargazers_count")
    except urllib.error.HTTPError as e:
        # 404 = repo not found/renamed; 403 = rate limited
        print(f"  !! {repo}: HTTP {e.code}", file=sys.stderr)
        if e.code == 403:
            time.sleep(60)
        return None
    except Exception as e:  # noqa: BLE001
        print(f"  !! {repo}: {e}", file=sys.stderr)
        return None


def repo_for_entry(line):
    """Pick the most likely GitHub repo (owner/name) for an entry line.

    Prefer the primary link ([Name](URL)); fall back to any other github.com
    URL on the line (badge / stargazers link).
    """
    m = ENTRY_RE.match(line)
    primary = m.group(4) if m else ""
    candidates = []
    if "github.com/" in primary:
        match = GITHUB_REPO_RE.search(primary)
        if match:
            candidates.append(match.group(1))
    for match in GITHUB_REPO_RE.finditer(line):
        candidates.append(match.group(1))
    # Dedupe, keep order
    seen = set()
    ordered = []
    for c in candidates:
        if c not in seen:
            seen.add(c)
            ordered.append(c)
    return ordered[0] if ordered else None


def load_cache():
    try:
        with open(CACHE) as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return {}


def save_cache(cache):
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    with open(CACHE, "w") as f:
        json.dump(cache, f, indent=2, sort_keys=True)


def main():
    refresh = "--refresh" in sys.argv
    check_only = "--check" in sys.argv

    with open(README) as f:
        lines = f.read().splitlines()

    # Locate the section
    try:
        start = lines.index(SECTION_START) + 1
    except ValueError:
        print(f"Section header not found: {SECTION_START}", file=sys.stderr)
        return 1
    end = len(lines)
    for i in range(start, len(lines)):
        if lines[i].startswith(SECTION_END):
            end = i
            break

    entries = []  # (line_number, line, repo, stars)
    cache = load_cache()
    for i in range(start, end):
        line = lines[i]
        if not line.startswith("* ["):
            continue
        repo = repo_for_entry(line)
        stars = None
        if repo:
            if refresh or repo not in cache or cache[repo].get("stars") is None:
                print(f"  fetching {repo} ...")
                stars = fetch_star_count(repo)
                cache[repo] = {"stars": stars, "fetched_at": time.time()}
            else:
                stars = cache[repo].get("stars")
        entries.append((i, line, repo, stars))

    save_cache(cache)

    # Sort: stars desc (stable), then entries with no stars (repo-less or 404)
    # in their original order at the end.
    def sort_key(e):
        _, _, repo, stars = e
        if stars is None:
            return (0, float("inf"))  # entries without a star count stay at the top
        return (1, -stars)

    entries_sorted = sorted(entries, key=sort_key)

    # Report
    print("\n=== Star counts (sorted) ===")
    for _, line, repo, stars in entries_sorted:
        name = ENTRY_RE.match(line).group(2)
        count = f"{stars:,}" if stars is not None else "N/A"
        print(f"  {count:>10}  {name}  ({repo})")

    if check_only:
        return 0

    # Rewrite the section
    new_lines = list(lines)
    for (old_i, _, _, _), (new_i, new_line, _, _) in zip(entries, entries_sorted):
        new_lines[old_i] = new_line
    # Sanity: make sure the sorted lines are exactly a permutation
    assert sorted(new_lines[start:end]) == sorted(lines[start:end]), "lines changed!"

    with open(README, "w") as f:
        f.write("\n".join(new_lines) + "\n")
    print(f"\nRewrote {len(entries)} entries in {os.path.relpath(README)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
