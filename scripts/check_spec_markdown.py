#!/usr/bin/env python3
"""Validate Markdown-first specification trees without creating routing state."""

from __future__ import annotations

import argparse
import re
import sys
from collections import deque
from pathlib import Path
from typing import Iterable

NODE_TYPE = re.compile(
    r"(?m)^- Node type: (root|branch|leaf|hybrid)\s*$"
)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


class CheckError(ValueError):
    """Raised when a Markdown specification tree is invalid."""


def physical_lines(text: str) -> int:
    return len(text.splitlines())


def node_type(text: str) -> str | None:
    match = NODE_TYPE.search(text)
    return match.group(1) if match else None


def local_markdown_targets(source: Path, text: str) -> list[Path]:
    targets: list[Path] = []
    for raw in MARKDOWN_LINK.findall(text):
        if "<" in raw or ">" in raw:
            continue
        value = raw.strip()
        if value.startswith("<") and value.endswith(">"):
            value = value[1:-1]
        if not value or value.startswith(("http://", "https://", "mailto:", "#")):
            continue
        value = value.split("#", 1)[0].split("?", 1)[0]
        if not value:
            continue
        target = Path(value)
        if not target.is_absolute():
            target = source.parent / target
        targets.append(target.resolve())
    return targets


def markdown_nodes(scan_roots: Iterable[Path]) -> set[Path]:
    result: set[Path] = set()
    for root in scan_roots:
        if root.is_file():
            candidates = [root]
        elif root.is_dir():
            candidates = root.rglob("*.md")
        else:
            raise CheckError(f"scan path does not exist: {root}")
        for path in candidates:
            path = path.resolve()
            if node_type(path.read_text(encoding="utf-8")):
                result.add(path)
    return result


def validate(
    roots: Iterable[Path],
    scan_roots: Iterable[Path],
    max_lines: int = 100,
    forbid_json: bool = True,
) -> dict[str, int]:
    roots = [path.resolve() for path in roots]
    scans = [path.resolve() for path in scan_roots]
    if not roots:
        raise CheckError("at least one Markdown root is required")
    if max_lines < 1:
        raise CheckError("max_lines must be positive")

    declared = markdown_nodes(scans)
    errors: list[str] = []
    reachable: set[Path] = set()
    links_checked = 0
    queue: deque[Path] = deque(roots)

    if forbid_json:
        for scan in scans:
            if scan.is_dir():
                for path in scan.rglob("*.json"):
                    errors.append(f"JSON is forbidden in Markdown node tree: {path}")

    while queue:
        source = queue.popleft()
        if source in reachable:
            continue
        if not source.is_file():
            errors.append(f"missing root or node: {source}")
            continue

        text = source.read_text(encoding="utf-8")
        kind = node_type(text)
        if not kind:
            errors.append(f"linked node does not declare Node type: {source}")
            continue

        reachable.add(source)
        count = physical_lines(text)
        if count > max_lines:
            errors.append(f"{source}: {count} lines exceeds maximum {max_lines}")

        for target in local_markdown_targets(source, text):
            links_checked += 1
            if not target.exists():
                errors.append(f"{source}: broken link to {target}")
                continue
            if target.suffix.lower() == ".md":
                target_text = target.read_text(encoding="utf-8")
                if node_type(target_text):
                    queue.append(target)

    orphans = declared - reachable
    for path in sorted(orphans):
        errors.append(f"declared node is unreachable from configured roots: {path}")

    if errors:
        raise CheckError("\n".join(errors))
    return {
        "roots": len(roots),
        "nodes": len(reachable),
        "links": links_checked,
        "max_lines": max_lines,
    }


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(
        description="Validate Markdown-only root/branch/leaf specification trees."
    )
    result.add_argument("--root", action="append", required=True, type=Path)
    result.add_argument("--scan", action="append", required=True, type=Path)
    result.add_argument("--max-lines", type=int, default=100)
    result.add_argument(
        "--allow-json",
        action="store_true",
        help="do not reject JSON below scan roots",
    )
    return result


def main() -> int:
    args = parser().parse_args()
    try:
        result = validate(
            args.root,
            args.scan,
            max_lines=args.max_lines,
            forbid_json=not args.allow_json,
        )
    except (CheckError, OSError, UnicodeError) as error:
        print(error, file=sys.stderr)
        return 1
    print(
        "valid Markdown spec tree "
        f"roots={result['roots']} nodes={result['nodes']} "
        f"links={result['links']} max_lines={result['max_lines']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
