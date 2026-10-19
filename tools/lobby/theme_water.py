"""Eau du spawn pour les décors saisonniers : fontaines, cascades, biome du thème : eau, herbe et feuillage (importé par gen_themes.py, jamais lancé seul).

Une source qui déborde (air dessous ou à côté) alimente un écoulement : toute l'eau voisine (6 blocs, jusqu'à 30 plus
bas) reste liquide (pas de glace à Noël) et lobby/theme/water_fix la remet d'aplomb à chaque bascule de thème.
load() calcule WATER, SPILL, FLOW et FOUNT à partir de theme_world.W (déjà chargé) ; écriture : write_fix, write_check, write_toggle,
write_biome.
"""
import os

import common as C
from theme_world import DYN, LIM, PAD_BOXES, PLANTS, PLOTS, RESERVED, W, bid, dyn, free, opening

WATER = set()                            # sources d'eau du spawn
SPILL = []                               # sources qui débordent
FLOW = {}                                # source qui déborde -> eau de son ouvrage
FOUNT = set()                            # toute l'eau des ouvrages (fontaines et cascades)


def load():
    """À appeler une fois theme_world.load() fait ; rappelable."""
    assert W, 'theme_world.load(F) doit être appelé avant theme_water.load()'
    for d in (WATER, SPILL, FLOW, FOUNT):
        d.clear()
    # (l'eau d'une zone modifiée ailleurs n'est plus celle du spawn : ex. l'ancienne fontaine sous le grand Hall des scores)
    WATER.update(k for k, b in W.items() if bid(b) == 'minecraft:water' and not dyn(*k))
    SPILL.extend(k for k in sorted(WATER) if opening((k[0], k[1] - 1, k[2]))
                 or any(opening((k[0] + a, k[1], k[2] + c)) for a, c in ((1, 0), (-1, 0), (0, 1), (0, -1))))
    for s in SPILL:
        FLOW[s] = {k for k in WATER if max(abs(k[0] - s[0]), abs(k[2] - s[2])) <= 6 and s[1] - 30 <= k[1] <= s[1]}
    FOUNT.update(set().union(*FLOW.values()) if FLOW else set())


# blocs dont la couleur vient du biome du thème : eau, herbe, touffes d'herbe, lianes (feuilles : suffixe _leaves)
TINTED = {'minecraft:water', 'minecraft:grass_block', 'minecraft:short_grass', 'minecraft:fern', 'minecraft:tall_grass',
          'minecraft:large_fern', 'minecraft:vine'}


def tinted(i):
    return i in TINTED or i.endswith('_leaves')


def theme_biome(biome):
    """fillbiome des colonnes de 16×16 qui contiennent de l'eau (couleur de l'eau) ou un bloc teinté par le biome : herbe,
    touffes, feuilles, lianes (aller : the_void → biome, retour : biome → the_void). Une seule boîte par colonne : sa hauteur
    monte jusqu'au sommet des arbres. Le biome se lit par cellule de 4 blocs : la marge de 2 en hauteur suffit à couvrir celle
    de chaque bloc."""
    cols = {}
    for (x, y, z), b in W.items():
        if tinted(bid(b)) and abs(x) <= LIM and abs(z) <= LIM:
            lo, hi = cols.get((x >> 4, z >> 4), (y, y))
            cols[(x >> 4, z >> 4)] = (min(lo, y), max(hi, y))
    box = [(cx * 16, lo - 2, cz * 16, cx * 16 + 15, hi + 2, cz * 16 + 15) for (cx, cz), (lo, hi) in sorted(cols.items())]
    assert all(16 * 16 * (e - b + 1) <= 32768 for _, b, _, _, e, _ in box), 'boîte fillbiome > 32768 blocs'
    go = [f'fillbiome {a} {b} {c} {d} {e} {f} {biome} replace minecraft:the_void' for a, b, c, d, e, f in box]
    back = [f'fillbiome {a} {b} {c} {d} {e} {f} minecraft:the_void replace {biome}' for a, b, c, d, e, f in box]
    return go, back


LILY = {'minecraft:lily_pad'}            # posé après l'eau (il ne tient pas sans elle) : jamais dans l'ouvrage reposé d'office
# blocs à données (inventaire, texte, tête...) ou fragiles : jamais reposés d'office ; id exact, préfixe ou suffixe (pas de sous-chaîne : bedrock)
DATA_IDS = {'chest', 'trapped_chest', 'ender_chest', 'barrel', 'lectern', 'flower_pot', 'decorated_pot', 'chiseled_bookshelf', 'campfire',
            'soul_campfire', 'spawner', 'trial_spawner', 'vault', 'hopper', 'furnace', 'blast_furnace', 'smoker', 'beacon', 'bell',
            'jukebox', 'dispenser', 'dropper', 'brewing_stand', 'enchanting_table', 'conduit', 'vine', 'beehive', 'bee_nest', 'crafter',
            'suspicious_sand', 'suspicious_gravel', 'creaking_heart', 'structure_block', 'jigsaw'}
