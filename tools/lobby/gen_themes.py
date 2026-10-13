"""🎃🎄 Décors saisonniers du spawn, réversibles : python tools/lobby/gen_themes.py .   (après gen_lobby.py)

Admin : menu des événements du lobby → « 🎃 Déco Halloween » (mg.opt 73) / « 🎄 Déco Noël » (mg.opt 74) : bascule
(pose le thème, ou le retire s'il est déjà en place ; un seul thème à la fois, l'autre est retiré d'abord).
Aussi : /function mg:lobby/theme/<halloween|noel>/on, /function mg:lobby/theme/off ($theme : 0 aucun, 1 Halloween, 2 Noël).

Le générateur relit les fonctions de construction du spawn (lobby/*build*, parkour/build) pour reconstituer chaque bloc
d'origine ; « on » ne pose un bloc que si le bloc d'origine est encore là, « off » ne remet l'original que si le bloc du
thème est encore là (rien d'autre n'est écrasé). Les plots et les zones modifiées par d'autres fonctions (jeux,
animations) ne sont jamais touchés. Les entités du décor (mg.lby) sont rhabillées par lobby/theme/<t>/reskin, rappelé à
chaque lobby/deco (bascule du resource pack) ; « off » relance lobby/deco, qui repose le décor d'origine.
Ajouter un thème : une fonction theme_<nom>() qui remplit CH et renvoie (reskin, fx, titre), puis l'inscrire dans THEMES
(et dans tools/lobby/gen_theme_maps.py, qui habille aussi les cartes de jeu pendant les parties).
"""
import glob
import os
import random
import re
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'arcade'))
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
F = C.F
G = 63                                   # sol du spawn (pieds en y 64)
LIM = 78                                 # zone décorée : |x|, |z| <= LIM (forceload du spawn : -80..80)
LOBBY = '@a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,gamemode=!spectator]'

# ------------------------------------------------------------------ plots (jamais touchés)
PLOTS = []
for l in open(os.path.join(F, 'plot', 'build_all.mcfunction'), encoding='utf-8'):
    m = re.search(r'wx1:(-?\d+),wx2:(-?\d+),wz1:(-?\d+),wz2:(-?\d+)', l)
    if m:
        PLOTS.append(tuple(int(v) for v in m.groups()))


def inplot(x, z):
    return any(a - 1 <= x <= b + 1 and c - 1 <= z <= d + 1 for a, b, c, d in PLOTS)


# ------------------------------------------------------------------ reconstitution des blocs du spawn
CMD = re.compile(r'^(setblock|fill) (-?\d+) (-?\d+) (-?\d+)(?: (-?\d+) (-?\d+) (-?\d+))? (.+)$')
W = {}                                   # (x, y, z) -> bloc (l'air n'est pas stocké)
DYN = []                                 # boîtes modifiées ailleurs (jeux, animations) : on n'y touche pas


def block_and_mode(rest):
    depth = 0
    for i, ch in enumerate(rest):
        if ch in '[{':
            depth += 1
        elif ch in ']}':
            depth -= 1
        elif ch == ' ' and depth == 0:
            return rest[:i], rest[i + 1:].split(' ')
    return rest, []


def clip(a, b):
    return max(min(a, b), -LIM - 2), min(max(a, b), LIM + 2)


def apply(line, dynamic):
    m = CMD.match(line.strip())
    if not m:
        return
    x1, y1, z1 = int(m[2]), int(m[3]), int(m[4])
    x2, y2, z2 = (x1, y1, z1) if m[5] is None else (int(m[5]), int(m[6]), int(m[7]))
    xa, xb = clip(x1, x2)
    za, zb = clip(z1, z2)
    if xa > xb or za > zb:
        return
    ya, yb = min(y1, y2), max(y1, y2)
    blk, mode = block_and_mode(m[8])
    if dynamic or (m[1] == 'fill' and mode and mode[0] in ('replace', 'hollow', 'outline')):
        DYN.append((xa, xb, ya, yb, za, zb))
        return
    keep = bool(mode) and mode[0] == 'keep'
    air = blk in ('minecraft:air', 'air')
    for x in range(xa, xb + 1):
        for z in range(za, zb + 1):
            for y in range(ya, yb + 1):
                k = (x, y, z)
                if air:
                    W.pop(k, None)
                elif not (keep and k in W):
                    W[k] = blk


def num(p):
    m = re.search(r'build_(\d+)', p)
    return int(m[1]) if m else 99


BASE = sorted(glob.glob(os.path.join(F, 'lobby', 'build_*.mcfunction')), key=num)
BASE += [p for p in sorted(glob.glob(os.path.join(F, 'lobby', '*build*.mcfunction')))
         if p not in BASE and not p.endswith(os.sep + 'build.mcfunction')]
BASE.append(os.path.join(F, 'parkour', 'build.mcfunction'))
for p in BASE:
    for l in open(p, encoding='utf-8'):
        apply(l, False)
