"""Données des variantes (pures, aucune écriture) : arènes de combat, sols, modes, réglages par difficulté, variantes.

Ids de variante : 100.. (combat puis sols), 190 au plus (190..196 = « variante au hasard » de chaque mode).
LAST_ID = premier id non attribué (le récapitulatif de gen_variants.py affiche LAST_ID - 1).
"""
# ============================================================ arènes de combat
# k, nom, couleur, taille, construction, centre z, spread (d, r, under), spawnpoint, perchoir y, ky (élimination),
# boîte d'items (x y z dx dy dz), plafond de barrière à ajouter pour OITC (x1 y z1 x2 z2) ou None,
# setup TNT Tag (cartes à relief : placement sur points fixes), origine (jeu de la carte), description
ARENAS = [
    dict(k=1, name='Poussière', col='gold', size='M', build='dust/build', z=11100, sp=(6, 18, 84), spawn='0 81 11116', py=100, ky=70,
         items='-24 60 11076 48 40 48', ceil=(-21, 93, 11079, 21, 11121), src='PvP', desc='style Dust, 43×43, couloirs et tunnels'),
    dict(k=2, name='Mirage', col='aqua', size='M', build='mirage/build', z=11300, sp=(6, 18, 84), spawn='0 81 11316', py=100, ky=70,
         items='-24 60 11276 48 40 48', ceil=(-21, 93, 11279, 21, 11321), src='PvP', desc='style Mirage, 43×43, appartements et fenêtre'),
    dict(k=3, name='Nuketown', col='green', size='M', build='nuketown/build', z=11500, sp=(6, 15, 84), spawn='0 81 11513', py=100, ky=70,
         items='-26 60 11474 52 40 52', ceil=(-25, 92, 11482, 25, 11518), src='PvP', desc='49×35, deux maisons face à face, bus au milieu'),
    dict(k=4, name='Arène OITC', col='gold', size='S', build='oitc/build', z=5800, sp=(5, 10, 90), spawn='0 81 5800', py=100, ky=70,
         items='-20 70 5780 40 30 40', ceil=None, src='One in the Chamber', desc='25×25, piliers'),
    dict(k=5, name='Château', col='gold', size='M', build='oitc/build_1', z=11700, sp=(5, 17, 84), spawn='0 81 11716', py=106, ky=70,
         items='-24 70 11676 48 40 48', ceil=None, src='One in the Chamber', desc='41×41, donjon à étage, tours à échelles'),
    dict(k=6, name='Grande forêt', col='dark_green', size='L', build='oitc/build_2', z=12000, sp=(8, 30, 86), spawn='0 84 12000', py=110, ky=70,
         items='-40 70 11960 80 45 80', ceil=None, src='One in the Chamber', desc='71×71, collines, arbres, ruines'),
    dict(k=7, name='Néon', col='aqua', size='S', build='quake/build', z=7300, sp=(5, 13, 90), spawn='13 81 7313', py=100, ky=70,
         items='-20 70 7280 40 30 40', ceil=None, src='Quakecraft', desc='33×33, couloirs lumineux'),
    dict(k=8, name='Volcan', col='red', size='L', build='quake/build_1', z=7600, sp=(8, 28, 90), spawn='28 81 7628', py=100, ky=70,
         items='-34 70 7566 68 30 68', ceil=None, src='Quakecraft', desc='63×63, coulées de magma (ça brûle !)', hazard=True),
    dict(k=9, name='Jungle', col='dark_green', size='L', build='quake/build_2', z=7900, sp=(8, 28, 90), spawn='28 81 7928', py=100, ky=70,
         items='-34 70 7866 68 30 68', ceil=None, src='Quakecraft', desc='63×63, végétation dense'),
    dict(k=10, name='Désert', col='gold', size='S', build='quake/build_3', z=8200, sp=(5, 13, 90), spawn='13 81 8213', py=100, ky=70,
         items='-20 70 8180 40 30 40', ceil=None, src='Quakecraft', desc='33×33, ruines de grès'),
    dict(k=11, name='Glacier', col='aqua', size='XS', build='quake/build_4', z=8500, sp=(3, 7, 90), spawn='7 81 8507', py=100, ky=70,
         items='-14 70 8486 28 30 28', ceil=None, src='Quakecraft', desc='21×21, minuscule'),
    dict(k=12, name='Arène TNT Tag', col='red', size='S', build='tnttag/build', z=6100, sp=(4, 13, 90), spawn='0 81 6100', py=100, ky=71,
         items='-25 70 6075 50 30 50', ceil=(-16, 92, 6084, 16, 6116), src='TNT Tag', desc='31×31, piliers et murets'),
    dict(k=13, name='Collines', col='green', size='M', setup='tnttag/map/setup_1', z=26500, sp=(3, 22, 100), py=115,
         ceil=(-24, 112, 26476, 24, 26524), src='TNT Tag', desc='51×51, prairie vallonnée, rivière, moulin', relief=True),
    dict(k=14, name='Canyon', col='gold', size='M', setup='tnttag/map/setup_2', z=26800, sp=(3, 22, 100), py=111,
         ceil=(-24, 108, 26776, 24, 26824), src='TNT Tag', desc='51×51, mesa à plateaux, arche, pont suspendu', relief=True),
    dict(k=15, name='Village perché', col='aqua', size='M', setup='tnttag/map/setup_3', z=27400, sp=(3, 22, 100), py=117,
         ceil=(-24, 114, 27376, 24, 27424), src='TNT Tag', desc='51×51, toits, passerelles, clocher', relief=True),
    dict(k=16, name='Paintball', col='gold', size='M', build='paintball/build', z=8800, sp=(6, 22, 90), spawn='0 81 8800', py=100, ky=70,
         items='-28 70 8766 56 30 68', ceil=None, src='Paintball', desc='49×61, murets blancs'),
    dict(k=17, name='Mini-paintball', col='gold', size='S', build='paintball/build_1', z=12300, sp=(4, 13, 90), spawn='0 81 12300', py=100, ky=70,
         items='-16 70 12279 32 30 42', ceil=None, src='Paintball', desc='29×39, rapide'),
    dict(k=18, name='Grand paintball', col='gold', size='XL', build='paintball/build_2', z=12700, sp=(8, 37, 90), spawn='0 81 12700', py=105, ky=70,
         items='-42 70 12648 84 30 104', ceil=None, src='Paintball', desc='79×99, immense'),
]
AR = {a['k']: a for a in ARENAS}

