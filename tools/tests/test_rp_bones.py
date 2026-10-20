"""Resource pack : os articulés des dinos (Terra Nova) et des bêtes (Ombrelune), générés par tools/resourcepack/dino_rp.py et ol_rp.py.
Vérifie dans resourcepack/ et data/ : pas de modèle dupliqué dans une espèce, items -> modèles existants, textures toutes utilisées,
et chaque item_model mg:dino/... | mg:beast/... posé par une fonction a son fichier items/.
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v   (la racine du dépôt est dérivée de ce fichier).
"""
import json
import re
import unittest
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / 'resourcepack' / 'assets' / 'mg'
FUNC = ROOT / 'data' / 'mg' / 'function'
FAMILIES = ('dino', 'beast')
ITEM_MODEL = re.compile(r'item_model":"mg:((?:dino|beast)/[a-z0-9_]+)"')


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def models(family):
    return sorted((ASSETS / 'models' / 'item' / family).glob('*.json'))


class RpBones(unittest.TestCase):
    def test_families_found(self):
        for fam in FAMILIES:
            self.assertTrue(models(fam), f'aucun modèle {fam} : lancer tools/resourcepack/gen_rp.py .')
            self.assertTrue(list((ASSETS / 'items' / fam).glob('*.json')), f'aucun item {fam}')

    def test_no_duplicate_model_in_species(self):
        for fam in FAMILIES:
            seen = defaultdict(dict)                    # espèce -> {contenu trié: premier fichier}
            for p in models(fam):
                # les noms sont <espèce>_<os> : ni clé d'espèce ni nom d'os ne contiennent « _ » (sinon split('_')[0] grouperait mal)
                self.assertEqual(p.stem.count('_'), 1, f'{fam}/{p.name} : attendu <espèce>_<os> sans autre « _ »')
                species = p.stem.split('_')[0]
                content = json.dumps(load(p), sort_keys=True)
                first = seen[species].setdefault(content, p.name)
                self.assertEqual(first, p.name, f'{fam}/{species} : {p.name} est identique à {first} (un seul modèle par contenu)')

    def test_items_point_to_existing_models(self):
        for fam in FAMILIES:
            for p in sorted((ASSETS / 'items' / fam).glob('*.json')):
                model = load(p)['model']['model']
                prefix = f'mg:item/{fam}/{p.stem.split("_")[0]}_'
                self.assertTrue(model.startswith(prefix), f'{p.name} : modèle hors espèce ({model}, attendu {prefix}...)')
                target = ASSETS / 'models' / 'item' / (model[len('mg:item/'):] + '.json')
                self.assertTrue(target.is_file(), f'{p.name} -> {model} : modèle absent')

    def test_item_shape_and_no_orphan_model(self):
        for fam in FAMILIES:
            pointed = set()
            for p in sorted((ASSETS / 'items' / fam).glob('*.json')):
                data = load(p)
                self.assertEqual(list(data), ['model'], f'{p.name} : seul le champ « model » est attendu')
                self.assertEqual(sorted(data['model']), ['model', 'type'], f'{p.name} : forme inattendue')
                self.assertEqual(data['model']['type'], 'minecraft:model', p.name)
                pointed.add(data['model']['model'])
            for m in models(fam):
                self.assertIn(f'mg:item/{fam}/{m.stem}', pointed, f'modèle {fam}/{m.name} pointé par aucun item')

    def test_every_texture_is_referenced(self):
        for fam in FAMILIES:
            used = set()
            for p in models(fam):
                used.update(v for v in load(p)['textures'].values())
            for p in sorted((ASSETS / 'textures' / 'item' / fam).glob('*.png')):
                self.assertIn(f'mg:item/{fam}/{p.stem}', used, f'texture {fam}/{p.name} jamais référencée par un modèle')
            for ref in sorted(used):
                self.assertTrue((ASSETS / 'textures' / (ref[len('mg:'):] + '.png')).is_file(), f'texture {ref} absente')

    def test_every_item_model_in_data_has_an_item(self):
        found = set()
        for p in FUNC.rglob('*.mcfunction'):
            found.update(ITEM_MODEL.findall(p.read_text(encoding='utf-8')))
        self.assertTrue(found, 'aucun item_model mg:dino/ ou mg:beast/ dans data/ : lancer gen_terranova.py et gen_ombrelune.py')
        for name in sorted(found):
            self.assertTrue((ASSETS / 'items' / (name + '.json')).is_file(), f'item_model mg:{name} sans items/{name}.json')


if __name__ == '__main__':
    unittest.main()
