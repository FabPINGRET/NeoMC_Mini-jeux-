"""Scission des fichiers de la carte (tools/resourcepack/floaty_split.py) : pack serveur forcé / pack optionnel.
Données synthétiques (manifeste et carte écrits ici : ni jar, ni carte, ni manifeste commité) ; le vrai manifeste est relu seulement par test_floaty_manifest.py.
Ici : contenu exact des deux packs, réécriture des références, classification, renommage, enveloppe, gardes (SystemExit qui liste les chemins),
pureté et reproductibilité octet pour octet. Les invariants (verifie() et ses cas inverses sur sorties falsifiées) sont dans test_floaty_split_inv.py,
qui importe les fixtures de ce fichier.
Lancer : python -m unittest discover -s tools/tests -v (racine dérivée de ce fichier).
"""
import copy
import importlib.util
import json
import random
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RP = ROOT / 'tools' / 'resourcepack'
spec = importlib.util.spec_from_file_location('floaty_split', RP / 'floaty_split.py')
fs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fs)

MC = 'assets/minecraft/'
SWORD, APPLE, ROD, DARK = MC + 'items/sword.json', MC + 'items/apple.json', MC + 'items/rod.json', MC + 'items/darkcompass.json'


def js(obj):
    return json.dumps(obj, indent=2).encode('utf-8')


def mdl(ref):
    return {'type': 'minecraft:model', 'model': ref}


VANILLA_SWORD = {'model': mdl('minecraft:item/sword'), 'oversized_in_gui': True}
MAP_SWORD = {'model': {'type': 'select', 'property': 'custom_model_data', 'fallback': mdl('item/sword'),
                       'cases': [{'when': '1', 'model': mdl('item/custom')}, {'when': '2', 'model': mdl('item/apple_child')}]}}
EXTRA = {
    MC + 'sounds.json': b'{}', MC + 'sounds/z/s.ogg': b'ogg', DARK: js({'model': mdl('minecraft:item/darkcompass_00')}),
    SWORD: js(MAP_SWORD), MC + 'models/item/custom.json': js({'parent': 'item/generated', 'textures': {'layer0': 'item/fresh'}}),
    MC + 'models/item/rod.json': js({'parent': 'item/handheld', 'textures': {'layer0': 'item/fresh'}}),
    MC + 'textures/item/apple.png': b'apple', MC + 'textures/item/apple.png.mcmeta': b'{"animation": {}}', MC + 'textures/item/fresh.png': b'fresh',
    MC + 'textures/block/stone.png': b'stone', MC + 'textures/block/stone.png.mcmeta': b'{"animation": {}}', MC + 'textures/block/new.png': b'new',
    MC + 'textures/entity/zombie/zombie.png': b'zombie', MC + 'textures/misc/enchanted_glint_entity.png': b'glint',
}
REPLACED = {'items': [SWORD], 'models': [MC + 'models/item/rod.json'], 'textures_item': [MC + 'textures/item/apple.png'],
            'textures_block': [MC + 'textures/block/stone.png'], 'textures_entity': [MC + 'textures/entity/zombie/zombie.png'],
            'mcmeta': [MC + 'textures/item/apple.png.mcmeta', MC + 'textures/block/stone.png.mcmeta']}
PACK_FMT = {'min_format': [88, 0], 'max_format': [88, 99]}
MANIFEST = {
    'names_sha256': fs.floaty_names_digest(EXTRA), 'version': {'id': '26.2', 'resource': [88, 0]},
    'sounds': {'new': ['zelda.a'], 'dropped': ['music.end']}, 'replaced': REPLACED, 'dropped': [MC + 'textures/misc/enchanted_glint_entity.png'],
    'items': {SWORD: VANILLA_SWORD, APPLE: {'model': mdl('minecraft:item/apple')}, ROD: {'model': mdl('minecraft:item/rod')}},
    'models': {MC + 'models/item/apple.json': {'parent': 'minecraft:item/generated', 'textures': {'layer0': 'minecraft:item/apple'}},
               MC + 'models/item/apple_child.json': {'parent': 'item/apple'}},
}