# Modes de combat : id du jeu, nom, couleur, arènes natives (exclues), étoiles selon la taille
COMBAT = [
    dict(key='pvp', game=3, name='Arène PvP', short='PVP', col='yellow', icon='⚔', rnd=190, native={1, 2, 3},
         st={'XS': 4, 'S': 3, 'M': 2, 'L': 2, 'XL': 1}, hazard=1, relief=0),
    dict(key='oitc', game=26, name='One in the Chamber', short='OITC', col='gold', icon='➶', rnd=191, native={4, 5, 6},
         st={'XS': 3, 'S': 2, 'M': 2, 'L': 3, 'XL': 4}, hazard=0, relief=0),
    dict(key='quake', game=31, name='Quakecraft', short='QUAKE', col='aqua', icon='⚡', rnd=192, native={1, 2, 3, 7, 8, 9, 10, 11},
         st={'XS': 3, 'S': 2, 'M': 2, 'L': 3, 'XL': 4}, hazard=0, relief=1),
    dict(key='tnttag', game=27, name='TNT Tag', short='TNT TAG', col='red', icon='✹', rnd=193, native={12, 13, 14, 15},
         st={'XS': 4, 'S': 3, 'M': 2, 'L': 1, 'XL': 1}, hazard=0, relief=0),
]

