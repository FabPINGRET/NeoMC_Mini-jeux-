"""Génère le resource pack NeoMC (pixel art, kart 3D, boîtes ?) : python tools/resourcepack/gen_rp.py <racine du dépôt>.

Tout est dans l'espace de noms « mg » : aucune texture vanilla n'est remplacée (la survie n'est pas touchée).
Sortie : resourcepack/ (dossier) et releases/neomc_resourcepack.zip (+ empreinte SHA-1 affichée).
"""
import hashlib, json, math, os, struct, sys, zipfile, zlib

R = sys.argv[1]
OUT = os.path.join(R, 'resourcepack')
A = os.path.join(OUT, 'assets', 'mg')

def wjson(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(obj, f, indent=2, ensure_ascii=False); f.write('\n')

def png(path, rows, pal):
    """rows : 16 chaînes de 16 caractères, pal : caractère -> (r, g, b, a)."""
    h, w = len(rows), len(rows[0])
    raw = b''.join(bytes([0]) + b''.join(bytes(pal[c]) for c in row) for row in rows)
    def chunk(t, d): return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb') as f:
        f.write(bytes([137, 80, 78, 71, 13, 10, 26, 10]) + chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 6, 0, 0, 0))
                + chunk(b'IDAT', zlib.compress(raw, 9)) + chunk(b'IEND', b''))

PAL = {'.': (0, 0, 0, 0), ' ': (0, 0, 0, 0), 'k': (20, 20, 24, 255), 'w': (250, 250, 250, 255), 'l': (190, 190, 196, 255), 'd': (90, 90, 98, 255),
       'y': (255, 222, 40, 255), 'Y': (196, 150, 20, 255), 'o': (255, 150, 30, 255), 'O': (200, 90, 10, 255),
       'r': (226, 40, 40, 255), 'R': (140, 16, 16, 255), 'g': (60, 200, 60, 255), 'G': (20, 120, 30, 255),
       'b': (60, 120, 255, 255), 'B': (20, 50, 170, 255), 'c': (120, 230, 255, 255), 'p': (170, 80, 220, 255), 'P': (90, 30, 140, 255),
       't': (245, 220, 170, 255), 'n': (110, 70, 30, 255), 'N': (70, 42, 18, 255), 's': (255, 255, 255, 140)}

def pad(rows):
    rows = [r.ljust(16, '.')[:16] for r in rows]
    while len(rows) < 16: rows.append('.' * 16)
    return rows[:16]