def split(extra=None, man=None, pack_fmt=None):
    return fs.floaty_split(copy.deepcopy(EXTRA if extra is None else extra), pack_fmt, copy.deepcopy(MANIFEST if man is None else man))


def plus(files, man=None):
    """(extra, manifeste) : EXTRA plus files, empreinte du manifeste recalculée (les fichiers ajoutés sont des fichiers neufs de la carte)."""
    extra = {**EXTRA, **files}
    man = copy.deepcopy(MANIFEST if man is None else man)
    man['names_sha256'] = fs.floaty_names_digest(extra)
    return extra, man


class Invariants(unittest.TestCase):
    def setUp(self):
        self.server, self.opt = split()

    def test_exact_contents(self):
        self.assertEqual(sorted(self.opt), [MC + 'textures/block/stone.png', MC + 'textures/block/stone.png.mcmeta', MC + 'textures/entity/zombie/zombie.png'])
        self.assertEqual(sorted(self.server), sorted([
            MC + 'sounds.json', MC + 'sounds/z/s.ogg', DARK, SWORD, APPLE, ROD, MC + 'models/item/custom.json', MC + 'textures/item/fresh.png',
            MC + 'textures/block/new.png', 'assets/floaty/textures/item/apple.png', 'assets/floaty/textures/item/apple.png.mcmeta',
            'assets/floaty/models/item/rod.json', 'assets/floaty/models/item/apple.json', 'assets/floaty/models/item/apple_child.json']))

    def test_new_files_are_untouched_and_replaced_textures_move(self):
        for p in (MC + 'sounds.json', DARK, MC + 'models/item/custom.json', MC + 'textures/item/fresh.png'):
            self.assertEqual(self.server[p], EXTRA[p], p)
        self.assertEqual(self.server['assets/floaty/textures/item/apple.png'], b'apple')
        self.assertEqual(self.server['assets/floaty/textures/item/apple.png.mcmeta'], b'{"animation": {}}')
        self.assertNotIn(MC + 'textures/item/apple.png', self.server)

    def test_map_item_becomes_the_floaty_case_with_rewritten_refs(self):
        sel = json.loads(self.server[SWORD].decode('utf-8'))['model']
        self.assertEqual(sel['fallback'], VANILLA_SWORD['model'])
        case = sel['cases'][0]['model']
        self.assertEqual(case['fallback'], mdl('item/sword'))                                       # pas un modèle renommé : inchangé
        self.assertEqual([c['model']['model'] for c in case['cases']], ['item/custom', 'floaty:item/apple_child'])
        self.assertTrue(json.loads(self.server[SWORD].decode('utf-8'))['oversized_in_gui'])        # autre clé vanilla conservée

    def test_vanilla_only_item_is_wrapped_with_its_rewritten_model(self):
        sel = json.loads(self.server[APPLE].decode('utf-8'))['model']
        self.assertEqual(sel['cases'], [{'when': 'mg:floaty', 'model': mdl('floaty:item/apple')}])
        self.assertEqual(sel['fallback'], mdl('minecraft:item/apple'))
        rod = json.loads(self.server[ROD].decode('utf-8'))['model']
        self.assertEqual(rod['cases'][0]['model'], mdl('floaty:item/rod'))                          # modèle remplacé par la carte

    def test_renamed_models_have_rewritten_textures_and_parent(self):
        apple = json.loads(self.server['assets/floaty/models/item/apple.json'].decode('utf-8'))
        self.assertEqual(apple, {'parent': 'minecraft:item/generated', 'textures': {'layer0': 'floaty:item/apple'}})
        self.assertEqual(json.loads(self.server['assets/floaty/models/item/apple_child.json'].decode('utf-8')), {'parent': 'floaty:item/apple'})
        rod = json.loads(self.server['assets/floaty/models/item/rod.json'].decode('utf-8'))
        self.assertEqual(rod, {'parent': 'item/handheld', 'textures': {'layer0': 'item/fresh'}})

    def test_special_base_is_rewritten(self):
        man = copy.deepcopy(MANIFEST)
        vanilla = {'model': {'type': 'minecraft:special', 'base': 'minecraft:item/apple', 'model': {'type': 'minecraft:trident'}}}
        man['items'][APPLE] = vanilla
        server, _ = split(man=man)
        sel = json.loads(server[APPLE].decode('utf-8'))['model']
        self.assertEqual(sel['cases'][0]['model']['base'], 'floaty:item/apple')
        self.assertEqual(sel['fallback'], vanilla['model'])

    def test_dropped_is_in_no_pack(self):
        p = MC + 'textures/misc/enchanted_glint_entity.png'
        self.assertNotIn(p, self.server)
        self.assertNotIn(p, self.opt)

    def test_empty_input_gives_two_empty_packs(self):
        self.assertEqual(fs.floaty_split({}), ({}, {}))
        self.assertEqual(fs.floaty_split({}, PACK_FMT, copy.deepcopy(MANIFEST)), ({}, {}))


