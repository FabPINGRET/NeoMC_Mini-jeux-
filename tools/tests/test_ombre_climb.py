"""Ombrelune : on monte à pied dans les tours, escaliers et colimaçons (tour de Liora, château, taverne, citadelle, arbres d'Aelindor),
et les échelles ont un dos plein et une sortie dégagée. Marche simulée sur les Vox de all_structures() (aucun serveur).
Lancer depuis la racine du dépôt : python -m unittest discover -s tools/tests -v   (la racine est dérivée de ce fichier).

Modèle : pieds en (x, y, z) ; appui solide dessous (ou échelle) ; pieds et tête libres ; montée de 1 avec une 3e case libre au-dessus de
la tête ; chute <= 3 ; échelle ; pas de diagonale. Tout bloc plein est un cube (dalles et escaliers aussi : plus strict que le jeu) ;
clôtures, murets, portillons et barreaux (1,5 de haut) ne se montent pas.
Hors Vox : au-dessus du sol virtuel c'est de l'air, en dessous c'est plein.
"""
import collections
import functools
import math
import re
import sys
import unittest
from pathlib import Path

ARCADE = Path(__file__).resolve().parents[2] / 'tools' / 'arcade'
if str(ARCADE) not in sys.path:
    sys.path.insert(0, str(ARCADE))
import ol_skit as K        # noqa: E402
import ol_structs as S     # noqa: E402

FREE_NAME = {'air', 'cave_air', 'void_air', 'ladder', 'lever', 'vine', 'rail', 'short_grass', 'bush', 'fern', 'poppy', 'dandelion',
             'cornflower', 'oxeye_daisy', 'azure_bluet', 'peony', 'lilac', 'rose_bush'}
FREE_END = ('_door', '_carpet', '_wall_banner', '_pressure_plate', '_button', '_sign', 'torch')
TALL_END = ('_fence', '_wall', '_fence_gate')      # `_wall_banner` n'y est pas : il est libre (FREE_END)
NOT_FULL_END = ('_stairs', '_slab', '_pane', '_fence', '_wall', '_trapdoor', '_carpet', 'lantern')
DIRS = ((1, 0), (-1, 0), (0, 1), (0, -1))
# arbres d'Aelindor (dx, dz, rayon, plateformes en hauteur au-dessus du sol), miroir de la liste `trees` de ol_region_nord.aelindor()
TREES = ((0, 0, 5, (10, 20, 32)), (-15, 12, 3, (10, 20)), (15, 10, 3, (10, 20)), (2, -16, 3, (10, 20)))
CASTLE_OUT = (0, -24)          # sur la rue, devant la porte de l'enceinte (z2 = -26)
TAVERN_OUT = (-22, 15)         # devant la porte est de la taverne (x2 = -24)


@functools.lru_cache(maxsize=None)
def structures():
    """all_structures() une seule fois pour tous les tests (construction lente, SPOTS / ARENAS ne s'enrichissent qu'une fois)."""
    return tuple(S.all_structures())


def name(b):
    return None if b is None else b.split('[')[0]


class Walk:
    def __init__(self, vox, ground, box):
        self.v, self.ground, self.box = vox.v, ground, box      # box = (x0, y0, z0, x1, y1, z1)

    def free(self, x, y, z):
        b = self.v.get((x, y, z))
        if b is None:
            return y > self.ground
        n = name(b)
        return n in FREE_NAME or n.endswith(FREE_END)

    def tall(self, x, y, z):
        """Clôture, muret, portillon, barreaux : 1,5 de haut, on ne les franchit pas d'un saut."""
        n = name(self.v.get((x, y, z)))
        return n is not None and (n.endswith(TALL_END) or n == 'iron_bars')

    def ladder(self, x, y, z):
        return name(self.v.get((x, y, z))) == 'ladder'

    def rises(self, x, y, z):
        """Monter d'une case sur place (échelle au-dessus) : surchargé par les marches qui nagent."""
        return self.ladder(x, y + 1, z)

    def sinks(self, x, y, z):
        """Descendre d'une case sur place (échelle sous les pieds ou eau dessous)."""
        return self.ladder(x, y, z)

    def supported(self, x, y, z):
        return not self.free(x, y - 1, z) or self.ladder(x, y, z) or self.ladder(x, y + 1, z)

    def moves(self, p):
        x, y, z = p
        out = []
        if self.rises(x, y, z) and self.free(x, y + 1, z) and self.free(x, y + 2, z):
            out.append((x, y + 1, z))
        if self.sinks(x, y, z) and self.free(x, y - 1, z):
            out.append((x, y - 1, z))
        for dx, dz in DIRS:
            nx, nz = x + dx, z + dz
            if self.free(nx, y, nz) and self.free(nx, y + 1, nz):
                yy = y
                while yy >= y - 3 and not self.supported(nx, yy, nz):
                    yy -= 1
                if yy >= y - 3:
                    out.append((nx, yy, nz))
            elif not self.free(nx, y, nz) and not self.tall(nx, y, nz) and self.free(nx, y + 1, nz) and self.free(nx, y + 2, nz) and self.free(x, y + 2, z):
                out.append((nx, y + 1, nz))
        return out

    def reach(self, start):
        x0, y0, z0, x1, y1, z1 = self.box
        seen = {start}
        q = collections.deque([start])
        while q:
            for n in self.moves(q.popleft()):
                if n not in seen and x0 <= n[0] <= x1 and y0 <= n[1] <= y1 and z0 <= n[2] <= z1:
                    seen.add(n)
                    q.append(n)
        return seen