for p in glob.glob(os.path.join(F, '**', '*.mcfunction'), recursive=True):
    if p in BASE or (os.sep + 'theme' + os.sep) in p or p.endswith(os.sep + 'desinstaller.mcfunction'):
        continue
    for l in open(p, encoding='utf-8'):
        if l.startswith(('setblock ', 'fill ')):
            apply(l, True)


def dyn(x, y, z):
    return any(a <= x <= b and c <= y <= d and e <= z <= f for a, b, c, d, e, f in DYN)


def bid(b):
    return (b or 'minecraft:air').split('[')[0].split('{')[0]


def states(b):
    m = re.search(r'\[([^\]]*)\]', b or '')
    return dict(kv.split('=') for kv in m[1].split(',')) if m and m[1] else {}


PLANTS = {'minecraft:short_grass', 'minecraft:fern', 'minecraft:pink_petals', 'minecraft:dandelion', 'minecraft:poppy',
          'minecraft:blue_orchid', 'minecraft:allium', 'minecraft:azure_bluet', 'minecraft:red_tulip', 'minecraft:orange_tulip',
          'minecraft:white_tulip', 'minecraft:pink_tulip', 'minecraft:oxeye_daisy', 'minecraft:cornflower',
          'minecraft:lily_of_the_valley'}
FLOWERS = PLANTS - {'minecraft:short_grass', 'minecraft:fern', 'minecraft:pink_petals'}
NOT_SOLID = PLANTS | {'minecraft:air', 'minecraft:light', 'minecraft:barrier', 'minecraft:water', 'minecraft:vine',
                      'minecraft:glow_lichen', 'minecraft:lantern', 'minecraft:spore_blossom', 'minecraft:bamboo',
                      'minecraft:pointed_dripstone'}
GROUND = {'minecraft:grass_block', 'minecraft:moss_block', 'minecraft:podzol', 'minecraft:coarse_dirt', 'minecraft:dirt',
          'minecraft:rooted_dirt'}
DIRT = GROUND - {'minecraft:grass_block', 'minecraft:moss_block'}
WALLS = {'minecraft:stone_bricks', 'minecraft:mossy_stone_bricks', 'minecraft:cracked_stone_bricks', 'minecraft:spruce_planks',
         'minecraft:deepslate_tiles', 'minecraft:polished_deepslate', 'minecraft:cobbled_deepslate', 'minecraft:cobblestone',
         'minecraft:mossy_cobblestone', 'minecraft:stone', 'minecraft:tuff', 'minecraft:deepslate', 'minecraft:andesite',
         'minecraft:spruce_log', 'minecraft:dark_oak_log', 'minecraft:oak_log', 'minecraft:stripped_spruce_log'}
# surfaces pleines où la neige tient (le haut d'un bloc entier)
SNOWABLE = GROUND | WALLS | {'minecraft:dirt_path', 'minecraft:packed_mud', 'minecraft:calcite', 'minecraft:smooth_quartz',
                             'minecraft:polished_andesite', 'minecraft:polished_diorite', 'minecraft:white_concrete',
                             'minecraft:gray_concrete'}


def solid(x, y, z):
    return bid(W.get((x, y, z))) not in NOT_SOLID


def free(x, y, z):
    return abs(x) <= LIM and abs(z) <= LIM and not inplot(x, z) and not dyn(x, y, z)


def opening(k):
    return k not in W or bid(W[k]) in PLANTS


# ------------------------------------------------------------------ fontaines et cascades (eau qui déborde)
# Une source qui déborde (air dessous ou à côté) alimente un écoulement : toute l'eau voisine (6 blocs, jusqu'à 30 plus
# bas) reste liquide (pas de glace à Noël) et lobby/theme/water_fix la remet d'aplomb à chaque bascule de thème.
WATER = {k for k, b in W.items() if bid(b) == 'minecraft:water'}
SPILL = [k for k in sorted(WATER) if opening((k[0], k[1] - 1, k[2]))
         or any(opening((k[0] + a, k[1], k[2] + c)) for a, c in ((1, 0), (-1, 0), (0, 1), (0, -1)))]
FLOW = {}                                # source qui déborde -> eau de son ouvrage
for s in SPILL:
    FLOW[s] = {k for k in WATER if max(abs(k[0] - s[0]), abs(k[2] - s[2])) <= 6 and s[1] - 30 <= k[1] <= s[1]}
FOUNT = set().union(*FLOW.values()) if FLOW else set()


CH = {}                                  # (x, y, z) -> (bloc d'origine, bloc du thème), rempli par un thème
FACES = ['north', 'south', 'east', 'west']


def change(k, new):
    if k not in CH and free(*k):
        CH[k] = (W.get(k, 'minecraft:air'), new)


def on_fences(rnd, p, blocks):
    for (x, y, z), b in sorted(W.items()):
        if bid(b) == 'minecraft:spruce_fence' and (x, y + 1, z) not in W and rnd.random() < p:
            change((x, y + 1, z), f'minecraft:{rnd.choice(blocks)}_candle[lit=true,candles={rnd.randint(1, 4)}]')


