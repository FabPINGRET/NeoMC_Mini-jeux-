"""Retire l'ancien portail des plots des fonctions de construction du spawn (lobby/build_*.mcfunction) : python3 tools/lobby/strip_plot_portal.py .

Le spawn (gen_lobby.py, données figées) construisait encore la place des plots (anneau de purpur/obsidienne, arche, cristaux)
avant que hub/build et hub/decofix ne la remplacent. Ce script réécrit les lignes concernées, une fois pour toutes (idempotent) :
- dans l'anneau de la place (même règle que hub/decofix) : sol purpur/obsidienne -> herbe ; arche, piliers, cristaux, end_rods,
  lumières -> rien. Le reste (arbres, haies) est gardé : hub/build vide sa boîte et hub/decofix retire les arbres qu'il coupe.
Les lignes d'air (build_1) et les autres blocs ne bougent pas.
"""
import glob
import math
import os
import sys

R = sys.argv[1] if len(sys.argv) > 1 else '.'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import theme_world as TW  # noqa: E402

RING_C, RING_R = (0, -47), 10.0                   # = gen_decofix
RING_GROUND = {'minecraft:purpur_block', 'minecraft:obsidian', 'minecraft:crying_obsidian'}
RING_UP = {'minecraft:purpur_block', 'minecraft:purpur_pillar', 'minecraft:end_rod', 'minecraft:amethyst_block',
           'minecraft:amethyst_cluster', 'minecraft:light', 'minecraft:crying_obsidian', 'minecraft:obsidian'}


def new_block(x, y, z, blk):
    """Bloc à poser à la place de blk (None = ne rien poser)."""
    k = TW.bid(blk)
    if k == 'minecraft:air':
        return blk
    if math.hypot(x - RING_C[0], z - RING_C[1]) <= RING_R:
        if y == 63 and k in RING_GROUND:
            return 'minecraft:grass_block'
        if y > 63 and k in RING_UP:
            return None
    return blk


def rewrite(line):
    m = TW.CMD.match(line.strip())
    if not m:
        return [line]
    x1, y1, z1 = int(m[2]), int(m[3]), int(m[4])
    x2, y2, z2 = (x1, y1, z1) if m[5] is None else (int(m[5]), int(m[6]), int(m[7]))
    xa, xb, ya, yb, za, zb = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2), min(z1, z2), max(z1, z2)
    if xb < -11 or xa > 11 or zb < -61 or za > -36 or yb < 63:
        return [line]
    blk, mode = TW.block_and_mode(m[8])
    if TW.bid(blk) == 'minecraft:air' or (xb - xa + 1) * (yb - ya + 1) * (zb - za + 1) > 4000:
        return [line]
    tail = (' ' + ' '.join(mode)) if mode else ''
    out, same = [], True
    for x in range(xa, xb + 1):
        for y in range(ya, yb + 1):
            run = None
            for z in list(range(za, zb + 1)) + [None]:
                b = None if z is None else new_block(x, y, z, blk)
                if z is not None and b != blk:
                    same = False
                if run and (z is None or b != run[1]):
                    if run[1] is not None:
                        out.append(f'setblock {x} {y} {run[0]} {run[1]}{tail}' if run[0] == run[2]
                                   else f'fill {x} {y} {run[0]} {x} {y} {run[2]} {run[1]}{tail}')
                    run = None
                if z is not None:
                    run = [z, b, z] if run is None else [run[0], b, z]
    return [line] if same else out


n = 0
for f in sorted(glob.glob(os.path.join(R, 'data/mg/function/lobby/build_*.mcfunction'))):
    src = open(f, encoding='utf-8').read().split('\n')
    dst = [o for l in src for o in rewrite(l)]
    if dst != src:
        n += 1
        open(f, 'w', encoding='utf-8', newline='\n').write('\n'.join(dst))
print(f'strip_plot_portal : {n} fichier(s) réécrit(s)')
