#!/usr/bin/env python3
"""Validate catalog metadata, resources, generated-page anchors, and local links."""

from __future__ import annotations

import argparse
from datetime import date
import html
import json
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit, urlunsplit

from generate_catalog import CATEGORIES

ROOT = Path(__file__).resolve().parents[1]
RESOURCE_FIELDS = {
    "id", "title", "url", "publisher", "category", "format", "access", "audience",
    "why", "use", "version", "verification_note", "last_reviewed",
}
REQUIRED_FILES = {
    "README.md", "CONTRIBUTING.md", "LICENSE", "catalog/resources.json", "docs/START-HERE.md",
    *("docs/" + details[0] for details in CATEGORIES.values()),
}
LABEL_RE = re.compile(r"!?\[((?:[^\[\]\n]|\[[^\]\n]*\])*)\]")
DEFINITION_RE = re.compile(r"^ {0,3}\[([^\]]+)\]:\s*(<[^>]+>|\S+)", re.MULTILINE)


def without_code(text: str, *, strip_inline: bool = True) -> str:
    """Mask fenced and inline code so example links are not treated as navigation."""
    lines = []
    fence = None
    for line in text.splitlines(keepends=True):
        match = re.match(r"^ {0,3}(`{3,}|~{3,})", line)
        if fence:
            if match and match.group(1)[0] == fence[0] and len(match.group(1)) >= len(fence):
                fence = None
            lines.append("\n")
        elif match:
            fence = match.group(1)
            lines.append("\n")
        else:
            lines.append(line)
    return re.sub(r"(`+)(.+?)\1", "" if strip_inline else r"\2", "".join(lines))


def reference_key(label: str) -> str:
    return " ".join(label.split()).casefold()


def inline_destination(text: str, start: int) -> str | None:
    """Read a Markdown destination, including angle brackets and balanced parentheses."""
    cursor = start
    while cursor < len(text) and text[cursor].isspace():
        cursor += 1
    if cursor < len(text) and text[cursor] == "<":
        end = text.find(">", cursor + 1)
        return text[cursor + 1:end] if end >= 0 else None
    depth, chars = 0, []
    while cursor < len(text):
        char = text[cursor]
        if char == "\\" and cursor + 1 < len(text):
            chars.append(text[cursor + 1])
            cursor += 2
            continue
        if char == "(" :
            depth += 1
        elif char == ")":
            if depth == 0:
                return "".join(chars)
            depth -= 1
        elif char.isspace() and depth == 0:
            return "".join(chars)
        chars.append(char)
        cursor += 1
    return None


def markdown_targets(text: str) -> tuple[list[str], list[str]]:
    text = without_code(text)
    definitions = {reference_key(m.group(1)): m.group(2).strip("<>") for m in DEFINITION_RE.finditer(text)}
    targets = list(definitions.values())
    missing = []
    text = DEFINITION_RE.sub("", text)
    for match in LABEL_RE.finditer(text):
        tail = text[match.end():]
        if tail.startswith("("):
            target = inline_destination(text, match.end() + 1)
            if target is not None:
                targets.append(target)
        elif tail.startswith("["):
            end = tail.find("]")
            if end >= 0:
                label = tail[1:end] or match.group(1)
                key = reference_key(label)
                if key in definitions:
                    targets.append(definitions[key])
                else:
                    missing.append(label)
        elif reference_key(match.group(1)) in definitions:
            targets.append(definitions[reference_key(match.group(1))])
    targets.extend(html.unescape(m.group(2)) for m in re.finditer(r"\b(?:href|src)\s*=\s*(['\"])(.*?)\1", text, re.I))
    return targets, missing


