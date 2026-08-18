import json
import tempfile
import unittest
from pathlib import Path

from scripts.spec_migration import (
    MigrationError,
    analyze_coverage,
    build_inventory,
    load_inventory,
    load_mapping_entries,
    render_status,
    verification_errors,
    write_inventory,
)


class SpecMigrationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.specs = self.root / "docs/specs"
        self.specs.mkdir(parents=True)
        self.state = self.specs / "migrations/legacy"
        self.inventory_path = self.state / "inventory.json"
        self.mapping_dir = self.state / "batches"
        self.mapping_dir.mkdir(parents=True)

    def tearDown(self) -> None:
        self.temp.cleanup()

    def write_spec(self, relative: str, text: str) -> Path:
        path = self.specs / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def write_batch(self, name: str, documents: list[dict]) -> Path:
        path = self.mapping_dir / f"{name}.json"
        path.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "batch_id": name,
                    "documents": documents,
                }
            ),
            encoding="utf-8",
        )
        return path

    def inventory(self) -> dict:
        payload = build_inventory(
            self.specs,
            self.inventory_path,
            exclusions=("migrations/**",),
        )
        write_inventory(payload, self.inventory_path)
        return payload

    def coverage(self) -> tuple[dict, dict]:
        inventory = load_inventory(self.inventory_path)
        entries = load_mapping_entries(self.mapping_dir)
        return inventory, analyze_coverage(inventory, entries)

    def test_inventory_is_deterministic_and_metadata_only(self) -> None:
        self.write_spec(
            "account/login.md",
            "# Login\n\n- Contract ID: `product.login`\n"
            "- Domain ID: `product.account`\n\nSee [QA](../qa.md).\n",
        )
        self.write_spec("notes.txt", "plain legacy notes\n")
        self.write_spec("migrations/old.md", "# Generated state\n")

        first = self.inventory()
        second = build_inventory(
            self.specs,
            self.inventory_path,
            exclusions=("migrations/**",),
        )

        self.assertEqual(first["inventory_digest"], second["inventory_digest"])
        self.assertEqual(first["totals"]["documents"], 2)
        self.assertEqual(
            [item["path"] for item in first["documents"]],
            ["account/login.md", "notes.txt"],
        )
        login = first["documents"][0]
        self.assertEqual(login["headings"], ["Login"])
        self.assertEqual(login["local_links"], ["../qa.md"])
        self.assertEqual(login["declared"]["contract_id"], "product.login")
        self.assertNotIn("See", json.dumps(login))

    def test_complete_terminal_mapping_verifies(self) -> None:
        self.write_spec("login.md", "# Login\n")
        self.write_spec("old.md", "# Old login\n")
        self.inventory()
        self.write_batch(
            "account",
            [
                {
                    "path": "login.md",
                    "disposition": "contract",
                    "node_id": "product.login",
                    "target": "login.md",
                },
                {
                    "path": "old.md",
                    "disposition": "superseded",
                    "canonical_path": "login.md",
                },
            ],
        )
        inventory, coverage = self.coverage()

        self.assertEqual(coverage["terminal"], 2)
        self.assertEqual(coverage["unclassified"], 0)
        self.assertEqual(
            verification_errors(
                inventory,
                self.inventory_path,
                coverage,
                source_override=None,
                require_complete=True,
            ),
            [],
        )

    def test_incomplete_and_deferred_are_visible(self) -> None:
        self.write_spec("one.md", "# One\n")
        self.write_spec("two.md", "# Two\n")
        self.inventory()
        self.write_batch(
            "pending",
            [{"path": "one.md", "disposition": "deferred"}],
        )
        inventory, coverage = self.coverage()
        errors = verification_errors(
            inventory,
            self.inventory_path,
            coverage,
            source_override=None,
            require_complete=True,
        )

        self.assertEqual(coverage["deferred"], 1)
        self.assertEqual(coverage["unclassified"], 1)
        self.assertTrue(any("unclassified" in error for error in errors))
        self.assertTrue(any("deferred" in error for error in errors))

    def test_duplicate_mapping_and_hash_drift_fail(self) -> None:
        source = self.write_spec("one.md", "# One\n")
        self.inventory()
        entry = {
            "path": "one.md",
            "disposition": "contract",
            "node_id": "product.one",
        }
        self.write_batch("first", [entry])
        self.write_batch("second", [entry])
        source.write_text("# One changed\n", encoding="utf-8")
        inventory, coverage = self.coverage()
        errors = verification_errors(
            inventory,
            self.inventory_path,
            coverage,
            source_override=None,
            require_complete=False,
        )

        self.assertTrue(any("duplicate mapping" in error for error in errors))
        self.assertTrue(any("hash drift" in error for error in errors))

    def test_tampered_inventory_is_rejected(self) -> None:
        self.write_spec("one.md", "# One\n")
        payload = self.inventory()
        payload["documents"][0]["path"] = "../outside.md"
        write_inventory(payload, self.inventory_path)

        with self.assertRaisesRegex(MigrationError, "must stay below source_root"):
            load_inventory(self.inventory_path)

    def test_thousand_document_status_stays_compact(self) -> None:
        for index in range(1000):
            self.write_spec(f"domain/spec-{index:04d}.md", f"# Spec {index}\n")
        inventory = self.inventory()
        coverage = analyze_coverage(inventory, [])
        status = render_status(inventory, coverage)

        self.assertEqual(inventory["totals"]["documents"], 1000)
        self.assertEqual(coverage["unclassified"], 1000)
        self.assertLess(len(status), 800)
        self.assertNotIn("spec-0999", status)


if __name__ == "__main__":
    unittest.main()
