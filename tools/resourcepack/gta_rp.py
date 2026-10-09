# ------------------------------------------------------------------ GTA : étoiles de recherche, viseurs, chiffres de l'argent, liasse de billets
# Exécuté par gen_rp.py (exec) : utilise png, png_rgba, pad, wjson, item_def, PAL, A, OUT, math, os.
#
# Police mg:gta (glyphes privés) :
#    étoile pleine,  étoile vide,  espace fin : noms des barres de boss mg:gtaw1..5 (haut de l'écran)
#    viseur blanc,  viseur rouge,  lunette du sniper : envoyés en titre, centrés sur le réticule
#   (titre = échelle 4, ligne à y -10 : ascent = hauteur / 2 - 3)
# Police mg:gta_cash : chiffres 0-9 et $ façon GTA (vert, contour noir) pour l'argent dans la barre d'action.
# Barre de boss blanche rendue transparente (aucune barre du pack ni de vanilla n'est blanche) : seules les étoiles s'affichent.

K_ = (0, 0, 0, 255)
T_ = (0, 0, 0, 0)


def blank(w, h):
    return [[T_ for _ in range(w)] for _ in range(h)]


def star_img(full):
    n = 32
    img = blank(n, n)
    cx = cy = (n - 1) / 2
    pts = []
    for i in range(10):
        r = 15.0 if i % 2 == 0 else 6.4
        a = -math.pi / 2 + i * math.pi / 5
        pts.append((cx + r * math.cos(a), cy + 1.2 + r * math.sin(a)))

    def inside(x, y):
        c = False
        for i in range(10):
            (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % 10]
            if (y1 > y) != (y2 > y) and x < (x2 - x1) * (y - y1) / (y2 - y1) + x1:
                c = not c
        return c
    mask = [[inside(x + 0.5, y + 0.5) for x in range(n)] for y in range(n)]
    for y in range(n):
        for x in range(n):
            if not mask[y][x]:
                continue
            edge = any(not (0 <= x + dx < n and 0 <= y + dy < n and mask[y + dy][x + dx])
                       for dx in (-1, 0, 1) for dy in (-1, 0, 1)) or any(
                not (0 <= x + dx < n and 0 <= y + dy < n and mask[y + dy][x + dx]) for dx, dy in ((2, 0), (-2, 0), (0, 2), (0, -2)))
            if edge:
                img[y][x] = K_
            elif full:
                shade = 255 if y < 18 else 228
                img[y][x] = (shade, shade, shade, 255)
            else:
                img[y][x] = (40, 40, 44, 110)
    return img


def reticle_img(rgb):
    n = 32
    img = blank(n, n)
    c = (n - 1) / 2
    col = rgb + (235,)
    for y in range(n):
        for x in range(n):
            d = math.hypot(x - c, y - c)
            if 10.2 <= d <= 11.4:
                img[y][x] = col
            elif 9.4 <= d < 10.2 or 11.4 < d <= 12.2:
                img[y][x] = (0, 0, 0, 120)
    for (x, y) in [(15, 15), (16, 15), (15, 16), (16, 16)]:
        img[y][x] = col
    for k in range(3):                       # 4 petits traits sur l'anneau
        for (x, y) in [(15 + 0, 3 + k), (16, 3 + k), (15, 26 + k), (16, 26 + k), (3 + k, 15), (3 + k, 16), (26 + k, 15), (26 + k, 16)]:
            img[y][x] = col
    return img