IT = 'execute as @e[type=minecraft:item_display,tag=mg.lby] if items entity @s contents '


def item_swap(pred, item):
    return f'{IT}{pred} run item replace entity @s contents with {item}'


def title(parts):
    return ('summon minecraft:text_display 0.5 74 0.5 {Tags:["mg.lby","mg.thm"],billboard:"center",background:1426063360,'
            'shadow:1b,text:' + js(parts) + ',transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],'
            'right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}')


# ------------------------------------------------------------------ animaux des thèmes
# Tenus à un nombre fixe, réapparaissent sur un point d'herbe tiré au hasard (lobby/theme/spot), ramenés s'ils sortent
# du spawn. Habillage (resource pack) : item_display « tête » monté sur l'animal, tourné comme lui à chaque tick.
MOB_BOX = 'x=-78,y=50,z=-78,dx=156,dy=70,dz=156'
MOB_BASE = 'PersistenceRequired:1b,Invulnerable:1b,DeathLootTable:"minecraft:empty"'
_rs = random.Random(20261013)
_cand = [(x, y + 1, z) for (x, y, z), b in sorted(W.items())
         if bid(b) in GROUND and y >= G - 1 and 100 <= x * x + z * z <= 62 * 62 and free(x, y + 1, z)
         and bid(W.get((x, y + 1, z))) in PLANTS | {'minecraft:air'} and (x, y + 2, z) not in W and (x, y + 3, z) not in W]
SPOTS = sorted(_rs.sample(_cand, min(48, len(_cand))))


def mob(key, entity, n, nbt='', dress=None, rand_yaw=False, rp_nbt=None):
    """dress = (modèle du resource pack, translation [x, y, z], échelle, invisible ?) ;
    rp_nbt = NBT utilisé à la place de nbt quand le resource pack est activé (variante dont la texture n'existe que dans le pack)"""
    return {'key': key, 'entity': entity, 'n': n, 'nbt': nbt, 'dress': dress, 'yaw': rand_yaw, 'rp_nbt': rp_nbt}


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


