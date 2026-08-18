#!/usr/bin/env python3
"""Inventory and verify bounded migration of a legacy specification library."""

from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import os
import re
import sys
from collections import Counter
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


SCHEMA_VERSION = 1
DEFAULT_EXTENSIONS = (".md", ".mdx", ".txt")
WORD = re.compile(r"\b[\w.-]+\b", re.UNICODE)
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
DISPOSITIONS = {
    "contract",
    "resource",
    "historical",
    "superseded",
    "duplicate",
    "deferred",
}
TERMINAL_DISPOSITIONS = DISPOSITIONS - {"deferred"}
METADATA_PATTERNS = {
    "contract_id": re.compile(
        r"(?im)^-\s*Contract(?:\s+ID)?\s*:\s*`?([^`\n]+?)`?\s*$"
    ),
    "domain_id": re.compile(
        r"(?im)^-\s*Domain(?:\s+ID)?\s*:\s*`?([^`\n]+?)`?\s*$"
    ),
    "revision": re.compile(
        r"(?im)^-\s*(?:Contract\s+revision(?:\s+or\s+epoch)?|Revision)\s*:\s*"
        r"`?([^`\n]+?)`?\s*$"
    ),
    "authority": re.compile(r"(?im)^-\s*Authority\s*:\s*([^\n]+?)\s*$"),
    "stability": re.compile(r"(?im)^-\s*Stability\s*:\s*([^\n]+?)\s*$"),
}


class MigrationError(ValueError):
    """Raised when migration state is invalid or cannot be verified."""


def count_words(text: str) -> int:
    return len(WORD.findall(text))


def normalized_extensions(values: Iterable[str]) -> tuple[str, ...]:
    result: list[str] = []
    for raw in values:
        value = raw.strip().lower()
        if not value:
            continue
        if not value.startswith("."):
            value = f".{value}"
        if value not in result:
            result.append(value)
    if not result:
        raise MigrationError("at least one file extension is required")
    return tuple(result)


def is_excluded(relative: str, patterns: Iterable[str]) -> bool:
    path = PurePosixPath(relative)
    return any(
        fnmatch.fnmatch(relative, pattern) or path.match(pattern)
        for pattern in patterns
    )


def local_links(text: str) -> list[str]:
    links: set[str] = set()
    for raw in MARKDOWN_LINK.findall(text):
        target = raw.strip()
        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1]
        if not target or target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        links.add(target)
    return sorted(links)


