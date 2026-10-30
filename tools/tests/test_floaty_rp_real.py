"""Resource pack : invariants du zip COMMITE releases/neomc_resourcepack.zip (fusion Floaty), sur les vraies donnees (sans la carte, sans relancer gen_rp).
Complete test_floaty_rp.py : pas de doublon, date fixe, ordre de gen_rp, prefixe NeoMC identique a resourcepack/ (noms + contenu), pack.mcmeta de NeoMC,
pas de lang/ ni __MACOSX/.DS_Store/._*, sounds.json valide dont chaque son existe, items/models de la carte sans reference cassee (hors vanilla).
Le bout en bout (gen_rp.py dans une copie temporaire, avec/sans NEOMC_FLOATY_RP) est un script ponctuel, pas un test permanent (copie de ~90 Mo, ~35 s).
Lancer : python -m unittest discover -s tools/tests -v
"""
import json
import os
import re
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ZIP = ROOT / 'releases' / 'neomc_resourcepack.zip'
OUT = ROOT / 'resourcepack'
DATE = (2026, 1, 1, 0, 0, 0)
SND = 'assets/minecraft/sounds.json'
# premiers segments des sons vanilla (un nom absent du zip n'est tolere que s'il en vient : l'index vanilla n'est pas dans le repo)
VANILLA_SOUND_DIRS = {'ambient', 'block', 'damage', 'dig', 'enchant', 'entity', 'event', 'fire', 'fireworks', 'item', 'liquid', 'minecart', 'mob',
                      'music', 'note', 'portal', 'random', 'records', 'step', 'tile', 'ui', 'weather'}


def neomc_walk():
    """Ordre exact de gen_rp.py : os.walk(OUT) descendant, dossiers triés, fichiers triés dans chaque dossier."""
    found = []
    for root, dirs, files in os.walk(OUT):
        dirs.sort()
        for f in sorted(files):
            found.append(os.path.relpath(os.path.join(root, f), OUT).replace(os.sep, '/'))
    return found


def same(zipped, disk):
    """Le zip a des fins de ligne LF (gen_rp écrit newline='\\n') ; une copie de travail Windows (autocrlf) peut avoir du CRLF sur disque."""
    return zipped == disk or zipped == disk.replace(b'\r\n', b'\n')


def ref(s, default='minecraft'):
    ns, _, p = s.rpartition(':')
    return (ns or default), p


def model_refs(node, out):
    if isinstance(node, dict):
        for k, v in node.items():
            if k == 'model' and isinstance(v, str):
                out.append(v)
            else:
                model_refs(v, out)
    elif isinstance(node, list):
        for v in node:
            model_refs(v, out)
    return out


