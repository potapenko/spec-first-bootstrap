#!/usr/bin/env python3
"""Validate Markdown-first specification trees without creating routing state."""

from __future__ import annotations

import argparse
import re
import sys
from collections import deque
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote

NODE_TYPE = re.compile(
    r"(?m)^- Node type: (root|branch|leaf|hybrid)\s*$"
)
STATUS = re.compile(r"(?m)^- Status: \S.*$")
READ_WHEN = re.compile(r"(?m)^- Read when: \S.*$")
DO_NOT_READ_WHEN = re.compile(r"(?m)^- Do not read when: \S.*$")
MAXIMUM_SIZE = re.compile(r"(?m)^- Maximum size: (\d+) physical lines\.\s*$")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")


class CheckError(ValueError):
    """Raised when a Markdown specification tree is invalid."""


def physical_lines(text: str) -> int:
    return len(text.splitlines())


def node_type(text: str) -> str | None:
    match = NODE_TYPE.search(text)
    return match.group(1) if match else None


def local_markdown_targets(source: Path, text: str) -> list[tuple[Path, str]]:
    targets: list[tuple[Path, str]] = []
    for raw in MARKDOWN_LINK.findall(text):
        value = raw.strip()
        if value.startswith("<") and value.endswith(">"):
            value = value[1:-1]
        if not value or value.startswith(("http://", "https://", "mailto:")):
            continue
        path_value, separator, fragment = value.partition("#")
        path_value = path_value.split("?", 1)[0]
        target = Path(unquote(path_value)) if path_value else source
        if not target.is_absolute():
            target = source.parent / target
        targets.append((target.resolve(), unquote(fragment) if separator else ""))
    return targets


def heading_anchors(text: str) -> set[str]:
    """Return the GitHub-style anchors needed for local heading validation."""
    anchors: set[str] = set()
    counts: dict[str, int] = {}
    for line in text.splitlines():
        match = HEADING.match(line)
        if not match:
            continue
        title = re.sub(r"[`*_~]", "", match.group(2)).strip().lower()
        title = re.sub(r"[^\w\- ]", "", title, flags=re.UNICODE)
        base = re.sub(r"\s+", "-", title)
        occurrence = counts.get(base, 0)
        counts[base] = occurrence + 1
        anchors.add(base if occurrence == 0 else f"{base}-{occurrence}")
    return anchors


def dependency_section_text(text: str) -> str:
    """Return content below level-two Dependency headings only."""
    selected: list[str] = []
    active = False
    for line in text.splitlines():
        heading = HEADING.match(line)
        if heading and len(heading.group(1)) <= 2:
            active = bool(
                len(heading.group(1)) == 2
                and re.match(r"dependenc(?:y|ies)\b", heading.group(2), re.IGNORECASE)
            )
            continue
        if active:
            selected.append(line)
    return "\n".join(selected)


def dependency_cycle(
    declared: set[Path], texts: dict[Path, str]
) -> list[Path] | None:
    graph: dict[Path, list[Path]] = {}
    for source in declared:
        targets = local_markdown_targets(
            source, dependency_section_text(texts[source])
        )
        graph[source] = [target for target, _ in targets if target in declared]

    visiting: set[Path] = set()
    visited: set[Path] = set()
    stack: list[Path] = []

    def visit(source: Path) -> list[Path] | None:
        if source in visiting:
            index = stack.index(source)
            return stack[index:] + [source]
        if source in visited:
            return None
        visiting.add(source)
        stack.append(source)
        for target in graph[source]:
            found = visit(target)
            if found:
                return found
        stack.pop()
        visiting.remove(source)
        visited.add(source)
        return None

    for source in sorted(declared):
        found = visit(source)
        if found:
            return found
    return None


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
    texts = {path: path.read_text(encoding="utf-8") for path in declared}
    errors: list[str] = []
    reachable: set[Path] = set()
    links_checked = 0
    queue: deque[Path] = deque(roots)

    if forbid_json:
        for scan in scans:
            if scan.is_dir():
                for path in scan.rglob("*.json"):
                    errors.append(f"JSON is forbidden in Markdown node tree: {path}")

    for path in sorted(declared):
        text = texts[path]
        for label, pattern in (
            ("Status", STATUS),
            ("Read when", READ_WHEN),
            ("Do not read when", DO_NOT_READ_WHEN),
        ):
            if not pattern.search(text):
                errors.append(f"{path}: missing required node metadata: {label}")
        declared_maximum = MAXIMUM_SIZE.search(text)
        if not declared_maximum:
            errors.append(f"{path}: missing required node metadata: Maximum size")
        else:
            declared_limit = int(declared_maximum.group(1))
            if declared_limit > max_lines:
                errors.append(
                    f"{path}: declared maximum {declared_limit} exceeds configured maximum {max_lines}"
                )
            count = physical_lines(text)
            if count > declared_limit:
                errors.append(
                    f"{path}: {count} lines exceeds declared maximum {declared_limit}"
                )

    cycle = dependency_cycle(declared, texts)
    if cycle:
        errors.append(
            "dependency cycle: " + " -> ".join(str(path) for path in cycle)
        )

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
        for target, fragment in local_markdown_targets(source, text):
            links_checked += 1
            if not target.exists():
                errors.append(f"{source}: broken link to {target}")
                continue
            if fragment and target.suffix.lower() == ".md":
                target_text = target.read_text(encoding="utf-8")
                if fragment not in heading_anchors(target_text):
                    errors.append(
                        f"{source}: broken heading anchor #{fragment} in {target}"
                    )
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
