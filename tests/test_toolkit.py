from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import install
import validate


class ToolkitTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.target = self.base / "Game With Spaces"
        self.target.mkdir()

    def test_repository_validates(self):
        self.assertEqual([], validate.validate(ROOT))

    def test_dry_run_writes_nothing(self):
        paths = install.install(self.target)
        self.assertEqual(len(install.COPY_PLAN), len(paths))
        self.assertEqual([], list(self.target.iterdir()))

    def test_install_copies_only_manifest_and_preserves_game(self):
        marker = self.target / "Game.cs"
        marker.write_text("unchanged", encoding="utf-8")
        paths = install.install(self.target, apply=True)
        for src, dst in install.COPY_PLAN.items():
            self.assertEqual((ROOT / src).read_bytes(), (self.target / dst).read_bytes())
        actual = {p.relative_to(self.target).as_posix() for p in self.target.rglob("*") if p.is_file()}
        self.assertEqual(set(install.COPY_PLAN.values()) | {"Game.cs"}, actual)
        self.assertEqual("unchanged", marker.read_text())
        self.assertEqual(len(paths), len(install.COPY_PLAN))

    def test_existing_file_aborts_before_any_write(self):
        conflict = self.target / "studio/THIRD_PARTY_NOTICES.md"
        conflict.parent.mkdir()
        conflict.write_text("keep", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "overwrite"):
            install.install(self.target, apply=True)
        self.assertEqual([conflict], [p for p in self.target.rglob("*") if p.is_file()])
        self.assertEqual("keep", conflict.read_text())

    def test_repeat_install_refuses_overwrite(self):
        install.install(self.target, apply=True)
        with self.assertRaisesRegex(ValueError, "overwrite"):
            install.install(self.target, apply=True)

    def test_missing_target_refused(self):
        with self.assertRaisesRegex(ValueError, "existing directory"):
            install.install(self.base / "missing", apply=True)
        self.assertFalse((self.base / "missing").exists())

    def test_source_target_refused(self):
        with self.assertRaisesRegex(ValueError, "inside"):
            install.install(ROOT)

    def test_parent_file_conflict(self):
        (self.target / "studio").write_text("not a directory")
        with self.assertRaisesRegex(ValueError, "not a directory"):
            install.install(self.target, apply=True)
        self.assertFalse((self.target / "AGENTS.md").exists())

    def make_symlink(self, link, target, directory=False):
        try:
            link.symlink_to(target, target_is_directory=directory)
        except (OSError, NotImplementedError) as error:
            self.skipTest(f"Symlinks unavailable in this environment: {error}")

    def test_symlink_target_refused(self):
        alias = self.base / "alias"
        self.make_symlink(alias, self.target, True)
        with self.assertRaisesRegex(ValueError, "Symlink"):
            install.install(alias, apply=True)
        self.assertEqual([], list(self.target.iterdir()))

    def test_symlink_destination_parent_refused(self):
        elsewhere = self.base / "elsewhere"
        elsewhere.mkdir()
        self.make_symlink(self.target / "studio", elsewhere, True)
        with self.assertRaisesRegex(ValueError, "Symlink"):
            install.install(self.target, apply=True)
        self.assertEqual([], list(elsewhere.iterdir()))
        self.assertFalse((self.target / "AGENTS.md").exists())

    def test_dangling_symlink_destination_refused(self):
        self.make_symlink(self.target / "AGENTS.md", self.base / "does-not-exist")
        with self.assertRaisesRegex(ValueError, "Symlink"):
            install.install(self.target, apply=True)

    def copy_toolkit(self):
        copy = self.base / "toolkit"
        shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        return copy

    def test_missing_source_refused_before_writes(self):
        copy = self.copy_toolkit()
        (copy / "templates/PROJECT.md").unlink()
        with self.assertRaisesRegex(ValueError, "Missing source"):
            install.install(self.target, apply=True, source=copy)
        self.assertEqual([], list(self.target.iterdir()))

    def test_validator_detects_missing_file(self):
        copy = self.copy_toolkit()
        (copy / "LICENSE").unlink()
        self.assertTrue(any("LICENSE" in error for error in validate.validate(copy)))

    def test_validator_detects_invalid_skill(self):
        copy = self.copy_toolkit()
        skill = copy / ".agents/skills/game-plan-feature/SKILL.md"
        skill.write_text("---\nname: wrong\n---\nBody\n", encoding="utf-8")
        self.assertTrue(any("skill name" in error for error in validate.validate(copy)))

    def test_validator_detects_broken_link(self):
        copy = self.copy_toolkit()
        with (copy / "README.md").open("a", encoding="utf-8") as f:
            f.write("\n[broken](missing-file.md)\n")
        self.assertTrue(any("Broken local link" in error for error in validate.validate(copy)))

    def test_cli_preview_and_failure_exit_status(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/install.py"), "--target", str(self.target)], capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("Preview only", result.stdout)
        self.assertEqual([], list(self.target.iterdir()))
        result = subprocess.run([sys.executable, str(ROOT / "scripts/install.py"), "--target", str(self.base / "absent")], capture_output=True, text=True)
        self.assertNotEqual(0, result.returncode)


if __name__ == "__main__":
    unittest.main()
