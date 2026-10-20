"""tools/lib/mcfn.py : écriture des .mcfunction et crochets idempotents (patch, replace, go_range), testés dans un dossier temporaire.
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v   (la racine du dépôt est dérivée de ce fichier).
"""
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'lib'))
import mcfn  # noqa: E402

GO = 'execute unless score @s mg.go matches 1..{n} unless score $game mg.st matches 1 run say go\n'


class FnCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.fdir = Path(self._tmp.name)
        self.fn = mcfn.Fn(str(self.fdir))

    def put(self, rel, text):
        p = self.fdir / (rel + '.mcfunction')
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(text.encode('utf-8'))

    def get(self, rel):
        return (self.fdir / (rel + '.mcfunction')).read_bytes().decode('utf-8')


class WriteTest(FnCase):
    def test_write_adds_final_newline_and_makes_dirs(self):
        self.fn.write('a/b/c', ['x', 'y'])
        self.assertEqual(self.get('a/b/c'), 'x\ny\n')

    def test_lines_of_roundtrip(self):
        self.put('f', 'x\ny\n')
        self.assertEqual(self.fn.lines_of('f'), ['x', 'y', ''])

    def test_lines_of_crlf_has_no_cr(self):
        self.put('f', 'x\r\ny\r\n')
        lines = self.fn.lines_of('f')
        self.assertFalse(any('\r' in l for l in lines))
        self.assertEqual(lines[:2], ['x', 'y'])

    def test_js_is_compact_and_keeps_unicode(self):
        self.assertEqual(mcfn.js({'a': ['é', 1]}), '{"a":["é",1]}')


class PatchTest(FnCase):
    def test_insert_after_and_before(self):
        self.put('f', 'a\nb\nc')
        self.fn.patch('f', 'b', ['x'])
        self.assertEqual(self.get('f'), 'a\nb\nx\nc')
        self.fn.patch('f', 'a', ['y'], where='before')
        self.assertEqual(self.get('f'), 'y\na\nb\nx\nc')

    def test_no_final_newline_added(self):
        self.put('f', 'a\nb\n')
        self.fn.patch('f', 'a', ['x'])
        self.assertEqual(self.get('f'), 'a\nx\nb\n')

    def test_nothing_rewritten_when_already_done(self):
        self.put('f', 'a\nx\nb')
        p = self.fdir / 'f.mcfunction'
        before = p.stat().st_mtime_ns
        self.fn.patch('f', 'zzz-absent', ['x'])         # déjà présent : l'ancre n'est même pas cherchée
        self.assertEqual(self.get('f'), 'a\nx\nb')
        self.assertEqual(p.stat().st_mtime_ns, before)

    def test_missing_anchor_exits(self):
        self.put('f', 'a\nb')
        with self.assertRaises(SystemExit):
            self.fn.patch('f', 'zzz', ['x'])
        self.assertEqual(self.get('f'), 'a\nb')

    def test_duplicate_anchor_exits(self):
        self.put('f', 'a\nb\na')
        with self.assertRaises(SystemExit):
            self.fn.patch('f', 'a', ['x'])
        self.assertEqual(self.get('f'), 'a\nb\na')

    def test_bad_where_raises_and_leaves_file(self):
        self.put('f', 'a\nb')
        with self.assertRaises(ValueError):
            self.fn.patch('f', 'a', ['x'], where='afterr')
        self.assertEqual(self.get('f'), 'a\nb')

    def test_rerun_is_idempotent(self):
        self.put('f', 'a\nb')
        self.fn.patch('f', 'a', ['x', 'y'])
        once = self.get('f')
        self.fn.patch('f', 'a', ['x', 'y'])
        self.assertEqual(self.get('f'), once)


class ReplaceTest(FnCase):
    def test_replace_once_then_idempotent(self):
        self.put('f', 'say old\nsay b')
        self.fn.replace('f', 'old', 'new')
        self.assertEqual(self.get('f'), 'say new\nsay b')
        self.fn.replace('f', 'old', 'new')
        self.assertEqual(self.get('f'), 'say new\nsay b')

    def test_missing_or_duplicate_exits(self):
        self.put('f', 'old\nold')
        with self.assertRaises(SystemExit):
            self.fn.replace('f', 'old', 'new')
        with self.assertRaises(SystemExit):
            self.fn.replace('f', 'zzz', 'new')
        self.assertEqual(self.get('f'), 'old\nold')


class DropLinesTest(FnCase):
    def test_drop_exact_lines_only(self):
        self.put('f', 'a\nb\nab\nc')
        self.fn.drop_lines('f', ['a', 'c'])
        self.assertEqual(self.get('f'), 'b\nab')

    def test_nothing_to_drop_leaves_file(self):
        self.put('f', 'a\nb\n')
        self.fn.drop_lines('f', ['zzz'])
        self.assertEqual(self.get('f'), 'a\nb\n')


class GoRangeTest(FnCase):
    def test_widens_never_narrows(self):
        self.put('core/go', GO.format(n=80))
        self.fn.go_range(234)
        self.assertEqual(self.get('core/go'), GO.format(n=234))
        self.fn.go_range(100)
        self.assertEqual(self.get('core/go'), GO.format(n=234))

    def test_equal_gid_unchanged(self):
        self.put('core/go', GO.format(n=80))
        self.fn.go_range(80)
        self.assertEqual(self.get('core/go'), GO.format(n=80))

    def test_pattern_absent_exits(self):
        self.put('core/go', 'say rien\n')
        with self.assertRaises(SystemExit):
            self.fn.go_range(5)


if __name__ == '__main__':
    unittest.main()
