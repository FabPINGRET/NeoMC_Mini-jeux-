"""tools/floaty : générateur (gen_floaty), propriété / suppressions (fl_owned) et lecteur NBT (fl_nbt) sur une fausse carte en dossier
temporaire — la vraie carte n'est pas nécessaire (la CI ne l'a pas). La réécriture des lignes est dans test_floaty_rewrite.py.
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v   (la racine du dépôt est dérivée de ce fichier).
"""
import gzip
import json
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools' / 'floaty'))
import fl_nbt  # noqa: E402
import gen_floaty as G  # noqa: E402

MANIFEST = 'tools/floaty/owned.txt'
DESINSTALLER = 'data/mg/function/desinstaller.mcfunction'
NEEDS_GIT = unittest.skipUnless(shutil.which('git'), 'git requis (--adopt consulte git ls-files)')


def git_init(repo):
    """Fait de repo un dépôt git (le dossier est créé au besoin) : --adopt refuse un dépôt sans git."""
    Path(repo).mkdir(parents=True, exist_ok=True)
    subprocess.run(['git', 'init', '-q'], cwd=repo, check=True)


def snapshot(base):
    """{chemin relatif : octets} de tous les fichiers sous base, hors .git."""
    base = Path(base)
    return {p.relative_to(base).as_posix(): p.read_bytes() for p in sorted(base.rglob('*')) if p.is_file() and '.git' not in p.relative_to(base).parts}


def nbt_bytes():
    """level.dat minimal : Data{ spawn{ pos:[I;1274,209,181], dimension }, version:int } en gzip."""
    def name(s):
        return struct.pack('>H', len(s)) + s.encode()
    spawn = b'\x0b' + name('pos') + struct.pack('>iiii', 3, 1274, 209, 181) + b'\x08' + name('dimension') + name('minecraft:overworld') + b'\x00'
    data = b'\x0a' + name('spawn') + spawn + b'\x03' + name('version') + struct.pack('>i', 19133) + b'\x00'
    return gzip.compress(b'\x0a' + name('') + b'\x0a' + name('Data') + data + b'\x00')


