#!/usr/bin/env python3
"""Check unique external links in Markdown and the resource catalog."""

from __future__ import annotations

import argparse
import json
import re
import ssl
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
URL_RE = re.compile(r"https://[^\s<>()\]\[\"']+")
RESTRICTED = {401, 403, 429}
HARD_FAILURES = {404, 410}


def collect_urls() -> list[str]:
    urls: set[str] = set()
    for markdown in ROOT.rglob("*.md"):
        for url in URL_RE.findall(markdown.read_text(encoding="utf-8")):
            urls.add(url.rstrip(".,;:"))
    catalog = json.loads((ROOT / "catalog/resources.json").read_text(encoding="utf-8"))
    urls.update(item["url"] for item in catalog["resources"])
    return sorted(urls)


def check(url: str, timeout: float) -> tuple[str, str, int | None]:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "AI-Governance-Resource-Hub-Link-Checker/1.0", "Range": "bytes=0-2048"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout, context=ssl.create_default_context()) as response:
            status = response.getcode()
            return ("ok" if status < 400 else "error", url, status)
    except urllib.error.HTTPError as exc:
        if exc.code in RESTRICTED:
            return "restricted", url, exc.code
        return ("error" if exc.code in HARD_FAILURES or exc.code >= 400 else "ok", url, exc.code)
    except (urllib.error.URLError, TimeoutError, ssl.SSLError, OSError):
        return "network", url, None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=16)
    parser.add_argument("--timeout", type=float, default=15)
    parser.add_argument("--strict-network", action="store_true", help="Fail on DNS, TLS, and timeout errors")
    args = parser.parse_args()
    urls = collect_urls()
    results: list[tuple[str, str, int | None]] = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(check, url, args.timeout): url for url in urls}
        for future in as_completed(futures):
            results.append(future.result())
    failures = sorted(result for result in results if result[0] == "error")
    network = sorted(result for result in results if result[0] == "network")
    restricted = sum(result[0] == "restricted" for result in results)
    for _, url, status in failures:
        print(f"ERROR {status}: {url}")
    for _, url, _ in network:
        print(f"NETWORK: {url}")
    ok = len(results) - len(failures) - len(network) - restricted
    print(f"Checked {len(urls)} links: {ok} OK, {restricted} restricted, {len(network)} network errors, {len(failures)} hard failures.")
    return 1 if failures or (args.strict_network and network) else 0


if __name__ == "__main__":
    raise SystemExit(main())

