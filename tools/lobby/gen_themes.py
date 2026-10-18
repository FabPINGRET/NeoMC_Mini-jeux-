"""🎃🎄 Décors saisonniers du spawn, réversibles : python tools/lobby/gen_themes.py .   (après gen_lobby.py, tools/admin/gen_tp_general.py et gen_events.py : ancres de core/opt et core/tick)

Admin : menu des événements du lobby → « 🎃 Déco Halloween » (mg.opt 73) / « 🎄 Déco Noël » (mg.opt 74) : bascule
(pose le thème, ou le retire s'il est déjà en place ; un seul thème à la fois, l'autre est retiré d'abord).
Aussi : /function mg:lobby/theme/<halloween|noel>/on, /function mg:lobby/theme/off ($theme : 0 aucun, 1 Halloween, 2 Noël).

Le générateur relit les fonctions de construction du spawn (lobby/*build*, parkour/build) pour reconstituer chaque bloc
d'origine ; « on » ne pose un bloc que si le bloc d'origine est encore là, « off » ne remet l'original que si le bloc du
thème est encore là (rien d'autre n'est écrasé). Les plots et les zones modifiées par d'autres fonctions (jeux,
animations) ne sont jamais touchés. Les entités du décor (mg.lby) sont rhabillées par lobby/theme/<t>/reskin, rappelé à
chaque lobby/deco (bascule du resource pack) ; « off » relance lobby/deco, qui repose le décor d'origine.
« on » = place (blocs, entités, eau) + messages ; lobby/theme/restore rappelle place après un redémarrage, d'après $theme
ou sa copie dans le storage mg:lobby theme (lobby/theme/sync rétablit $theme d'après le storage s'il est perdu ; $thrs :
compteur de restore, remis à 1 par core/load et par la reconstruction du spawn, lobby/build_end).
Entités : toutes portent le tag mg.thx (jamais mg.thm : Tron l'utilise comme tag temporaire) ; lobby/theme/clear retire le
titre et toutes les entités des thèmes (animaux, habillages) et, pour les anciens mondes, le titre taggé mg.thm (jamais de kill
générique sur ce tag) ; lobby/theme/gone retire un animal (la traînée d'un bonhomme de neige fond) ; lobby/theme/allay_drop
fait lâcher à un allay du thème l'objet qu'on lui a donné. Sans thème, core/tick balaie les animaux restants. Les socles
d'élytra sont réservés (theme_world.reserve) : ni décor ni animal autour.
Les fichiers générés pour un nouveau thème ou une nouvelle fonctionnalité restent sous lobby/theme/ : theme_world.load ignore
ce dossier en cherchant les zones modifiées par les jeux.
Ajouter un thème : une fonction theme_<nom>() qui remplit CH et renvoie (reskin, fx, hello, mobs, extra), puis l'inscrire
dans THEMES (et dans tools/lobby/gen_theme_maps.py, qui habille aussi les cartes de jeu pendant les parties). Particules qui
tombent par intermittence : les déclarer dans SPECS de theme_fall.py et mettre TF.fx_call(clé, LOBBY) dans le fx du thème.

Modules (jamais lancés seuls, chargés ici après C.init) : theme_world.py (modèle du spawn : W, DYN, CH, familles de
blocs, zones réservées), theme_water.py (fontaines, cascades, biome du thème (eau, herbe, feuillage), water_fix, water_check), theme_mobs.py (animaux,
spot/back/gone/clear), theme_core.py (off, sync, restore, reskin, tick), theme_fall.py (feuilles et neige qui tombent
par intermittence), theme_npcs.py (PNJ : sorcière d'Halloween, lutin de Noël), theme_stew.py (ragoût de la sorcière : effets
vanilla et maison tirés à la consommation, chronos, nettoyages), theme_banner.py (bandeau : bossbar qui présente à tour de rôle
les nouveautés du thème en place).
"""
import os
import random
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'arcade'))
sys.path.insert(0, HERE)
import common as C                                               # noqa: E402

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
F = C.F

import theme_core as TC                                          # noqa: E402
import theme_fall as TF                                          # noqa: E402
import theme_mobs as TM                                          # noqa: E402
import theme_banner as TB                                        # noqa: E402
import theme_npcs as TN                                          # noqa: E402
import theme_water as TWA                                        # noqa: E402
import theme_world as TW                                         # noqa: E402
from theme_mobs import mob                                       # noqa: E402
from theme_water import FOUNT, theme_biome                       # noqa: E402
from theme_world import (CH, DIRT, DYN, FLOWERS, G, GROUND, LOBBY, SNOWABLE, TUFT, W, WALLS, bid, canopy,  # noqa: E402
                         change, solid, states, tuft_free)

TW.load(F)                               # W, DYN, PLOTS, RESERVED remplis sur place, puis ce qui en dérive
TWA.load()                               # (TM.load : après les thèmes, il lui faut les cellules qu'ils changent)
TN.prepare()                             # place du PNJ vérifiée et réservée : avant les thèmes (change() passe par free())
HALLOWEEN_BIOME = 'halloween'            # biome du thème (eau rouge, herbe et feuillage gris) : worldgen/biome/<nom>.json, mg:<nom> dans fillbiome

