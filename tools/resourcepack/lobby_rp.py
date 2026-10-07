# ------------------------------------------------------------------ spawn : armes du lobby, trophée, cristal, logo et panneaux (police mg:lobby)
# Exécuté par gen_rp.py (exec) : utilise png, pad, wjson, item_def, box, solid, png_rgba, PAL, A.
LPAL = dict(PAL)
LPAL.update({'C': (40, 200, 230, 255), 'e': (170, 245, 255, 255), 'v': (150, 100, 220, 255), 'V': (90, 50, 150, 255),
             'h': (225, 240, 255, 255), 'H': (150, 195, 235, 255)})

def orb(kind):
    rows = []
    for y in range(16):
        s = ''
        for x in range(16):
            dx, dy = x - 7.5, y - 7.5
            d = math.hypot(dx, dy)
            if d > 6.6: s += '.'; continue
            if d > 5.7: s += 'H' if kind == 'snow' else 'C'; continue
            if kind == 'snow':
                s += 'w' if dx + dy < -3 else ('h' if dx + dy < 4 else 'H')
            else:
                band = (math.atan2(dy, dx) * 2 / math.pi + d / 2.2) % 2
                s += 'e' if band < 0.7 else ('h' if band < 1.1 else 'C')
        rows.append(s)
    return rows

LSPR = {
    'laser_gun': ['', '', '', '  dddddddddd', ' dllllllllllddd', ' dlrrrrrrrrldCe', ' dlrwwwwrrrldCe', ' dlllllllllldd', ' ddRRRddddd',
                  '  dRRRd kd', ' dRRRd kkd', ' dRRRdddd', 'dRRRd', 'dRRRd', 'ddddd'],
    'magic_wand': ['            y', '           yyy', '         yyyyyyy', '          yyyyy', '          yy yy', '         VV', '        Vv',
                   '       Vv', '      Vv', '     Vv', '    Vv', '   Vv', '  Vv', ' YY', 'YY'],
    'wind_orb': orb('wind'),
    'snow_orb': orb('snow'),
}
for name, rows in LSPR.items():
    png(os.path.join(A, 'textures', 'item', name + '.png'), pad(rows), LPAL)
    parent = 'minecraft:item/handheld' if name == 'magic_wand' else 'minecraft:item/generated'
    wjson(os.path.join(A, 'models', 'item', name + '.json'), {"parent": parent, "textures": {"layer0": f"mg:item/{name}"}})
    item_def(name, f'mg:item/{name}')

# trophée (coupe dorée) et cristal (teinté par dyed_color)
for name, (c1, c2) in {'trophy_gold': ((255, 208, 50, 255), (232, 168, 24, 255)), 'trophy_base': ((62, 42, 30, 255), (44, 30, 22, 255)),
                       'crystal': ((240, 240, 255, 255), (200, 205, 230, 255))}.items():
    rows, pal = solid(c1, c2)
    png(os.path.join(A, 'textures', 'item', name + '.png'), rows, pal)
wjson(os.path.join(A, 'models', 'item', 'trophy.json'), {
    "textures": {"g": "mg:item/trophy_gold", "b": "mg:item/trophy_base", "particle": "mg:item/trophy_gold"},
    "elements": [box([4, 0, 4], [12, 2, 12], 'b'), box([5, 2, 5], [11, 3, 11], 'g'), box([7, 3, 7], [9, 7, 9], 'g'), box([6, 7, 6], [10, 8, 10], 'g'),
                 box([4, 8, 4], [12, 14, 12], 'g'), box([3, 14, 3], [13, 16, 13], 'g'), box([5, 15.5, 5], [11, 16.2, 11], 'b'),
                 box([1, 9, 7], [4, 10, 9], 'g'), box([1, 10, 7], [2, 13, 9], 'g'), box([12, 9, 7], [15, 10, 9], 'g'), box([14, 10, 7], [15, 13, 9], 'g')],
    "display": {"gui": {"rotation": [30, 225, 0], "scale": [0.6, 0.6, 0.6]}}})
