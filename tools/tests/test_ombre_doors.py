"""Ombrelune : portes de quete (citadelle, kgate, pyramide) et synchro des stations (st/<region>), lues dans les fonctions generees
(data/mg/function/ombre). Une porte ouverte par la quete est memorisee (mg:ombre doors.<porte>) : la synchro, rejouee a chaque changement
de SV, ne la referme que si le drapeau est absent. Seuls world_build / wb_done (reconstruction) et la desinstallation l'effacent ; door/catchup
rouvre ensuite toute porte sans drapeau des qu'un joueur a depasse l'etape qui l'ouvre (st/done, enter, second).
Lancer depuis la racine du depot : python -m unittest discover -s tools/tests -v   (la racine est derivee de ce fichier).
"""
import re
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OMBRE = ROOT / 'data' / 'mg' / 'function' / 'ombre'
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
import test_ombre_zones as Z   # noqa: E402
import ol_skit as K            # noqa: E402
import ol_world as W           # noqa: E402

DOORS = ('kgate', 'citadel', 'pyramid')
FILL = re.compile(r'^fill (-?\d+ -?\d+ -?\d+ -?\d+ -?\d+ -?\d+) (minecraft:\w+)$')
CATCHUP = 'function mg:ombre/door/catchup'
IN_DIM = 'execute in mg:ombrelune run ' + CATCHUP


def lines(path):
    return [l.strip() for l in Path(path).read_text(encoding='utf-8').splitlines() if l.strip() and not l.startswith('#')]


def guard(k):
    return 'execute unless data storage mg:ombre doors.%s run ' % k


def stations():
    """(fichier, ligne) de toutes les synchros de stations st/<n>.mcfunction."""
    return [(p.name, l) for p in sorted((OMBRE / 'st').glob('[0-9]*.mcfunction')) for l in lines(p)]


def open_box(k):
    fills = [FILL.match(l) for l in lines(OMBRE / 'door' / ('%s_open.mcfunction' % k))]
    fills = [m for m in fills if m and m.group(2) == 'minecraft:air']
    assert len(fills) == 1, '%s_open : un seul fill air attendu' % k
    return fills[0].group(1)


def open_step(k):
    """Etape de campagne qui ouvre la porte k, lue dans les q/actdone<i> generes (issus de Q.STEPS, door=<k>) : i, apres controle que
    l'appel est suivi de q/adv, qui incremente mg.olch (donc un joueur qui a fini l'etape i a mg.olch >= i + 1)."""
    call = 'execute in mg:ombrelune run function mg:ombre/door/%s_open' % k
    found = []
    for p in (OMBRE / 'q').glob('actdone[0-9]*.mcfunction'):
        ls = lines(p)
        if call in ls:
            assert ls[ls.index(call) + 1] == 'function mg:ombre/q/adv', '%s : q/adv doit suivre l\'ouverture' % p.name
            found.append(int(re.fullmatch(r'actdone(\d+)\.mcfunction', p.name).group(1)))
    assert len(found) == 1, 'porte %s : une seule etape attendue (%s)' % (k, found)
    return found[0]


