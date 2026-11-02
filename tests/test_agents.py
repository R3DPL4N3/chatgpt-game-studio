from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import install
import studio
import validate


class AgentSystemTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)

    def copy(self):
        dest = self.base / 'toolkit'
        shutil.copytree(ROOT, dest, ignore=shutil.ignore_patterns('__pycache__', '.git'))
        return dest

    def test_exact_49_unique_native_roles(self):
        agents = studio.load_registry()['agents']
        self.assertEqual(49, len(agents))
        self.assertEqual(49, len(set(a['id'] for a in agents)))
        self.assertEqual(set(install.AGENT_IDS), {a['id'] for a in agents})
        for a in agents:
            data = tomllib.loads((ROOT / a['file']).read_text())
            self.assertEqual(a['id'], data['name'])
            self.assertEqual(a['description'], data['description'])
            self.assertIn(a['focus'], data['developer_instructions'])

    def test_all_routes_valid_and_bounded(self):
        ids = set(install.AGENT_IDS)
        for area in studio.ROUTES:
            for engine in ('any', *studio.ENGINE_ROLES):
                plan = studio.route(area, engine)
                self.assertLessEqual(len(plan['suggested_roles']), 4)
                self.assertEqual(len(set(plan['suggested_roles'])), len(plan['suggested_roles']))
                self.assertTrue(set(plan['suggested_roles']) <= ids)
                self.assertIn('NOT STARTED', plan['execution'])

    def test_engine_specific_routing(self):
        self.assertIn('ue-replication-specialist', studio.route('network', 'unreal')['suggested_roles'])
        self.assertIn('unity-ui-specialist', studio.route('ui', 'unity')['suggested_roles'])
        self.assertIn('godot-specialist', studio.route('gameplay', 'godot')['suggested_roles'])

    def test_invalid_route_rejected(self):
        for area, engine in [('unknown', 'unity'), ('ui', 'unknown')]:
            with self.assertRaises(ValueError): studio.route(area, engine)

    def test_every_role_can_prepare_handoff(self):
        for role in install.AGENT_IDS:
            result = studio.brief(role, 'Read only: inspect movement')
            self.assertIn('Exclusive writable files', result)
            self.assertIn('Read only: inspect movement', result)
            self.assertIn('PASS/FAIL/BLOCKED/NOT RUN', result)

    def test_unknown_role_rejected(self):
        with self.assertRaises(ValueError): studio.brief('../secret', 'task')

    def test_registry_duplicate_rejected(self):
        copy = self.copy(); path = copy / 'studio/agents.json'
        data = json.loads(path.read_text()); data['agents'][-1] = data['agents'][0]
        path.write_text(json.dumps(data))
        self.assertTrue(any('49 expected unique' in e for e in validate.validate(copy)))

    def test_agent_file_missing_rejected(self):
        copy = self.copy(); (copy / '.codex/agents/producer.toml').unlink()
        self.assertTrue(validate.validate(copy))
        game = self.base / 'game'; game.mkdir()
        with self.assertRaises(ValueError): install.install(game, apply=True, source=copy)
        self.assertEqual([], list(game.iterdir()))

    def test_native_name_mismatch_rejected(self):
        copy = self.copy(); path = copy / '.codex/agents/producer.toml'
        path.write_text(path.read_text().replace('name = "producer"', 'name = "fake"', 1))
        self.assertTrue(any('mismatch' in e for e in validate.validate(copy)))

    def test_native_permission_override_rejected(self):
        copy = self.copy(); path = copy / '.codex/agents/producer.toml'
        path.write_text(path.read_text() + '\nsandbox_mode = "danger-full-access"\n')
        self.assertTrue(any('Unexpected native' in e for e in validate.validate(copy)))

    def test_cap_tampering_rejected(self):
        copy = self.copy(); path = copy / '.codex/config.toml'
        path.write_text(path.read_text().replace('= 4', '= 49'))
        self.assertTrue(any('concurrency cap' in e for e in validate.validate(copy)))

    def test_lead_cycle_rejected(self):
        copy = self.copy(); path = copy / 'studio/agents.json'
        data = json.loads(path.read_text())
        next(a for a in data['agents'] if a['id'] == 'producer')['lead'] = 'technical-director'
        path.write_text(json.dumps(data))
        self.assertTrue(any('Lead cycle' in e for e in validate.validate(copy)))

    def test_agent_path_escape_rejected(self):
        copy = self.copy(); path = copy / 'studio/agents.json'
        data = json.loads(path.read_text()); data['agents'][0]['file'] = '../elsewhere'
        path.write_text(json.dumps(data))
        self.assertTrue(any('Invalid agent path' in e for e in validate.validate(copy)))

    def test_existing_config_preserved_before_writes(self):
        game = self.base / 'game'; (game / '.codex').mkdir(parents=True)
        config = game / '.codex/config.toml'; config.write_text('# existing')
        with self.assertRaises(ValueError): install.install(game, apply=True)
        self.assertEqual('# existing', config.read_text())
        self.assertFalse((game / 'AGENTS.md').exists())

    def test_installed_routing_cli_works(self):
        game = self.base / 'game'; game.mkdir(); install.install(game, apply=True)
        result = subprocess.run([sys.executable, str(game / 'studio/tools/studio.py'), 'route', '--area', 'network', '--engine', 'unreal'], capture_output=True, text=True, cwd=self.base)
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn('ue-replication-specialist', json.loads(result.stdout)['suggested_roles'])
        result = subprocess.run([sys.executable, str(game / 'studio/tools/studio.py'), 'list'], capture_output=True, text=True)
        self.assertEqual(49, len(result.stdout.strip().splitlines()))

    def test_cli_invalid_role_fails_without_writes(self):
        before = list(self.base.iterdir())
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/studio.py'), 'brief', '--role', 'unknown', '--task', 'test'], capture_output=True, text=True, cwd=self.base)
        self.assertNotEqual(0, result.returncode)
        self.assertEqual(before, list(self.base.iterdir()))


if __name__ == '__main__': unittest.main()