# ------------------------------------------------------------------ 🎃 Halloween
def theme_halloween():
    rnd = random.Random(20261031)
    for k, b in sorted(W.items()):                       # feuillages, éclairage, fleurs
        i = bid(b)
        if i.endswith('_leaves'):
            if i in ('minecraft:cherry_leaves', 'minecraft:azalea_leaves', 'minecraft:flowering_azalea_leaves') or rnd.random() < 0.55:
                change(k, 'minecraft:pale_oak_leaves[persistent=true]')
        elif i == 'minecraft:lantern':
            change(k, 'minecraft:soul_lantern' + b[len(i):])
        elif i == 'minecraft:wall_torch':
            change(k, 'minecraft:soul_wall_torch' + b[len(i):])
        elif i == 'minecraft:torch':
            change(k, 'minecraft:soul_torch')
        elif i == 'minecraft:pink_petals':
            s = states(b)
            change(k, f'minecraft:leaf_litter[segment_amount={s.get("flower_amount", "4")},facing={s.get("facing", "north")}]')
        elif i == 'minecraft:short_grass' and rnd.random() < 0.4:
            change(k, 'minecraft:short_dry_grass')
        elif i in FLOWERS and rnd.random() < 0.45:
            change(k, 'minecraft:dead_bush' if bid(W.get((k[0], k[1] - 1, k[2]))) in DIRT else 'minecraft:short_dry_grass')
    for (x, y, z), (_, new) in list(CH.items()):          # mousse pâle pendante
        if new.startswith('minecraft:pale_oak_leaves') and (x, y - 1, z) not in W and rnd.random() < 0.3:
            change((x, y - 1, z), 'minecraft:pale_hanging_moss[tip=true]')
    for (x, y, z), b in sorted(W.items()):               # citrouilles sur l'herbe, loin du point d'apparition
        if bid(b) not in GROUND or x * x + z * z < 64 or y < G - 1:
            continue
        up = (x, y + 1, z)
        if bid(W.get(up)) in ('minecraft:air', 'minecraft:short_grass', 'minecraft:fern') and (x, y + 2, z) not in W \
                and up not in CH and rnd.random() < 0.045:
            kind = rnd.choice(['minecraft:carved_pumpkin', 'minecraft:jack_o_lantern', 'minecraft:jack_o_lantern', 'minecraft:pumpkin'])
            change(up, kind + ('' if kind == 'minecraft:pumpkin' else f'[facing={rnd.choice(FACES)}]'))
    for (x, y, z), b in sorted(W.items()):               # toiles d'araignée dans les coins sous plafond
        if bid(b) not in WALLS:
            continue
        for dx, dz in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
            cx, cy, cz = x + dx, y, z
            if (cx, cy, cz) in W or (cx, cy, cz) in CH or G + 1 <= cy <= G + 2 or cx * cx + cz * cz < 100:
                continue
            if solid(cx, cy + 1, cz) and bid(W.get((cx, cy, cz + dz))) in WALLS and rnd.random() < 0.08:
                change((cx, cy, cz), 'minecraft:cobweb')
    on_fences(rnd, 0.3, ['orange', 'orange', 'black', 'purple'])
    lrnd = random.Random(20261101)                       # tirage à part : le reste du décor ne bouge pas
    canopy = {}                                          # colonne (x, z) -> plus haut feuillage à 2 blocs près
    for (x, y, z), b in W.items():
        if bid(b).endswith('_leaves'):
            for a in range(-2, 3):
                for c in range(-2, 3):
                    canopy[(x + a, z + c)] = max(canopy.get((x + a, z + c), y), y)
    for (x, y, z), b in sorted(W.items()):               # feuilles mortes : tapis sous les arbres, quelques-unes ailleurs
        if bid(b) not in GROUND or x * x + z * z < 36 or y < G - 1:
            continue
        up = (x, y + 1, z)
        under = y < canopy.get((x, z), -999) <= y + 12
        if (bid(W.get(up)) in ('minecraft:air', 'minecraft:short_grass', 'minecraft:fern') and (x, y + 2, z) not in W
                and up not in CH and lrnd.random() < (0.4 if under else 0.06)):
            change(up, f'minecraft:leaf_litter[segment_amount={lrnd.randint(1, 4)},facing={lrnd.choice(FACES)}]')
    PUMP = [0xFF8A1C, 0x8E3BD6, 0x4FC23A, 0xECECF4, 0x3A3440, 0xD62A2A, 0x3A7BE0, 0x2FC8B5, 0xFF6FB5]
    pump = {st: ['execute store result score $thp mg.st run random value 1..' + str(len(PUMP))]
            + [f'execute if score $thp mg.st matches {i} run item replace entity @s contents with minecraft:leather_horse_armor'
               f'[minecraft:item_model="mg:pumpkin_{st}",minecraft:dyed_color={c}]' for i, c in enumerate(PUMP, 1)]
            for st in ('lit', 'carved')}             # citrouilles colorées du resource pack (couleur tirée au hasard)
    reskin = [f'{IT}*[minecraft:item_model="mg:{m}"] if score $rp mg.st matches 1 run function mg:lobby/theme/halloween/pumpkin_{st}'
              for m, st in (('balloon', 'lit'), ('item_box', 'carved'), ('star', 'lit'))]
    reskin += [f'{IT}minecraft:nether_star if score $rp mg.st matches 1 run function mg:lobby/theme/halloween/pumpkin_lit',
               item_swap('*[minecraft:item_model="mg:balloon"]', 'minecraft:jack_o_lantern'),
              item_swap('*[minecraft:item_model="mg:item_box"]', 'minecraft:carved_pumpkin'),
              item_swap('*[minecraft:item_model="mg:star"]', 'minecraft:jack_o_lantern'),
              item_swap('minecraft:nether_star', 'minecraft:jack_o_lantern'),
              item_swap('*[minecraft:item_model="mg:crystal"]', 'minecraft:wither_skeleton_skull'),
              item_swap('minecraft:amethyst_cluster', 'minecraft:wither_skeleton_skull'),
              'execute as @e[type=minecraft:armor_stand,tag=mg.lby] run item replace entity @s armor.head with minecraft:carved_pumpkin',
              title([{'text': '🎃 Joyeux Halloween ! 🎃', 'color': 'gold', 'bold': True},
                     {'text': '\nBonbons ou mini-jeux ?', 'color': 'dark_purple', 'italic': True}])]
    fx = [f'execute in minecraft:overworld as {LOBBY} at @s run particle minecraft:ash ~ ~3 ~ 8 3 8 0 25 normal @s',
          f'execute in minecraft:overworld as {LOBBY} at @s run particle minecraft:soul ~ ~0.3 ~ 6 0.5 6 0.01 2 normal @s',
          *[f'execute in minecraft:overworld as {LOBBY} at @s run particle minecraft:tinted_leaves{{color:[{c}]}} ~ ~7 ~ 10 3 10 0 {n} normal @s'
            for c, n in (('0.93,0.45,0.08,1.0', 5), ('0.78,0.16,0.08,1.0', 3), ('0.95,0.72,0.15,1.0', 3), ('0.52,0.30,0.14,1.0', 2))],
          'execute store result score $thr mg.st run random value 1..40',
          f'execute if score $thr mg.st matches 1 in minecraft:overworld as {LOBBY} at @s run playsound minecraft:ambient.cave ambient @s ~ ~ ~ 0.6 1']
    hello = ([{'text': '🎃 ', 'color': 'gold'}, {'text': 'Le spawn se pare de ses habits d\'Halloween… Bouh !', 'color': 'gold', 'bold': True}],
             'minecraft:entity.witch.celebrate')
    mobs = [mob('bat', 'minecraft:bat', 8),
            mob('ghost', 'minecraft:allay', 6, 'Silent:1b', ('mg:hat/ghost', [0, -0.3, 0], 1.0, True))]
    return reskin, fx, hello, mobs, {'water': water_biome('mg:halloween'),
                                     'files': {f'pumpkin_{st}': [f'# 🎃 Halloween : citrouille {st} de couleur aléatoire (pack activé)'] + ls
                                               for st, ls in pump.items()}}


