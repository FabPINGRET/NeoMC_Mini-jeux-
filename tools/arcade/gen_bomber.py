"""💣 Bombardier (id 99) : une grande ville façon Manhattan vue du ciel, on largue des bombes, le plus de dégâts gagne.

    python tools/arcade/gen_bomber.py .

- La ville (177 × 177, centre 0 64 32400) : avenues nord-sud, rues est-ouest, gratte-ciel de verre, immeubles de brique
  avec châteaux d'eau, tours art déco à gradins, deux géants (Empire et Chrysler), un carrefour à écrans, Central Park
  avec son lac, l'East River avec un pont suspendu et une statue verte sur son île. Taxis jaunes, réverbères.
- Les joueurs attendent sur un plancher invisible (barrières) à y 170 pendant le compte à rebours ; au GO il disparaît
  et ils VOLENT dans la ville en élytres (fusées illimitées ; posé au sol, accroupi = catapulte vers le ciel) et lâchent
  les bombes devant eux, dans la direction du regard : bombe (rayon 8), méga-bombe (16), bombe à fragmentation
  (7 sous-munitions de rayon 5) et des bombes atomiques (rayon 28) : une par joueur à 20 s, 50 s et 1 min 20.
- Dégâts = blocs détruits (bloc doré ou statue : 10 points). Une explosion = fills « replace #mg:bomb_city »
  empilés en sphère (le nombre de blocs remplacés est le score), sans vraie explosion ni objets au sol.
- 2 min, le plus gros score gagne. Barre de boss : part de la ville détruite. Reconstruite à chaque partie
  (en 80 étapes pendant le compte à rebours), sol et plancher posés une fois (storage mg:bomber v1).
"""
import math
import os
import random
import sys
import json
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
GID = 99
Z = 32400
HX = 88                      # demi-côté de la ville
Y0, YT = 56, 170             # bas du sol, plancher de barrières
GY = 64                      # surface (routes, trottoirs) ; bâtiments à partir de 65
LIMIT = 2400                 # 2 min
NUKE_AT = (400, 1000, 1600)  # bombes atomiques : à 20 s, 50 s et 1 min 20 (une par joueur, case 4)
random.seed(1999)

# ---------------------------------------------------------------- grille de blocs (comptage) + commandes
NX, NY, NZ = 2 * HX + 1, YT - Y0 + 1, 2 * HX + 1
PAL = ['air']
PIDX = {'air': 0}
CITY = set()                 # palette des blocs « destructibles » (posés par la ville, pas par le sol)
GSET = set()                 # blocs du sol : ne doivent jamais être destructibles
grid = bytearray(NX * NY * NZ)


def pid(b, city):
    n = b.split('[')[0].replace('minecraft:', '')
    if n not in PIDX:
        PIDX[n] = len(PAL)
        PAL.append(n)
        assert len(PAL) < 256
    if n != 'air':
        (CITY if city else GSET).add(n)
    return PIDX[n]


def mark(x1, y1, z1, x2, y2, z2, b, city, hollow=False):
    v = pid(b, city)
    for y in range(y1, y2 + 1):
        for z in range(z1, z2 + 1):
            base = ((y - Y0) * NZ + (z + HX)) * NX + HX
            if hollow and y1 < y < y2 and z1 < z < z2:
                grid[base + x1:base + x1 + 1] = bytes([v])
                grid[base + x2:base + x2 + 1] = bytes([v])
                grid[base + x1 + 1:base + x2] = bytes(x2 - x1 - 1)
            else:
                grid[base + x1:base + x2 + 1] = bytes([v]) * (x2 - x1 + 1)


CMDS = []                    # commandes de la ville (reconstruites à chaque partie)
GROUND = []                  # sol, fleuve, plancher (une fois)


