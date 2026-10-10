"""Variantes : les modes de jeu sur les cartes des autres jeux, avec une difficulté ★ à ★★★★.

    python tools/variantes/gen_variants.py .        (depuis la racine du dépôt ; idempotent)

Génère :
  data/mg/function/var/**          remap des ids, annonce, préparation par mode, arènes, sols, réglages
  data/mg/dialog/var_*.json        menus (★ Variantes ▸ dans le menu principal et les sous-menus)
  data/mg/tags/block/ray_pass.json blocs traversés par le rayon du Quake (herbes, fleurs…)
et applique de petits crochets (marqués « [variantes] ») dans les fichiers des jeux concernés.

Principe : un id de variante (100..196) fixe $ar (arène ou sol, 0 = carte native), $dif (1..4)
et $vmode (jeu). Les jeux gardent leur comportement natif tant que $ar = 0 (et $dif = 2 = réglages actuels).

Familles :
  combat  : PvP (3), One in the Chamber (26), Quakecraft (31), TNT Tag (27) sur 18 arènes
            (cartes PvP, OITC, Quake, TNT Tag, Paintball). Exclus : l'arène PvP classique (sol y 63),
            le Paintball comme mode (il lui faut du béton blanc et deux bases).
  sols    : Spleef (1), TNT Run (2), Splegg (20) sur 6 formes de sol construites au même endroit
            (centre 0 ~ 24300) : 4 reprises des jeux + Pyramide + Anneaux.
            Exclus : Pluie d'enclumes et Block Party (mécaniques liées à leur sol).
"""
import json
import os
import re
import sys

R = sys.argv[1] if len(sys.argv) > 1 else '.'
D = os.path.join(R, 'data/mg')
F = os.path.join(D, 'function')
OUT = os.path.join(F, 'var')
written = []


def w(rel, lines):
    path = os.path.join(F, rel + '.mcfunction')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')
    written.append(path)


def wjson(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write('\n')
    written.append(path)


def stars(n):
    return '★' * n + '☆' * (4 - n)


def js(o):
    return json.dumps(o, ensure_ascii=False, separators=(',', ':'))


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
         items='-26 60 11474 52 40 52', ceil=(-25, 92, 11482, 25, 11518), src='PvP', desc='deux maisons face à face, bus au milieu'),
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
         desc='4 étages qui rétrécissent (29 → 17)'),
    dict(k=22, name='Tour de TNT Run', col='red', floors=[(84, 14, 0), (80, 12, 0), (76, 10, 0)], src='TNT Run',
         desc='3 étages de laine qui rétrécissent'),
    dict(k=23, name='Cube de Splegg', col='yellow', floors=[(80, 18, 0), (76, 18, 0), (72, 18, 0)], src='Splegg',
         desc='3 grands étages identiques (37×37)'),
    dict(k=24, name='Splegg XXL', col='gold', floors=[(80, 30, 0), (76, 26, 0), (72, 22, 0)], src='Splegg',
         desc='3 étages géants (61 → 45)'),
    dict(k=25, name='Pyramide', col='light_purple', floors=[(84, 16, 0), (80, 13, 0), (76, 10, 0), (72, 7, 0), (68, 4, 0)], src='nouveau',
         desc='5 étages en pyramide, de plus en plus petits'),
    dict(k=26, name='Anneaux', col='dark_aqua', floors=[(80, 18, 7), (76, 11, 0), (72, 20, 12)], src='nouveau',
         desc='anneau troué, plateau central, anneau large', ring_spawn=True),
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

# ============================================================ remap + annonce
lines = ['# Variantes (généré par tools/variantes/gen_variants.py) : id → $vmode (jeu), $ar (arène/sol), $dif (1..4)',
         '# Appelé par core/request quand $game = 100..196 ; ne change pas $game (pour ne pas déclencher les annonces natives)']
for m in MODES:
    n = len(m['vars'])
    lines.append(f'execute if score $game mg.st matches {m["rnd"]} store result score $vr mg.st run random value 0..{n - 1}')
    for i, v in enumerate(m['vars']):
        lines.append(f'execute if score $game mg.st matches {m["rnd"]} if score $vr mg.st matches {i} run scoreboard players set $game mg.st {v["id"]}')
for v in VARIANTS:
    lines += [f'execute if score $game mg.st matches {v["id"]} run scoreboard players set $vmode mg.st {v["mode"]["game"]}',
              f'execute if score $game mg.st matches {v["id"]} run scoreboard players set $ar mg.st {v["ar"]}',
              f'execute if score $game mg.st matches {v["id"]} run scoreboard players set $dif mg.st {v["dif"]}']
lines.append('scoreboard players operation $vid mg.st = $game mg.st')
w('var/remap', lines)

lines = ['# Variante : annonce puis $game = jeu réel (@s = demandeur). Généré.']
for v in VARIANTS:
    m, a = v['mode'], v['map']
    st = v['dif']
    lines.append(f'execute if score $vid mg.st matches {v["id"]} run tellraw @a ' + js([
        {'selector': '@s', 'color': 'yellow'}, {'text': ' lance ', 'color': 'gray'},
        {'text': f'{m["icon"]} {m["short"]} — {a["name"].upper()} ', 'color': m['col'], 'bold': True},
        {'text': '★' * st, 'color': 'gold'}, {'text': '☆' * (4 - st), 'color': 'dark_gray'}, {'text': ' !', 'color': 'gray'}]))
    lines.append(f'execute if score $vid mg.st matches {v["id"]} run tellraw @a ' + js([
        {'text': 'Variante : ', 'color': 'gray'}, {'text': f'carte {a["src"]} ({a["desc"]})', 'color': 'white'},
        {'text': ' · réglages : ', 'color': 'gray'}, {'text': SET[m['key']][st - 1], 'color': 'gold'}]))
lines.append('scoreboard players operation $game mg.st = $vmode mg.st')
w('var/start', lines)

# ============================================================ arènes de combat : setup (construction + placement)
for a in ARENAS:
    k = a['k']
    d, r, u = a['sp']
    L = [f'# Arène {k} « {a["name"]} » (carte {a["src"]}, centre 0 ~ {a["z"]}) : construction, perchoir, élimination, placement. Généré.']
    if a.get('setup'):
        L += [f'function mg:{a["setup"]}',
              'scoreboard players operation $ky mg.st = $tty mg.st']
    else:
        L += [f'function mg:{a["build"]}',
              f'kill @e[type=minecraft:item,x={a["items"].split()[0]},y={a["items"].split()[1]},z={a["items"].split()[2]},'
              f'dx={a["items"].split()[3]},dy={a["items"].split()[4]},dz={a["items"].split()[5]}]',
              'scoreboard players set $px mg.st 0', f'scoreboard players set $py mg.st {a["py"]}', f'scoreboard players set $pz mg.st {a["z"]}',
              f'scoreboard players set $ky mg.st {a["ky"]}',
              'gamemode adventure @a[tag=mg.play]',
              f'execute as @a[tag=mg.play] run spawnpoint @s {a["spawn"]}',
              f'spreadplayers 0 {a["z"]} {d} {r} under {u} false @a[tag=mg.play]']
    L.append(f'data modify storage mg:var a set value {{x:0,z:{a["z"]},r:{r},u:{u}}}')
    w(f'var/arena/a{k}', L)
    if a['ceil']:
        x1, y, z1, x2, z2 = a['ceil']
        w(f'var/arena/ceil{k}', [f'# Plafond de barrière (garde les flèches dans l’arène {a["name"]}) ; retiré à la prochaine construction de la carte',
                                 f'fill {x1} {y} {z1} {x2} {y} {z2} minecraft:barrier replace #minecraft:air'])

w('var/arena/setup', ['# Construit l’arène $ar et place les joueurs (@a[tag=mg.play]). Généré.'] +
  [f'execute if score $ar mg.st matches {a["k"]} run function mg:var/arena/a{a["k"]}' for a in ARENAS])
w('var/arena/ceil', ['# Plafond de barrière pour One in the Chamber sur les arènes ouvertes. Généré.'] +
  [f'execute if score $ar mg.st matches {a["k"]} run function mg:var/arena/ceil{a["k"]}' for a in ARENAS if a['ceil']])
w('var/spread_one', ['# Réapparition (@s) dans l’arène de la variante (storage mg:var a = x z r under)',
                     'function mg:var/spread_m with storage mg:var a'])
w('var/spread_m', ['# Macro : placement aléatoire de @s dans l’arène',
                   '$spreadplayers $(x) $(z) 2 $(r) under $(u) false @s'])

# ============================================================ modes de combat : préparation + réglages
w('var/mode/pvp_prepare', [
    '# Arène PvP sur une autre carte ($ar) — appelé par pvp/prepare. Généré.',
    'function mg:var/arena/setup',
    'scoreboard players reset @a mg.pk'])
w('var/mode/pvp_go', [
    '# Arène PvP, variante : kit selon la difficulté (appelé à la fin de pvp/go). Généré.',
    'execute if score $dif mg.st matches 1 run give @a[tag=mg.play] minecraft:golden_apple 2',
    'execute if score $dif mg.st matches 1 run give @a[tag=mg.play] minecraft:arrow 16',
    'execute if score $dif mg.st matches 3.. run item replace entity @a[tag=mg.play] weapon.offhand with minecraft:air',
    'execute if score $dif mg.st matches 3 run clear @a[tag=mg.play] minecraft:golden_apple 1',
    'execute if score $dif mg.st matches 4 run clear @a[tag=mg.play] minecraft:golden_apple',
    'execute if score $dif mg.st matches 4 run item replace entity @a[tag=mg.play] armor.chest with minecraft:leather_chestplate',
    'execute if score $dif mg.st matches 4 run tellraw @a[tag=mg.play] {"text":"★★★★ Pas de bouclier, pas de pomme d’or, plastron en cuir : chaque coup compte.","color":"red"}'])
w('var/mode/oitc_prepare', [
    '# One in the Chamber sur une autre carte ($ar) — appelé par oitc/prepare. Généré.',
    'kill @e[distance=0..,type=minecraft:arrow]',
    'function mg:var/arena/setup',
    'function mg:var/arena/ceil',
    'scoreboard players reset @a mg.pk',
    'scoreboard players set @a[tag=mg.play] mg.lv 3',
    'scoreboard players set @a[tag=mg.play] mg.ok 0',
    'scoreboard players set @a[tag=mg.play] mg.cd 0'])
w('var/mode/oitc_go', [
    '# One in the Chamber, variante : kills pour gagner ($og) et flèches enchantées ($osi). Généré.',
    'execute if score $dif mg.st matches 1 run scoreboard players set $og mg.st 7',
    'execute if score $dif mg.st matches 4 run scoreboard players set $og mg.st 12',
    'execute if score $dif mg.st matches 1 run scoreboard players set $osi mg.st 300',
    'execute if score $dif mg.st matches 3 run scoreboard players set $osi mg.st 900',
    'execute if score $dif mg.st matches 4 run scoreboard players set $osi mg.st 2000000000',
    'tellraw @a[tag=mg.play] [{"text":"➶ Objectif de la variante : ","color":"gold"},{"score":{"name":"$og","objective":"mg.st"},"color":"yellow","bold":true},{"text":" kills.","color":"gold"}]'])