DATA_PREFIX = ('potted_',)
DATA_SUFFIX = ('_sign', '_banner', '_head', '_skull', '_bed', '_shulker_box', '_shelf', '_chest', '_door', 'command_block')


def structural(b):
    """Bloc d'ouvrage (pierre, dalle, mur, sable...) : ni eau, ni plante, ni nénuphar, ni bloc à données."""
    n = bid(b).split(':')[-1]
    return bid(b) not in PLANTS | LILY | {'minecraft:water'} and n not in DATA_IDS and not n.startswith(DATA_PREFIX) \
        and not n.endswith(DATA_SUFFIX)


def overlap(a, b):
    return all(a[i] <= b[i + 1] and b[i] <= a[i + 1] for i in (0, 2, 4))


def boxes():
    """Une boîte (x1, x2, y1, y2, z1, z2) par source qui déborde (son eau à 2 blocs près, 1 en hauteur), les boîtes qui se
    recouvrent fusionnées (jusqu'à stabilité) : chaque cellule n'est traitée qu'une fois. Jamais de boîte sur une zone modifiée
    ailleurs, une parcelle ou une zone réservée : le fill de water_fix y viderait l'eau d'un autre système."""
    out = set()
    for blocks in FLOW.values():
        xs, ys, zs = [k[0] for k in blocks], [k[1] for k in blocks], [k[2] for k in blocks]
        out.add((min(xs) - 2, max(xs) + 2, min(ys) - 1, max(ys) + 1, min(zs) - 2, max(zs) + 2))
    out = sorted(out)
    merged = True
    while merged:
        merged = False
        for i, a in enumerate(out):
            for b in out[i + 1:]:
                if overlap(a, b):
                    out.remove(b)
                    out[i] = tuple(f(a[n], b[n]) for n, f in enumerate((min, max) * 3))
                    merged = True
                    break
            if merged:
                break
    for box in out:
        bad = conflicts(box)
        assert not bad, f"boîte d'eau {box} sur une zone dynamique, une parcelle, une zone réservée ou hors décor : {bad[:3]}"
    return out


def conflicts(box):
    """Ce que la boîte recouvre sans y avoir droit : zones DYN, réservées, parcelles (marge 1), hors décor."""
    bad = [d for d in DYN + RESERVED + PAD_BOXES if overlap(box, d)]
    bad += [p for p in PLOTS if box[0] <= p[1] + 1 and p[0] - 1 <= box[1] and box[4] <= p[3] + 1 and p[2] - 1 <= box[5]]
    return bad + ([box] if min(box[0], box[4]) < -LIM or max(box[1], box[5]) > LIM else [])


def plan(touched):
    """(boîte, sources d'eau, plantes et nénuphars, ouvrage à reposer, passage à dégager) par boîte, d'après W ; partagé par
    water_fix et water_check. Ouvrage = blocs d'ouvrage autour de l'eau des ouvrages (3x3x3). Passage = couche au-dessus de cette
    eau + chute depuis chaque source qui déborde (ses 4 voisins et dessous, jusqu'au premier bloc d'origine, 30 au plus ; sans
    bloc dessous, seules les 2 premières cellules). Les cellules d'un thème (touched) et les zones hors décor (free) ne sont
    jamais reposées ni dégagées."""
    out = []
    for box in boxes():
        x1, x2, y1, y2, z1, z2 = box
        inside = {k: b for k, b in sorted(W.items()) if x1 <= k[0] <= x2 and y1 <= k[1] <= y2 and z1 <= k[2] <= z2 and free(*k)}
        wet = FOUNT & set(inside)
        near = {(x + a, y + d, z + c) for x, y, z in wet for a in (-1, 0, 1) for c in (-1, 0, 1) for d in (-1, 0, 1)}
        path = {(x, y + 1, z) for x, y, z in wet}
        for x, y, z in (k for k in SPILL if k in wet):
            for a, c in ((1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)):
                col, yy = [], y - (1 if (a, c) == (0, 0) else 0)
                while yy >= y - 30 and (x + a, yy, z + c) not in W:
                    col.append((x + a, yy, z + c))
                    yy -= 1
                path.update(col if yy >= y - 30 else col[:2])
        out.append((box, [(k, b) for k, b in inside.items() if bid(b) == 'minecraft:water'],
                    [(k, b) for k, b in inside.items() if bid(b) in PLANTS | LILY],
                    [(k, b) for k, b in inside.items() if k in near and k not in touched and structural(b)],
                    sorted(k for k in path if k not in W and k not in touched and free(*k))))
    return out


# ------------------------------------------------------------------ fonctions écrites
def write_toggle(T, label, water):
    """water = (aller, retour) de theme_biome ; écrit T/water_on et T/water_off, renvoie (on_x, off_x) à greffer à place / off.
    Fonctions à part : le biome du pack n'existe qu'après un redémarrage du serveur, d'ici là seules elles échouent au
    chargement (place et off restent valides)."""
    go, back = water
    # water = biome du thème (eau + herbe + feuillage) : les noms water/water_on/water_off restent ceux des fonctions générées
    C.w(f'{T}/water_on', [f'# {label} : biome du thème sur les colonnes d\'eau et de sol du spawn (couleur de l\'eau, teinte de l\'herbe et du feuillage)'] + go)
    C.w(f'{T}/water_off', [f'# {label} : rend le biome the_void aux colonnes d\'eau et de sol du spawn'] + back)
    return [f'function mg:{T}/water_on'], [f'function mg:{T}/water_off']


