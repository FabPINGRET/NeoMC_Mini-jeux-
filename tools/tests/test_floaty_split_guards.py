"""Gardes de la scission (tools/resourcepack/floaty_split.py) : SystemExit qui liste les chemins en cause, avec leurs cas inverses (l'entrée valide passe).
Fixtures synthétiques partagées avec test_floaty_split.py (importées : pas de jar, de carte ni de manifeste commité).
Gardes : empreinte des chemins / chemins du manifeste absents / définitions vanilla perdues (relancer le manifeste), assets/floaty/ réservé,
version du manifeste couverte par PACK_FMT, événements de sounds.json = ceux du manifeste, clés générées sans collision.
Lancer : python -m unittest discover -s tools/tests -v (racine dérivée de ce fichier).
"""
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))          # fixtures de test_floaty_split (même dossier, comme test_floaty_chunks)
from test_floaty_split import DARK, EXTRA, MANIFEST, MC, PACK_FMT, ROD, SWORD, fs, js, plus, split  # noqa: E402

SND = MC + 'sounds.json'


class Guards(unittest.TestCase):
    def fails(self, extra=None, man=None, *needles, rerun=True, pack_fmt=None):
        with self.assertRaises(SystemExit) as cm:
            split(extra, man, pack_fmt)
        msg = str(cm.exception)
        self.assertEqual('floaty_manifest.py' in msg and 'NEOMC_MC_JAR' in msg and 'NEOMC_MC_ASSET_INDEX' in msg, rerun, msg)     # consigne de relancer le manifeste
        for n in needles:
            self.assertIn(n, msg)
        return msg

    def test_names_digest_mismatch(self):
        self.fails({**EXTRA, MC + 'textures/item/added.png': b'x'}, None, 'ne correspond plus')
        self.fails({p: d for p, d in EXTRA.items() if p != MC + 'sounds/z/s.ogg'}, None, 'ne correspond plus')

    def test_missing_manifest_path_is_listed(self):
        extra = {p: d for p, d in EXTRA.items() if p != MC + 'textures/block/stone.png'}
        self.fails(extra, None, '1 fichier(s) du manifeste absents', MC + 'textures/block/stone.png')

    def test_missing_vanilla_definition_is_listed(self):
        man = copy.deepcopy(MANIFEST)
        del man['items'][SWORD]
        self.fails(None, man, '1 définition(s) vanilla attendue(s)', SWORD)

    def test_unreadable_map_item_names_the_file(self):
        extra, man = plus({SWORD: b'{pas du json'})
        self.fails(extra, man, SWORD, 'illisible', rerun=False)

    def test_map_item_without_model_object_is_listed(self):
        extra, man = plus({SWORD: js({'model': 'item/sword'})})
        self.fails(extra, man, SWORD, rerun=False)


class Reserved(unittest.TestCase):
    """assets/floaty/ est l'espace de noms des fichiers générés : la carte n'y met rien (le manifeste n'y peut rien : pas de consigne de relance)."""
    def test_map_file_under_floaty_namespace_is_refused_and_listed(self):
        extra, man = plus({'assets/floaty/models/item/apple.json': b'{}', 'assets/floaty/textures/item/x.png': b'x'})
        with self.assertRaises(SystemExit) as cm:
            split(extra, man)
        msg = str(cm.exception)
        self.assertIn('2 fichier(s)', msg)
        self.assertIn('assets/floaty/models/item/apple.json', msg)
        self.assertIn('assets/floaty/textures/item/x.png', msg)
        self.assertNotIn('floaty_manifest.py', msg)

    def test_namespace_lookalikes_are_not_refused(self):
        extra, man = plus({'assets/floaty2/x.png': b'x', MC + 'textures/item/floaty/x.png': b'x'})          # préfixe voisin : pas le nôtre
        server, _ = split(extra, man)
        self.assertIn('assets/floaty2/x.png', server)