qsz = {'XS': (20, 7200), 'S': (20, 7200), 'M': (25, 9600), 'L': (30, 12000), 'XL': (30, 12000)}
L = ['# Quakecraft sur une autre carte ($ar) — appelé par quake/prepare. Généré.',
     'kill @e[distance=0..,type=minecraft:item]',
     'scoreboard players reset @a mg.qs', 'tag @a remove mg.prot', 'tag @a remove mg.qdd', 'tag @a remove mg.qsh']
for a in ARENAS:
    g, t = qsz[a['size']]
    L += [f'execute if score $ar mg.st matches {a["k"]} run scoreboard players set $qg mg.st {g}',
          f'execute if score $ar mg.st matches {a["k"]} run scoreboard players set $qt mg.st {t}']
L += ['scoreboard players set $qcd mg.st 22',
      'execute if score $dif mg.st matches 1 run scoreboard players set $qcd mg.st 16',
      'execute if score $dif mg.st matches 3 run scoreboard players set $qcd mg.st 28',
      'execute if score $dif mg.st matches 4 run scoreboard players set $qcd mg.st 34',
      'function mg:var/arena/setup',
      'scoreboard players set @a[tag=mg.play] mg.qk 0', 'scoreboard players set @a[tag=mg.play] mg.cd 0']
w('var/mode/quake_prepare', L)
w('var/mode/tnttag_prepare', [
    '# TNT Tag sur une autre carte ($ar) — appelé par tnttag/prepare. Généré.',
    'function mg:var/arena/setup',
    'scoreboard players operation $tty mg.st = $ky mg.st'])
w('var/mode/tnttag_go', [
    '# TNT Tag, variante : durée de la bombe = base + 5 s par survivant en plus, plafonnée. Généré.',
    'execute if score $dif mg.st matches 1 run scoreboard players set $ttb mg.st 300',
    'execute if score $dif mg.st matches 1 run scoreboard players set $mx mg.st 800',
    'execute if score $dif mg.st matches 3 run scoreboard players set $ttb mg.st 160',
    'execute if score $dif mg.st matches 3 run scoreboard players set $mx mg.st 450',
    'execute if score $dif mg.st matches 4 run scoreboard players set $ttb mg.st 120',
    'execute if score $dif mg.st matches 4 run scoreboard players set $mx mg.st 300'])

# ============================================================ sols : construction, rétrécissement, étage du haut, décroissance
def box(l):
    H = max(f[1] for f in l['floors']) + 1
    ys = [f[0] for f in l['floors']]
    return H, min(ys), max(ys)


GH = max(box(l)[0] for l in LAYOUTS)
GY1 = min(box(l)[1] for l in LAYOUTS) - 6
GY2 = max(box(l)[2] for l in LAYOUTS) + 7
for l in LAYOUTS:
    k = l['k']
    H, ymin, ymax = box(l)
    for mat in ('snow_block', 'white_wool'):
        tag = 'snow' if mat == 'snow_block' else 'wool'
        L = [f'# Sol {k} « {l["name"]} » en {mat} (centre {FX} ~ {FZ}). Généré.',
             '# Nettoyage couche par couche (limite de volume de /fill)']
        for y in range(GY1, GY2 + 1):   # boîte commune à tous les sols (efface le sol précédent, quel qu'il soit)
            L.append(f'fill {FX - GH - 1} {y} {FZ - GH - 1} {FX + GH + 1} {y} {FZ + GH + 1} minecraft:air')
        for (y, h, hole) in l['floors']:
            L.append(f'fill {FX - h} {y} {FZ - h} {FX + h} {y} {FZ + h} minecraft:{mat}')
            if hole:
                L.append(f'fill {FX - hole} {y} {FZ - hole} {FX + hole} {y} {FZ + hole} minecraft:air')
        y1, y2 = ymin - 6, ymax + 7
        L += [f'fill {FX - H - 1} {y1} {FZ - H - 1} {FX + H + 1} {y2} {FZ - H - 1} minecraft:barrier',
              f'fill {FX - H - 1} {y1} {FZ + H + 1} {FX + H + 1} {y2} {FZ + H + 1} minecraft:barrier',
              f'fill {FX - H - 1} {y1} {FZ - H} {FX - H - 1} {y2} {FZ + H} minecraft:barrier',
              f'fill {FX + H + 1} {y1} {FZ - H} {FX + H + 1} {y2} {FZ + H} minecraft:barrier']
        w(f'var/floor/l{k}/build_{tag}', L)

    # placement : sur l'étage du haut
    top_y, top_h, top_hole = l['floors'][0]
    sp = [f'# Sol {k} : perchoir, élimination, placement sur l’étage du haut. Généré.',
          'scoreboard players set $px mg.st 0', f'scoreboard players set $py mg.st {ymax + 10}', f'scoreboard players set $pz mg.st {FZ}',
          f'scoreboard players set $yd mg.st {ymin - 4}', f'scoreboard players set $ky mg.st {ymin - 4}',
          f'scoreboard players set $nf mg.st {len(l["floors"])}',
          'gamemode adventure @a[tag=mg.play]',
          f'execute as @a[tag=mg.play] run spawnpoint @s {FX} {top_y + 8} {FZ}']
    if top_hole:
        # anneau : 12 points fixes sur l'anneau (pas de départ au-dessus du trou)
        r = (top_h + top_hole) // 2 + 1
        pts = []
        for (px, pz) in [(-r, -r), (0, -r), (r, -r), (r, 0), (r, r), (0, r), (-r, r), (-r, 0),
                         (-r + 3, -r), (r, -r + 3), (r - 3, r), (-r, r - 3)]:
            pts.append((FX + px + 0.5, top_y + 1, FZ + pz + 0.5))
        sp.append('tag @a remove mg.tts')
        for _ in range(2):
            for (px, py, pz) in pts:
                sp.append(f'execute as @r[tag=mg.play,tag=!mg.tts] run function mg:tnttag/map/sp {{x:{px},y:{py},z:{pz},fx:{FX + 0.5},fz:{FZ + 0.5}}}')
        sp += [f'tp @a[tag=mg.play,tag=!mg.tts] {pts[0][0]} {pts[0][1]} {pts[0][2]}', 'tag @a remove mg.tts']
    else:
        sp.append(f'spreadplayers {FX} {FZ} 3 {max(2, top_h - 2)} under {top_y + 2} false @a[tag=mg.play]')
    w(f'var/floor/l{k}/place', sp)

    # rétrécissement (Spleef) : étape s retire l'anneau extérieur de chaque étage, taille mini 9×9 (ou trou + 2)
    for s in range(1, 11):
        L = [f'# Sol {k}, rétrécissement étape {s} (neige). Généré.']
        for (y, h, hole) in l['floors']:
            rr = h - s + 1
            if rr - 1 < max(4, hole + 2):
                continue
            L += [f'fill {FX - rr} {y} {FZ - rr} {FX + rr} {y} {FZ - rr} minecraft:air replace minecraft:snow_block',
                  f'fill {FX - rr} {y} {FZ + rr} {FX + rr} {y} {FZ + rr} minecraft:air replace minecraft:snow_block',
                  f'fill {FX - rr} {y} {FZ - rr + 1} {FX - rr} {y} {FZ + rr - 1} minecraft:air replace minecraft:snow_block',
                  f'fill {FX + rr} {y} {FZ - rr + 1} {FX + rr} {y} {FZ + rr - 1} minecraft:air replace minecraft:snow_block']
        w(f'var/floor/l{k}/shrink_{s}', L)

    # décroissance TNT Run
    L = [f'# Sol {k}, TNT Run : laine orange → vide, rouge → orange. Généré.', 'scoreboard players operation $dk mg.st = $vdk mg.st']
    for (y, h, hole) in l['floors']:
        L.append(f'fill {FX - h} {y} {FZ - h} {FX + h} {y} {FZ + h} minecraft:air replace minecraft:orange_wool')
    for (y, h, hole) in l['floors']:
        L.append(f'fill {FX - h} {y} {FZ - h} {FX + h} {y} {FZ + h} minecraft:orange_wool replace minecraft:red_wool')
    w(f'var/floor/l{k}/decay', L)

    # étage du haut (Spleef / Splegg) : même logique que spleef/top_check, sur les 3 étages du haut
    fl = l['floors'][:3]
    L = [f'# Sol {k} : un seul joueur reste sur l’étage occupé le plus haut → il disparaît après 15 s. Généré.',
         'scoreboard players set $tfn mg.st 0', 'scoreboard players set #tf20 mg.st 20']
    for i, (y, h, hole) in enumerate(fl, 1):
        L.append(f'execute store result score $tf{i} mg.st if entity @a[tag=mg.play,scores={{mg.t={y + 1}..}}]')
    L.append('execute if score $tf1 mg.st matches 1 if score $alive mg.st matches 2.. run scoreboard players set $tfn mg.st 1')
    if len(fl) > 1:
        L.append('execute if score $tf1 mg.st matches 0 if score $tf2 mg.st matches 1 if score $alive mg.st matches 2.. run scoreboard players set $tfn mg.st 2')
    if len(fl) > 2:
        L.append('execute if score $tf1 mg.st matches 0 if score $tf2 mg.st matches 0 if score $tf3 mg.st matches 1 if score $alive mg.st matches 2.. run scoreboard players set $tfn mg.st 3')
    L += ['execute if score $tfn mg.st matches 0 run return run scoreboard players set $tff mg.st 0',
          'execute unless score $tfn mg.st = $tff mg.st run tellraw @a[tag=!mg.surv] [{"text":"⚠ ","color":"gold"},{"text":"Un joueur est seul en haut : l\'étage disparaît dans 15 secondes !","color":"gold"}]',
          'execute unless score $tfn mg.st = $tff mg.st run scoreboard players set $tfc mg.st 300',
          'scoreboard players operation $tff mg.st = $tfn mg.st',
          'scoreboard players remove $tfc mg.st 1',
          'scoreboard players operation $tfs mg.st = $tfc mg.st',
          'scoreboard players add $tfs mg.st 19',
          'scoreboard players operation $tfs mg.st /= #tf20 mg.st',
          'title @a[tag=!mg.surv,tag=!mg.lk] actionbar [{"text":"⚠ L\'étage du haut disparaît dans ","color":"gold"},{"score":{"name":"$tfs","objective":"mg.st"},"color":"red","bold":true},{"text":" s","color":"gold"}]',
          'execute if score $tfc mg.st matches 1.. run return 0']
    for i, (y, h, hole) in enumerate(fl, 1):
        L.append(f'execute if score $tff mg.st matches {i} run fill {FX - h} {y} {FZ - h} {FX + h} {y} {FZ + h} minecraft:air replace minecraft:snow_block')
    L += ['tellraw @a[tag=!mg.surv] [{"text":"💥 L\'étage du haut a disparu !","color":"red","bold":true}]',
          'execute as @a[tag=mg.play] at @s run playsound minecraft:block.snow.break master @s ~ ~ ~ 1 0.5',
          'scoreboard players set $tff mg.st 0']
    w(f'var/floor/l{k}/top_check', L)

disp = lambda name: [f'execute if score $ar mg.st matches {l["k"]} run function mg:var/floor/l{l["k"]}/{name}' for l in LAYOUTS]
w('var/floor/top_check', ['# Étage du haut (Spleef / Splegg en variante). Généré.'] + disp('top_check'))
w('var/floor/decay', ['# TNT Run en variante : décroissance sur le sol $ar. Généré.'] + disp('decay'))
L = ['# Spleef en variante : rétrécissement (étape $ss, intervalle $vsk2). Généré.',
     'scoreboard players add $ss mg.st 1', 'scoreboard players operation $sk mg.st = $vsk2 mg.st']