SPRITES = {
    'banana': ['', '          nn', '         yyY', '        yyyY', '       yyyYY', '      yyyyY', '     yyyyY', '    yyyyY', '   yyyyY',
               '  yyyyYY', ' yyyyY', ' yyyY', '  YYY'],
    'shell': ['', '', '     GGGGGG', '    GgggggGG', '   GgwgggwggG', '  GggggggggggG', '  GgggwgggwggG', '  GgggggggggGG',
              '  wwwwwwwwwwww', '  wttttttttttw', '   wwwwwwwwww'],
    'shell_red': ['', '', '     RRRRRR', '    RrrrrrRR', '   RrwrrrwrrR', '  RrrrrrrrrrrR', '  RrrrwrrrwrrR', '  RrrrrrrrrrRR',
                  '  wwwwwwwwwwww', '  wttttttttttw', '   wwwwwwwwww'],
    'shell_blue': ['', '    w  w  w', '   BwBBwBBwB', '   BbbbbbbbbB', '  BbwbbbbbwbbB', '  BbbbbbbbbbbB', ' wBbbbwbbbwbbBw', '  BbbbbbbbbbBB',
                   '  wwwwwwwwwwww', '  wccccccccccw', '   wwwwwwwwww'],
    'mushroom': ['', '     rrrrrr', '   rrwwrrrrrr', '  rrwwwrrrwwrr', '  rrrwrrrrwwwr', ' rrrrrrrrrrwrrr', ' rwwrrrrrrrrrrr', ' rwwwrrrwwrrrrr',
                 ' rrrrrrrwwrrrrr', '   tttttttttt', '   ttkttttktt', '   ttkttttktt', '   tttttttttt', '    tttttttt'],
    'mushroom_gold': ['', '     yyyyyy', '   yywwyyyyyy', '  yywwwyyywwyy', '  yyywyyyywwwy', ' yyyyyyyyyywyyy', ' ywwyyyyyyyyyyy', ' ywwwyyywwyyyyy',
                      ' yyyyyyywwyyyyy', '   oooooooooo', '   ookooooko', '   ookooooko', '   oooooooooo', '    oooooooo'],
    'mushroom_mega': ['     RRRRRR', '   RRrrrrrrRR', '  RrrwwrrrrrrR', ' RrrwwwrrrwwrrR', ' RrrrwrrrrwwwrR', 'RrrrrrrrrrrwrrrR', 'RrwwrrrrrrrrrrrR',
                      'RrwwwrrrwwrrrrrR', ' RRRRRRRRRRRRRR', '   tttttttttt', '   ttkttttktt', '   ttkttttktt', '   tttttttttt', '    tttttttt'],
    'star': ['       y', '      yyy', '      yyy', '     yyyyy', 'yyyyyyyyyyyyyyy', ' yyyyyyyyyyyyy', '  yyyykyykyyy', '   yyykyykyy',
             '   yyyyyyyyy', '  yyyyyyyyyyy', '  yyyyy yyyyy', ' yyyy     yyyy', ' yyy       yyy', 'yy           yy'],
    'lightning': ['        yyyy', '       yyyY', '      yyyY', '     yyyY', '    yyyY', '   yyyyyyyy', '      yyyY', '     yyyY', '    yyyY',
                  '   yyyY', '  yyyY', ' yyY', ' yY'],
    'bobomb': ['          oO', '         o', '        dd', '      kkkkk', '    kkkkkkkkk', '   kkkkkkkkkkk', '  kkkwkkkwkkkk', '  kkkwkkkwkkkkl',
               '  kkkkkkkkkkkll', '  kkkkkkkkkkkkl', '   kkkkkkkkkkk', '    kkkkkkkkk', '     tt   tt', '    ttt   ttt'],
    'bullet': ['', '', '', '    kkkkkkkk', '  kkkkkkkkkkdd', ' kkkwwkkkkkkddl', 'kkkkwkkkkkkkddl', 'kkkkkkkkkkkkddl', 'kkkrrrrrkkkkddl',
               ' kkkkkkkkkkkddl', '  kkkkkkkkkkdd', '    kkkkkkkk'],
    'blooper': ['      wwww', '     wwwwww', '    wwwwwwww', '    wkwwwwkw', '    wkwwwwkw', '    wwwwwwww', '    wwwwwwww', '     wwwwww',
                '    w w ww w', '    w w ww w', '   w  w  w  w', '   w  w  w  w', '  w   w  w   w'],
    'horn': ['', '', '            yy', '          yyyy', '        yyyyyY', '  ooooyyyyyyyY', ' oOOOOyyyyyyyY', ' oOOOOyyyyyyyY', '  ooooyyyyyyyY',
             '        yyyyyY', '          yyyy', '            yy'],
    'boo': ['', '     wwwwww', '   wwwwwwwwww', '  wwkkwwwwkkww', '  wwkkwwwwkkww', ' wwwwwwwwwwwwww', ' wwwwrrrrrrwwww', ' wwwwrrrrrrwwww',
            ' wwwwwwwwwwwwww', '  wwwwwwwwwwww', '  ww wwwwww ww', '   w  wwww  w'],
    'dice': ['', ' wwwwwwwwwwwwww', ' wwwwwwwwwwwwlw', ' wwkkwwwwwwkklw', ' wwkkwwwwwwkklw', ' wwwwwwwwwwwwlw', ' wwwwwwkkwwwwlw', ' wwwwwwkkwwwwlw',
             ' wwwwwwwwwwwwlw', ' wwkkwwwwwwkklw', ' wwkkwwwwwwkklw', ' wwwwwwwwwwwwlw', ' wllllllllllllw', ' wwwwwwwwwwwwww'],
}
for name, rows in SPRITES.items():
    png(os.path.join(A, 'textures', 'item', name + '.png'), pad(rows), PAL)

