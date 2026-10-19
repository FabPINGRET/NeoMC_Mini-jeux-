# ------------------------------------------------------------------ Ombrelune : dragons articulés (un modèle par os)
# Exécuté par gen_rp.py (exec) après dino_rp.py (réutilise _tex et _uv) : données tools/arcade/ol_beasts.py.
# Os d'une espèce -> assets/mg/items/beast/<espèce>_<os>.json + modèle mg:item/beast/<espèce>_<os> (même convention que dino_rp.py).
import sys as _sys
_sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'arcade'))
import ol_beasts as _OB


for _sp in _OB.SPECIES.values():
    for _m, (_rgb, _pat, _blk) in _sp.mats.items():
        png_rgba(os.path.join(A, 'textures', 'item', 'beast', f'{_sp.key}_{_m}.png'), _tex(_rgb, _pat, zlib.crc32(f'{_sp.key}/{_m}'.encode())))
    for _b in _sp.bones:
        _s = _OB.bone_scale(_b)
        _els = []
        for (x1, y1, z1, x2, y2, z2, m) in _b.boxes:
            fx = (8 + 16 * x1 / _s, 8 + 16 * x2 / _s)
            fz = (8 + 16 * z1 / _s, 8 + 16 * z2 / _s)
            fy = (8 + 16 * y1 / _s, 8 + 16 * y2 / _s)
            dx, dy, dz = x2 - x1, y2 - y1, z2 - z1
            uvs = {'north': _uv(dx, dy), 'south': _uv(dx, dy), 'east': _uv(dz, dy), 'west': _uv(dz, dy), 'up': _uv(dx, dz), 'down': _uv(dx, dz)}
            _els.append({'from': [round(fx[0], 3), round(fy[0], 3), round(fz[0], 3)], 'to': [round(fx[1], 3), round(fy[1], 3), round(fz[1], 3)],
                         'faces': {d: {'texture': f'#{m}', 'uv': uv} for d, uv in uvs.items()}})
        _used = sorted({bx[6] for bx in _b.boxes})
        _name = f'beast/{_sp.key}_{_b.name}'
        wjson(os.path.join(A, 'models', 'item', _name + '.json'),
              {'textures': {**{m: f'mg:item/beast/{_sp.key}_{m}' for m in _used}, 'particle': f'mg:item/beast/{_sp.key}_{_used[0]}'},
               'elements': _els})
        wjson(os.path.join(A, 'items', _name + '.json'), {'model': {'type': 'minecraft:model', 'model': f'mg:item/{_name}'}})
