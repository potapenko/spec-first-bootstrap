from __future__ import annotations

import argparse
import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from scripts.spec_migration import MigrationError, census, coverage


class MigrationTests(unittest.TestCase):
    def test_census_is_compact_and_reports_oversized(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            (root / "large.md").write_text("\n".join(["secret"] * 101), encoding="utf-8")
            args = argparse.Namespace(
                source_root=root,
                exclude=[],
                extension=[".md"],
                max_lines=100,
                show_oversized=10,
            )
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(census(args), 0)
            value = output.getvalue()
            self.assertIn("documents=1", value)
            self.assertIn("oversized=1", value)
            self.assertNotIn("\nsecret\n", value)

    def test_markdown_coverage_complete(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            base = Path(raw)
            source = base / "specs"
            batches = base / "migration" / "batches"
            source.mkdir()
            batches.mkdir(parents=True)
            (source / "one.md").write_text("# One\n", encoding="utf-8")
            (source / "two.md").write_text("# Two\n", encoding="utf-8")
            (batches / "batch.md").write_text(
                "[One](../../specs/one.md)\n[Two](../../specs/two.md)\n",
                encoding="utf-8",
            )
            args = argparse.Namespace(
                source_root=source,
                batch_root=batches,
                exclude=[],
                extension=[".md"],
                require_complete=True,
                show_problems=10,
            )
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                self.assertEqual(coverage(args), 0)
            self.assertIn("missing=0", output.getvalue())

    def test_duplicate_mapping_fails_complete_check(self) -> None:
        with tempfile.TemporaryDirectory() as raw:
            base = Path(raw)
            source = base / "specs"
            batches = base / "migration" / "batches"
            source.mkdir()
            batches.mkdir(parents=True)
            (source / "one.md").write_text("# One\n", encoding="utf-8")
            link = "[One](../../specs/one.md)\n"
            (batches / "a.md").write_text(link, encoding="utf-8")
            (batches / "b.md").write_text(link, encoding="utf-8")
            args = argparse.Namespace(
                source_root=source,
                batch_root=batches,
                exclude=[],
                extension=[".md"],
                require_complete=True,
                show_problems=10,
            )
            with self.assertRaises(MigrationError):
                coverage(args)


if __name__ == "__main__":
    unittest.main()
