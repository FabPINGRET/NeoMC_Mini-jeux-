# ------------------------------------------------------------------ 🎩 chapeaux cosmétiques : modèles 3D portés sur la tête
# Exécuté par gen_rp.py (exec) : utilise wjson, png, A. Données : tools/cosmetics/hats_data.py (aussi lues par tools/cosmetics/gen_hats.py).
# Objet porté dans l'emplacement tête sans asset_id : rendu « head » du modèle (bloc = 1,25 tête), 1 pixel de tête = 1,6 unité.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'cosmetics'))
import hats_data as _hd

_hpal = {'.': (0, 0, 0, 0), **_hd.PAL}
png(os.path.join(A, 'textures', 'item', 'hat_pal.png'),
    [''.join(_hd.PAL_KEYS[i] if (i := (y // 2) * 8 + x // 2) < len(_hd.PAL_KEYS) else '.' for x in range(16)) for y in range(16)], _hpal)


def _hk(p):
    return round(1.6 + 1.6 * p, 3)


def _hat_el(b):
    x1, y1, z1, x2, y2, z2, c = b[:7]
    i = _hd.PAL_KEYS.index(c)
    u, v = (i % 8) * 2 + 0.5, (i // 8) * 2 + 0.5        # centre de la case 2×2 de la couleur
    el = {"from": [_hk(x1), _hk(y1), _hk(z1)], "to": [_hk(x2), _hk(y2), _hk(z2)],
          "faces": {d: {"texture": "#p", "uv": [u, v, u + 1, v + 1]} for d in ('north', 'south', 'east', 'west', 'up', 'down')}}
    for o in b[7:]:
        if o == 'glow':
            el["light_emission"] = 15
        else:
            _, ax, ang, ox, oy, oz = o
            el["rotation"] = {"angle": ang, "axis": ax, "origin": [_hk(ox), _hk(oy), _hk(oz)]}
    return el


for _n, _key, _name, _rar, _boxes in _hd.HATS:
    wjson(os.path.join(A, 'models', 'hat', _key + '.json'),
          {"textures": {"p": "mg:item/hat_pal", "particle": "mg:item/hat_pal"}, "elements": [_hat_el(b) for b in _boxes],
           "display": {"gui": {"rotation": [30, 225, 0], "translation": [0, -3, 0], "scale": [0.5, 0.5, 0.5]}}})
    wjson(os.path.join(A, 'items', 'hat', _key + '.json'), {"model": {"type": "minecraft:model", "model": f"mg:hat/{_key}"}})
