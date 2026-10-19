"""🌙 Ombrelune : RPG médiéval-fantastique en monde ouvert (dimension mg:ombrelune), relié au lobby par un portail (avenue est).

    python tools/arcade/gen_ombrelune.py .     (après gen_terranova.py ; puis tools/resourcepack/gen_rp.py pour les dragons 3D)

Modules : ol_world (relief, biomes, végétation), ol_structs (constructions, donjons), ol_beasts / ol_beast_fn (dragons articulés),
ol_mobs (bestiaire, apparitions, victoires), ol_class (niveaux, classes, compétences, forge), ol_quest (campagne, PNJ, quêtes, boutiques,
voyages, succès), ol_boss (boss, donjons), ol_cine (cinématiques, indicateur). Tout est écrit sous data/mg/function/ombre/ (repartie de zéro).
Ajouter la dimension et ses biomes demande un redémarrage du serveur ; la carte se construit seule ensuite (~4 min).
"""
import os
import re
import shutil
import sys
import json

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
shutil.rmtree(os.path.join(C.F, 'ombre'), ignore_errors=True)
shutil.rmtree(os.path.join(C.D, 'advancement', 'ombre'), ignore_errors=True)

import ol_world as W
import ol_structs as S
from ol_core import w, js, P, TEXT, DIM, TR, tdisp, wjson, say, nm, lo, WF

STRUCTS = S.all_structures()
import ol_beast_fn  # noqa: E402,F401
import ol_mobs as M  # noqa: E402
import ol_class as CL  # noqa: E402
import ol_quest as Q  # noqa: E402
import ol_boss as BO  # noqa: E402
import ol_cine  # noqa: E402,F401

PX, PZ = 40, -9                      # portail du lobby (avenue est, côté nord ; ouverture x 39..41, z -9)
SPAWN = (0.5, 65, 9.5)

# ================================================================ construction du monde, région par région
# Les commandes de construction sont stockées comme du texte (stockage mg:ombre q, par paquets de 2500) et exécutées par une macro
# ($$(c)) au fil de la construction : compilées une à une, elles ne pèsent rien en mémoire au chargement du datapack. Seuls les chunks
# de la région en cours sont chargés (forceload), et chaque région attend que tous ses chunks soient prêts avant de construire.
RKEYS = list(W.REGIONS)
RIDX = {r: i + 1 for i, r in enumerate(RKEYS)}
PACK = 2500
PACKS = []                                   # (n° de région, commandes)
for r in RKEYS:
    cmds = W.terrain_cmds(r) + W.biome_fill(r) + W.VEG[r] + [c for n_, rg, v in STRUCTS if rg == r for c in v.cmds()] + W.WALLS_R[r]
    for i in range(0, len(cmds), PACK):
        PACKS.append((RIDX[r], cmds[i:i + PACK]))
NP = len(PACKS)
NS = sum(len(c) for _, c in PACKS)
for i, (ri, cmds) in enumerate(PACKS):
    w(f'd/{i + 1}', [f'# Données de construction {i + 1}/{NP} (région {ri}, commandes en texte)', f'scoreboard players set $olrr mg.st {ri}',
                     'data modify storage mg:ombre q set value [' + ','.join(json.dumps(c, ensure_ascii=False) for c in cmds) + ']'])


def chunks_of(r):
    x0, z0, x1, z1 = W.rect(r)
    return [(x, z) for x in range(x0, x1, 16) for z in range(z0, z1, 16)]


FLR = {r: '{} {} {} {}'.format(W.rect(r)[0], W.rect(r)[1], W.rect(r)[2] - 1, W.rect(r)[3] - 1) for r in RKEYS}
for r in RKEYS:
    w(f'b/ld{RIDX[r]}', [f'# Tous les chunks de la région {r} sont-ils chargés ?'] + [f'execute unless loaded {x} 64 {z} run return 0' for x, z in chunks_of(r)] + ['return 1'])
    w(f'b/fl{RIDX[r]}', [f'forceload add {FLR[r]}'])
    w(f'b/uf{RIDX[r]}', [f'forceload remove {FLR[r]}'])
w('b/ready', ['# La région en cours ($olrl) est-elle chargée ?'] + [f'execute if score $olrl mg.st matches {i} run return run function mg:{P}/b/ld{i}' for i in RIDX.values()] + ['return 0'])
w('b/switch', ["# Région suivante : on décharge l'ancienne, on charge la nouvelle"] +
  [f'execute if score $olrl mg.st matches {i} run function mg:{P}/b/uf{i}' for i in RIDX.values()] +
  ['scoreboard players operation $olrl mg.st = $olrr mg.st'] + [f'execute if score $olrl mg.st matches {i} run function mg:{P}/b/fl{i}' for i in RIDX.values()])
w('b/exec', ['$$(c)'])
w('b/run', ['# Exécute la prochaine commande de construction (boucle de $olk commandes)', 'execute unless data storage mg:ombre q[0] run return 0',
            'data modify storage mg:ombre c.c set from storage mg:ombre q[0]', 'data remove storage mg:ombre q[0]', f'function mg:{P}/b/exec with storage mg:ombre c',
            'scoreboard players remove $olk mg.st 1', f'execute if score $olk mg.st matches 1.. run function mg:{P}/b/run'])
w('b/next', ['# Paquet suivant de commandes', 'scoreboard players add $olb mg.st 1'] +
  [f'execute if score $olb mg.st matches {i + 1} run function mg:{P}/d/{i + 1}' for i in range(NP)])
w('wb_step', ['# Construction : 220 commandes par tick, dans la région chargée',
              f'execute unless data storage mg:ombre q[0] run function mg:{P}/b/next',
              f'execute if score $olb mg.st matches {NP + 1}.. run return run function mg:{P}/wb_done',
              f'execute unless score $olrl mg.st = $olrr mg.st in {DIM} run function mg:{P}/b/switch',
              f'execute in {DIM} unless function mg:{P}/b/ready run return run schedule function mg:{P}/wb_step 2t',
              'scoreboard players set $olk mg.st 220', f'execute in {DIM} run function mg:{P}/b/run',
              f'schedule function mg:{P}/wb_step 1t'])