class Passthrough(unittest.TestCase):
    """Les modèles et items JSON neufs de la carte qui lisent une texture item ou un modèle renommé sont réécrits vers floaty: ; le reste, jamais."""
    def test_new_model_reading_a_renamed_texture_or_parent_is_rewritten(self):
        extra, man = plus({MC + 'models/item/held.json': js({'parent': 'item/handheld', 'textures': {'layer0': 'minecraft:item/apple', 'layer1': 'item/fresh'}}),
                           MC + 'models/block/kid.json': js({'parent': 'minecraft:item/apple_child'})})
        server, _ = split(extra, man)
        held = json.loads(server[MC + 'models/item/held.json'].decode('utf-8'))
        self.assertEqual(held['textures'], {'layer0': 'floaty:item/apple', 'layer1': 'item/fresh'})          # seule la texture déplacée change
        self.assertEqual(held['parent'], 'item/handheld')
        self.assertEqual(json.loads(server[MC + 'models/block/kid.json'].decode('utf-8')), {'parent': 'floaty:item/apple_child'})

    def test_new_item_reading_a_renamed_model_is_rewritten(self):
        extra, man = plus({MC + 'items/brand.json': js({'model': mdl('minecraft:item/apple'), 'oversized_in_gui': True})})
        server, _ = split(extra, man)
        brand = json.loads(server[MC + 'items/brand.json'].decode('utf-8'))
        self.assertEqual(brand, {'model': mdl('floaty:item/apple'), 'oversized_in_gui': True})

    def test_files_without_renamed_refs_keep_their_exact_bytes(self):
        raw = {MC + 'models/item/plain.json': b'{"parent":"item/handheld","textures":{"layer0":"mg:item/apple"}}',      # autre espace de noms : jamais réécrit
               MC + 'items/plain.json': b'{ "model" : {"type":"minecraft:model","model":"item/fresh"} }',
               MC + 'models/item/list.json': b'[1, 2]', MC + 'textures/item/apple.json': b'{"model": "item/apple"}'}      # pas un modèle / un item : intact
        extra, man = plus(raw)
        server, _ = split(extra, man)
        for path, data in raw.items():
            self.assertEqual(server[path], data, path)

    def test_unreadable_new_model_names_the_file(self):
        extra, man = plus({MC + 'models/item/broken.json': b'{pas du json'})
        with self.assertRaises(SystemExit) as cm:
            split(extra, man)
        self.assertIn(MC + 'models/item/broken.json', str(cm.exception))


