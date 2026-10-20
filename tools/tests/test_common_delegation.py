"""common.py (arcade) et var_common.py (variantes) delegant a tools/lib/mcfn.py : alias poses par init, comportement conserve."""
import os
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / 'tools' / sub) for sub in ('arcade', 'variantes') if str(ROOT / 'tools' / sub) not in sys.path]
import common
import var_common

CLONE = {'sfx': '2', 'keys': ['koth'], 'ids': {'86': 206}, 'entry': 'koth', 'label': 'x', 'p': {}}
TX_IN = ['function mg:koth/go', 'execute if score $game mg.st matches 86 run say hi']


class Base(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = tmp.name
        os.makedirs(os.path.join(self.root, 'data/mg/function/core'))

    def path(self, rel):
        return Path(self.root) / 'data/mg/function' / (rel + '.mcfunction')

    def read(self, rel):
        return self.path(rel).read_bytes().decode('utf-8')


class CommonDelegation(Base):
    def setUp(self):
        super().setUp()
        self.addCleanup(setattr, common, 'MAP', common.MAP)   # _finish (atexit) ne fait rien si MAP est None
        common.MAP = None
        common.init(self.root)

    def test_write_and_lines_of(self):
        common.w('x/y', ['a'])
        self.assertEqual(self.read('x/y'), 'a\n')
        self.assertEqual(common.lines_of('x/y'), ['a', ''])   # l'element vide vient du \n final

    def test_patch_idempotent_and_unknown_anchor(self):
        common.w('x/y', ['a'])
        common.patch('x/y', 'a', ['b'])
        self.assertEqual(self.read('x/y'), 'a\nb\n')
        os.utime(self.path('x/y'), (1000, 1000))
        common.patch('x/y', 'a', ['b'])
        self.assertEqual(int(self.path('x/y').stat().st_mtime), 1000)   # pas de reecriture
        with self.assertRaises(SystemExit):
            common.patch('x/y', 'zzz', ['c'])

    def test_patch_applies_tx_with_map(self):
        common.w('x/y', ['a'])
        common.MAP = dict(CLONE)
        common.patch('x/y', 'a', TX_IN)
        common.patch('x/y', 'a', TX_IN)
        self.assertEqual(self.read('x/y'),
                         'a\nfunction mg:koth2/go\nexecute if score $game mg.st matches 206 run say hi\n')

    def test_go_range(self):
        common.w('core/go', ['say rien'])
        common.go_range(99)                                   # motif absent : silencieux, fichier intact
        self.assertEqual(self.read('core/go'), 'say rien\n')
        common.w('core/go', ['execute unless score @s mg.go matches 1..5 unless entity @s'])
        common.go_range(9)
        common.go_range(3)                                    # jamais l'inverse
        self.assertIn('matches 1..9 unless', self.read('core/go'))


class VarCommonDelegation(Base):
    def setUp(self):
        super().setUp()
        n = len(var_common.written)
        self.addCleanup(lambda: var_common.written.__delitem__(slice(n, None)))
        var_common.init(self.root)

    def test_w_records_path(self):
        var_common.w('x/y', ['a', 'b'])
        self.assertEqual(self.read('x/y'), 'a\nb\n')
        self.assertEqual(Path(var_common.written[-1]), self.path('x/y'))

    def test_replace_idempotent_and_drop_lines(self):
        var_common.w('x/y', ['a', 'b', 'c'])
        var_common.replace('x/y', 'b', 'B')
        var_common.replace('x/y', 'b', 'B')
        self.assertEqual(self.read('x/y'), 'a\nB\nc\n')
        var_common.drop_lines('x/y', ['B'])
        var_common.drop_lines('x/y', ['B'])                   # deja retiree : sans effet
        self.assertEqual(self.read('x/y'), 'a\nc\n')
