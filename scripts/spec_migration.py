#!/usr/bin/env python3
"""Mechanical census and Markdown-batch coverage for legacy spec migration."""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import re
import sys
from collections import Counter
from pathlib import Path, PurePosixPath
from typing import Iterable

DEFAULT_EXTENSIONS = (".md", ".mdx", ".txt")
WORD = re.compile(r"\b[\w.-]+\b", re.UNICODE)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


class MigrationError(ValueError):
    """Raised when migration input or Markdown coverage is invalid."""


def extensions(values: Iterable[str]) -> tuple[str, ...]:
    result: list[str] = []
    for raw in values:
        value = raw.lower().strip()
        if not value:
            continue
        if not value.startswith("."):
            value = f".{value}"
        if value not in result:
            result.append(value)
    if not result:
        raise MigrationError("at least one extension is required")
    return tuple(result)


def excluded(relative: str, patterns: Iterable[str]) -> bool:
    path = PurePosixPath(relative)
    return any(
        fnmatch.fnmatch(relative, pattern) or path.match(pattern)
        for pattern in patterns
    )


def source_files(
    root: Path,
    patterns: Iterable[str],
    allowed: Iterable[str],
) -> list[Path]:
    root = root.resolve()
    if not root.is_dir():
        raise MigrationError(f"source root is not a directory: {root}")
    suffixes = set(allowed)
    result: list[Path] = []
    for path in sorted(root.rglob("*")):
        if path.is_symlink() or not path.is_file():
            continue
        if path.suffix.lower() not in suffixes:
            continue
        relative = path.relative_to(root).as_posix()
        if not excluded(relative, patterns):
            result.append(path)
    return result


def fingerprint(path: Path) -> tuple[int, int, int, str]:
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    return (
        len(raw),
        len(WORD.findall(text)),
        len(text.splitlines()),
        hashlib.sha256(raw).hexdigest(),
    )


def local_links(source: Path) -> list[Path]:
    text = source.read_text(encoding="utf-8")
    result: list[Path] = []
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
        path = Path(value)
        if not path.is_absolute():
            path = source.parent / path
        result.append(path.resolve())
    return result


def census(args: argparse.Namespace) -> int:
    root = args.source_root.resolve()
    allowed = extensions(args.extension)
    files = source_files(root, args.exclude, allowed)
    totals = Counter()
    oversized: list[tuple[int, str]] = []
    for path in files:
        size, words, lines, _ = fingerprint(path)
        totals.update(bytes=size, words=words, lines=lines)
        if lines > args.max_lines:
            oversized.append((lines, path.relative_to(root).as_posix()))

    print(
        f"census documents={len(files)} words={totals['words']} "
        f"lines={totals['lines']} oversized={len(oversized)}"
    )
    for lines, relative in sorted(oversized, reverse=True)[: args.show_oversized]:
        print(f"oversized lines={lines} path={relative}")
    return 0


def coverage(args: argparse.Namespace) -> int:
    root = args.source_root.resolve()
    batch_root = args.batch_root.resolve()
    allowed = extensions(args.extension)
    files = source_files(root, args.exclude, allowed)
    expected = {path.resolve() for path in files}

    if not batch_root.is_dir():
        raise MigrationError(f"batch root is not a directory: {batch_root}")

    mapped: Counter[Path] = Counter()
    unknown: set[Path] = set()
    batch_files = sorted(batch_root.rglob("*.md"))
    for batch in batch_files:
        for target in local_links(batch):
            if target in expected:
                mapped[target] += 1
            elif target.suffix.lower() in set(allowed) and target.is_file():
                unknown.add(target)

    missing = expected - set(mapped)
    duplicates = {path for path, count in mapped.items() if count > 1}
    print(
        f"coverage sources={len(expected)} mapped={len(mapped)} "
        f"missing={len(missing)} duplicates={len(duplicates)} "
        f"unknown={len(unknown)} batches={len(batch_files)}"
    )
    for path in sorted(missing)[: args.show_problems]:
        print(f"missing {path.relative_to(root).as_posix()}")
    for path in sorted(duplicates)[: args.show_problems]:
        print(f"duplicate {path.relative_to(root).as_posix()}")
    if args.require_complete and (missing or duplicates or unknown):
        raise MigrationError("Markdown migration coverage is incomplete")
    return 0


def build_parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser(
        description="Inspect legacy specs without committed machine routing state."
    )
    subparsers = result.add_subparsers(dest="command", required=True)

    census_parser = subparsers.add_parser("census")
    census_parser.add_argument("source_root", type=Path)
    census_parser.add_argument("--exclude", action="append", default=[])
    census_parser.add_argument(
        "--extension", action="append", default=list(DEFAULT_EXTENSIONS)
    )
    census_parser.add_argument("--max-lines", type=int, default=100)
    census_parser.add_argument("--show-oversized", type=int, default=10)
    census_parser.set_defaults(handler=census)

    coverage_parser = subparsers.add_parser("coverage")
    coverage_parser.add_argument("source_root", type=Path)
    coverage_parser.add_argument("--batch-root", required=True, type=Path)
    coverage_parser.add_argument("--exclude", action="append", default=[])
    coverage_parser.add_argument(
        "--extension", action="append", default=list(DEFAULT_EXTENSIONS)
    )
    coverage_parser.add_argument("--require-complete", action="store_true")
    coverage_parser.add_argument("--show-problems", type=int, default=10)
    coverage_parser.set_defaults(handler=coverage)
    return result


def main() -> int:
    args = build_parser().parse_args()
    try:
        return args.handler(args)
    except (MigrationError, OSError, UnicodeError) as error:
        print(error, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