# boîte ? : bordure arc-en-ciel, point d'interrogation blanc
rainbow = [(255, 60, 60, 255), (255, 160, 40, 255), (255, 230, 50, 255), (80, 220, 80, 255), (70, 170, 255, 255), (170, 90, 255, 255)]
pal_box = dict(PAL)
box_rows = []
for y in range(16):
    row = ''
    for x in range(16):
        edge = x in (0, 15) or y in (0, 15)
        row += str((x + y) // 3 % 6) if edge else 's'
    box_rows.append(row)
q = ['', '', '', '      wwww', '     ww  ww', '         ww', '        ww', '       ww', '       ww', '', '       ww', '       ww']
for y, line in enumerate(pad(q)):
    box_rows[y] = ''.join('w' if c == 'w' else box_rows[y][x] for x, c in enumerate(line))
for i, c in enumerate(rainbow): pal_box[str(i)] = c
pal_box['s'] = (255, 255, 255, 90)
png(os.path.join(A, 'textures', 'item', 'item_box.png'), box_rows, pal_box)

# textures du kart : carrosserie blanche (teinte du pilote), pneus, siège, métal
def solid(c1, c2):
    return [''.join('a' if (x + y) % 7 else 'b' for x in range(16)) for y in range(16)], {'a': c1, 'b': c2}
for name, (c1, c2) in {'kart_body': ((245, 245, 245, 255), (220, 220, 220, 255)), 'kart_seat': ((45, 45, 52, 255), (30, 30, 36, 255)),
                       'kart_metal': ((200, 200, 210, 255), (160, 160, 170, 255))}.items():
    rows, pal = solid(c1, c2)
    png(os.path.join(A, 'textures', 'item', name + '.png'), rows, pal)
tire = [''.join('h' if 5 <= x <= 10 and 5 <= y <= 10 else ('g' if (x + y) % 4 == 0 else 'k') for x in range(16)) for y in range(16)]
png(os.path.join(A, 'textures', 'item', 'kart_wheel.png'), tire, {'h': (180, 180, 190, 255), 'g': (50, 50, 55, 255), 'k': (20, 20, 22, 255)})

# ------------------------------------------------------------------ modèles
def item_def(name, model, tint=None, oversized=False):
    m = {"type": "minecraft:model", "model": model}
    if tint is not None: m["tints"] = [{"type": "minecraft:dye", "default": tint}]
    d = {"model": m}
    if oversized: d["oversized_in_gui"] = True       # aperçu en grand dans les fenêtres de choix du kart
    wjson(os.path.join(A, 'items', name + '.json'), d)

FLAT = {'banana': 'banana', 'shell_green': 'shell', 'shell_red': 'shell_red', 'shell_blue': 'shell_blue', 'mushroom': 'mushroom',
        'mushroom_gold': 'mushroom_gold', 'mushroom_mega': 'mushroom_mega', 'star': 'star', 'lightning': 'lightning', 'bobomb': 'bobomb',
        'bullet': 'bullet', 'blooper': 'blooper', 'horn': 'horn', 'boo': 'boo', 'dice': 'dice'}
for name, tex in FLAT.items():
    wjson(os.path.join(A, 'models', 'item', name + '.json'), {"parent": "minecraft:item/generated", "textures": {"layer0": f"mg:item/{tex}"}})
    item_def(name, f'mg:item/{name}')
# boîte ? : un cube (faces identiques)
wjson(os.path.join(A, 'models', 'item', 'item_box.json'), {"parent": "minecraft:block/cube_all", "textures": {"all": "mg:item/item_box"}})
item_def('item_box', 'mg:item/item_box')

# kart 3D (16 unités = 1 bloc, avant vers +z) ; la carrosserie (#body, tintindex 0) prend la couleur du pilote
def box(fr, to, tex, tint=False):
    faces = {d: {"texture": f"#{tex}", **({"tintindex": 0} if tint else {})} for d in ('north', 'south', 'east', 'west', 'up', 'down')}
    return {"from": fr, "to": to, "faces": faces}
elements = [
    box([2, 2, -2], [14, 6, 18], 'body', True),            # coque
    box([4, 2, 18], [12, 5, 21], 'body', True),            # nez
    box([2, 1, 21], [14, 3, 23], 'metal'),                 # pare-chocs
    box([3, 6, 14], [13, 7, 19], 'body', True),            # capot
    box([4, 5, 6], [12, 7, 11], 'seat'),                   # siège (sous la tête du pilote)
    box([4, 7, 4], [12, 13, 6], 'seat'),                   # dossier
    box([7, 6, 13], [9, 10, 15], 'metal'),                 # colonne de direction
    box([5, 10, 13], [11, 11.5, 15], 'seat'),              # volant
    box([-1, 0, 13], [3, 5, 18], 'wheel'), box([13, 0, 13], [17, 5, 18], 'wheel'),   # roues avant
    box([-1, 0, -2], [3, 5, 4], 'wheel'), box([13, 0, -2], [17, 5, 4], 'wheel'),     # roues arrière
    box([3, 9, -4], [13, 10, -1], 'body', True),           # aileron
    box([4, 6, -3], [5, 9, -2], 'metal'), box([11, 6, -3], [12, 9, -2], 'metal'),    # montants de l'aileron
    box([4, 3, -5], [6, 5, -2], 'metal'), box([10, 3, -5], [12, 5, -2], 'metal'),    # pots d'échappement
]
wjson(os.path.join(A, 'models', 'item', 'kart.json'), {
    "textures": {"body": "mg:item/kart_body", "seat": "mg:item/kart_seat", "metal": "mg:item/kart_metal", "wheel": "mg:item/kart_wheel",
                 "particle": "mg:item/kart_body"},
    "elements": elements,
    "display": {"gui": {"rotation": [25, 210, 0], "translation": [0, -1, 0], "scale": [1.6, 1.6, 1.6]}}})
item_def('kart', 'mg:item/kart', tint=-1, oversized=True)
KTEX = {"body": "mg:item/kart_body", "seat": "mg:item/kart_seat", "metal": "mg:item/kart_metal", "wheel": "mg:item/kart_wheel", "particle": "mg:item/kart_body"}
KDISP = {"gui": {"rotation": [25, 210, 0], "translation": [0, -1, 0], "scale": [1.6, 1.6, 1.6]}}
VARIANTS = {
    # Bolide : long et bas, nez pointu, grand aileron, gros pots
    'kart_bolide': [
        box([3, 2, -3], [13, 5, 19], 'body', True), box([5, 2, 19], [11, 4, 23], 'body', True), box([6, 2, 23], [10, 3, 25], 'metal'),
        box([4, 5, 13], [12, 6, 19], 'body', True), box([5, 4, 2], [11, 6, 7], 'seat'), box([5, 6, 1], [11, 11, 3], 'seat'),
        box([7, 5, 12], [9, 9, 14], 'metal'), box([5, 9, 12], [11, 10.5, 14], 'seat'),
        box([0, 0, 14], [3, 4, 19], 'wheel'), box([13, 0, 14], [16, 4, 19], 'wheel'),
        box([-1, 0, -3], [3, 5, 3], 'wheel'), box([13, 0, -3], [17, 5, 3], 'wheel'),
        box([1, 10, -6], [15, 11, -2], 'body', True), box([1, 7, -6], [2, 11, -2], 'body', True), box([14, 7, -6], [15, 11, -2], 'body', True),
        box([4, 6, -4], [5, 10, -3], 'metal'), box([11, 6, -4], [12, 10, -3], 'metal'),
        box([3, 2, -6], [6, 5, -3], 'metal'), box([10, 2, -6], [13, 5, -3], 'metal')],
    # Mini : court, haut et rond, grosses roues
    'kart_mini': [
        box([3, 2, 0], [13, 8, 15], 'body', True), box([4, 8, 9], [12, 9, 15], 'body', True), box([4, 2, 15], [12, 6, 17], 'metal'),
        box([5, 7, 2], [11, 9, 7], 'seat'), box([5, 9, 1], [11, 14, 3], 'seat'),
        box([7, 8, 10], [9, 12, 12], 'metal'), box([5, 12, 10], [11, 13.5, 12], 'seat'),
        box([-1, 0, 10], [3, 6, 16], 'wheel'), box([13, 0, 10], [17, 6, 16], 'wheel'),
        box([-1, 0, -1], [3, 6, 5], 'wheel'), box([13, 0, -1], [17, 6, 5], 'wheel'),
        box([7, 4, -2], [9, 6, 0], 'metal')],
    # Costaud : large et massif, pare-buffle, roues de tracteur
    'kart_costaud': [
        box([0, 3, -3], [16, 8, 19], 'body', True), box([1, 3, 19], [15, 7, 22], 'body', True), box([-1, 2, 22], [17, 6, 24], 'metal'),
        box([1, 8, 12], [15, 9, 19], 'body', True), box([4, 7, 1], [12, 10, 7], 'seat'), box([4, 10, 0], [12, 16, 3], 'seat'),
        box([7, 8, 11], [9, 12, 13], 'metal'), box([4, 12, 11], [12, 13.5, 13], 'seat'),
        box([-4, 0, 12], [0, 7, 19], 'wheel'), box([16, 0, 12], [20, 7, 19], 'wheel'),
        box([-4, 0, -3], [0, 7, 5], 'wheel'), box([16, 0, -3], [20, 7, 5], 'wheel'),
        box([1, 8, -4], [3, 18, -2], 'metal'), box([13, 8, -4], [15, 18, -2], 'metal'),
        box([0, 9, 17], [2, 11, 19], 'metal'), box([14, 9, 17], [16, 11, 19], 'metal')],
}
for name, els in VARIANTS.items():
    wjson(os.path.join(A, 'models', 'item', name + '.json'), {"textures": KTEX, "elements": els, "display": KDISP})
    item_def(name, f'mg:item/{name}', tint=-1, oversized=True)

# ------------------------------------------------------------------ portraits des karts (police mg:kart) pour les fenêtres de choix
# Rendu maison en vue 3/4 avant (faces +x, +y, +z visibles), algorithme du peintre, contours foncés.
# Caractère  + 16 * type + couleur (type 0..3, couleur 0..7) ; police mg:kart (72 px) et mg:kartxl (128 px).
KCOLS = [(229, 57, 53), (41, 98, 255), (100, 221, 23), (255, 214, 0), (142, 36, 170), (255, 109, 0), (0, 184, 212), (255, 64, 129)]
FLATC = {'seat': (48, 48, 56), 'metal': (196, 196, 206), 'wheel': (30, 30, 34)}
PORTRAITS = [('kart', elements)] + list(VARIANTS.items())
PS = 3.0
def proj(x, y, z):
    return ((x - z) * 0.866 * PS, ((x + z) * 0.5 - y) * PS)
def faces_of(el):
    (x1, y1, z1), (x2, y2, z2) = el['from'], el['to']
    return [((x1, y2, z1), (x2, y2, z1), (x2, y2, z2), (x1, y2, z2), 1.0),     # dessus
            ((x2, y1, z1), (x2, y2, z1), (x2, y2, z2), (x2, y1, z2), 0.72),    # côté +x
            ((x1, y1, z2), (x2, y1, z2), (x2, y2, z2), (x1, y2, z2), 0.86)]    # avant +z
allp = [proj(*p) for _, els in PORTRAITS for el in els for f in faces_of(el) for p in f[:4]]
PX0, PY0 = min(p[0] for p in allp) - 3, min(p[1] for p in allp) - 3
PW, PH = int(max(p[0] for p in allp) - PX0) + 4, int(max(p[1] for p in allp) - PY0) + 4
def render(els, tint):
    img = [[(0, 0, 0, 0)] * PW for _ in range(PH)]
    order = sorted(els, key=lambda e: sum(e['from']) + sum(e['to']))
    for el in order:
        tex = el['faces']['north']['texture'][1:]
        base = tint if tex == 'body' else FLATC.get(tex, (200, 200, 200))
        for *quad, shade in faces_of(el):
            pts = [(proj(*p)[0] - PX0, proj(*p)[1] - PY0) for p in quad]
            col = tuple(min(255, int(c * shade)) for c in base) + (255,)
            edge = tuple(int(c * shade * 0.45) for c in base) + (255,)
            xs, ys = [p[0] for p in pts], [p[1] for p in pts]
            for py in range(max(0, int(min(ys))), min(PH, int(max(ys)) + 1)):
                for px in range(max(0, int(min(xs))), min(PW, int(max(xs)) + 1)):
                    cx, cy = px + 0.5, py + 0.5
                    sgn, inside, near = 0, True, False
                    for k in range(4):
                        ax, ay = pts[k]; bx, by = pts[(k + 1) % 4]
                        cr = (bx - ax) * (cy - ay) - (by - ay) * (cx - ax)
                        if abs(cr) > 1e-9:
                            if sgn == 0: sgn = 1 if cr > 0 else -1
                            elif (cr > 0) != (sgn > 0): inside = False; break
                        ln = math.hypot(bx - ax, by - ay) or 1
                        if abs(cr) / ln < 0.9: near = True
                    if inside: img[py][px] = edge if near else col
    return img
def png_rgba(path, img):
    h, w = len(img), len(img[0])
    raw = b''.join(bytes([0]) + b''.join(bytes(p) for p in row) for row in img)
    def chunk(t, d): return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(t + d) & 0xffffffff)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb') as f:
        f.write(bytes([137, 80, 78, 71, 13, 10, 26, 10]) + chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 6, 0, 0, 0))
                + chunk(b'IDAT', zlib.compress(raw, 9)) + chunk(b'IEND', b''))
