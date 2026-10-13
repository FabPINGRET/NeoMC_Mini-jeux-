# ------------------------------------------------------------------ Buffet du spawn : boissons et friandises des décors saisonniers
# Exécuté par gen_rp.py (exec) : utilise png, wjson, item_def, A, math, os. Posés par lobby/food_skin, food_halloween, food_noel.
FPAL = {'.': (0, 0, 0, 0), 'k': (40, 24, 16, 255), 'w': (250, 248, 240, 255), 'W': (220, 214, 200, 255), 'c': (160, 90, 40, 255),
        'L': (245, 240, 230, 255), 'l': (200, 192, 180, 255), 'o': (240, 130, 30, 255), 'O': (196, 92, 18, 255),
        'b': (120, 74, 40, 255), 'B': (92, 54, 28, 255), 'y': (255, 214, 60, 255),
        'g': (196, 222, 236, 255), 'G': (140, 170, 190, 255), 'e': (246, 228, 160, 255), 'E': (228, 200, 120, 255),
        'r': (214, 30, 40, 255), 'R': (120, 10, 20, 255)}
FOOD = {
    'pumpkin_latte': ['................',
                      '.......ww.......',
                      '.....wwcwww.....',
                      '....kwwwwcwk....',
                      '...kLLLLLLLLk...',
                      '...kllllllllk...',
                      '....koooooOk....',
                      '....koooooOk....',
                      '....kbbbbbBk....',
                      '....kbbyybBk....',
                      '....kbbbbbBk....',
                      '....koooooOk....',
                      '.....kooooOk....',
                      '.....kooooOk....',
                      '.....kkkkkk.....',
                      '................'],
    'eggnog': ['................',
               '..........c.....',
               '.........c......',
               '...GGGGGGcGG....',
               '...GwwwWwwwG....',
               '...GwWwwwWwGGG..',
               '...GeeeeeeeG.G..',
               '...GeeEeeeeG.G..',
               '...GeeeeeEeG.G..',
               '...GeEeeeeeGGG..',
               '...GeeeeeeeG....',
               '...GrrrrrrrG....',
               '...GeeeeEeeG....',
               '...GgggggggG....',
               '....GGGGGGG.....',
               '................'],
}
for _nm, _rows in FOOD.items():
    png(os.path.join(A, 'textures', 'item', _nm + '.png'), _rows, FPAL)
# sucre d'orge : crosse (demi-cercle) puis tige en diagonale, rayures rouges et blanches le long du tracé, liseré sombre
_path = [(7.5 + 3.5 * math.cos(math.pi - math.pi * i / 24), 5.0 - 3.5 * math.sin(math.pi * i / 24)) for i in range(25)]
_path = [(4.0, 6.5), (4.0, 6.0)] + _path + [(11.0 - 7.0 * i / 20, 5.0 + 9.5 * i / 20) for i in range(1, 21)]
_t = [0.0]
for (_x1, _y1), (_x2, _y2) in zip(_path, _path[1:]):
    _t.append(_t[-1] + math.hypot(_x2 - _x1, _y2 - _y1))
_cane = {}
for _y in range(16):
    for _x in range(16):
        _d, _i = min((math.hypot(_x + 0.5 - _px, _y + 0.5 - _py), _i) for _i, (_px, _py) in enumerate(_path))
        if _d <= 1.05:
            _cane[(_x, _y)] = 'r' if int(_t[_i] / 1.6) % 2 else 'w'
_rows = [''.join(_cane.get((_x, _y), 'R' if any((_x + _dx, _y + _dy) in _cane for _dx, _dy in ((1, 0), (-1, 0), (0, 1), (0, -1))) else '.')
                 for _x in range(16)) for _y in range(16)]
png(os.path.join(A, 'textures', 'item', 'candy_cane.png'), _rows, FPAL)
for _nm in list(FOOD) + ['candy_cane']:
    wjson(os.path.join(A, 'models', 'item', _nm + '.json'), {"parent": "minecraft:item/generated", "textures": {"layer0": f"mg:item/{_nm}"}})
    item_def(_nm, f'mg:item/{_nm}')