def around(cx, cz, rad, y0, y1):
    return (cx - rad, y0, cz - rad, cx + rad, y1, cz + rad)


def cell(spot):
    return tuple(math.floor(c) for c in spot)


class OmbreClimb(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vox = {n: v for n, _region, v in structures()}
        cls.city = cls.vox['city']

    def floor_cells(self, reach, vox, y_feet, mat):
        """Cases atteintes dont les pieds sont à y_feet, posées sur le bloc mat."""
        return [p for p in reach if p[1] == y_feet and name(vox.v.get((p[0], y_feet - 1, p[2]))) == mat]

    def test_mage_tower_every_floor(self):
        lx, _, lz = cell(K.SPOTS['liora'])
        cx, cz = lx - 2, lz - 2                                     # spot('liora', cx + 2, Y + 1, cz + 2)
        G = K.G
        reach = Walk(self.city, G, around(cx, cz, 12, G, G + 45)).reach((cx + 7, G + 1, cz))   # dehors, devant la porte est
        for fy in (G + 9, G + 17, G + 25):
            self.assertEqual(name(self.city.v.get((cx, fy, cz))), 'dark_oak_planks', fy)
            self.assertIn((cx, fy + 1, cz), reach, 'plancher y%d de la tour de Liora inatteignable (max y%d)' % (fy, max(p[1] for p in reach)))

    def test_castle_keep_floors(self):
        G = K.G
        reach = Walk(self.city, G, (-25, G, -52, 25, G + 25, -22)).reach((CASTLE_OUT[0], G + 1, CASTLE_OUT[1]))
        for fy in (G + 10, G + 17):
            self.assertTrue(self.floor_cells(reach, self.city, fy, 'dark_oak_planks'), 'étage y%d du donjon inatteignable' % fy)

    def test_tavern_upper_floor(self):
        G = K.G
        reach = Walk(self.city, G, (-46, G, 6, -20, G + 12, 26)).reach((TAVERN_OUT[0], G + 1, TAVERN_OUT[1]))
        self.assertTrue(self.floor_cells(reach, self.city, G + 6, 'spruce_planks'), "étage de la taverne inatteignable")

    def test_citadel_keep_roof(self):
        (cx, y1, cz), (_, y36, _) = cell(K.ARENAS['malveth']['c']), cell(K.ARENAS['nyxar']['c'])
        reach = Walk(self.vox['citadel'], y1 - 1, around(cx, cz, 16, y1 - 1, y36 + 2)).reach((cx, y1, cz))
        self.assertIn((cx, y36, cz), reach, 'toit du donjon de la citadelle inatteignable (max y%d)' % max(p[1] for p in reach))

    def test_aelindor_platforms_and_queen(self):
        v = self.vox['aelindor']
        sx, sy, sz = cell(K.SPOTS['elf_ground'])
        ground = sy - 1
        cx, cz = sx + 8, sz - 8                                     # spot('elf_ground', cx - 8, y + 1, cz + 8)
        for tx, tz, r, plats in TREES:      # un BFS par arbre : les ponts de corde relient les plateformes entre elles, ce qui masquerait un colimaçon cassé
            with self.subTest(arbre=(cx + tx, cz + tz)):
                w = Walk(v, ground, around(cx + tx, cz + tz, r + 5, ground, ground + 50))
                start = (cx + tx + r + 4, sy, cz + tz)                      # au sol, à côté du tronc
                self.assertTrue(w.free(*start) and w.free(start[0], sy + 1, start[2]) and w.supported(*start), 'départ %s invalide' % (start,))
                reach = w.reach(start)
                for h in plats:
                    py = ground + h
                    got = [p for p in reach if p[1] == py + 1 and name(v.v.get((p[0], py, p[2]))) == 'birch_planks'
                           and r + 0.5 < math.hypot(p[0] - cx - tx, p[2] - cz - tz) <= r + 5]
                    self.assertTrue(got, 'plateforme y%d de l\'arbre (%d, %d) inatteignable (max y%d)' % (py, cx + tx, cz + tz, max(p[1] for p in reach)))
        reach = Walk(v, ground, around(cx, cz, 40, ground, ground + 50)).reach((sx, sy, sz))
        self.assertIn(cell(K.SPOTS['elyndra']), reach, "salle d'Elyndra inatteignable")

    def ladder_problems(self, vox):
        """Échelles sans dos plein, ou dont le sommet n'a pas de sortie (case libre au-dessus + sol voisin au même niveau)."""
        w, bad = Walk(vox, -10 ** 6, None), []
        for (x, y, z), b in vox.v.items():
            if name(b) != 'ladder':
                continue
            dx, dz = K.dir_vec(b[len('ladder[facing='):].split(',')[0].rstrip(']'))
            back = vox.v.get((x - dx, y, z - dz))
            if back is None or w.free(x - dx, y, z - dz) or name(back).endswith(NOT_FULL_END) or name(back) in ('iron_bars', 'iron_chain'):
                bad.append(('dos', x, y, z, back))
            if name(vox.v.get((x, y + 1, z))) != 'ladder':
                exits = [n for n in DIRS if not w.free(x + n[0], y, z + n[1]) and w.free(x + n[0], y + 1, z + n[1])
                         and w.free(x + n[0], y + 2, z + n[1])]
                if not (exits and w.free(x, y + 1, z) and w.free(x, y + 2, z)):
                    bad.append(('sortie', x, y, z, None))
        return bad

    def test_ladders_have_solid_back_and_free_exit(self):
        for n in ('city', 'brumecombe', 'bandit_fort'):
            with self.subTest(n):
                self.assertEqual(self.ladder_problems(self.vox[n]), [])

    @staticmethod
    def emit_order(cmds):
        """Rang d'émission de chaque case (x, y, z) dans une liste de commandes setblock / fill."""
        rank = {}
        for i, c in enumerate(cmds):
            p = c.split()
            if p[0] == 'setblock':
                x1, y1, z1, x2, y2, z2 = (int(t) for t in (p[1], p[2], p[3]) * 2)
            else:
                x1, y1, z1, x2, y2, z2 = (int(t) for t in p[1:7])
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    for z in range(z1, z2 + 1):
                        rank[(x, y, z)] = i
        return rank

    def test_ladders_emitted_after_their_back(self):
        """Reconstruction en place : une échelle posée avant son dos saute si l'ancien dos est une vitre. Même conversion que gen_ombrelune.py."""
        for n, _region, v in structures():
            with self.subTest(n):
                rank = self.emit_order(K.struct_cmds(v))
                bad = []
                for (x, y, z), b in v.v.items():
                    if name(b) != 'ladder':
                        continue
                    dx, dz = K.dir_vec(b[len('ladder[facing='):].split(',')[0].rstrip(']'))
                    back = (x - dx, y, z - dz)
                    if back in v.v and rank[back] > rank[(x, y, z)]:
                        bad.append(((x, y, z), back))
                self.assertEqual(bad, [], 'échelle émise avant son dos')

    def test_generator_uses_struct_cmds(self):
        """Garde de source : gen_ombrelune écrit les structures via struct_cmds (échelles en fin de passe), pas via un v.cmds() nu."""
        src = (ARCADE / 'gen_ombrelune.py').read_text(encoding='utf-8')
        self.assertIn('S.struct_cmds(v)', src)
        self.assertIsNone(re.search(r'\bv\.cmds\(', src), 'gen_ombrelune appelle v.cmds() directement')


if __name__ == '__main__':
    unittest.main()
