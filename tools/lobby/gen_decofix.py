"""Décor du spawn remis d'aplomb après les déplacements (portails, socles d'élytra, entrée du foot) : python tools/lobby/gen_decofix.py .

Écrit hub/decofix (une seule fois par monde : drapeau mg:lobby decofix4 ; relancé aussi après chaque mg:hub/build) :
1. Anciens sites rendus au décor du spawn (theme_world.W : sol, haies, bancs, lampadaires, fleurs, arbres) : anciens portails GTA / Terra Nova /
   Ombrelune et leurs passages (haies de l'avenue nord refermées), anciens socles et allées d'élytra, anneau de l'ancienne place des plots
   hors du hub (en herbe). Les cases des constructions actuelles (hub, socles d'élytra, foot, arène PvP, Hall) ne sont jamais touchées.
2. Arbres coupés : tout arbre du spawn (tronc + feuillage rattaché) dont un bloc tombe dans un effacement ou une construction actuels
   est retiré en entier (plus de demi-arbres au bord du hub ou des allées).
Après gen_hub.py, gen_foot.py, gen_elytra.py, gen_pvpcave.py et le Hall.
"""
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
R = sys.argv[1] if len(sys.argv) > 1 else '.'
F = os.path.join(R, 'data/mg/function')
sys.path.insert(0, os.path.join(HERE, '..', 'lib'))
sys.path.insert(0, HERE)
import mcfn  # noqa: E402
import theme_world as TW  # noqa: E402

TW.load(F)
W = TW.W
_fn = mcfn.Fn(F)
w, patch = _fn.write, _fn.patch

Y1, Y2 = 63, 85
ZONES = [(4, 13, -37, -11),        # anciens portails GTA (9,-19 et 9,-33) et leur passage depuis l'avenue
         (-18, -4, -36, -11),      # anciens portails Terra Nova (-9,-19) et Ombrelune (-9,-29), passages
         (12, 38, 5, 19),          # anciens socles et allées d'élytra (sud)
         (12, 36, -24, -4),        # anciens socles et allées d'élytra (nord), dont le socle des élytres libres (24, -10)
         (-10, 10, -41, -37)]      # ancienne place des plots, hors du hub
RING_C, RING_R = (0, -47), 10.0
RING_GROUND = {'minecraft:purpur_block', 'minecraft:obsidian', 'minecraft:crying_obsidian'}
RING_UP = {'minecraft:purpur_block', 'minecraft:purpur_pillar', 'minecraft:end_rod', 'minecraft:amethyst_block',
           'minecraft:amethyst_cluster', 'minecraft:light', 'minecraft:crying_obsidian', 'minecraft:obsidian'}
STRUCT = ['hub/build', 'elytra/build', 'elytra/spawn_clean', 'foot/build', 'pvpc/build', 'hall/build']
OLD_ENTRY = (-8, -4, -41, -37)    # foot/build y rend le décor du spawn : pas une construction


def cells(line):
    """(cases, bloc, filtre) d'un fill / setblock du lobby (y 63..85), sinon None."""
    m = TW.CMD.match(line.strip())
    if not m:
        return None
    x1, y1, z1 = int(m[2]), int(m[3]), int(m[4])
    x2, y2, z2 = (x1, y1, z1) if m[5] is None else (int(m[5]), int(m[6]), int(m[7]))
    blk, mode = TW.block_and_mode(m[8])
    filt = mode[1] if (m[1] == 'fill' and len(mode) > 1 and mode[0] == 'replace') else None
    ya, yb = max(min(y1, y2), Y1), min(max(y1, y2), Y2)
    if ya > yb:
        return None
    xs, zs = range(min(x1, x2), max(x1, x2) + 1), range(min(z1, z2), max(z1, z2) + 1)
    if len(xs) * len(zs) > 6000 or max(abs(min(xs)), abs(max(xs)), abs(min(zs)), abs(max(zs))) > 80:
        return None
    return [(x, y, z) for x in xs for y in range(ya, yb + 1) for z in zs], blk, filt


PROT, CUT = set(), set()           # cases des constructions actuelles ; cases qu'un arbre ne doit pas toucher
for rel in STRUCT:
    for l in open(os.path.join(F, *rel.split('/')) + '.mcfunction', encoding='utf-8'):
        c = cells(l)
        if not c:
            continue
        cs, blk, filt = c
        if rel == 'foot/build':
            cs = [k for k in cs if not (OLD_ENTRY[0] <= k[0] <= OLD_ENTRY[1] and OLD_ENTRY[2] <= k[2] <= OLD_ENTRY[3])]
        if filt is None:
            PROT.update(cs)
        CUT.update(k for k in cs if k[1] >= 64)


def in_ring(x, z):
    return math.hypot(x - RING_C[0], z - RING_C[1]) <= RING_R