class Purity(unittest.TestCase):
    def test_inputs_are_not_modified(self):
        extra, man = copy.deepcopy(EXTRA), copy.deepcopy(MANIFEST)
        fs.floaty_split(extra, PACK_FMT, man)
        self.assertEqual((extra, man), (EXTRA, MANIFEST))

    def test_reproducible_and_independent_of_input_order(self):
        first = split()
        keys = list(EXTRA)
        random.Random(7).shuffle(keys)
        again = split({k: EXTRA[k] for k in keys})
        self.assertEqual(first, again)
        self.assertEqual(list(first[0]), list(again[0]))          # même ordre d'insertion
        self.assertEqual(list(first[1]), list(again[1]))

    def test_manifest_is_read_once_from_floaty_vanilla_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'm.json'
            path.write_text(json.dumps(MANIFEST), encoding='utf-8')
            old = fs.FLOATY_MANIFEST
            fs.FLOATY_MANIFEST = str(path)
            try:
                self.assertEqual(fs.floaty_split(copy.deepcopy(EXTRA)), split())
            finally:
                fs.FLOATY_MANIFEST = old
        self.assertEqual(Path(old), RP / 'floaty_vanilla.json')

    def test_names_digest_is_order_independent(self):
        self.assertEqual(fs.floaty_names_digest(['b', 'a']), fs.floaty_names_digest(['a', 'b']))
        self.assertNotEqual(fs.floaty_names_digest(['a', 'b']), fs.floaty_names_digest(['a', 'c']))


class Units(unittest.TestCase):
    IX = fs.floaty_sets(MANIFEST)

    def test_classify(self):
        cases = {MC + 'textures/misc/enchanted_glint_entity.png': 'drop', SWORD: 'wrap', MC + 'textures/item/apple.png': 'rename',
                 MC + 'textures/item/apple.png.mcmeta': 'rename', MC + 'models/item/rod.json': 'rename', MC + 'textures/block/stone.png': 'opt',
                 MC + 'textures/block/stone.png.mcmeta': 'opt', MC + 'textures/entity/zombie/zombie.png': 'opt', DARK: 'server',
                 MC + 'textures/item/fresh.png': 'server', MC + 'sounds.json': 'server'}
        for path, kind in cases.items():
            self.assertEqual(fs.floaty_classify(path, self.IX), kind, path)

    def test_rename(self):
        self.assertEqual(fs.floaty_rename(MC + 'textures/item/a/b.png'), 'assets/floaty/textures/item/a/b.png')
        self.assertEqual(fs.floaty_rename(MC + 'models/item/m.json'), 'assets/floaty/models/item/m.json')
        for bad in (MC + 'textures/block/stone.png', MC + 'items/sword.json', MC + 'models/block/x.json'):
            with self.assertRaises(ValueError):
                fs.floaty_rename(bad)

    def test_id_and_ref(self):
        self.assertEqual(fs.floaty_id('minecraft:item/x'), 'item/x')
        self.assertEqual(fs.floaty_id('item/x'), 'item/x')
        self.assertEqual(fs.floaty_id('mg:item/x'), 'mg:item/x')
        self.assertEqual(fs.floaty_ref('mg:item/apple', {'item/apple'}), 'mg:item/apple')       # autre espace de noms : jamais réécrit
        self.assertEqual(fs.floaty_ref('item/apple', {'item/apple'}), 'floaty:item/apple')

    def test_wrap_item_keeps_other_keys_and_does_not_alias_vanilla(self):
        vanilla = {'model': mdl('minecraft:item/x'), 'hand_animation_on_swap': False, 'swap_animation_scale': 2.0}
        before = copy.deepcopy(vanilla)
        out = fs.floaty_wrap_item(vanilla, mdl('floaty:item/x'))
        self.assertEqual({k: v for k, v in out.items() if k != 'model'}, {'hand_animation_on_swap': False, 'swap_animation_scale': 2.0})
        self.assertEqual(out['model'], {'type': 'minecraft:select', 'property': 'minecraft:context_dimension',
                                        'cases': [{'when': 'mg:floaty', 'model': mdl('floaty:item/x')}], 'fallback': mdl('minecraft:item/x')})
        out['model']['fallback']['model'] = 'changed'
        self.assertEqual(vanilla, before)

    def test_encode_is_deterministic_lf_utf8(self):
        data = fs.floaty_encode({'a': 'é', 'b': [1, 2]})
        self.assertTrue(data.endswith(b'\n') and b'\r' not in data)
        self.assertEqual(json.loads(data.decode('utf-8')), {'a': 'é', 'b': [1, 2]})
        self.assertEqual(data, fs.floaty_encode({'a': 'é', 'b': [1, 2]}))


if __name__ == '__main__':
    unittest.main()
