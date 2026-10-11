#!/usr/bin/env python3
"""Synthetic regression for first-party marketplace/manifest field equality.

Only loads the localization-check declarations and uses in-memory JSON data.
It does not load DSP-004 candidates, invoke providers, or modify project files.
"""

from __future__ import annotations

import copy
import runpy
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parent.parent
CHECKS = runpy.run_path(str(ROOT / "scripts" / "localization-regression.py"))
CHECK_MARKETPLACE = CHECKS["check_marketplace"]
MODULES = sorted(CHECKS["ROOT_MODULES"])


class MarketplaceConsistencyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.entries = [
            {
                "name": name,
                "source": f"./{name}",
                "description": "中国法静态审查测试描述；不授权实际执行。",
                "author": {"name": "Synthetic regression author"},
            }
            for name in MODULES
        ]
        self.manifests = {
            item["name"]: {key: copy.deepcopy(item[key]) for key in ("name", "description", "author")}
            for item in self.entries
        }

    def evaluate(self) -> list[str]:
        def synthetic_json(path: Path, errors: list[str]):
            if path.name == "marketplace.json":
                return {"plugins": self.entries}
            return self.manifests[path.parent.parent.name]

        errors: list[str] = []
        with patch.dict(CHECK_MARKETPLACE.__globals__, {"load_json": synthetic_json}):
            CHECK_MARKETPLACE(errors)
        return errors

    def test_equal_fields_pass(self) -> None:
        self.assertEqual(self.evaluate(), [])

    def test_name_mismatch_is_rejected(self) -> None:
        self.manifests[MODULES[0]]["name"] = "synthetic-other-name"
        self.assertEqual(len(self.evaluate()), 1)
        self.assertIn(" name does not match ", self.evaluate()[0])

    def test_description_mismatch_is_rejected(self) -> None:
        self.manifests[MODULES[0]]["description"] = "不同的合成测试描述。"
        self.assertEqual(len(self.evaluate()), 1)
        self.assertIn(" description does not match ", self.evaluate()[0])

    def test_author_mismatch_is_rejected(self) -> None:
        self.manifests[MODULES[0]]["author"] = {"name": "Different synthetic author"}
        self.assertEqual(len(self.evaluate()), 1)
        self.assertIn(" author does not match ", self.evaluate()[0])

    def test_multiple_field_mismatches_are_all_reported(self) -> None:
        self.manifests[MODULES[0]]["name"] = "synthetic-other-name"
        self.manifests[MODULES[0]]["description"] = "不同的合成测试描述。"
        self.manifests[MODULES[0]]["author"] = {"name": "Different synthetic author"}
        self.assertEqual(len(self.evaluate()), 3)

    def test_missing_manifest_description_is_rejected(self) -> None:
        del self.manifests[MODULES[0]]["description"]
        self.assertEqual(len(self.evaluate()), 1)
        self.assertIn(" description does not match ", self.evaluate()[0])

    def test_missing_manifest_author_is_rejected(self) -> None:
        del self.manifests[MODULES[0]]["author"]
        self.assertEqual(len(self.evaluate()), 1)
        self.assertIn(" author does not match ", self.evaluate()[0])


if __name__ == "__main__":
    unittest.main()
