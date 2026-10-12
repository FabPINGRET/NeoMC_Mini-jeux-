"""🎃🎄 Décors saisonniers des cartes de jeu, réversibles : python tools/lobby/gen_theme_maps.py .   (après les générateurs de cartes)

Quand un décor saisonnier est en place ($theme, voir gen_themes.py), chaque carte où se trouve un joueur au « GO ! »
(core/begin) est habillée, puis rétablie au retour au lobby (core/return_lobby, avant tout nettoyage de jeu).
Seulement de l'habillage sans effet sur le jeu : feuillages, lanternes et torches, herbes et fleurs, mousse sous les
feuilles, neige fine sur les cimes — jamais de sol, d'eau, de bloc gênant (citrouille, toile) ni de zone modifiée en jeu.

Le générateur rejoue les fonctions de construction des cartes (*build*) en ne retenant que les blocs décoratifs, puis
vérifie au besoin le bloc voisin (air sous la mousse, sur la neige) ; « on » ne pose un bloc que si l'original est encore
là, « off » ne remet l'original que si le bloc du thème est encore là. Une carte = un groupe de blocs voisins d'un même
dossier de jeu (cellules de 64 blocs) : le déclencheur est un joueur mg.play dans sa boîte.
"""
import glob
import os
import random
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'arcade'))
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w = C.w
F = C.F
SKIP = {'lobby', 'parkour', 'plot', 'lobkart', 'gta', 'survie', 'bb'}   # spawn (gen_themes.py), autre dimension, parcelles
SPAWN = 84                                                             # carré du spawn (|x|, |z| <= SPAWN) : jamais touché
CMD = re.compile(r'^(setblock|fill) (-?\d+) (-?\d+) (-?\d+)(?: (-?\d+) (-?\d+) (-?\d+))? (.+)$')
OVER = 'execute in minecraft:overworld run '
IN = 'execute in minecraft:overworld '
FLOWERS = {'minecraft:dandelion', 'minecraft:poppy', 'minecraft:blue_orchid', 'minecraft:allium', 'minecraft:azure_bluet',
           'minecraft:red_tulip', 'minecraft:orange_tulip', 'minecraft:white_tulip', 'minecraft:pink_tulip',
           'minecraft:oxeye_daisy', 'minecraft:cornflower', 'minecraft:lily_of_the_valley'}
DECO = FLOWERS | {'minecraft:lantern', 'minecraft:torch', 'minecraft:wall_torch', 'minecraft:short_grass', 'minecraft:fern',
                  'minecraft:pink_petals'}


def bid(b):
    return (b or 'minecraft:air').split('[')[0].split('{')[0]


def states(b):
    m = re.search(r'\[([^\]]*)\]', b or '')
    return dict(kv.split('=') for kv in m[1].split(',')) if m and m[1] else {}


def apples(f, i):
    """Feuillage qui donne des pommes dans un jeu de survie (UHC, Hunger Games) : on n'y touche pas."""
    return f.startswith(('uhc', 'hg')) and i in ('minecraft:oak_leaves', 'minecraft:dark_oak_leaves')


def deco(b):
    i = bid(b)
    return i in DECO or i.endswith('_leaves')


def parse(line):
    """(x1, x2, y1, y2, z1, z2, bloc, mode) d'un setblock/fill en coordonnées absolues, sinon None."""
    line = line.strip()
    if line.startswith(OVER):
        line = line[len(OVER):]
    m = CMD.match(line)
    if not m:
        return None
    x1, y1, z1 = int(m[2]), int(m[3]), int(m[4])
    x2, y2, z2 = (x1, y1, z1) if m[5] is None else (int(m[5]), int(m[6]), int(m[7]))
    rest, depth = m[8], 0
    for i, ch in enumerate(rest):
        depth += ch in '[{'
        depth -= ch in ']}'
        if ch == ' ' and depth == 0:
            rest, mode = rest[:i], rest[i + 1:].split(' ')[0]
            break
    else:
        mode = ''
    return min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2), min(z1, z2), max(z1, z2), rest, mode


def num(p):
    m = re.search(r'build_?(\d+)', os.path.basename(p))
    return int(m[1]) if m else -1


# ------------------------------------------------------------------ fichiers de construction (base) et le reste (zones dynamiques)
BASE, OTHER = [], []
for p in sorted(glob.glob(os.path.join(F, '**', '*.mcfunction'), recursive=True)):
    folder = os.path.relpath(p, F).split(os.sep)[0]
    if folder in SKIP or folder == 'desinstaller.mcfunction':
        continue
    (BASE if 'build' in os.path.basename(p) else OTHER).append((folder, p))
BASE.sort(key=lambda t: (t[0], os.path.dirname(t[1]), num(t[1]), t[1]))