prov_s, prov_l = [], []
for t, (name, els) in enumerate(PORTRAITS):
    for k, rgb in enumerate(KCOLS):
        png_rgba(os.path.join(A, 'textures', 'font', f'kart_{t}_{k}.png'), render(els, rgb))
        ch = chr(0xE000 + 16 * t + k)
        prov_s.append({"type": "bitmap", "file": f"mg:font/kart_{t}_{k}.png", "ascent": 60, "height": 72, "chars": [ch]})
        prov_l.append({"type": "bitmap", "file": f"mg:font/kart_{t}_{k}.png", "ascent": 110, "height": 128, "chars": [ch]})
wjson(os.path.join(A, 'font', 'kart.json'), {"providers": prov_s + [{"type": "space", "advances": {" ": 14}}]})
wjson(os.path.join(A, 'font', 'kartxl.json'), {"providers": prov_l + [{"type": "space", "advances": {" ": 14}}]})
print('portraits', PW, 'x', PH)
# ballon de bataille (teinté à la couleur du kart)
bal_rows = [''.join('w' if (x - 6) ** 2 + (y - 5) ** 2 <= 3 else 'b' for x in range(16)) for y in range(16)]
png(os.path.join(A, 'textures', 'item', 'balloon.png'), bal_rows, {'w': (255, 255, 255, 255), 'b': (225, 225, 225, 255)})
png(os.path.join(A, 'textures', 'item', 'balloon_string.png'), ['w' * 16] * 16, {'w': (240, 240, 240, 255)})
wjson(os.path.join(A, 'models', 'item', 'balloon.json'), {
    "textures": {"b": "mg:item/balloon", "s": "mg:item/balloon_string", "particle": "mg:item/balloon"},
    "elements": [box([4, 8, 4], [12, 18, 12], 'b', True), box([5, 7, 5], [11, 19, 11], 'b', True), box([3, 9, 5], [13, 17, 11], 'b', True),
                 box([5, 9, 3], [11, 17, 13], 'b', True), box([7, 6, 7], [9, 7, 9], 'b', True), box([7.5, -6, 7.5], [8.5, 6, 8.5], 's')],
    "display": {"gui": {"rotation": [0, 0, 0], "scale": [0.6, 0.6, 0.6]}}})