for l in LAYOUTS:
    for s in range(1, 11):
        L.append(f'execute if score $ar mg.st matches {l["k"]} if score $ss mg.st matches {s} run function mg:var/floor/l{l["k"]}/shrink_{s}')
L.append('execute as @a[tag=!mg.surv] at @s run playsound minecraft:block.snow.break master @s ~ ~ ~ 1 0.6')
w('var/floor/shrink', L)


def floor_prepare(mode, tag, extra):
    L = [f'# {mode["name"]} sur un autre sol ($ar) — appelé par {mode["key"]}/prepare. Généré.']
    for l in LAYOUTS:
        L.append(f'execute if score $ar mg.st matches {l["k"]} run function mg:var/floor/l{l["k"]}/build_{tag}')
    L += [f'kill @e[type=minecraft:item,x={FX - 40},y=40,z={FZ - 40},dx=80,dy=70,dz=80]']
    L += extra
    for l in LAYOUTS:
        L.append(f'execute if score $ar mg.st matches {l["k"]} run function mg:var/floor/l{l["k"]}/place')
    return L


w('var/mode/spleef_prepare', floor_prepare(FLOOR_MODES[0], 'snow', [
    'scoreboard players set $vsk1 mg.st 800', 'scoreboard players set $vsk2 mg.st 240',
    'execute if score $dif mg.st matches 1 run scoreboard players set $vsk1 mg.st 1000',
    'execute if score $dif mg.st matches 1 run scoreboard players set $vsk2 mg.st 300',
    'execute if score $dif mg.st matches 3 run scoreboard players set $vsk1 mg.st 600',
    'execute if score $dif mg.st matches 3 run scoreboard players set $vsk2 mg.st 180',
    'execute if score $dif mg.st matches 4 run scoreboard players set $vsk1 mg.st 400',
    'execute if score $dif mg.st matches 4 run scoreboard players set $vsk2 mg.st 120']))
w('var/mode/spleef_go', ['# Spleef, variante : premier rétrécissement selon la difficulté (après spleef/go). Généré.',
                         'scoreboard players operation $sk mg.st = $vsk1 mg.st'])
w('var/mode/tntrun_prepare', floor_prepare(FLOOR_MODES[1], 'wool', [
    'scoreboard players set $vdk mg.st 9',
    'execute if score $dif mg.st matches 1 run scoreboard players set $vdk mg.st 12',
    'execute if score $dif mg.st matches 3 run scoreboard players set $vdk mg.st 7',
    'execute if score $dif mg.st matches 4 run scoreboard players set $vdk mg.st 5',
    'scoreboard players operation $dk mg.st = $vdk mg.st']))
w('var/mode/splegg_prepare', floor_prepare(FLOOR_MODES[2], 'snow', [
    'kill @e[distance=0..,type=minecraft:egg]',
    f'kill @e[type=minecraft:chicken,x={FX - 40},y=40,z={FZ - 40},dx=80,dy=70,dz=80]',
    'scoreboard players set $vrs mg.st 160', 'scoreboard players set $vcr mg.st 0',
    'execute if score $dif mg.st matches 1 run scoreboard players set $vrs mg.st 60',
    'execute if score $dif mg.st matches 3.. run scoreboard players set $vcr mg.st 1',
    'execute if score $dif mg.st matches 4 run scoreboard players set $vrs mg.st 240']))

w('var/fl', ['# Zones chargées des variantes (sols, centre 0 ~ 24300). Généré.',
             f'forceload add {FX - 48} {FZ - 48} {FX + 48} {FZ + 48}'])

# ============================================================ menus
def label_for(v):
    st = v['dif']
    return [{'text': f'✦ {v["map"]["name"]} ', 'color': v['map']['col']},
            {'text': '★' * st, 'color': 'gold'}, {'text': '☆' * (4 - st), 'color': 'dark_gray'}]


def tip_for(v):
    return [{'text': f'Carte {v["map"]["src"]} : {v["map"]["desc"]}\n', 'color': 'gray'},
            {'text': 'Réglages : ' + SET[v['mode']['key']][v['dif'] - 1], 'color': 'gold'}]


# tag de blocs traversés par le rayon du Quake
wjson(os.path.join(D, 'tags/block/ray_pass.json'), {'values': [
    '#minecraft:air', 'minecraft:short_grass', 'minecraft:tall_grass', 'minecraft:fern', 'minecraft:large_fern',
    '#minecraft:small_flowers', 'minecraft:dead_bush', '#minecraft:wool_carpets', 'minecraft:moss_carpet',
    'minecraft:water', 'minecraft:snow', 'minecraft:vine', 'minecraft:light', 'minecraft:sugar_cane',
    {'id': 'minecraft:short_dry_grass', 'required': False}, {'id': 'minecraft:tall_dry_grass', 'required': False},
    {'id': 'minecraft:bush', 'required': False}, {'id': 'minecraft:leaf_litter', 'required': False}]})


# ============================================================ crochets dans les fichiers existants (idempotents)
MARK = '[variantes]'


def patch(rel, anchor, new_lines, where='after', count=1):
    """Insère new_lines (marquées) avant/après la ligne qui contient exactement `anchor` ; ne fait rien si déjà fait."""
    path = os.path.join(F, rel + '.mcfunction')
    txt = open(path, encoding='utf-8').read()
    if all(l in txt for l in new_lines):
        return
    lines = txt.split('\n')
    idx = [i for i, l in enumerate(lines) if l == anchor]
    if len(idx) != count:
        raise SystemExit(f'{rel} : ancre introuvable ou multiple ({len(idx)}) : {anchor!r}')
    i = idx[0] + (1 if where == 'after' else 0)
    lines[i:i] = new_lines
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines))


def replace(rel, old, new):
    path = os.path.join(F, rel + '.mcfunction')
    txt = open(path, encoding='utf-8').read()
    if new in txt:
        return
    if txt.count(old) != 1:
        raise SystemExit(f'{rel} : texte à remplacer introuvable ou multiple : {old!r}')
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(txt.replace(old, new))


VR = 'execute if score $ar mg.st matches 1.. run return run function mg:var/'

# core
patch('core/request', 'scoreboard players reset @s mg.go', [
    f'# {MARK} ids 100..196 : carte d\'un autre jeu + difficulté ($ar, $dif) ; $ar = 0 → carte native',
    'scoreboard players set $ar mg.st 0',
    'scoreboard players set $dif mg.st 2',
    'execute if score $game mg.st matches 100..196 run function mg:var/remap'])
patch('core/request', '# Préparation de l\'arène + téléportation', [
    f'# {MARK} annonce de la variante puis $game = jeu réel',
    'execute if score $ar mg.st matches 1.. run function mg:var/start'], where='before')
if 'matches 100..196' not in open(os.path.join(F, 'core/go.mcfunction'), encoding='utf-8').read():
    replace('core/go', 'execute unless score @s mg.go matches 1..78 run return run scoreboard players reset @s mg.go',
            'execute unless score @s mg.go matches 1..78 unless score @s mg.go matches 100..196 run return run scoreboard players reset @s mg.go')
patch('core/forceloads', 'function mg:tnttag/map/fl', [f'# {MARK} sols des variantes (z 24300)', 'function mg:var/fl'])
patch('core/opt', 'execute if score @s mg.opt matches 1 run function mg:core/opt_spec', [
    'execute if score @s mg.opt matches 32..39 unless entity @s[tag=mg.admin] run tellraw @s {"text":"⚠ Menus de lancement réservés aux admins.","color":"red"}',
    'execute if score @s mg.opt matches 32..39 if entity @s[tag=mg.admin] run function mg:var/menu/open'], where='before')

# PvP
patch('pvp/prepare', '# Arène PvP — préparation', [VR + 'mode/pvp_prepare'])
replace('pvp/tick', 'execute as @a[tag=mg.play,scores={mg.t=..55}] run function mg:core/eliminate',
        'execute if score $ar mg.st matches 0 as @a[tag=mg.play,scores={mg.t=..55}] run function mg:core/eliminate\n'
        f'execute if score $ar mg.st matches 1.. as @a[tag=mg.play] if score @s mg.t <= $ky mg.st run function mg:core/eliminate')
patch('pvp/go', 'tellraw @a[tag=mg.play] [{"text":"⚔ Chacun pour soi : dernier survivant = gagnant !","color":"yellow"}]',
      ['execute if score $ar mg.st matches 1.. run function mg:var/mode/pvp_go'])

# One in the Chamber
patch('oitc/prepare', '# One in the Chamber — préparation (centre 0 ~ 5800)', [VR + 'mode/oitc_prepare'])
replace('oitc/death', 'execute if score $om mg.st matches 0 run spreadplayers 0 5800 5 10 under 90 false @s',
        'execute if score $ar mg.st matches 1.. run function mg:var/spread_one\n'
        'execute if score $ar mg.st matches 0 if score $om mg.st matches 0 run spreadplayers 0 5800 5 10 under 90 false @s')
replace('oitc/death', 'execute if score $om mg.st matches 1 run spreadplayers',
        'execute if score $ar mg.st matches 0 if score $om mg.st matches 1 run spreadplayers')
replace('oitc/death', 'execute if score $om mg.st matches 2 run spreadplayers',
        'execute if score $ar mg.st matches 0 if score $om mg.st matches 2 run spreadplayers')
replace('oitc/tick', 'execute as @a[tag=mg.play,scores={mg.t=..70}] run function mg:oitc/death',
        'execute if score $ar mg.st matches 0 as @a[tag=mg.play,scores={mg.t=..70}] run function mg:oitc/death\n'
        'execute if score $ar mg.st matches 1.. as @a[tag=mg.play] if score @s mg.t <= $ky mg.st run function mg:oitc/death')
replace('oitc/tick', 'execute if score $os mg.st matches 600.. run function mg:oitc/special_timer',
        'execute if score $os mg.st >= $osi mg.st run function mg:oitc/special_timer')
replace('oitc/tick', 'execute if score $state mg.st matches 2 as @a[tag=mg.play,scores={mg.ok=10..},limit=1] run function mg:core/win_player',
        'execute if score $state mg.st matches 2 as @a[tag=mg.play] if score @s mg.ok >= $og mg.st run return run function mg:core/win_player')
patch('oitc/go', 'scoreboard players set $og mg.st 10', ['scoreboard players set $osi mg.st 600',
                                                          'execute if score $ar mg.st matches 1.. run function mg:var/mode/oitc_go'])
replace('oitc/kill_reward', '{"text":" / 10  ","color":"gray"}',
        '{"text":" / ","color":"gray"},{"score":{"name":"$og","objective":"mg.st"},"color":"gray"},{"text":"  ","color":"gray"}')

# Quakecraft
patch('quake/prepare', '# Quakecraft — préparation (carte $qm : 0 néon, 1 volcan XL, 2 jungle XL, 3 désert, 4 glacier mini)',
      ['scoreboard players set $qcd mg.st 22', VR + 'mode/quake_prepare'])
patch('quake/spread_one', '# Quakecraft — placement aléatoire selon la carte (@s)', [VR + 'spread_one'])
replace('quake/tick', 'execute as @a[tag=mg.play,scores={mg.t=..70}] run function mg:quake/respawn',
        'execute if score $ar mg.st matches 0 as @a[tag=mg.play,scores={mg.t=..70}] run function mg:quake/respawn\n'
        'execute if score $ar mg.st matches 1.. as @a[tag=mg.play] if score @s mg.t <= $ky mg.st run function mg:quake/respawn')
