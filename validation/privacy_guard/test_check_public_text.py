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
        for num in ("（2030）京民终123号", "（2030）最高法民终123号", "（2030）浙00民终1号", "(2030)沪0000民初1号"):
            self.assertIn("COURT_CASE_NUMBER", rules(num), num)
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


class RealGit(unittest.TestCase):
    def test_chinese_file_name_in_staged_diff(self):
        import os
        import subprocess
        with tempfile.TemporaryDirectory() as d:
            env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid",
                   "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.invalid"}
            run = lambda *a: subprocess.run(["git", *a], cwd=d, env=env, check=True, capture_output=True)
            run("init", "-q")
            pathlib.Path(d, "案件 记录.md").write_text("电话 13900000000\n", encoding="utf-8")
            pathlib.Path(d, "note.md").write_text("++ heading\n@@ not a hunk\n电话 13900000001\n", encoding="utf-8")
            run("add", "-A")
            for quote in ("true", "false"):
                diff = subprocess.run(["git", "-c", f"core.quotePath={quote}", "diff", "--cached", "--unified=0", "--no-color"],
                                      cwd=d, capture_output=True, text=True, encoding="utf-8", check=True).stdout
                found = list(c.added_lines(diff))
                self.assertEqual(sorted({p for p, _, _ in found}), ["note.md", "案件 记录.md"], quote)
                self.assertEqual(len(c.run(found, [], case_check=False)), 2)
                self.assertIn(("note.md", 3), [(p, n) for p, n, _ in found])


class PartialStaging(unittest.TestCase):
    def test_case_code_read_from_index_not_worktree(self):
        import os
        import subprocess
        guard = pathlib.Path(__file__).resolve().parents[2] / "scripts" / "privacy_guard" / "check_public_text.py"
        with tempfile.TemporaryDirectory() as d:
            env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.invalid",
                   "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.invalid"}
            run = lambda *a: subprocess.run(["git", *a], cwd=d, env=env, check=True, capture_output=True)
            run("init", "-q")
            f = pathlib.Path(d, "rec.md")
            f.write_text("CASE-Z\n该冻结未续冻\n", encoding="utf-8")
            run("add", "rec.md")
            f.write_text("该冻结未续冻\n", encoding="utf-8")  # worktree no longer names the code
            res = subprocess.run([sys.executable, str(guard), "--staged"], cwd=d, capture_output=True, text=True)
            self.assertEqual(res.returncode, 1, res.stdout + res.stderr)
            self.assertIn("CASE_FACT_WORD", res.stdout)
            f.unlink()  # deleted from the worktree after staging
            res = subprocess.run([sys.executable, str(guard), "--staged"], cwd=d, capture_output=True, text=True)
            self.assertEqual(res.returncode, 1)


class Diff(unittest.TestCase):
    def test_added_lines_only(self):
        diff = ("diff --git a/x.md b/x.md\nindex 1..2 100644\n--- a/x.md\n+++ b/x.md\n@@ -1,0 +2,2 @@\n"
                "+safe line\n+电话 13900000000\n")
        found = list(c.added_lines(diff))
        self.assertEqual([(p, n) for p, n, _ in found], [("x.md", 2), ("x.md", 3)])
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(len(c.run(found, [], case_check=False)), 1)


if __name__ == "__main__":
    unittest.main()
