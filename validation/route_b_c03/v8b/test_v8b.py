"""Tests for C03 V8-B (design R3, B2 not enabled). All data and keys are fictional and test-only.

Run: python3 -m unittest discover -s validation/route_b_c03/v8b -t validation/route_b_c03/v8b
"""

from __future__ import annotations

import copy
import hashlib
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "validation" / "route_b_c03" / "v8"))

from phase2_runtime.route_b_c03 import gate_records as g  # noqa: E402
from phase2_runtime.route_b_c03 import v8b  # noqa: E402
import test_gate_records as fx  # noqa: E402

HAVE_SSH = shutil.which("ssh-keygen") is not None
T0 = "2026-12-03T12:00:00+08:00"
T_USE = "2026-12-05T09:00:00+08:00"


def keypair(d: pathlib.Path, name: str) -> tuple[pathlib.Path, str]:
    key = d / name
    subprocess.run(["ssh-keygen", "-q", "-t", "ed25519", "-N", "", "-C", "test-only", "-f", str(key)], check=True)
    return key, (d / f"{name}.pub").read_text().strip()


def full_from(bd: dict, max_uses: int = 1) -> dict:
    ls = fx.LaterStages
    bd["Q1"] = ls.q1(bd, "2026-12-02T13:00:00+08:00")
    bd["Q2"] = fx.mk("Q", "2026-12-02T14:00:00+08:00", refs={"Q1": fx.sha(bd["Q1"]), "application_body": fx.SHA_D},
                     stage="Q2", rows=ls.rows(bd), h_increment=copy.deepcopy(fx.EMPTY_Q), auth_checks=None)
    bd["AUTH"] = fx.mk("AUTH", "2026-12-02T15:00:00+08:00", refs={"Q2": fx.sha(bd["Q2"]), "application_body": fx.SHA_D},
                       action=bd["T"]["next_step"], scope={"candidate": "CAND-Z", "version": "v1", "M": fx.sha(bd["M"])},
                       own_deadline="2026-12-10T00:00:00+08:00", max_uses=max_uses)
    bd["Q3"] = fx.mk("Q", "2026-12-04T10:00:00+08:00", refs={"AUTH": fx.sha(bd["AUTH"]), "Q2": fx.sha(bd["Q2"])}, stage="Q3",
                     rows=ls.rows(bd), h_increment=copy.deepcopy(fx.EMPTY_Q), auth_checks={k: True for k in g.AUTH_CHECK_KEYS})
    bd["G"] = [{"kind": "initial", "auth": fx.sha(bd["AUTH"]), "max_uses": max_uses, "used": 0, "at": "2026-12-02T15:00:00+08:00"}]
    return bd


def write_folder(root: pathlib.Path, bd: dict, names: tuple[str, ...]) -> None:
    root.mkdir(parents=True, exist_ok=True)
    for n in names:
        if bd.get(n):
            (root / f"{n}.json").write_bytes(g.canonical_bytes(bd[n]))
    for prefix in ("X", "V", "W", "CORR"):
        for i, rec in enumerate(bd.get(prefix) or [], 1):
            (root / f"{prefix}_{i}.json").write_bytes(g.canonical_bytes(rec))
    if "G" in names:
        (root / "G.jsonl").write_text("".join(g.canonical_bytes(e).decode() + "\n" for e in bd["G"]), encoding="utf-8")


def h_line(case: str, at: str) -> str:
    return g.canonical_bytes(fx.disc(at) | {"case": case}).decode() + "\n"