replace('quake/shoot', 'scoreboard players set @s mg.cd 22', 'scoreboard players operation @s mg.cd = $qcd mg.st')
replace('quake/ray', 'execute unless block ~ ~ ~ #minecraft:air run return run', 'execute unless block ~ ~ ~ #mg:ray_pass run return run')

# TNT Tag
patch('tnttag/prepare', 'tag @a remove mg.bomb', [VR + 'mode/tnttag_prepare'])
patch('tnttag/go', 'scoreboard players set $mx mg.st 600', ['scoreboard players set $ttb mg.st 200',
                                                             'execute if score $ar mg.st matches 1.. run function mg:var/mode/tnttag_go'])
replace('tnttag/new_round', 'scoreboard players add $tt mg.st 200', 'scoreboard players operation $tt mg.st += $ttb mg.st')

# Spleef
patch('spleef/prepare', '# Spleef — préparation (appelé au lancement)', [VR + 'mode/spleef_prepare'])
patch('spleef/go', 'scoreboard players set $sk mg.st 800', ['execute if score $ar mg.st matches 1.. run function mg:var/mode/spleef_go'])
patch('spleef/shrink', '# Spleef — l\'arène rétrécit (appelé toutes les 12 s après les 40 premières secondes)', [VR + 'floor/shrink'])
patch('spleef/top_check', 'scoreboard players set $tfn mg.st 0', [VR + 'floor/top_check'], where='before')

# TNT Run
patch('tntrun/prepare', '# TNT Run — préparation', [VR + 'mode/tntrun_prepare'])
replace('tntrun/tick', 'execute as @a[tag=mg.play,scores={mg.t=..58}] run function mg:core/eliminate',
        'execute if score $ar mg.st matches 0 as @a[tag=mg.play,scores={mg.t=..58}] run function mg:core/eliminate\n'
        'execute if score $ar mg.st matches 1.. as @a[tag=mg.play] if score @s mg.t <= $ky mg.st run function mg:core/eliminate')
patch('tntrun/decay', '# (un bloc piétiné disparaît entre 9 et 18 ticks plus tard, jamais instantanément)', [VR + 'floor/decay'])

# Splegg
patch('splegg/prepare', '# Splegg — préparation (centre 0 ~ 4200) ; $sg = 1 → version XXL', [VR + 'mode/splegg_prepare'])
patch('splegg/shoot', 'scoreboard players set $rs mg.st 160', ['execute if score $ar mg.st matches 1.. run scoreboard players operation $rs mg.st = $vrs mg.st'])
patch('splegg/hit', 'execute if score $sg mg.st matches 1 run fill ~-1 ~ ~-1 ~1 ~ ~1 minecraft:air replace minecraft:snow_block',
      ['execute if score $ar mg.st matches 1.. if score $vcr mg.st matches 1 run fill ~-1 ~ ~-1 ~1 ~ ~1 minecraft:air replace minecraft:snow_block'])
patch('splegg/top_check', 'scoreboard players set $tfn mg.st 0', [VR + 'floor/top_check'], where='before')

# désinstallation
patch('desinstaller', 'forceload remove all', ['data remove storage mg:var a'])


patch('core/menu_chat', 'tellraw @s ["",{"text":" [🪽 Élytra ▸]","color":"aqua","click_event":{"action":"run_command","command":"trigger mg.opt set 31"},"hover_event":{"action":"show_text","value":"Course d\'anneaux, course + combat, survie en vol"}}]',
      ['tellraw @s ' + js(['', {'text': f' [★ Variantes ({len(VARIANTS)}) ▸]', 'color': 'gold',
                                'click_event': {'action': 'run_command', 'command': 'trigger mg.opt set 32'},
                                'hover_event': {'action': 'show_text', 'value': 'Chaque mode sur les cartes des autres jeux, de ★ à ★★★★'}}])])

# ============================================================ arbre des menus
# Menu principal = catégories ; catégorie = jeux ; jeu = cartes natives puis variantes (★ → ★★★★).
def load_dialog(name):
    p = os.path.join(D, f'dialog/{name}.json')
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else None


def save_dialog(name, d):
    wjson(os.path.join(D, f'dialog/{name}.json'), d)


def act(label, col, cmd, tip=None, bold=False):
    a = {'label': [{'text': label, 'color': col, **({'bold': True} if bold else {})}]}
    if tip:
        a['tooltip'] = [{'text': tip, 'color': 'gray'}]
    a['action'] = {'type': 'minecraft:run_command', 'command': cmd}
    return a


def is_generated(a):
    cmd = a.get('action', {}).get('command', '')
    m = re.match(r'trigger mg\.(go|opt) set (\d+)$', cmd)
    return bool(m) and ((m.group(1) == 'go' and 100 <= int(m.group(2)) <= 196) or (m.group(1) == 'opt' and 32 <= int(m.group(2)) <= 39))


def is_back(a):
    lab = a['label'][0]['text'] if isinstance(a['label'], list) else a['label']
    return lab.startswith('«')


# actions existantes (pour garder leurs infobulles), lues dans tous les menus
KNOWN = {}
for f in sorted(os.listdir(os.path.join(D, 'dialog'))):
    if f.endswith('.json') and (f in ('menu.json', 'pvp.json') or f.startswith('cat_')):
        for a in load_dialog(f[:-5]).get('actions', []):
            KNOWN.setdefault(a.get('action', {}).get('command'), a)


def known(cmd, label, col, tip=None):
    return KNOWN.get(cmd) or act(label, col, cmd, tip)


BODY_NOTE = [{'text': '\nCartes d’origine, puis ✦ variantes (ce jeu sur la carte d’un autre jeu, réglages adaptés). ', 'color': 'gray'},
             {'text': '★', 'color': 'gold'}, {'text': ' facile → ', 'color': 'gray'}, {'text': '★★★★', 'color': 'gold'},
             {'text': ' difficile.', 'color': 'gray'}]
OPT_CAT = {'sols': 40, 'equipes': 41, 'courses': 42, 'fete': 43, 'votes': 44, 'joueur': 45, 'kart': 46, 'arcade': 47, 'combat': 14,
           # choix de la carte des jeux d'arcade (cartes supplémentaires : tools/arcade/gen_maps.py)
           'tron': 50, 'koth': 51, 'uhc': 52, 'hg': 53, 'zombies': 54, 'infection': 55, 'wii': 56, 'autotamp': 57}
SUB = {'pvp': ('sub_pvparena', 'combat'), 'oitc': ('sub_oitc', 'combat'), 'quake': ('quakemaps', 'combat'),
       'tnttag': ('sub_tnttag', 'combat'), 'spleef': ('sub_spleef', 'sols'), 'tntrun': ('sub_tntrun', 'sols'),
       'splegg': ('sub_splegg', 'sols')}
NEW_SUB = {'spleef': ('❄ Spleef', 'aqua', [act('❄ Spleef (tour de neige)', 'aqua', 'trigger mg.go set 1', 'Carte d’origine : 4 étages de neige')]),
           'tntrun': ('✷ TNT Run', 'red', [act('✷ TNT Run (3 étages de laine)', 'red', 'trigger mg.go set 2', 'Carte d’origine')])}


def back(cat):
    if cat == 'menu':
        return act('« Retour au menu', 'yellow', 'trigger mg.menu')
    return act('« Retour', 'yellow', f'trigger mg.opt set {OPT_CAT[cat]}')


for m in MODES:
    name, parent = SUB[m['key']]
    d = load_dialog(name)
    if d is None:
        t, col, natives = NEW_SUB[m['key']]
        d = {'type': 'minecraft:multi_action', 'title': {'text': t, 'color': col, 'bold': True}, 'pause': False,
             'can_close_with_escape': True, 'body': [{'type': 'minecraft:plain_message', 'contents': [{'text': 'Choisis la carte.', 'color': 'gray'}]}],
             'columns': 2, 'exit_action': {'label': [{'text': 'Fermer', 'color': 'gray'}]}, 'actions': natives}
    natives = [a for a in d['actions'] if not is_generated(a) and not is_back(a)]
    vacts = [act(f'🎲 Variante au hasard', 'gold', f'trigger mg.go set {m["rnd"]}', f'Une des {len(m["vars"])} variantes ★, tirée au sort')]
    for v in sorted(m['vars'], key=lambda v: (v['dif'], v['id'])):
        vacts.append({'label': label_for(v), 'tooltip': tip_for(v),
                      'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.go set {v["id"]}'}})
    d['actions'] = natives + vacts + [back(parent)]
    body = d['body'][0]['contents']
    cut = next((i for i, c in enumerate(body) if isinstance(c, dict) and c.get('text', '').startswith('\n') and ('variante' in c.get('text', ''))), None)
    if cut is not None:
        del body[cut:]
    body += BODY_NOTE
    save_dialog(name, d)
    L = [f'# {m["name"]} : cartes + variantes (@s = admin) — fenêtre, sinon menu texte. Généré.',
         'scoreboard players set $dlg mg.st 0',
         f'execute store success score $dlg mg.st run dialog show @s mg:{name}',
         'execute if score $dlg mg.st matches 1 run return 0',
         'tellraw @s ' + js([{'text': f'\n{m["icon"]} {m["name"]} — variantes ', 'color': m['col'], 'bold': True},
                             {'text': '(★ facile → ★★★★ difficile)', 'color': 'gray'}]),
         'tellraw @s ' + js(['', {'text': ' [🎲 Au hasard]', 'color': 'gold',
                                  'click_event': {'action': 'run_command', 'command': f'trigger mg.go set {m["rnd"]}'}}])]
    for v in sorted(m['vars'], key=lambda v: (v['dif'], v['id'])):
        L.append('tellraw @s ' + js(['', {'text': ' [' + v['map']['name'] + ' ', 'color': v['map']['col'],
                                         'click_event': {'action': 'run_command', 'command': f'trigger mg.go set {v["id"]}'},
                                         'hover_event': {'action': 'show_text', 'value': tip_for(v)}},
                                        {'text': '★' * v['dif'], 'color': 'gold'}, {'text': '☆' * (4 - v['dif']) + ']', 'color': 'dark_gray'}]))
    w(f'var/menu/{m["key"]}', L)

for f in os.listdir(os.path.join(D, 'dialog')):      # anciens menus séparés des variantes
    if f.startswith('var_') and f.endswith('.json'):
        os.remove(os.path.join(D, 'dialog', f))

