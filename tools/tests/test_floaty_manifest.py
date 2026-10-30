"""Manifeste Floaty (tools/resourcepack/floaty_manifest.py) : classement « remplacé / neuf / écarté » et fermeture items -> modèles -> textures.
Faux jar synthétique (aucun accès au vrai jar ni à la carte) ; le manifeste commité (floaty_vanilla.json) n'est relu que pour figer ses comptes.
Règles vérifiées : un X.png.mcmeta prend le statut de X.png ; modèles vanilla qui lisent une texture item remplacée (directement ou par parent) ;
items vanilla qui lisent ces modèles ou un modèle remplacé par la carte ; fichiers neufs sans effet écartés (jamais un fichier remplaçant du vanilla).
Lancer : python -m unittest discover -s tools/tests -v (racine dérivée de ce fichier).
"""
import importlib.util
import io
import json
import os
import tempfile
import unittest
import zipfile
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RP = ROOT / 'tools' / 'resourcepack'
spec = importlib.util.spec_from_file_location('floaty_manifest', RP / 'floaty_manifest.py')
fm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fm)

MC = 'assets/minecraft/'


def js(obj):
    return json.dumps(obj).encode('utf-8')


def model_item(ref):
    return {'model': {'type': 'minecraft:model', 'model': ref}}


# faux jar : chemin -> octets
JAR = {
    MC + 'textures/item/apple.png': b'p', MC + 'textures/item/other.png': b'p', MC + 'textures/item/rod.png': b'p', MC + 'textures/item/sword.png': b'p',
    MC + 'textures/block/stone.png': b'p', MC + 'textures/block/cactus.png': b'p', MC + 'textures/block/cactus.png.mcmeta': b'{}',
    MC + 'textures/entity/zombie/zombie.png': b'p', MC + 'textures/gui/container/shulker_box.png': b'p',
    MC + 'models/item/apple.json': js({'parent': 'minecraft:item/generated', 'textures': {'layer0': 'minecraft:item/apple'}}),
    MC + 'models/item/apple_child.json': js({'parent': 'item/apple'}),
    MC + 'models/item/other.json': js({'parent': 'item/generated', 'textures': {'layer0': 'item/other'}}),
    MC + 'models/item/rod.json': js({'parent': 'item/handheld', 'textures': {'layer0': 'item/rod'}}),
    MC + 'models/item/sword.json': js({'parent': 'item/handheld', 'textures': {'layer0': 'item/sword'}}),
    MC + 'models/item/generated.json': js({'display': {}}),
    MC + 'items/apple.json': js(model_item('minecraft:item/apple')),
    MC + 'items/gadget.json': js({'model': {'type': 'minecraft:condition', 'on_true': model_item('item/apple_child')['model'],
                                            'on_false': {'type': 'minecraft:special', 'base': 'minecraft:item/other', 'model': {'type': 'minecraft:x'}}}}),
    MC + 'items/other.json': js(model_item('minecraft:item/other')),
    MC + 'items/rod.json': js(model_item('minecraft:item/rod')),
    MC + 'items/sword.json': js(model_item('minecraft:item/sword')),
    MC + 'items/lone.json': js(model_item('minecraft:item/lone')),
    'version.json': js({'id': '26.2', 'pack_version': {'resource_major': 88, 'resource_minor': 0}}),
}
# faux index d'assets du lanceur : chemins vanilla de sons (le jar n'en a pas) et événements du sounds.json vanilla
ASSETS = {'assets/minecraft/sounds.json', MC + 'sounds/mob/x.ogg'}
EVENTS = {'block.stone.break', 'music.end', 'music.game'}
SOUNDS = js({'zelda.a': {'sounds': ['zelda/a']}, 'music.end': {'replace': True, 'sounds': []}})
# faux pack de la carte : noms seulement (le contenu n'entre pas dans le manifeste)
MAP = [
    MC + 'textures/item/apple.png', MC + 'textures/item/apple.png.mcmeta', MC + 'textures/item/fresh.png', MC + 'textures/item/fresh.png.mcmeta',
    MC + 'textures/block/stone.png.mcmeta', MC + 'textures/block/cactus.png', MC + 'textures/block/cactus.png.mcmeta',
    MC + 'textures/block/new_block.png', MC + 'textures/entity/zombie/zombie.png',
    MC + 'models/item/rod.json', MC + 'models/item/fresh.json', MC + 'items/sword.json', MC + 'items/darkcompass.json', MC + 'sounds.json',
    MC + 'sounds/zelda/a.ogg', MC + 'sounds/mob/x.ogg', MC + 'textures/gui/container/shulker_box.png',
    MC + 'textures/trims/models/armor/circles.png', MC + 'textures/trims/models/armor/circles.png.mcmeta', MC + 'textures/trims/color_palettes/template.png',
    MC + 'textures/entity/equipment/wings/elytra_old.png', MC + 'textures/misc/enchanted_glint_entity.png',
    MC + 'textures/misc/enchanted_item_glint.png.mcmeta',
]