def fill(x1, y1, z1, x2, y2, z2, b, city=True, out=None):
    x1, x2 = sorted((x1, x2)); y1, y2 = sorted((y1, y2)); z1, z2 = sorted((z1, z2))
    x1, z1, x2, z2 = max(x1, -HX), max(z1, -HX), min(x2, HX), min(z2, HX)
    if x1 > x2 or z1 > z2:
        return
    out = CMDS if out is None else out
    area = (x2 - x1 + 1) * (z2 - z1 + 1)
    step = max(1, 32768 // area)
    for ya in range(y1, y2 + 1, step):
        yb = min(y2, ya + step - 1)
        out.append(f'fill {x1} {ya} {Z + z1} {x2} {yb} {Z + z2} minecraft:{b}' if (x1, ya, z1) != (x2, yb, z2)
                   else f'setblock {x1} {ya} {Z + z1} minecraft:{b}')
    if Y0 <= y1 and y2 <= YT:
        mark(x1, y1, z1, x2, y2, z2, b if b != 'barrier' else 'air', city)


def put(x, y, z, b, city=True):
    fill(x, y, z, x, y, z, b, city)


# ---------------------------------------------------------------- plan
AV = [-76, -44, -12, 20, 52]                     # avenues (nord-sud), largeur 7
ST = [-78, -54, -30, -6, 18, 42, 66]             # rues (est-ouest), largeur 5
LAND = 64                                        # x > 64 : East River
PARK = (-40, 21, 16, 63)                         # Central Park (x1, z1, x2, z2)
BRIDGE_Z = -30


def spans(centers, half, lo, hi):
    s, prev = [], lo
    for c in centers:
        if c - half - 1 >= prev:
            s.append((prev, c - half - 1))
        prev = c + half + 1
    if prev <= hi:
        s.append((prev, hi))
    return s


LOTX = spans(AV, 3, -HX, LAND)
LOTZ = spans(ST, 2, -HX, HX)


def in_park(x, z):
    return PARK[0] <= x <= PARK[2] and PARK[1] <= z <= PARK[3]


# ---------------------------------------------------------------- sol (une fois)
G = GROUND
for y in range(Y0, YT + 7):
    fill(-HX, y, -HX, HX, y, HX, 'air', False, G)
fill(-HX, Y0, -HX, HX, 60, HX, 'stone', False, G)
fill(-HX, 61, -HX, HX, 63, HX, 'dirt', False, G)
fill(-HX, GY, -HX, LAND, GY, HX, 'smooth_stone', False, G)                   # trottoirs partout, puis chaussées
for c in AV:
    fill(c - 3, GY, -HX, c + 3, GY, HX, 'polished_blackstone', False, G)
    for z in range(-HX, HX + 1, 6):
        fill(c, GY, z, c, GY, z + 2, 'white_concrete_powder', False, G)
for c in ST:
    fill(-HX, GY, c - 2, LAND, GY, c + 2, 'polished_blackstone', False, G)
    for x in range(-HX, LAND + 1, 6):
        fill(x, GY, c, x + 2, GY, c, 'white_concrete_powder', False, G)
for c in AV:                                                                  # passages piétons
    for s in ST:
        for k in range(-2, 3, 2):
            fill(c - 3, GY, s + k, c + 3, GY, s + k, 'white_concrete_powder', False, G)
# East River : quai en pierre taillée, eau, île de la statue
fill(LAND + 1, 57, -HX, HX, 57, HX, 'sand', False, G)
fill(LAND + 1, 58, -HX, HX, 63, HX, 'water', False, G)
fill(LAND + 1, GY, -HX, HX, GY, HX, 'air', False, G)
fill(LAND, 58, -HX, LAND, GY - 1, HX, 'stone', False, G)
G += [f'fill {HX + 1} 57 {Z - HX - 1} {HX + 1} {GY} {Z + HX + 1} minecraft:stone',          # le fleuve ne coule pas hors de la carte
      f'fill {LAND} 57 {Z - HX - 1} {HX} {GY} {Z - HX - 1} minecraft:stone', f'fill {LAND} 57 {Z + HX + 1} {HX} {GY} {Z + HX + 1} minecraft:stone']
for x in range(LAND + 1, HX + 1):
    for z in range(-HX, -58):
        d = math.hypot(x - 78, z + 72)
        if d <= 7.5:
            fill(x, 58, z, x, 63, z, 'sand', False, G)
            put(x, GY, z, 'grass_block' if d <= 6 else 'sand', False)
            G.append(CMDS.pop())
# Central Park : pelouse, allées, lac
px1, pz1, px2, pz2 = PARK
fill(px1, GY, pz1, px2, GY, pz2, 'grass_block', False, G)
fill(px1, 63, pz1, px2, 63, pz2, 'dirt', False, G)
fill(-14, GY, pz1, -10, GY, pz2, 'dirt_path', False, G)
fill(px1, GY, 40, px2, GY, 43, 'dirt_path', False, G)
for z in range(pz1, pz2 + 1):
    for x in range(px1, px2 + 1):
        if math.hypot((x + 26) / 9, (z - 52) / 6) <= 1:
            fill(x, 61, z, x, GY, z, 'water', False, G)
# murs invisibles au-dessus de la ville (le plancher de départ est posé par prepare et retiré au GO)
for (a, b, c, d) in [(-HX, -HX, HX, -HX), (-HX, HX, HX, HX), (-HX, -HX, -HX, HX), (HX, -HX, HX, HX)]:
    fill(a, YT + 1, b, c, YT + 6, d, 'barrier', False, G)

# Les 4 parts partagent les globals de ce fichier ; chacune est une tranche contiguë de l'ancien script, exécutée à sa place :
# bomber_city.py (skyline), bomber_park.py (parc, rues, pont, comptage), bomber_export.py (neo_city.json, carte, étapes, boom),
# bomber_game.py (bombes, item).
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bomber_city.py'), encoding='utf-8').read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bomber_park.py'), encoding='utf-8').read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bomber_export.py'), encoding='utf-8').read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'bomber_game.py'), encoding='utf-8').read())

C.register([GID], 'bomber', [C.announce(GID, '', '💣 BOMBARDIER', 'red', 'largue des bombes sur la ville, le plus de dégâts gagne !')])
C.objectives([('mg.bmb', 'dummy {"text":"💣 Dégâts","color":"red","bold":true}'), ('mg.bid', 'dummy'), ('mg.bty', 'dummy'),
              ('mg.bc1', 'dummy'), ('mg.bc2', 'dummy'), ('mg.bc3', 'dummy'), ('mg.bc4', 'dummy')])
C.forceload([f'# Bombardier (z {Z})', f'forceload add -{HX} {Z - HX} {HX} {Z + HX}'])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw', ['bossbar remove mg:bomber', 'schedule clear mg:bomber/build_step',
                                                              'data remove storage mg:bomber v1'])
print(f'Bombardier OK : {len(CMDS)} commandes en {NPART} étapes, sol {len(GROUND)} en {NG}, {TOTAL} blocs destructibles ({TB} bonus), '
      f'{len(CITY)} matériaux')