OPEN = lambda o: f'trigger mg.opt set {o}'
CATS = {
    'sols': ('❄ Jeux de sol', 'aqua', 'Casse, cours, pousse : le dernier debout gagne.', [
        act('❄ Spleef ▸', 'aqua', OPEN(37), 'Casse la neige sous les autres'),
        act('✷ TNT Run ▸', 'red', OPEN(38), 'Le sol disparaît sous tes pas'),
        known(OPEN(17), '❍ Splegg ▸', 'yellow'), known(OPEN(18), '✊ Sumo ▸', 'gold'),
        known('trigger mg.go set 28', '▦ Block Party', 'light_purple'),
        act('▦ Block Party — bandes', 'light_purple', 'trigger mg.go set 91', 'Le sol est fait de bandes de couleur'),
        act('▦ Block Party — mixte', 'light_purple', 'trigger mg.go set 92', 'Carrés ou bandes, ça change à chaque manche'), known(OPEN(20), '⚓ Pluie d\'Enclumes ▸', 'dark_gray')], 'menu'),
    'equipes': ('⚑ Équipes', 'light_purple', 'Jeux en équipes.', [
        act('⚑ Bedwars ▸', 'light_purple', OPEN(30), 'Protège ton lit, détruis les autres'),
        act('☁ Sheep War ▸', 'white', OPEN(8), 'Moutons explosifs, 8 cartes'),
        known(OPEN(21), '▓ Paintball ▸', 'gold'), known('trigger mg.go set 30', '▮ Turf Wars', 'gold'),
        act('🏰 The Towers', 'gold', 'trigger mg.go set 88', 'Saute dans le puits adverse, 5 points pour gagner'),
        act('🚚 Convoi', 'gold', 'trigger mg.go set 89', 'Escorte ou bloque le convoi, 2 manches'),
        act('🚚 Convoi — coop', 'green', 'trigger mg.go set 90', 'Tous ensemble contre les monstres'),
        act('🚩 Capture the Flag', 'gold', 'trigger mg.go set 93', 'Ramène le drapeau adverse sur ton socle, 3 captures')], 'menu'),
    'courses': ('🏁 Courses et vol', 'gold', 'Le premier arrivé gagne.', [
        act('🏎 Kart ▸', 'gold', OPEN(46), 'Circuit Champignon, Royaume Koopa, Bataille'),
        known('trigger mg.go set 56', '⛵ Course de bateaux (glace)', 'aqua'),
        known(OPEN(28), '🪽 Course d\'élytres ▸', 'aqua'), known(OPEN(31), '🪽 Élytra ▸', 'aqua'),
        known(OPEN(19), '⬇ The Dropper ▸', 'aqua')], 'menu'),
    'arcade': ('🕹 Arcade', 'light_purple', 'Jeux d’adresse et de stratégie.', [
        act('⚡ Tron ▸', 'aqua', OPEN(50), 'À pied ou à moto, arène normale ou XXL'),
        act('👑 King of the Hill ▸', 'gold', OPEN(51), 'Solo ou équipes, 3 cartes'),
        act('⛏ Mini UHC Run ▸', 'gold', OPEN(52), '5 min : farm, PvP, zone qui rétrécit — 3 cartes'),
        act('🏹 Mini Hunger Games ▸', 'gold', OPEN(53), 'Coffres, corne d\'abondance — 3 cartes'),
        act('🧟 Zombies ▸', 'dark_green', OPEN(54), 'Coop, armes réelles, 10 manches — 3 cartes'),
        act('🧪 Infection ▸', 'green', OPEN(55), 'Survivants contre zombies contagieux — 3 cartes'),
        act('🎭 Prop Hunt', 'gold', 'trigger mg.go set 96', 'Cache-toi en objet, ou trouve les objets qui bougent'),
        act('💣 Bombardier', 'red', 'trigger mg.go set 99', 'Bombarde la ville du ciel, le plus de dégâts gagne, 2 min 30'),
        act('🦎 Meccha Chameleon', 'green', 'trigger mg.go set 198', 'Peins-toi aux couleurs du décor et cache-toi, ou chasse les caméléons'),
        act('🔴 1, 2, 3 Soleil', 'red', 'trigger mg.go set 220', 'Façon Squid Game : avance dos tourné, fige-toi quand la poupée regarde'),
        act('🚗 Autos tamponneuses ▸', 'aqua', OPEN(57), 'Bateaux sur la glace : tamponne, ne te fais pas tamponner'),
        act('🎾 Wii Sports ▸', 'aqua', OPEN(56), 'Bowling, golf, tennis : chacun sa piste')], 'menu'),
    'autotamp': ('🚗 Autos tamponneuses', 'aqua', 'Choisis le nombre de coups avant d\'être éliminé.', [
        act('🚗 3 coups', 'red', 'trigger mg.go set 222', 'Partie courte et brutale'),
        act('🚗 5 coups', 'aqua', 'trigger mg.go set 221', 'Le classique'),
        act('🚗 8 coups', 'green', 'trigger mg.go set 223', 'Partie longue')], 'arcade'),
    'wii': ('🎾 Wii Sports', 'aqua', 'Chacun sa piste, tout le monde joue en même temps.', [
        act('🎳 Bowling', 'light_purple', 'trigger mg.go set 214', '8 pistes, 5 frames, vraies règles (strike, spare)'),
        act('⛳ Golf', 'green', 'trigger mg.go set 215', '6 trous (par 23), chacun sa balle, le moins de coups gagne'),
        act('🎾 Tennis', 'yellow', 'trigger mg.go set 216', '1 contre 1 sur 4 courts (robot si joueur impair), 3 jeux gagnants')], 'arcade'),
    'tron': ('⚡ Tron', 'aqua', 'Choisis le mode et l\'arène.', [
        act('⚡ Tron à pied', 'aqua', 'trigger mg.go set 84', 'Arène 101×101 dans la pénombre'),
        act('🏍 Tron moto', 'gold', 'trigger mg.go set 85', 'À cheval, saut toutes les 20 s'),
        act('⚡ Tron à pied — XXL', 'aqua', 'trigger mg.go set 200', 'Arène géante 201×201'),
        act('🏍 Tron moto — XXL', 'gold', 'trigger mg.go set 201', 'Arène géante 201×201, à cheval')], 'arcade'),
    'koth': ('👑 King of the Hill', 'gold', 'Solo ou équipes, choisis la carte.', [
        act('👑 Solo — Colline', 'gold', 'trigger mg.go set 86', 'Colline en gradins, 60 points'),
        act('👑 Équipes — Colline', 'red', 'trigger mg.go set 87', 'Rouge contre Bleu, 90 points'),
        act('👑 Solo — Pyramide', 'gold', 'trigger mg.go set 206', 'Pyramide de grès dans le sable'),
        act('👑 Équipes — Pyramide', 'red', 'trigger mg.go set 207', 'Pyramide de grès, Rouge contre Bleu'),
        act('👑 Solo — Glacier', 'gold', 'trigger mg.go set 208', 'Colline de glace : ça glisse !'),
        act('👑 Équipes — Glacier', 'red', 'trigger mg.go set 209', 'Glacier, Rouge contre Bleu')], 'arcade'),
    'uhc': ('⛏ Mini UHC Run', 'gold', 'Choisis la carte.', [
        act('⛏ UHC — Plaines', 'green', 'trigger mg.go set 94', 'Plaines et forêts'),
        act('⛏ UHC — Désert', 'yellow', 'trigger mg.go set 202', 'Dunes, cactus, acacias'),
        act('⛏ UHC — Taïga enneigée', 'aqua', 'trigger mg.go set 204', 'Neige, sapins, lacs gelés')], 'arcade'),
    'hg': ('🏹 Mini Hunger Games', 'gold', 'Choisis la carte.', [
        act('🏹 HG — Plaines', 'green', 'trigger mg.go set 95', 'Plaines et forêts'),
        act('🏹 HG — Jungle', 'dark_green', 'trigger mg.go set 203', 'Jungle dense, roche moussue'),
        act('🏹 HG — Canyon', 'gold', 'trigger mg.go set 205', 'Terres cuites et sable rouge')], 'arcade'),
    'zombies': ('🧟 Zombies', 'dark_green', 'Choisis la carte.', [
        act('🧟 Zombies — Bunker', 'gray', 'trigger mg.go set 97', 'Le bunker d\'origine'),
        act('🧟 Zombies — Laboratoire', 'white', 'trigger mg.go set 210', 'Labo tout blanc'),
        act('🧟 Zombies — Manoir', 'dark_red', 'trigger mg.go set 212', 'Manoir sombre')], 'arcade'),
    'infection': ('🧪 Infection', 'green', 'Choisis la carte et le mode.', [
        act('🧪 Infection — Bunker', 'gray', 'trigger mg.go set 98', 'Le bunker d\'origine'),
        act('🧪 Infection — Laboratoire', 'white', 'trigger mg.go set 211', 'Labo tout blanc'),
        act('🧪 Infection — Manoir', 'dark_red', 'trigger mg.go set 213', 'Manoir sombre'),
        act('🧟 Joueurs vs mobs — Bunker', 'red', 'trigger mg.go set 217', 'Tous survivants contre des zombies mobs ; touché = infecté'),
        act('🧟 Joueurs vs mobs — Laboratoire', 'red', 'trigger mg.go set 218', 'Tous survivants contre des zombies mobs ; touché = infecté'),
        act('🧟 Joueurs vs mobs — Manoir', 'red', 'trigger mg.go set 219', 'Tous survivants contre des zombies mobs ; touché = infecté')], 'arcade'),
    'kart': ('🏎 Kart', 'gold', 'Choisis le circuit.', [
        known('trigger mg.go set 61', '🏎 KART : Circuit Champignon', 'gold'), known('trigger mg.go set 62', '🏎 KART : Royaume Koopa', 'red'),
        known('trigger mg.go set 63', '🎈 KART : Bataille', 'light_purple')], 'courses'),
    'fete': ('🎉 Fête et création', 'green', 'Les grands formats.', [
        known(OPEN(16), '★ Mini Party ▸', 'gold'), known(OPEN(22), '✎ Build Battle ▸', 'green'),
        act('📞 Téléphone (5+)', 'gold', 'trigger mg.go set 83', 'Mot → construction → devinette → construction → devinette. 5 à 12 joueurs.')], 'menu'),
    'votes': ('☑ Votes', 'green', 'Vote pour le prochain jeu.', [
        known('trigger mg.vote set 98', '☑ Votes : voir', 'green'), known(OPEN(12), '☑ Votes : lancer le plus voté', 'green'),
        known(OPEN(13), '☑ Votes : réinitialiser', 'green')], 'menu'),
    'joueur': ('👤 Joueur et plots', 'aqua', 'Tes options et ton plot.', [
        known(OPEN(1), 'Mode spectateur ON/OFF', 'gray'), known(OPEN(2), 'Classement des victoires', 'gold'),
        known('trigger mg.pl set 1', '⌂ Aller sur mon plot', 'green'), known('trigger mg.pl set 2', '↩ Quitter mon plot', 'yellow'),
        known('trigger mg.pl set 3', '◎ Visiter les plots', 'aqua')], 'menu'),
}
for key, (title, col, body, acts, parent) in CATS.items():
    save_dialog(f'cat_{key}', {'type': 'minecraft:multi_action', 'title': {'text': title, 'color': col, 'bold': True},
                               'pause': False, 'can_close_with_escape': True,
                               'body': [{'type': 'minecraft:plain_message', 'contents': [{'text': body, 'color': 'gray'}]}],
                               'columns': 2, 'exit_action': {'label': [{'text': 'Fermer', 'color': 'gray'}]},
                               'actions': acts + [back(parent)]})
    w(f'var/menu/cat_{key}', [f'# Catégorie « {title} » (@s = joueur) — fenêtre, sinon menu texte complet. Généré.',
                              'scoreboard players set $dlg mg.st 0',
                              f'execute store success score $dlg mg.st run dialog show @s mg:cat_{key}',
                              'execute unless score $dlg mg.st matches 1 run function mg:core/menu_chat'])

# Combat : le sous-menu PvP existant devient la catégorie (Bedwars et Sheep War passent dans Équipes)
d = load_dialog('pvp')
d['title'] = {'text': '⚔ Combat', 'color': 'red', 'bold': True}
d['actions'] = [known(OPEN(23), '⚔ Arène PvP ▸', 'yellow'), known(OPEN(24), '➶ One in the Chamber ▸', 'gold'),
                known(OPEN(10), '⚡ Quakecraft ▸', 'aqua'), act('✹ TNT Tag ▸', 'red', OPEN(29), 'La patate chaude'), back('menu')]
