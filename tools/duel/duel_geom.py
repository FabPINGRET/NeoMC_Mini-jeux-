"""Duel sniper : géométrie des arènes (utilisé par gen_duel_maps.py).

Repère local : x et zl comptés depuis le centre de la carte (bloc 0), y absolu ; l'arène intérieure fait
x -20..20 et zl -70..70 (41 x 141). La carte est symétrique par rotation de 180 degrés autour du bloc (0, 0) :
sfill / sput posent la forme ET son double tourné (les orientations facing=... sont inversées), donc les deux
départs sont strictement équivalents. Tout remplissage est découpé en morceaux de 32 768 blocs au plus.
"""
import re

LIM = 32768
OPP = {'north': 'south', 'south': 'north', 'east': 'west', 'west': 'east'}
DIR_Z = {-1: 'north', 1: 'south'}
HX, HZ = 20, 70                 # demi-emprise intérieure
TOP, BOT = 113, 62              # tranche d'air et de barrières


VOL = 100000                    # blocs posés au plus par lot (un tick de construction raisonnable)


def volume(line):
    """Nombre de blocs posés par une commande fill / setblock."""
    t = line.split(' ')
    if t[0] != 'fill':
        return 1 if t[0] == 'setblock' else 0
    x1, y1, z1, x2, y2, z2 = map(int, t[1:7])
    return (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1) * (abs(z2 - z1) + 1)


def blk(b):
    return b if ':' in b else 'minecraft:' + b


def rot(b):
    """Bloc tourné de 180 degrés (facing=north <-> south, east <-> west)."""
    return re.sub(r'facing=(north|south|east|west)', lambda m: 'facing=' + OPP[m.group(1)], b)


def split(lo, hi):
    """Boîte (lo, hi) découpée en morceaux de LIM blocs au plus."""
    n = (hi[0] - lo[0] + 1) * (hi[1] - lo[1] + 1) * (hi[2] - lo[2] + 1)
    if n <= LIM:
        return [(lo, hi)]
    ax = max(range(3), key=lambda i: hi[i] - lo[i])
    mid = (lo[ax] + hi[ax]) // 2
    a_hi, b_lo = list(hi), list(lo)
    a_hi[ax], b_lo[ax] = mid, mid + 1
    return split(lo, tuple(a_hi)) + split(tuple(b_lo), hi)


class Arena:
    def __init__(self, z0):
        self.z0 = z0
        self.L = []

    def note(self, text):
        self.L.append('# ' + text)

    def fill(self, x1, y1, z1, x2, y2, z2, b):
        lo = (min(x1, x2), min(y1, y2), min(z1, z2))
        hi = (max(x1, x2), max(y1, y2), max(z1, z2))
        for (a, c) in split(lo, hi):
            self.L.append(f'fill {a[0]} {a[1]} {self.z0 + a[2]} {c[0]} {c[1]} {self.z0 + c[2]} {blk(b)}')

    def put(self, x, y, z, b):
        self.L.append(f'setblock {x} {y} {self.z0 + z} {blk(b)}')

    def sfill(self, x1, y1, z1, x2, y2, z2, b):
        self.fill(x1, y1, z1, x2, y2, z2, b)
        self.fill(-x2, y1, -z2, -x1, y2, -z1, rot(b))

    def sput(self, x, y, z, b):
        self.put(x, y, z, b)
        self.put(-x, y, -z, rot(b))

    def stairs(self, x1, x2, z, dz, y0, n, mat, under, floor, sym=True):
        """Escalier de n marches de largeur x1..x2, parcouru dans le sens dz (+-1) en montant d'un bloc par marche."""
        f = self.sfill if sym else self.fill
        for i in range(n):
            f(x1, floor, z + dz * i, x2, y0 + i - 1, z + dz * i, under)
            f(x1, y0 + i, z + dz * i, x2, y0 + i, z + dz * i, f'{mat}[facing={DIR_Z[dz]},half=bottom]')

    def prologue(self):
        self.note('air sur toute la tranche, puis barrieres (le rayon du sniper s\'arrete dessus)')
        self.fill(-HX - 2, BOT, -HZ - 2, HX + 2, TOP, HZ + 2, 'air')

    def cage(self):
        self.fill(-HX - 1, BOT, -HZ - 1, HX + 1, TOP, -HZ - 1, 'barrier')
        self.fill(-HX - 1, BOT, HZ + 1, HX + 1, TOP, HZ + 1, 'barrier')
        self.fill(-HX - 1, BOT, -HZ - 1, -HX - 1, TOP, HZ + 1, 'barrier')
        self.fill(HX + 1, BOT, -HZ - 1, HX + 1, TOP, HZ + 1, 'barrier')
        self.fill(-HX - 1, TOP, -HZ - 1, HX + 1, TOP, HZ + 1, 'barrier')

    def chunks(self, size, blocks=VOL):
        """Commandes en lots de `size` commandes ou `blocks` blocs au plus (les commentaires ne comptent pas)."""
        out, cur, n, v = [], [], 0, 0
        for l in self.L:
            if cur and not l.startswith('#') and (n >= size or v + volume(l) > blocks):
                out.append(cur)
                cur, n, v = [], 0, 0
            cur.append(l)
            if not l.startswith('#'):
                n += 1
                v += volume(l)
        if cur:
            out.append(cur)
        return out