item_def('balloon', 'mg:item/balloon', tint=-6265536)

# ------------------------------------------------------------------ dangers du Royaume Koopa (modèles 3D, devant vers +z)
HZ_TEX = {
    'thwomp_side': ['dddddddddddddddd', 'dllllllllllllld', 'dlldllllllldlld', 'dllllllllllllld', 'dllllldlllllllld', 'dllllllllllllld',
                    'dlllllllllldllld', 'dllldllllllllld', 'dllllllllllllld', 'dllllllldllllld', 'dldllllllllllld', 'dllllllllllllld',
                    'dlllldlllllldld', 'dllllllllllllld', 'dllllllllllllld', 'dddddddddddddddd'],
    'thwomp_face': ['dddddddddddddddd', 'dllllllllllllld', 'dlkkkllllllkkkld', 'dllkkkllllkkklld', 'dlllwwkllkwwllld', 'dlllwkkllkkwllld',
                    'dllllllllllllld', 'dllllllllllllld', 'dlkkkkkkkkkkkkld', 'dlkwkwkwkwkwkkld', 'dlkkkkkkkkkkkkld', 'dlkwkwkwkwkwkkld',
                    'dlkkkkkkkkkkkkld', 'dllllllllllllld', 'dllllllllllllld', 'dddddddddddddddd'],
    'piranha_head': ['rrrrrrrrrrrrrrrr', 'rrwwrrrrrrrwwrrr', 'rwwwrrrrrrwwwwrr', 'rrwrrrrrrrrwwrrr', 'rrrrrrwwrrrrrrrr', 'rrrrrwwwwrrrrrrr',
                     'rrrrrrwwrrrrrrwr', 'rwwrrrrrrrrrwwwr', 'wwwwrrrrrrrrrwrr', 'rwwrrrrwwrrrrrrr', 'rrrrrrwwwwrrrrrr', 'rrrrrrrwwrrrrrrr',
                     'rrwwrrrrrrrrwwrr', 'rwwwwrrrrrrwwwwr', 'rrwwrrrrrrrrwwrr', 'rrrrrrrrrrrrrrrr'],
    'piranha_mouth': ['rrrrrrrrrrrrrrrr', 'rrrwwwwwwwwwwrrr', 'rrwwwwwwwwwwwwrr', 'rwwkkkkkkkkkkwwr', 'rwkwkwkwkwkwkkwr', 'rwkkkkkkkkkkkkwr',
                      'rwkkkkRRRRkkkkwr', 'rwkkkRRRRRRkkkwr', 'rwkkkkRRRRkkkkwr', 'rwkkkkkkkkkkkkwr', 'rwkwkwkwkwkwkkwr', 'rwwkkkkkkkkkkwwr',
                      'rrwwwwwwwwwwwwrr', 'rrrwwwwwwwwwwrrr', 'rrrrrrrrrrrrrrrr', 'rrrrrrrrrrrrrrrr'],
    'stem': ['gGgGgGgGgGgGgGgG'] * 16,
    'goomba_head': ['nnnnnnnnnnnnnnnn', 'nnnnNnnnnnnnNnnn', 'nnnnnnnnnnnnnnnn', 'nNnnnnnnnnnNnnnn', 'nnnnnnnnnnnnnnnn', 'nnnnnnnNnnnnnnnn',
                    'nnnnnnnnnnnnnnNn', 'nnnNnnnnnnnnnnnn', 'nnnnnnnnnnnnnnnn', 'nnnnnnnnnNnnnnnn', 'nnnnnnnnnnnnnnnn', 'nNnnnnnnnnnnnnnn',
                    'nnnnnnnnnnnNnnnn', 'nnnnnNnnnnnnnnnn', 'nnnnnnnnnnnnnnnn', 'nnnnnnnnnnnnnnnn'],
    'goomba_face': ['nnnnnnnnnnnnnnnn', 'nnkknnnnnnnnkknn', 'nnnkkknnnnkkknnn', 'nnnnwwkkkkwwnnnn', 'nnnnwkknnkkwnnnn', 'nnnnwkknnkkwnnnn',
                    'nnnnwwwnnwwwnnnn', 'nnnnnnnnnnnnnnnn', 'ttttttttttttttttt', 'ttttttttttttttttt', 'ttwttttttttttwtt', 'ttwwttttttttwwtt',
                    'tttttkkkkkkttttt', 'ttttttttttttttttt', 'ttttttttttttttttt', 'ttttttttttttttttt'],
    'goomba_body': ['tttttttttttttttt'] * 16,
    'goomba_feet': ['kkkkkkkkkkkkkkkk', 'kNkkkkkkkkkkkNkk'] * 8,
    'pokey_body': ['yyyyyyyyyyyyyyyy', 'yykyyyyyyyykyyyy', 'yyyyyyykyyyyyyyy', 'yyyyyyyyyyyyyyky', 'ykyyyyyyyyyyyyyy', 'yyyyyykyyyyyyyyy',
                   'yyyyyyyyyyyykyyy', 'yyykyyyyyyyyyyyy', 'yyyyyyyyykyyyyyy', 'yyyyyyyyyyyyyyyy', 'ykyyyyyyyyyyykyy', 'yyyyyykyyyyyyyyy',
                   'yyyyyyyyyyyyyyyy', 'yyykyyyyyykyyyyy', 'yyyyyyyyyyyyyyyy', 'yyyyyyyyyyyyyyyy'],
    'pokey_face': ['yyyyyyyyyyyyyyyy', 'yyyyyyyyyyyyyyyy', 'yyyyyyyyyyyyyyyy', 'yyykkyyyyyykkyyy', 'yyykkyyyyyykkyyy', 'yyykkyyyyyykkyyy',
                   'yyyyyyyyyyyyyyyy', 'yyyyyyyyyyyyyyyy', 'yyyyyyyyyyyyyyyy', 'yyyyykkkkkkyyyyy', 'yyyykyyyyyykyyyy', 'yyyyyyyyyyyyyyyy',
                   'yyyyyyyyyyyyyyyy', 'yyyyyyyyyyyyyyyy', 'yyyyyyyyyyyyyyyy', 'yyyyyyyyyyyyyyyy'],
    'pokey_flower': ['ooooyyyyyyyyoooo'] * 16,
    'chomp_side': ['kkkkkkkkkkkkkkkk', 'kkkkkkkkkkkkkkkk', 'kkdddkkkkkkkkkkk', 'kkddkkkkkkkkkkkk', 'kkdkkkkkkkkkkkkk', 'kkkkkkkkkkkkkkkk',
                   'kkkkkkkkkkkkkkkk', 'kkkkkkkkkkkkkkkk', 'kkkkkkkkkkkkkkkk', 'kkkkkkkkkkkkkkkk', 'kkkkkkkkkkkkkkkk', 'kkkkkkkkkkkkkkkk',
                   'kkkkkkkkkkkkkkkk', 'kkkkkkkkkkkkkkkk', 'kkkkkkkkkkkkkkkk', 'kkkkkkkkkkkkkkkk'],
    'chomp_face': ['kkkkkkkkkkkkkkkk', 'kkwwwkkkkkkwwwkk', 'kwwwwwkkkkwwwwwk', 'kwwkkwkkkkwkkwwk', 'kwwkkwkkkkwkkwwk', 'kkwwwkkkkkkwwwkk',
                   'kkkkkkkkkkkkkkkk', 'kwwwwwwwwwwwwwwk', 'kwkwkwkwkwkwkwwk', 'kRRRRRRRRRRRRRRk', 'kRRRrrrrrrrrRRRk', 'kRRRRRRRRRRRRRRk',
                   'kwkwkwkwkwkwkwwk', 'kwwwwwwwwwwwwwwk', 'kkkkkkkkkkkkkkkk', 'kkkkkkkkkkkkkkkk'],
}
for name, rows in HZ_TEX.items():
    png(os.path.join(A, 'textures', 'item', name + '.png'), pad([r[:16] for r in rows]), PAL)
