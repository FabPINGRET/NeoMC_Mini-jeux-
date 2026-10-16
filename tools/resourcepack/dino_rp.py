# ------------------------------------------------------------------ Terra Nova : dinosaures articulés (un modèle par os)
# Exécuté par gen_rp.py (exec) : utilise wjson, png_rgba, A, os. Données : tools/arcade/tv_dinos.py.
# Os d'une espèce -> assets/mg/items/dino/<espèce>_<os>.json + modèle mg:item/dino/<espèce>_<os> (articulation au centre 8,8,8,
# échelle réduite de bone_scale ; vérifié en jeu : l'item_display affiche le modèle sans le retourner).
import random as _rnd
import sys as _sys
_sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'arcade'))
import tv_dinos as _TD


def _clamp(v):
    return max(0, min(255, int(v)))


def _tex(rgb, pat, seed):
    r = _rnd.Random(seed)
    R, G, B = rgb
    img = []
    for y in range(16):
        row = []
        for x in range(16):
            k = 1 + r.uniform(-0.09, 0.09)
            if pat == 'scales':
                if (x + 2 * (y // 3)) % 4 == 0 and y % 3 == 0:
                    k *= 0.8
                elif (x + y) % 5 == 0:
                    k *= 1.08
            elif pat == 'stripes':
                k *= 0.7 if (y // 3) % 2 == 0 else 1.0
            elif pat == 'frill':
                d = abs(x - 7.5) + abs(y - 7.5)
                k *= 0.65 if 4 < d < 6 else (1.15 if d >= 11 else 1.0)
            elif pat == 'plates':
                k *= 0.6 if (x % 5 == 0 or y % 5 == 0) else 1.05
            elif pat == 'wing':
                k *= 0.75 if (x == y or x == 2 * y - 8 or y == 3) else 1.0
            px = (_clamp(R * k), _clamp(G * k), _clamp(B * k), 255)
            if pat == 'eye':
                px = (20, 14, 10, 255) if x in (7, 8) and 3 <= y <= 12 else (
                    (40, 30, 20, 255) if x in (0, 15) or y in (0, 15) else (_clamp(R * k), _clamp(G * k), _clamp(B * k), 255))
            if pat == 'teeth':
                px = (_clamp(R * k), _clamp(G * k), _clamp(B * k), 255) if (x % 4 in (0, 1) and y < 8 + (x % 4) * 4) else (70, 30, 30, 255)
            row.append(px)
        img.append(row)
    return img


def _uv(a, b):
    return [0, 0, max(1.0, min(16.0, round(a * 16, 2))), max(1.0, min(16.0, round(b * 16, 2)))]


for _sp in _TD.SPECIES.values():
    for _m, (_rgb, _pat, _blk) in _sp.mats.items():
        png_rgba(os.path.join(A, 'textures', 'item', 'dino', f'{_sp.key}_{_m}.png'), _tex(_rgb, _pat, zlib.crc32(f'{_sp.key}/{_m}'.encode())))
    for _b in _sp.bones:
        _s = _TD.bone_scale(_b)
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
        _name = f'dino/{_sp.key}_{_b.name}'
        wjson(os.path.join(A, 'models', 'item', _name + '.json'),
              {'textures': {**{m: f'mg:item/dino/{_sp.key}_{m}' for m in _used}, 'particle': f'mg:item/dino/{_sp.key}_{_used[0]}'},
               'elements': _els})
        wjson(os.path.join(A, 'items', _name + '.json'), {'model': {'type': 'minecraft:model', 'model': f'mg:item/{_name}'}})
