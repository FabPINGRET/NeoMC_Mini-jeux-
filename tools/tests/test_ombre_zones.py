"""Ombrelune : acces a pied aux trois zones qui etaient fermees (citadelle de Malveth, ile de Morvaine, cathedrale de Havreclair).
Marche simulee (modele de test_ombre_climb.Walk) sur le relief reel (W.H / W.COL) et toutes les constructions fusionnees dans l'ordre
d'all_structures(), comme sur le serveur. L'eau se nage : on y monte sur place et on la quitte par un saut d'une case ; la lave ne se traverse pas.
Lancer depuis la racine du depot : python -m unittest discover -s tools/tests -v   (la racine est derivee de ce fichier).
"""
import collections
import functools
import sys
import types
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ARCADE = HERE.parent / 'arcade'
for p in (str(ARCADE), str(HERE)):
    if p not in sys.path:
        sys.path.insert(0, p)
import ol_skit as K            # noqa: E402
import ol_world as W           # noqa: E402
import test_ombre_climb as T   # noqa: E402

WATER = {'water', 'bubble_column', 'seagrass', 'tall_seagrass', 'kelp', 'kelp_plant'}


@functools.lru_cache(maxsize=None)
def world():
    """Toutes les constructions en une seule table (x, y, z) -> bloc : le dernier ecrit gagne, dans l'ordre d'all_structures(), comme sur le serveur.
    Hors vegetation (W.VEG) et murs de region (W.WALLS_R), que le serveur pose avant / apres les constructions et que ce modele ne simule pas."""
    merged = {}
    for _n, _region, vox in T.structures():
        merged.update(vox.v)
    return merged


class ZoneWalk(T.Walk):
    """Walk sur la carte entiere : hors constructions, plein sous le relief (H) et libre au-dessus ; eau nageable, lave interdite.
    opened : cases forcees a l'air (une porte ouverte par door/*_open)."""

    def __init__(self, box, opened=()):
        overlay = {c: 'air' for c in opened}
        super().__init__(types.SimpleNamespace(v=collections.ChainMap(overlay, world())), None, box)

    def fluid(self, x, y, z):
        c = W.COL.get((x, z))
        return c is not None and c[2] is not None and W.H[(x, z)] < y <= (c[3] or 0)

    def free(self, x, y, z):
        b = self.v.get((x, y, z))
        if b is None:
            h = W.H.get((x, z))
            return h is not None and y > h and not (self.fluid(x, y, z) and 'lava' in W.COL[(x, z)][2])
        n = T.name(b)
        return n in T.FREE_NAME or n.endswith(T.FREE_END) or n in WATER

    def wet(self, x, y, z):
        b = self.v.get((x, y, z))
        if b is None:
            return self.fluid(x, y, z) and 'water' in W.COL[(x, z)][2]
        return T.name(b) in WATER

    def ladder(self, x, y, z):
        return T.name(self.v.get((x, y, z))) in ('ladder', 'vine')

    def rises(self, x, y, z):
        return self.ladder(x, y + 1, z) or self.wet(x, y, z)

    def sinks(self, x, y, z):
        return self.ladder(x, y, z) or self.wet(x, y - 1, z)

    def supported(self, x, y, z):
        return super().supported(x, y, z) or self.wet(x, y, z)

    def stand(self, x, z, hint):
        """Position debout (pieds) en (x, z) a +-3 de hint, ou None."""
        for y in range(hint + 3, hint - 4, -1):
            if self.free(x, y, z) and self.free(x, y + 1, z) and self.supported(x, y, z):
                return (x, y, z)
        return None


class OmbreZones(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        world()            # SPOTS / ARENAS ne sont remplis que par all_structures() : les lire avant ferait un KeyError (test lance seul)

    def assertStandable(self, w, p):
        self.assertTrue(w.free(*p) and w.free(p[0], p[1] + 1, p[2]) and w.supported(*p), 'depart %s invalide' % (p,))

    def test_citadel_gate_guards_keep(self):
        """Depuis le camp rebelle : cour et pied du donjon atteignables, salle du trone fermee par la grille, ouverte une fois la grille tombee."""
        (sx, sy, sz), (cx, y1, cz), (_, y36, _) = T.cell(K.SPOTS['cit_out']), T.cell(K.ARENAS['malveth']['c']), T.cell(K.ARENAS['nyxar']['c'])
        gx, gy1, gz1, _, gy2, gz2 = (int(c) for c in K.SPOTS['cit_gate'])
        box = T.around(cx, cz, 44, sy - 10, y36 + 2)
        w = ZoneWalk(box)
        self.assertStandable(w, (sx, sy, sz))
        reach = w.reach((sx, sy, sz))
        self.assertIn((gx + 1, gy1, (gz1 + gz2) // 2), reach, 'pied de la grille du donjon inatteignable depuis cit_out (max y%d)' % max(p[1] for p in reach))
        px, py, pz = T.cell(K.SPOTS['pylons'][0])
        self.assertIn((px + 2, py, pz), reach, 'cour de la citadelle (pylone) inatteignable sans ouvrir la grille')
        self.assertNotIn((cx, y1, cz), reach, 'la grille du donjon ne ferme plus la salle du trone')
        opened = [(gx, y, z) for y in range(gy1, gy2 + 1) for z in range(gz1, gz2 + 1)]
        reach = ZoneWalk(box, opened).reach((sx, sy, sz))
        self.assertIn((cx, y1, cz), reach, 'salle du trone inatteignable grille ouverte')
        self.assertIn((cx, y36, cz), reach, 'sommet du donjon inatteignable grille ouverte')

    def test_morvaine_totems_reach_arena(self):
        """Depuis chaque totem de la rive : l'arene de la sorciere, par le ponton ou a la nage."""
        ax, ay, az = T.cell(K.ARENAS['morvaine']['c'])
        w = ZoneWalk(T.around(ax, az, 45, ay - 14, ay + 6))
        for t in K.SPOTS['totems']:
            tx, ty, tz = T.cell(t)
            with self.subTest(totem=(tx, tz)):
                starts = [s for s in (w.stand(tx + dx, tz + dz, ty) for dx, dz in T.DIRS) if s]
                self.assertTrue(starts, 'aucune case libre autour du totem')
                reach = w.reach(starts[0])
                self.assertIn((ax, ay, az), reach, "arene de Morvaine inatteignable depuis le totem (max y%d)" % max(p[1] for p in reach))

    def test_cathedral_nave_transept_altar(self):
        """Depuis la rue, devant l'entree sud : nef, bras du transept et autel (les murs du transept coupaient la nef)."""
        G = K.G
        w = ZoneWalk(T.around(33, -31, 20, G, G + 30))
        start = (33, G + 1, -18)
        self.assertStandable(w, start)
        reach = w.reach(start)
        ax, ay, az = T.cell(K.SPOTS['altar'])
        self.assertIn((ax, ay, az), reach, "autel de la cathedrale inatteignable (max z%d)" % min(p[2] for p in reach))
        for x in (26, 41):
            self.assertIn((x, ay, -31), reach, 'bras du transept (x%d) inatteignable' % x)


if __name__ == '__main__':
    unittest.main()