w('world_build', ["# Construction d'Ombrelune (ou reconstruction complète, ~3 min)", 'scoreboard players set $olb mg.st 0', 'scoreboard players set $olrl mg.st 0',
                  'scoreboard players set $olrr mg.st 0', 'data remove storage mg:ombre q', f'execute in {DIM} run forceload remove all',
                  f'schedule function mg:{P}/wb_step 20t', 'tellraw @a[tag=mg.admin] {"text":"🌙 Construction de la carte d\'Ombrelune lancée (~3 min).","color":"light_purple"}'])
w('wb_done', ['# Ombrelune construite : entités permanentes ensuite', f'execute in {DIM} run kill @e[type=minecraft:item,x=-240,y=0,z=-240,dx=480,dy=300,dz=480]',
              f'execute in {DIM} run forceload remove all', 'data modify storage mg:ombre built set value 1b', 'data remove storage mg:ombre q',
              'tellraw @a[tag=mg.admin] {"text":"🌙 Ombrelune est construite (PNJ et objets en cours de pose).","color":"light_purple"}', f'function mg:{P}/st/start'])

# dimension et biomes
wjson('dimension/ombrelune.json', {'type': 'minecraft:overworld', 'generator': {'type': 'minecraft:flat', 'settings': {
    'biome': 'minecraft:the_void', 'layers': [], 'lakes': False, 'features': False, 'structure_overrides': []}}})
for b, d in W.BIOMES.items():
    p = os.path.join(C.D, 'worldgen', 'biome', b.split(':')[1] + '.json')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(W.biome_json(**d), f, separators=(',', ':'), sort_keys=True)
        f.write('\n')

# ================================================================ portail du lobby
PB = ['# Portail d\'Ombrelune au lobby (avenue est, côté nord), reconstruit s\'il disparaît', 'kill @e[tag=mg.olport]',
      f'fill {PX - 4} 64 {PZ - 4} {PX + 4} 75 {PZ + 1} minecraft:air',
      f'fill {PX - 4} 63 {PZ - 4} {PX + 4} 63 {PZ + 1} minecraft:polished_deepslate',
      f'fill {PX - 3} 63 {PZ - 3} {PX + 3} 63 {PZ} minecraft:deepslate_tiles',
      f'fill {PX - 1} 63 {PZ + 1} {PX + 1} 63 {PZ + 5} minecraft:stone_bricks',
      f'fill {PX - 1} 64 {PZ + 1} {PX + 1} 66 {PZ + 5} minecraft:air',
      f'fill {PX - 2} 64 {PZ} {PX - 2} 70 {PZ} minecraft:polished_blackstone_bricks', f'fill {PX + 2} 64 {PZ} {PX + 2} 70 {PZ} minecraft:polished_blackstone_bricks',
      f'fill {PX - 3} 64 {PZ} {PX - 3} 69 {PZ} minecraft:crying_obsidian', f'fill {PX + 3} 64 {PZ} {PX + 3} 69 {PZ} minecraft:crying_obsidian',
      f'fill {PX - 3} 71 {PZ} {PX + 3} 71 {PZ} minecraft:polished_blackstone_brick_slab',
      f'fill {PX - 1} 70 {PZ} {PX + 1} 70 {PZ} minecraft:chiseled_polished_blackstone',
      f'setblock {PX} 72 {PZ} minecraft:amethyst_block', f'setblock {PX} 73 {PZ} minecraft:amethyst_cluster[facing=up]',
      f'setblock {PX - 3} 70 {PZ} minecraft:soul_lantern', f'setblock {PX + 3} 70 {PZ} minecraft:soul_lantern',
      f'setblock {PX} 63 {PZ} minecraft:chiseled_polished_blackstone',
      f'summon minecraft:text_display {PX + 0.5} 75.4 {PZ + 0.6} {{Tags:["mg.olport"],text:{js(TEXT("🌙 OMBRELUNE", "light_purple", bold=True))},background:-1442840576,{TR % (0, 0, 0, 2.6, 2.6, 2.6)}}}',
      f'summon minecraft:text_display {PX + 0.5} 74.95 {PZ + 0.6} {{Tags:["mg.olport"],text:{js(TEXT("RPG médiéval-fantastique : 8 régions, dragons, donjons", "gray"))},background:0,{TR % (0, 0, 0, 0.9, 0.9, 0.9)}}}',
      f'summon minecraft:text_display {PX + 0.5} 64.4 {PZ + 1.2} {{Tags:["mg.olport"],text:{js(TEXT("▶ entre dans le portail", "yellow"))},background:0,{TR % (0, 0, 0, 0.8, 0.8, 0.8)}}}',
      f'function mg:{P}/spawn_clean']
w('portal_build', PB)
w('spawn_clean', ['# Abords du portail : arbres coupés, passage depuis l\'avenue',
                  f'fill {PX - 7} 64 {PZ - 8} {PX + 7} 80 {PZ + 2} minecraft:air replace #minecraft:leaves',
                  f'fill {PX - 7} 64 {PZ - 8} {PX + 7} 80 {PZ + 2} minecraft:air replace #minecraft:logs',
                  'data modify storage mg:lobby olclean set value 1b'])
ENTER_SEL = ('tag=!mg.play,tag=!mg.out,tag=!mg.surv,tag=!mg.inplot,tag=!mg.visit,tag=!mg.lk,tag=!mg.pkr,tag=!mg.ely,tag=!mg.elyf,'
             f'gamemode=adventure,x={PX - 1},y=64,z={PZ},dx=2,dy=2,dz=0')
w('lobby_tick', ['# Chaque tick (monde des mini-jeux) : portail d\'Ombrelune, session du monde',
                 f'execute if score $setup mg.st matches 1 as @a[{ENTER_SEL}] run function mg:{P}/enter',
                 f'particle minecraft:dust{{color:[0.7,0.45,1.0],scale:1.1}} {PX + 0.5} 67 {PZ + 0.5} 1.0 1.4 0.05 0 3',
                 f'particle minecraft:reverse_portal {PX + 0.5} 67 {PZ + 0.5} 1.0 1.4 0.05 0 2',
                 f'execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block {PX} 63 {PZ} minecraft:chiseled_polished_blackstone run function mg:{P}/portal_build',
                 f'execute unless score $olw mg.st matches 1 if entity @a[tag=mg.olw] run function mg:{P}/session_start',
                 f'execute if score $olw mg.st matches 1 unless entity @a[tag=mg.olw] run function mg:{P}/session_end',
                 f'execute if score $olw mg.st matches 1 in {DIM} run function mg:{P}/tick'])