DYN = {}                                 # chunk -> boîtes posées hors construction (jeu, remise à zéro) : on n'y touche pas
for _, p in OTHER:
    for l in open(p, encoding='utf-8'):
        c = parse(l) if l.startswith(('setblock ', 'fill ', OVER)) else None
        if c:
            for cx in range(c[0] >> 4, (c[1] >> 4) + 1):
                for cz in range(c[4] >> 4, (c[5] >> 4) + 1):
                    DYN.setdefault((cx, cz), []).append(c[:6])


def dyn(x, y, z):
    return any(a <= x <= b and c <= y <= d and e <= z <= f for a, b, c, d, e, f in DYN.get((x >> 4, z >> 4), ()))


def replay(watch):
    """Rejoue toutes les constructions. watch=None : suit les blocs décoratifs (dossier, bloc) ; sinon l'état final
    (bloc ou None pour l'air) des positions de watch."""
    track = watch is None
    W, IDX = {}, {}                      # position -> valeur ; chunk -> positions connues
    if not track:
        for k in watch:
            IDX.setdefault((k[0] >> 4, k[2] >> 4), set()).add(k)
            W[k] = None
    for folder, p in BASE:
        for l in open(p, encoding='utf-8'):
            c = parse(l)
            if not c:
                continue
            xa, xb, ya, yb, za, zb, blk, mode = c
            if xb >= -SPAWN and xa <= SPAWN and zb >= -SPAWN and za <= SPAWN and track:
                continue
            simple = mode in ('', 'destroy')
            if track and simple and deco(blk) and (xb - xa + 1) * (yb - ya + 1) * (zb - za + 1) <= 200000:
                for x in range(xa, xb + 1):
                    for z in range(za, zb + 1):
                        for y in range(ya, yb + 1):
                            W[(x, y, z)] = (folder, blk)
                            IDX.setdefault((x >> 4, z >> 4), set()).add((x, y, z))
                continue
            air = blk in ('minecraft:air', 'air')
            for cx in range(xa >> 4, (xb >> 4) + 1):
                for cz in range(za >> 4, (zb >> 4) + 1):
                    for k in list(IDX.get((cx, cz), ())):
                        if not (xa <= k[0] <= xb and ya <= k[1] <= yb and za <= k[2] <= zb):
                            continue
                        if track:                      # écrasé (ou incertain : keep, replace, hollow) : oublié
                            IDX[(cx, cz)].discard(k)
                            W.pop(k, None)
                        elif mode == 'keep':
                            W[k] = W[k] if W[k] is not None or air else blk
                        elif simple:
                            W[k] = None if air else blk
                        else:
                            W[k] = W[k] or 'minecraft:stone'   # incertain : considéré comme occupé
    return W


W = {k: v for k, v in replay(None).items() if not (abs(k[0]) <= SPAWN and abs(k[2]) <= SPAWN) and not dyn(*k)}
# voisins à vérifier : au-dessus et au-dessous des feuillages et des plantes
NB = replay({(x, y + d, z) for (x, y, z) in W for d in (-1, 1)} - set(W))


def empty(k):
    return k not in W and NB.get(k) is None


# ------------------------------------------------------------------ thèmes
def halloween(rnd, ch):
    for k, (f, b) in sorted(W.items()):
        i = bid(b)
        if i.endswith('_leaves') and not apples(f, i):
            if i in ('minecraft:cherry_leaves', 'minecraft:azalea_leaves', 'minecraft:flowering_azalea_leaves') or rnd.random() < 0.55:
                ch[k] = (f, b, 'minecraft:pale_oak_leaves[persistent=true]')
                below = (k[0], k[1] - 1, k[2])
                if empty(below) and not dyn(*below) and rnd.random() < 0.3:
                    ch[below] = (f, 'minecraft:air', 'minecraft:pale_hanging_moss[tip=true]')
        elif i in ('minecraft:lantern', 'minecraft:wall_torch'):
            ch[k] = (f, b, 'minecraft:soul_' + b[len('minecraft:'):])
        elif i == 'minecraft:torch':
            ch[k] = (f, b, 'minecraft:soul_torch')
        elif i == 'minecraft:pink_petals':
            s = states(b)
            ch[k] = (f, b, f'minecraft:leaf_litter[segment_amount={s.get("flower_amount", "4")},facing={s.get("facing", "north")}]')
        elif (i == 'minecraft:short_grass' and rnd.random() < 0.4) or (i in FLOWERS and rnd.random() < 0.45):
            ch[k] = (f, b, 'minecraft:short_dry_grass')


def noel(rnd, ch):
    lights = ['minecraft:pearlescent_froglight', 'minecraft:ochre_froglight', 'minecraft:verdant_froglight',
              'minecraft:sea_lantern', 'minecraft:redstone_lamp[lit=true]']
    for k, (f, b) in sorted(W.items()):
        i = bid(b)
        x, y, z = k
        if i.endswith('_leaves'):
            if not apples(f, i) and rnd.random() < 0.06:
                ch[k] = (f, b, rnd.choice(lights))
            elif empty((x, y + 1, z)) and not dyn(x, y + 1, z) and rnd.random() < 0.6:
                ch[(x, y + 1, z)] = (f, 'minecraft:air', 'minecraft:snow[layers=1]')
        elif (i in FLOWERS or i == 'minecraft:pink_petals' or (i in ('minecraft:short_grass', 'minecraft:fern') and rnd.random() < 0.7)) \
                and not empty((x, y - 1, z)):
            ch[k] = (f, b, 'minecraft:snow[layers=1]')