@unittest.skipUnless(HAVE_SSH, "ssh-keygen not available")
class V8B(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.d = pathlib.Path(self.tmp.name)
        self.trust_dir = self.d / "trust"; self.trust_dir.mkdir()
        self.key, pub = keypair(self.d, "owner")
        (self.trust_dir / "allowed_signers").write_text(f'{v8b.PRINCIPAL} namespaces="{v8b.NAMESPACE}" {pub}\n')
        self.trust = v8b.Trust(self.trust_dir)
        self.signer = v8b.SshSigner(self.key)
        self.cand = self.d / "cand.md"; self.cand.write_text("虚构候选\n", encoding="utf-8")
        self.digest = hashlib.sha256(self.cand.read_bytes()).hexdigest().upper()
        self.hfile = self.d / "H_case.jsonl"; self.hfile.write_text(h_line("CASE-Y", "2026-11-30T09:00:00+08:00"), encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    # -- builders
    def l1(self, folder="rec"):
        bd = full_from(fx.l1_bundle(self.digest))
        root = self.d / folder
        write_folder(root, bd, ("M", "I", "T", "R"))
        return bd, root

    def sign(self, root, stage, now=T0):
        return v8b.sign_stage(root, stage, self.trust, self.signer, h=str(self.hfile), now=now)

    def add(self, root, bd, names):
        write_folder(root, bd, names)

    def through_s3(self):
        bd, root = self.l1()
        self.assertEqual(self.sign(root, "S1")["result"], "SIGNED")
        self.add(root, bd, ("Q1", "Q2", "AUTH", "Q3", "G"))
        self.assertEqual(self.sign(root, "S3")["result"], "SIGNED")
        return bd, root

    def use(self, root, dest="out", now=T_USE):
        return v8b.use(root, self.cand, self.d / dest, self.trust, self.signer, h=str(self.hfile), now=now)

    # -- tests
    def test_l1_positive_path(self):
        bd, root = self.through_s3()
        out = self.use(root)
        self.assertEqual(out["result"], "USED", out)
        reg = self.trust.registry.read()
        self.assertEqual([e["type"] for e in reg], ["intent", "committed"])
        chk = v8b.verify_chain(root, self.trust, self.signer, upto="S4")
        self.assertTrue(chk["ok"], chk)

    def test_l2_positive_and_cooling(self):
        bd = full_from(fx.l2_bundle())
        bd["M"]["candidate"]["output_sha256"] = self.digest
        bd = full_from(fx.rebind(bd))
        root = self.d / "l2"
        write_folder(root, bd, ("M", "I", "T", "R", "E", "S"))
        out = self.sign(root, "S1", now="2026-12-02T09:00:00+08:00")
        self.assertEqual(out["result"], "SIGNED", out)
        self.add(root, bd, ("P",))
        early = self.sign(root, "S2", now="2026-12-02T10:00:00+08:00")
        self.assertEqual(early["reasons"], ["COOLING_PERIOD_UNMET"])
        self.assertEqual(self.sign(root, "S2", now="2026-12-03T10:00:00+08:00")["result"], "SIGNED")
        self.add(root, bd, ("Q1", "Q2", "AUTH", "Q3", "G"))
        self.assertEqual(self.sign(root, "S3", now="2026-12-03T11:00:00+08:00")["result"], "SIGNED")
        self.assertEqual(self.use(root)["result"], "USED")

    def test_untrusted_key_refused(self):
        bd, root = self.l1()
        other, _ = keypair(self.d, "recorder")
        (root / "allowed_signers").write_text("decoy: never read\n")
        out = v8b.sign_stage(root, "S1", self.trust, v8b.SshSigner(other), h=str(self.hfile), now=T0)
        self.assertEqual(out["reasons"], ["SIGNATURE_INVALID"])
        self.assertFalse((root / "V8B_S1.json").exists())

    def test_closed_manifest(self):
        bd, root = self.through_s3()
        self.assertTrue(v8b.verify_chain(root, self.trust, self.signer, upto="S3")["ok"])
        r = root / "R.json"; r.write_bytes(r.read_bytes().replace("虚构".encode(), "改动".encode(), 1))
        chk = v8b.verify_chain(root, self.trust, self.signer, upto="S3")
        self.assertIn("SIGNED_MANIFEST_MISMATCH:S1", chk["reasons"])

    def test_replay_across_folders(self):
        bd, root = self.through_s3()
        twin = self.d / "twin"; shutil.copytree(root, twin)
        self.assertEqual(self.use(root)["result"], "USED")
        out = self.use(twin, dest="out2")
        self.assertIn("AUTHORIZATION_REPLAYED", out["reasons"])
        self.assertFalse((self.d / "out2").exists())

    def test_orphan_intent_blocks_until_recovered(self):
        bd, root = self.through_s3()
        intent = self.trust.registry.append({"type": "intent", "auth_key": "X:Y", "case": "CASE-Z", "folder": "x",
                                             "challenge": "00", "at": T0})
        self.assertEqual(self.use(root)["reasons"], ["REGISTRY_RECOVERY_REQUIRED"])
        self.assertEqual(v8b.recover(self.trust, intent["seq"], "aborted", "test")["result"], "RESOLVED")
        self.assertEqual(self.use(root)["result"], "USED")

    def test_withdrawal_blocks(self):
        bd, root = self.through_s3()
        v8b.withdraw(self.trust, "CASE-Z", None, "所有者叫停", now=T0)
        self.assertIn("WITHDRAWN_OR_SUPERSEDED", self.use(root)["reasons"])

    def test_stop_index_rollback_and_new_stop(self):
        bd, root = self.through_s3()
        self.hfile.write_text("", encoding="utf-8")
        self.assertIn("STOP_INDEX_ROLLED_BACK", self.use(root)["reasons"])
        self.hfile.write_text(h_line("CASE-Y", "2026-11-30T09:00:00+08:00") + h_line("CASE-Z", "2026-12-04T12:00:00+08:00"),
                              encoding="utf-8")
        self.assertIn("NEW_STOP_AFTER_Q3", self.use(root)["reasons"])

    def test_global_lock_and_expiry(self):
        bd, root = self.through_s3()
        self.trust.lock_path.write_text("held")
        self.assertEqual(self.use(root)["reasons"], ["BUSY_GLOBAL"])
        self.trust.lock_path.unlink()
        late = self.use(root, now="2026-12-21T00:00:00+08:00")
        self.assertEqual(late["result"], "REFUSED")
        self.assertFalse((root / "V8B_S4.json").exists())

    def test_trust_log_tamper_detected(self):
        bd, root = self.through_s3()
        log = self.trust_dir / "sign_log.jsonl"
        lines = log.read_text(encoding="utf-8").splitlines()
        lines[0] = lines[0].replace('"S1"', '"S3"')
        log.write_text("\n".join(lines) + "\n", encoding="utf-8")
        chk = v8b.verify_chain(root, self.trust, self.signer, upto="S3")
        self.assertFalse(chk["ok"])

    def test_s1_requires_review_pass(self):
        bd, root = self.l1()
        rp = root / "R.json"
        R = g.parse_record(rp.read_text(encoding="utf-8")); R["material_conflict"] = "有"
        rp.write_bytes(g.canonical_bytes(R))
        out = self.sign(root, "S1")
        self.assertEqual(out["result"], "REFUSED")
        self.assertFalse((root / "V8B_S1.json").exists())


if __name__ == "__main__":
    unittest.main()
