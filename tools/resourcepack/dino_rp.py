# ------------------------------------------------------------------ Terra Nova : dinosaures articulés (un modèle par os)
# Exécuté par gen_rp.py (exec) : utilise wjson, png_rgba, A, os, json, zlib. Données : tools/arcade/tv_dinos.py.
# Os d'une espèce -> assets/mg/items/dino/<espèce>_<os>.json + modèle mg:item/dino/<espèce>_<os> (articulation au centre 8,8,8,
# échelle réduite de bone_scale ; vérifié en jeu : l'item_display affiche le modèle sans le retourner).
# _bone_assets (aussi utilisée par ol_rp.py) : os gauche/droite identiques = un seul modèle, textures inutilisées non écrites.
import random as _rnd
import shutil as _shutil
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


def _bone_model(sp, family, b, bone_scale):
    s = bone_scale(b)
    els = []
    for (x1, y1, z1, x2, y2, z2, m) in b.boxes:
        fx = (8 + 16 * x1 / s, 8 + 16 * x2 / s)
        fz = (8 + 16 * z1 / s, 8 + 16 * z2 / s)
        fy = (8 + 16 * y1 / s, 8 + 16 * y2 / s)
        dx, dy, dz = x2 - x1, y2 - y1, z2 - z1
        uvs = {'north': _uv(dx, dy), 'south': _uv(dx, dy), 'east': _uv(dz, dy), 'west': _uv(dz, dy), 'up': _uv(dx, dz), 'down': _uv(dx, dz)}
        els.append({'from': [round(fx[0], 3), round(fy[0], 3), round(fz[0], 3)], 'to': [round(fx[1], 3), round(fy[1], 3), round(fz[1], 3)],
                    'faces': {d: {'texture': f'#{m}', 'uv': uv} for d, uv in uvs.items()}})
    used = sorted({bx[6] for bx in b.boxes})
    return {'textures': {**{m: f'mg:item/{family}/{sp.key}_{m}' for m in used}, 'particle': f'mg:item/{family}/{sp.key}_{used[0]}'},
            'elements': els}


def _bone_assets(species_map, family, bone_scale):
    """Os de chaque espèce -> textures, modèles et items de assets/mg/{textures/item,models/item,items}/<family>/.
    Les dossiers sont vidés avant (les générateurs n'effacent pas leurs anciens fichiers). Une texture n'est écrite que si une boîte de
    l'espèce l'utilise ; un os dont le modèle est identique à celui d'un os déjà écrit (gauche/droite) réutilise ce modèle."""
    assert family and family.isidentifier(), family          # garde : family sert de nom de dossier vidé par rmtree
    for d in (('textures', 'item'), ('models', 'item'), ('items',)):
        _shutil.rmtree(os.path.join(A, *d, family), ignore_errors=True)
    for sp in species_map.values():
        boxed = {bx[6] for b in sp.bones for bx in b.boxes}
        for m, (rgb, pat, _blk) in sp.mats.items():
            if m in boxed:
                png_rgba(os.path.join(A, 'textures', 'item', family, f'{sp.key}_{m}.png'), _tex(rgb, pat, zlib.crc32(f'{sp.key}/{m}'.encode())))
        written = {}
        for b in sp.bones:
            model = _bone_model(sp, family, b, bone_scale)
            key = json.dumps(model, sort_keys=True)
            if key not in written:
                written[key] = f'{family}/{sp.key}_{b.name}'
                wjson(os.path.join(A, 'models', 'item', written[key] + '.json'), model)
            wjson(os.path.join(A, 'items', f'{family}/{sp.key}_{b.name}.json'),
                  {'model': {'type': 'minecraft:model', 'model': f'mg:item/{written[key]}'}})


_bone_assets(_TD.SPECIES, 'dino', _TD.bone_scale)