FACES = ['north', 'south', 'east', 'west']


def on_fences(rnd, p, blocks):
    for (x, y, z), b in sorted(W.items()):
        if bid(b) == 'minecraft:spruce_fence' and (x, y + 1, z) not in W and rnd.random() < p:
            change((x, y + 1, z), f'minecraft:{rnd.choice(blocks)}_candle[lit=true,candles={rnd.randint(1, 4)}]')


IT = 'execute as @e[type=minecraft:item_display,tag=mg.lby] if items entity @s contents '


def item_swap(pred, item):
    return f'{IT}{pred} run item replace entity @s contents with {item}'


def title(parts):
    return ('summon minecraft:text_display 0.5 74 0.5 {Tags:["mg.lby","' + TM.THEME_TAG + '"],billboard:"center",background:1426063360,'
            'shadow:1b,text:' + js(parts) + ',transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],'
            'right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}')


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
        if tuft_free(up) and rnd.random() < 0.045:
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
    crown = canopy()                                     # colonne (x, z) -> plus haut feuillage à 2 blocs près
    for (x, y, z), b in sorted(W.items()):               # feuilles mortes : tapis sous les arbres, quelques-unes ailleurs
        if bid(b) not in GROUND or x * x + z * z < 36 or y < G - 1:
            continue
        up = (x, y + 1, z)
        under = y < crown.get((x, z), -999) <= y + 12
        if tuft_free(up) and lrnd.random() < (0.4 if under else 0.06):
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
          *TF.fx_call('halloween', LOBBY),               # feuilles qui tombent par intermittence (theme_fall.py)
          'execute store result score $thr mg.st run random value 1..40',
          f'execute if score $thr mg.st matches 1 in minecraft:overworld as {LOBBY} at @s run playsound minecraft:ambient.cave ambient @s ~ ~ ~ 0.6 1']
    hello = ([{'text': '🎃 ', 'color': 'gold'}, {'text': 'Le spawn se pare de ses habits d\'Halloween… Bouh !', 'color': 'gold', 'bold': True}],
             'minecraft:entity.witch.celebrate')
    mobs = [mob('bat', 'minecraft:bat', 8),
            mob('ghost', 'minecraft:allay', 6, 'Silent:1b', ('mg:hat/ghost', [0, -0.3, 0], 1.0, True))]
    # water = biome du thème (eau + herbe + feuillage)
    return reskin, fx, hello, mobs, {'water': theme_biome(f'mg:{HALLOWEEN_BIOME}'), 'npc': 'witch',
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
        if near_log and bid(W.get(up)) in TUFT and rnd.random() < 0.5:
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
    fx = [*TF.fx_call('noel', LOBBY),                   # neige et cendre blanche qui tombent par intermittence (theme_fall.py)
          'execute store result score $thr mg.st run random value 1..45',
          f'execute if score $thr mg.st matches 1 in minecraft:overworld as {LOBBY} at @s run playsound minecraft:block.amethyst_block.chime ambient @s ~ ~2 ~ 1 0.8']
    hello = ([{'text': '🎄 ', 'color': 'red'}, {'text': 'Il neige sur le spawn… Joyeuses fêtes !', 'color': 'green', 'bold': True}],
             'minecraft:entity.player.levelup')
    # bonshommes de neige immobiles : le spawn a mob_griefing à true, en marchant ils laisseraient des traînées de neige
    mobs = [mob('snowman', 'minecraft:snow_golem', 6, 'NoAI:1b,Pumpkin:0b', rand_yaw=True),
            mob('reindeer', 'minecraft:cow', 3, 'Silent:1b,variant:"minecraft:cold"', rp_nbt='Silent:1b,variant:"mg:reindeer"'),
            mob('rudolph', 'minecraft:cow', 1, 'Silent:1b,variant:"minecraft:cold"', rp_nbt='Silent:1b,variant:"mg:rudolph"')]
    return reskin, fx, hello, mobs, {'npc': 'elf'}       # la traînée de chaque bonhomme fond dans lobby/theme/gone


THEMES = [(1, 'halloween', '🎃 Halloween', 73, theme_halloween), (2, 'noel', '🎄 Noël', 74, theme_noel)]

# ------------------------------------------------------------------ fonctions
stats = []
NPC_THEMES = []                          # (id, clé) des thèmes qui ont un PNJ
ALLCH = set()                            # cellules changées par au moins un thème (points d'apparition des animaux)
for tid, key, label, opt, make in THEMES:
    CH.clear()
    reskin, fx, (hello, snd), mobs, extra = make()
    T = f'lobby/theme/{key}'
    on_x, off_x = [], list(extra.get('off', []))
    if 'water' in extra:                 # water = biome du thème (eau + herbe + feuillage)
        on_x, off_water = TWA.write_toggle(T, label, extra['water'])
        off_x = off_water + off_x
    for n, ls in extra.get('files', {}).items():
        w(f'{T}/{n}', ls)
    fx = fx + [f'function mg:{T}/mobs']
    if 'npc' in extra:                   # PNJ du thème : réhabillé avec le décor, gardé chaque seconde, cadeaux retirés au off
        npc_reskin, npc_fx, npc_off = TN.write_npc(T, label, extra['npc'])
        reskin, fx, off_x = reskin + npc_reskin, fx + npc_fx, off_x + npc_off
        NPC_THEMES.append((tid, key))
    TM.write_mobs(T, label, mobs)
    if key in TF.SPECS:                  # chutes par intermittence (feuilles, neige) : thème sans SPECS = pas de chute
        TF.write_fall(key, label)
    on = [f'execute if block {x} {y} {z} {bid(o)} run setblock {x} {y} {z} {n}' for (x, y, z), (o, n) in sorted(CH.items())]
    off = [f'execute if block {x} {y} {z} {bid(n)} run setblock {x} {y} {z} {o}' for (x, y, z), (o, n) in sorted(CH.items())]
    ALLCH.update(CH)
    w(f'{T}/on', [f'# {label} : pose le décor du spawn (généré par tools/lobby/gen_themes.py ; inverse : lobby/theme/off)',
                  'function mg:lobby/theme/sync',
                  f'execute if score $theme mg.st matches {tid} run return run tellraw @s {{"text":"Ce décor est déjà en place.","color":"gray"}}',
                  '# $thsw : l\'autre thème est retiré pour laisser la place, sans le message « décor retiré »',
                  'scoreboard players set $thsw mg.st 1',
                  'execute if score $theme mg.st matches 1.. run function mg:lobby/theme/off',
                  'scoreboard players set $thsw mg.st 0',
                  f'scoreboard players set $theme mg.st {tid}', f'data modify storage mg:lobby theme set value {tid}',
                  *(TF.on_lines() if key in TF.SPECS else []), f'function mg:{T}/place', 'tellraw @a ' + js(hello), f'execute as {LOBBY} at @s run playsound {snd} master @s ~ ~ ~ 1 0.8'])
    w(f'{T}/place', [f"# {label} : blocs du décor (là où le bloc d'origine est encore là), entités, eau ; "
                     'appelé par on et par lobby/theme/restore (redémarrage)',
                     '# eau remise d\'aplomb d\'abord : le décor (glace...) se pose sur l\'eau réparée',
                     'function mg:lobby/theme/water_fix'] + on + on_x + [f'function mg:{T}/reskin', 'function mg:lobby/food_skin', 'function mg:hall/theme_on'])
    w(f'{T}/off', [f'# {label} : chaque bloc d\'origine revient (s\'il n\'a pas changé entre-temps) — appelé par lobby/theme/off'] +
      off + off_x)
    w(f'{T}/reskin', [f'# {label} : entités du décor (mg.lby) ; rappelé par lobby/deco tant que le thème est actif',
                      'function mg:lobby/theme/clear'] + reskin)
    w(f'{T}/fx', [f'# {label} : ambiance, chaque seconde'] + fx)
    w(f'{T}/toggle', [f'# Admin (mg.opt {opt}) : pose ou retire le décor {label}', 'function mg:lobby/theme/sync',
                      f'execute if score $theme mg.st matches {tid} run return run function mg:lobby/theme/off',
                      f'function mg:{T}/on'])
    n = {}
    for _, nw in CH.values():
        n[bid(nw)[10:]] = n.get(bid(nw)[10:], 0) + 1
    stats.append(f'{key} : {len(CH)} blocs (' + ', '.join(f'{v} {k}' for k, v in sorted(n.items(), key=lambda t: -t[1])) + ')')

TC.write_dispatch(THEMES)               # off, sync, restore, reskin, tick (appellent le thème actif)
TF.write_common()                        # fall_tick, fall_flip (cycle des chutes)
TM.load(ALLCH)                           # points d'apparition des animaux (hors cellules changées par un thème)
TM.write_common()                        # spot, back, gone, clear, allay_drop
TWA.write_fix(ALLCH)                     # water_fix
TWA.write_check(ALLCH)                   # water_check (diagnostic, ne modifie rien)
TN.write_common(NPC_THEMES)              # npc_use, npc_second, fw_use, advancement mg:theme_fw
TWA.write_biome(HALLOWEEN_BIOME, water_color='#a3120c', fog_color='#3a0505', grass_color='#778272',
                foliage_color='#878d76', dry_foliage_color='#a0a69c')   # worldgen/biome/halloween.json (herbe, feuillage, feuillage sec : palette du jardin pâle)

# ------------------------------------------------------------------ branchements
TC.write_wiring(THEMES)                # branchements dans core/tick, core/load, lobby/deco, core/opt, desinstaller
TN.wire()                                # objectif mg.thc, boucle de clic, nettoyages
TB.write(THEMES)                         # bandeau (bossbar mg:thb) : lignes par thème, banner, banner_hide, branchements (tick, off, load, désinstaller)
print(f'Thèmes ({len(DYN)} zones dynamiques évitées) :')
for s in stats:
    print('  ' + s)