SPR2 = {
    'cheep': ['', '', '    ww', '   rrrrr    rr', '  rrrrrrr  rrr', ' rrwkrrrrrrrrr', ' rrkkrrrrrrrrr', ' rrrrrrrrrrrr', ' wwrrrrrrr rrr',
              '  wwrrrrr   rr', '   wwwww', '    ww'],
    'podoboo': ['', '     oooo', '   ooyyyyoo', '  oyyyyyyyyo', '  oyywkyywkyo', ' oyyykkyykkyyo', ' oyyyyyyyyyyyo', ' oyyyyyyyyyyyo', '  oyyyyyyyyyo',
                '  ooyyyyyyoo', '   oorrrroo', '    rr  rr', '   r  rr  r'],
}
for name, rows in SPR2.items():
    png(os.path.join(A, 'textures', 'item', name + '.png'), pad(rows), PAL)
    wjson(os.path.join(A, 'models', 'item', name + '.json'), {"parent": "minecraft:item/generated", "textures": {"layer0": f"mg:item/{name}"}})
    item_def(name, f'mg:item/{name}')

def ebox(fr, to, tex, front=None):
    faces = {d: {"texture": f"#{front if (front and d == 'south') else tex}", "uv": [0, 0, 16, 16]} for d in ('north', 'south', 'east', 'west', 'up', 'down')}
    return {"from": fr, "to": to, "faces": faces}