class CommittedZip(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        assert ZIP.is_file(), f'{ZIP} absent (suivi par git)'
        cls.zf = zipfile.ZipFile(ZIP)
        cls.addClassCleanup(cls.zf.close)
        cls.names = cls.zf.namelist()
        cls.nameset = set(cls.names)
        cls.neo = neomc_walk()
        cls.extra = cls.names[len(cls.neo):]            # ajouts Floaty (floaty_write, après la boucle NeoMC)

    # ---- structure
    def test_no_duplicate_names(self):
        self.assertEqual(len(self.names), len(self.nameset), 'noms en double dans le zip')

    def test_every_entry_has_the_fixed_date(self):
        self.assertEqual([i.filename for i in self.zf.infolist() if i.date_time != DATE], [])

    def test_neomc_prefix_matches_resourcepack_dir_names_and_content(self):
        self.assertEqual(self.names[:len(self.neo)], self.neo, 'préfixe NeoMC != resourcepack/ (ordre/noms) : relancer gen_rp.py avec NEOMC_FLOATY_RP')
        diff = [n for n in self.neo if not same(self.zf.read(n), (OUT / n).read_bytes())]
        self.assertEqual(diff, [], 'contenu NeoMC différent de resourcepack/')

    def test_floaty_part_sorted_and_disjoint_from_neomc(self):
        self.assertTrue(self.extra, 'aucun ajout Floaty')
        self.assertEqual(self.extra, sorted(self.extra))
        self.assertFalse(set(self.extra) & set(self.neo))
        self.assertTrue(all(n.startswith('assets/') and not n.startswith('assets/mg/') for n in self.extra))

    def test_pack_mcmeta_is_neomc_not_the_map(self):
        mc = json.loads(self.zf.read('pack.mcmeta').decode('utf-8'))
        self.assertTrue(same(self.zf.read('pack.mcmeta'), (OUT / 'pack.mcmeta').read_bytes()))
        self.assertIn('NeoMC', json.dumps(mc))
        self.assertEqual(self.names.count('pack.mcmeta'), 1)
        self.assertNotIn('pack.png', [n for n in self.extra])           # logo de la carte ignoré

    def test_no_lang_no_junk(self):
        parts = [n.split('/') for n in self.names]
        self.assertEqual([n for n in self.names if re.match(r'assets/[^/]+/lang/', n)], [])
        self.assertEqual([n for n in self.names if '__MACOSX' in n or n.endswith('.DS_Store') or '/._' in n or n.startswith('._')], [])
        self.assertTrue(all(not p[-1].startswith('._') for p in parts))

    # ---- sounds.json
    def test_sounds_json_valid_without_empty_music_and_every_sound_exists(self):
        snd = json.loads(self.zf.read(SND).decode('utf-8'))
        self.assertIsInstance(snd, dict)
        self.assertEqual([k for k, v in snd.items() if k.startswith('music.') and v.get('replace') and v.get('sounds') == []], [])
        missing = []
        for event, v in snd.items():
            for s in v.get('sounds', []):
                if isinstance(s, dict):
                    if s.get('type') == 'event':
                        continue                                           # renvoi vers un autre événement
                    s = s['name']
                ns, p = ref(s)
                if f'assets/{ns}/sounds/{p}.ogg' not in self.nameset and not (ns == 'minecraft' and p.split('/')[0] in VANILLA_SOUND_DIRS):
                    missing.append(f'{event} -> {s}')
        self.assertEqual(missing, [], f'{len(missing)} son(s) référencé(s) absent(s) du zip et non vanilla')

    # ---- items / models de la carte
    def test_item_models_exist_or_are_vanilla(self):
        item_stems = {Path(n).stem for n in self.extra if n.startswith('assets/minecraft/items/')}
        refs = [(n, r) for n in self.extra if n.startswith('assets/minecraft/items/')
                for r in model_refs(json.loads(self.zf.read(n).decode('utf-8')), [])]
        self.assertTrue(refs)
        broken = []
        for n, r in refs:
            ns, p = ref(r)
            if f'assets/{ns}/models/{p}.json' in self.nameset:
                continue
            m = re.fullmatch(r'item/([a-z0-9_]+?)(?:_pulling_\d+|_charged|_firework|_cast|_blocking)?', p) if ns == 'minecraft' else None
            if not (m and m.group(1) in item_stems):                        # modèle vanilla item/<objet> dont l'objet est redéfini par la carte
                broken.append(f'{n} -> {r}')
        self.assertEqual(broken, [], f'{len(broken)} modèle(s) référencé(s) introuvable(s) : {broken[:5]}')

    def test_model_textures_and_parents_exist_or_are_vanilla(self):
        broken, count = [], 0
        for n in self.extra:
            if not (n.startswith('assets/') and '/models/' in n and n.endswith('.json')):
                continue
            m = json.loads(self.zf.read(n).decode('utf-8'))
            for t in (m.get('textures') or {}).values():
                if not isinstance(t, str) or t.startswith('#'):
                    continue
                count += 1
                ns, p = ref(t)
                if f'assets/{ns}/textures/{p}.png' not in self.nameset:
                    broken.append(f'{n} -> {t}')
            par = m.get('parent')
            if par:
                ns, p = ref(par)
                if f'assets/{ns}/models/{p}.json' not in self.nameset and not (ns == 'minecraft' and p.split('/')[0] in ('item', 'block', 'builtin')):
                    broken.append(f'{n} -> parent {par}')
        self.assertGreater(count, 0)
        self.assertEqual(broken, [], f'{len(broken)} référence(s) cassée(s) : {broken[:5]}')


if __name__ == '__main__':
    unittest.main()
