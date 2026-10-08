"""Terrain des parcours de la Course d'elytres : relief en cellules, coque creuse, fusion de rectangles, fills.

Le relief est stocke par cellules de S x S blocs ; chaque cellule porte une liste d'intervalles pleins
[(y0, y1)] (un seul pour un relief simple, plusieurs pour les arches et les chapeaux de cheminees de fee).
Pour tenir dans un budget de commandes raisonnable, seule une COQUE de `tv` blocs sous la surface
(et de `th` cellules sur les parois) est construite : tout le reste est vide.
Python stdlib uniquement (compatible 3.8).
"""
import math
import random

S = 4                       # cote d'une cellule (blocs)
BIG = 10000                 # « moins l'infini » : les cellules de relief descendent sans fond
MAX_FILL = 32768            # limite de blocs d'un fill (gamerule maxCommandModificationLimit)


# ---------------------------------------------------------------- bruit
def _hash(ix, iz, seed):
    n = (ix * 374761393 + iz * 668265263 + seed * 1442695040888963407) & 0xFFFFFFFF
    n = ((n ^ (n >> 13)) * 1274126177) & 0xFFFFFFFF
    return ((n ^ (n >> 16)) & 0xFFFFFF) / 16777215.0


def vnoise(x, z, seed):
    """Bruit de valeur lisse dans [0, 1]."""
    ix, iz = math.floor(x), math.floor(z)
    fx, fz = x - ix, z - iz
    fx, fz = fx * fx * (3 - 2 * fx), fz * fz * (3 - 2 * fz)
    a, b = _hash(ix, iz, seed), _hash(ix + 1, iz, seed)
    c, d = _hash(ix, iz + 1, seed), _hash(ix + 1, iz + 1, seed)
    return (a + (b - a) * fx) + ((c + (d - c) * fx) - (a + (b - a) * fx)) * fz


def fbm(x, z, seed, octaves=4, scale=60.0):
    """Bruit fractal (fBm) dans [-1, 1]."""
    tot, amp, norm, f = 0.0, 1.0, 0.0, 1.0 / scale
    for o in range(octaves):
        tot += (vnoise(x * f, z * f, seed + o * 101) * 2 - 1) * amp
        norm += amp
        amp *= 0.5
        f *= 2.0
    return tot / norm