THEMES = [(1, 'halloween', halloween, 20261031), (2, 'noel', noel, 20261225)]

# ------------------------------------------------------------------ cartes : groupes de cellules de 64 blocs voisines, par dossier
CELLS = {}
for (x, y, z), (f, _) in W.items():
    CELLS.setdefault(f, set()).add((x >> 6, z >> 6))
REGIONS = []                             # (dossier, cellules)
for f in sorted(CELLS):
    left = set(CELLS[f])
    while left:
        stack, comp = [min(left)], set()
        left.discard(stack[0])
        while stack:
            cx, cz = stack.pop()
            comp.add((cx, cz))
            for dx in (-1, 0, 1):
                for dz in (-1, 0, 1):
                    n = (cx + dx, cz + dz)
                    if n in left:
                        left.discard(n)
                        stack.append(n)
        REGIONS.append((f, comp))
RID = {}
for i, (f, comp) in enumerate(REGIONS):
    for c in comp:
        RID[(f, c)] = i

BY = {}                                  # (thème, carte) -> [(position, original, thème)]
for tid, key, make, seed in THEMES:
    ch = {}
    make(random.Random(seed), ch)
    for k, (ff, o, n) in ch.items():
        BY.setdefault((key, RID.get((ff, (k[0] >> 6, k[2] >> 6)))), []).append((k, o, n))

begin, end, stats = [], [], []
for i, (f, comp) in enumerate(REGIONS):
    name = f'{f}_{i}'
    T = f'lobby/theme/map/{name}'
    per = {key: sorted(BY.get((key, i), [])) for _, key, _, _ in THEMES}
    if not any(per.values()):
        continue
    pts = [k for v in per.values() for k, _, _ in v]
    xa, xb = min(p[0] for p in pts) - 8, max(p[0] for p in pts) + 8
    za, zb = min(p[2] for p in pts) - 8, max(p[2] for p in pts) + 8
    sel = f'@a[tag=mg.play,x={xa},y=-64,z={za},dx={xb - xa},dy=384,dz={zb - za},limit=1]'
    for tid, key, _, _ in THEMES:
        lines = per[key]
        w(f'{T}/{key}_on', [f'# {key} : habille la carte {f} (généré par tools/lobby/gen_theme_maps.py ; inverse : {key}_off)',
                            f'scoreboard players set $tm{i} mg.st {tid}'] +
          [f'execute if block {x} {y} {z} {bid(o)} run setblock {x} {y} {z} {n}' for (x, y, z), o, n in lines])
        w(f'{T}/{key}_off', [f'# {key} : carte {f} rétablie (bloc d\'origine remis si le bloc du thème est encore là)'] +
          [f'execute if block {x} {y} {z} {bid(n)} run setblock {x} {y} {z} {o}' for (x, y, z), o, n in lines])
        begin.append(f'execute if score $theme mg.st matches {tid} unless score $tm{i} mg.st matches 1.. '
                     f'if entity {sel} run function mg:{T}/{key}_on')
        end.append(f'execute if score $tm{i} mg.st matches {tid} run function mg:{T}/{key}_off')
    end.append(f'scoreboard players reset $tm{i} mg.st')
    stats.append(f'{name} : ' + ', '.join(f'{k} {len(v)}' for k, v in per.items()))

w('lobby/theme/map/begin', ['# GO ! (core/begin) avec un décor saisonnier en place : habille les cartes où sont les joueurs',
                            'scoreboard players set $tmap mg.st 1'] + [IN + l[len('execute '):] for l in begin])
w('lobby/theme/map/end', ['# Retour au lobby (core/return_lobby, avant les nettoyages) : chaque carte habillée est rétablie',
                          'scoreboard players set $tmap mg.st 0'] + [IN + l[len('execute '):] if l.startswith('execute ') else l for l in end])

# ------------------------------------------------------------------ branchements
C.patch('core/begin', 'function mg:sb/start', ['execute if score $theme mg.st matches 1.. run function mg:lobby/theme/map/begin'])
C.patch('core/return_lobby', '# Retour au lobby de tous les participants + nettoyage du monde',
        ['execute if score $tmap mg.st matches 1 run function mg:lobby/theme/map/end'])
C.patch('desinstaller', '# Désinstallation (OP) — retire scoreboards, équipes, décor et zones chargées',
        ['execute if score $tmap mg.st matches 1 run function mg:lobby/theme/map/end'])
print(f'Cartes saisonnières : {len(stats)} cartes, {len(W)} blocs décoratifs suivis')
for s in stats:
    print('  ' + s)
