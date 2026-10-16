# ------------------------------------------------------------------ 🧟 Zombies : masques qui font peur (portés sur la tête des mobs) + chien de l'enfer
# Exécuté par gen_rp.py (exec) : utilise wjson, png, A, os.
# Masques : modèles à boîtes (même principe que hats_rp.py : 1 pixel de tête = 1,6 unité, avant = z 0), couleurs d'une palette
# 16×16 mg:item/zm_pal ; yeux lumineux (light_emission). Objets mg:zm/mask_<n> (datapack : tools/arcade/gen_zombies.py).
# Chien de l'enfer : variante de loup mg:hellhound (data/mg/wolf_variant/hellhound.json), textures 64×32 du loup adulte.
import random as _zr

ZPAL = {'S': (214, 206, 182, 255), 's': (150, 140, 118, 255), 'k': (14, 10, 10, 255), 'E': (255, 36, 24, 255), 'e': (255, 214, 60, 255),
        'F': (132, 36, 36, 255), 'f': (82, 18, 22, 255), 'B': (96, 0, 0, 255), 'g': (78, 98, 58, 255), 'G': (44, 62, 36, 255),
        'c': (36, 30, 30, 255), 'C': (58, 48, 46, 255), 'L': (255, 112, 20, 255), 'w': (236, 230, 208, 255), 'h': (54, 44, 40, 255),
        'v': (120, 200, 255, 255)}