item_def('trophy', 'mg:item/trophy')
wjson(os.path.join(A, 'models', 'item', 'crystal.json'), {
    "textures": {"c": "mg:item/crystal", "particle": "mg:item/crystal"},
    "elements": [box([6, 0, 6], [10, 2, 10], 'c', True), box([5, 2, 5], [11, 5, 11], 'c', True), box([4, 5, 4], [12, 10, 12], 'c', True),
                 box([5, 10, 5], [11, 13, 11], 'c', True), box([6, 13, 6], [10, 15, 10], 'c', True), box([7, 15, 7], [9, 16.5, 9], 'c', True)],
    "display": {"gui": {"rotation": [30, 225, 0], "scale": [0.6, 0.6, 0.6]}}})
item_def('crystal', 'mg:item/crystal', tint=-1)

# ------------------------------------------------------------------ police pixel 5 x 7 (+ 2 lignes d'accent) pour le logo et les panneaux
FONT5 = {
    'A': [' ### ', '#   #', '#   #', '#####', '#   #', '#   #', '#   #'], 'B': ['#### ', '#   #', '#   #', '#### ', '#   #', '#   #', '#### '],
    'C': [' ### ', '#   #', '#    ', '#    ', '#    ', '#   #', ' ### '], 'D': ['#### ', '#   #', '#   #', '#   #', '#   #', '#   #', '#### '],
    'E': ['#####', '#    ', '#    ', '#### ', '#    ', '#    ', '#####'], 'G': [' ### ', '#   #', '#    ', '# ###', '#   #', '#   #', ' ####'],
    'I': ['###', ' # ', ' # ', ' # ', ' # ', ' # ', '###'], 'J': ['  ###', '   # ', '   # ', '   # ', '   # ', '#  # ', ' ##  '],
    'K': ['#   #', '#  # ', '# #  ', '##   ', '# #  ', '#  # ', '#   #'], 'L': ['#    ', '#    ', '#    ', '#    ', '#    ', '#    ', '#####'],
    'M': ['#   #', '## ##', '# # #', '# # #', '#   #', '#   #', '#   #'], 'N': ['#   #', '##  #', '# # #', '#  ##', '#   #', '#   #', '#   #'],
    'O': [' ### ', '#   #', '#   #', '#   #', '#   #', '#   #', ' ### '], 'P': ['#### ', '#   #', '#   #', '#### ', '#    ', '#    ', '#    '],
    'R': ['#### ', '#   #', '#   #', '#### ', '# #  ', '#  # ', '#   #'], 'S': [' ####', '#    ', '#    ', ' ### ', '    #', '    #', '#### '],
    'T': ['#####', '  #  ', '  #  ', '  #  ', '  #  ', '  #  ', '  #  '], 'U': ['#   #', '#   #', '#   #', '#   #', '#   #', '#   #', ' ### '],
    'V': ['#   #', '#   #', '#   #', '#   #', '#   #', ' # # ', '  #  '], 'X': ['#   #', '#   #', ' # # ', '  #  ', ' # # ', '#   #', '#   #'],
    '-': ['   ', '   ', '   ', '###', '   ', '   ', '   '], ' ': ['  ', '  ', '  ', '  ', '  ', '  ', '  '],
}
ACCENT = {'É': ('E', ['   # ', '  #  '])}

def text_mask(txt):
    cols = []
    for i, ch in enumerate(txt):
        base, acc = ACCENT.get(ch, (ch, ['', '']))
        g = FONT5[base]; w = len(g[0])
        rows = [a.ljust(w)[:w] for a in acc] + g
        for x in range(w): cols.append([rows[y][x] == '#' for y in range(9)])
        if i < len(txt) - 1: cols.append([False] * 9)
    return [[cols[x][y] for x in range(len(cols))] for y in range(9)]