def declared_metadata(text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for key, pattern in METADATA_PATTERNS.items():
        match = pattern.search(text)
        if match:
            result[key] = match.group(1).strip().strip("`")
    return result


def document_record(path: Path, root: Path) -> dict[str, Any]:
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        raise MigrationError(f"{path}: specification text must be UTF-8") from error
    relative = path.relative_to(root).as_posix()
    is_markdown = path.suffix.lower() in {".md", ".mdx"}
    return {
        "path": relative,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
        "words": count_words(text),
        "headings": HEADING.findall(text) if is_markdown else [],
        "local_links": local_links(text) if is_markdown else [],
        "declared": declared_metadata(text),
    }


def build_inventory(
    source_root: Path,
    output_path: Path,
    exclusions: Iterable[str] = (),
    extensions: Iterable[str] = DEFAULT_EXTENSIONS,
) -> dict[str, Any]:
    source_root = source_root.resolve()
    output_path = output_path.resolve()
    if not source_root.is_dir():
        raise MigrationError(f"source root is not a directory: {source_root}")

    allowed = set(normalized_extensions(extensions))
    patterns = tuple(exclusions)
    documents: list[dict[str, Any]] = []
    for path in sorted(source_root.rglob("*")):
        if path.is_symlink() or not path.is_file():
            continue
        if path.suffix.lower() not in allowed or path.resolve() == output_path:
            continue
        relative = path.relative_to(source_root).as_posix()
        if is_excluded(relative, patterns):
            continue
        documents.append(document_record(path, source_root))

    canonical = json.dumps(
        documents, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    source_reference = Path(os.path.relpath(source_root, output_path.parent)).as_posix()
    return {
        "schema_version": SCHEMA_VERSION,
        "source_root": source_reference,
        "extensions": sorted(allowed),
        "excluded": list(patterns),
        "inventory_digest": hashlib.sha256(canonical).hexdigest(),
        "totals": {
            "documents": len(documents),
            "bytes": sum(item["bytes"] for item in documents),
            "words": sum(item["words"] for item in documents),
        },
        "documents": documents,
    }


def write_inventory(payload: dict[str, Any], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def load_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except OSError as error:
        raise MigrationError(f"cannot read {path}: {error}") from error
    except json.JSONDecodeError as error:
        raise MigrationError(f"{path}: invalid JSON: {error}") from error
    if not isinstance(payload, dict):
        raise MigrationError(f"{path}: expected a JSON object")
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise MigrationError(f"{path}: schema_version must be {SCHEMA_VERSION}")
    return payload


def load_inventory(path: Path) -> dict[str, Any]:
    payload = load_json(path)
    documents = payload.get("documents")
    if not isinstance(documents, list) or not all(
        isinstance(item, dict) for item in documents
    ):
        raise MigrationError(f"{path}: documents must be a list of objects")
    seen: set[str] = set()
    for item in documents:
        document_path = item.get("path")
        digest = item.get("sha256")
        if not isinstance(document_path, str) or not document_path:
            raise MigrationError(f"{path}: inventory document path is invalid")
        pure_path = PurePosixPath(document_path)
        if pure_path.is_absolute() or ".." in pure_path.parts:
            raise MigrationError(
                f"{path}: inventory path must stay below source_root: {document_path}"
            )
        if document_path in seen:
            raise MigrationError(f"{path}: duplicate inventory path: {document_path}")
        seen.add(document_path)
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise MigrationError(f"{path}: invalid SHA-256 for {document_path}")
        for key in ("bytes", "words"):
            if not isinstance(item.get(key), int) or item[key] < 0:
                raise MigrationError(f"{path}: invalid {key} for {document_path}")

    canonical = json.dumps(
        documents, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    expected_digest = hashlib.sha256(canonical).hexdigest()
    if payload.get("inventory_digest") != expected_digest:
        raise MigrationError(f"{path}: inventory_digest does not match documents")
    expected_totals = {
        "documents": len(documents),
        "bytes": sum(item["bytes"] for item in documents),
        "words": sum(item["words"] for item in documents),
    }
    if payload.get("totals") != expected_totals:
        raise MigrationError(f"{path}: inventory totals do not match documents")
    return payload


def load_mapping_entries(mapping_dir: Path) -> list[tuple[Path, dict[str, Any]]]:
    if not mapping_dir.is_dir():
        raise MigrationError(f"mapping directory is not a directory: {mapping_dir}")
    entries: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(mapping_dir.rglob("*.json")):
        payload = load_json(path)
        batch_id = payload.get("batch_id")
        documents = payload.get("documents")
        if not isinstance(batch_id, str) or not batch_id.strip():
            raise MigrationError(f"{path}: batch_id must be a non-empty string")
        if not isinstance(documents, list) or not all(
            isinstance(item, dict) for item in documents
        ):
            raise MigrationError(f"{path}: documents must be a list of objects")
        entries.extend((path, item) for item in documents)
    return entries


def entry_errors(path: Path, entry: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    source = entry.get("path")
    disposition = entry.get("disposition")
    if not isinstance(source, str) or not source:
        return [f"{path}: mapping entry requires a non-empty path"]
    if disposition not in DISPOSITIONS:
        errors.append(f"{path}: {source} has invalid disposition: {disposition}")
    if disposition in {"contract", "resource"}:
        node_id = entry.get("node_id")
        if not isinstance(node_id, str) or not node_id.strip():
            errors.append(f"{path}: {source} disposition {disposition} requires node_id")
    if disposition in {"duplicate", "superseded"}:
        canonical = entry.get("canonical_path")
        if not isinstance(canonical, str) or not canonical.strip():
            errors.append(
                f"{path}: {source} disposition {disposition} requires canonical_path"
            )
    target = entry.get("target")
    if target is not None and (not isinstance(target, str) or not target.strip()):
        errors.append(f"{path}: {source} target must be a non-empty string")
    return errors


def analyze_coverage(
    inventory: dict[str, Any], entries: list[tuple[Path, dict[str, Any]]]
) -> dict[str, Any]:
    inventory_paths = {item["path"] for item in inventory["documents"]}
    mapped: dict[str, list[tuple[Path, dict[str, Any]]]] = {}
    invalid: list[str] = []
    unknown: list[str] = []
    dispositions: Counter[str] = Counter()

    for source_file, entry in entries:
        invalid.extend(entry_errors(source_file, entry))
        source = entry.get("path")
        if not isinstance(source, str) or not source:
            continue
        mapped.setdefault(source, []).append((source_file, entry))
        if source not in inventory_paths:
            unknown.append(f"{source_file}: unknown inventory path: {source}")
        disposition = entry.get("disposition")
        if disposition in DISPOSITIONS:
            dispositions[disposition] += 1

    duplicate_mappings = {
        source: values for source, values in mapped.items() if len(values) > 1
    }
    known_mapped = set(mapped) & inventory_paths
    deferred = {
        source
        for source, values in mapped.items()
        if source in inventory_paths
        and any(item.get("disposition") == "deferred" for _, item in values)
    }
    terminal = {
        source
        for source, values in mapped.items()
        if source in inventory_paths
        and len(values) == 1
        and values[0][1].get("disposition") in TERMINAL_DISPOSITIONS
    }
    return {
        "total": len(inventory_paths),
        "mapped": len(known_mapped),
        "terminal": len(terminal),
        "deferred": len(deferred),
        "unclassified": len(inventory_paths - known_mapped),
        "dispositions": dispositions,
        "duplicate_mappings": duplicate_mappings,
        "unknown": unknown,
        "invalid": invalid,
    }


def render_status(inventory: dict[str, Any], coverage: dict[str, Any]) -> str:
    totals = inventory.get("totals", {})
    disposition_text = ", ".join(
        f"{name}={coverage['dispositions'].get(name, 0)}"
        for name in sorted(DISPOSITIONS)
    )
    return "\n".join(
        [
            f"inventory documents={coverage['total']} words={totals.get('words', 0)} "
            f"digest={inventory.get('inventory_digest', 'unknown')}",
            f"coverage mapped={coverage['mapped']} terminal={coverage['terminal']} "
            f"deferred={coverage['deferred']} unclassified={coverage['unclassified']}",
            f"dispositions {disposition_text}",
            f"problems duplicate_mappings={len(coverage['duplicate_mappings'])} "
            f"unknown={len(coverage['unknown'])} invalid={len(coverage['invalid'])}",
        ]
    ) + "\n"


def verify_sources(
    inventory: dict[str, Any], inventory_path: Path, source_override: Path | None
) -> list[str]:
    if source_override is None:
        source_value = inventory.get("source_root")
        if not isinstance(source_value, str) or not source_value:
            raise MigrationError(f"{inventory_path}: source_root is missing")
        source_root = (inventory_path.parent / source_value).resolve()
    else:
        source_root = source_override.resolve()
    if not source_root.is_dir():
        return [f"source root is not a directory: {source_root}"]

    errors: list[str] = []
    for item in inventory["documents"]:
        path = source_root / item["path"]
        if not path.is_file():
            errors.append(f"missing source: {item['path']}")
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != item["sha256"]:
            errors.append(f"source hash drift: {item['path']}")
    return errors


def verification_errors(
    inventory: dict[str, Any],
    inventory_path: Path,
    coverage: dict[str, Any],
    source_override: Path | None,
    require_complete: bool,
) -> list[str]:
    errors = [*coverage["invalid"], *coverage["unknown"]]
    for source, values in sorted(coverage["duplicate_mappings"].items()):
        locations = ", ".join(str(path) for path, _ in values)
        errors.append(f"duplicate mapping for {source}: {locations}")
    errors.extend(verify_sources(inventory, inventory_path, source_override))
    if require_complete:
        if coverage["unclassified"]:
            errors.append(
                f"migration incomplete: {coverage['unclassified']} unclassified documents"
            )
        if coverage["deferred"]:
            errors.append(
                f"migration incomplete: {coverage['deferred']} deferred documents"
            )
        if coverage["terminal"] != coverage["total"]:
            errors.append(
                "migration incomplete: terminal coverage does not equal inventory"
            )
    return errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    inventory_parser = subparsers.add_parser(
        "inventory", help="create a deterministic metadata inventory"
    )
    inventory_parser.add_argument("source_root", type=Path)
    inventory_parser.add_argument("--output", type=Path, required=True)
    inventory_parser.add_argument("--exclude", action="append", default=[])
    inventory_parser.add_argument(
        "--extension",
        action="append",
        dest="extensions",
        help="included extension; repeat for multiple values",
    )

    for name in ("status", "verify"):
        command_parser = subparsers.add_parser(name)
        command_parser.add_argument("inventory", type=Path)
        command_parser.add_argument("--mapping-dir", type=Path, required=True)
        if name == "verify":
            command_parser.add_argument("--source-root", type=Path)
            command_parser.add_argument("--require-complete", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "inventory":
            extensions = args.extensions or DEFAULT_EXTENSIONS
            payload = build_inventory(
                args.source_root, args.output, args.exclude, extensions
            )
            write_inventory(payload, args.output)
            print(
                f"inventory written: {args.output} "
                f"documents={payload['totals']['documents']} "
                f"words={payload['totals']['words']}"
            )
            return 0

        inventory_path = args.inventory.resolve()
        inventory = load_inventory(inventory_path)
        entries = load_mapping_entries(args.mapping_dir.resolve())
        coverage = analyze_coverage(inventory, entries)
        sys.stdout.write(render_status(inventory, coverage))
        if args.command == "status":
            return 0

        errors = verification_errors(
            inventory,
            inventory_path,
            coverage,
            args.source_root,
            args.require_complete,
        )
        if errors:
            for error in errors:
                print(error, file=sys.stderr)
            return 1
        print("migration verification passed")
        return 0
    except MigrationError as error:
        print(error, file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
