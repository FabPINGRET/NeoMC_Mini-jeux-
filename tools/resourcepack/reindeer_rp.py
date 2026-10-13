# ------------------------------------------------------------------ Noël : rennes (variantes de vache mg:reindeer et mg:rudolph, modèle « cold »)
# Exécuté par gen_rp.py (exec) : utilise png, A, os. Variantes côté datapack : data/mg/cow_variant/{reindeer,rudolph}.json.
# Peint face par face sur la disposition UV de la vache froide (tête 8x8x6, museau 6x3x2, cornes 2x6x2, corps 12x18x10,
# toison 12x18x10 sans face ventrale, pattes 4x12x4 ; bébé : corps 8x6x12, tête 6x6x5, museau 4x3x1, cornes 1x2x1, pattes 3x6x3).
# Repères du renne de Noël : dos brun foncé, ventre crème, crinière blanche au poitrail, miroir blanc à la croupe,
# pattes sombres à manchettes claires, museau crème, bois clairs, harnais rouge à grelots dorés ; Rudolph a le nez rouge.
import random
DEER_PAL = {'.': (0, 0, 0, 0), 'b': (104, 74, 52, 255), 'B': (86, 60, 42, 255), 'm': (138, 102, 72, 255), 'M': (118, 86, 60, 255),
            'c': (236, 226, 206, 255), 'C': (212, 200, 176, 255), 'g': (70, 52, 40, 255), 'G': (56, 42, 32, 255), 'o': (36, 30, 26, 255),
            'h': (226, 206, 168, 255), 'H': (180, 152, 112, 255), 'r': (200, 30, 36, 255), 'R': (140, 18, 26, 255),
            'y': (252, 208, 64, 255), 'Y': (196, 148, 30, 255), 'k': (20, 16, 14, 255), 'w': (250, 250, 250, 255),
            'n': (236, 34, 38, 255), 'N': (160, 18, 24, 255), 'p': (255, 150, 150, 255), 'x': (44, 34, 30, 255), 'X': (24, 18, 16, 255)}
# frange de la toison (vanilla) : largeur opaque des flancs droits / début des flancs gauches, rangées 40-41 des faces poitrail/croupe
SHAG_R = [9, 9, 9, 10, 9, 8, 10, 9, 10, 8, 9, 10, 9, 10, 9, 8, 10, 9]
SHAG_L = [43, 42, 44, 43, 44, 42, 43, 44, 42, 43, 44, 43, 42, 43, 42, 43, 44, 42]
SHAG_ROWS = ['################.##.####', '.#..#...#..#.#........#.']


def _box(u, v, w, h, d):
    return {'top': (u + d, v, w, d), 'bottom': (u + d + w, v, w, d), 'right': (u, v + d, d, h),
            'front': (u + d, v + d, w, h), 'left': (u + d + w, v + d, d, h), 'back': (u + 2 * d + w, v + d, w, h)}


