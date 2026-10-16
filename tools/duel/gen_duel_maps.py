"""Duel sniper : les 3 arènes 41 x 141 (une par instance de duel) et leur construction.

    python tools/duel/gen_duel_maps.py .        (depuis la racine du dépôt ; idempotent ; puis gen_duel.py)

  1 « Canyon »  (centre 0 ~ 40000) : deux plateaux face à face (y 88), canyon (fond y 72), pont central à portique,
                                      rampes décalées de chaque côté, buttes à escalier, rochers.
  2 « Ville »   (centre 0 ~ 40400) : ruines à façades percées de fenêtres, rues décalées d'une rangée à l'autre,
                                      étages par échelle intérieure, clocher central.
  3 « Glacier » (centre 0 ~ 40800) : congères, séracs de glace, lac gelé central, tours de guet en bois.

Principes : chaque poste de tir offre une ligne de vue, un accès (rampe, escalier, échelle) et se laisse contrer
(jamais imprenable) ; au moins deux routes entre les départs ; les deux départs (zl -66 et +66) ne se voient pas
(écran de rochers / bâtiment / séracs sur l'axe) ; la carte est symétrique par rotation de 180 degrés (duel_geom.py).
Construction : build_all (forceload + lots build_<carte>_<n> étalés par schedule, drapeau mg:duel built à la fin).
Zones z 40000 / 40400 / 40800 libres (vérifié : Zombies 39772..40236, Bomberman 40689..40711, Labyrinthe 41049+).
"""
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'arcade'))
import common as C
from duel_geom import Arena, HX, HZ

CHUNK = 60        # commandes par lot build_<carte>_<n>
STEP = 4          # ticks entre deux lots
FIRST = 60        # ticks avant le premier lot (le temps que les chunks se chargent)


def rock(a, x, z, y, w, d, h, mat='andesite'):
    """Rocher w x d x h (posé en y), dessus moussu ; sym = avec son double tourné."""
    a.sfill(x, y, z, x + w - 1, y + h - 1, z + d - 1, mat)
    a.sfill(x, y + h - 1, z, x + w - 1, y + h - 1, z + d - 1, 'mossy_cobblestone')


# ---------------------------------------------------------------------------------------------- Canyon
BANDS = [(72, 80, 'red_sandstone'), (81, 83, 'terracotta'), (84, 85, 'orange_terracotta'),
         (86, 87, 'terracotta'), (88, 88, 'coarse_dirt')]


def canyon(a):
    a.note('Canyon : plateaux y 88 (zl -70..-34 et miroir), fond y 72, falaises x +-17..20, pont y 88')
    a.fill(-HX, 62, -HZ, HX, 71, HZ, 'red_sandstone')
    a.fill(-HX, 72, -33, HX, 72, 33, 'coarse_dirt')
    for y1, y2, b in BANDS:
        a.sfill(-HX, y1, -HZ, HX, y2, -34, b)          # plateau
        a.sfill(-HX, y1, -33, -17, y2, 33, b)          # falaises latérales
    a.note('lit de gravier, buttes (sommet y 82) et leur escalier')
    for (x1, z1, x2, z2) in [(-12, -26, -5, -18), (3, -12, 10, -6), (-8, 14, 0, 22)]:
        a.sfill(x1, 72, z1, x2, 72, z2, 'gravel')
    a.sfill(-12, 73, 0, -8, 81, 5, 'terracotta')
    a.sfill(-12, 82, 0, -8, 82, 5, 'orange_terracotta')
    a.stairs(-12, -10, 15, -1, 73, 10, 'red_sandstone_stairs', 'red_sandstone', 72)
    a.note('rampes décalées : le départ nord descend côté ouest, le départ sud côté est')
    a.stairs(-16, -11, -18, -1, 73, 16, 'red_sandstone_stairs', 'red_sandstone', 72)
    a.note('pont central y 88 : deux piles, garde-corps, sacs de couverture, portique au centre')
    a.fill(-3, 87, -33, 3, 88, 33, 'stone_bricks')
    a.sfill(-3, 73, -22, 3, 86, -20, 'stone_bricks')
    a.sfill(-3, 89, -32, -3, 89, -7, 'stone_brick_wall')
    a.sfill(3, 89, -32, 3, 89, -7, 'stone_brick_wall')
    a.sfill(-2, 89, -26, -1, 90, -25, 'hay_block')
    a.sfill(1, 89, -14, 2, 90, -13, 'hay_block')
    a.fill(-3, 89, -2, -3, 93, 2, 'stone_bricks')
    a.fill(3, 89, -2, 3, 93, 2, 'stone_bricks')
    a.fill(-3, 94, -2, 3, 94, 2, 'stone_bricks')
    a.note('plateaux : écran de rochers devant le départ, couverts et postes en bord de falaise')
    rock(a, -8, -60, 89, 16, 3, 4)
    for (x, z, w, d, h) in [(-14, -48, 4, 3, 2), (9, -44, 4, 2, 3), (-4, -41, 6, 2, 2),
                            (-12, -37, 5, 2, 2), (7, -37, 5, 2, 2), (-17, -56, 3, 4, 3)]:
        rock(a, x, z, 89, w, d, h)
    a.note('fond du canyon : rochers de couverture')
    for (x, z, w, d, h) in [(-8, -31, 3, 3, 3), (4, -27, 4, 3, 3), (-3, -18, 3, 3, 2),
                            (-14, -12, 3, 3, 3), (2, -9, 3, 3, 3)]:
        rock(a, x, z, 73, w, d, h)
    a.sfill(-2, 88, -67, 2, 88, -65, 'polished_andesite')