HZ_MODELS = {
    'thwomp': ({'s': 'thwomp_side', 'f': 'thwomp_face'},
               [ebox([0, 0, 0], [16, 16, 16], 's', 'f')] +
               [ebox([x, 16, z], [x + 3, 19, z + 3], 's') for x in (1, 6.5, 12) for z in (1, 12)] +
               [ebox([-3, y, 6.5], [0, y + 3, 9.5], 's') for y in (3, 10)] + [ebox([16, y, 6.5], [19, y + 3, 9.5], 's') for y in (3, 10)]),
    'piranha': ({'h': 'piranha_head', 'm': 'piranha_mouth', 'g': 'stem'},
                [ebox([2, 5, 2], [14, 16, 14], 'h', 'm'), ebox([3, 4, 13], [13, 14, 15], 'm'), ebox([7, -10, 7], [9, 5, 9], 'g'),
                 ebox([0, -6, 7], [7, -5, 11], 'g'), ebox([9, -4, 5], [16, -3, 9], 'g')]),
    'goomba': ({'h': 'goomba_head', 'f': 'goomba_face', 'b': 'goomba_body', 'k': 'goomba_feet'},
               [ebox([0, 7, 0], [16, 14, 16], 'h'), ebox([2, 3, 2], [14, 8, 14], 'b', 'f'), ebox([1, 14, 1], [15, 16, 15], 'h'),
                ebox([2, 0, 3], [7, 3, 11], 'k'), ebox([9, 0, 3], [14, 3, 11], 'k')]),
    'pokey': ({'b': 'pokey_body', 'f': 'pokey_face', 'o': 'pokey_flower'},
              [ebox([3, 0, 3], [13, 9, 13], 'b'), ebox([3, 9, 3], [13, 18, 13], 'b'), ebox([2, 18, 2], [14, 29, 14], 'b', 'f'),
               ebox([6, 29, 6], [10, 31, 10], 'o')]),
    'chomp': ({'s': 'chomp_side', 'f': 'chomp_face'}, [ebox([0, 0, 0], [16, 16, 16], 's', 'f')]),
}
for name, (texs, els) in HZ_MODELS.items():
    wjson(os.path.join(A, 'models', 'item', name + '.json'),
          {"textures": {**{k: f"mg:item/{v}" for k, v in texs.items()}, "particle": f"mg:item/{list(texs.values())[0]}"}, "elements": els,
           "display": {"gui": {"rotation": [30, 225, 0], "scale": [0.5, 0.5, 0.5]}}})
    item_def(name, f'mg:item/{name}')

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lobby_rp.py'), encoding='utf-8').read())
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'guns_rp.py'), encoding='utf-8').read())

# ------------------------------------------------------------------ pack.mcmeta, zip
wjson(os.path.join(OUT, 'pack.mcmeta'), {"pack": {"description": [{"text": "NeoMC Mini-Jeux", "color": "gold"},
                                                                     {"text": "\nKart 3D, objets Mario Kart, spawn", "color": "gray"}],
                                                  "min_format": [88, 0], "max_format": [88, 99]}})
z = os.path.join(R, 'releases', 'neomc_resourcepack.zip')
os.makedirs(os.path.dirname(z), exist_ok=True)
with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, _, files in os.walk(OUT):
        for f in sorted(files):
            p = os.path.join(root, f)
            info = zipfile.ZipInfo(os.path.relpath(p, OUT).replace(os.sep, '/'), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, open(p, 'rb').read())
sha = hashlib.sha1(open(z, 'rb').read()).hexdigest()
print('resource pack :', z, '| sha1', sha, '|', os.path.getsize(z), 'octets')