def scope_img():
    """Lunette du sniper : 512 × 256, noir hors du cercle, fin réticule à graduations."""
    w, h = 512, 256
    img = [[(0, 0, 0, 255) for _ in range(w)] for _ in range(h)]
    cx, cy, r = (w - 1) / 2, (h - 1) / 2, 118
    for y in range(h):
        for x in range(w):
            d = math.hypot(x - cx, y - cy)
            if d < r - 3:
                img[y][x] = T_
            elif d < r:
                img[y][x] = (0, 0, 0, 200)
            elif d < r + 2:
                img[y][x] = (20, 20, 20, 255)
    line = (10, 10, 10, 230)
    for x in range(int(cx - r), int(cx + r) + 1):
        if abs(x - cx) > 3:
            img[127][x] = line; img[128][x] = line
    for y in range(int(cy - r), int(cy + r) + 1):
        if 0 <= y < h and abs(y - cy) > 3:
            img[y][255] = line; img[y][256] = line
    for k in range(1, 8):                       # graduations (mil-dots)
        for sgn in (-1, 1):
            for dd in (-1, 0, 1, 2):
                x = int(cx + sgn * k * 14)
                img[127 + dd][x] = line
                y = int(cy + sgn * k * 14)
                if 0 <= y < h:
                    img[y][255 + dd] = line
    img[127][255] = img[128][256] = img[127][256] = img[128][255] = (220, 30, 30, 255)
    return img


png_rgba(os.path.join(A, 'textures', 'font', 'gta_scope.png'), scope_img())
png_rgba(os.path.join(A, 'textures', 'font', 'gta_star.png'), star_img(True))
png_rgba(os.path.join(A, 'textures', 'font', 'gta_star_empty.png'), star_img(False))
png_rgba(os.path.join(A, 'textures', 'font', 'gta_reticle.png'), reticle_img((255, 255, 255)))
png_rgba(os.path.join(A, 'textures', 'font', 'gta_reticle_red.png'), reticle_img((235, 40, 40)))
wjson(os.path.join(A, 'font', 'gta.json'), {"providers": [
    {"type": "bitmap", "file": "mg:font/gta_star.png", "ascent": 9, "height": 11, "chars": [""]},
    {"type": "bitmap", "file": "mg:font/gta_star_empty.png", "ascent": 9, "height": 11, "chars": [""]},
    {"type": "space", "advances": {"": 1, " ": 4}},
    {"type": "bitmap", "file": "mg:font/gta_reticle.png", "ascent": 1, "height": 8, "chars": [""]},
    {"type": "bitmap", "file": "mg:font/gta_reticle_red.png", "ascent": 1, "height": 8, "chars": [""]},
    {"type": "bitmap", "file": "mg:font/gta_scope.png", "ascent": 29, "height": 64, "chars": [""]}]})

# chiffres : 6 × 9 « gras », contour noir, dégradé vert (style Pricedown)
DIG = {
    '0': ['.####.', '##..##', '##..##', '##.###', '###.##', '##..##', '##..##', '##..##', '.####.'],
    '1': ['..##..', '.###..', '####..', '..##..', '..##..', '..##..', '..##..', '..##..', '######'],
    '2': ['.####.', '##..##', '....##', '...##.', '..##..', '.##...', '##....', '##....', '######'],
    '3': ['.####.', '##..##', '....##', '..###.', '....##', '....##', '....##', '##..##', '.####.'],
    '4': ['...##.', '..###.', '.####.', '##.##.', '##.##.', '######', '...##.', '...##.', '...##.'],
    '5': ['######', '##....', '##....', '#####.', '....##', '....##', '....##', '##..##', '.####.'],
    '6': ['.####.', '##..##', '##....', '#####.', '##..##', '##..##', '##..##', '##..##', '.####.'],
    '7': ['######', '....##', '...##.', '...##.', '..##..', '..##..', '.##...', '.##...', '.##...'],
    '8': ['.####.', '##..##', '##..##', '.####.', '##..##', '##..##', '##..##', '##..##', '.####.'],
    '9': ['.####.', '##..##', '##..##', '##..##', '.#####', '....##', '....##', '##..##', '.####.'],
    '$': ['..##..', '.####.', '##.#.#', '##.#..', '.####.', '..#.##', '#.#.##', '.####.', '..##..'],
}
CH = '0123456789$'
CW, CHH = 8, 11
sheet = blank(CW * len(CH), CHH)
for i, ch in enumerate(CH):
    rows = DIG[ch]
    on = [[rows[y][x] == '#' for x in range(6)] for y in range(9)]
    for y in range(CHH):
        for x in range(CW):
            gx, gy = x - 1, y - 1
            if 0 <= gx < 6 and 0 <= gy < 9 and on[gy][gx]:
                g = 214 - gy * 9
                sheet[y][i * CW + x] = (int(g * 0.52), g, int(g * 0.42), 255)
            elif any(0 <= gx + dx < 6 and 0 <= gy + dy < 9 and on[gy + dy][gx + dx] for dx in (-1, 0, 1) for dy in (-1, 0, 1)):
                sheet[y][i * CW + x] = (10, 22, 10, 255)