class OmbreDoors(unittest.TestCase):
    def test_open_sets_flag(self):
        for k in DOORS:
            with self.subTest(k):
                ls = lines(OMBRE / 'door' / ('%s_open.mcfunction' % k))
                self.assertEqual(ls.count('data modify storage mg:ombre doors.%s set value 1b' % k), 1, ls)

    def test_close_is_guarded_by_flag(self):
        sts = stations()
        for k in DOORS:
            with self.subTest(k):
                box = open_box(k)
                closes = [(f, l) for f, l in sts if re.search(r'fill %s minecraft:(?!air$)' % re.escape(box), l)]
                self.assertEqual(len(closes), 1, 'fermeture de %s : une seule ligne attendue (%s)' % (k, closes))
                self.assertTrue(closes[0][1].startswith(guard(k)), 'fermeture de %s non gardee : %s' % (k, closes[0]))

    def test_no_close_outside_stations(self):
        """Aucune fermeture (fill de la boite de la porte avec un bloc autre que l'air) hors de la synchro st/ : sinon le drapeau serait contourne."""
        files = [p for p in OMBRE.rglob('*.mcfunction') if 'st' not in p.relative_to(OMBRE).parts[:-1]]
        self.assertGreater(len(files), 100, 'ombre/** : fonctions generees introuvables')
        for k in DOORS:
            with self.subTest(k):
                pat = re.compile(r'fill %s minecraft:(?!air\b)' % re.escape(open_box(k)))
                bad = [(str(p.relative_to(OMBRE)).replace('\\', '/'), l) for p in files for l in lines(p) if pat.search(l)]
                self.assertEqual(bad, [], 'fermeture de %s hors st/ : %s' % (k, bad))

    def test_flag_erased_by_rebuild_and_uninstall(self):
        rm = 'data remove storage mg:ombre doors'
        wb, done = lines(OMBRE / 'world_build.mcfunction'), lines(OMBRE / 'wb_done.mcfunction')
        self.assertIn(rm, wb)
        self.assertIn(rm, done)
        self.assertLess(done.index(rm), done.index('function mg:ombre/st/start'), 'wb_done : le drapeau doit tomber avant la resynchro (st/start)')
        self.assertIn(rm, lines(ROOT / 'data' / 'mg' / 'function' / 'desinstaller.mcfunction'))

    def test_only_known_functions_erase_flag(self):
        """Aucune autre fonction d'Ombrelune ne referme les portes ou n'efface le drapeau (pas de reset de quete qui les referme)."""
        erasers = sorted(str(p.relative_to(OMBRE)).replace('\\', '/') for p in OMBRE.rglob('*.mcfunction')
                         if any(l.startswith('data remove storage mg:ombre doors') for l in lines(p)))
        self.assertEqual(erasers, ['wb_done.mcfunction', 'world_build.mcfunction'])

    def test_catchup_line_per_door(self):
        """door/catchup : une ligne par porte, borne = etape qui l'ouvre + 1 (lue dans q/actdone<i>), coins de la boite charges, joueurs d'Ombrelune."""
        ls = lines(OMBRE / 'door' / 'catchup.mcfunction')
        self.assertEqual(len(ls), len(DOORS), ls)
        for k in DOORS:
            with self.subTest(k):
                x1, y1, z1, x2, y2, z2 = open_box(k).split()
                want = ('execute unless data storage mg:ombre doors.%s if loaded %s %s %s if loaded %s %s %s '
                        'if entity @a[tag=mg.olw,scores={mg.olch=%d..}] run function mg:ombre/door/%s_open' % (k, x1, y1, z1, x2, y2, z2, open_step(k) + 1, k))
                self.assertEqual([l for l in ls if l.endswith('door/%s_open' % k)], [want])
        self.assertIn('tag @s add mg.olw', lines(OMBRE / 'enter.mcfunction'), 'mg.olw : tag des joueurs dans Ombrelune')
        self.assertIn('scoreboard players add @s mg.olch 1', lines(OMBRE / 'q' / 'adv.mcfunction'), 'mg.olch : +1 par etape finie')

    def test_catchup_called_after_sync_and_on_enter(self):
        """Apres la synchro (st/done, derniere region deja resynchronisee), a l'entree (enter) et chaque seconde (second, chunks charges plus tard)."""
        self.assertIn(IN_DIM, lines(OMBRE / 'st' / 'done.mcfunction'))
        self.assertIn(IN_DIM, lines(OMBRE / 'enter.mcfunction'))
        self.assertIn(CATCHUP, lines(OMBRE / 'second.mcfunction'))
        enter = lines(OMBRE / 'enter.mcfunction')
        self.assertLess(enter.index('tag @s add mg.olw'), enter.index(IN_DIM), 'enter : le joueur doit etre tague avant le rattrapage')

    def test_open_uses_absolute_coordinates(self):
        """door/<k>_open s'execute sous `execute in <dimension>` sans joueur : fill et playsound en coordonnees absolues (aucun ~ ni ^)."""
        for k in DOORS:
            with self.subTest(k):
                for l in lines(OMBRE / 'door' / ('%s_open.mcfunction' % k)):
                    if l.startswith(('fill', 'playsound')):
                        self.assertNotRegex(l, r'[~^]', l)

    def test_legacy_enclosure_grille_cleared(self):
        """Serveur deja construit : l'ancienne grille d'enceinte (x2, y + 1..8) est videe par la synchro, et c'est de l'air dans l'etat genere."""
        w = Z.world()      # remplit aussi K.SPOTS (all_structures)
        x1, y1, z1, x2, y2, z2 = (int(c) for c in K.SPOTS['cit_gate_old'])
        self.assertNotEqual(x1, int(K.SPOTS['cit_gate'][0]), "la grille du donjon doit etre ailleurs que l'ancienne")
        fill = 'fill %d %d %d %d %d %d minecraft:air' % (x1, y1, z1, x2, y2, z2)
        self.assertEqual(sum(1 for _f, l in stations() if l == fill), 1, fill)

        def air(x, y, z):
            """Case absente des constructions : de l'air seulement au-dessus du relief (y > W.H), sinon c'est du terrain plein."""
            b = w.get((x, y, z))
            if b is None:
                h = W.H.get((x, z))
                return h is not None and y > h
            return Z.T.name(b).replace('minecraft:', '') == 'air'
        solid = [(x, y, z) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1) for z in range(z1, z2 + 1) if not air(x, y, z)]
        self.assertEqual(solid, [], 'la synchro viderait des blocs generes')


if __name__ == '__main__':
    unittest.main()
