"""Terra Nova : donjons à salles et vagues (tools/arcade/tv_dungeons.py). Vérifie les fonctions générées dans data/ et la taille des sources.
Lancer depuis n'importe où : python -m unittest discover -s tools/tests -v   (la racine du dépôt est dérivée de ce fichier).
"""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FUNC = ROOT / 'data' / 'mg' / 'function'
KEYS = ('arbre', 'pic', 'mine', 'tube')                 # ordre de DUNGEONS (tv_world.py) : l'indice i sert aux scores $trds<i>, mg.trdw<i>
SOURCES = ('tools/arcade/tv_dungeons.py', 'tools/arcade/tv_classes.py')
SOURCE_MAX = 500                                        # plafond dur (cible 300)


def bases():
    """Dossiers rpg de Terra Nova : l'original, et les copies suffixées (terra2/rpg…) si un générateur de variantes en produit."""
    return [b / 'rpg' for b in sorted(FUNC.glob('terra*')) if (b / 'rpg' / 'dungeons.mcfunction').is_file()]


def read(base, rel):
    return (base / rel).read_text(encoding='utf-8')


class TerraDungeons(unittest.TestCase):
    def test_bases_found(self):
        self.assertTrue(bases(), 'aucun terra*/rpg/dungeons.mcfunction : lancer tools/arcade/gen_terranova.py .')

    def test_setup_resets_state(self):
        for base in bases():
            setup = read(base, 'dg_setup.mcfunction')
            for i in range(len(KEYS)):
                self.assertIn(f'scoreboard players set $trds{i} mg.st 0', setup, f'{base}: dg_setup sans $trds{i}')

    def test_reset_and_win_clear_state(self):
        for base in bases():
            for i, key in enumerate(KEYS):
                for fn in ('reset', 'win'):
                    self.assertIn(f'scoreboard players set $trds{i} mg.st 0', read(base, f'dg/{key}_{fn}.mcfunction'), f'{base}: {key}_{fn} ne remet pas $trds{i} à 0')
                reset = read(base, f'dg/{key}_reset.mcfunction')
                self.assertIn(f'tag=mg.trdw{i}', reset, f'{base}: {key}_reset ne renvoie pas les mobs de vague (mg.trdw{i})')
                self.assertIn('-400', reset)

    def test_alpha_start_gated_by_state_6(self):
        for base in bases():
            ns = base.parent.name                           # terra, ou terra2… pour une copie suffixée (common._tx réécrit mg:terra/)
            lines = read(base, 'dungeons.mcfunction').splitlines()
            for i, key in enumerate(KEYS):
                starts = [l for l in lines if l.endswith(f'run function mg:{ns}/rpg/dg/{key}_start')]
                self.assertEqual(len(starts), 1, f'{base}: appel de {key}_start introuvable ou multiple')
                self.assertIn(f'if score $trds{i} mg.st matches 6 ', starts[0], f'{base}: {key}_start non gardé par $trds{i} = 6')

    def test_room_functions(self):
        for base in bases():
            ns = base.parent.name
            dungeons = read(base, 'dungeons.mcfunction')
            for i, key in enumerate(KEYS):
                for n in range(3):
                    wave = read(base, f'dg/{key}_w{n}.mcfunction')           # FileNotFoundError si absente
                    clear = read(base, f'dg/{key}_c{n}.mcfunction')
                    self.assertIn(f'scoreboard players set $trds{i} mg.st {2 * n + 1}', wave)
                    self.assertIn(f'tag @e[tag=mg.trnew] add mg.trdw{i}', wave)
                    self.assertIn('tag @e[tag=mg.trnew] add mg.trr', wave)
                    self.assertIn(f'scoreboard players set $trds{i} mg.st {2 * n + 2}', clear)
                    self.assertIn(f'if score $trds{i} mg.st matches {2 * n} ', dungeons, f'{base}: déclencheur de {key} salle {n + 1}')
                    self.assertIn(f'if score $trds{i} mg.st matches {2 * n + 1} ', dungeons, f'{base}: nettoyage de {key} salle {n + 1}')
                    spawned = wave.count(f'run function mg:{ns}/dino/')
                    self.assertEqual(spawned, 6, f'{base}: {key}_w{n} : 6 emplacements d\'apparition attendus (plafond de la vague)')

    def test_wave_size_capped(self):
        for base in bases():
            for key in KEYS:
                for n in range(3):
                    wave = read(base, f'dg/{key}_w{n}.mcfunction')
                    self.assertIn('matches 7.. run scoreboard players set $trwn mg.st 6', wave, f'{base}: {key}_w{n} sans plafond à 6')
                    self.assertNotIn('matches 7.. positioned', wave)

    def test_absence_reset_covers_waves(self):
        for base in bases():
            ns = base.parent.name
            dungeons = read(base, 'dungeons.mcfunction')
            for i, key in enumerate(KEYS):
                self.assertIn(f'unless score $trds{i} mg.st matches 0 if score $trdr{i} mg.st matches 20.. run function mg:{ns}/rpg/dg/{key}_reset', dungeons)
                self.assertNotIn('trdr', read(base, f'dg/{key}.mcfunction'), f'{base}: le reset par absence doit rester unique (dungeons.mcfunction)')

    def test_cooldown_and_safety_net(self):
        for base in bases():
            dungeons = read(base, 'dungeons.mcfunction').splitlines()
            for i, key in enumerate(KEYS):
                for n in range(3):
                    trig = [l for l in dungeons if f'run function mg:{base.parent.name}/rpg/dg/{key}_w{n}' in l]
                    self.assertEqual(len(trig), 1, f'{base}: déclencheur de {key}_w{n} introuvable ou multiple')
                    self.assertIn(f'if score $trdc{i} mg.st matches ..0 ', trig[0], f'{base}: {key}_w{n} non gardé par le cooldown $trdc{i}')
                    net = [l for l in dungeons if f'matches {2 * n + 1} as @e[tag=mg.trdw{i}]' in l and 'run tp @s' in l]
                    self.assertEqual(len(net), 1, f'{base}: filet de {key} salle {n + 1} introuvable ou multiple')
                lock = [l for l in dungeons if l.endswith(f'dg/{key}_lock')]
                self.assertEqual(len(lock), 1)
                self.assertIn(f'if score $trdc{i} mg.st matches ..0 unless entity @e[tag=mg.trdw{i}]', lock[0], f'{base}: {key}_lock affiché pendant le cooldown ou une vague')
                reset = read(base, f'dg/{key}_reset.mcfunction')
                self.assertLess(reset.index(f'$trdc{i} mg.st 60'), reset.index(f'set $trds{i} mg.st 0'), f'{base}: {key}_reset : cooldown à poser avant la remise à 0')
                for n in range(3):
                    self.assertIn('gamemode=adventure', next(l for l in read(base, f'dg/{key}_c{n}.mcfunction').splitlines() if '/xp ' in l))
                self.assertIn('gamemode=adventure', next(l for l in read(base, f'dg/{key}_win.mcfunction').splitlines() if f'dg/{key}_rw' in l))


class SourceSize(unittest.TestCase):
    def test_sources_under_hard_cap(self):
        for rel in SOURCES:
            n = len((ROOT / rel).read_text(encoding='utf-8').splitlines())
            self.assertLessEqual(n, SOURCE_MAX, f'{rel} : {n} lignes (plafond dur {SOURCE_MAX})')


if __name__ == '__main__':
    unittest.main()