def smooth(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def lerp_pts(pts, x):
    """Interpolation lineaire par morceaux sur [(x, v), ...] trie."""
    if x <= pts[0][0]:
        return pts[0][1]
    for (xa, va), (xb, vb) in zip(pts, pts[1:]):
        if x <= xb:
            return va + (vb - va) * (x - xa) / float(xb - xa)
    return pts[-1][1]


def smooth_pts(pts, x):
    """Comme lerp_pts mais avec des raccords doux entre les points."""
    if x <= pts[0][0]:
        return pts[0][1]
    for (xa, va), (xb, vb) in zip(pts, pts[1:]):
        if x <= xb:
            return va + (vb - va) * smooth((x - xa) / float(xb - xa))
    return pts[-1][1]


# ---------------------------------------------------------------- intervalles
def iv_union(ivs):
    out = []
    for a, b in sorted(ivs):
        if out and a <= out[-1][1] + 1:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return out


def iv_cut(ivs, a, b):
    out = []
    for lo, hi in ivs:
        if hi < a or lo > b:
            out.append([lo, hi])
            continue
        if lo < a:
            out.append([lo, a - 1])
        if hi > b:
            out.append([b + 1, hi])
    return out


def iv_inter(p, q):
    out, i, j = [], 0, 0
    while i < len(p) and j < len(q):
        a, b = max(p[i][0], q[j][0]), min(p[i][1], q[j][1])
        if a <= b:
            out.append([a, b])
        if p[i][1] < q[j][1]:
            i += 1
        else:
            j += 1
    return out


def iv_sub(p, q):
    """p moins q."""
    out = [list(x) for x in p]
    for a, b in q:
        out = iv_cut(out, a, b)
    return out


def iv_erode(ivs, t):
    return [[a + t, b - t] for a, b in ivs if b - a >= 2 * t]


# ---------------------------------------------------------------- strates
def make_strata(seed, palette, top=420):
    """Bandes horizontales de materiaux : liste de (y0, y1, bloc), epaisseurs 3 a 8."""
    rnd = random.Random(seed)
    bands, y, last = [], 0, None
    while y < top:
        h = rnd.choice([3, 3, 4, 4, 5, 6, 8])
        blk = rnd.choice(palette)
        while blk == last:
            blk = rnd.choice(palette)
        bands.append((y, y + h - 1, blk))
        last = blk
        y += h
    return bands


class World:
    """Grille de cellules + boites pleines (anneaux, ponts, batiments) servant aux collisions du pilote."""

    def __init__(self, x0, z0, nx, nz):
        self.x0, self.z0, self.nx, self.nz = x0, z0, nx, nz
        self.cells = [[[[-BIG, -BIG]] for _ in range(nz)] for _ in range(nx)]
        self.vox = set()            # blocs pleins hors cellules
        self.cmds = []              # commandes posees apres le relief : ('fill', x1, y1, z1, x2, y2, z2, bloc) ou ('set', x, y, z, bloc)

    # --- cellules
    def cell_x(self, i):
        return self.x0 + i * S

    def cell_z(self, j):
        return self.z0 + j * S

    def ij(self, x, z):
        return int((x - self.x0) // S), int((z - self.z0) // S)

    def ground(self, i, j, h):
        self.cells[i][j] = [[-BIG, int(h)]]

    def top(self, i, j):
        return self.cells[i][j][-1][1]

    def add(self, i, j, y0, y1):
        if 0 <= i < self.nx and 0 <= j < self.nz:
            self.cells[i][j] = iv_union(self.cells[i][j] + [[int(y0), int(y1)]])

    def cut(self, i, j, y0, y1):
        if 0 <= i < self.nx and 0 <= j < self.nz:
            self.cells[i][j] = iv_cut(self.cells[i][j], int(y0), int(y1))

    # --- boites (blocs)
    def box(self, x1, y1, z1, x2, y2, z2, blk, solid=True):
        x1, x2, y1, y2, z1, z2 = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2), min(z1, z2), max(z1, z2)
        self.cmds.append(('fill', x1, y1, z1, x2, y2, z2, blk))
        if solid and blk not in ('air', 'light'):
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    for z in range(z1, z2 + 1):
                        self.vox.add((x, y, z))
        elif blk == 'air':
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    for z in range(z1, z2 + 1):
                        self.vox.discard((x, y, z))

    def block(self, x, y, z, blk, solid=False):
        self.cmds.append(('set', x, y, z, blk))
        if solid:
            self.vox.add((x, y, z))

    def solid(self, x, y, z):
        if (x, y, z) in self.vox:
            return True
        i, j = (x - self.x0) >> 2, (z - self.z0) >> 2
        if i < 0 or j < 0 or i >= self.nx or j >= self.nz:
            return False
        for a, b in self.cells[i][j]:
            if a <= y <= b:
                return True
        return False

    # --- coque creuse
    def shell(self, tv=6, th=2):
        """Intervalles conserves par cellule : seules les parties a moins de tv blocs (verticalement) ou th cellules
        (horizontalement) de l'air sont construites."""
        er = [[iv_erode(self.cells[i][j], tv) for j in range(self.nz)] for i in range(self.nx)]
        kept = {}
        for i in range(self.nx):
            for j in range(self.nz):
                inner = er[i][j]
                for di in range(-th, th + 1):
                    ii = min(max(i + di, 0), self.nx - 1)
                    for dj in range(-th, th + 1):
                        if inner:
                            inner = iv_inter(inner, er[ii][min(max(j + dj, 0), self.nz - 1)])
                k = iv_sub(self.cells[i][j], inner)
                if k:
                    kept[(i, j)] = k
        return kept

    def rects(self, kept, strata, ymin):
        """Decoupe en bandes de materiaux, puis fusionne les cellules voisines identiques en rectangles.
        Retourne une liste de (x1, y1, z1, x2, y2, z2, bloc)."""
        groups = {}
        for (i, j), ivs in kept.items():
            for a, b in ivs:
                a = max(a, ymin)
                for (s0, s1, blk) in strata:
                    if s1 < a:
                        continue
                    if s0 > b:
                        break
                    groups.setdefault((max(a, s0), min(b, s1), blk), set()).add((i, j))
        out = []
        for (ya, yb, blk), cs in groups.items():
            done = set()
            for (i, j) in sorted(cs):
                if (i, j) in done:
                    continue
                i2 = i
                while (i2 + 1, j) in cs and (i2 + 1, j) not in done:
                    i2 += 1
                j2 = j
                while all((ii, j2 + 1) in cs and (ii, j2 + 1) not in done for ii in range(i, i2 + 1)):
                    j2 += 1
                for ii in range(i, i2 + 1):
                    for jj in range(j, j2 + 1):
                        done.add((ii, jj))
                out.append((self.cell_x(i), ya, self.cell_z(j), self.cell_x(i2) + S - 1, yb, self.cell_z(j2) + S - 1, blk))
        out.sort(key=lambda r: (r[0], r[2], r[1]))
        return out


def split_fill(f):
    """Decoupe un fill ('fill', x1, y1, z1, x2, y2, z2, bloc) en morceaux de MAX_FILL blocs au plus."""
    _, x1, y1, z1, x2, y2, z2, blk = f
    n = (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
    if n <= MAX_FILL:
        return [f]
    dims = [x2 - x1 + 1, y2 - y1 + 1, z2 - z1 + 1]
    ax = dims.index(max(dims))
    lo, hi = (x1, y1, z1)[ax], (x2, y2, z2)[ax]
    mid = (lo + hi) // 2
    a, b = [x1, y1, z1, x2, y2, z2], [x1, y1, z1, x2, y2, z2]
    a[3 + ax], b[ax] = mid, mid + 1
    return split_fill(('fill',) + tuple(a) + (blk,)) + split_fill(('fill',) + tuple(b) + (blk,))


def clip_cmd(c, xa, xb):
    """Restreint une commande a la tranche x [xa, xb] (None si hors tranche)."""
    if c[0] == 'set':
        return c if xa <= c[1] <= xb else None
    _, x1, y1, z1, x2, y2, z2, blk = c
    if x2 < xa or x1 > xb:
        return None
    return ('fill', max(x1, xa), y1, z1, min(x2, xb), y2, z2, blk)


def cmd_text(c):
    if c[0] == 'set':
        return 'setblock %d %d %d minecraft:%s' % c[1:]
    return 'fill %d %d %d %d %d %d minecraft:%s' % c[1:]