def target(x, y, z):
    b = W.get((x, y, z), 'minecraft:air')
    if in_ring(x, z):
        k = TW.bid(b)
        if y == 63 and k in RING_GROUND:
            return 'minecraft:grass_block'
        if y > 63 and k in RING_UP:
            return 'minecraft:air'
    return b


# ---------------------------------------------------------------- 1. anciens sites rendus (fill par suite de cases identiques le long de z)
L = ['# Décor du spawn remis d\'aplomb (généré par tools/lobby/gen_decofix.py) : anciens sites rendus, arbres coupés retirés en entier']
done = set()
for (x1, x2, z1, z2) in ZONES:
    for x in range(x1, x2 + 1):
        for y in range(Y1, Y2 + 1):
            run = None
            for z in list(range(z1, z2 + 1)) + [None]:
                b = None if z is None or (x, y, z) in PROT or (x, y, z) in done else target(x, y, z)
                if z is not None and b is not None:
                    done.add((x, y, z))
                if run and (b != run[1] or z is None):
                    za, zb = run[0], run[2]
                    L.append(f'setblock {x} {y} {za} {run[1]}' if za == zb else f'fill {x} {y} {za} {x} {y} {zb} {run[1]}')
                    run = None
                if b is not None:
                    run = [z, b, z] if run is None else [run[0], b, z]
n_restore = len(L) - 1

# ---------------------------------------------------------------- 2. arbres coupés retirés en entier
LOG = ('_log', '_wood', 'mushroom_stem')
LEAF = ('_leaves', 'mushroom_block')
logs = {k for k, b in W.items() if k[1] >= 64 and TW.bid(b).endswith(LOG)}
trunk_of, trunks = {}, []
for k in logs:                                       # troncs = composantes connexes de bûches (26 voisins)
    if k in trunk_of:
        continue
    comp, todo = [], [k]
    trunk_of[k] = len(trunks)
    while todo:
        c = todo.pop()
        comp.append(c)
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    n = (c[0] + dx, c[1] + dy, c[2] + dz)
                    if n in logs and n not in trunk_of:
                        trunk_of[n] = len(trunks)
                        todo.append(n)
    trunks.append(comp)
cols = {}
for i, comp in enumerate(trunks):
    for (x, y, z) in comp:
        cols.setdefault((x, z), []).append(i)
tree_blocks = [list(c) for c in trunks]
for k, b in W.items():                              # feuillage rattaché au tronc le plus proche (5 blocs au plus) ; haies (sans tronc) ignorées
    if k[1] < 64 or not TW.bid(b).endswith(LEAF) or (k[1] == 64 and 'azalea' in b):     # haies d'azalée (y 64) : pas des arbres
        continue
    best = None
    for dx in range(-5, 6):
        for dz in range(-5, 6):
            for i in cols.get((k[0] + dx, k[2] + dz), ()):
                d = max(abs(dx), abs(dz))
                if best is None or d < best[0]:
                    best = (d, i)
    if best:
        tree_blocks[best[1]].append(k)
removed = 0
for blocks in tree_blocks:
    if any(k in CUT for k in blocks):
        removed += 1
        if os.environ.get('DECOFIX_DEBUG'):
            xs, zs = [k[0] for k in blocks], [k[2] for k in blocks]
            print('arbre retiré', (min(xs), max(xs)), (min(zs), max(zs)), TW.bid(W[blocks[0]]), 'coupé en', next(k for k in blocks if k in CUT))
        L += [f'setblock {x} {y} {z} minecraft:air' for (x, y, z) in sorted(blocks) if (x, y, z) not in PROT]

L += ['# ancien socle « élytres libres » (24, -10) : ses panneaux et son élytre flottante (gen_elytra.py ne le construit plus)',
      'execute positioned 24.5 66 -9.5 run kill @e[tag=mg.elyd,distance=..4]']
L += ['execute unless score $ftoff mg.st matches 1 run function mg:foot/labels',
      'data modify storage mg:lobby decofix4 set value 1b']
w('hub/decofix', L)
w('hub/decofix_start', ['# Charge la zone du décor à remettre d\'aplomb, puis hub/decofix (2 s plus tard)',
                        'forceload add -20 -61 40 20', 'schedule function mg:hub/decofix_go 2s'])
w('hub/decofix_go', ['function mg:hub/decofix', 'forceload remove -20 -61 40 20', 'function mg:core/forceloads'])
patch('core/load', 'execute if score $setup mg.st matches 1 unless data storage mg:lobby elyclean6 run schedule function mg:elytra/spawn_clean 9s',
      ['execute if score $setup mg.st matches 1 unless data storage mg:lobby decofix4 run schedule function mg:hub/decofix_start 30s'])
patch('desinstaller', 'data remove storage mg:hub floaty',
      ['data remove storage mg:lobby decofix4', 'schedule clear mg:hub/decofix_start', 'schedule clear mg:hub/decofix_go'])
print(f'decofix OK : {n_restore} lignes de décor rendu, {removed} arbres coupés retirés ({len(trunks)} arbres au spawn), {len(L)} lignes')