save_dialog('pvp', d)

# Menu principal : les catégories
d = load_dialog('menu')
keep = {a['action']['command']: a for a in d['actions']}
d['body'] = [{'type': 'minecraft:plain_message', 'contents': [
    {'text': 'Choisis une catégorie, puis un jeu, puis sa carte. ', 'color': 'gray'},
    {'text': '★', 'color': 'gold'}, {'text': ' = variantes sur les cartes des autres jeux.', 'color': 'gray'}]}]
d['actions'] = [
    act('❄ Jeux de sol ▸', 'aqua', OPEN(40), 'Spleef, TNT Run, Splegg, Sumo, Block Party, Enclumes', True),
    act('⚔ Combat ▸', 'red', OPEN(14), 'Arène PvP, One in the Chamber, Quakecraft, TNT Tag', True),
    act('⚑ Équipes ▸', 'light_purple', OPEN(41), 'Bedwars, Sheep War, Paintball, Turf Wars', True),
    act('🏁 Courses et vol ▸', 'gold', OPEN(42), 'Kart, bateaux, élytres, Dropper', True),
    known(OPEN(7), '☠ PvE ▸', 'dark_green'),
    act('🕹 Arcade ▸', 'light_purple', OPEN(47), 'Tron, King of the Hill, UHC, Hunger Games…', True),
    act('🎉 Fête et création ▸', 'green', OPEN(43), 'Mini Party, Build Battle, Téléphone', True),
    act('☑ Votes ▸', 'green', OPEN(44), 'Voter pour le prochain jeu'),
    act('👤 Joueur et plots ▸', 'aqua', OPEN(45), 'Spectateur, classement, plots'),
    keep.get('trigger mg.sv set 1') or act('🌲 Survie (monde libre)', 'green', 'trigger mg.sv set 1'),
    keep.get(OPEN(9)) or act('⛔ Arrêter la partie en cours', 'dark_red', OPEN(9)),
    act('🌍 TP général (admin) ▸', 'gold', OPEN(62), 'Tout le monde au lobby (sortie survie, GTA, plots…), en survie ou à Neo GTA'),
    act('ℹ Version du datapack', 'gray', OPEN(48), 'Version en place / reçue de GitHub : savoir si une mise à jour a planté'),
    act('🚫 Exclure Zinedine', 'red', OPEN(49), 'Exclut Zinedine du serveur (définitivement, cette fois)')]
save_dialog('menu', d)

# Boutons retour des sous-menus : vers leur catégorie
for name, cat in [('sub_sumo', 'sols'), ('sub_anvil', 'sols'), ('sub_bedwars', 'equipes'), ('sub_paint', 'equipes'), ('sheepmaps', 'equipes'),
                  ('sub_dropper', 'courses'), ('sub_elyrace', 'courses'), ('sub_elytra', 'courses'), ('sub_party', 'fete'), ('sub_bb', 'fete')]:
    d = load_dialog(name)
    d['actions'] = [a for a in d['actions'] if not is_back(a)] + [back(cat)]
    save_dialog(name, d)

w('var/menu/main', ['# Ancien menu des variantes (opt 32) → menu principal. Généré.', 'function mg:core/menu_use'])
w('var/menu/open', ['# mg.opt 32..46 → menus (catégories, jeux + variantes). Généré.',
                    'execute if score @s mg.opt matches 32 run function mg:var/menu/main'] +
  [f'execute if score @s mg.opt matches {m["opt"]} run function mg:var/menu/{m["key"]}' for m in MODES] +
  [f'execute if score @s mg.opt matches {o} run function mg:var/menu/cat_{k}' for k, o in OPT_CAT.items() if k != 'combat'])


def drop_lines(rel, lines):
    path = os.path.join(F, rel + '.mcfunction')
    txt = open(path, encoding='utf-8').read().split('\n')
    txt = [l for l in txt if l not in lines]
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(txt))


drop_lines('core/opt', ['execute if score @s mg.opt matches 32..39 unless entity @s[tag=mg.admin] run tellraw @s {"text":"⚠ Menus de lancement réservés aux admins.","color":"red"}',
                        'execute if score @s mg.opt matches 32..39 if entity @s[tag=mg.admin] run function mg:var/menu/open',
                        'execute if score @s mg.opt matches 46 unless entity @s[tag=mg.admin] run tellraw @s {"text":"⚠ Menus de lancement réservés aux admins : vote plutôt (≡ → ☑ Votes).","color":"red"}',
                        'execute if score @s mg.opt matches 44..46 if entity @s[tag=mg.admin] run function mg:var/menu/open'])
patch('core/opt', 'execute if score @s mg.opt matches 1 run function mg:core/opt_spec', [
    'execute if score @s mg.opt matches 32..43 unless entity @s[tag=mg.admin] run tellraw @s {"text":"⚠ Menus de lancement réservés aux admins : vote plutôt (≡ → ☑ Votes).","color":"red"}',
    'execute if score @s mg.opt matches 46..47 unless entity @s[tag=mg.admin] run tellraw @s {"text":"⚠ Menus de lancement réservés aux admins : vote plutôt (≡ → ☑ Votes).","color":"red"}',
    'execute if score @s mg.opt matches 32..43 if entity @s[tag=mg.admin] run function mg:var/menu/open',
    'execute if score @s mg.opt matches 44..47 if entity @s[tag=mg.admin] run function mg:var/menu/open',
    'execute if score @s mg.opt matches 44..45 unless entity @s[tag=mg.admin] run function mg:var/menu/open'], where='before')


# ============================================================ noms courts + étoiles sur les cartes d'origine
# Étoiles des cartes d'origine = difficulté de la carte (indicatif : leurs réglages restent ceux d'origine).
NATIVE = {
    1: ('Tour de neige', 2), 2: ('Tour de laine', 2), 20: ('Splegg', 2), 21: ('Splegg XXL', 1),
    22: ('Disque', 2), 24: ('Arène complexe', 3), 28: ('Block Party', 2), 29: ('Classique', 2), 42: ('Sol troué', 3),
    3: ('Arène classique', 3), 13: ('Classes : classique', 3), 44: ('Poussière', 2), 45: ('Classes : Poussière', 2),
    47: ('Mirage', 2), 48: ('Classes : Mirage', 2), 50: ('Nuketown', 2), 51: ('Classes : Nuketown', 2),
    26: ('Arène', 2), 52: ('Château', 2), 53: ('Grande forêt', 3),
    31: ('Néon', 2), 32: ('Volcan XL', 3), 33: ('Jungle XL', 3), 34: ('Désert', 2), 35: ('Glacier', 3),
    43: ('Poussière', 2), 46: ('Mirage', 2), 49: ('Nuketown', 2), 79: ('🎯 Ravin (sniper)', 3), 80: ('🎯 Tours (sniper)', 3),
    67: ('Classique', 3), 68: ('Collines', 2), 69: ('Canyon', 2), 70: ('Village perché', 2),
    71: ('Classique', 2), 72: ('Caldeira', 2), 73: ('Hanami', 2), 74: ('Banquise', 3),
    5: ('Classique', 2), 7: ('Forteresses', 2), 14: ('Bastions', 2), 15: ('Cubes voxel', 2), 16: ('Pyramides inversées', 3),
    17: ('Archipel', 2), 18: ('Double canyon', 3), 19: ('Nuages voxel', 3),
    36: ('Terrain', 2), 54: ('Mini-terrain', 3), 55: ('Grand terrain', 1),
    6: ('Classique', 2), 8: ('Nether', 3), 9: ('End', 3), 10: ('Ultra hard', 4), 11: ('Volant', 3), 12: ('Araignée', 3),
    37: ('Cathédrale (20 vagues)', 4), 38: ('Laboratoire (20 vagues)', 4), 39: ('Temple (20 vagues)', 4),
    40: ('Forge (20 vagues)', 4), 41: ('Vaisseau (20 vagues)', 4),
    23: ('Dropper', 2), 25: ('Tube commun', 2), 64: ('Aventure', 3), 65: ('Défi', 3),
    75: ('Course d\'anneaux', 2), 76: ('Course + combat', 3), 77: ('Survie en vol', 4),
    61: ('Circuit Champignon', 2), 62: ('Royaume Koopa', 3), 63: ('Bataille', 2), 56: ('Bateaux sur glace', 2),
    81: ('Canyon du Couchant', 3), 30: ('Turf Wars', 2),
    83: ('📞 Téléphone (5+)', 2), 84: ('⚡ Tron (à pied)', 3), 85: ('🏍 Tron moto', 4), 86: ('👑 King of the Hill', 2), 87: ('👑 KotH — équipes', 2), 88: ('🏰 The Towers', 3), 89: ('🚚 Convoi', 3), 90: ('🚚 Convoi — coop', 3), 91: ('▦ Block Party — bandes', 3), 92: ('▦ Block Party — mixte', 3), 93: ('🚩 Capture the Flag', 3), 94: ('⛏ Mini UHC Run', 3), 95: ('🏹 Mini Hunger Games', 3), 96: ('🎭 Prop Hunt', 2), 97: ('🧟 Zombies', 3), 98: ('🧪 Infection', 2), 220: ('🔴 1, 2, 3 Soleil', 2), 221: ('🚗 Autos tamponneuses', 2), 222: ('🚗 Autos tamponneuses — 3 coups', 2), 223: ('🚗 Autos tamponneuses — 8 coups', 2),   # 81 = Canyon du Couchant (Course d'élytres : 66 = parcours au hasard, plus une carte)
}
SHORT_OPT = {   # boutons de navigation (mg.opt) : noms courts
    24: '➶ OITC ▸', 10: '⚡ Quake ▸', 20: '⚓ Enclumes ▸', 19: '⬇ Dropper ▸', 28: '🪽 Course élytres ▸', 23: '⚔ Arène PvP ▸',
    8: '☁ Sheep War ▸', 21: '▓ Paintball ▸', 29: '✹ TNT Tag ▸', 17: '❍ Splegg ▸', 18: '✊ Sumo ▸',
}
SHORT_TITLE = {'sub_oitc': '➶ OITC', 'quakemaps': '⚡ Quake', 'sub_anvil': '⚓ Enclumes', 'sub_dropper': '⬇ Dropper', 'sub_elyrace': '🪽 Course élytres'}


def star_label(name, n, col):
    return [{'text': name + ' ', 'color': col}, {'text': '★' * n, 'color': 'gold'}, {'text': '☆' * (4 - n), 'color': 'dark_gray'}]


for f in sorted(os.listdir(os.path.join(D, 'dialog'))):
    if not f.endswith('.json') or f.startswith('vote'):
        continue
    name = f[:-5]
    d = load_dialog(name)
    changed = False
    for a in d.get('actions', []) or []:
        cmd = a.get('action', {}).get('command', '')
        mg_ = re.match(r'trigger mg\.(go|opt) set (\d+)$', cmd)
        if not mg_ or not isinstance(a.get('label'), list):
            continue
        kind, n = mg_.group(1), int(mg_.group(2))
        col = a['label'][0].get('color', 'white')
        if kind == 'go' and n in NATIVE:
            nm, st = NATIVE[n]
            icon = a['label'][0].get('text', '').split(' ')[0]
            if name.startswith('cat_') and len(icon) <= 2 and not icon[:1].isalnum():   # dans une catégorie, garder l'icône du jeu
                nm = f'{icon} {nm}'
            new = star_label(nm, st, col)
            if a['label'] != new:
                a['label'] = new
                changed = True
        elif kind == 'opt' and n in SHORT_OPT and a['label'][0].get('text') != SHORT_OPT[n]:
            a['label'] = [{**a['label'][0], 'text': SHORT_OPT[n]}]
            changed = True
    if name in SHORT_TITLE and d.get('title', {}).get('text') != SHORT_TITLE[name]:
        d['title']['text'] = SHORT_TITLE[name]
        changed = True
    if changed:
        save_dialog(name, d)