# ============================================================ sols (centre 0 ~ 24300)
FX, FZ = 0, 24300
# étages : (y, demi-côté, demi-côté du trou ou 0)
LAYOUTS = [
    dict(k=21, name='Tour de Spleef', col='aqua', floors=[(80, 14, 0), (76, 12, 0), (72, 10, 0), (68, 8, 0)], src='Spleef',
         desc='4 étages qui rétrécissent (29×29 → 17×17)'),
    dict(k=22, name='Tour de TNT Run', col='red', floors=[(84, 14, 0), (80, 12, 0), (76, 10, 0)], src='TNT Run',
         desc='3 étages de laine qui rétrécissent (29×29 → 21×21)'),
    dict(k=23, name='Cube de Splegg', col='yellow', floors=[(80, 18, 0), (76, 18, 0), (72, 18, 0)], src='Splegg',
         desc='3 grands étages identiques (37×37)'),
    dict(k=24, name='Splegg XXL', col='gold', floors=[(80, 30, 0), (76, 26, 0), (72, 22, 0)], src='Splegg',
         desc='3 étages géants (61×61 → 45×45)'),
    dict(k=25, name='Pyramide', col='light_purple', floors=[(84, 16, 0), (80, 13, 0), (76, 10, 0), (72, 7, 0), (68, 4, 0)], src='nouveau',
         desc='5 étages en pyramide, de plus en plus petits (33×33 → 9×9)'),
    dict(k=26, name='Anneaux', col='dark_aqua', floors=[(80, 18, 7), (76, 11, 0), (72, 20, 12)], src='nouveau',
         desc='anneau troué, plateau central, anneau large (jusqu’à 41×41)', ring_spawn=True),
]
LY = {l['k']: l for l in LAYOUTS}
FLOOR_MODES = [
    dict(key='spleef', game=1, name='Spleef', short='SPLEEF', col='aqua', icon='❄', rnd=194, mat='snow_block', native={21},
         st={21: 2, 22: 2, 23: 1, 24: 1, 25: 3, 26: 4}),
    dict(key='tntrun', game=2, name='TNT Run', short='TNT RUN', col='red', icon='✷', rnd=195, mat='white_wool', native={22},
         st={21: 1, 22: 2, 23: 2, 24: 1, 25: 3, 26: 4}),
    dict(key='splegg', game=20, name='Splegg', short='SPLEGG', col='yellow', icon='❍', rnd=196, mat='snow_block', native={23, 24},
         st={21: 2, 22: 3, 23: 2, 24: 1, 25: 3, 26: 4}),
]

# Réglages selon la difficulté (indice = $dif - 1)
SET = {
    'pvp': ['+2 pommes d’or, +16 flèches', 'kit standard', 'sans bouclier, 1 pomme d’or', 'sans bouclier ni pomme, plastron en cuir'],
    'oitc': ['flèche enchantée toutes les 15 s, 7 kills', 'flèche enchantée toutes les 30 s, 10 kills',
             'flèche enchantée toutes les 45 s, 10 kills', 'aucune flèche enchantée, 12 kills'],
    'quake': ['rechargement 0,8 s', 'rechargement 1,1 s', 'rechargement 1,4 s', 'rechargement 1,7 s'],
    'tnttag': ['bombe lente (15 à 40 s)', 'bombe normale (10 à 30 s)', 'bombe rapide (8 à 22 s)', 'bombe éclair (6 à 15 s)'],
    'spleef': ['rétrécit après 50 s puis toutes les 15 s', 'rétrécit après 40 s puis toutes les 12 s',
               'rétrécit après 30 s puis toutes les 9 s', 'rétrécit après 20 s puis toutes les 6 s'],
    'tntrun': ['les blocs tiennent 0,6 s', 'les blocs tiennent 0,45 s', 'les blocs tiennent 0,35 s', 'les blocs tiennent 0,25 s'],
    'splegg': ['les œufs volent 0,75 s', 'les œufs volent 2 s', 'les œufs volent 2 s, cratères 3×3', 'les œufs volent 3 s, cratères 3×3'],
}

# ============================================================ liste des variantes (ids 100..)
VARIANTS = []
vid = 100
for m in COMBAT:
    for a in ARENAS:
        if a['k'] in m['native']:
            continue
        s = m['st'][a['size']] + (m['hazard'] if a.get('hazard') else 0) + (m['relief'] if a.get('relief') else 0)
        VARIANTS.append(dict(id=vid, mode=m, ar=a['k'], dif=max(1, min(4, s)), map=a))
        vid += 1
for m in FLOOR_MODES:
    for l in LAYOUTS:
        if l['k'] in m['native']:
            continue
        VARIANTS.append(dict(id=vid, mode=m, ar=l['k'], dif=m['st'][l['k']], map=l))
        vid += 1
assert vid <= 190, vid
MODES = COMBAT + FLOOR_MODES
for i, m in enumerate(MODES):
    m['opt'] = 33 + i
    m['vars'] = [v for v in VARIANTS if v['mode'] is m]

LAST_ID = vid
