"""Resource pack : fusion des textures de Scourge of the Floaty Isles (tools/resourcepack/floaty_rp.py, branché dans gen_rp.py).
Variable NEOMC_FLOATY_RP absente -> avertissement, rien d'autre ; vide -> erreur ; conflit -> erreur qui liste tous les chemins sans rien écrire ;
__MACOSX / .DS_Store / pack.mcmeta / lang/ ignorés ; noms invalides ou en double -> erreur listée ; identique à l'octet -> toléré ;
sounds.json sans les music.* vides (filtré avant la détection de conflit) ; rien sous assets/mg/ ; zip trié, à date fixe, reproductible.
Données synthétiques (aucun accès à la carte), plus un test gardien sur releases/neomc_resourcepack.zip (zip commité).
Lancer : python -m unittest discover -s tools/tests -v (racine dérivée de ce fichier).
"""
import importlib.util
import io
import json
import tempfile
import unittest
import warnings
import zipfile
import zlib
from contextlib import redirect_stdout
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
RP = ROOT / 'tools' / 'resourcepack'
spec = importlib.util.spec_from_file_location('floaty_rp', RP / 'floaty_rp.py')
fr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fr)

ENV = fr.FLOATY_ENV
SND = 'assets/minecraft/sounds.json'
# contenu d'un pack de carte : les 5 derniers doivent être ignorés
MAP_FILES = {
    'assets/minecraft/textures/item/a.png': b'png-a',
    'assets/minecraft/models/item/a.json': b'{"x": 1}',
    'assets/minecraft/sounds/z/s.ogg': b'ogg',
    'assets/.DS_Store': b'junk',
    '__MACOSX/assets/._.DS_Store': b'junk',
    'assets/minecraft/lang/en_us.json': b'{"old.key": "o"}',
    'pack.mcmeta': b'{"pack": {}}',
    'pack.png': b'logo',
}
KEPT = ['assets/minecraft/models/item/a.json', 'assets/minecraft/sounds/z/s.ogg', 'assets/minecraft/textures/item/a.png']


def put(base, files):
    for rel, data in files.items():
        p = Path(base) / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)


def make_zip(path, files):
    with zipfile.ZipFile(path, 'w') as zf:
        zf.writestr('assets/', b'')
        for rel, data in files.items():
            zf.writestr(rel, data)


def snapshot(base):
    return {p.relative_to(base).as_posix(): p.read_bytes() for p in Path(base).rglob('*') if p.is_file()}


def run(out, env):
    buf = io.StringIO()
    with redirect_stdout(buf):
        res = fr.floaty_extra(str(out), env)
    return res, buf.getvalue()