w('pre_tick', [f'execute as @a[tag=mg.olw] at @s unless dimension {DIM} run function mg:{P}/strayed'])
w('strayed', ['# @s a quitté Ombrelune autrement', 'tag @s remove mg.olw', 'tag @s remove mg.surv', f'function mg:{P}/untag'])

# ================================================================ entrée, sortie, session
w('enter', ['# @s entre dans le portail d\'Ombrelune (contexte : monde des mini-jeux)',
            f'execute unless data storage mg:ombre built run return run function mg:{P}/not_ready',
            'execute if entity @s[tag=mg.mpp] run return run tellraw @s {"text":"⚠ Tu participes à la Mini Party : Ombrelune sera accessible après.","color":"red"}',
            'function mg:lobkart/leave', 'function mg:parkour/quit', 'tag @s remove mg.inplot', 'tag @s remove mg.plabel', 'tag @s remove mg.visit',
            'tag @s add mg.surv', 'tag @s add mg.olw',
            'execute if score $state mg.st matches 0 run scoreboard players reset @s mg.vc', 'execute if score $state mg.st matches 0 run function mg:vote/refresh',
            'team leave @s', 'effect clear @s', 'clear @s', 'gamemode adventure @s', 'function mg:core/attr_reset',
            'attribute @s minecraft:fall_damage_multiplier base set 1', f'function mg:{P}/join', 'function mg:core/heal',
            f'execute in {DIM} run spawnpoint @s 6 65 7', f'execute in {DIM} run tp @s {SPAWN[0]} {SPAWN[1]} {SPAWN[2]} 180 0',
            f'function mg:{P}/kit', 'scoreboard players operation @s mg.olmp = @s mg.olmm', f'function mg:{P}/mana_bar',
            'title @s times 10 60 20', 'title @s title {"text":"OMBRELUNE","color":"light_purple","bold":true}',
            'title @s subtitle {"text":"Le royaume du crépuscule éternel","color":"gray"}',
            'tellraw @s ' + js([TEXT('🌙 OMBRELUNE', 'light_purple', bold=True), TEXT(' : bienvenue à Havreclair, voyageur !', 'yellow')]),
            'tellraw @s ' + js([TEXT(' 📖 Journal (case 8) : ', 'gold'), TEXT('quête, caractéristiques, bestiaire, voyage', 'gray')]),
            'tellraw @s ' + js([TEXT(' ✦ Mana : ', 'aqua'), TEXT('la barre d\'XP. Compétences en cases 3 à 6 (clic droit).', 'gray')]),
            'tellraw @s ' + js([TEXT(' 🌀 Pierres d\'appel : ', 'light_purple'), TEXT('voyage entre les régions. Sortir : pierre de la place ou Échap → ≡ Menu', 'gray')]),
            f'execute if score @s mg.olch matches 1.. run function mg:{P}/q/say', f'function mg:{P}/qloc',
            'execute at @s run playsound minecraft:block.portal.travel master @s ~ ~ ~ 0.3 1.6'])
w('not_ready', [f'tp @s {PX}.5 64 {PZ + 4}.5 180 0',
                'tellraw @s {"text":"🚧 Ombrelune est en construction (quelques minutes après le démarrage du serveur). Réessaie bientôt !","color":"yellow"}'])
w('menu_go', ['# @s : « Aller à Ombrelune » (menu Échap, trigger mg.sv 8)',
              'execute unless score $setup mg.st matches 1 run return run tellraw @s {"text":"⚠ Installation manquante : un OP doit d\'abord lancer /function mg:setup","color":"red"}',
              'execute if entity @s[tag=mg.olw] run return run tellraw @s {"text":"Tu es déjà à Ombrelune.","color":"gray"}',
              'execute if entity @s[tag=mg.play] run return run tellraw @s {"text":"⚠ Tu participes à la partie en cours : Ombrelune sera accessible après.","color":"red"}',
              'execute if entity @s[tag=mg.out] run return run tellraw @s {"text":"⚠ Partie en cours : Ombrelune sera accessible après.","color":"red"}',
              'execute if entity @s[tag=mg.dl] run return run tellraw @s [{"text":"⚔ Duel en cours : termine-le (ou abandonne-le) avant.","color":"red"}]',
              'execute if entity @s[tag=mg.gtw] run function mg:gta/leave', 'execute if entity @s[tag=mg.tvw] run function mg:terra/leave',
              'execute if entity @s[tag=mg.surv] run function mg:survie/leave', f'execute in minecraft:overworld run function mg:{P}/enter'])
JOIN_DEF = [('mg.olxp', 0), ('mg.olg', 50), ('mg.olch', 0), ('mg.olqp', 0), ('mg.olcl', 0), ('mg.olwt', 1), ('mg.olat', 0), ('mg.olsp', 0),
            ('mg.ols1', 0), ('mg.ols2', 0), ('mg.ols3', 0), ('mg.ols4', 0), ('mg.olbs', 0), ('mg.olbs2', 0), ('mg.olkt', 0), ('mg.olel', 0),
            ('mg.olsa', 0), ('mg.olsd', 0), ('mg.olct', 0), ('mg.olcn', 0), ('mg.olcp', 0), ('mg.olcd', 0), ('mg.olws', 0), ('mg.olpo', 0),
            ('mg.olpg', 0), ('mg.oltc', 0), ('mg.olac', 0), ('mg.olfur', 0), ('mg.olfire', 0), ('mg.olbless', 0), ('mg.olhorse', 0), ('mg.olsh', 0),
            ('mg.olbk', 0), ('mg.oldg', 0)] + [(f'mg.olm{i}', 0) for i in range(1, 10)] + [(f'mg.olq{i}', 0) for i in range(1, 17)]
