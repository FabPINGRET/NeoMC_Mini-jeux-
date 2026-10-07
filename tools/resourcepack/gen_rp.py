"""Génère le resource pack NeoMC (pixel art, kart 3D, boîtes ?) : python tools/resourcepack/gen_rp.py <racine du dépôt>.

Tout est dans l'espace de noms « mg » : aucune texture vanilla n'est remplacée (la survie n'est pas touchée).
Sortie : resourcepack/ (dossier) et releases/neomc_resourcepack.zip (+ empreinte SHA-1 affichée).
"""
import hashlib, json, os, struct, sys, zipfile, zlib

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
       't': (245, 220, 170, 255), 'n': (110, 70, 30, 255), 's': (255, 255, 255, 140)}

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
def item_def(name, model, tint=None):
    m = {"type": "minecraft:model", "model": model}
    if tint is not None: m["tints"] = [{"type": "minecraft:dye", "default": tint}]
    wjson(os.path.join(A, 'items', name + '.json'), {"model": m})

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
    "display": {"gui": {"rotation": [30, 225, 0], "translation": [0, 0, 0], "scale": [0.45, 0.45, 0.45]}}})
item_def('kart', 'mg:item/kart', tint=-1)

# ------------------------------------------------------------------ pack.mcmeta, zip
wjson(os.path.join(OUT, 'pack.mcmeta'), {"pack": {"description": [{"text": "NeoMC Mini-Jeux", "color": "gold"},
                                                                     {"text": "\nKart 3D, objets Mario Kart, boîtes ?", "color": "gray"}],
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