class FloatyRp(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.out = self.base / 'out'                  # le dossier resourcepack/ de gen_rp
        put(self.out, {'assets/mg/items/k.json': b'{}', 'pack.mcmeta': b'{"pack": {}}'})
        self.src_dir = self.base / 'map_rp'
        put(self.src_dir, MAP_FILES)
        self.src_zip = self.base / 'resources.zip'
        make_zip(self.src_zip, MAP_FILES)

    def fails(self, env, *needles):
        """run() doit sortir en erreur sans rien écrire ; renvoie le message (qui contient chaque needle)."""
        before = snapshot(self.base)
        with self.assertRaises(SystemExit) as cm:
            run(self.out, env)
        self.assertEqual(before, snapshot(self.base), 'une erreur ne doit rien écrire')
        for n in needles:
            self.assertIn(n, str(cm.exception))
        return str(cm.exception)

    def zip_with(self, files, name='x.zip'):
        path = self.base / name
        make_zip(path, files)
        return {ENV: str(path)}

    # ---- variable
    def test_variable_absent_warns_and_does_nothing(self):
        before = snapshot(self.base)
        res, text = run(self.out, {})
        self.assertEqual(res, {})
        self.assertIn('ATTENTION', text)
        self.assertIn(ENV, text)
        self.assertEqual(before, snapshot(self.base))

    def test_variable_blank_is_an_error(self):
        for blank in ('', '   '):
            self.fails({ENV: blank}, ENV, 'vide')

    def test_bad_sources_exit_cleanly(self):
        junk = self.base / 'junk.txt'
        junk.write_bytes(b'pas un zip')
        empty = self.base / 'empty'
        put(empty, {'pack.mcmeta': b'{}'})
        for src in (self.base / 'absent', junk, empty):
            self.fails({ENV: str(src)}, ENV)

    def test_unreadable_zip_content_is_an_error_not_a_traceback(self):
        for exc in (RuntimeError('File is encrypted, password required'), NotImplementedError('compression type 14 (lzma)'),
                    zlib.error('Error -3 while decompressing data')):
            with mock.patch.object(zipfile.ZipFile, 'read', side_effect=exc):
                self.fails({ENV: str(self.src_zip)}, ENV)

    # ---- sélection des fichiers
    def test_skips_macosx_dsstore_pack_files_and_lang(self):
        for src in (self.src_dir, self.src_zip):
            res, text = run(self.out, {ENV: str(src)})
            self.assertEqual(sorted(res), KEPT)
            self.assertIn('3 fichier(s)', text)
        put(self.src_dir, {'assets/other/lang/fr_fr.json': b'{}', 'assets/other/lang/x/y.json': b'{}'})
        self.assertEqual(sorted(run(self.out, {ENV: str(self.src_dir)})[0]), KEPT)             # aucun assets/*/lang/* importé

    def test_dir_and_zip_give_same_content(self):
        self.assertEqual(run(self.out, {ENV: str(self.src_dir)})[0], run(self.out, {ENV: str(self.src_zip)})[0])

    def test_invalid_names_are_listed_not_ignored(self):
        bad = ['assets/__MACOSX/x.png', 'assets//x.png', 'assets/minecraft/._x.png', 'assets/Minecraft/x.png', '/assets/x.png',
               'C:/assets/x.png', 'assets/../x.png', 'assets/minecraft/a b.png']
        env = self.zip_with({**MAP_FILES, **{n: b'x' for n in bad}})
        msg = self.fails(env, f'{len(bad)} nom(s) invalide(s)')
        for n in bad:
            self.assertIn(n, msg)
        self.assertNotIn('a.png', msg)                                                          # les noms valides ne sont pas listés

    def test_select_rejects_backslash_names(self):
        # zipfile convertit « \ » en « / » sous Windows : on teste la sélection directement
        names = ['assets' + chr(92) + 'minecraft' + chr(92) + 'x.png', 'assets/minecraft/ok.png']
        self.assertEqual(fr.floaty_select(names), (['assets/minecraft/ok.png'], [names[0]]))

    def test_duplicate_names_in_zip_are_an_error(self):
        path = self.base / 'dup.zip'
        with zipfile.ZipFile(path, 'w') as zf, warnings.catch_warnings():
            warnings.simplefilter('ignore')
            zf.writestr('assets/minecraft/a.png', b'1')
            zf.writestr('assets/minecraft/a.png', b'2')
        self.assertIn('assets/minecraft/a.png (en double)', self.fails({ENV: str(path)}))

    def test_assets_mg_is_an_error(self):
        env = self.zip_with({**MAP_FILES, 'assets/mg/items/banana.json': b'{}', 'assets/mg/font/kart.json': b'{}'})
        self.fails(env, '2 fichier(s) sous assets/mg/', 'assets/mg/items/banana.json', 'assets/mg/font/kart.json')

    def test_scope_summary(self):
        text = run(self.out, {ENV: str(self.src_zip)})[1]
        self.assertIn('minecraft/models 1', text)
        self.assertIn('minecraft/sounds 1', text)
        self.assertIn('textures : 1', text)

    # ---- conflits
    def test_conflict_lists_every_path_and_writes_nothing(self):
        put(self.out, {'assets/minecraft/textures/item/a.png': b'neomc', 'assets/minecraft/models/item/a.json': b'{}'})
        for src in (self.src_dir, self.src_zip):
            msg = self.fails({ENV: str(src)}, '2 fichier(s)', 'assets/minecraft/textures/item/a.png', 'assets/minecraft/models/item/a.json')
            self.assertNotIn('sounds/z/s.ogg', msg)

    def test_identical_bytes_tolerated_and_not_added(self):
        put(self.out, {'assets/minecraft/textures/item/a.png': b'png-a'})
        res, _ = run(self.out, {ENV: str(self.src_zip)})
        self.assertEqual(sorted(res), [p for p in KEPT if not p.endswith('a.png')])

    def test_identical_plus_different_still_conflicts(self):
        put(self.out, {'assets/minecraft/textures/item/a.png': b'png-a', 'assets/minecraft/sounds/z/s.ogg': b'autre'})
        msg = self.fails({ENV: str(self.src_zip)}, 'assets/minecraft/sounds/z/s.ogg')
        self.assertNotIn('textures/item/a.png', msg)

    def test_mergeable_json_conflict_is_hinted_not_merged(self):
        files = {SND: b'{"a": {}}', 'assets/minecraft/atlases/blocks.json': b'{}', 'assets/minecraft/font/default.json': b'{}'}
        put(self.src_dir, files)
        put(self.out, {SND: b'{"b": {}}', 'assets/minecraft/atlases/blocks.json': b'{"sources": []}', 'assets/minecraft/font/default.json': b'{"p": 1}'})
        msg = self.fails({ENV: str(self.src_dir)}, SND, 'assets/minecraft/atlases/blocks.json', 'assets/minecraft/font/default.json')
        self.assertIn('fusion JSON', msg)

    # ---- sounds.json
    def sounds(self, snd):
        return run(self.out, self.zip_with({**MAP_FILES, SND: snd if isinstance(snd, bytes) else json.dumps(snd).encode('utf-8')}))[0][SND]

    def test_sounds_drops_empty_music_only_and_is_deterministic(self):
        snd = {'music.menu': {'replace': True, 'sounds': []}, 'soundtrack.b': {'category': 'record', 'sounds': ['soundtrack/b']},
               'music.game': {'replace': True, 'sounds': ['music/x']}, 'music.end': {'sounds': []},
               'music.creative': {'replace': True, 'sounds': []}, 'zelda.a': {'sounds': ['zelda/a']}}
        runs = [self.sounds(snd) for _ in range(2)]
        self.assertEqual(runs[0], runs[1])
        self.assertTrue(runs[0].endswith(b'\n') and b'\r' not in runs[0])
        out = json.loads(runs[0].decode('utf-8'))
        self.assertEqual(list(out), ['soundtrack.b', 'music.game', 'music.end', 'zelda.a'])        # ordre de la source conservé
        self.assertEqual(out['music.game'], {'replace': True, 'sounds': ['music/x']})

    def test_sounds_not_an_object_is_an_error(self):
        for bad in (b'[1, 2]', b'"x"', b'{"music.menu": []}', b'{"a": {}, "b": 3}', b'{pas du json', b'\xff\xfe'):
            self.fails(self.zip_with({**MAP_FILES, SND: bad}, 'bad.zip'), ENV)

    def test_conflict_is_checked_after_filtering(self):
        raw = {'music.menu': {'replace': True, 'sounds': []}, 'soundtrack.a': {'sounds': ['s/a']}}
        put(self.out, {SND: fr.floaty_dump({'soundtrack.a': {'sounds': ['s/a']}})})              # NeoMC fournit exactement la sortie filtrée
        res, _ = run(self.out, self.zip_with({**MAP_FILES, SND: json.dumps(raw).encode('utf-8')}))
        self.assertNotIn(SND, res)                                                              # identique à l'octet : toléré, pas ajouté
        self.assertEqual(sorted(res), KEPT)

    # ---- écriture du zip, câblage
    def test_write_is_sorted_dated_and_reproducible(self):
        extra = run(self.out, {ENV: str(self.src_zip)})[0]
        blobs = []
        for _ in range(2):
            buf = io.BytesIO()
            with zipfile.ZipFile(buf, 'w') as zf:
                zf.writestr('assets/mg/items/k.json', b'{}')          # un fichier NeoMC déjà écrit : les extras viennent après
                fr.floaty_write(zf, dict(reversed(list(extra.items()))))
            blobs.append(buf.getvalue())
        self.assertEqual(blobs[0], blobs[1])
        with zipfile.ZipFile(io.BytesIO(blobs[0])) as zf:
            self.assertEqual(zf.namelist(), ['assets/mg/items/k.json'] + KEPT)
            added = zf.infolist()[1:]                                              # sans le fichier NeoMC factice
            self.assertTrue(all(i.date_time == fr.FLOATY_DATE for i in added))
            self.assertTrue(all(i.compress_type == zipfile.ZIP_DEFLATED for i in added))

    def test_write_opt_is_sorted_dated_and_reproducible(self):
        opt = {'assets/minecraft/textures/block/z.png': b'z', 'assets/minecraft/textures/block/a.png': b'a'}
        meta = {'pack': {'description': 'opt', 'min_format': [88, 0], 'max_format': [88, 99]}}
        blobs = []
        for name, files in (('a.zip', opt), ('b.zip', dict(reversed(list(opt.items()))))):
            path = self.base / 'releases' / name                      # le dossier est créé
            fr.floaty_write_opt(str(path), files, meta)
            blobs.append(path.read_bytes())
        self.assertEqual(blobs[0], blobs[1])
        with zipfile.ZipFile(io.BytesIO(blobs[0])) as zf:
            self.assertEqual(zf.namelist(), ['assets/minecraft/textures/block/a.png', 'assets/minecraft/textures/block/z.png', 'pack.mcmeta'])
            self.assertEqual(json.loads(zf.read('pack.mcmeta').decode('utf-8')), meta)
            self.assertTrue(all(i.date_time == fr.FLOATY_DATE and i.compress_type == zipfile.ZIP_DEFLATED for i in zf.infolist()))

    def test_write_opt_refuses_its_own_pack_mcmeta_and_leaves_inputs(self):
        opt = {'pack.mcmeta': b'{}'}
        with self.assertRaises(ValueError):
            fr.floaty_write_opt(str(self.base / 'x.zip'), opt, {'pack': {}})
        self.assertFalse((self.base / 'x.zip').exists())
        opt = {'assets/minecraft/textures/block/a.png': b'a'}
        fr.floaty_write_opt(str(self.base / 'y.zip'), opt, {'pack': {}})
        self.assertEqual(opt, {'assets/minecraft/textures/block/a.png': b'a'})              # pas de pack.mcmeta ajouté à l'entrée

    def test_gen_rp_wiring(self):
        src = (RP / 'gen_rp.py').read_text(encoding='utf-8')
        self.assertIn("'floaty_rp.py'", src)
        self.assertIn("'floaty_split.py'", src)
        self.assertLess(src.index("'floaty_rp.py'"), src.index("'floaty_split.py'"))
        call = 'floaty_settle(*floaty_split(floaty_extra(OUT, keep_same=True), PACK_FMT), OUT)'      # empreinte sur toute la carte, dédoublonnage après
        self.assertLess(src.index('PACK_FMT = '), src.index(call))                             # PACK_FMT défini avant la scission qui le contrôle
        self.assertLess(src.index(call), src.index('zipfile.ZipFile(z'))                       # scission faite avant d'ouvrir le zip
        self.assertGreater(src.index('floaty_write_opt('), src.index('floaty_write(zf'))
        self.assertEqual(src.count('**PACK_FMT'), 2)                                         # pack.mcmeta du pack serveur et de l'optionnel
        self.assertNotIn('hashlib', src)                                                     # plus d'empreinte affichée (décision de Maxime)
        self.assertNotIn('sha1', src)
        self.assertLess(src.index('floaty_extra(OUT'), src.index('zipfile.ZipFile(z'))       # conflit détecté avant d'ouvrir le zip
        self.assertGreater(src.index('floaty_write(zf'), src.index('zipfile.ZipFile(z'))
        self.assertEqual(fr.FLOATY_DATE, (2026, 1, 1, 0, 0, 0))
        self.assertIn('date_time=(2026, 1, 1, 0, 0, 0)', src)                                 # même date que les fichiers NeoMC


class FloatyCommittedZip(unittest.TestCase):
    """Garde : releases/neomc_resourcepack.zip (suivi par git) doit contenir la fusion Floaty. Un build sans NEOMC_FLOATY_RP l'appauvrit en silence."""
    ZIP = ROOT / 'releases' / 'neomc_resourcepack.zip'
    # chemins de la carte, absents de resourcepack/ (donc seule la fusion peut les apporter)
    KNOWN = ['assets/minecraft/sounds.json', 'assets/minecraft/items/bow.json', 'assets/minecraft/textures/entity/zombie/zombie.png']

    def test_zip_exists(self):
        self.assertTrue(self.ZIP.is_file(), f'{self.ZIP} absent : le zip est suivi par git (pas de skip)')

    def test_known_paths_are_not_produced_by_neomc(self):
        for p in self.KNOWN:
            self.assertFalse((ROOT / 'resourcepack' / p).exists(), f'{p} existe dans resourcepack/ : choisir un autre chemin gardien')

    def test_zip_contains_floaty_textures(self):
        self.assertTrue(self.ZIP.is_file(), f'{self.ZIP} absent')
        with zipfile.ZipFile(self.ZIP) as zf:
            names = set(zf.namelist())
            self.assertTrue(names & set(self.KNOWN), 'zip commité sans textures Floaty : relancer gen_rp.py avec NEOMC_FLOATY_RP (cf. README, section Floaty)')
            snd = json.loads(zf.read(SND).decode('utf-8')) if SND in names else {}
        self.assertFalse([k for k in snd if k.startswith('music.')], 'sounds.json du zip : les music.* vides doivent être retirés')
        self.assertFalse([n for n in names if n.startswith('assets/minecraft/lang/')], 'la langue de la carte ne doit pas être importée')


if __name__ == '__main__':
    unittest.main()