# ------------------------------------------------------------------ 🎄 Noël
def theme_noel():
    rnd = random.Random(20261225)
    LIGHTS = ['minecraft:pearlescent_froglight', 'minecraft:ochre_froglight', 'minecraft:verdant_froglight',
              'minecraft:sea_lantern', 'minecraft:redstone_lamp[lit=true]']
    for k, b in sorted(W.items()):                       # guirlandes dans les arbres, eau gelée, fleurs sous la neige
        i = bid(b)
        x, y, z = k
        if i.endswith('_leaves') and (x, y + 1, z) in W and rnd.random() < 0.07:
            change(k, rnd.choice(LIGHTS))
        elif i == 'minecraft:water' and (x, y + 1, z) not in W and states(b).get('level', '0') == '0' and k not in FOUNT:
            change(k, 'minecraft:ice')
        elif i in FLOWERS or i == 'minecraft:pink_petals' or (i in ('minecraft:short_grass', 'minecraft:fern') and rnd.random() < 0.7):
            if bid(W.get((x, y - 1, z))) in SNOWABLE:
                change(k, 'minecraft:snow[layers=1]')
    for (x, y, z), b in sorted(W.items()):               # neige sur les surfaces à l'air libre (sauf à côté du point d'apparition)
        i = bid(b)
        up = (x, y + 1, z)
        if (i in SNOWABLE or i.endswith('_leaves')) and up not in W and up not in CH and x * x + z * z >= 25 \
                and not any((x, yy, z) in W for yy in range(y + 2, y + 40)) and rnd.random() < 0.85:
            change(up, f'minecraft:snow[layers={1 if rnd.random() < 0.8 else 2}]')
    for (x, y, z), b in sorted(W.items()):               # cadeaux au pied des arbres (sur l'herbe, à côté d'un tronc)
        if bid(b) not in GROUND or x * x + z * z < 64:
            continue
        up = (x, y + 1, z)
        near_log = any(bid(W.get((x + dx, y + 1, z + dz))).endswith('_log') for dx, dz in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        if near_log and bid(W.get(up)) in ('minecraft:air', 'minecraft:short_grass', 'minecraft:fern') and rnd.random() < 0.5:
            CH.pop(up, None)
            change(up, rnd.choice(['minecraft:red_shulker_box', 'minecraft:green_shulker_box', 'minecraft:white_shulker_box',
                                   'minecraft:red_wool', 'minecraft:lime_wool']))
    on_fences(rnd, 0.3, ['red', 'red', 'green', 'white'])
    reskin = [item_swap('*[minecraft:item_model="mg:balloon"]', 'minecraft:snow_block'),
              item_swap('*[minecraft:item_model="mg:item_box"]', 'minecraft:red_shulker_box'),
              item_swap('*[minecraft:item_model="mg:crystal"]', 'minecraft:blue_ice'),
              item_swap('minecraft:amethyst_cluster', 'minecraft:blue_ice'),
              'execute as @e[type=minecraft:armor_stand,tag=mg.lby] run item replace entity @s armor.head with '
              'minecraft:leather_helmet[minecraft:dyed_color=13369344]',
              title([{'text': '🎄 Joyeux Noël ! 🎄', 'color': 'red', 'bold': True},
                     {'text': '\net bonnes fêtes sur NeoMC', 'color': 'dark_green', 'italic': True}])]
    fx = [f'execute in minecraft:overworld as {LOBBY} at @s run particle minecraft:snowflake ~ ~6 ~ 10 4 10 0 30 normal @s',
          f'execute in minecraft:overworld as {LOBBY} at @s run particle minecraft:white_ash ~ ~3 ~ 8 3 8 0 20 normal @s',
          'execute store result score $thr mg.st run random value 1..45',
          f'execute if score $thr mg.st matches 1 in minecraft:overworld as {LOBBY} at @s run playsound minecraft:block.amethyst_block.chime ambient @s ~ ~2 ~ 1 0.8']
    hello = ([{'text': '🎄 ', 'color': 'red'}, {'text': 'Il neige sur le spawn… Joyeuses fêtes !', 'color': 'green', 'bold': True}],
             'minecraft:entity.player.levelup')
    # bonshommes de neige immobiles : le spawn a mob_griefing à true, en marchant ils laisseraient des traînées de neige
    mobs = [mob('snowman', 'minecraft:snow_golem', 6, 'NoAI:1b,Pumpkin:0b', rand_yaw=True),
            mob('reindeer', 'minecraft:cow', 3, 'Silent:1b,variant:"minecraft:cold"', rp_nbt='Silent:1b,variant:"mg:reindeer"'),
            mob('rudolph', 'minecraft:cow', 1, 'Silent:1b,variant:"minecraft:cold"', rp_nbt='Silent:1b,variant:"mg:rudolph"')]
    melt = ['execute as @e[type=minecraft:snow_golem,tag=mg.thmob] at @s run fill ~-1 ~ ~-1 ~1 ~ ~1 minecraft:air '
            'replace minecraft:snow[layers=1]']
    return reskin, fx, hello, mobs, {'off': melt}


THEMES = [(1, 'halloween', '🎃 Halloween', 73, theme_halloween), (2, 'noel', '🎄 Noël', 74, theme_noel)]

# ------------------------------------------------------------------ fonctions
stats = []
for tid, key, label, opt, make in THEMES:
    CH.clear()
    reskin, fx, (hello, snd), mobs, extra = make()
    T = f'lobby/theme/{key}'
    on_x, off_x = [], list(extra.get('off', []))
    if 'water' in extra:                 # fonctions à part : le biome du pack n'existe qu'après un redémarrage du serveur,
        go, back = extra['water']        # d'ici là seules elles échouent au chargement (on/off restent valides)
        w(f'{T}/water_on', [f'# {label} : biome du thème sur les colonnes d\'eau du spawn (couleur de l\'eau)'] + go)
        w(f'{T}/water_off', [f'# {label} : rend le biome the_void aux colonnes d\'eau du spawn'] + back)
        on_x, off_x = [f'function mg:{T}/water_on'], [f'function mg:{T}/water_off'] + off_x
    for n, ls in extra.get('files', {}).items():
        w(f'{T}/{n}', ls)
    fx = fx + [f'function mg:{T}/mobs']
    mob_lines = [f'# {label} : animaux du thème, chaque seconde (joueur au spawn : chunks chargés, comptes justes)',
                 'execute unless entity @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,limit=1] run return 0',
                 f'execute as @e[tag=mg.thmob] unless entity @s[{MOB_BOX}] run function mg:lobby/theme/spot {{f:"lobby/theme/back"}}']
    for m in mobs:
        sel = f'@e[type={m["entity"]},tag=mg.th_{m["key"]}]'
        mob_lines += [f'execute store result score $thn mg.st if entity {sel}',
                      f'execute if score $thn mg.st matches ..{m["n"] - 1} run function mg:lobby/theme/spot {{f:"{T}/{m["key"]}"}}',
                      f'execute if score $thn mg.st matches {m["n"] + 1}.. as {sel[:-1]},limit=1,sort=random] run function mg:lobby/theme/gone']
        tags = ['mg.thm', 'mg.thmob', f'mg.th_{m["key"]}'] + (['mg.thdress'] if m['dress'] else [])
        summon = lambda nb: f'summon {m["entity"]} ~ ~ ~ {{Tags:{js(tags)},{MOB_BASE}{"," + nb if nb else ""}}}'
        body = [f'# {label} : un animal du thème à cet endroit (appelé par lobby/theme/spot)']
        if m['rp_nbt']:
            body += ['execute if score $rp mg.st matches 1 run ' + summon(m['rp_nbt']), 'execute unless score $rp mg.st matches 1 run ' + summon(m['nbt'])]
        else:
            body.append(summon(m['nbt']))
        if m['yaw']:
            body.append(f'execute as @e[type={m["entity"]},tag=mg.th_{m["key"]},distance=..0.1] store result entity @s Rotation[0] float 1 run random value 0..359')
        w(f'{T}/{m["key"]}', body)
        if m['dress']:
            model, (tx, ty, tz), sc, invis = m['dress']
            w(f'{T}/dress_{m["key"]}', [f'# {label} : habillage resource pack (@s = animal, position = animal)',
                                        'summon minecraft:item_display ~ ~ ~ {Tags:["mg.thm","mg.thrid","mg.thnew"],item_display:"head",'
                                        'teleport_duration:3,item:{id:"minecraft:flower_banner_pattern",count:1,components:'
                                        f'{{"minecraft:item_model":"{model}"}}}},transformation:{{left_rotation:[0f,0f,0f,1f],'
                                        f'right_rotation:[0f,0f,0f,1f],translation:[{tx}f,{ty}f,{tz}f],scale:[{sc}f,{sc}f,{sc}f]}}}}',
                                        'ride @e[type=minecraft:item_display,tag=mg.thnew,limit=1] mount @s',
                                        'tag @e[tag=mg.thnew] remove mg.thnew'] +
              (['effect give @s minecraft:invisibility infinite 0 true'] if invis else []))
    if any(m['dress'] for m in mobs):
        mob_lines += ['# habillage : chaque animal à habiller a son item_display monté, les orphelins disparaissent',
                      'execute if score $rp mg.st matches 1 run tag @e[tag=mg.thdress] add mg.thnd',
                      'execute as @e[type=minecraft:item_display,tag=mg.thrid] on vehicle run tag @s remove mg.thnd'] + \
                     [f'execute as @e[tag=mg.thnd,tag=mg.th_{m["key"]}] at @s run function mg:{T}/dress_{m["key"]}'
                      for m in mobs if m['dress']] + \
                     ['tag @e[tag=mg.thnd] remove mg.thnd',
                      'tag @e[type=minecraft:item_display,tag=mg.thrid] add mg.thor',
                      'execute as @e[tag=mg.thmob] on passengers run tag @s remove mg.thor',
                      'kill @e[tag=mg.thor]']
    if any(m['entity'] == 'minecraft:allay' for m in mobs):
        mob_lines += ['# un objet donné à un allay retombe par terre (on ne le perd pas, l\'allay ne le duplique pas)',
                      'execute as @e[type=minecraft:allay,tag=mg.thmob] if items entity @s weapon.mainhand * at @s run function mg:lobby/theme/allay_drop']
    w(f'{T}/mobs', mob_lines)
    on = [f'execute if block {x} {y} {z} {bid(o)} run setblock {x} {y} {z} {n}' for (x, y, z), (o, n) in sorted(CH.items())]
    off = [f'execute if block {x} {y} {z} {bid(n)} run setblock {x} {y} {z} {o}' for (x, y, z), (o, n) in sorted(CH.items())]
    w(f'{T}/on', [f'# {label} : pose le décor du spawn (généré par tools/lobby/gen_themes.py ; inverse : lobby/theme/off)',
                  f'execute if score $theme mg.st matches {tid} run return run tellraw @s {{"text":"Ce décor est déjà en place.","color":"gray"}}',
                  'execute if score $theme mg.st matches 1.. run function mg:lobby/theme/off',
                  f'scoreboard players set $theme mg.st {tid}', f'data modify storage mg:lobby theme set value {tid}',
                  f'function mg:{T}/place', 'tellraw @a ' + js(hello), f'execute as {LOBBY} at @s run playsound {snd} master @s ~ ~ ~ 1 0.8'])
    w(f'{T}/place', [f"# {label} : blocs du décor (là où le bloc d'origine est encore là), entités, eau ; "
                     'appelé par on et par lobby/theme/restore (redémarrage)'] + on + on_x +
      [f'function mg:{T}/reskin', 'function mg:lobby/food_skin', 'function mg:lobby/theme/water_fix'])
    w(f'{T}/off', [f'# {label} : chaque bloc d\'origine revient (s\'il n\'a pas changé entre-temps) — appelé par lobby/theme/off'] +
      off + off_x)
    w(f'{T}/reskin', [f'# {label} : entités du décor (mg.lby) ; rappelé par lobby/deco tant que le thème est actif',
                      'function mg:lobby/theme/clear'] + reskin)
    w(f'{T}/fx', [f'# {label} : ambiance, chaque seconde'] + fx)
    w(f'{T}/toggle', [f'# Admin (mg.opt {opt}) : pose ou retire le décor {label}',
                      f'execute if score $theme mg.st matches {tid} run return run function mg:lobby/theme/off',
                      f'function mg:{T}/on'])
    n = {}
    for _, nw in CH.values():
        n[bid(nw)[10:]] = n.get(bid(nw)[10:], 0) + 1
    stats.append(f'{key} : {len(CH)} blocs (' + ', '.join(f'{v} {k}' for k, v in sorted(n.items(), key=lambda t: -t[1])) + ')')

w('lobby/theme/off', ['# Retire le décor saisonnier en place ($theme) et rétablit le spawn d\'origine',
                      'execute unless score $theme mg.st matches 1.. run return run tellraw @s {"text":"Aucun décor saisonnier en place.","color":"gray"}'] +
  [f'execute if score $theme mg.st matches {tid} run function mg:lobby/theme/{key}/off' for tid, key, *_ in THEMES] +
  ['scoreboard players set $theme mg.st 0', 'data remove storage mg:lobby theme', 'function mg:lobby/theme/clear', 'function mg:lobby/theme/water_fix',
   'function mg:lobby/deco', 'function mg:lobby/food_skin',
   'tellraw @a[tag=mg.admin] {"text":"Décor saisonnier retiré, spawn d\'origine rétabli.","color":"gray"}'])
# Redémarrage / rechargement : le décor actif (score $theme, sinon sa copie mg:lobby theme) est reposé quand un joueur
# est au spawn depuis 5 s (chunks chargés) : blocs manquants, entités, eau ; rien n'est doublé
w('lobby/theme/restore', ['# Décor saisonnier reposé après un redémarrage (appelé par core/tick tant que $thrs >= 1)',
                          'scoreboard players add $thrs mg.st 1',
                          'execute if score $thrs mg.st matches ..100 run return 0',
                          'scoreboard players set $thrs mg.st 0',
                          'execute unless score $theme mg.st matches 1.. store result score $theme mg.st run data get storage mg:lobby theme'] +
  [f'execute if score $theme mg.st matches {tid} run function mg:lobby/theme/{key}/place' for tid, key, *_ in THEMES] +
  ['execute if score $theme mg.st matches 1.. store result storage mg:lobby theme int 1 run scoreboard players get $theme mg.st'])
w('lobby/theme/reskin', ['# Appelé à la fin de lobby/deco : rhabille les entités du décor selon le thème actif'] +
  [f'execute if score $theme mg.st matches {tid} run function mg:lobby/theme/{key}/reskin' for tid, key, *_ in THEMES] + ['function mg:lobby/food_skin'])
w('lobby/theme/tick', ['# Habillage des animaux tourné comme eux (chaque tick), puis ambiance du thème (chaque seconde)',
                       'execute as @e[type=minecraft:item_display,tag=mg.thrid] at @s on vehicle rotated as @s on passengers '
                       'if entity @s[tag=mg.thrid] run rotate @s ~ 0',
                       'scoreboard players add $tht mg.st 1', 'execute if score $tht mg.st matches ..19 run return 0',
                       'scoreboard players set $tht mg.st 0'] +
  [f'execute if score $theme mg.st matches {tid} run function mg:lobby/theme/{key}/fx' for tid, key, *_ in THEMES])
w('lobby/theme/spot', ['# Point d\'herbe du spawn tiré au hasard : y lance mg:$(f) (exécutant conservé) — généré par gen_themes.py',
                       f'execute store result score $thp mg.st run random value 1..{len(SPOTS)}'] +
  [f'$execute if score $thp mg.st matches {i} positioned {x + 0.5} {y} {z + 0.5} run function mg:$(f)' for i, (x, y, z) in enumerate(SPOTS, 1)])
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
w('lobby/theme/water_fix', fix)
w('lobby/theme/back', ['# Animal du thème sorti du spawn : ramené sur un point au hasard (appelé par lobby/theme/spot)', 'tp @s ~ ~ ~'])
w('lobby/theme/gone', ['# Retire un animal du thème sans animation de mort ni butin (@s)',
                       'execute on passengers run kill @s[type=minecraft:item_display]',
                       'execute at @s run tp @s ~ -300 ~', 'kill @s'])
w('lobby/theme/clear', ['# Retire toutes les entités des thèmes (titre, animaux, habillages)',
                        'kill @e[type=minecraft:item_display,tag=mg.thrid]',
                        'execute as @e[tag=mg.thmob] run function mg:lobby/theme/gone', 'kill @e[tag=mg.thm]'])
w('lobby/theme/allay_drop', ['# Allay du thème qui tient un objet (@s, position = allay) : l\'objet retombe au sol',
                             'summon minecraft:item ~ ~ ~ {Tags:["mg.thdrop"],Item:{id:"minecraft:stone",count:1},PickupDelay:10s}',
                             'data modify entity @e[type=minecraft:item,tag=mg.thdrop,limit=1] Item set from entity @s equipment.mainhand',
                             'tag @e[tag=mg.thdrop] remove mg.thdrop',
                             'item replace entity @s weapon.mainhand with minecraft:air'])
os.makedirs(os.path.join(C.D, 'worldgen', 'biome'), exist_ok=True)      # eau rouge d'Halloween : the_void + water_color
with open(os.path.join(C.D, 'worldgen', 'biome', 'halloween.json'), 'w', encoding='utf-8', newline='\n') as f:
    f.write(js({'attributes': {'minecraft:visual/sky_color': '#7ba4ff', 'minecraft:visual/water_fog_color': '#3a0505'},
                'carvers': [], 'downfall': 0.5, 'effects': {'water_color': '#a3120c'}, 'features': [],
                'has_precipitation': False, 'spawn_costs': {},
                'spawners': {k: [] for k in ('ambient', 'axolotls', 'creature', 'misc', 'monster', 'underground_water_creature',
                                              'water_ambient', 'water_creature')},
                'temperature': 0.5}) + '\n')

# ------------------------------------------------------------------ branchements
C.patch('core/tick', 'execute if score $setup mg.st matches 1 run function mg:lobby/ev/tick',
        ['execute if score $theme mg.st matches 1.. run function mg:lobby/theme/tick'])
C.patch('core/tick', 'execute if score $theme mg.st matches 1.. run function mg:lobby/theme/tick',
        [f'execute if score $thrs mg.st matches 1.. if entity {LOBBY} run function mg:lobby/theme/restore'])
C.patch('core/load', 'scoreboard objectives add mg.st dummy', ['scoreboard players set $thrs mg.st 1'])
C.patch('lobby/deco', 'data modify storage mg:lobby deco3 set value 1b',
        ['execute if score $theme mg.st matches 1.. run function mg:lobby/theme/reskin'])
C.patch('core/opt', 'execute if score @s mg.opt matches 62..65 run function mg:tpg/run',
        [f'execute if score @s mg.opt matches {THEMES[0][3]}..{THEMES[-1][3]} unless entity @s[tag=mg.admin] run tellraw @s {{"text":"⚠ Réservé aux admins.","color":"red"}}'] +
        [f'execute if score @s mg.opt matches {opt} if entity @s[tag=mg.admin] run function mg:lobby/theme/{key}/toggle' for _, key, _, opt, _ in THEMES])
C.patch('desinstaller', '# Désinstallation (OP) — retire scoreboards, équipes, décor et zones chargées',
        ['execute if score $theme mg.st matches 1.. run function mg:lobby/theme/off'])
print(f'Thèmes ({len(DYN)} zones dynamiques évitées) :')
for s in stats:
    print('  ' + s)