def build(map_names=MAP, jar=JAR, sounds=SOUNDS, assets=ASSETS):
    return fm.build_manifest(map_names, set(jar), jar.__getitem__, assets, EVENTS, sounds)


class Classification(unittest.TestCase):
    def setUp(self):
        self.man = build()
        self.rep = self.man['replaced']

    def test_replaced_by_category(self):
        self.assertEqual(self.rep['items'], [MC + 'items/sword.json'])
        self.assertEqual(self.rep['models'], [MC + 'models/item/rod.json'])
        self.assertEqual(self.rep['textures_item'], [MC + 'textures/item/apple.png'])
        self.assertEqual(self.rep['textures_block'], [MC + 'textures/block/cactus.png'])
        self.assertEqual(self.rep['textures_entity'], [MC + 'textures/entity/zombie/zombie.png'])
        self.assertEqual(self.rep['textures_other'], [MC + 'textures/gui/container/shulker_box.png'])

    def test_mcmeta_takes_the_status_of_its_png(self):
        # stone.png est dans le jar mais pas stone.png.mcmeta : remplacé ; cactus.png.mcmeta est dans le jar : remplacé ; fresh.png absent : neuf
        self.assertEqual(self.rep['mcmeta'], [MC + 'textures/block/cactus.png.mcmeta', MC + 'textures/block/stone.png.mcmeta',
                                              MC + 'textures/item/apple.png.mcmeta'])

    def test_new_files_are_not_replaced(self):
        everything = {p for paths in self.rep.values() for p in paths}
        for n in (MC + 'textures/item/fresh.png', MC + 'textures/item/fresh.png.mcmeta', MC + 'models/item/fresh.json', MC + 'items/darkcompass.json',
                  MC + 'sounds.json', MC + 'sounds/zelda/a.ogg', MC + 'textures/block/new_block.png'):
            self.assertNotIn(n, everything, n)

    def test_sound_file_is_replaced_when_the_asset_index_has_it(self):
        self.assertEqual(self.rep['sounds'], [MC + 'sounds/mob/x.ogg'])
        self.assertEqual(build(assets=frozenset())['replaced']['sounds'], [])           # cas inverse : sans l'index, le chemin passe pour neuf

    def test_sounds_json_is_classified_by_event(self):
        self.assertEqual(self.man['sounds'], {'new': ['zelda.a'], 'dropped': ['music.end']})
        self.assertEqual(build(sounds=None)['sounds'], {'new': [], 'dropped': []})
        self.assertNotIn(MC + 'sounds.json', {p for paths in self.rep.values() for p in paths})

    def test_vanilla_event_left_in_sounds_json_is_an_error(self):
        for event in ({'block.stone.break': {'sounds': ['x']}}, {'music.game': {'replace': True, 'sounds': ['x']}}):          # vanilla ; music.* non vide
            with self.assertRaises(SystemExit) as cm:
                build(sounds=js(event))
            self.assertIn(next(iter(event)), str(cm.exception))
        self.assertEqual(build(sounds=js({'music.game': {'replace': True, 'sounds': []}}))['sounds'], {'new': [], 'dropped': ['music.game']})   # vide : retiré

    def test_version_comes_from_the_jar(self):
        self.assertEqual(self.man['version'], {'id': '26.2', 'resource': [88, 0]})
        jar = {**JAR, 'version.json': js({'id': '26.3', 'pack_version': {'resource_major': 89, 'resource_minor': 4}})}
        self.assertEqual(build(jar=jar)['version'], {'id': '26.3', 'resource': [89, 4]})
        with self.assertRaises(SystemExit):
            build(jar={n: d for n, d in JAR.items() if n != 'version.json'})

    def test_dropped_are_new_files_matching_the_rules(self):
        self.assertEqual(self.man['dropped'], [MC + 'textures/entity/equipment/wings/elytra_old.png', MC + 'textures/misc/enchanted_glint_entity.png',
                                               MC + 'textures/misc/enchanted_item_glint.png.mcmeta', MC + 'textures/trims/color_palettes/template.png',
                                               MC + 'textures/trims/models/armor/circles.png', MC + 'textures/trims/models/armor/circles.png.mcmeta'])
        everything = {p for paths in self.rep.values() for p in paths}
        self.assertFalse(everything & set(self.man['dropped']))

    def test_drop_rule_never_hides_a_vanilla_replacement(self):
        jar = {**JAR, MC + 'textures/entity/equipment/wings/elytra_old.png': b'p'}          # cas inverse : le jar a ce fichier
        with self.assertRaises(SystemExit) as cm:
            build(jar=jar)
        self.assertIn('elytra_old.png', str(cm.exception))

    def test_spider_rule_is_limited_to_trims(self):
        jar = {**JAR, MC + 'textures/entity/spider/spider.png': b'p'}
        man = build(MAP + [MC + 'textures/entity/spider/spider.png'], jar)                 # remplacé : jamais écarté
        self.assertIn(MC + 'textures/entity/spider/spider.png', man['replaced']['textures_entity'])
        man = build(MAP + [MC + 'textures/entity/spider/spider_new.png'], jar)             # neuf, hors trims : gardé
        self.assertNotIn(MC + 'textures/entity/spider/spider_new.png', man['dropped'])


