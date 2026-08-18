#!/usr/bin/env python3
"""Validate hierarchical spec routes and resolve a minimal contract closure."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable


WORD = re.compile(r"\b[\w.-]+\b", re.UNICODE)
AUTHORITY = {"Draft", "Active", "Superseded", "Historical"}
STABILITY = {"Evolving", "Accepted", "Released", "Deprecated"}


class RouteError(ValueError):
    """Raised when a route tree is invalid or cannot be resolved."""


@dataclass(frozen=True)
class Contract:
    path: Path
    revision: str
    clauses: tuple[str, ...]
    context_budget_words: int
    authority: str
    stability: str
    baseline: str


@dataclass(frozen=True)
class Resource:
    path: Path
    role: str
    revision: str
    context_budget_words: int


@dataclass
class Node:
    node_id: str
    summary: str
    read_when: tuple[str, ...]
    do_not_read_when: tuple[str, ...]
    manifest: Path
    contract: Contract | None = None
    resources: tuple[Resource, ...] = ()
    route: Path | None = None
    requires: tuple[dict[str, Any], ...] = ()
    precedence: tuple[str, ...] = ()
    parent_id: str | None = None
    children: list[str] = field(default_factory=list)


@dataclass
class RouteGraph:
    root_manifest: Path
    root_id: str
    nodes: dict[str, Node]
    manifests: set[Path]
    manifest_revisions: dict[Path, str]
    profiles: dict[str, tuple[str, ...]]

    def validate(self) -> None:
        errors: list[str] = []
        clause_owners: dict[str, str] = {}
        for profile, node_ids in self.profiles.items():
            for node_id in node_ids:
                if node_id not in self.nodes:
                    errors.append(f"profile {profile}: unknown node: {node_id}")
        for node in self.nodes.values():
            if not node.read_when:
                errors.append(f"{node.node_id}: read_when must not be empty")
            if not node.do_not_read_when:
                errors.append(f"{node.node_id}: do_not_read_when must not be empty")
            if not node.contract and not node.resources and not node.children:
                errors.append(
                    f"{node.node_id}: node has neither contract, resources, nor children"
                )
            if node.contract:
                contract = node.contract
                for clause in contract.clauses:
                    owner = clause_owners.get(clause)
                    if owner:
                        errors.append(
                            f"duplicate clause ID {clause}: {owner} and {node.node_id}"
                        )
                    else:
                        clause_owners[clause] = node.node_id
                if not contract.path.is_file():
                    errors.append(
                        f"{node.node_id}: missing contract: "
                        f"{contract.path.relative_to(self.root_manifest.parent)}"
                    )
                else:
                    contract_text = contract.path.read_text(encoding="utf-8")
                    words = count_words(contract_text)
                    if words > contract.context_budget_words:
                        errors.append(
                            f"{node.node_id}: contract uses {words} words, exceeds "
                            f"budget {contract.context_budget_words}"
                        )
                    if contract.revision not in contract_text:
                        errors.append(
                            f"{node.node_id}: contract file does not declare revision "
                            f"{contract.revision}"
                        )
                    for clause in contract.clauses:
                        if clause not in contract_text:
                            errors.append(
                                f"{node.node_id}: contract file does not declare clause "
                                f"{clause}"
                            )
            for resource in node.resources:
                if not resource.path.is_file():
                    errors.append(
                        f"{node.node_id}: missing {resource.role} resource: "
                        f"{relative(resource.path, self.root_manifest.parent)}"
                    )
                else:
                    words = count_words(resource.path.read_text(encoding="utf-8"))
                    if words > resource.context_budget_words:
                        errors.append(
                            f"{node.node_id}: {resource.role} resource uses {words} "
                            f"words, exceeds budget {resource.context_budget_words}"
                        )
            for dependency in node.requires:
                target = dependency.get("node_id")
                if target not in self.nodes:
                    errors.append(f"{node.node_id}: unknown dependency: {target}")
                clauses = dependency.get("clauses")
                reason = dependency.get("reason")
                if not isinstance(reason, str) or not reason.strip():
                    errors.append(
                        f"{node.node_id}: dependency {target} requires a reason"
                    )
                if not isinstance(clauses, list) or not all(
                    isinstance(value, str) and value for value in clauses
                ):
                    errors.append(
                        f"{node.node_id}: dependency {target} requires non-empty clauses"
                    )
                elif target in self.nodes:
                    target_contract = self.nodes[target].contract
                    if not target_contract:
                        errors.append(
                            f"{node.node_id}: dependency {target} has no local contract"
                        )
                    else:
                        unknown = set(clauses) - set(target_contract.clauses)
                        if unknown:
                            errors.append(
                                f"{node.node_id}: dependency {target} has unknown clauses: "
                                + ", ".join(sorted(unknown))
                            )
            for target in node.precedence:
                if target not in self.nodes:
                    errors.append(f"{node.node_id}: unknown precedence target: {target}")

        errors.extend(find_cycles(self.nodes, dependency_edges, "dependency"))
        errors.extend(
            find_cycles(self.nodes, lambda node: node.precedence, "precedence")
        )
        if errors:
            raise RouteError("\n".join(errors))

    def resolve(self, selected_ids: Iterable[str]) -> list[Node]:
        selected = list(dict.fromkeys(selected_ids))
        missing = [node_id for node_id in selected if node_id not in self.nodes]
        if missing:
            raise RouteError(f"unknown selected node(s): {', '.join(missing)}")

        resolved: list[Node] = []
        visited: set[str] = set()

        def visit(node_id: str) -> None:
            if node_id in visited:
                return
            visited.add(node_id)
            node = self.nodes[node_id]
            for dependency in node.requires:
                visit(dependency["node_id"])
            resolved.append(node)

        for node_id in selected:
            visit(node_id)
        return resolved

    def select(
        self, selected_ids: Iterable[str], selected_profiles: Iterable[str]
    ) -> list[str]:
        selected = list(selected_ids)
        for profile in selected_profiles:
            if profile not in self.profiles:
                raise RouteError(f"unknown profile: {profile}")
            selected.extend(self.profiles[profile])
        selected = list(dict.fromkeys(selected))
        if not selected:
            raise RouteError("select at least one node or profile")
        return selected

    def receipt(self, selected_ids: Iterable[str]) -> str:
        selected = list(dict.fromkeys(selected_ids))
        closure = self.resolve(selected)
        closure_ids = {node.node_id for node in closure}
        route_paths: set[Path] = set()
        excluded: set[str] = set()
        selected_paths: set[str] = set(closure_ids)

        for closure_id in closure_ids:
            current = self.nodes[closure_id]
            route_paths.add(current.manifest)
            while current.parent_id:
                parent = self.nodes[current.parent_id]
                selected_paths.add(parent.node_id)
                route_paths.add(parent.manifest)
                current = parent
        for node_id in selected_paths:
            parent_id = self.nodes[node_id].parent_id
            if parent_id:
                excluded.update(
                    set(self.nodes[parent_id].children) - selected_paths
                )

        contract_nodes = [node for node in closure if node.contract]
        contract_words = sum(
            count_words(node.contract.path.read_text(encoding="utf-8"))
            for node in contract_nodes
            if node.contract
        )
        resources = {
            resource.path: resource
            for node in closure
            for resource in node.resources
        }
        resource_words = sum(
            count_words(resource.path.read_text(encoding="utf-8"))
            for resource in resources.values()
        )
        total_words = contract_words + resource_words
        root = self.root_manifest.parent

        lines = [
            "# Route Receipt",
            "",
            f"- Root manifest: `{relative(self.root_manifest, root)}`",
            f"- Selected nodes: {', '.join(f'`{value}`' for value in selected)}",
            f"- Resolved context words: {total_words}",
            "",
            "## Routing manifests",
            "",
        ]
        lines.extend(
            f"- `{relative(path, root)}` ({self.manifest_revisions[path]})"
            for path in sorted(route_paths)
        )
        lines.extend(["", "## Contract closure", ""])
        for node in contract_nodes:
            assert node.contract is not None
            clauses = ", ".join(f"`{value}`" for value in node.contract.clauses)
            lines.append(
                f"- `{node.node_id}` — `{relative(node.contract.path, root)}` "
                f"({node.contract.revision}; clauses: {clauses})"
            )
        lines.extend(["", "## Supporting resources", ""])
        if resources:
            for resource in sorted(resources.values(), key=lambda item: str(item.path)):
                lines.append(
                    f"- `{relative(resource.path, root)}` "
                    f"({resource.role}; {resource.revision})"
                )
        else:
            lines.append("- None")
        lines.extend(["", "## Explicitly excluded siblings", ""])
        if excluded:
            lines.extend(f"- `{value}`" for value in sorted(excluded))
        else:
            lines.append("- None")
        return "\n".join(lines) + "\n"


def count_words(text: str) -> int:
    return len(WORD.findall(text))


def relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return Path(os.path.relpath(path, root)).as_posix()


def require_string(payload: dict[str, Any], key: str, source: Path) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        raise RouteError(f"{source}: {key} must be a non-empty string")
    return value


def string_list(payload: dict[str, Any], key: str, source: Path) -> tuple[str, ...]:
    value = payload.get(key, [])
    if not isinstance(value, list) or not all(
        isinstance(item, str) and item.strip() for item in value
    ):
        raise RouteError(f"{source}: {key} must be a list of non-empty strings")
    return tuple(value)


def parse_contract(payload: Any, manifest: Path, node_id: str) -> Contract | None:
    if payload is None:
        return None
    if not isinstance(payload, dict):
        raise RouteError(f"{manifest}: {node_id}.contract must be an object")
    path_value = require_string(payload, "path", manifest)
    budget = payload.get("context_budget_words")
    if not isinstance(budget, int) or budget <= 0:
        raise RouteError(
            f"{manifest}: {node_id}.contract.context_budget_words must be positive"
        )
    authority = require_string(payload, "authority", manifest)
    stability = require_string(payload, "stability", manifest)
    if authority not in AUTHORITY:
        raise RouteError(f"{manifest}: {node_id} has invalid authority {authority}")
    if stability not in STABILITY:
        raise RouteError(f"{manifest}: {node_id} has invalid stability {stability}")
    clauses = string_list(payload, "clauses", manifest)
    if not clauses:
        raise RouteError(f"{manifest}: {node_id}.contract.clauses must not be empty")
    return Contract(
        path=(manifest.parent / path_value).resolve(),
        revision=require_string(payload, "revision", manifest),
        clauses=clauses,
        context_budget_words=budget,
        authority=authority,
        stability=stability,
        baseline=require_string(payload, "baseline", manifest),
    )


def parse_resources(payload: Any, manifest: Path, node_id: str) -> tuple[Resource, ...]:
    if payload is None:
        return ()
    if not isinstance(payload, list) or not all(isinstance(item, dict) for item in payload):
        raise RouteError(f"{manifest}: {node_id}.resources must be a list of objects")
    resources: list[Resource] = []
    for item in payload:
        budget = item.get("context_budget_words")
        if not isinstance(budget, int) or budget <= 0:
            raise RouteError(
                f"{manifest}: {node_id}.resource context_budget_words must be positive"
            )
        resources.append(
            Resource(
                path=(manifest.parent / require_string(item, "path", manifest)).resolve(),
                role=require_string(item, "role", manifest),
                revision=require_string(item, "revision", manifest),
                context_budget_words=budget,
            )
        )
    return tuple(resources)


def load_graph(root_manifest: Path) -> RouteGraph:
    root_manifest = root_manifest.resolve()
    nodes: dict[str, Node] = {}
    manifests: set[Path] = set()
    manifest_revisions: dict[Path, str] = {}
    active_manifests: list[Path] = []

    def load_manifest(path: Path, parent_id: str | None) -> str:
        path = path.resolve()
        if path in active_manifests:
            chain = " -> ".join(relative(item, root_manifest.parent) for item in [*active_manifests, path])
            raise RouteError(f"route cycle: {chain}")
        if not path.is_file():
            raise RouteError(f"missing route manifest: {path}")
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            raise RouteError(f"{path}: invalid JSON: {error}") from error
        if not isinstance(payload, dict):
            raise RouteError(f"{path}: route manifest must be an object")
        if payload.get("schema_version") != 1:
            raise RouteError(f"{path}: schema_version must be 1")

        budget = payload.get("context_budget_words")
        if not isinstance(budget, int) or budget <= 0:
            raise RouteError(f"{path}: context_budget_words must be positive")
        words = count_words(path.read_text(encoding="utf-8"))
        if words > budget:
            raise RouteError(f"{path}: route uses {words} words, exceeds budget {budget}")

        node_id = require_string(payload, "node_id", path)
        manifest_revision = require_string(payload, "revision", path)
        if node_id in nodes:
            raise RouteError(f"duplicate node ID: {node_id}")
        node = Node(
            node_id=node_id,
            summary=require_string(payload, "summary", path),
            read_when=string_list(payload, "read_when", path),
            do_not_read_when=string_list(payload, "do_not_read_when", path),
            manifest=path,
            contract=parse_contract(payload.get("contract"), path, node_id),
            resources=parse_resources(payload.get("resources"), path, node_id),
            requires=tuple(payload.get("requires", [])),
            precedence=string_list(payload, "precedence", path),
            parent_id=parent_id,
        )
        if not isinstance(payload.get("requires", []), list) or not all(
            isinstance(item, dict) for item in payload.get("requires", [])
        ):
            raise RouteError(f"{path}: requires must be a list of objects")
        nodes[node_id] = node
        manifests.add(path)
        manifest_revisions[path] = manifest_revision
        active_manifests.append(path)

        children = payload.get("children", [])
        if not isinstance(children, list) or not all(isinstance(item, dict) for item in children):
            raise RouteError(f"{path}: children must be a list of objects")
        for child_payload in children:
            child_id = require_string(child_payload, "node_id", path)
            child_route_value = child_payload.get("route")
            child_contract = child_payload.get("contract")
            if child_route_value is not None:
                if child_contract is not None:
                    raise RouteError(
                        f"{path}: {child_id} must put a hybrid contract in its child route"
                    )
                if not isinstance(child_route_value, str) or not child_route_value:
                    raise RouteError(f"{path}: {child_id}.route must be a path string")
                child_path = (path.parent / child_route_value).resolve()
                loaded_id = load_manifest(child_path, node_id)
                if loaded_id != child_id:
                    raise RouteError(
                        f"{path}: child ID {child_id} does not match routed node {loaded_id}"
                    )
                child = nodes[child_id]
                child.summary = require_string(child_payload, "summary", path)
                child.read_when = string_list(child_payload, "read_when", path)
                child.do_not_read_when = string_list(
                    child_payload, "do_not_read_when", path
                )
            else:
                if child_id in nodes:
                    raise RouteError(f"duplicate node ID: {child_id}")
                child = Node(
                    node_id=child_id,
                    summary=require_string(child_payload, "summary", path),
                    read_when=string_list(child_payload, "read_when", path),
                    do_not_read_when=string_list(child_payload, "do_not_read_when", path),
                    manifest=path,
                    contract=parse_contract(child_contract, path, child_id),
                    resources=parse_resources(
                        child_payload.get("resources"), path, child_id
                    ),
                    requires=tuple(child_payload.get("requires", [])),
                    precedence=string_list(child_payload, "precedence", path),
                    parent_id=node_id,
                )
                if not isinstance(child_payload.get("requires", []), list) or not all(
                    isinstance(item, dict) for item in child_payload.get("requires", [])
                ):
                    raise RouteError(f"{path}: {child_id}.requires must be objects")
                nodes[child_id] = child
            node.children.append(child_id)

        active_manifests.pop()
        return node_id

    root_id = load_manifest(root_manifest, None)
    root_payload = json.loads(root_manifest.read_text(encoding="utf-8"))
    raw_profiles = root_payload.get("profiles", {})
    if not isinstance(raw_profiles, dict) or not all(
        isinstance(name, str)
        and isinstance(values, list)
        and all(isinstance(value, str) and value for value in values)
        for name, values in raw_profiles.items()
    ):
        raise RouteError(f"{root_manifest}: profiles must map names to node ID lists")
    profiles = {name: tuple(values) for name, values in raw_profiles.items()}
    graph = RouteGraph(
        root_manifest, root_id, nodes, manifests, manifest_revisions, profiles
    )
    graph.validate()
    return graph


def dependency_edges(node: Node) -> Iterable[str]:
    return (dependency["node_id"] for dependency in node.requires)


def find_cycles(
    nodes: dict[str, Node], edge_factory: Any, label: str
) -> list[str]:
    errors: list[str] = []
    state: dict[str, int] = {}
    stack: list[str] = []

    def visit(node_id: str) -> None:
        marker = state.get(node_id, 0)
        if marker == 2:
            return
        if marker == 1:
            start = stack.index(node_id)
            errors.append(f"{label} cycle: " + " -> ".join([*stack[start:], node_id]))
            return
        state[node_id] = 1
        stack.append(node_id)
        for target in edge_factory(nodes[node_id]):
            if target in nodes:
                visit(target)
        stack.pop()
        state[node_id] = 2

    for node_id in nodes:
        visit(node_id)
    return errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    validate = subparsers.add_parser("validate", help="validate a route tree")
    validate.add_argument("root", type=Path)
    resolve = subparsers.add_parser("resolve", help="resolve selected node closure")
    resolve.add_argument("root", type=Path)
    resolve.add_argument("--node", action="append", default=[], dest="nodes")
    resolve.add_argument("--profile", action="append", default=[], dest="profiles")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        graph = load_graph(args.root)
        if args.command == "validate":
            print(f"valid route tree: {len(graph.nodes)} nodes")
        else:
            selected = graph.select(args.nodes, args.profiles)
            print(graph.receipt(selected), end="")
    except (OSError, RouteError) as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