class Collisions(unittest.TestCase):
    """Une clé générée n'en écrase jamais une autre : la scission s'arrête et nomme le chemin."""
    def collides(self, man, path, extra=None):
        with self.assertRaises(SystemExit) as cm:
            split(extra, man)
        msg = str(cm.exception)
        self.assertIn('collision', msg)
        self.assertIn(path, msg)
        self.assertNotIn('floaty_manifest.py', msg)

    def test_renamed_map_model_and_vanilla_model_copy_collide(self):
        man = copy.deepcopy(MANIFEST)
        man['models'][MC + 'models/item/rod.json'] = {'parent': 'item/handheld'}               # le manifeste recopie aussi le modèle que la carte remplace
        self.collides(man, 'assets/floaty/models/item/rod.json')

    def test_wrapped_item_collides_with_a_new_map_item(self):
        man = copy.deepcopy(MANIFEST)
        man['items'][DARK] = {'model': {'type': 'minecraft:model', 'model': 'minecraft:item/darkcompass'}}      # attendu vanilla, mais la carte le dit neuf
        self.collides(man, DARK)

    def test_valid_manifest_has_no_collision(self):
        server, _ = split()
        self.assertIn(ROD, server)                 # cas inverse : manifeste cohérent, tous les chemins distincts


class Version(unittest.TestCase):
    def pack(self, lo, hi):
        return {'min_format': lo, 'max_format': hi}

    def test_pack_fmt_covering_the_version_passes(self):
        split(pack_fmt=PACK_FMT)
        split(pack_fmt=self.pack([88, 0], [88, 0]))                       # bornes incluses
        split(pack_fmt=self.pack([87, 5], [88, 3]))
        split(pack_fmt=None)                                              # sans PACK_FMT : version non contrôlée

    def test_pack_fmt_not_covering_the_version_is_refused(self):
        for lo, hi in (([89, 0], [89, 99]), ([88, 1], [88, 99]), ([87, 0], [87, 99])):          # autre majeure ; sous le minimum ; au-dessus du maximum
            msg = self.assertFails(self.pack(lo, hi))
            self.assertIn('PACK_FMT', msg)
            self.assertIn('26.2', msg)

    def assertFails(self, pack_fmt):
        with self.assertRaises(SystemExit) as cm:
            split(pack_fmt=pack_fmt)
        return str(cm.exception)

    def test_manifest_version_decides(self):
        man = copy.deepcopy(MANIFEST)
        man['version'] = {'id': '26.3', 'resource': [88, 5]}
        split(man=man, pack_fmt=PACK_FMT)
        man['version'] = {'id': '27.0', 'resource': [89, 0]}
        with self.assertRaises(SystemExit):
            split(man=man, pack_fmt=PACK_FMT)


class Sounds(unittest.TestCase):
    """sounds.json reste dans le pack forcé : ses événements doivent tous être « neufs » dans le manifeste (son contenu n'est pas dans l'empreinte)."""
    def test_new_events_pass_and_bytes_are_kept(self):
        data = js({'zelda.a': {'sounds': ['zelda/a']}})
        extra, man = plus({SND: data})
        server, _ = split(extra, man)
        self.assertEqual(server[SND], data)

    def test_vanilla_or_unfiltered_event_is_refused_and_listed(self):
        for event in ('block.stone.break', 'music.end'):             # vanilla redéfini ; music.* vide que le filtre aurait dû retirer
            extra, man = plus({SND: js({'zelda.a': {}, event: {'replace': True, 'sounds': []}})})
            with self.assertRaises(SystemExit) as cm:
                split(extra, man)
            msg = str(cm.exception)
            self.assertIn(event, msg)
            self.assertIn('floaty_manifest.py', msg)

    def test_no_sounds_json_or_empty_object_passes(self):
        extra, man = plus({SND: b'{}'})
        split(extra, man)
        extra = {p: d for p, d in EXTRA.items() if p != SND}
        man = copy.deepcopy(MANIFEST)
        man['names_sha256'] = fs.floaty_names_digest(extra)
        split(extra, man)

    def test_unreadable_or_non_object_sounds_json_is_refused(self):
        for data in (b'{pas du json', b'[1]', b'[{"a": 1}]'):
            extra, man = plus({SND: data})
            with self.assertRaises(SystemExit) as cm:
                split(extra, man)
            self.assertIn(SND, str(cm.exception))


if __name__ == '__main__':
    unittest.main()
