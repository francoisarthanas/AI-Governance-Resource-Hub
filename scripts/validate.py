#!/usr/bin/env python3
"""Validate repository structure, local links, the resource catalog, and control CSV."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
REQUIRED_FILES = {
    "README.md",
    "CONTRIBUTING.md",
    "LICENSE",
    "catalog/resources.json",
    "catalog/control-baseline.csv",
    "docs/START-HERE.md",
    "docs/AGENTIC-AI-GOVERNANCE.md",
    "docs/IMPLEMENTATION-PLAYBOOK.md",
    "templates/ai-inventory.csv",
    "templates/ai-impact-assessment.md",
    "templates/agentic-risk-assessment.md",
    "templates/go-live-checklist.md",
    "templates/ai-incident-report.md",
}
RESOURCE_FIELDS = {
    "id",
    "title",
    "url",
    "publisher",
    "tier",
    "type",
    "access",
    "focus",
    "why",
    "use",
}
CONTROL_FIELDS = {
    "id",
    "domain",
    "objective",
    "applies_to",
    "minimum_evidence",
    "nist_ai_rmf",
    "primary_owner",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_structure(errors: list[str]) -> None:
    for relative in sorted(REQUIRED_FILES):
        if not (ROOT / relative).is_file():
            fail(errors, f"missing required file: {relative}")


def validate_catalog(errors: list[str]) -> int:
    path = ROOT / "catalog/resources.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"cannot parse catalog/resources.json: {exc}")
        return 0

    resources = data.get("resources")
    if not isinstance(resources, list) or not resources:
        fail(errors, "catalog resources must be a non-empty list")
        return 0

    seen_ids: set[str] = set()
    seen_urls: set[str] = set()
    for index, resource in enumerate(resources, start=1):
        label = resource.get("id", f"entry-{index}") if isinstance(resource, dict) else f"entry-{index}"
        if not isinstance(resource, dict):
            fail(errors, f"{label}: resource must be an object")
            continue
        missing = RESOURCE_FIELDS - resource.keys()
        if missing:
            fail(errors, f"{label}: missing fields {sorted(missing)}")
        resource_id = resource.get("id")
        if not isinstance(resource_id, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", resource_id):
            fail(errors, f"{label}: invalid id")
        elif resource_id in seen_ids:
            fail(errors, f"{label}: duplicate id")
        else:
            seen_ids.add(resource_id)
        url = resource.get("url")
        if not isinstance(url, str) or urlsplit(url).scheme != "https" or not urlsplit(url).netloc:
            fail(errors, f"{label}: URL must be an absolute HTTPS URL")
        elif url in seen_urls:
            fail(errors, f"{label}: duplicate URL")
        else:
            seen_urls.add(url)
        if resource.get("tier") not in {"essential", "core", "deep-dive"}:
            fail(errors, f"{label}: invalid tier")
        if resource.get("access") not in {"free", "paid", "freemium", "mixed"}:
            fail(errors, f"{label}: invalid access")
        focus = resource.get("focus")
        if not isinstance(focus, list) or not focus or not all(isinstance(item, str) and item for item in focus):
            fail(errors, f"{label}: focus must be a non-empty string list")
        for field in ("title", "publisher", "type", "why", "use"):
            if not isinstance(resource.get(field), str) or not resource[field].strip():
                fail(errors, f"{label}: {field} must be a non-empty string")
    return len(resources)


def validate_controls(errors: list[str]) -> int:
    path = ROOT / "catalog/control-baseline.csv"
    try:
        with path.open(encoding="utf-8", newline="") as stream:
            reader = csv.DictReader(stream)
            rows = list(reader)
            fields = set(reader.fieldnames or [])
    except OSError as exc:
        fail(errors, f"cannot read control baseline: {exc}")
        return 0
    if fields != CONTROL_FIELDS:
        fail(errors, f"control baseline fields differ: found {sorted(fields)}")
    if not rows:
        fail(errors, "control baseline is empty")
        return 0
    seen: set[str] = set()
    for line, row in enumerate(rows, start=2):
        control_id = (row.get("id") or "").strip()
        if not re.fullmatch(r"[A-Z]{3,4}-\d{2}", control_id):
            fail(errors, f"control line {line}: invalid id {control_id!r}")
        elif control_id in seen:
            fail(errors, f"control line {line}: duplicate id {control_id}")
        else:
            seen.add(control_id)
        for field in CONTROL_FIELDS:
            if not (row.get(field) or "").strip():
                fail(errors, f"control {control_id or line}: blank {field}")
    return len(rows)


def validate_local_links(errors: list[str]) -> int:
    checked = 0
    for markdown in sorted(ROOT.rglob("*.md")):
        text = markdown.read_text(encoding="utf-8")
        for raw in LINK_RE.findall(text):
            target = raw.strip().split(maxsplit=1)[0].strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme in {"http", "https", "mailto"} or target.startswith("#"):
                continue
            if parsed.scheme:
                continue
            relative = unquote(parsed.path)
            if not relative:
                continue
            checked += 1
            destination = (markdown.parent / relative).resolve()
            try:
                destination.relative_to(ROOT)
            except ValueError:
                fail(errors, f"{markdown.relative_to(ROOT)}: link escapes repository: {target}")
                continue
            if not destination.exists():
                fail(errors, f"{markdown.relative_to(ROOT)}: missing local link target: {target}")
    return checked


def main() -> int:
    errors: list[str] = []
    validate_structure(errors)
    resources = validate_catalog(errors)
    controls = validate_controls(errors)
    local_links = validate_local_links(errors)
    if errors:
        print(f"Validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Validation passed: {resources} resources, {controls} controls, {local_links} local links checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