# ============================================================ votes par carte (au choix : le jeu, ou une carte précise)
# mg.vote = 1000 + id de lancement → vote pour cette carte (compte aussi pour son jeu) ; 91 = menu des cartes ;
# 900 + n = cartes du jeu n. Au lancement, le jeu le plus voté (votes jeu + cartes) gagne, puis sa carte la plus votée.
def dialog_labels():
    out = {}
    for f in sorted(os.listdir(os.path.join(D, 'dialog'))):
        d = json.load(open(os.path.join(D, 'dialog', f), encoding='utf-8'))
        for a in d.get('actions', []) or []:
            mm = re.match(r'trigger mg\.go set (\d+)$', a.get('action', {}).get('command', ''))
            if mm and int(mm.group(1)) < 100:
                lab = ''.join(x.get('text', '') for x in a['label']) if isinstance(a['label'], list) else a['label']
                out.setdefault(int(mm.group(1)), lab.strip())
    return out


LAB = dialog_labels()
VBYID = {v['id']: v for v in VARIANTS}
# (n° de vote du jeu, joueur fictif du compteur, nom, couleur, ids des cartes)
VG = [
    (1, 'Spleef', '❄ Spleef', 'aqua', [1] + [v['id'] for v in FLOOR_MODES[0]['vars']]),
    (2, 'TNT-Run', '✷ TNT Run', 'red', [2] + [v['id'] for v in FLOOR_MODES[1]['vars']]),
    (8, 'Splegg', '❍ Splegg', 'yellow', [20, 21] + [v['id'] for v in FLOOR_MODES[2]['vars']]),
    (9, 'Sumo', '✊ Sumo', 'gold', [22, 24]),
    (13, 'Enclumes', '⚓ Pluie d\'Enclumes', 'gray', [29, 42]),
    (3, 'PvP', '⚔ Arène PvP', 'yellow', [3, 44, 47, 50] + [v['id'] for v in COMBAT[0]['vars']]),
    (4, 'PvP-classes', '⚔ PvP classes', 'gold', [13, 45, 48, 51]),
    (17, 'One-in-Chamber', '➶ One in the Chamber', 'gold', [26, 52, 53] + [v['id'] for v in COMBAT[1]['vars']]),
    (15, 'Quakecraft', '⚡ Quakecraft', 'aqua', [31, 32, 33, 34, 35, 43, 46, 49, 79, 80] + [v['id'] for v in COMBAT[2]['vars']]),
    (11, 'TNT-Tag', '✹ TNT Tag', 'red', [67, 68, 69, 70] + [v['id'] for v in COMBAT[3]['vars']]),
    (5, 'Bedwars', '⚑ Bedwars', 'light_purple', [71, 72, 73, 74]),
    (6, 'Sheep-War', '☁ Sheep War', 'white', [5, 7, 14, 15, 16, 17, 18, 19]),
    (16, 'Paintball', '▓ Paintball', 'gold', [36, 54, 55]),
    (7, 'Mob-Arena', '☠ Mob Arena', 'dark_green', [6, 8, 9, 10, 11, 12, 37, 38, 39, 40, 41]),
    (10, 'Dropper', '⬇ The Dropper', 'aqua', [23, 25, 64, 65]),
    (21, 'Elytra', '🪽 Élytra', 'aqua', [75, 76, 77]),
]


def map_name(i):
    if i in VBYID:
        v = VBYID[i]
        return f'✦ {v["map"]["name"]} ' + '★' * v['dif'] + '☆' * (4 - v['dif'])
    return LAB.get(i, str(i))


L = ['# Votes par carte : compteurs #vm<id> (mg.st), ajoutés au total du jeu (mg.vb). Appelé par vote/refresh. Généré.']
for n, fake, name, col, ids in VG:
    for i in ids:
        L += [f'execute store result score #vm{i} mg.st if entity @a[scores={{mg.vc={1000 + i}}}]',
              f'execute if score #vm{i} mg.st matches 1.. run scoreboard players operation {fake} mg.vb += #vm{i} mg.st']
w('vote/map_refresh', L)

L = ['# @s vote pour une carte (mg.vote = 1000 + id). Généré.',
     'scoreboard players operation @s mg.vc = @s mg.vote', 'function mg:vote/refresh',
     'execute at @s run playsound minecraft:ui.button.click master @s ~ ~ ~ 1 1.4']
for n, fake, name, col, ids in VG:
    for i in ids:
        L.append(f'execute if score @s mg.vote matches {1000 + i} run tellraw @s ' + js([
            {'text': '☑ Tu votes pour : ', 'color': 'gray'}, {'text': name, 'color': col, 'bold': True},
            {'text': ' — carte ', 'color': 'gray'}, {'text': map_name(i), 'color': 'white'},
            {'text': ' (', 'color': 'gray'}, {'score': {'name': fake, 'objective': 'mg.vb'}, 'color': 'gold'},
            {'text': ' vote(s) pour ce jeu)', 'color': 'gray'}]))
        L.append(f'execute if score @s mg.vote matches {1000 + i} run tellraw @a[tag=mg.admin] ' + js([
            {'text': '☑ ', 'color': 'green'}, {'selector': '@s', 'color': 'yellow'}, {'text': ' vote pour ', 'color': 'gray'},
            {'text': f'{name} — {map_name(i)}', 'color': col}]))
w('vote/map_choose', L)

L = ['# Le jeu $vwin a gagné : sa carte la plus votée (égalité : au hasard) remplace la carte par défaut (@s = admin). Généré.',
     'scoreboard players set $vmm mg.st 0']
for n, fake, name, col, ids in VG:
    for i in ids:
        L.append(f'execute if score $vwin mg.st matches {n} run scoreboard players operation $vmm mg.st > #vm{i} mg.st')
L += ['execute if score $vmm mg.st matches 0 run return 0', 'scoreboard players set $vmc mg.st 0']
for n, fake, name, col, ids in VG:
    for i in ids:
        L.append(f'execute if score $vwin mg.st matches {n} if score #vm{i} mg.st = $vmm mg.st run scoreboard players add $vmc mg.st 1')
L += ['execute store result score $vmk mg.st run random value 0..9999', 'scoreboard players operation $vmk mg.st %= $vmc mg.st',
      'scoreboard players add $vmk mg.st 1']
for n, fake, name, col, ids in VG:
    for i in ids:
        L += [f'execute if score $vwin mg.st matches {n} if score #vm{i} mg.st = $vmm mg.st run scoreboard players remove $vmk mg.st 1',
              f'execute if score $vwin mg.st matches {n} if score #vm{i} mg.st = $vmm mg.st if score $vmk mg.st matches 0 run scoreboard players set @s mg.go {i}',
              f'execute if score $vwin mg.st matches {n} if score #vm{i} mg.st = $vmm mg.st if score $vmk mg.st matches 0 run tellraw @a ' + js([
                  {'text': '☑ Carte la plus votée : ', 'color': 'gray'}, {'text': map_name(i), 'color': col, 'bold': True},
                  {'text': ' (', 'color': 'gray'}, {'score': {'name': f'#vm{i}', 'objective': 'mg.st'}, 'color': 'gold'}, {'text': ' vote(s))', 'color': 'gray'}])]
w('vote/map_pick', L)

L = ['# Détail des votes par carte (@s), après vote/show. Généré.']
for n, fake, name, col, ids in VG:
    for i in ids:
        L.append(f'execute if score #vm{i} mg.st matches 1.. run tellraw @s ' + js([
            {'text': '    ↳ carte ', 'color': 'dark_gray'}, {'text': f'{name} — {map_name(i)}', 'color': col},
            {'text': ' : ', 'color': 'gray'}, {'score': {'name': f'#vm{i}', 'objective': 'mg.st'}, 'color': 'gold'}]))
w('vote/map_show', L)

# menus de vote par carte
acts = []
for n, fake, name, col, ids in VG:
    acts.append(act(f'{name} ▸', col, f'trigger mg.vote set {900 + n}', f'{len(ids)} cartes'))
acts.append(act('« Retour aux votes', 'yellow', 'trigger mg.vote set 97'))
save_dialog('vote_maps', {'type': 'minecraft:multi_action', 'title': {'text': '🗺 VOTE : une carte précise', 'color': 'green', 'bold': True},
                          'pause': False, 'can_close_with_escape': True,
                          'body': [{'type': 'minecraft:plain_message', 'contents': [
                              {'text': 'Choisis un jeu puis la carte. Ton vote compte pour le jeu ; si le jeu gagne, sa carte la plus votée est jouée.', 'color': 'gray'}]}],
                          'columns': 2, 'exit_action': {'label': [{'text': 'Fermer', 'color': 'gray'}]}, 'actions': acts})
OPENL = ['# Menus de vote par carte (@s = joueur, mg.vote = 91 ou 900 + n). Généré.',
         'execute if score @s mg.vote matches 91 run function mg:vote/map_menu {d:"vote_maps",n:0}']
for n, fake, name, col, ids in VG:
    acts = [act(f'🎲 {name} (carte au hasard)', col, f'trigger mg.vote set {n}', 'Vote pour le jeu, sans choisir la carte')]
    for i in ids:
        tip = None
        if i in VBYID:
            v = VBYID[i]
            tip = f'Variante : carte {v["map"]["src"]} ({v["map"]["desc"]}) · réglages : {SET[v["mode"]["key"]][v["dif"] - 1]}'
        acts.append(act(map_name(i), 'gold' if i in VBYID else 'white', f'trigger mg.vote set {1000 + i}', tip))
    acts.append(act('« Autres jeux', 'yellow', 'trigger mg.vote set 91'))
    save_dialog(f'vote_m{n}', {'type': 'minecraft:multi_action', 'title': {'text': f'🗺 VOTE : {name}', 'color': col, 'bold': True},
                               'pause': False, 'can_close_with_escape': True,
                               'body': [{'type': 'minecraft:plain_message', 'contents': [{'text': 'Vote pour une carte : cartes d’origine puis ✦ variantes ; ★ facile → ★★★★ difficile.', 'color': 'gray'}]}],
                               'columns': 2, 'exit_action': {'label': [{'text': 'Fermer', 'color': 'gray'}]}, 'actions': acts})
    OPENL.append(f'execute if score @s mg.vote matches {900 + n} run function mg:vote/map_menu {{d:"vote_m{n}",n:{n}}}')
    C = [f'# Repli chat : cartes de {name} (@s). Généré.',
         'tellraw @s ' + js([{'text': f'\n🗺 VOTE : {name} ', 'color': col, 'bold': True}, {'text': '(clique une carte)', 'color': 'gray'}])]
    for i in ids:
        C.append('tellraw @s ' + js(['', {'text': f' [{map_name(i)}]', 'color': 'gold' if i in VBYID else 'white',
                                          'click_event': {'action': 'run_command', 'command': f'trigger mg.vote set {1000 + i}'}}]))
    w(f'vote/map_chat_{n}', C)