def anchors_in(text: str) -> set[str]:
    text = without_code(text, strip_inline=False)
    anchors = {html.unescape(m.group(2)) for m in re.finditer(r"\b(?:id|name)\s*=\s*(['\"])(.*?)\1", text, re.I)}
    seen: dict[str, int] = {}
    lines = text.splitlines()
    headings = []
    for index, line in enumerate(lines):
        match = re.match(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            headings.append(match.group(1))
        elif index > 0 and re.fullmatch(r" {0,3}(?:=+|-+)\s*", line) and lines[index - 1].strip():
            headings.append(lines[index - 1].strip())
    for heading in headings:
        heading = re.sub(r"!?\[([^\]]+)\]\([^)]*\)", r"\1", heading)
        heading = html.unescape(re.sub(r"<[^>]*>", "", heading)).lower()
        slug = "".join(c for c in heading if c in " -_" or unicodedata.category(c)[0] in "LNM").replace(" ", "-")
        count = seen.get(slug, 0)
        candidate = slug if count == 0 else f"{slug}-{count}"
        while candidate in anchors:
            count += 1
            candidate = f"{slug}-{count}"
        seen[slug] = count + 1
        anchors.add(candidate)
    return anchors


def canonical_url(url: str) -> str:
    parsed = urlsplit(url)
    hostname = (parsed.hostname or "").lower()
    port = parsed.port
    authority = hostname if port in (None, 443) else f"{hostname}:{port}"
    return urlunsplit((parsed.scheme.lower(), authority, parsed.path.rstrip("/"), parsed.query, ""))


def valid_date(value: object) -> bool:
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        return date.fromisoformat(value) <= date.today()
    except ValueError:
        return False


def validate_catalog(root: Path, errors: list[str]) -> int:
    try:
        data = json.loads((root / "catalog/resources.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"cannot parse catalog/resources.json: {exc}")
        return 0
    if not isinstance(data, dict):
        errors.append("catalog must be an object")
        return 0
    if data.get("schema_version") != "2.0":
        errors.append('catalog schema_version must be "2.0"')
    if not valid_date(data.get("last_reviewed")):
        errors.append("catalog last_reviewed must be a real YYYY-MM-DD date no later than today")
    resources = data.get("resources")
    if not isinstance(resources, list) or not resources:
        errors.append("catalog resources must be a non-empty list")
        return 0
    ids, urls = set(), set()
    for number, item in enumerate(resources, start=1):
        label = f"resource {number}"
        if not isinstance(item, dict):
            errors.append(f"{label}: must be an object")
            continue
        for field in sorted(RESOURCE_FIELDS):
            if not isinstance(item.get(field), str) or not item[field].strip():
                errors.append(f"{label}: {field} must be a non-empty string")
        extras = item.keys() - RESOURCE_FIELDS - {"starter"}
        if extras:
            errors.append(f"{label}: unsupported fields {sorted(extras)}")
        resource_id = item.get("id")
        if not isinstance(resource_id, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", resource_id):
            errors.append(f"{label}: invalid id")
        elif resource_id in ids:
            errors.append(f"{resource_id}: duplicate id")
        else:
            ids.add(resource_id)
            label = resource_id
        if "starter" in item and not isinstance(item["starter"], bool):
            errors.append(f"{label}: starter must be a boolean")
        category = item.get("category")
        if not isinstance(category, str) or category not in CATEGORIES:
            errors.append(f"{label}: unknown category {category!r}")
        if not valid_date(item.get("last_reviewed")):
            errors.append(f"{label}: last_reviewed must be a real YYYY-MM-DD date no later than today")
        elif valid_date(data.get("last_reviewed")) and item["last_reviewed"] > data["last_reviewed"]:
            errors.append(f"{label}: review date is later than catalog last_reviewed")
        url = item.get("url")
        try:
            parsed = urlsplit(url) if isinstance(url, str) else None
            if not parsed or parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password or re.search(r"\s", url):
                raise ValueError("invalid URL")
            normalized = canonical_url(url)
            if normalized in urls:
                errors.append(f"{label}: duplicate canonical URL {normalized}")
            urls.add(normalized)
        except ValueError:
            errors.append(f"{label}: url must be an absolute HTTPS URL without credentials or whitespace")
        if isinstance(category, str) and category in CATEGORIES and isinstance(resource_id, str):
            page = root / "docs" / CATEGORIES[category][0]
            if page.is_file():
                content = page.read_text(encoding="utf-8")
                marker = f'<a id="{resource_id}"></a>'
                if marker not in content:
                    errors.append(f"{label}: missing explicit anchor in docs/{page.name}")
                else:
                    section = content.split(marker, 1)[1].split('<a id="', 1)[0]
                    targets, _ = markdown_targets(section)
                    if url not in targets:
                        errors.append(f"{label}: official URL missing from its category-page section")
    return len(resources)


def validate_local_links(root: Path, errors: list[str]) -> int:
    count = 0
    cache: dict[Path, set[str]] = {}
    for markdown in sorted(root.rglob("*.md")):
        if any(part in {".git", "node_modules", ".venv"} for part in markdown.relative_to(root).parts):
            continue
        targets, missing = markdown_targets(markdown.read_text(encoding="utf-8"))
        label = markdown.relative_to(root)
        for reference in missing:
            errors.append(f"{label}: undefined link reference [{reference}]")
        for target in targets:
            try:
                parsed = urlsplit(html.unescape(target))
            except ValueError:
                errors.append(f"{label}: malformed link target {target!r}")
                continue
            if parsed.scheme or parsed.netloc:
                continue
            count += 1
            path = unquote(parsed.path)
            destination = (root / path.lstrip("/") if path.startswith("/") else markdown.parent / path).resolve() if path else markdown
            try:
                destination.relative_to(root)
            except ValueError:
                errors.append(f"{label}: link escapes repository: {target}")
                continue
            if not destination.exists():
                errors.append(f"{label}: missing local link target: {target}")
                continue
            if parsed.fragment and destination.is_dir():
                readme = destination / "README.md"
                if readme.is_file():
                    destination = readme
            if parsed.fragment and destination.suffix.lower() in {".md", ".html", ".htm"}:
                if destination not in cache:
                    cache[destination] = anchors_in(destination.read_text(encoding="utf-8"))
                fragment = unquote(parsed.fragment)
                if fragment not in cache[destination]:
                    errors.append(f"{label}: missing local anchor: {target}")
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root")
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    for relative in sorted(REQUIRED_FILES):
        if not (root / relative).is_file():
            errors.append(f"missing required file: {relative}")
    resource_count = validate_catalog(root, errors)
    link_count = validate_local_links(root, errors)
    if errors:
        print(f"Validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Validation passed: {resource_count} resources and {link_count} local links/anchors checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