class Closure(unittest.TestCase):
    def setUp(self):
        self.man = build()

    def test_models_reading_a_replaced_item_texture(self):
        # apple (direct) et apple_child (par parent) ; pas other (texture non remplacée), pas rod (modèle remplacé : il vient de la carte)
        self.assertEqual(sorted(self.man['models']), [MC + 'models/item/apple.json', MC + 'models/item/apple_child.json'])
        self.assertEqual(self.man['models'][MC + 'models/item/apple.json']['textures'], {'layer0': 'minecraft:item/apple'})

    def test_items_wrapped(self):
        # sword : remplacé par la carte ; apple/gadget : lisent un modèle réécrit (gadget par un parent, via une branche) ; rod : lit un modèle remplacé
        self.assertEqual(sorted(self.man['items']), [MC + 'items/apple.json', MC + 'items/gadget.json', MC + 'items/rod.json', MC + 'items/sword.json'])
        self.assertEqual(self.man['items'][MC + 'items/apple.json'], json.loads(JAR[MC + 'items/apple.json']))        # copie vanilla intacte

    def test_untouched_items_are_not_wrapped(self):
        for n in ('other', 'lone', 'darkcompass'):
            self.assertNotIn(MC + f'items/{n}.json', self.man['items'])

    def test_model_outside_models_item_is_an_error(self):
        jar = {**JAR, MC + 'models/block/x.json': js({'textures': {'all': 'item/apple'}})}
        with self.assertRaises(SystemExit) as cm:
            build(jar=jar)
        self.assertIn('block/x', str(cm.exception))

    def test_digest_covers_the_map_names_only(self):
        self.assertEqual(self.man['names_sha256'], fm.fs.floaty_names_digest(MAP))
        self.assertEqual(build(list(reversed(MAP)))['names_sha256'], self.man['names_sha256'])
        self.assertNotEqual(build(MAP + [MC + 'textures/item/more.png'])['names_sha256'], self.man['names_sha256'])

    def test_no_map_content_in_the_manifest(self):
        self.assertEqual(sorted(self.man), ['dropped', 'items', 'models', 'names_sha256', 'replaced', 'sounds', 'version'])


