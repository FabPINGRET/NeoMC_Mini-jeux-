"""Eau du spawn pour les décors saisonniers : fontaines, cascades, biome d'eau (importé par gen_themes.py, jamais lancé seul).

Une source qui déborde (air dessous ou à côté) alimente un écoulement : toute l'eau voisine (6 blocs, jusqu'à 30 plus
bas) reste liquide (pas de glace à Noël) et lobby/theme/water_fix la remet d'aplomb à chaque bascule de thème.
load() calcule WATER, SPILL, FLOW et FOUNT à partir de theme_world.W (déjà chargé) ; écriture : write_fix, write_toggle, write_biome.
"""
import os

import common as C
from theme_world import LIM, PLANTS, W, bid, opening

WATER = set()                            # sources d'eau du spawn
SPILL = []                               # sources qui débordent
FLOW = {}                                # source qui déborde -> eau de son ouvrage
FOUNT = set()                            # toute l'eau des ouvrages (fontaines et cascades)


def load():
    """À appeler une fois theme_world.load() fait ; rappelable."""
    assert W, 'theme_world.load(F) doit être appelé avant theme_water.load()'
    for d in (WATER, SPILL, FLOW, FOUNT):
        d.clear()
    WATER.update(k for k, b in W.items() if bid(b) == 'minecraft:water')
    SPILL.extend(k for k in sorted(WATER) if opening((k[0], k[1] - 1, k[2]))
                 or any(opening((k[0] + a, k[1], k[2] + c)) for a, c in ((1, 0), (-1, 0), (0, 1), (0, -1))))
    for s in SPILL:
        FLOW[s] = {k for k in WATER if max(abs(k[0] - s[0]), abs(k[2] - s[2])) <= 6 and s[1] - 30 <= k[1] <= s[1]}
    FOUNT.update(set().union(*FLOW.values()) if FLOW else set())


def water_biome(biome):
    """fillbiome des colonnes de 16×16 qui contiennent de l'eau (aller : the_void → biome, retour : biome → the_void)"""
    cols = {}
    for (x, y, z), b in W.items():
        if bid(b) == 'minecraft:water' and abs(x) <= LIM and abs(z) <= LIM:
            lo, hi = cols.get((x >> 4, z >> 4), (y, y))
            cols[(x >> 4, z >> 4)] = (min(lo, y), max(hi, y))
    box = [(cx * 16, lo - 2, cz * 16, cx * 16 + 15, hi + 2, cz * 16 + 15) for (cx, cz), (lo, hi) in sorted(cols.items())]
    go = [f'fillbiome {a} {b} {c} {d} {e} {f} {biome} replace minecraft:the_void' for a, b, c, d, e, f in box]
    back = [f'fillbiome {a} {b} {c} {d} {e} {f} minecraft:the_void replace {biome}' for a, b, c, d, e, f in box]
    return go, back


# ------------------------------------------------------------------ fonctions écrites
def write_toggle(T, label, water):
    """water = (aller, retour) de water_biome ; écrit T/water_on et T/water_off, renvoie (on_x, off_x) à greffer à place / off.
    Fonctions à part : le biome du pack n'existe qu'après un redémarrage du serveur, d'ici là seules elles échouent au
    chargement (place et off restent valides)."""
    go, back = water
    C.w(f'{T}/water_on', [f'# {label} : biome du thème sur les colonnes d\'eau du spawn (couleur de l\'eau)'] + go)
    C.w(f'{T}/water_off', [f'# {label} : rend le biome the_void aux colonnes d\'eau du spawn'] + back)
    return [f'function mg:{T}/water_on'], [f'function mg:{T}/water_off']


def write_fix():
    fix = ['# Fontaines et cascades du spawn remises d\'aplomb : eau débordée retirée, sources et plantes d\'origine reposées',
           '# (relancé à chaque bascule de thème ; à la main : /function mg:lobby/theme/water_fix)']
    boxes = set()
    for s, blocks in sorted(FLOW.items()):
        xs, ys, zs = [k[0] for k in blocks], [k[1] for k in blocks], [k[2] for k in blocks]
        boxes.add((min(xs) - 2, max(xs) + 2, min(ys) - 1, max(ys) + 1, min(zs) - 2, max(zs) + 2))
    for x1, x2, y1, y2, z1, z2 in sorted(boxes):
        inside = [(k, b) for k, b in sorted(W.items()) if x1 <= k[0] <= x2 and y1 <= k[1] <= y2 and z1 <= k[2] <= z2]
        fix.append(f'fill {x1} {y1} {z1} {x2} {y2} {z2} minecraft:air replace minecraft:water')
        fix += [f'setblock {x} {y} {z} {b}' for (x, y, z), b in inside if bid(b) == 'minecraft:water']
        fix += [f'execute if block {x} {y} {z} minecraft:air run setblock {x} {y} {z} {b}' for (x, y, z), b in inside if bid(b) in PLANTS]
    C.w('lobby/theme/water_fix', fix)


def write_biome(name, water_color, fog_color):
    """Biome d'eau colorée (the_void + water_color) : data/mg/worldgen/biome/<name>.json, référencé par water_biome('mg:<name>')"""
    os.makedirs(os.path.join(C.D, 'worldgen', 'biome'), exist_ok=True)
    with open(os.path.join(C.D, 'worldgen', 'biome', f'{name}.json'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(C.js({'attributes': {'minecraft:visual/sky_color': '#7ba4ff', 'minecraft:visual/water_fog_color': fog_color},
                      'carvers': [], 'downfall': 0.5, 'effects': {'water_color': water_color}, 'features': [],
                      'has_precipitation': False, 'spawn_costs': {},
                      'spawners': {k: [] for k in ('ambient', 'axolotls', 'creature', 'misc', 'monster', 'underground_water_creature',
                                                    'water_ambient', 'water_creature')},
                      'temperature': 0.5}) + '\n')