w('vote/map_open', OPENL)
w('vote/map_menu', ['# Macro : ouvre la fenêtre $(d), sinon le menu chat des cartes du jeu $(n). Généré.',
                    'scoreboard players set $dlg mg.st 0',
                    '$execute store success score $dlg mg.st run dialog show @s mg:$(d)',
                    'execute if score $dlg mg.st matches 1 run return 0',
                    '$execute if score $dlg mg.st matches 0 run function mg:vote/map_chat {n:$(n)}'])
w('vote/map_chat', ['# Macro : repli chat des cartes du jeu $(n) (0 = liste des jeux). Généré.', '$function mg:vote/map_chat_$(n)'])
C = ['# Repli chat : liste des jeux pour voter une carte (@s). Généré.',
     'tellraw @s ' + js([{'text': '\n🗺 VOTE : une carte précise ', 'color': 'green', 'bold': True}, {'text': '(choisis le jeu)', 'color': 'gray'}])]
for n, fake, name, col, ids in VG:
    C.append('tellraw @s ' + js(['', {'text': f' [{name} ▸]', 'color': col, 'click_event': {'action': 'run_command', 'command': f'trigger mg.vote set {900 + n}'}}]))
w('vote/map_chat_0', C)

# crochets
patch('vote/cast', 'execute if score @s mg.vote matches 1..21 run function mg:vote/choose', [
    'execute if score @s mg.vote matches 1001..1199 run function mg:vote/map_choose',
    'execute if score @s mg.vote matches 91 run function mg:vote/map_open',
    'execute if score @s mg.vote matches 901..921 run function mg:vote/map_open'])
patch('vote/refresh', 'function mg:vote/sidebar', ['function mg:vote/map_refresh'], where='before')
patch('vote/launch', 'function mg:core/go', ['function mg:vote/map_pick'], where='before')
p = os.path.join(F, 'vote/show.mcfunction')
if 'function mg:vote/map_show' not in open(p, encoding='utf-8').read():
    with open(p, 'a', encoding='utf-8', newline='\n') as f:
        f.write('\nfunction mg:vote/map_show\n')
VBTN = act('🗺 Voter pour une carte ▸', 'green', 'trigger mg.vote set 91', 'Choisis la carte précise (cartes d’origine et variantes ★)', True)
for name in ('vote', 'vote_pvp'):
    d = load_dialog(name)
    if not any(a.get('action', {}).get('command') == 'trigger mg.vote set 91' for a in d['actions']):
        d['actions'].insert(0, VBTN)
        save_dialog(name, d)
# 🚫 « Exclure Zinedine » (running gag) : aussi dans le menu des joueurs (fenêtre de vote) et son menu texte
ZBTN = act('🚫 Exclure Zinedine', 'red', 'trigger mg.opt set 49', 'Exclut Zinedine du serveur (définitivement, cette fois)')
d = load_dialog('vote')
if not any(a.get('action', {}).get('command') == 'trigger mg.opt set 49' for a in d['actions']):
    d['actions'].append(ZBTN)
    save_dialog('vote', d)
patch('vote/chat', 'tellraw @s [{"text":"\\n☑ VOTE : quel jeu veux-tu jouer ? ","color":"green","bold":true},{"text":"(clique)","color":"gray"}]',
      ['tellraw @s ' + js(['', {'text': ' [🚫 Exclure Zinedine]', 'color': 'red',
                                'click_event': {'action': 'run_command', 'command': 'trigger mg.opt set 49'}}])])
patch('vote/chat', 'tellraw @s [{"text":"\\n☑ VOTE : quel jeu veux-tu jouer ? ","color":"green","bold":true},{"text":"(clique)","color":"gray"}]',
      ['tellraw @s ' + js(['', {'text': ' [🗺 Voter pour une carte précise ▸]', 'color': 'green', 'bold': True,
                                'click_event': {'action': 'run_command', 'command': 'trigger mg.vote set 91'}}])])

# ============================================================ lancement automatique par majorité de votes
# ≥ 3 joueurs et plus de la moitié votent pour le même jeu (votes jeu + cartes) → compte à rebours de 10 s → lancement.
GV = []   # (n°, joueur fictif, libellé, couleur) lus dans vote/refresh et vote/show
ref = open(os.path.join(F, 'vote/refresh.mcfunction'), encoding='utf-8').read()
shw = open(os.path.join(F, 'vote/show.mcfunction'), encoding='utf-8').read()
for fake, n in re.findall(r'execute store result score (\S+) mg\.vb if entity @a\[scores=\{mg\.vc=(\d+)\}\]', ref):
    mm = re.search(r'execute if score ' + re.escape(fake) + r' mg\.vb matches 1\.\. run tellraw @s \[\{"text":" ▸ ","color":"gray"\},\{"text":"([^"]+)","color":"(\w+)"\}', shw)
    GV.append((int(n), fake, mm.group(1) if mm else fake, mm.group(2) if mm else 'gold'))
AUTO = 200
L = ['# Votes à la majorité (core/tick, toutes les secondes, lobby uniquement). Généré.',
     '# Joueurs comptés : tous les joueurs connectés hors monde de survie et hors pause. Il en faut 3 au moins.',
     'execute unless score $state mg.st matches 0 run return run scoreboard players set $vat mg.st -1',
     'execute if score $setup mg.st matches 0 run return 0',
     'execute store result score $vnp mg.st if entity @a[tag=mg.init,tag=!mg.spectate,tag=!mg.surv]',
     '# recompte seulement si le nombre de joueurs a changé (un votant a pu partir) ; sinon les votes sont déjà à jour',
     'execute unless score $vnp mg.st = $vnpo mg.st run function mg:vote/refresh',
     'scoreboard players operation $vnpo mg.st = $vnp mg.st',
     'scoreboard players set $vmax mg.st 0']
L += [f'scoreboard players operation $vmax mg.st > {fake} mg.vb' for n, fake, lab, col in GV]
L += ['scoreboard players operation $vm2 mg.st = $vmax mg.st', 'scoreboard players operation $vm2 mg.st += $vmax mg.st',
      'scoreboard players set $vok mg.st 0',
      'execute if score $vnp mg.st matches 3.. if score $vm2 mg.st > $vnp mg.st run scoreboard players set $vok mg.st 1',
      '# Majorité perdue pendant le compte à rebours → annulé',
      'execute if score $vok mg.st matches 0 if score $vat mg.st matches 1.. run tellraw @a[tag=!mg.surv] {"text":"☑ Plus de majorité : lancement automatique annulé.","color":"gray"}',
      'execute if score $vok mg.st matches 0 run return run scoreboard players set $vat mg.st -1',
      'scoreboard players set $vlead mg.st 0']
L += [f'execute if score {fake} mg.vb = $vmax mg.st run scoreboard players set $vlead mg.st {n}' for n, fake, lab, col in GV]
L += ['# Nouvelle majorité → compte à rebours',
      f'execute unless score $vat mg.st matches 1.. run scoreboard players set $vat mg.st {AUTO // 20 + 1}']
for n, fake, lab, col in GV:
    L.append(f'execute if score $vat mg.st matches {AUTO // 20 + 1} if score $vlead mg.st matches {n} run tellraw @a[tag=!mg.surv] ' + js([
        {'text': '☑ Majorité pour ', 'color': 'green'}, {'text': lab, 'color': col, 'bold': True},
        {'text': ' (', 'color': 'gray'}, {'score': {'name': fake, 'objective': 'mg.vb'}, 'color': 'gold'}, {'text': ' / ', 'color': 'gray'},
        {'score': {'name': '$vnp', 'objective': 'mg.st'}, 'color': 'gold'}, {'text': ' joueurs) : lancement dans 10 s !', 'color': 'gray'}]))
L += ['scoreboard players remove $vat mg.st 1',
      'execute if score $vat mg.st matches 1..10 run title @a[tag=!mg.surv] actionbar [{"text":"☑ Jeu voté : lancement dans ","color":"green"},{"score":{"name":"$vat","objective":"mg.st"},"color":"gold","bold":true},{"text":" s","color":"green"}]',
      'execute if score $vat mg.st matches 1..3 as @a[tag=!mg.surv] at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.5',
      'execute if score $vat mg.st matches 0 run function mg:vote/auto_launch']
w('vote/auto_tick', L)
w('vote/auto_launch', ['# Fin du compte à rebours : un votant (marqué mg.vauto, accepté par core/go comme un admin) lance le jeu le plus voté. Généré.',
                       'scoreboard players set $vat mg.st -1',
                       'tag @r[tag=mg.init,tag=!mg.surv,scores={mg.vc=1..}] add mg.vauto',
                       'execute as @a[tag=mg.vauto,limit=1] run function mg:vote/launch',
                       'tag @a remove mg.vauto'])
patch('core/tick', 'execute as @a[scores={mg.vote=1..}] run function mg:vote/cast', [
    '# Votes à la majorité : lancement automatique (une fois par seconde)',
    'scoreboard players add $vtk mg.st 1',
    'execute if score $vtk mg.st matches 20.. run function mg:vote/auto_tick',
    'execute if score $vtk mg.st matches 20.. run scoreboard players set $vtk mg.st 0'])
replace('core/go', 'execute unless entity @s[tag=mg.admin] run tellraw @s [{"text":"⚠ Seul un admin peut lancer un jeu.","color":"red"}]',
        'execute unless entity @s[tag=mg.admin] unless entity @s[tag=mg.vauto] run tellraw @s [{"text":"⚠ Seul un admin peut lancer un jeu.","color":"red"}]')
replace('core/go', 'execute unless entity @s[tag=mg.admin] run return run scoreboard players reset @s mg.go',
        'execute unless entity @s[tag=mg.admin] unless entity @s[tag=mg.vauto] run return run scoreboard players reset @s mg.go')

# ============================================================ récapitulatif (docs)
md = ['# Variantes (générées par `tools/variantes/gen_variants.py`)', '',
      'Chaque mode sur les cartes des autres jeux. La difficulté (★ à ★★★★) dépend de la carte et change les réglages.',
      'Menu : ≡ → catégorie (❄ Jeux de sol / ⚔ Combat) → jeu → cartes d’origine puis variantes ★.', '',
      '| Réglages | ★ | ★★ | ★★★ | ★★★★ |', '|---|---|---|---|---|']
for m in MODES:
    md.append(f'| {m["name"]} | ' + ' | '.join(SET[m['key']]) + ' |')
md += ['', '| Id | Mode | Carte (origine) | Difficulté |', '|---|---|---|---|']
for m in MODES:
    md.append(f'| {m["rnd"]} | {m["name"]} | variante au hasard | |')
    for v in m['vars']:
        md.append(f'| {v["id"]} | {m["name"]} | {v["map"]["name"]} ({v["map"]["src"]}) | {stars(v["dif"])} |')
os.makedirs(os.path.join(R, 'docs'), exist_ok=True)
with open(os.path.join(R, 'docs/VARIANTES.md'), 'w', encoding='utf-8', newline='\n') as f:
    f.write('\n'.join(md) + '\n')

print(f'{len(VARIANTS)} variantes (ids 100..{vid - 1}, hasard 190..196), {len(written)} fichiers générés')
for m in MODES:
    print(f'  {m["name"]:<20} {len(m["vars"]):>2}  opt {m["opt"]}  ' + ' '.join(f'{v["id"]}{stars(v["dif"])}' for v in m['vars']))

# Les notes des joueurs remplacent les étoiles dans les menus : à refaire après chaque régénération des menus
import runpy
runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'rating', 'gen_rating.py'), run_name='__main__')
