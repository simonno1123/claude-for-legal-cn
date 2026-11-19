"""Tests for the public-repository privacy guard. All values are fictional.

Run: python3 -m unittest discover -s validation/privacy_guard -t validation/privacy_guard
"""

from __future__ import annotations

import pathlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "scripts" / "privacy_guard"))

import check_public_text as c  # noqa: E402


def rules(line, terms=(), case_file=False):
    return [r for r, _ in c.scan_line(line, list(terms), case_file)]


class Generic(unittest.TestCase):
    def test_identifiers(self):
        self.assertIn("PRC_ID_NUMBER", rules("身份号码 330100198001010013"))
        self.assertIn("MOBILE_NUMBER", rules("电话 13900000000"))
        self.assertIn("CARD_LENGTH_DIGITS", rules("账号 6222000000000000000"))
        self.assertIn("COURT_CASE_NUMBER", rules("（2030）浙0000执9999号之一"))
        self.assertIn("WINDOWS_USER_PATH", rules(r"C:\Users\someone\Documents"))
        self.assertIn("HOST_NAME", rules("DESKTOP-ABC1234"))
        self.assertIn("MACHINE_SID", rules("S-1-5-21-1234567890"))
        self.assertIn("PRIVATE_FOLDER", rules("Documents/legal-cn-private/CASE-X"))

    def test_not_flagged(self):
        self.assertEqual(rules("SHA-256 " + "A1" * 32), [])
        self.assertEqual(rules("法释〔2014〕8号；浙委法办函〔2020〕19号"), [])
        self.assertEqual(rules(r"C:\Users\REDACTED-OWNER; DESKTOP-REDACTED; S-1-5-21-REDACTED"), [])
        self.assertEqual(rules("max int 9223372036854775807"), [])

    def test_allow_marker(self):
        self.assertEqual(rules("13900000000 <!-- privacy-guard: allow -->"), [])


class Terms(unittest.TestCase):
    def test_private_terms_case_insensitive(self):
        self.assertIn("PRIVATE_TERM", rules("party Zhao Fictional appears", ["zhao fictional"]))
        self.assertEqual(rules("nothing here", ["zhao fictional"]), [])

    def test_load_terms_skips_comments(self):
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False, encoding="utf-8") as f:
            f.write("# comment\n虚构甲\n\nX\n")
        self.assertEqual(c.load_terms(f.name), ["虚构甲"])


class CaseFact(unittest.TestCase):
    def test_only_in_case_files(self):
        line = "复核人陈述：该冻结已失效，未续冻"
        self.assertIn("CASE_FACT_WORD", rules(line, case_file=True))
        self.assertEqual(rules(line, case_file=False), [])
        self.assertIn("CASE_FACT_WORD", rules("已分得 1234.5 元", case_file=True))
        self.assertEqual(rules("C5 出现停点；处置 APPROVE；授权用尽", case_file=True), [])


class Diff(unittest.TestCase):
    def test_added_lines_only(self):
        diff = ("diff --git a/x.md b/x.md\n--- a/x.md\n+++ b/x.md\n@@ -1,0 +2,2 @@\n"
                "+safe line\n+电话 13900000000\n")
        found = list(c.added_lines(diff))
        self.assertEqual([(p, n) for p, n, _ in found], [("x.md", 2), ("x.md", 3)])
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(len(c.run(found, [], case_check=False)), 1)


if __name__ == "__main__":
    unittest.main()