class Main(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.base = Path(tmp.name)
        self.jar = self.base / 'fake.jar'
        with zipfile.ZipFile(self.jar, 'w') as zf:
            for n, data in JAR.items():
                zf.writestr(n, data)
        self.rp = self.base / 'map'
        for n in MAP:
            p = self.rp / n
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(SOUNDS if n == MC + 'sounds.json' else b'x')
        digest = 'ab' + '0' * 38                                  # faux dossier d'assets du lanceur : indexes/32.json + objects/ab/<hash> (sounds.json vanilla)
        self.assets = self.base / 'assets'
        (self.assets / 'indexes').mkdir(parents=True)
        (self.assets / 'objects' / 'ab').mkdir(parents=True)
        index = {'objects': {k[len('assets/'):]: {'hash': digest} for k in ASSETS}}
        (self.assets / 'indexes' / '32.json').write_text(json.dumps(index), encoding='utf-8')
        (self.assets / 'objects' / 'ab' / digest).write_text(json.dumps({e: {} for e in EVENTS}), encoding='utf-8')
        self.env = {'NEOMC_MC_JAR': str(self.jar), 'NEOMC_FLOATY_RP': str(self.rp), 'NEOMC_MC_ASSETS': str(self.assets), 'NEOMC_MC_ASSET_INDEX': '32'}

    def run_main(self, name):
        out = self.base / name
        with redirect_stdout(io.StringIO()) as buf:
            fm.main([str(out)], self.env)
        return out.read_bytes(), buf.getvalue()

    def test_writes_a_reproducible_manifest(self):
        a, text = self.run_main('a.json')
        b, _ = self.run_main('b.json')
        self.assertEqual(a, b)
        self.assertTrue(a.endswith(b'\n') and b'\r' not in a)
        self.assertEqual(json.loads(a.decode('utf-8')), build())
        self.assertIn('items enveloppés=4', text)
        self.assertIn('événements de sons neufs=1 retirés=1', text)

    def test_missing_variables_are_an_error(self):
        for key in self.env:
            env = {k: v for k, v in self.env.items() if k != key}
            with self.assertRaises(SystemExit) as cm:
                fm.main([str(self.base / 'x.json')], env)
            self.assertIn('usage', str(cm.exception))
        self.assertFalse((self.base / 'x.json').exists())

    def test_bad_jar_is_an_error_not_a_traceback(self):
        self.env['NEOMC_MC_JAR'] = str(self.base / 'absent.jar')
        with self.assertRaises(SystemExit):
            fm.main([str(self.base / 'x.json')], self.env)

    def test_bad_asset_index_is_an_error_not_a_traceback(self):
        self.env['NEOMC_MC_ASSET_INDEX'] = '99'                                       # index absent (OSError)
        with self.assertRaises(SystemExit) as cm:
            fm.main([str(self.base / 'x.json')], self.env)
        self.assertIn('manifeste', str(cm.exception))
        (self.assets / 'indexes' / '99.json').write_text('{"objects": {}}', encoding='utf-8')      # sans sounds.json vanilla (KeyError)
        with self.assertRaises(SystemExit):
            fm.main([str(self.base / 'x.json')], self.env)
        self.assertFalse((self.base / 'x.json').exists())


class CommittedManifest(unittest.TestCase):
    """Comptes du floaty_vanilla.json commité (produit avec le jar 26.2 et la carte Scourge) : un changement doit être voulu, pas silencieux."""
    MAN = json.loads((RP / 'floaty_vanilla.json').read_text(encoding='utf-8'))

    def test_counts(self):
        counts = {c: len(p) for c, p in self.MAN['replaced'].items()}
        self.assertEqual(counts, {'items': 18, 'models': 1, 'textures_item': 45, 'textures_block': 26, 'textures_entity': 21, 'textures_particle': 12,
                                  'textures_painting': 32, 'textures_other': 3, 'sounds': 0, 'mcmeta': 17, 'other': 0})
        self.assertEqual((len(self.MAN['items']), len(self.MAN['models']), len(self.MAN['dropped'])), (33, 50, 10))

    def test_version_and_sounds(self):
        self.assertEqual(self.MAN['version'], {'id': '26.2', 'resource': [88, 0]})
        snd = self.MAN['sounds']
        self.assertEqual((len(snd['new']), len(snd['dropped'])), (41, 31))
        self.assertTrue(all(e.startswith('music.') for e in snd['dropped']))
        self.assertFalse(set(snd['new']) & set(snd['dropped']))
        self.assertFalse([e for e in snd['new'] if e.startswith('music.')])             # données réelles : aucun music.* neuf

    def test_every_replaced_item_has_its_vanilla_definition(self):
        for p in self.MAN['replaced']['items']:
            self.assertIn(p, self.MAN['items'])
        for p in (MC + 'items/compass.json', MC + 'items/brush.json', MC + 'items/blaze_rod.json', MC + 'items/trident.json'):
            self.assertIn(p, self.MAN['items'])

    def test_dropped_and_replaced_are_disjoint_and_no_lang(self):
        everything = [p for paths in self.MAN['replaced'].values() for p in paths]
        self.assertEqual(len(everything), len(set(everything)))
        self.assertFalse(set(everything) & set(self.MAN['dropped']))
        self.assertFalse([p for p in everything + self.MAN['dropped'] if '/lang/' in p])
        self.assertTrue(all(p.startswith(MC + 'models/item/') for p in self.MAN['models']))
        self.assertEqual(len(self.MAN['names_sha256']), 64)


if __name__ == '__main__':
    unittest.main()
