#!/usr/bin/env python3
"""
Download every article written by “user-3” on the archived Sqreen blog.

• Start URL  : https://web.archive.org/web/20230526170501/https://blog.sqreen.com/author/user-3/
• Output dir : ./articles   (created automatically)
• Requirements: Python 3 standard library only – no external packages.

Each article is stored as {slugified-title}.html containing the full
Wayback-captured HTML.

Run:
    python sqreen_scraper_stdlib.py
"""

import html
import os
import re
import time
from urllib.parse import urljoin
from urllib.request import Request, urlopen

START_URL = (
    "https://web.archive.org/web/20230526170501/"
    "https://blog.sqreen.com/author/user-3/"
)
OUTPUT_DIR = "articles"
USER_AGENT = "Mozilla/5.0 (compatible; WaybackBot/1.0)"
POLITE_DELAY = 0.5  # seconds between page fetches


# ---------- helpers ---------------------------------------------------------- #
def fetch(url: str) -> str:
    """Return the HTML (decoded as UTF-8) for *url*."""
    req = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(req, timeout=20) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def slugify(text: str) -> str:
    """Transform *text* into a filesystem-safe slug."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\-]+", "-", text)
    return re.sub(r"-{2,}", "-", text).strip("-") or "untitled"


def extract_article_links(page_html: str) -> list[str]:
    """Return every article link found in an author page’s HTML."""
    pattern = re.compile(
        r'<h2[^>]*class="[^"]*entry-title[^"]*"[^>]*>\s*'
        r'<a[^>]*href="([^"]+)"',
        re.I,
    )
    return pattern.findall(page_html)


def extract_next_page(page_html: str) -> str | None:
    """Return the URL of the “next” author page, or None if on the last page."""
    pattern = re.compile(
        r'<a[^>]+(?:rel="next"[^>]*|class="[^"]*\bnext\b[^"]*")[^>]*href="([^"]+)"',
        re.I,
    )
    match = pattern.search(page_html)
    return match.group(1) if match else None


def extract_title(article_html: str) -> str:
    """Extract the article <h1 class="entry-title">…</h1> text."""
    pattern = re.compile(
        r'<h1[^>]*class="[^"]*entry-title[^"]*"[^>]*>(.*?)</h1>',
        re.I | re.S,
    )
    match = pattern.search(article_html)
    if not match:
        return "untitled"
    raw = re.sub(r"<[^>]+>", "", match.group(1))  # strip nested tags
    return html.unescape(raw.strip()) or "untitled"


def save_article(url: str) -> None:
    """Download the article at *url* and write it to disk."""
    html_text = fetch(url)
    title = extract_title(html_text)
    filename = slugify(title) + ".html"
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as fp:
        fp.write(html_text)
    print(f"✓ Saved {filename}")


# ---------- main crawler ----------------------------------------------------- #
def crawl(start_url: str) -> None:
    """Walk the author pagination, saving every article encountered."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    visited_pages: set[str] = set()
    page_url: str | None = start_url

    while page_url and page_url not in visited_pages:
        print(f"• Scanning {page_url}")
        visited_pages.add(page_url)
        page_html = fetch(page_url)

        # 1) harvest & save each article
        for link in extract_article_links(page_html):
            abs_link = urljoin(page_url, link)
            save_article(abs_link)
            time.sleep(POLITE_DELAY)  # keep traffic gentle

        # 2) follow pagination if there's a “next” page
        next_url = extract_next_page(page_html)
        page_url = urljoin(page_url, next_url) if next_url else None


if __name__ == "__main__":
    crawl(START_URL)
