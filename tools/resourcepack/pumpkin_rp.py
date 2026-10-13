# ------------------------------------------------------------------ Halloween : citrouilles colorées (décor tournant du spawn)
# Exécuté par gen_rp.py (exec) : utilise png, wjson, box, item_def, A, os.
# Peau en niveaux de gris teintée par dyed_color (tintindex 0) ; visage et tige non teintés.
# mg:pumpkin_lit (visage allumé) et mg:pumpkin_carved (visage creux) : posés par lobby/theme/halloween/pumpkin_*.
GREY = {str(i): (v, v, v, 255) for i, v in enumerate((150, 185, 215, 240, 255))}
png(os.path.join(A, 'textures', 'item', 'pumpkin_skin.png'),
    [''.join('0' if x % 4 == 0 else ('1' if x % 4 == 3 else ('3' if (x + y // 5) % 4 == 1 else '4')) for x in range(16)) for y in range(16)], GREY)
png(os.path.join(A, 'textures', 'item', 'pumpkin_top.png'),
    [''.join('0' if 6 <= x <= 9 and 6 <= y <= 9 else ('1' if (x - 7.5) ** 2 + (y - 7.5) ** 2 < 25 else '3') for x in range(16)) for y in range(16)], GREY)
png(os.path.join(A, 'textures', 'item', 'pumpkin_stem.png'),
    [''.join('g' if (x + y) % 3 else 'G' for x in range(16)) for y in range(16)], {'g': (96, 120, 40, 255), 'G': (64, 84, 28, 255)})
FACE = ['................',
        '................',
        '................',
        '..###......###..',
        '..####....####..',
        '..#####..#####..',
        '................',
        '.......##.......',
        '................',
        '.#............#.',
        '.##..##..##..##.',
        '..############..',
        '...##########...',
        '.....#....#.....',
        '................',
        '................']
for _nm, _col in (('lit', (255, 214, 60, 255)), ('carved', (34, 20, 10, 255))):
    png(os.path.join(A, 'textures', 'item', f'pumpkin_face_{_nm}.png'), FACE, {'.': (0, 0, 0, 0), '#': _col})
    _skin = box([1, 0, 1], [15, 14, 15], 's', True)
    _skin['faces']['up']['texture'] = _skin['faces']['down']['texture'] = '#t'
    wjson(os.path.join(A, 'models', 'item', f'pumpkin_{_nm}.json'), {
        "textures": {"s": "mg:item/pumpkin_skin", "t": "mg:item/pumpkin_top", "st": "mg:item/pumpkin_stem",
                     "f": f"mg:item/pumpkin_face_{_nm}", "particle": "mg:item/pumpkin_skin"},
        "elements": [_skin, box([7, 14, 7], [9, 17, 9], 'st'),
                     {"from": [1, 0, 0.9], "to": [15, 14, 0.9], "faces": {"north": {"texture": "#f", "uv": [1, 2, 15, 16]}}}],
        "display": {"gui": {"rotation": [30, 225, 0], "scale": [0.6, 0.6, 0.6]}}})
    item_def(f'pumpkin_{_nm}', f'mg:item/pumpkin_{_nm}', tint=-1)