png_rgba(os.path.join(A, 'textures', 'font', 'gta_cash.png'), sheet)
wjson(os.path.join(A, 'font', 'gta_cash.json'), {"providers": [
    {"type": "bitmap", "file": "mg:font/gta_cash.png", "ascent": 10, "height": 12, "chars": [CH]},
    {"type": "space", "advances": {" ": 5}}]})

# liasse de billets (valises, sacs lâchés à la mort)
CPAL = dict(PAL)
CPAL.update({'m': (96, 160, 80, 255), 'M': (58, 110, 48, 255), 'h': (170, 214, 150, 255), 'x': (34, 70, 30, 255), 'e': (230, 200, 90, 255)})
CASH = ['', '',
        '   xxxxxxxxxx',
        '  xhhhhhhhhhhx',
        ' xmmmmmmmmmmmmx',
        ' xmMmmmeemmmMmx',
        ' xmmmmeMMemmmmx',
        ' xmMmmmeemmmMmx',
        ' xmmmmmmmmmmmmx',
        ' xhhhhhhhhhhhhx',
        ' xmmmmmmmmmmmmx',
        ' xmMmmmmmmmmMmx',
        ' xmmmmmmmmmmmmx',
        '  xxxxxxxxxxxx']
png(os.path.join(A, 'textures', 'item', 'cash.png'), pad(CASH), CPAL)
wjson(os.path.join(A, 'models', 'item', 'cash.json'), {"parent": "minecraft:item/generated", "textures": {"layer0": "mg:item/cash"}})
item_def('cash', 'mg:item/cash')

# barre de boss blanche transparente (étoiles seules en haut de l'écran)
for part in ('white_background', 'white_progress'):
    png_rgba(os.path.join(OUT, 'assets', 'minecraft', 'textures', 'gui', 'sprites', 'boss_bar', part + '.png'), blank(182, 5))

# carte de Neo City (police mg:gta_map) :  = plan (image écrite par tools/arcade/gen_bomber.py, 177 × 177),
#  = espace de -65 (retour au bord gauche du plan),  + 30 × ligne + colonne = point « tu es ici »
# (image transparente de la taille du plan : même avance de 65, le point tombe à la bonne case). Titre : ascent = 64 / 2 - 3.
MAPN, CELLS = 177, 30
map_prov = [{"type": "bitmap", "file": "mg:font/gta_map.png", "ascent": 29, "height": 64, "chars": [""]},
            {"type": "space", "advances": {"": -65}}]
for j in range(CELLS):
    for i in range(CELLS):
        im = blank(MAPN, MAPN)
        im[0][0] = (0, 0, 0, 1); im[0][MAPN - 1] = (0, 0, 0, 1)          # pleine largeur : même avance que le plan
        cx, cy = int((i + 0.5) * MAPN / CELLS), int((j + 0.5) * MAPN / CELLS)
        for dy in range(-4, 5):
            for dx in range(-4, 5):
                d = max(abs(dx), abs(dy))
                if 0 <= cx + dx < MAPN and 0 <= cy + dy < MAPN and d <= 4:
                    im[cy + dy][cx + dx] = (255, 255, 255, 255) if d >= 3 else (230, 30, 30, 255)
        png_rgba(os.path.join(A, 'textures', 'font', 'gta_dot', f'{j}_{i}.png'), im)
        map_prov.append({"type": "bitmap", "file": f"mg:font/gta_dot/{j}_{i}.png", "ascent": 29, "height": 64, "chars": [chr(0xE500 + CELLS * j + i)]})
wjson(os.path.join(A, 'font', 'gta_map.json'), {"providers": map_prov})