ZKEYS = list(ZPAL)
png(os.path.join(A, 'textures', 'item', 'zm_pal.png'),
    [''.join(ZKEYS[i] if (i := (y // 2) * 8 + x // 2) < len(ZKEYS) else '.' for x in range(16)) for y in range(16)], {'.': (0, 0, 0, 0), **ZPAL})


def _zk(p):
    return round(1.6 + 1.6 * p, 3)


def _zel(b):
    x1, y1, z1, x2, y2, z2, c = b[:7]
    i = ZKEYS.index(c)
    u, v = (i % 8) * 2 + 0.5, (i // 8) * 2 + 0.5
    el = {"from": [_zk(x1), _zk(y1), _zk(z1)], "to": [_zk(x2), _zk(y2), _zk(z2)],
          "faces": {d: {"texture": "#p", "uv": [u, v, u + 1, v + 1]} for d in ('north', 'south', 'east', 'west', 'up', 'down')}}
    if 'glow' in b[7:]:
        el["light_emission"] = 15
    return el


def _mir(boxes):
    return [(8 - b[3], b[1], b[2], 8 - b[0], b[4], b[5]) + tuple(b[6:]) for b in boxes]


def _eyes(col, y1=4.4, y2=5.8):
    """orbites noires + pupilles lumineuses, symétriques"""
    L = [(1.0, y1 - 0.3, -0.48, 3.2, y2 + 0.5, -0.31, 'k'), (1.6, y1, -0.6, 2.7, y2, -0.47, col, 'glow')]
    return L + _mir(L)


B = (-0.3, -0.3, -0.3, 8.3, 8.3, 8.3)
MASKS = {
    # 1 : crâne blanchi, orbites noires, yeux rouges, dents
    1: [B + ('S',), (-0.35, -0.35, -0.35, 8.35, 2.6, 5.0, 's'), (3.4, 2.8, -0.5, 4.6, 3.9, -0.32, 'k'),
        (1.3, 0.5, -0.5, 6.7, 2.3, -0.38, 'k'), (1.5, 1.3, -0.55, 6.5, 2.3, -0.45, 'w'), (1.5, 0.5, -0.55, 6.5, 1.0, -0.45, 'w'),
        (2.9, 0.4, -0.6, 3.1, 2.4, -0.5, 'k'), (4.9, 0.4, -0.6, 5.1, 2.4, -0.5, 'k'), (5.4, 6.6, -0.42, 5.8, 8.3, -0.32, 's'),
        (1.0, 8.31, 2.0, 1.4, 8.45, 6.0, 's')] + _eyes('E'),
    # 2 : écorché, mâchoire à nu, yeux jaunes, sang
    2: [B + ('F',), (-0.35, 5.5, -0.35, 8.35, 8.35, 8.35, 'f'), (0.8, -0.4, -0.5, 7.2, 2.7, -0.32, 'S'),
        (1.3, 1.1, -0.6, 6.7, 2.3, -0.48, 'w'), (1.3, 0.6, -0.62, 6.7, 1.1, -0.5, 'k'), (2.0, 2.7, -0.42, 2.6, 4.2, -0.33, 'B'),
        (5.6, 2.7, -0.42, 6.1, 3.6, -0.33, 'B'), (-0.36, 1.0, 2.0, -0.31, 6.0, 6.5, 'f'), (8.31, 1.0, 2.0, 8.36, 6.0, 6.5, 'f')] + _eyes('e'),
    # 3 : brûlé, fissures de lave lumineuses, bouche de braise
    3: [B + ('c',), (-0.35, -0.35, -0.35, 8.35, 3.0, 8.35, 'C'), (0.4, 3.2, -0.42, 7.6, 3.55, -0.33, 'L', 'glow'),
        (3.8, 3.5, -0.42, 4.2, 8.2, -0.33, 'L', 'glow'), (6.6, 0.4, -0.42, 6.95, 3.2, -0.33, 'L', 'glow'),
        (-0.42, 2.0, 1.0, -0.33, 2.35, 7.0, 'L', 'glow'), (8.33, 4.0, 1.0, 8.42, 4.35, 7.0, 'L', 'glow'),
        (2.0, 0.7, -0.45, 6.0, 2.3, -0.33, 'k'), (2.5, 0.9, -0.5, 5.5, 1.5, -0.44, 'L', 'glow')] + _eyes('E'),
    # 4 : pourri (vert), un œil crevé, mâchoire pendante
    4: [B + ('g',), (-0.35, 4.5, -0.35, 8.35, 8.35, 8.35, 'G'), (1.6, 4.6, -0.6, 2.7, 5.7, -0.47, 'v', 'glow'),
        (1.0, 4.1, -0.48, 3.2, 6.3, -0.31, 'k'), (4.8, 4.0, -0.48, 7.2, 6.4, -0.31, 'k'), (5.4, 4.3, -0.5, 6.6, 4.9, -0.45, 'B'),
        (1.5, -0.9, -0.55, 6.5, 2.0, -0.32, 'S'), (1.8, -0.6, -0.6, 6.2, 1.4, -0.5, 'k'), (2.2, 0.8, -0.66, 5.8, 1.4, -0.58, 'w')],
    # 5 : brute — crâne sombre à cornes, yeux rouges
    5: [B + ('h',), (-0.35, -0.35, -0.35, 8.35, 2.4, 8.35, 'k'), (1.3, 0.5, -0.5, 6.7, 2.1, -0.38, 'w'),
        (-2.5, 7.0, 2.5, -0.3, 8.6, 5.0, 'S'), (-3.5, 8.6, 2.7, -2.0, 11.0, 4.8, 'S'), (-3.8, 11.0, 3.0, -3.0, 12.6, 4.4, 's')] +
       _mir([(-2.5, 7.0, 2.5, -0.3, 8.6, 5.0, 'S'), (-3.5, 8.6, 2.7, -2.0, 11.0, 4.8, 'S'), (-3.8, 11.0, 3.0, -3.0, 12.6, 4.4, 's')]) + _eyes('E'),
}
for _n, _boxes in MASKS.items():
    wjson(os.path.join(A, 'models', 'zm', f'mask_{_n}.json'),
          {"textures": {"p": "mg:item/zm_pal", "particle": "mg:item/zm_pal"}, "elements": [_zel(b) for b in _boxes],
           "display": {"gui": {"rotation": [30, 225, 0], "translation": [0, -3, 0], "scale": [0.5, 0.5, 0.5]}}})
    wjson(os.path.join(A, 'items', 'zm', f'mask_{_n}.json'), {"model": {"type": "minecraft:model", "model": f"mg:zm/mask_{_n}"}})

# --- chien de l'enfer : loup calciné, veines de lave, yeux rouges (variante mg:hellhound)
HPAL = {'.': (0, 0, 0, 0), 'c': (30, 24, 24, 255), 'C': (44, 34, 32, 255), 'd': (20, 16, 16, 255), 'L': (255, 104, 18, 255),
        'l': (190, 52, 12, 255), 'E': (255, 30, 20, 255), 'Y': (255, 220, 70, 255), 'w': (236, 228, 204, 255), 'k': (8, 6, 6, 255)}


def _hound(angry):
    rnd = _zr.Random(666)
    img = [[rnd.choice('cccCCd') for _ in range(64)] for _ in range(32)]
    for _ in range(46):                      # veines de lave (marche aléatoire)
        x, y = rnd.randrange(64), rnd.randrange(32)
        for _ in range(rnd.randint(3, 8)):
            img[y][x] = 'L' if rnd.random() < 0.55 else 'l'
            x = max(0, min(63, x + rnd.choice((-1, 0, 1))))
            y = max(0, min(31, y + rnd.choice((-1, 0, 1))))
    # tête 6×6×4 en (0, 0) : face avant en (4..9, 4..9) — orbites noires, yeux rouges (jaunes si enragé), gueule
    for x in range(4, 10):
        for y in range(4, 10):
            img[y][x] = 'd'
    for (x, y) in [(4, 6), (5, 6), (8, 6), (9, 6), (4, 7), (9, 7)]:
        img[y][x] = 'k'
    eye = 'Y' if angry else 'E'
    for (x, y) in [(5, 7), (8, 7)]:
        img[y][x] = eye
    for x in range(5, 9):
        img[9][x] = 'L'
    # museau 3×3×4 en (0, 10) : face avant en (4..6, 14..16) — crocs
    for x in range(4, 7):
        img[14][x], img[15][x], img[16][x] = 'k', 'k', 'w'
    img[15][4] = img[15][6] = 'w'
    return [''.join(r) for r in img]


for _n, _ang in [('hellhound', False), ('hellhound_angry', True)]:
    png(os.path.join(A, 'textures', 'entity', 'wolf', f'{_n}.png'), _hound(_ang), HPAL)
