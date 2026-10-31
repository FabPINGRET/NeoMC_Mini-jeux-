"""Chaque bouton de carte des menus (mg.go set <id>, vote mg.vote set 1000+<id>) affiche la taille de la carte dans son infobulle."""
import json
import os
import re
import sys
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
sys.path.insert(0, os.path.join(ROOT, 'tools', 'variantes'))
import var_sizes as VS  # noqa: E402

DIALOG = os.path.join(ROOT, 'data', 'mg', 'dialog')
VARIANT = re.compile(r'trigger mg\.(?:go set |vote set 1)(1\d\d)$')   # variantes ✦ 100..189 (190..196 = au hasard)


class MapSizes(unittest.TestCase):
    def test_every_map_button_shows_its_size(self):
        missing = []
        for f in sorted(os.listdir(DIALOG)):
            d = json.load(open(os.path.join(DIALOG, f), encoding='utf-8'))
            for a in d.get('actions', []) or []:
                i, tip = VS.map_id(a), VS.text(a.get('tooltip', ''))
                cmd = a.get('action', {}).get('command', '')
                m = VARIANT.match(cmd)
                variant = bool(m) and int(m.group(1)) < 190
                if (i in VS.SIZES or variant) and not (VS.HAS_SIZE.search(tip) or (i in VS.SIZES and VS.SIZES[i] in tip)):
                    missing.append(f'{f} : {VS.text(a["label"])}')
        self.assertEqual(missing, [], 'cartes sans taille (relancer tools/variantes/gen_variants.py)')


if __name__ == '__main__':
    unittest.main()