# ---------------------------------------------------------------------------------------------- Ville
def ruin(a, rng, x1, z1, x2, z2, h, doors='ns', s=True):
    """Bâtiment en ruine : coque, étages (planchers y 85 / 89), échelle contre le mur ouest, fenêtres, brèches."""
    f = a.sfill if s else a.fill
    pu = a.sput if s else a.put
    top = 80 + h
    floors = [y for y in (85, 89) if y < top - 2]
    f(x1, 81, z1, x2, top, z2, 'stone_bricks')
    f(x1 + 1, 81, z1 + 1, x2 - 1, top, z2 - 1, 'air')
    for y in floors:
        f(x1 + 1, y, z1 + 1, x2 - 1, y, z2 - 1, 'dark_oak_planks')
    if floors:
        f(x1 + 1, 81, z2 - 1, x1 + 1, floors[-1], z2 - 1, 'ladder[facing=east]')
    cx, cz = (x1 + x2) // 2, (z1 + z2) // 2
    for y in [83] + [fy + 3 for fy in floors if fy + 3 < top]:
        pu(cx, y, cz, 'light[level=13]')
    sills = [82] + [fy + 2 for fy in floors]
    for wy in sills:                                   # fenêtres 2 x 2
        for wx in range(x1 + 2, x2 - 2, 4):
            f(wx, wy, z1, wx + 1, wy + 1, z1, 'air')
            f(wx, wy, z2, wx + 1, wy + 1, z2, 'air')
        for wz in range(z1 + 2, z2 - 2, 4):
            f(x1, wy, wz, x1, wy + 1, wz + 1, 'air')
            f(x2, wy, wz, x2, wy + 1, wz + 1, 'air')
    for side, z in (('n', z1), ('s', z2)):             # portes 2 x 2
        if side in doors:
            f(cx, 81, z, cx + 1, 82, z, 'air')
    for _ in range(3):                                 # brèches en haut des murs
        z = rng.choice((z1, z2))
        hx = rng.randint(x1 + 1, max(x1 + 1, x2 - 3))
        f(hx, top - rng.randint(1, 3), z, hx + rng.randint(1, 3), top, z, 'air')
    for _ in range(4):                                 # pierres abîmées
        z = rng.choice((z1, z2))
        mx = rng.randint(x1 + 1, max(x1 + 1, x2 - 2))
        f(mx, rng.randint(81, top - 1), z, mx + 1, rng.randint(81, top - 1), z, rng.choice(('mossy_stone_bricks', 'cracked_stone_bricks')))
    f(x1 + 1, top, z1 + 1, x1 + (x2 - x1) // 2, top, z2 - 1, 'stone_brick_slab[type=bottom]')


def ville(a):
    rng = random.Random(40400)
    a.note('Ville : sol y 80, rangées de ruines (rues décalées), clocher central (zl -4..4)')
    a.fill(-HX, 62, -HZ, HX, 79, HZ, 'stone')
    a.fill(-HX, 80, -HZ, HX, 80, HZ, 'cobblestone')
    for _ in range(26):                                # pavés, gravats, terre
        x, z = rng.randint(-HX, HX - 6), rng.randint(-HZ, 0)
        a.sfill(x, 80, z, x + rng.randint(2, 6), 80, z + rng.randint(2, 6), rng.choice(('gravel', 'coarse_dirt', 'mossy_cobblestone', 'stone_bricks')))
    a.fill(-8, 80, -8, 8, 80, 8, 'stone_bricks')
    rows = [(-20, -54, -9, -45, 7), (-3, -54, 9, -45, 9), (14, -54, 20, -45, 6),         # rue ouest x -8..-4, rue est x 10..13
            (-20, -41, -5, -31, 8), (1, -41, 12, -31, 7), (16, -41, 20, -31, 5),         # rue x -4..0
            (-20, -27, -13, -18, 6), (-7, -27, 6, -18, 10), (11, -27, 20, -18, 7),       # rues x -12..-8 et 7..10
            (-20, -14, -4, -7, 6), (2, -14, 20, -7, 8)]                                  # rue x -3..1
    for (x1, z1, x2, z2, h) in rows:
        ruin(a, rng, x1, z1, x2, z2, h)
    ruin(a, rng, -4, -4, 4, 4, 14, s=False)
    a.note('façades-écrans autour du départ et couverts de rue')
    for (x1, x2) in [(-20, -7), (6, 20)]:
        a.sfill(x1, 81, -61, x2, 85, -61, 'stone_bricks')
        for wx in range(x1 + 2, x2 - 2, 4):
            a.sfill(wx, 82, -61, wx + 1, 83, -61, 'air')
    for (x1, z, x2) in [(-14, -43, -10), (4, -43, 9), (2, -29, 6), (-18, -29, -14), (-12, -16, -8), (6, -16, 11)]:
        a.sfill(x1, 81, z, x2, 82, z, 'stone_bricks')
        a.sfill(x1 + 1, 83, z, x2 - 2, 83, z, 'cracked_stone_bricks')


# ---------------------------------------------------------------------------------------------- Glacier
def mound(a, cx, cz, r, h):
    """Congère : couches de neige de plus en plus étroites (croix), neige fine au sommet."""
    for k in range(h):
        rk = max(1, r - 2 * k)
        a.sfill(cx - rk, 81 + k, cz - rk + 1, cx + rk, 81 + k, cz + rk - 1, 'snow_block')
        a.sfill(cx - rk + 1, 81 + k, cz - rk, cx + rk - 1, 81 + k, cz + rk, 'snow_block')
    a.sput(cx, 81 + h, cz, 'snow[layers=4]')


def serac(a, cx, cz, h, lean, s=True):
    """Sérac : pilier de glace 3 x 3 qui se penche (lean) et s'affine vers le sommet."""
    f = a.sfill if s else a.fill
    for k in range(h):
        off = (k // 4) * lean
        w = 1 if k < h - 3 else 0
        f(cx - w + off, 81 + k, cz - w, cx + w + off, 81 + k, cz + w, 'packed_ice' if k < h // 2 else 'blue_ice')


def watchtower(a, cx, cz):
    """Tour de guet : pieds en bois, mât à échelle, plateforme y 89, garde-corps ajouré (meurtrières au milieu)."""
    for dx in (-2, 2):
        for dz in (-2, 2):
            a.sfill(cx + dx, 81, cz + dz, cx + dx, 88, cz + dz, 'spruce_log')
    a.sfill(cx, 81, cz, cx, 88, cz, 'spruce_log')
    a.sfill(cx - 2, 89, cz - 2, cx + 2, 89, cz + 2, 'spruce_planks')
    a.sfill(cx, 81, cz - 1, cx, 89, cz - 1, 'ladder[facing=north]')
    for dz in (-2, 2):
        a.sfill(cx - 2, 90, cz + dz, cx - 1, 90, cz + dz, 'spruce_fence')
        a.sfill(cx + 1, 90, cz + dz, cx + 2, 90, cz + dz, 'spruce_fence')
    for dx in (-2, 2):
        a.sfill(cx + dx, 90, cz - 2, cx + dx, 90, cz - 1, 'spruce_fence')
        a.sfill(cx + dx, 90, cz + 1, cx + dx, 90, cz + 2, 'spruce_fence')


def glacier(a):
    rng = random.Random(40800)
    a.note('Glacier : sol de neige y 80, lac gelé central, congères, séracs, tours de guet, mur de séracs sur l\'axe')
    a.fill(-HX, 62, -HZ, HX, 75, HZ, 'stone')
    a.fill(-HX, 76, -HZ, HX, 80, HZ, 'snow_block')
    for _ in range(18):
        x, z = rng.randint(-HX, HX - 6), rng.randint(-HZ, 0)
        a.sfill(x, 80, z, x + rng.randint(2, 6), 80, z + rng.randint(2, 6), 'packed_ice')
    a.fill(-11, 80, -11, 11, 80, 11, 'blue_ice')
    for (cx, cz, r, h) in [(-12, -60, 5, 3), (10, -63, 4, 2), (-4, -52, 5, 3), (14, -52, 4, 3),
                           (3, -30, 5, 3), (-17, -24, 4, 2), (-8, -14, 3, 2), (6, -8, 3, 2)]:
        mound(a, cx, cz, r, h)
    for (cx, cz, h, lean) in [(-15, -44, 9, 1), (4, -40, 12, -1), (14, -32, 8, 1), (-6, -26, 10, 1),
                              (-18, -12, 7, 0), (16, -22, 6, -1), (-3, 0, 10, 0)]:
        serac(a, cx, cz, h, lean)
    serac(a, 0, 0, 14, 0, s=False)
    watchtower(a, -14, -34)
    watchtower(a, 12, -16)


MAPS = [dict(key='canyon', name='Canyon', z=40000, y=89, build=canyon),
        dict(key='ville', name='Ville', z=40400, y=81, build=ville),
        dict(key='glacier', name='Glacier', z=40800, y=81, build=glacier)]


def zone(m):
    return f'forceload add {-HX - 2} {m["z"] - HZ - 2} {HX + 2} {m["z"] + HZ + 2}'


def main(root):
    C.init(root)
    sched, names = [], []
    t = FIRST
    for i, m in enumerate(MAPS):
        a = Arena(m['z'])
        a.prologue()
        m['build'](a)
        a.cage()
        lots = a.chunks(CHUNK)
        for k, lines in enumerate(lots, 1):
            fn = f'build_{m["key"]}_{k}'
            body = [f'# Duel sniper : {m["name"]} (z {m["z"]}), lot {k}/{len(lots)} — généré par tools/duel/gen_duel_maps.py'] + lines
            if i == len(MAPS) - 1 and k == len(lots):
                body += ['data modify storage mg:duel built set value 1b',
                         'tellraw @a[tag=mg.admin] [{"text":"⚔ Duel sniper : les 3 arènes sont construites.","color":"gold"}]']
            C.w('duel/' + fn, body)
            sched.append(f'schedule function mg:duel/{fn} {t}t')
            names.append(fn)
            t += STEP
    C.w('duel/build_all', ['# Duel sniper : (re)construit les 3 arènes (une fois au chargement, ou à la main : /function mg:duel/build_all)',
                           'execute if entity @a[tag=mg.dl] run return run tellraw @a[tag=mg.admin] '
                           + C.js([{'text': '⚔ Duel sniper : reconstruction ignorée, un duel est en cours (réessaie après).', 'color': 'red'}]),
                           'data remove storage mg:duel built'] + [zone(m) for m in MAPS] + sched)
    C.w('duel/build_clear', ['# Duel sniper : annule la construction en cours (appelé par duel/remove)', 'schedule clear mg:duel/build_all']
        + [f'schedule clear mg:duel/{n}' for n in names])
    C.forceload(['# Duel sniper (Canyon z 40000, Ville z 40400, Glacier z 40800)'] + [zone(m) for m in MAPS])
    print(f'{len(MAPS)} arènes, {len(names)} lots de construction (dernier lot à {t - STEP} ticks)')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else '.')
