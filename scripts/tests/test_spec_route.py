import json
import tempfile
import unittest
from pathlib import Path

from scripts.spec_route import RouteError, load_graph


class SpecRouteTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        (self.root / "root.md").write_text(
            "# Root\n\nbranch@1\n\nROOT.CORE\n", encoding="utf-8"
        )
        (self.root / "leaf.md").write_text(
            "# Leaf\n\nleaf@1\n\nLEAF.RULE\n", encoding="utf-8"
        )
        (self.root / "dependency.md").write_text(
            "# Dependency\n\ndependency@1\n\nDEPENDENCY.RULE\n", encoding="utf-8"
        )
        (self.root / "qa.md").write_text("# QA\n\nVerify the leaf.\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_json(self, relative: str, payload: dict) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload), encoding="utf-8")
        return path

    @staticmethod
    def contract(path: str, revision: str, clause: str, budget: int = 50) -> dict:
        return {
            "path": path,
            "revision": revision,
            "clauses": [clause],
            "context_budget_words": budget,
            "authority": "Active",
            "stability": "Accepted",
            "baseline": "test",
        }

    def valid_tree(self) -> Path:
        self.write_json(
            "branch/route.json",
            {
                "schema_version": 1,
                "node_id": "branch",
                "revision": "branch.route@1",
                "summary": "Hybrid branch.",
                "read_when": ["working on branch"],
                "do_not_read_when": ["unrelated"],
                "context_budget_words": 200,
                "contract": self.contract("../root.md", "branch@1", "ROOT.CORE"),
                "requires": [],
                "precedence": [],
                "children": [
                    {
                        "node_id": "leaf",
                        "summary": "Leaf contract.",
                        "read_when": ["working on leaf"],
                        "do_not_read_when": ["branch only"],
                        "contract": self.contract(
                            "../leaf.md", "leaf@1", "LEAF.RULE"
                        ),
                        "requires": [
                            {
                                "node_id": "dependency",
                                "clauses": ["DEPENDENCY.RULE"],
                                "reason": "shared rule",
                            }
                        ],
                        "resources": [
                            {
                                "path": "../qa.md",
                                "role": "qa",
                                "revision": "qa@1",
                                "context_budget_words": 20,
                            }
                        ],
                        "precedence": [],
                    },
                    {
                        "node_id": "dependency",
                        "summary": "Shared dependency.",
                        "read_when": ["required explicitly"],
                        "do_not_read_when": ["not required"],
                        "contract": self.contract(
                            "../dependency.md", "dependency@1", "DEPENDENCY.RULE"
                        ),
                        "requires": [],
                        "precedence": [],
                    },
                ],
            },
        )
        return self.write_json(
            "route.json",
            {
                "schema_version": 1,
                "node_id": "root",
                "revision": "root.route@1",
                "summary": "Root router.",
                "read_when": ["all product work"],
                "do_not_read_when": ["non-product work"],
                "context_budget_words": 100,
                "profiles": {"leaf-work": ["leaf"]},
                "requires": [],
                "precedence": [],
                "children": [
                    {
                        "node_id": "branch",
                        "summary": "Branch route.",
                        "read_when": ["branch work"],
                        "do_not_read_when": ["other work"],
                        "route": "branch/route.json",
                    }
                ],
            },
        )

    def test_resolves_leaf_dependency_and_hybrid_contract(self) -> None:
        graph = load_graph(self.valid_tree())
        closure = graph.resolve(["leaf", "branch"])
        self.assertEqual(
            [node.node_id for node in closure], ["dependency", "leaf", "branch"]
        )
        receipt = graph.receipt(["leaf"])
        self.assertIn("`dependency`", receipt)
        self.assertIn("`leaf`", receipt)
        self.assertIn("root.route@1", receipt)
        self.assertIn("branch.route@1", receipt)
        self.assertIn("qa.md", receipt)
        self.assertIn("Resolved context words", receipt)
        self.assertIn("Explicitly excluded siblings", receipt)
        self.assertEqual(graph.select([], ["leaf-work"]), ["leaf"])

    def test_rejects_unknown_dependency(self) -> None:
        path = self.valid_tree()
        branch_path = self.root / "branch/route.json"
        payload = json.loads(branch_path.read_text(encoding="utf-8"))
        payload["children"][0]["requires"][0]["node_id"] = "missing"
        branch_path.write_text(json.dumps(payload), encoding="utf-8")
        with self.assertRaisesRegex(RouteError, "unknown dependency"):
            load_graph(path)

    def test_rejects_dependency_cycle(self) -> None:
        path = self.valid_tree()
        branch_path = self.root / "branch/route.json"
        payload = json.loads(branch_path.read_text(encoding="utf-8"))
        payload["children"][1]["requires"] = [
            {"node_id": "leaf", "clauses": ["LEAF.RULE"], "reason": "cycle"}
        ]
        branch_path.write_text(json.dumps(payload), encoding="utf-8")
        with self.assertRaisesRegex(RouteError, "dependency cycle"):
            load_graph(path)

    def test_rejects_unknown_dependency_clause(self) -> None:
        path = self.valid_tree()
        branch_path = self.root / "branch/route.json"
        payload = json.loads(branch_path.read_text(encoding="utf-8"))
        payload["children"][0]["requires"][0]["clauses"] = ["MISSING.CLAUSE"]
        branch_path.write_text(json.dumps(payload), encoding="utf-8")
        with self.assertRaisesRegex(RouteError, "unknown clauses"):
            load_graph(path)

    def test_rejects_duplicate_clause_id(self) -> None:
        path = self.valid_tree()
        branch_path = self.root / "branch/route.json"
        payload = json.loads(branch_path.read_text(encoding="utf-8"))
        payload["children"][1]["contract"]["clauses"] = ["LEAF.RULE"]
        branch_path.write_text(json.dumps(payload), encoding="utf-8")
        with self.assertRaisesRegex(RouteError, "duplicate clause ID"):
            load_graph(path)

    def test_rejects_contract_budget_overflow(self) -> None:
        path = self.valid_tree()
        branch_path = self.root / "branch/route.json"
        payload = json.loads(branch_path.read_text(encoding="utf-8"))
        payload["children"][0]["contract"]["context_budget_words"] = 1
        branch_path.write_text(json.dumps(payload), encoding="utf-8")
        with self.assertRaisesRegex(RouteError, "exceeds budget"):
            load_graph(path)

    def test_rejects_resource_budget_overflow(self) -> None:
        path = self.valid_tree()
        branch_path = self.root / "branch/route.json"
        payload = json.loads(branch_path.read_text(encoding="utf-8"))
        payload["children"][0]["resources"][0]["context_budget_words"] = 1
        branch_path.write_text(json.dumps(payload), encoding="utf-8")
        with self.assertRaisesRegex(RouteError, "resource uses"):
            load_graph(path)

    def test_rejects_route_cycle(self) -> None:
        path = self.valid_tree()
        branch_path = self.root / "branch/route.json"
        payload = json.loads(branch_path.read_text(encoding="utf-8"))
        payload["children"] = [
            {
                "node_id": "root",
                "summary": "Cycle.",
                "read_when": ["never"],
                "do_not_read_when": ["always"],
                "route": "../route.json",
            }
        ]
        branch_path.write_text(json.dumps(payload), encoding="utf-8")
        with self.assertRaisesRegex(RouteError, "route cycle"):
            load_graph(path)

    def test_rejects_unknown_profile_node(self) -> None:
        path = self.valid_tree()
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload["profiles"]["broken"] = ["missing"]
        path.write_text(json.dumps(payload), encoding="utf-8")
        with self.assertRaisesRegex(RouteError, "profile broken"):
            load_graph(path)


if __name__ == "__main__":
    unittest.main()
