"""Ombrelune : chaque fonction réexportée par la façade ol_structs est l'objet défini dans son module de découpe,
et la façade ne définit elle-même que all_structures. Lancer : python -m unittest discover -s tools/tests -v
"""
import importlib
import sys
import types
import unittest
from pathlib import Path

ARCADE = Path(__file__).resolve().parents[2] / 'tools' / 'arcade'
SPLIT = ('ol_skit', 'ol_city', 'ol_city_b', 'ol_hamlets', 'ol_dungeons', 'ol_region_nord', 'ol_region_est', 'ol_region_sud')
BUILDERS = ('city', 'castle', 'temple', 'mage_tower', 'guild', 'tavern', 'forge_b', 'market', 'stables', 'alchemist',
            'village', 'brumecombe', 'windmill', 'bandit_fort', 'dungeon', 'giant_tree', 'rope_bridge', 'aelindor', 'spider_lair',
            'shrine', 'longhouse', 'hrafnheim', 'giant_hold', 'stilt_village', 'witch_isle', 'oasis_town', 'pyramid', 'obelisks',
            'bastion', 'caldera', 'dwarf_camp', 'dwarf_gate', 'rebel_camp', 'citadel', 'soul_well_entry', 'chapel')
TOOLS = ('spot', 'dir_vec', 'opp', 'cone_roof', 'round_tower', 'crenels', 'brace_ladders', 'stone_mix', 'house')

if str(ARCADE) not in sys.path:
    sys.path.insert(0, str(ARCADE))
import ol_structs   # noqa: E402


class OlStructsIdentity(unittest.TestCase):
    def test_reexports_are_split_module_objects(self):
        for name in BUILDERS + TOOLS:
            fn = getattr(ol_structs, name)
            self.assertIsInstance(fn, types.FunctionType, name)
            self.assertIn(fn.__module__, SPLIT, '%s defini hors des modules de decoupe : %s' % (name, fn.__module__))
            origin = importlib.import_module(fn.__module__)
            self.assertIs(fn, getattr(origin, name), name)

    def test_facade_defines_only_all_structures(self):
        own = [k for k, v in vars(ol_structs).items() if isinstance(v, types.FunctionType) and v.__module__ == ol_structs.__name__]
        self.assertEqual(own, ['all_structures'])
        for k, v in vars(ol_structs).items():
            if isinstance(v, types.FunctionType) and k != 'all_structures':
                self.assertNotEqual(v.__module__, 'ol_structs', k)


if __name__ == '__main__':
    unittest.main()
