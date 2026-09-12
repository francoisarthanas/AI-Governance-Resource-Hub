#!/usr/bin/env python3
"""Report external-link reachability; never equate restricted access with verification."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import json
from pathlib import Path
import ssl
import urllib.error
import urllib.request
from urllib.parse import urldefrag, urlsplit

from validate import markdown_targets

ROOT = Path(__file__).resolve().parents[1]
RESTRICTED = {401, 403, 407, 429, 451}
HARD_FAILURES = {404, 410}
STATUSES = ("ok", "restricted", "network", "dead", "review")


def collect_urls(root: Path) -> list[str]:
    urls: set[str] = set()
    for markdown in root.rglob("*.md"):
        if any(part in {".git", "node_modules", ".venv", "reports"} for part in markdown.relative_to(root).parts):
            continue
        targets, _ = markdown_targets(markdown.read_text(encoding="utf-8"))
        urls.update(urldefrag(url)[0] for url in targets if urlsplit(url).scheme in {"http", "https"})
    catalog = json.loads((root / "catalog/resources.json").read_text(encoding="utf-8"))
    urls.update(urldefrag(item["url"])[0] for item in catalog["resources"])
    return sorted(urls)


def check(url: str, timeout: float) -> dict:
    result = {"url": url, "status": "network", "http_status": None, "final_url": None, "detail": ""}
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "AI-Governance-Resource-Hub-Link-Checker", "Range": "bytes=0-1023"},
        method="GET",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout, context=ssl.create_default_context()) as response:
            code = response.getcode()
            result.update(http_status=code, final_url=response.geturl())
            result["status"] = "ok" if 200 <= code < 300 else "review"
    except urllib.error.HTTPError as exc:
        result.update(http_status=exc.code, final_url=exc.geturl())
        result["status"] = "restricted" if exc.code in RESTRICTED else "dead" if exc.code in HARD_FAILURES else "review"
        result["detail"] = "Access restricted; content not verified." if exc.code in RESTRICTED else str(exc.reason)
    except (urllib.error.URLError, TimeoutError, ssl.SSLError, OSError, ValueError) as exc:
        result["detail"] = str(exc)[:300]
    return result


def markdown_report(report: dict) -> str:
    counts = report["counts"]
    lines = [
        "# External link report", "", f'Checked: {report["checked_at"]}', "",
        "HTTP reachability is not a review of content, accuracy, suitability, or current version. A successful response can still be a login screen or a soft 404.", "",
        "Access restrictions, network errors, and other HTTP failures need manual review. This check does not change the catalog.", "",
        "| Reachable | Restricted | Network | 404 / 410 | Other HTTP review |",
        "| ---: | ---: | ---: | ---: | ---: |",
        f'| {counts["ok"]} | {counts["restricted"]} | {counts["network"]} | {counts["dead"]} | {counts["review"]} |', "",
        "## Links requiring attention", "",
        "| Result | HTTP | URL |", "| --- | --- | --- |",
    ]
    attention = [item for item in report["results"] if item["status"] != "ok"]
    for item in attention:
        url = item["url"].replace("|", "%7C")
        lines.append(f'| {item["status"]} | {item["http_status"] or "—"} | [Open source](<{url}>) |')
    if not attention:
        lines.append("| None | — | All checked URLs returned successful HTTP responses. |")
    return "\n".join(lines) + "\n"


def positive_int(value: str) -> int:
    result = int(value)
    if result < 1:
        raise argparse.ArgumentTypeError("must be at least 1")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--workers", type=positive_int, default=6)
    parser.add_argument("--timeout", type=float, default=15)
    parser.add_argument("--json", dest="json_path", type=Path, help="Write the complete machine-readable report")
    parser.add_argument("--markdown", dest="markdown_path", type=Path, help="Write the human-readable report")
    parser.add_argument("--report-only", action="store_true", help="Return success even for 404/410; scheduled review uses this mode")
    args = parser.parse_args()
    if args.timeout <= 0:
        parser.error("--timeout must be greater than zero")
    urls = collect_urls(args.root.resolve())
    results = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(check, url, args.timeout) for url in urls]
        for future in as_completed(futures):
            results.append(future.result())
    results.sort(key=lambda item: (item["status"], item["url"]))
    counts = {status: sum(item["status"] == status for item in results) for status in STATUSES}
    report = {
        "checked_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "scope": "HTTP reachability only; restricted links are unverified; source quality requires human review.",
        "total": len(results), "counts": counts, "results": results,
    }
    for path, content in (
        (args.json_path, json.dumps(report, indent=2, ensure_ascii=False) + "\n"),
        (args.markdown_path, markdown_report(report)),
    ):
        if path:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    print(f"Checked {len(results)} links: " + ", ".join(f"{counts[status]} {status}" for status in STATUSES) + ".")
    for item in results:
        if item["status"] != "ok":
            print(f'{item["status"].upper()} {item["http_status"] or "—"}: {item["url"]}')
    return 1 if counts["dead"] and not args.report_only else 0


if __name__ == "__main__":
    raise SystemExit(main())