def new_img(w, h): return [[(0, 0, 0, 0)] * w for _ in range(h)]

def render_text(txt, sc, top, bot, outline, ol=1, shadow=None, sh=0):
    m = text_mask(txt)
    mh, mw = len(m), len(m[0])
    pad_ = ol + sh
    W_, H_ = mw * sc + 2 * ol + sh, mh * sc + 2 * ol + sh
    big = [[m[y // sc][x // sc] for x in range(mw * sc)] for y in range(mh * sc)]
    img = new_img(W_, H_)
    def on(x, y): return 0 <= y < mh * sc and 0 <= x < mw * sc and big[y][x]
    y0 = 2 * sc                                   # haut des lettres (sous l'accent)
    for y in range(H_):
        for x in range(W_):
            bx, by = x - ol, y - ol
            if on(bx, by):
                t = max(0.0, min(1.0, (by - y0) / max(1, 7 * sc - 1)))
                c = tuple(int(top[i] + (bot[i] - top[i]) * t) for i in range(3))
                if by - y0 < sc // 2 + 1 and not on(bx, by - 1): c = tuple(min(255, v + 50) for v in c)
                img[y][x] = c + (255,)
            elif any(on(bx + dx, by + dy) for dx in range(-ol, ol + 1) for dy in range(-ol, ol + 1)):
                img[y][x] = outline + (255,)
            elif shadow and any(on(bx - sh + dx, by - sh + dy) for dx in range(-ol, ol + 1) for dy in range(-ol, ol + 1)):
                img[y][x] = shadow
    return img

def blit(dst, src, ox, oy):
    for y, row in enumerate(src):
        for x, p in enumerate(row):
            if p[3] and 0 <= oy + y < len(dst) and 0 <= ox + x < len(dst[0]): dst[oy + y][ox + x] = p

def sparkle(img, cx, cy, col):
    for d in range(-3, 4):
        for (x, y) in ((cx + d, cy), (cx, cy + d)):
            if 0 <= y < len(img) and 0 <= x < len(img[0]): img[y][x] = col if abs(d) < 3 else tuple(col[:3]) + (140,)

t1 = render_text('NEOMC', 5, (255, 240, 120), (245, 120, 20), (70, 28, 4), ol=2, shadow=(0, 0, 0, 110), sh=3)
t2 = render_text('MINI-JEUX', 3, (255, 255, 255), (140, 205, 255), (18, 38, 92), ol=2, shadow=(0, 0, 0, 110), sh=2)
LW = max(len(t1[0]), len(t2[0])) + 24
logo = new_img(LW, len(t1) + len(t2) + 2)
blit(logo, t1, (LW - len(t1[0])) // 2, 0)
blit(logo, t2, (LW - len(t2[0])) // 2, len(t1) + 2)
for (sx, sy) in ((4, 12), (LW - 5, 20), (8, len(t1) + 10), (LW - 9, len(t1) + 4)):
    sparkle(logo, sx, sy, (255, 245, 170, 255))
png_rgba(os.path.join(A, 'textures', 'font', 'lobby_logo.png'), logo)

def icon_img(kind):
    g = [['.'] * 12 for _ in range(12)]
    def s(x, y, c):
        if 0 <= x < 12 and 0 <= y < 12: g[y][x] = c
    if kind == 'swords':
        for i in range(8): s(1 + i, 1 + i, 'w'); s(10 - i, 1 + i, 'w')
        for (x, y) in ((7, 9), (9, 7), (2, 7), (4, 9)): s(x, y, 'y')
        for (x, y) in ((9, 9), (10, 10), (2, 9), (1, 10)): s(x, y, 'n')
    elif kind == 'target':
        for y in range(12):
            for x in range(12):
                d = math.hypot(x - 5.5, y - 5.5)
                if d < 6: s(x, y, 'r' if d < 1.6 or 3 <= d < 4.5 else 'w')
    elif kind == 'flag':
        for y in range(1, 12): s(2, y, 'n')
        for y in range(1, 6):
            for x in range(3, 10): s(x, y, 'k' if (x // 2 + y // 2) % 2 else 'w')
    elif kind == 'house':
        for y in range(0, 5):
            for x in range(5 - y, 7 + y): s(x, y + 1, 'r')
        for y in range(6, 11):
            for x in range(2, 10): s(x, y, 't')
        for y in range(8, 11): s(5, y, 'n'); s(6, y, 'n')
        for x in range(12): s(x, 11, 'g')
    elif kind == 'wheel':
        for y in range(12):
            for x in range(12):
                d = math.hypot(x - 5.5, y - 5.5)
                if 4.3 <= d < 5.9: s(x, y, 'k')
                elif d < 1.6: s(x, y, 'r')
        for i in range(2, 10): s(i, 6, 'd'); s(i, 5, 'd')
        for i in range(6, 10): s(5, i, 'd'); s(6, i, 'd')
    elif kind == 'cup':
        for y in range(1, 6):
            for x in range(3, 9): s(x, y, 'y')
        for y in (2, 3): s(1, y, 'y'); s(10, y, 'y')
        s(2, 4, 'y'); s(9, 4, 'y')
        for y in (6, 7): s(5, y, 'Y'); s(6, y, 'Y')
        for x in range(3, 9): s(x, 9, 'n'); s(x, 10, 'n')
        for x in range(4, 8): s(x, 8, 'Y')
    return [''.join(r) for r in g]

def sign_img(txt, icon, bg, border):
    t = render_text(txt, 2, (255, 255, 255), (215, 215, 225), (20, 20, 24), ol=1, shadow=(0, 0, 0, 120), sh=1)
    ic = icon_img(icon)
    w, h = 10 + 24 + 6 + len(t[0]) + 10, max(30, len(t) + 10)
    img = new_img(w, h)
    for y in range(h):
        for x in range(w):
            corner = min(x, w - 1 - x) + min(y, h - 1 - y)
            if corner < 2: continue
            edge = x < 2 or y < 2 or x >= w - 2 or y >= h - 2 or corner < 4
            shade = 0.82 if y > h * 0.6 else 1.0
            img[y][x] = (tuple(border) if edge else tuple(int(c * shade) for c in bg)) + (255,)
    for y, row in enumerate(ic):
        for x, c in enumerate(row):
            if c != '.':
                for dy in range(2):
                    for dx in range(2): img[(h - 24) // 2 + y * 2 + dy][10 + x * 2 + dx] = PAL[c]
    blit(img, t, 10 + 24 + 6, (h - len(t)) // 2 + 1)
    return img

SIGNS = [('ARMURERIE', 'swords', (92, 42, 28), (236, 186, 70)), ('STAND DE TIR', 'target', (66, 66, 76), (230, 70, 60)),
         ('PARKOUR', 'flag', (28, 104, 48), (150, 240, 120)), ('PLOTS', 'house', (72, 40, 120), (205, 160, 255)),
         ('GARAGE KART', 'wheel', (170, 28, 28), (255, 255, 255)), ('ARRIVÉE', 'cup', (26, 76, 150), (130, 220, 255))]
prov = [{"type": "bitmap", "file": "mg:font/lobby_logo.png", "ascent": len(logo) - 8, "height": len(logo), "chars": [""]}]
for i, (txt, ic, bg, bd) in enumerate(SIGNS):
    img = sign_img(txt, ic, bg, bd)
    png_rgba(os.path.join(A, 'textures', 'font', f'lobby_sign_{i}.png'), img)
    prov.append({"type": "bitmap", "file": f"mg:font/lobby_sign_{i}.png", "ascent": len(img) - 6, "height": len(img), "chars": [chr(0xE101 + i)]})
wjson(os.path.join(A, 'font', 'lobby.json'), {"providers": prov})
print('spawn : logo', len(logo[0]), 'x', len(logo))