class FakeMap(unittest.TestCase):
    FILES = {
        'boss/function/a.mcfunction': 'tag @a add x\nschedule function boss:b 5s\n',
        'boss/function/b.mcfunction': 'kill @e[type=item]\nexecute as LordDrewpicus run say hi\nscoreboard objectives setdisplay sidebar Value\n',
        'boss/function/model/s.bdstudio': 'x',
        'boss/.DS_Store': 'x',
        'utility/stray.mcfunction': 'say stray',
        'npc/function/zzTemplates/t.mcfunction': 'say id invalide (majuscule)',
        'utility/function/legacy hb2/x.mcfunction': 'say id invalide (espace)',
        'utility/function/u.mcfunction': 'say u',
        'main_quest/advancement/root.json': '{"display":{"title":"R"},"criteria":{}}',
        'main_quest/advancement/q1.json': '{"parent":"main_quest:root","display":{"announce_to_chat":true},"criteria":{}}',
        'main_quest/advancement/q2.json': '{"parent":"main_quest:root","display":{"announce_to_chat":false},"criteria":{}}',
        'game/function/init.mcfunction': 'advancement revoke @a everything\n',
        'minecraft/function/tick.mcfunction': 'xp set @a 0 levels\n',
        'minecraft/function/load.mcfunction': 'say load\n',
        'minecraft/advancement/story/root.json': '{}',
        'minecraft/advancement/recipies/misc/book.json': '{}',
        'minecraft/recipe/circles_armor_trim.json': '{}',
        'minecraft/recipe/coast_armor_trim.json': '{}',
        'minecraft/trim_pattern/circles.json': '{\r\n"asset_id":"circles"\r\n}\r\n',
        'minecraft/tags/entity_type/hb_projectiles.json': '{"values":[]}',
        'minecraft/tags/entity_type/undead.json': '{"values":[]}',
        'minecraft/tags/function/tick.json': '{"values":["tick"]}',
        'minecraft/tags/dialog/quick_actions.json': '{"values":[]}',
        'minecraft/tags/item/trimmable_armor.json': '{"values":[]}',
    }
    BIOMES = ('virion.json', 'small_end_islands.json', '.DS_Store')
    NAMESPACES = ['boss', 'game', 'main_quest', 'utility']
    MC_FILES = ['data/minecraft/recipe/circles_armor_trim.json', 'data/minecraft/tags/entity_type/hb_projectiles.json',
                'data/minecraft/trim_pattern/circles.json', 'data/minecraft/worldgen/biome/virion.json']

    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.map, self.repo = Path(tmp.name) / 'map', Path(tmp.name) / 'repo'
        for rel, txt in self.FILES.items():
            self.put(self.map / G.PACK / rel, txt)
        for b in self.BIOMES:
            self.put(self.map / G.BIOMES / b, '{}')
        (self.map / 'level.dat').write_bytes(nbt_bytes())
        self.put(self.repo / 'data/mg/function/keep.mcfunction', 'say mg')
        self.put(self.repo / DESINSTALLER, 'say d\nfunction mg:elyrace/uninstall\n')
        self.put(self.repo / 'data/minecraft/tags/dialog/quick_actions.json', '{"values":["mine"]}')

    @staticmethod
    def put(p, txt):
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(txt, encoding='utf-8', newline='\n')

    def tree(self):
        return snapshot(self.repo)

    def manifest(self, lines):
        self.put(self.repo / MANIFEST, '\n'.join(lines) + '\n')

    def refused(self, **kw):
        """generate doit lever SystemExit sans rien supprimer ni écrire."""
        before = self.tree()
        with self.assertRaises(SystemExit):
            G.generate(self.map, self.repo, **kw)
        self.assertEqual(self.tree(), before)

    def test_import_filter(self):
        invalid = []
        got = {f'{ns}/{rel}' for ns, rel, _ in G.collect(self.map / G.PACK, self.map / G.BIOMES, invalid)}
        self.assertEqual(sorted(invalid), ['npc/function/zzTemplates/t.mcfunction', 'utility/function/legacy hb2/x.mcfunction'])
        self.assertEqual(got, {
            'boss/function/a.mcfunction', 'boss/function/b.mcfunction', 'utility/function/u.mcfunction',
            'main_quest/advancement/root.json', 'main_quest/advancement/q1.json', 'main_quest/advancement/q2.json',
            'game/function/init.mcfunction',
            'minecraft/recipe/circles_armor_trim.json', 'minecraft/trim_pattern/circles.json',
            'minecraft/tags/entity_type/hb_projectiles.json', 'minecraft/worldgen/biome/virion.json'})

    def test_generate_and_idempotence(self):
        before_mg = (self.repo / 'data/mg/function/keep.mcfunction').read_bytes()
        st, n, spawn, roots, missing = G.generate(self.map, self.repo)
        self.assertEqual((spawn, roots, missing), ((1274, 209, 181), ['main_quest:root'], []))
        self.assertEqual((st.dropped, st.setdisplay, st.announce), (1, 1, 2))
        r = self.repo / 'data'
        self.assertEqual((r / 'boss/function/a.mcfunction').read_text(encoding='utf-8'),
                         'tag @a[tag=mg.flw] add x\nschedule function floaty:sched/boss/b 5s\n')
        self.assertEqual((r / 'boss/function/b.mcfunction').read_text(encoding='utf-8'), 'kill @e[type=item,distance=0..]\n')
        self.assertEqual((r / 'game/function/init.mcfunction').read_text(encoding='utf-8'),
                         'advancement revoke @a[tag=mg.flw] from main_quest:root\n')
        self.assertIn('xp set @a[tag=mg.flw] 0 levels', (r / 'floaty/function/map/tick.mcfunction').read_text(encoding='utf-8'))
        self.assertIn('tellraw @a[tag=mg.flw] "load"', (r / 'floaty/function/map/load.mcfunction').read_text(encoding='utf-8'))
        self.assertFalse((r / 'floaty/function/tick.mcfunction').exists())          # floaty:tick / load : à L3, plus générés
        self.assertIn('positioned 1274 209 181 run function boss:b',
                      (r / 'floaty/function/sched/boss/b.mcfunction').read_text(encoding='utf-8'))
        # rien posé sur les tags tick/load vanilla, ni sur les fichiers qu'il n'a pas créés
        self.assertFalse((r / 'minecraft/tags/function').exists())
        self.assertEqual((r / 'minecraft/tags/dialog/quick_actions.json').read_text(encoding='utf-8'), '{"values":["mine"]}')
        self.assertEqual((r / 'mg/function/keep.mcfunction').read_bytes(), before_mg)
        first = self.tree()
        self.assertEqual((self.repo / MANIFEST).read_text(encoding='utf-8').split('\n')[:-1],
                         [f'data/{ns}/' for ns in self.NAMESPACES] + self.MC_FILES)
        G.generate(self.map, self.repo)
        self.assertEqual(self.tree(), first)

    def test_advancements_announce_forced_off(self):
        G.generate(self.map, self.repo)
        for q in ('root', 'q1', 'q2'):
            d = json.loads((self.repo / f'data/main_quest/advancement/{q}.json').read_text(encoding='utf-8'))
            self.assertIs(d['display']['announce_to_chat'], False, q)
        self.assertEqual(json.loads((self.repo / 'data/main_quest/advancement/q1.json').read_text(encoding='utf-8'))['parent'], 'main_quest:root')

    def test_json_normalised_to_lf(self):
        G.generate(self.map, self.repo)
        for p in (self.repo / 'data').rglob('*.json'):
            self.assertNotIn(b'\r', p.read_bytes(), p)
        self.assertEqual((self.repo / 'data/minecraft/trim_pattern/circles.json').read_text(encoding='utf-8'), '{\n"asset_id":"circles"\n}\n')

    def test_refuses_to_overwrite_foreign_minecraft_file(self):
        self.put(self.repo / 'data/minecraft/worldgen/biome/virion.json', '{"mine":1}')
        self.refused()

    def test_protected_namespace(self):
        self.put(self.map / G.PACK / 'mg/function/x.mcfunction', 'say x')
        self.refused()
        self.assertFalse((self.repo / 'data/boss').exists())

    @NEEDS_GIT
    def test_unowned_namespace_refused_before_any_deletion(self):
        git_init(self.repo)
        G.generate(self.map, self.repo)
        (self.repo / MANIFEST).unlink()                       # le dossier existe, plus rien ne dit qu'il est au générateur
        self.put(self.repo / 'data/main_quest/function/mine.mcfunction', 'say mine')
        self.refused()
        self.assertTrue((self.repo / 'data/floaty/function/sched/boss/b.mcfunction').exists())
        G.generate(self.map, self.repo, adopt=True)           # premier passage : --adopt
        self.assertFalse((self.repo / 'data/main_quest/function/mine.mcfunction').exists())
        G.generate(self.map, self.repo)                       # le manifeste existe maintenant : plus besoin de --adopt

    def test_obsolete_entries_of_manifest_are_deleted(self):
        self.manifest(['data/oldns/', 'data/minecraft/worldgen/biome/old.json'])
        self.put(self.repo / 'data/oldns/function/f.mcfunction', 'say old')
        self.put(self.repo / 'data/minecraft/worldgen/biome/old.json', '{}')
        self.put(self.repo / 'data/minecraft/worldgen/biome/not_listed.json', '{}')
        G.generate(self.map, self.repo)
        self.assertFalse((self.repo / 'data/oldns').exists())
        self.assertFalse((self.repo / 'data/minecraft/worldgen/biome/old.json').exists())
        self.assertTrue((self.repo / 'data/minecraft/worldgen/biome/not_listed.json').exists())

    def test_manifest_cannot_escape_data_minecraft(self):
        self.manifest(['data/minecraft/../mg/function/keep.mcfunction'])
        self.refused()
        self.manifest(['data/mg/'])
        self.refused()
        self.manifest(['tools/floaty/fl_rewrite.py'])
        self.refused()


class NbtCase(unittest.TestCase):
    def test_spawn_and_types(self):
        root = fl_nbt.loads(nbt_bytes())
        self.assertEqual(fl_nbt.spawn(root), (1274, 209, 181))
        self.assertEqual(root['Data']['version'], 19133)
        self.assertEqual(root['Data']['spawn']['dimension'], 'minecraft:overworld')

    def test_legacy_spawn_and_errors(self):
        self.assertEqual(fl_nbt.spawn({'Data': {'SpawnX': 1, 'SpawnY': 2, 'SpawnZ': 3}}), (1, 2, 3))
        with self.assertRaises(ValueError):
            fl_nbt.spawn({'Data': {}})
        with self.assertRaises(ValueError):
            fl_nbt.loads(b'\x0a\x00\x00\x0a')


if __name__ == '__main__':
    unittest.main()
