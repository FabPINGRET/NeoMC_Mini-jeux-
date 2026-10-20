"""Ombrelune : la façade tools/arcade/ol_structs.py expose les mêmes noms qu'avant la découpe en modules ol_*.
Lancer depuis la racine du dépôt : python -m unittest discover -s tools/tests -v   (la racine est dérivée de ce fichier).
"""
import importlib
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARCADE = ROOT / 'tools' / 'arcade'
SOURCE_MAX = 500                                        # plafond dur (cible 300)
# noms lus par les consommateurs (gen_ombrelune, ol_boss, ol_cine, ol_mobs, ol_quest : grep `S\.<nom>`) + état partagé
USED = ('SPOTS', 'DUNGEONS', 'ARENAS', 'LORE', 'CHESTS', 'G', 'DUN_THEMES', 'all_structures', 'dir_vec')
# modules issus de la découpe d'ol_structs.py : ceux qui importent l'état depuis ol_skit (façade comprise), ol_skit exclu (c'est la référence)
SPLIT = tuple(p.stem for p in sorted(ARCADE.glob('ol_*.py'))
              if p.stem != 'ol_skit' and 'from ol_skit import' in p.read_text(encoding='utf-8'))
STATE = ('SPOTS', 'DUNGEONS', 'ARENAS', 'LORE', 'CHESTS', 'G')
# les 22 bâtisseurs appelés par all_structures() + dungeon
BUILDERS = ('city', 'brumecombe', 'windmill', 'bandit_fort', 'chapel', 'aelindor', 'spider_lair', 'shrine', 'hrafnheim', 'giant_hold',
            'stilt_village', 'witch_isle', 'oasis_town', 'pyramid', 'obelisks', 'bastion', 'caldera', 'dwarf_camp', 'dwarf_gate',
            'rebel_camp', 'citadel', 'soul_well_entry', 'dungeon')
# ol_quest.py et ol_world.py dépassaient déjà le plafond avant la découpe (hors périmètre du lot)
SIZE_EXEMPT = {'ol_quest', 'ol_world'}

if str(ARCADE) not in sys.path:
    sys.path.insert(0, str(ARCADE))
import ol_structs   # noqa: E402
import ol_skit      # noqa: E402


class OlStructsFacade(unittest.TestCase):
    def test_used_names_exposed(self):
        for name in USED:
            self.assertTrue(hasattr(ol_structs, name), 'ol_structs.%s manquant' % name)

    def test_state_is_shared(self):
        """Un SPOTS = {} local dans un module bâtisseur casserait le partage : chaque module qui expose un nom d'état doit avoir celui d'ol_skit."""
        for modname in SPLIT:
            mod = importlib.import_module(modname)
            for name in STATE:
                if hasattr(mod, name):
                    self.assertIs(getattr(mod, name), getattr(ol_skit, name), '%s.%s : objet d\'état différent de ol_skit' % (modname, name))

    def test_builders_exposed(self):
        for name in BUILDERS:
            self.assertTrue(callable(getattr(ol_structs, name, None)), 'ol_structs.%s manquant' % name)

    def test_sources_size(self):
        for p in sorted(ARCADE.glob('ol_*.py')):
            if p.stem in SIZE_EXEMPT:
                continue
            n = len(p.read_text(encoding='utf-8').splitlines())
            self.assertLessEqual(n, SOURCE_MAX, '%s : %d lignes (plafond %d)' % (p.name, n, SOURCE_MAX))


if __name__ == '__main__':
    unittest.main()