def write_fix(touched):
    """touched = cellules qu'au moins un thème change (ALLCH) : jamais reposées ni dégagées, et leur eau (glace de Noël) n'est
    pas remise en source. Par ouvrage : ouvrage reposé, passage dégagé, eau débordée retirée, sources, plantes et nénuphars."""
    fix = ['# Fontaines et cascades du spawn remises d\'aplomb : ouvrage reposé, passage de l\'eau dégagé, eau débordée retirée,',
           '# sources, plantes et nénuphars d\'origine reposés (relancé à chaque bascule de thème ; à la main : /function mg:lobby/theme/water_fix)',
           '# Contrôle sans rien modifier : /function mg:lobby/theme/water_check']
    for (x1, x2, y1, y2, z1, z2), water, plants, near, path in plan(touched):
        fix += [f'setblock {x} {y} {z} {b}' for (x, y, z), b in near]
        fix += [f'execute unless block {x} {y} {z} minecraft:air unless block {x} {y} {z} minecraft:water run setblock {x} {y} {z} minecraft:air'
                for x, y, z in path]
        # nénuphars retirés d'abord (sans objet lâché), puis l'eau : le fill les détruirait en les laissant tomber en objets
        fix.append(f'fill {x1} {y1} {z1} {x2} {y2} {z2} minecraft:air replace minecraft:lily_pad')
        fix.append(f'fill {x1} {y1} {z1} {x2} {y2} {z2} minecraft:air replace minecraft:water')
        for (x, y, z), b in water:                # la glace d'un thème sur une source reste de la glace
            cond = f'execute unless block {x} {y} {z} minecraft:ice run ' if (x, y, z) in touched else ''
            fix.append(f'{cond}setblock {x} {y} {z} {b}')
        fix += [f'execute if block {x} {y} {z} minecraft:air run setblock {x} {y} {z} {b}' for (x, y, z), b in plants]   # après l'eau
    C.w('lobby/theme/water_fix', fix)


def write_check(touched):
    """lobby/theme/water_check : liste (à @s) ce que water_fix reposerait ou dégagerait, sans rien modifier."""
    chk = ['# Contrôle des fontaines et cascades du spawn : liste les positions que lobby/theme/water_fix remettrait d\'aplomb',
           '# (ne modifie rien ; aucune ligne affichée = tout est en ordre)',
           'tellraw @s {"text":"Contrôle des fontaines : seules les anomalies sont listées.","color":"gray"}']
    for _, water, plants, near, path in plan(touched):
        chk += [f'execute unless block {x} {y} {z} minecraft:water unless block {x} {y} {z} minecraft:ice run '
                f'tellraw @s "{x} {y} {z} : attendu minecraft:water"' for (x, y, z), _ in water]
        chk += [f'execute if block {x} {y} {z} minecraft:air run tellraw @s "{x} {y} {z} : attendu {bid(b)}"' for (x, y, z), b in plants]
        chk += [f'execute unless block {x} {y} {z} {bid(b)} run tellraw @s "{x} {y} {z} : attendu {bid(b)}"' for (x, y, z), b in near]
        chk += [f'execute unless block {x} {y} {z} minecraft:air unless block {x} {y} {z} minecraft:water run '
                f'tellraw @s "{x} {y} {z} : devrait être de l\'air ou de l\'eau"' for x, y, z in path]
    chk.append('tellraw @s {"text":"Contrôle terminé.","color":"gray"}')
    C.w('lobby/theme/water_check', chk)


def write_biome(name, water_color, fog_color, grass_color, foliage_color, dry_foliage_color):
    """Biome du thème (the_void + couleurs de l'eau, de l'herbe, du feuillage et du feuillage sec, en #rrggbb) :
    data/mg/worldgen/biome/<name>.json, référencé par theme_biome('mg:<name>')"""
    os.makedirs(os.path.join(C.D, 'worldgen', 'biome'), exist_ok=True)
    with open(os.path.join(C.D, 'worldgen', 'biome', f'{name}.json'), 'w', encoding='utf-8', newline='\n') as f:
        f.write(C.js({'attributes': {'minecraft:visual/sky_color': '#7ba4ff', 'minecraft:visual/water_fog_color': fog_color},
                      'carvers': [], 'downfall': 0.5, 'effects': {'water_color': water_color, 'grass_color': grass_color,
                                              'foliage_color': foliage_color, 'dry_foliage_color': dry_foliage_color},
                      'features': [],
                      'has_precipitation': False, 'spawn_costs': {},
                      'spawners': {k: [] for k in ('ambient', 'axolotls', 'creature', 'misc', 'monster', 'underground_water_creature',
                                                    'water_ambient', 'water_creature')},
                      'temperature': 0.5}) + '\n')