w('join', ['# @s : scores à la première visite (gardés ensuite), réglages de la visite',
           'execute unless score @s mg.olpid matches 1.. run scoreboard players add $olpn mg.st 1',
           'execute unless score @s mg.olpid matches 1.. run scoreboard players operation @s mg.olpid = $olpn mg.st',
           'execute unless score @s mg.ollv matches 1.. run scoreboard players set @s mg.ollv 1'] +
  [f'execute unless score @s {o} matches -2147483648.. run scoreboard players set @s {o} {v}' for o, v in JOIN_DEF] +
  ['scoreboard players set @s mg.olrg -1', 'scoreboard players set @s mg.olal 0', 'scoreboard players set @s mg.olcf 0', 'scoreboard players set @s mg.olpk 0',
   'scoreboard players set @s mg.deaths 0', 'scoreboard players reset @s mg.olq', 'scoreboard players enable @s mg.oltk'] +
  [f'scoreboard players set @s mg.olc{i} 0' for i in range(0, 5)] +
  ['team add mg_ol', 'team modify mg_ol friendlyFire false', 'team modify mg_ol color light_purple', 'team join mg_ol @s', f'function mg:{P}/stats'])
w('untag', ['# @s : plus joueur d\'Ombrelune', f'function mg:{P}/cs/stop', 'title @s clear', 'title @s reset', 'team leave @s', f'function mg:{P}/stats_rm',
            'xp set @s 0 levels', 'xp set @s 0 points', f'function mg:{P}/horse_gone', 'tag @s remove mg.olintro', 'tag @s remove mg.olboss_in'])
w('leave', ['# @s retourne au lobby (contexte : monde des mini-jeux)', 'execute unless entity @s[tag=mg.olw] run return 0',
            'tag @s remove mg.olw', 'tag @s remove mg.surv', f'function mg:{P}/untag', 'function mg:core/reset_player',
            'attribute @s minecraft:fall_damage_multiplier base set 0',
            'tellraw @s [{"text":"⌂ Retour au lobby. Ta progression reste à Ombrelune (niveau ","color":"gold"},{"score":{"name":"@s","objective":"mg.ollv"},"color":"yellow"},{"text":", ","color":"gold"},{"score":{"name":"@s","objective":"mg.olg"},"color":"yellow"},{"text":" 💰).","color":"gold"}]'])
# ---- session : aucune zone chargée de force (seuls les chunks autour des joueurs). Les PNJ, pierres d'appel, objets de quête,
# marqueurs d'apparition… sont des entités permanentes (tag mg.ols) posées une fois dans le monde, région par région (st/…).
w('session_start', ['# Premier joueur à Ombrelune', 'scoreboard players set $olw mg.st 1', 'scoreboard players add $olses mg.st 1',
                    'scoreboard players set $olt mg.st 0', 'scoreboard players set $olsu mg.st 0', f'schedule function mg:{P}/session_setup 20t'])
w('session_setup', ['execute unless score $olw mg.st matches 1 run return 0', f'execute in {DIM} run function mg:{P}/setup'])
w('session_end', ['# Plus personne : entités de la session retirées', 'scoreboard players set $olw mg.st 0', 'schedule clear mg:ombre/session_setup', f'function mg:{P}/clear'])
w('clear', ['# Retire ce que la session a posé (pas les entités permanentes)', f'execute in {DIM} run kill @e[tag=mg.ol,tag=!mg.ols]', f'function mg:{P}/boss/clear',
            'team remove mg_ol', 'team remove mg_olel',
            f'execute in {DIM} run kill @e[type=minecraft:item,x=-240,y=0,z=-240,dx=480,dy=300,dz=480]',
            f'execute in {DIM} run kill @e[type=minecraft:experience_orb,x=-240,y=0,z=-240,dx=480,dy=300,dz=480]',
            f'execute in {DIM} run kill @e[type=minecraft:vex,x=-240,y=0,z=-240,dx=480,dy=300,dz=480]',
            f'execute in {DIM} run kill @e[type=minecraft:area_effect_cloud,x=-240,y=0,z=-240,dx=480,dy=300,dz=480]'])
RULES = [f'execute in {DIM} run difficulty normal', f'execute in {DIM} run gamerule spawn_mobs false', f'execute in {DIM} run gamerule mob_griefing false',
         f'execute in {DIM} run gamerule keep_inventory true', f'execute in {DIM} run gamerule immediate_respawn true',
         f'execute in {DIM} run gamerule advance_time false', f'execute in {DIM} run gamerule advance_weather false',
         f'execute in {DIM} run time set 11200', f'execute in {DIM} run weather clear']
w('rules', ["# Règles du monde d'Ombrelune : crépuscule fixe, pas d'apparitions naturelles, inventaire gardé"] + RULES)
w('setup', ['# Session (dans la dimension) : équipes, règles, barres des boss', f'function mg:{P}/clear', f'function mg:{P}/rules', f'function mg:{P}/consts',
            'team add mg_olel', 'team modify mg_olel color gold', 'team add mg_ol', 'team modify mg_ol friendlyFire false', 'team modify mg_ol color light_purple',
            'team join mg_ol @a[tag=mg.olw]', f'function mg:{P}/boss/setup', 'scoreboard players set $olsu mg.st 1'])

# ---- entités permanentes (posées après la construction, puis à chaque mise à jour du datapack qui les change)
STAT = Q.SETUP_NPC + Q.SETUP_WS + Q.SETUP_Q + Q.SETUP_LORE + Q.DECO + [l for k in Q.DOORS for l in Q.DOORS[k][1]] + BO.PSUM
STAT.append(tdisp(0.5, 76, 0.5, [TEXT('HAVRECLAIR\n', 'gold', bold=True), TEXT("Dernière cité libre d'Ombrelune", 'gray', bold=False)], 3.0))
for r, pts in M.SPAWN_PTS.items():
    for (x, y, z) in pts:
        STAT.append(f'summon minecraft:marker {x + 0.5} {y} {z + 0.5} {{Tags:["mg.ol","mg.olsp_{r}"]}}')