def _deer(baby, rudolph):
    rnd = random.Random(1225)
    img = [['.'] * 64 for _ in range(64)]
    fur = lambda c: c.upper() if c in 'bmcgh' and rnd.random() < 0.22 else c

    def fill(rect, f):
        x0, y0, w, h = rect
        for j in range(h):
            for i in range(w):
                c = f(i, j, w, h)
                if c:
                    img[y0 + j][x0 + i] = fur(c)

    def coat(s, t):  # flanc : s 0 échine -> 1 ventre, t 0 poitrail -> 1 croupe
        s += rnd.uniform(-0.06, 0.06)
        if t < 0.18:
            return 'm' if s < 0.25 else 'c'
        if t > 0.85 and s < 0.6:
            return 'c'
        return 'b' if s < 0.4 else ('m' if s < 0.78 else 'c')

    nose = ('n', 'N', 'p') if rudolph else ('x', 'X', 'x')
    if not baby:
        hd = _box(0, 0, 8, 8, 6)
        fill(hd['top'], lambda i, j, w, h: 'b')
        fill(hd['bottom'], lambda i, j, w, h: 'c')
        for f in ('right', 'left'):
            fill(hd[f], lambda i, j, w, h: 'b' if j < 2 else ('c' if j == h - 1 else 'm'))
        fill(hd['back'], lambda i, j, w, h: 'b' if j < 5 else 'c')
        fill(hd['front'], lambda i, j, w, h: 'b' if j < 2 else ({0: 'k', 1: 'w', 6: 'w', 7: 'k'}.get(i, 'm') if j == 3 else 'm'))
        mz = _box(8, 32, 6, 3, 2)
        for f in ('top', 'bottom', 'right', 'left', 'back'):
            fill(mz[f], lambda i, j, w, h: 'c')
        if rudolph:
            fill(mz['top'], lambda i, j, w, h: 'n' if j == 1 and 1 <= i <= 4 else None)
        fill(mz['front'], lambda i, j, w, h: ('c' + nose[0] + nose[2] + nose[0] + nose[1] + 'c', 'c' + nose[1] * 4 + 'c', 'CCccCC')[j][i])
        for v in (32, 40):
            hn = _box(0, v, 2, 6, 2)
            for f in hn:
                fill(hn[f], lambda i, j, w, h: 'H' if f not in ('top', 'bottom') and j in (2, 4) and i == 0 else 'h')
        lg = _box(0, 16, 4, 12, 4)
        fill(lg['top'], lambda i, j, w, h: 'm')
        fill(lg['bottom'], lambda i, j, w, h: 'o')
        for f in ('right', 'front', 'left', 'back'):
            fill(lg[f], lambda i, j, w, h: 'm' if j < 3 else ('g' if j < 9 else ('c' if j == 9 else 'o')))
        for y, x0, x1 in [(0, 53, 61)] + [(y, 52, 58) for y in range(1, 7)]:  # pis : couleur du ventre
            for x in range(x0, x1):
                img[y][x] = 'c'
        band, bell = (5, 6), (7, 8)  # rangées (depuis le poitrail) du harnais, grelots en dessous côté ventre

        def flank(right):
            def f(i, j, w, h):
                s = i / (w - 1) if right else 1 - i / (w - 1)
                if j in band:
                    return 'R' if j == band[1] else 'r'
                if j in bell and 0.6 < s < 0.9:
                    return 'y' if j == bell[0] else 'Y'
                return coat(s, j / (h - 1))
            return f

        for v, u in ((4, 18), (32, 20)):
            bx = _box(u, v, 12, 18, 10)
            fill(bx['right'], flank(True))
            fill(bx['left'], flank(False))
            fill(bx['back'], lambda i, j, w, h: ('y' if 5 <= i <= 6 else 'r') if j in band else
                 ('m' if j < 3 else ('c' if j > 14 and 3 <= i <= 8 else ('B' if 5 <= i <= 6 else 'b'))))
            fill(bx['top'], lambda i, j, w, h: 'm' if j < 2 else (('y' if 5 <= i <= 6 else 'r') if j == 5 else 'c'))
            fill(bx['bottom'], lambda i, j, w, h: 'b' if j < 2 else ('m' if i in (0, w - 1) else 'c'))
            if u == 18:
                fill(bx['front'], lambda i, j, w, h: 'r' if j in band else 'c')
        for k, y in enumerate(range(42, 60)):  # frange de la toison
            for x in range(20 + SHAG_R[k], 30):
                img[y][x] = '.'
            for x in range(42, SHAG_L[k]):
                img[y][x] = '.'
        for k, row in enumerate(SHAG_ROWS):
            for i, ch in enumerate(row):
                if ch == '.':
                    img[40 + k][30 + i] = '.'
    else:
        bd = _box(0, 0, 8, 6, 12)
        fill(bd['top'], lambda i, j, w, h: 'm' if j > 9 else ('c' if j < 2 and 2 <= i <= 5 else 'b'))
        fill(bd['bottom'], lambda i, j, w, h: 'c')
        fill(bd['right'], lambda i, j, w, h: coat(j / (h - 1), 1 - i / (w - 1)))
        fill(bd['left'], lambda i, j, w, h: coat(j / (h - 1), i / (w - 1)))
        fill(bd['front'], lambda i, j, w, h: 'm' if j == 0 else 'c')
        fill(bd['back'], lambda i, j, w, h: 'b' if j == 0 else ('m' if i in (0, w - 1) else 'c'))
        hd = _box(0, 18, 6, 6, 5)
        fill(hd['top'], lambda i, j, w, h: 'b')
        fill(hd['bottom'], lambda i, j, w, h: 'c')
        for f in ('right', 'left'):
            fill(hd[f], lambda i, j, w, h: 'c' if j == h - 1 else 'm')
        fill(hd['back'], lambda i, j, w, h: 'b' if j < 3 else 'c')
        fill(hd['front'], lambda i, j, w, h: 'b' if j == 0 else ('k' if j == 2 and i in (0, 5) else 'm'))
        for u in (4, 8):
            hn = _box(u, 29, 1, 2, 1)
            for f in hn:
                fill(hn[f], lambda i, j, w, h: 'h')
        mz = _box(12, 29, 4, 3, 1)
        for f in ('top', 'bottom', 'right', 'left', 'back'):
            fill(mz[f], lambda i, j, w, h: 'c')
        fill(mz['front'], lambda i, j, w, h: ('c' + nose[0] * 2 + 'c', 'c' + nose[1] * 2 + 'c', 'CccC')[j][i])
        for u, v in ((22, 18), (34, 18), (22, 27), (34, 27)):
            lg = _box(u, v, 3, 6, 3)
            fill(lg['top'], lambda i, j, w, h: 'm')
            fill(lg['bottom'], lambda i, j, w, h: 'o')
            for f in ('right', 'front', 'left', 'back'):
                fill(lg[f], lambda i, j, w, h: 'g' if j < 4 else ('c' if j == 4 else 'o'))
    return [''.join(r) for r in img]


for _nm, _rud in (('reindeer', False), ('rudolph', True)):
    for _baby in (False, True):
        png(os.path.join(A, 'textures', 'entity', 'cow', _nm + ('_baby' if _baby else '') + '.png'), _deer(_baby, _rud), DEER_PAL)
