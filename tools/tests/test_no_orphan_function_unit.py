"""Cas unitaires des aides de test_no_orphan_function : prefixe ALLOWED et auto-citation."""
import unittest
from pathlib import Path

import test_no_orphan_function as t


class Allowed(unittest.TestCase):
    def test_prefix_covers_root_and_children(self):
        self.assertTrue(t.allowed('setup'))            # racine couverte par le prefixe `setup/`
        self.assertTrue(t.allowed('setup/menu_x'))
        self.assertTrue(t.allowed('admin/a/b'))

    def test_prefix_is_not_a_substring_match(self):
        self.assertFalse(t.allowed('setupx'))
        self.assertFalse(t.allowed('xsetup/a'))
        self.assertFalse(t.allowed('admins/a'))

    def test_exact_name_does_not_cover_children(self):
        self.assertTrue(t.allowed('installer'))
        self.assertFalse(t.allowed('installer/x'))
        self.assertFalse(t.allowed('installe'))


class OwnName(unittest.TestCase):
    def test_mcfunction_in_function_dir(self):
        self.assertEqual(t.own_name(t.FUNC / 'a' / 'b.mcfunction'), 'a/b')
        self.assertEqual(t.own_name(t.FUNC / 'root.mcfunction'), 'root')

    def test_other_files_have_no_own_name(self):
        self.assertIsNone(t.own_name(t.ROOT / 'data' / 'mg' / 'tags' / 'function' / 'x.json'))
        self.assertIsNone(t.own_name(t.ROOT / 'tools' / 'x.py'))
        self.assertIsNone(t.own_name(Path('elsewhere') / 'y.mcfunction'))


if __name__ == '__main__':
    unittest.main()