x, y, z = S.SPOTS['stable_pen']
for dx in (-4, 0, 4):
    STAT.append(f'summon minecraft:horse {x + dx} {y} {z} {{Tags:["mg.ol"],Variant:{abs(dx) * 129},PersistenceRequired:1b,Tame:1b}}')
for fac in ('north', 'south', 'east', 'west'):
    gx, gy_, gz = S.SPOTS['gate_' + fac]
    dx, dz = S.dir_vec(fac)
    for side in (-3, 3):
        px_, pz_ = (gx - dx * 13 + (side if dz else 0), gz - dz * 13 + (side if dx else 0))
        STAT.append(f'summon minecraft:vindicator {px_} 65 {pz_} {{Tags:["mg.ol"],NoAI:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,'
                    f'CustomName:{js(TEXT("Garde de Havreclair", "aqua"))},equipment:{{mainhand:{{id:"minecraft:iron_sword",count:1}},head:{{id:"minecraft:iron_helmet",count:1}},'
                    'chest:{id:"minecraft:iron_chestplate",count:1}},drop_chances:{mainhand:0f,head:0f,chest:0f},Rotation:[' + {'north': '180', 'south': '0', 'east': '-90', 'west': '90'}[fac] + 'f,0f]}')
GROUPS = {r: [] for r in RKEYS}
cur_r = None
for l in STAT:
    m = re.match(r'(?:summon \S+|setblock|fill) (-?[\d.]+) (-?[\d.]+) (-?[\d.]+)', l)
    if m:
        cur_r = W.region_at(int(float(m.group(1)) // 1), int(float(m.group(3)) // 1)) or 'hub'
    if l.startswith('#') or l.startswith('function') or cur_r is None:
        continue
    GROUPS[cur_r].append(l.replace('Tags:["mg.ol"', 'Tags:["mg.ol","mg.ols"'))
import zlib  # noqa: E402
SV = zlib.crc32(json.dumps(GROUPS, sort_keys=True).encode()) & 0x7fffffff
for r in RKEYS:
    x0, z0, x1, z1 = W.rect(r)
    w(f'st/{RIDX[r]}', [f'# Entités permanentes de la région {r} (retirées puis reposées)',
                         f'kill @e[tag=mg.ols,x={x0},y=-64,z={z0},dx={x1 - x0 - 1},dy=400,dz={z1 - z0 - 1}]'] + GROUPS[r])
w('st/start', ['# Pose des entités permanentes, région par région (chunks chargés le temps de la pose)', 'scoreboard players set $ols mg.st 1',
               'scoreboard players set $olsw mg.st 0', f'schedule function mg:{P}/st/step 10t'])
w('st/step', [f'execute if score $ols mg.st matches {len(RKEYS) + 1}.. run return run function mg:{P}/st/done',
              'execute if score $olsw mg.st matches 0 run scoreboard players operation $olrl mg.st = $ols mg.st'] +
  [f'execute if score $olsw mg.st matches 0 if score $ols mg.st matches {i} in {DIM} run function mg:{P}/b/fl{i}' for i in RIDX.values()] +
  ['scoreboard players set $olsw mg.st 1',
   f'execute in {DIM} unless function mg:{P}/b/ready run return run schedule function mg:{P}/st/step 5t'] +
  [f'execute if score $ols mg.st matches {i} in {DIM} run function mg:{P}/st/{i}' for i in RIDX.values()] +
  [f'execute if score $ols mg.st matches {i} in {DIM} run function mg:{P}/b/uf{i}' for i in RIDX.values()] +
  ['scoreboard players add $ols mg.st 1', 'scoreboard players set $olsw mg.st 0', f'schedule function mg:{P}/st/step 2t'])
w('st/done', [f'data modify storage mg:ombre sv set value {SV}', 'scoreboard players set $olrl mg.st 0',
              'tellraw @a[tag=mg.admin] {"text":"🌙 Ombrelune : PNJ et objets posés.","color":"light_purple"}'])
w('st/check', ['# Au chargement : entités permanentes à (re)poser si le datapack les a changées', 'execute unless data storage mg:ombre built run return 0',
               f'execute unless data storage mg:ombre {{sv:{SV}}} run function mg:{P}/st/start'])

# ================================================================ objets : localisateur, destrier, potions
w('loc', ['# @s : 📍 localisateur (boussole) vers $(x) $(y) $(z), en case 9', 'clear @s minecraft:compass[minecraft:custom_data~{olloc:1b}]',
          f'$item replace entity @s hotbar.8 with minecraft:compass[custom_data={{olloc:1b}},lodestone_tracker={{target:{{pos:[I;$(x),$(y),$(z)],dimension:"{DIM}"}},tracked:false}},'
          f'custom_name={nm("📍 Localisateur", "light_purple")},lore={lo("Indique ton objectif (faisceau violet)")}]',
          '$scoreboard players set @s mg.olox $(x)', '$scoreboard players set @s mg.oloy $(y)', '$scoreboard players set @s mg.oloz $(z)', 'scoreboard players set @s mg.olon 1'])
w('horse', ['# @s : sifflet : son destrier apparaît et il monte dessus', 'execute if score @s mg.olhorse matches ..0 run return 0',
            'execute if entity @s[tag=mg.olboss_in] run return run tellraw @s {"text":"Pas de destrier pendant un combat de boss.","color":"red"}',
            f'function mg:{P}/horse_gone', 'tag @e[tag=mg.ollast] remove mg.ollast',
            'summon minecraft:horse ~ ~ ~ {Tags:["mg.ol","mg.olmount","mg.ollast"],Tame:1b,PersistenceRequired:1b,Variant:515,'
            'equipment:{saddle:{id:"minecraft:saddle",count:1},body:{id:"minecraft:iron_horse_armor",count:1}},'
            'attributes:[{id:"minecraft:movement_speed",base:0.33},{id:"minecraft:jump_strength",base:0.9},{id:"minecraft:max_health",base:40},{id:"minecraft:step_height",base:1.2}]}',
            'data modify entity @e[tag=mg.ollast,limit=1] Owner set from entity @s UUID', 'scoreboard players operation @e[tag=mg.ollast] mg.olo = @s mg.olpid',
            'ride @s mount @e[tag=mg.ollast,limit=1]', 'execute at @s run playsound minecraft:entity.horse.gallop player @a ~ ~ ~ 1 1'])
w('horse_gone', ['scoreboard players operation $own mg.st = @s mg.olpid', 'execute as @e[tag=mg.olmount] if score @s mg.olo = $own mg.st run kill @s'])
w('mana_pot', ['# @s a bu une potion de mana', 'scoreboard players set @s mg.olhb 0', 'clear @s minecraft:glass_bottle 1', 'scoreboard players add @s mg.olmp 60',
               'execute if score @s mg.olmp > @s mg.olmm run scoreboard players operation @s mg.olmp = @s mg.olmm', f'function mg:{P}/mana_bar',
               'execute at @s run particle minecraft:glow ~ ~1 ~ 0.4 0.6 0.4 0 20'])

# ================================================================ mort, barre d'action
w('died', ['# @s est tombé (inventaire gardé) : -10 % d\'or, réapparition à la dernière pierre d\'appel', 'scoreboard players set @s mg.deaths 0',
           'scoreboard players operation $l mg.st = @s mg.olg', 'scoreboard players operation $l mg.st /= #10 mg.st', 'scoreboard players operation @s mg.olg -= $l mg.st',
           'scoreboard players operation @s mg.olmp = @s mg.olmm', f'function mg:{P}/mana_bar', 'title @s times 5 40 15',
           'title @s title {"text":"☠ TU ES TOMBÉ","color":"dark_red","bold":true}',
           'title @s subtitle [{"text":"Le temple a pris ","color":"gray"},{"score":{"name":"$l","objective":"mg.st"},"color":"gold"},{"text":" 💰 pour te ranimer","color":"gray"}]'])
CRED = ('{"text":"⭐","color":"gold"},{"score":{"name":"@s","objective":"mg.ollv"},"color":"gold","bold":true},{"text":"  💰","color":"gold"},'
        '{"score":{"name":"@s","objective":"mg.olg"},"color":"yellow"},{"text":"  ✦","color":"aqua"},{"score":{"name":"@s","objective":"mg.olmp"},"color":"aqua"},'
        '{"text":"/","color":"dark_aqua"},{"score":{"name":"@s","objective":"mg.olmm"},"color":"dark_aqua"},{"text":"   ","color":"gray"}')
DST = ',{"text":"  📍 ","color":"light_purple"},{"score":{"name":"@s","objective":"mg.olod"},"color":"yellow","bold":true},{"text":" m","color":"light_purple"}'
HUD = ['# @s : barre d\'action (niveau, or, mana, objectif)']
for i, s_ in enumerate(Q.STEPS):
    obj = s_['obj'] if len(s_['obj']) < 60 else s_['obj'][:57] + '…'
    d = DST if s_.get('at') else ''
    if s_['kind'] == 'kill':
        HUD.append(f'execute if score @s mg.olch matches {i} run return run title @s actionbar [{CRED},{js(TEXT("📜 " + obj + " ", "yellow"))},'
                   f'{{"score":{{"name":"@s","objective":"mg.olqp"}},"color":"white","bold":true}},{{"text":"/{s_["n"]}","color":"white"}}]')
    else:
        HUD.append(f'execute if score @s mg.olch matches {i} run return run title @s actionbar [{CRED},{js(TEXT("📜 " + obj, "yellow"))}{d}]')
w('hud', HUD)

# ================================================================ boucles
w('tick', ['# 🌙 Ombrelune : chaque tick tant qu\'un joueur y est (contexte : dimension)', 'scoreboard players add $olt mg.st 1',
           'scoreboard players operation $olq mg.st = $olt mg.st', 'scoreboard players operation $olq mg.st %= #20 mg.st',
           'scoreboard players operation $olq2 mg.st = $olt mg.st', 'scoreboard players operation $olq2 mg.st %= #2 mg.st',
           'scoreboard players operation $olq4 mg.st = $olt mg.st', 'scoreboard players operation $olq4 mg.st %= #4 mg.st',
           'scoreboard players operation $olq5 mg.st = $olt mg.st', 'scoreboard players operation $olq5 mg.st %= #5 mg.st',
           'scoreboard players operation $olq60 mg.st = $olt mg.st', 'scoreboard players operation $olq60 mg.st %= #60 mg.st',
           'scoreboard players operation $olq100 mg.st = $olt mg.st', 'scoreboard players operation $olq100 mg.st %= #100 mg.st',
           'scoreboard players set #8 mg.st 8',
           '# objets, potions, choix, interactions',
           f'execute as @a[tag=mg.olw,scores={{mg.olq=1..}}] at @s run function mg:{P}/use', 'scoreboard players reset @a[scores={mg.olq=1..}] mg.olq',
           f'execute as @a[tag=mg.olw,scores={{mg.olhb=1..}}] run function mg:{P}/mana_pot',
           f'execute as @a[tag=mg.olw,scores={{mg.oltk=1..}}] run function mg:{P}/tk',
           f'execute as @a[tag=mg.olw,scores={{mg.oldt=1..}}] run function mg:{P}/m/hurt',
           f'execute as @e[type=minecraft:interaction,tag=mg.olnpc] if data entity @s interaction run function mg:{P}/npc/int',
           f'execute as @e[type=minecraft:interaction,tag=mg.olway] if data entity @s interaction run function mg:{P}/way_int',
           f'execute as @e[type=minecraft:interaction,tag=mg.olint] if data entity @s interaction run function mg:{P}/q/int',
           f'execute as @e[type=minecraft:interaction,tag=mg.olint] if data entity @s attack run function mg:{P}/q/int',
           f'execute as @e[type=minecraft:interaction,tag=mg.oljar] if data entity @s interaction run function mg:{P}/boss/jar_int',
           f'execute as @e[type=minecraft:interaction,tag=mg.oljar] if data entity @s attack run function mg:{P}/boss/jar_int',
           f'execute as @e[type=minecraft:interaction,tag=mg.olpill] if data entity @s interaction run function mg:{P}/boss/pill_int',
           'execute as @e[type=minecraft:item_display,tag=mg.olspin] at @s run tp @s ~ ~ ~ ~4 ~',
           '# créatures articulées : chaque tick près d\'un joueur, sinon 2 fois par seconde',
           f'execute as @e[tag=mg.olbd] at @s if entity @a[tag=mg.olw,distance=..48] run function mg:{P}/bsync',
           f'execute if score $olq mg.st matches 0 as @e[tag=mg.olbd] at @s unless entity @a[tag=mg.olw,distance=..48] run function mg:{P}/bsync',
           f'execute if score $olq mg.st matches 10 as @e[tag=mg.olbd] at @s unless entity @a[tag=mg.olw,distance=..48] run function mg:{P}/bsync',
           f'function mg:{P}/cl/tick', f'function mg:{P}/m/web_tick',
           f'execute if score $olq5 mg.st matches 0 run function mg:{P}/q/coltick', f'execute if score $olq5 mg.st matches 0 run function mg:{P}/pg_tick',
           f'execute if score $olq5 mg.st matches 0 run function mg:{P}/tc_tick',
           f'execute if score $olq5 mg.st matches 0 as @a[tag=mg.olw,scores={{mg.olpk=1..}}] unless predicate mg:sneak run scoreboard players set @s mg.olpk 0',
           f'execute as @a[tag=mg.olcine] run function mg:{P}/cs/run',
           f'execute if score $olq mg.st matches 0 as @a[tag=mg.olw,tag=!mg.olcine,scores={{mg.olon=1}}] at @s run function mg:{P}/ind',
           f'execute if score $olq mg.st matches 10 as @a[tag=mg.olw,tag=!mg.olcine,scores={{mg.olon=1}}] at @s run function mg:{P}/ind',
           f'execute as @a[tag=mg.olw,scores={{mg.deaths=1..}}] run function mg:{P}/died',
           'scoreboard players remove @a[tag=mg.olw,scores={mg.olal=1..}] mg.olal 1',
           f'execute if score $olq mg.st matches 0 run function mg:{P}/second',
           f'execute if score $olq mg.st matches 5 as @a[tag=mg.olw,tag=!mg.olcine,scores={{mg.olal=..0}}] run function mg:{P}/hud',
           f'execute if score $olq mg.st matches 15 as @a[tag=mg.olw,tag=!mg.olcine,scores={{mg.olal=..0}}] run function mg:{P}/hud'])
w('second', ['# Chaque seconde (dimension) : régions, lieux, quêtes, monstres, classes, boss, donjons',
             'execute unless score $olsu mg.st matches 1.. run return 0',
             'effect give @a[tag=mg.olw] minecraft:saturation infinite 0 true', 'scoreboard players enable @a[tag=mg.olw] mg.oltk',
             f'execute as @a[tag=mg.olw,tag=!mg.olcine] at @s run function mg:{P}/region',
             f'execute as @a[tag=mg.olw,tag=!mg.olcine] at @s run function mg:{P}/q/gotick',
             f'function mg:{P}/ws_tick',
             f'execute as @a[tag=mg.olw,tag=!mg.olintro,tag=!mg.olcine,scores={{mg.olch=0}}] run function mg:{P}/intro_go',
             f'execute if score $olq60 mg.st matches 0 run function mg:{P}/pois', f'execute if score $olq60 mg.st matches 40 run function mg:{P}/pois',
             f'execute if score $olq60 mg.st matches 20 as @a[tag=mg.olw,tag=!mg.olcine] at @s run function mg:{P}/hazard',
             f'execute if score $olq60 mg.st matches 40 as @a[tag=mg.olw,tag=!mg.olcine] at @s run function mg:{P}/hazard',
             f'execute if score $olq100 mg.st matches 0 as @a[tag=mg.olw] run function mg:{P}/achievements',
             f'function mg:{P}/m/second', f'function mg:{P}/cl/second', f'function mg:{P}/bosses', f'function mg:{P}/bclean',
             '# entités d\'une session précédente restées dans une zone non chargée : retirées',
             'execute as @e[tag=mg.olm] unless score @s mg.olses = $olses mg.st run kill @s'])
w('intro_go', ['# @s arrive pour la première fois : cinématique d\'introduction', 'tag @s add mg.olintro', f'function mg:{P}/cs/intro'])

# ================================================================ câblage dans le datapack
C.patch('core/tick', 'function mg:terra/lobby_tick', ['function mg:ombre/lobby_tick'])
C.patch('core/tick', 'function mg:terra/pre_tick', ['function mg:ombre/pre_tick'])
C.patch('survie/leave', 'execute if entity @s[tag=mg.tvw] run return run function mg:terra/leave',
        ['execute if entity @s[tag=mg.olw] run return run function mg:ombre/leave'])
C.patch('survie/cmd', 'execute if score @s mg.sv matches 7 run function mg:terra/menu_go', ['execute if score @s mg.sv matches 8 run function mg:ombre/menu_go'])
_cmd = C.lines_of('survie/cmd')
if _cmd and '7 = Terra Nova,' in _cmd[0] and 'Ombrelune' not in _cmd[0]:
    _cmd[0] = _cmd[0].replace('7 = Terra Nova,', '7 = Terra Nova, 8 = Ombrelune,')
    C.w('survie/cmd', _cmd[:-1] if _cmd[-1] == '' else _cmd)
_pa = C.lines_of('core/pull_all')
_pa = [l.replace('tag @a[tag=mg.surv,tag=!mg.gtw,tag=!mg.tvw] add mg.pulls', 'tag @a[tag=mg.surv,tag=!mg.gtw,tag=!mg.tvw,tag=!mg.olw] add mg.pulls') for l in _pa]
if 'tag @a[tag=mg.olw] add mg.pullo' not in _pa:
    i = _pa.index('tag @a[tag=mg.tvw] add mg.pullt')
    _pa[i + 1:i + 1] = ['tag @a[tag=mg.olw] add mg.pullo']
    j = _pa.index('execute as @a[tag=mg.pullt] in minecraft:overworld run function mg:terra/leave')
    _pa[j + 1:j + 1] = ['execute as @a[tag=mg.pullo] in minecraft:overworld run function mg:ombre/leave']
C.w('core/pull_all', _pa[:-1] if _pa[-1] == '' else _pa)
C.patch('core/optout', 'execute if entity @s[tag=mg.pullt] in minecraft:overworld run function mg:terra/enter',
        ['execute if entity @s[tag=mg.pullo] in minecraft:overworld run function mg:ombre/enter'])
C.patch('core/optout', 'tag @s remove mg.pullt', ['tag @s remove mg.pullo'])
C.patch('core/request', 'tag @a remove mg.pullt', ['tag @a remove mg.pullo'])
_st = C.lines_of('survie/tick')
_st = [l.replace('tag=!mg.gtw,tag=!mg.tvw,tag=!mg.svg2,', 'tag=!mg.gtw,tag=!mg.tvw,tag=!mg.olw,tag=!mg.svg2,') for l in _st]
C.w('survie/tick', _st[:-1] if _st[-1] == '' else _st)
C.patch('desinstaller', 'execute as @a[tag=mg.tvw] in minecraft:overworld run function mg:terra/leave',
        ['execute as @a[tag=mg.olw] in minecraft:overworld run function mg:ombre/leave'])
C.patch('core/load', 'execute if score $setup mg.st matches 1 unless data storage mg:terra built run schedule function mg:terra/world_build 200s',
        ['# Ombrelune : construite une fois (dimension mg:ombrelune, ~4 min, après Terra Nova), règles du monde',
         'execute if score $setup mg.st matches 1 unless data storage mg:ombre built unless score $olb mg.st matches 1.. run schedule function mg:ombre/world_build 260s',
         'execute if score $setup mg.st matches 1 unless data storage mg:lobby olclean run schedule function mg:ombre/spawn_clean 10s',
         'execute if score $setup mg.st matches 1 run schedule function mg:ombre/st/check 30s',
         'scoreboard players set $olw mg.st 0', 'function mg:ombre/rules'])
OBJ_DUMMY = sorted({o for o, _ in JOIN_DEF} | {'mg.ollv', 'mg.olpid', 'mg.olmp', 'mg.olmm', 'mg.olal', 'mg.olrg', 'mg.olsx', 'mg.olsy', 'mg.olsz', 'mg.olpk',
                                               'mg.olcs', 'mg.olctk', 'mg.olcf', 'mg.olox', 'mg.oloy', 'mg.oloz', 'mg.olon', 'mg.olod', 'mg.olid', 'mg.olab',
                                               'mg.olak', 'mg.olaf', 'mg.olat', 'mg.olses', 'mg.olo', 'mg.olst', 'mg.olpw', 'mg.olnid', 'mg.olmk'} |
                    {f'mg.olc{i}' for i in range(5)})
C.objectives([(o, 'dummy') for o in OBJ_DUMMY] + [('mg.olq', 'minecraft.used:minecraft.warped_fungus_on_a_stick'), ('mg.oldt', 'minecraft.custom:minecraft.damage_taken'),
                                                  ('mg.oltk', 'trigger'), ('mg.olhb', 'minecraft.used:minecraft.honey_bottle')])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw',
        ['schedule clear mg:ombre/wb_step', 'schedule clear mg:ombre/world_build', 'schedule clear mg:ombre/session_setup', 'schedule clear mg:ombre/spawn_clean',
         'schedule clear mg:ombre/st/step', 'schedule clear mg:ombre/st/check', 'schedule clear mg:ombre/boss/wake', f'execute in {DIM} run forceload remove all', 'kill @e[tag=mg.olport]',
         f'execute in {DIM} run kill @e[tag=mg.ol]', 'team remove mg_ol', 'team remove mg_olel', 'function mg:ombre/boss/clear',
         'data remove storage mg:ombre built', 'data remove storage mg:ombre sv', 'data remove storage mg:lobby olclean'])
# menu Échap : bouton « Aller à Ombrelune » (après Terra Nova)
_mp = os.path.join(C.D, 'dialog', 'main_menu.json')
_m = json.load(open(_mp, encoding='utf-8'))
if not any(a['action'].get('command') == 'trigger mg.sv set 8' for a in _m['actions']):
    i = next(i for i, a in enumerate(_m['actions']) if a['action'].get('command') == 'trigger mg.sv set 7')
    _m['actions'].insert(i + 1, {'label': [{'text': '🌙 Aller à Ombrelune', 'color': 'light_purple', 'bold': True}],
                                 'tooltip': [{'text': 'RPG médiéval-fantastique : 8 régions, dragons, donjons (ta progression y est gardée)', 'color': 'gray'}],
                                 'action': {'type': 'minecraft:run_command', 'command': 'trigger mg.sv set 8'}})
    with open(_mp, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(_m, f, ensure_ascii=False, indent=2)
        f.write('\n')

# ================================================================ contrôle : objectifs utilisés mais jamais créés
used = set()
for root, _, files in os.walk(os.path.join(C.F, P)):
    for fn_ in files:
        t = open(os.path.join(root, fn_), encoding='utf-8').read()
        used |= set(re.findall(r'(?:scores=\{|players (?:set|add|remove|reset|operation|get|enable) \S+ |score \S+ |"objective":")(mg\.ol\w+)', t))
        used |= set(re.findall(r'operation \S+ \S+ [-+*/%<>=]+ \S+ (mg\.ol\w+)', t))
missing = sorted(used - set(OBJ_DUMMY) - {'mg.olq', 'mg.oldt', 'mg.oltk', 'mg.olhb'})
if missing:
    print('⚠ objectifs non créés :', missing)
em = [os.path.join(r_, f_) for r_, _, fs in os.walk(os.path.join(C.F, P)) for f_ in fs if chr(0x2014) in open(os.path.join(r_, f_), encoding='utf-8').read()]
if em:
    print('⚠ tiret cadratin dans :', em[:5])
print(f'Ombrelune OK : {NS} commandes de construction ({NP} paquets), {len(M.KINDS)} espèces, {len(Q.STEPS)} étapes de campagne, '
      f'{len(Q.NPCS)} PNJ, {len(Q.SIDE)} quêtes secondaires, {len(BO.BOSSES)} boss, {len(S.DUNGEONS)} donjons')
