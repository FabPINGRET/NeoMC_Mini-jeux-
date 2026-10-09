"""🎾 Tennis façon Wii Sports (id 216) : 1 contre 1, chacun son court, 4 courts côte à côte (centre 0 65 35400).

    python tools/arcade/gen_tennis.py .

- 4 courts de 40 blocs de large (x −80..79, z 35375..35425) : surface terre battue ou dur, lignes blanches, filet
  (barreaux + bande blanche, poteaux à fanions, mur de barrières invisible au-dessus : on ne passe pas chez l'autre),
  gradins, chaise d'arbitre, tableau d'affichage (text_display) au-dessus du filet.
- Joueurs appariés au hasard (court 1, 2, …) : côté 1 = BLEU (nord, joue vers +z), côté 2 = ROUGE (sud, joue vers −z).
  Joueur impair : un robot (mannequin) côté rouge. Au-delà de 8 joueurs : spectateurs.
- Raquette = warped_fungus_on_a_stick custom_data {mg_racket:1b} : le clic droit incrémente mg.qs (comme les armes
  de gun/ et bomber/, qui ne tournent pas pendant le tennis ; core/request remet mg.qs à zéro).
- Balle = item_display (étoile de feu d'artifice jaune-vert) déplacée par scores (coordonnées relatives au court ×1000,
  vitesse 3D, gravité G, rebond amorti). Une frappe vise un point d'impact (Lx, Lz) atteint en T ticks :
  v = (L − pos) / T, vy = (sol − y) / T + G·T/2 → la trajectoire passe le filet si la balle est frappée assez haut.
- Score : jeux à 4 points (0/15/30/40/AV, 2 d'écart), match en 1 set de GAMES jeux gagnants.
"""
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js

# ---------------------------------------------------------------- réglages
GID = 216
CZ = 35400                      # ligne du filet (bloc), origine z relative = CZ + 0.5
GY = 64                         # surface du court ; joueurs à y 65
NCOURT = 4
POINTS = C.param('points', 4)   # points pour un jeu (2 d'écart)
GAMES = C.param('games', 3)     # jeux pour gagner le match
LIMIT = C.param('limit', 9600)  # sécurité : 8 min
SURF = C.param('surfaces', ['clay', 'hard', 'clay', 'hard'])
G = 16                          # gravité (millièmes de bloc / tick²)
REACH = 2.5                     # portée de la raquette (depuis la poitrine)
ROBOT_REACH = 2.3
ROBOT_SPEED = 200               # millièmes de bloc / tick par axe
ROBOT_MISS = 10                 # % de balles ratées exprès par le robot
TOSS_VY = 230                   # lancer de balle au service
HW, HL = 5500, 12500            # limites du simple (demi-largeur, demi-longueur), lignes comprises
GROUND = 65100                  # centre de la balle au sol
NET_TOP = 66100
SHOTS = {                       # (T ticks, profondeur d'impact) selon le timing
    'fort': (26, 10500), 'normal': (32, 8500), 'tard': (38, 6000), 'lob': (50, 10500), 'service': (30, 8500)}

def cx(k):                      # x du bloc central du court k (1..4)
    return -60 + 40 * (k - 1)

ZO = CZ * 1000 + 500            # origine z (×1000)
BALL_ITEM = ('{id:"minecraft:firework_star",count:1,components:{"minecraft:firework_explosion":'
             '{shape:"small_ball",colors:[I;13434675]}}}')
PRED_SNEAK = '{condition:"minecraft:entity_properties",entity:"this",predicate:{flags:{is_sneaking:true}}}'
BALL = '@e[type=minecraft:item_display,tag=mg.tnball,tag=mg.tnk,limit=1]'
BALLS = '@e[type=minecraft:item_display,tag=mg.tnball,tag=mg.tnk]'
MARK = '@e[type=minecraft:marker,tag=mg.tncm,tag=mg.tnk,limit=1]'
ROB = '@e[type=minecraft:mannequin,tag=mg.tnrob,tag=mg.tnk]'
DIR = '@e[type=minecraft:marker,tag=mg.tndir,limit=1]'
NEAR = '@a[tag=!mg.surv,distance=..40]'
SIDE_TXT = {1: {'text': 'BLEU', 'color': 'aqua', 'bold': True}, 2: {'text': 'ROUGE', 'color': 'red', 'bold': True}}

# ---------------------------------------------------------------- construction
B = [f'# 🎾 Tennis — {NCOURT} courts (x −80..79, z {CZ - 25}..{CZ + 25}), surface y {GY}']
for k in range(1, NCOURT + 1):
    X = cx(k)
    x1, x2 = X - 20, X + 19
    B += [f'fill {x1} 65 {CZ - 25} {x2} 75 {CZ + 25} minecraft:air', f'fill {x1} 76 {CZ - 25} {x2} 86 {CZ + 25} minecraft:air',
          f'fill {x1} {GY - 1} {CZ - 25} {x2} {GY - 1} {CZ + 25} minecraft:dirt',
          f'fill {x1} {GY} {CZ - 25} {x2} {GY} {CZ + 25} minecraft:grass_block']
for k in range(1, NCOURT + 1):
    X = cx(k)
    clay = SURF[(k - 1) % len(SURF)] == 'clay'
    out_c, in_c = ('terracotta', 'terracotta') if clay else ('green_concrete', 'blue_concrete')
    B.append(f'# Court {k} ({"terre battue" if clay else "dur"})')
    B += [f'fill {X - 10} {GY} {CZ - 18} {X + 10} {GY} {CZ + 18} minecraft:{out_c}',
          f'fill {X - 5} {GY} {CZ - 12} {X + 5} {GY} {CZ + 12} minecraft:{in_c}',
          # lignes : fonds de court, couloirs, lignes de service, ligne médiane, marques centrales
          f'fill {X - 5} {GY} {CZ - 12} {X + 5} {GY} {CZ - 12} minecraft:white_concrete',
          f'fill {X - 5} {GY} {CZ + 12} {X + 5} {GY} {CZ + 12} minecraft:white_concrete',
          f'fill {X - 5} {GY} {CZ - 12} {X - 5} {GY} {CZ + 12} minecraft:white_concrete',
          f'fill {X + 5} {GY} {CZ - 12} {X + 5} {GY} {CZ + 12} minecraft:white_concrete',
          f'fill {X - 5} {GY} {CZ - 7} {X + 5} {GY} {CZ - 7} minecraft:white_concrete',
          f'fill {X - 5} {GY} {CZ + 7} {X + 5} {GY} {CZ + 7} minecraft:white_concrete',
          f'fill {X} {GY} {CZ - 7} {X} {GY} {CZ + 7} minecraft:white_concrete',
          f'setblock {X} {GY} {CZ - 11} minecraft:white_concrete', f'setblock {X} {GY} {CZ + 11} minecraft:white_concrete',
          # murs de fond (bâches vertes)
          f'fill {X - 10} 65 {CZ - 22} {X + 10} 67 {CZ - 22} minecraft:green_concrete' if not clay else
          f'fill {X - 10} 65 {CZ - 22} {X + 10} 67 {CZ - 22} minecraft:green_terracotta',
          f'fill {X - 10} 65 {CZ + 22} {X + 10} 67 {CZ + 22} minecraft:green_concrete' if not clay else
          f'fill {X - 10} 65 {CZ + 22} {X + 10} 67 {CZ + 22} minecraft:green_terracotta',
          # mur invisible dans l'axe du filet (sur toute la largeur de l'emplacement)
          f'fill {X - 19} 65 {CZ} {X + 18} 75 {CZ} minecraft:barrier',
          # filet : barreaux + bande blanche, poteaux à fanions
          f'fill {X - 6} 65 {CZ} {X + 6} 65 {CZ} minecraft:iron_bars',
          f'fill {X - 6} 66 {CZ} {X + 6} 66 {CZ} minecraft:white_carpet',
          f'fill {X - 7} 65 {CZ} {X - 7} 66 {CZ} minecraft:dark_oak_fence', f'fill {X + 7} 65 {CZ} {X + 7} 66 {CZ} minecraft:dark_oak_fence',
          f'setblock {X - 7} 67 {CZ} minecraft:blue_banner[rotation=4]', f'setblock {X + 7} 67 {CZ} minecraft:red_banner[rotation=12]',
          # chaise d'arbitre
          f'fill {X - 9} 65 {CZ} {X - 9} 66 {CZ} minecraft:dark_oak_planks', f'setblock {X - 9} 67 {CZ} minecraft:dark_oak_stairs[facing=west]',
          f'fill {X - 10} 65 {CZ} {X - 10} 66 {CZ} minecraft:ladder[facing=west]',
          f'setblock {X - 9} 68 {CZ} minecraft:air']
    # gradins (5 rangées face au court) + mur du fond
    for i in range(5):
        x = X + 13 + i
        if i:
            B.append(f'fill {x} 65 {CZ - 14} {x} {64 + i} {CZ + 14} minecraft:{"light_gray_concrete" if i % 2 else "white_concrete"}')
        B.append(f'fill {x} {65 + i} {CZ - 14} {x} {65 + i} {CZ + 14} minecraft:spruce_stairs[facing=east]')
    B += [f'fill {X + 18} 65 {CZ - 14} {X + 18} 70 {CZ + 14} minecraft:{"orange_concrete" if clay else "blue_concrete"}',
          f'fill {X + 13} 70 {CZ - 14} {X + 17} 70 {CZ - 14} minecraft:white_concrete',
          f'fill {X + 13} 70 {CZ + 14} {X + 17} 70 {CZ + 14} minecraft:white_concrete']
    # éclairage invisible
    B += [f'setblock {X + dx} 70 {CZ + dz} minecraft:light[level=15]' for dx in (-8, 0, 8) for dz in (-15, -7, 7, 15)]
# murs invisibles : fond, côtés, séparations entre courts
B += [f'fill -80 65 {CZ - 25} 79 80 {CZ - 25} minecraft:barrier', f'fill -80 65 {CZ + 25} 79 80 {CZ + 25} minecraft:barrier',
      f'fill -80 65 {CZ - 24} -80 80 {CZ + 24} minecraft:barrier']
B += [f'fill {cx(k) + 19} 65 {CZ - 24} {cx(k) + 19} 80 {CZ + 24} minecraft:barrier' for k in range(1, NCOURT + 1)]
w('tennis/build', B)

# ---------------------------------------------------------------- préparation
P = ['# 🎾 Tennis — préparation : courts remis à neuf, appariement au hasard, robot si joueur impair',
     'function mg:tennis/build', 'kill @e[tag=mg.tent]',
     f'kill @e[type=minecraft:item,x=-80,y=60,z={CZ - 25},dx=160,dy=30,dz=51]',
     'scoreboard players set $px mg.st 0', 'scoreboard players set $py mg.st 78', f'scoreboard players set $pz mg.st {CZ - 20}',
     'tag @a remove mg.tnk', 'tag @a remove mg.tnwin', 'tag @a remove mg.tnsrv',
     'scoreboard players reset * mg.tnc', 'scoreboard players reset * mg.tns', 'scoreboard players reset * mg.tngw',
     'scoreboard players reset @a mg.tnt',
     'gamemode adventure @a[tag=mg.play]', 'clear @a[tag=mg.play]',
     # constantes
     'scoreboard players set #tnm1 mg.st -1', 'scoreboard players set #tnm7 mg.st -7', 'scoreboard players set #tn2 mg.st 2',
     'scoreboard players set #tn3 mg.st 3', 'scoreboard players set #tn4 mg.st 4', 'scoreboard players set #tn10 mg.st 10',
     'scoreboard players set #tn40000 mg.st 40000', f'scoreboard players set #tng mg.st {G}',
     # appariement
     'scoreboard players set $tni mg.st 0', 'execute as @a[tag=mg.play,sort=random] run function mg:tennis/assign',
     'scoreboard players operation $tncourts mg.st = $tni mg.st', 'scoreboard players add $tncourts mg.st 1',
     'scoreboard players operation $tncourts mg.st /= #tn2 mg.st',
     'execute if score $tncourts mg.st matches 0 run scoreboard players set $tncourts mg.st 1',
     f'summon minecraft:marker 0 64 {CZ} {{Tags:["mg.tent","mg.npc","mg.tndir"]}}']
for k in range(1, NCOURT + 1):
    X = cx(k)
    P += [f'execute if score $tncourts mg.st matches {k}.. run summon minecraft:marker {X}.5 65 {CZ}.5 '
          f'{{Tags:["mg.tent","mg.npc","mg.tncm","mg.tnnew"],data:{{k:{k},a:"0",b:"0",ga:0,gb:0}}}}',
          f'execute if score $tncourts mg.st matches {k}.. run summon minecraft:text_display {X}.5 71.5 {CZ}.5 '
          '{Tags:["mg.tent","mg.npc","mg.tntd","mg.tnnew"],billboard:"center",background:1711276032,line_width:220,'
          'alignment:"center",transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],'
          f'scale:[1.6f,1.6f,1.6f]}},text:{{"text":"🎾 Court {k}","color":"gold","bold":true}}}}',
          f'scoreboard players set @e[tag=mg.tnnew] mg.tnc {k}', 'tag @e[tag=mg.tnnew] remove mg.tnnew']
# robot : joueur impair → côté rouge du dernier court
P += ['scoreboard players operation $tnq mg.st = $tni mg.st', 'scoreboard players operation $tnq mg.st %= #tn2 mg.st',
      ]
for k in range(1, NCOURT + 1):
    P.append(f'execute if score $tnq mg.st matches 1 if score $tncourts mg.st matches {k} run summon minecraft:mannequin {cx(k)}.5 65 {CZ + 14}.5 '
             '{Tags:["mg.tent","mg.npc","mg.tnrob","mg.tnnew"],NoGravity:1b,Invulnerable:1b,Silent:1b,PersistenceRequired:1b,'
             'CustomName:{"text":"🤖 Robot","color":"gold"},CustomNameVisible:1b,description:{"text":"Robot de tennis","color":"gray"},'
             'equipment:{mainhand:{id:"minecraft:warped_fungus_on_a_stick",count:1},'
             'chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":16733525}}}}')
P += ['execute as @e[type=minecraft:mannequin,tag=mg.tnnew] run scoreboard players operation @s mg.tnc = $tncourts mg.st',
      'scoreboard players set @e[type=minecraft:mannequin,tag=mg.tnnew] mg.tns 2', 'scoreboard players set @e[type=minecraft:mannequin,tag=mg.tnnew] mg.tnt 0',
      'tag @e[tag=mg.tnnew] remove mg.tnnew',
      'execute as @a[tag=mg.play] run function mg:tennis/kit',
      'scoreboard players set $tntm mg.st 0',
      'execute as @e[type=minecraft:marker,tag=mg.tncm] run function mg:tennis/court_init']
w('tennis/prepare', P)

w('tennis/assign', ['# @s : joueur suivant (ordre aléatoire) → court $tni/2 + 1, côté $tni%2 + 1 ; au-delà de 8 : spectateur',
                    f'execute if score $tni mg.st matches {2 * NCOURT}.. run tellraw @s {{"text":"🎾 Tous les courts sont pris : tu regardes ce tournoi.","color":"gray"}}',
                    f'execute if score $tni mg.st matches {2 * NCOURT}.. run return run function mg:core/eliminate',
                    'scoreboard players operation @s mg.tnc = $tni mg.st', 'scoreboard players operation @s mg.tnc /= #tn2 mg.st',
                    'scoreboard players add @s mg.tnc 1',
                    'scoreboard players operation @s mg.tns = $tni mg.st', 'scoreboard players operation @s mg.tns %= #tn2 mg.st',
                    'scoreboard players add @s mg.tns 1', 'scoreboard players add $tni mg.st 1'])

w('tennis/kit', ['# @s : raquette + tenue de son camp',
                 'give @s minecraft:warped_fungus_on_a_stick[minecraft:custom_data={mg_racket:1b},minecraft:unbreakable={},'
                 'minecraft:custom_name={"text":"🎾 Raquette","color":"yellow","italic":false},'
                 'minecraft:lore=[{"text":"Clic droit près de la balle : renvoyer","color":"gray","italic":false},'
                 '{"text":"Accroupi : lob — clic droit au service : lancer","color":"gray","italic":false}]]',
                 'execute if score @s mg.tns matches 1 run item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=3381759,unbreakable={}]',
                 'execute if score @s mg.tns matches 2 run item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=16733525,unbreakable={}]',
                 'effect give @s minecraft:saturation infinite 0 true', 'scoreboard players set @s mg.tnt 0'])

w('tennis/court_init', ['# @s : marqueur d\'un court — score à zéro, premier serveur au hasard',
                        'scoreboard players operation $tnk mg.st = @s mg.tnc', 'function mg:tennis/tagk',
                        'scoreboard players set @s mg.tnp1 0', 'scoreboard players set @s mg.tnp2 0',
                        'scoreboard players set @s mg.tng1 0', 'scoreboard players set @s mg.tng2 0',
                        'execute store result score @s mg.tnl run random value 1..2',
                        'function mg:tennis/labels', 'function mg:tennis/point_setup'])

w('tennis/tagk', ['# Court $tnk : tag mg.tnk sur ses entités et ses joueurs, $tncx = x de son centre (×1000)',
                  'tag @e[tag=mg.tnk] remove mg.tnk',
                  'execute as @e[tag=mg.tent] if score @s mg.tnc = $tnk mg.st run tag @s add mg.tnk',
                  'execute as @a[tag=mg.play] if score @s mg.tnc = $tnk mg.st run tag @s add mg.tnk',
                  'scoreboard players operation $tncx mg.st = $tnk mg.st', 'scoreboard players operation $tncx mg.st *= #tn40000 mg.st',
                  'scoreboard players remove $tncx mg.st 99500'])

PL = ['# Placement pour le point (court $tnk, $tnpar = parité des points) : en diagonale, derrière la ligne de fond']
for k in range(1, NCOURT + 1):
    X = cx(k)
    for par, o in ((0, 1.5), (1, -1.5)):
        PL += [f'execute if score $tnk mg.st matches {k} if score $tnpar mg.st matches {par} as @e[tag=mg.tnk,scores={{mg.tns=1}}] run tp @s {X + 0.5 + o} 65 {CZ - 13.5} 0 0',
               f'execute if score $tnk mg.st matches {k} if score $tnpar mg.st matches {par} as @e[tag=mg.tnk,scores={{mg.tns=2}}] run tp @s {X + 0.5 - o} 65 {CZ + 14.5} 180 0']
w('tennis/place', PL)

w('tennis/point_setup', ['# @s : marqueur — nouveau point (balle retirée, joueurs replacés, service au serveur mg.tnl)',
                         f'kill {BALLS}', 'scoreboard players set @s mg.tnph 0', 'scoreboard players set @s mg.tnt 0',
                         'tag @e[tag=mg.tnk] remove mg.tnsrv',
                         'scoreboard players operation $tnside mg.st = @s mg.tnl',
                         'execute as @e[tag=mg.tnk] if score @s mg.tns = $tnside mg.st run tag @s add mg.tnsrv',
                         f'tag {ROB} remove mg.tnchase', f'tag {ROB} remove mg.tnmiss',
                         'scoreboard players operation $tnpar mg.st = @s mg.tnp1', 'scoreboard players operation $tnpar mg.st += @s mg.tnp2',
                         'scoreboard players operation $tnpar mg.st %= #tn2 mg.st',
                         'function mg:tennis/place'])

# ---------------------------------------------------------------- départ / tick
w('tennis/go', ['# Départ', 'scoreboard players reset @a mg.qs', 'scoreboard players set $tntm mg.st 0',
                'scoreboard players set @a[tag=mg.play] mg.tngw 0',
                f'execute if entity @e[type=minecraft:mannequin,tag=mg.tnrob] run scoreboard players set Robot mg.tngw 0',
                'scoreboard objectives setdisplay sidebar mg.tngw',
                'tellraw @a[tag=mg.play] ' + js([
                    {'text': '🎾 TENNIS : ', 'color': 'yellow', 'bold': True},
                    {'text': 'clic droit avec la raquette quand la balle est à portée pour la renvoyer, dans la direction de ton regard. '
                             'Frappe tôt (balle encore loin) = coup fort et long ; accroupi = lob. Au service : clic droit pour lancer la balle. '
                             f'La balle doit passer le filet et rebondir une fois dans le camp adverse. Jeux en {POINTS} points (2 d\'écart), '
                             f'premier à {GAMES} jeux !', 'color': 'gray'}])] +
  [f'execute if score $tncourts mg.st matches {k}.. run tellraw @a[tag=mg.play] ' + js([
      {'text': f'  Court {k} : ', 'color': 'gold'},
      {'selector': f'@e[scores={{mg.tnc={k},mg.tns=1}},type=!minecraft:marker]', 'color': 'aqua'}, {'text': ' contre ', 'color': 'gray'},
      {'selector': f'@e[scores={{mg.tnc={k},mg.tns=2}},type=!minecraft:marker]', 'color': 'red'}]) for k in range(1, NCOURT + 1)])

w('tennis/tick', ['# 🎾 Tennis — tick', 'scoreboard players add $tntm mg.st 1',
                  'execute as @a[tag=mg.play,scores={mg.qs=1..}] at @s run function mg:tennis/swing',
                  'scoreboard players reset @a[scores={mg.qs=1..}] mg.qs',
                  'scoreboard players remove @a[tag=mg.play,scores={mg.tnt=1..}] mg.tnt 1',
                  'scoreboard players remove @e[type=minecraft:mannequin,tag=mg.tnrob,scores={mg.tnt=1..}] mg.tnt 1',
                  'scoreboard players operation $tnab mg.st = $tntm mg.st', 'scoreboard players operation $tnab mg.st %= #tn10 mg.st',
                  'execute as @e[type=minecraft:marker,tag=mg.tncm] run function mg:tennis/court',
                  f'execute if score $tntm mg.st matches {LIMIT - 1200} run tellraw @a[tag=mg.play] {{"text":"🎾 Plus qu\'une minute : ensuite, le meilleur de chaque court gagne !","color":"yellow"}}',
                  f'execute if score $state mg.st matches 2 if score $tntm mg.st matches {LIMIT}.. run return run function mg:tennis/timeout',
                  'execute if score $state mg.st matches 2 unless entity @e[type=minecraft:marker,tag=mg.tncm,scores={mg.tnph=0..3}] run function mg:tennis/finish'])

LINE = js([{'text': '🟦 ', 'color': 'aqua'}, {'selector': '@e[tag=mg.tnk,scores={mg.tns=1}]', 'color': 'aqua'},
           {'text': '  ', 'color': 'gray'}, {'nbt': 'data.a', 'entity': MARK, 'color': 'white', 'bold': True},
           {'text': ' — ', 'color': 'gray'}, {'nbt': 'data.b', 'entity': MARK, 'color': 'white', 'bold': True},
           {'text': '  ', 'color': 'gray'}, {'selector': '@e[tag=mg.tnk,scores={mg.tns=2}]', 'color': 'red'},
           {'text': ' 🟥', 'color': 'red'}, {'text': '   jeux ', 'color': 'gray'},
           {'nbt': 'data.ga', 'entity': MARK, 'color': 'aqua'}, {'text': '-', 'color': 'gray'}, {'nbt': 'data.gb', 'entity': MARK, 'color': 'red'}])
w('tennis/court', ['# @s : marqueur d\'un court (chaque tick)',
                   'scoreboard players operation $tnk mg.st = @s mg.tnc', 'function mg:tennis/tagk',
                   'execute if score @s mg.tnph matches 4 run return 0',
                   # forfait (joueur parti)
                   'execute store result score $tnn1 mg.st if entity @e[tag=mg.tnk,scores={mg.tns=1}]',
                   'execute store result score $tnn2 mg.st if entity @e[tag=mg.tnk,scores={mg.tns=2}]',
                   'execute if score $tnn1 mg.st matches 0 if score $tnn2 mg.st matches 0 run return run function mg:tennis/court_end',
                   'execute if score $tnn1 mg.st matches 0 run scoreboard players set $tnw mg.st 2',
                   'execute if score $tnn2 mg.st matches 0 run scoreboard players set $tnw mg.st 1',
                   'execute if score $tnn1 mg.st matches 0 run return run function mg:tennis/forfeit',
                   'execute if score $tnn2 mg.st matches 0 run return run function mg:tennis/forfeit',
                   # phases : 0 attente du service, 1 lancer, 2 échange, 3 pause après le point
                   'execute if score @s mg.tnph matches 0 run function mg:tennis/phase0',
                   f'execute if score @s mg.tnph matches 1..3 as {BALLS} run function mg:tennis/ball',
                   f'execute if score @s mg.tnph matches 1..2 unless entity {BALL} run function mg:tennis/point_setup',
                   'execute if score @s mg.tnph matches 3 run function mg:tennis/phase3',
                   f'execute as {ROB} at @s run function mg:tennis/robot',
                   # affichage (toutes les 10 ticks)
                   'execute if score $tnab mg.st matches 0 unless score @s mg.tnph matches 0 run title @a[tag=mg.tnk] actionbar ' + LINE,
                   'execute if score $tnab mg.st matches 0 if score @s mg.tnph matches 0 run title @a[tag=mg.tnk,tag=!mg.tnsrv] actionbar ' + LINE,
                   'execute if score $tnab mg.st matches 0 if score @s mg.tnph matches 0 run title @a[tag=mg.tnk,tag=mg.tnsrv] actionbar '
                   '{"text":"🎾 À toi de servir : clic droit avec la raquette (service auto dans 10 s)","color":"yellow"}'])

w('tennis/phase0', ['# @s : marqueur — attente du service (robot : 1,5 s ; joueur : clic droit, ou service automatique après 10 s)',
                    'scoreboard players add @s mg.tnt 1', 'scoreboard players operation $tnside mg.st = @s mg.tnl',
                    f'execute if score @s mg.tnt matches 30.. as {ROB} if score @s mg.tns = $tnside mg.st at @s run return run function mg:tennis/toss',
                    'execute if score @s mg.tnt matches 200.. as @a[tag=mg.tnk] if score @s mg.tns = $tnside mg.st at @s run return run function mg:tennis/toss'])

w('tennis/phase3', ['# @s : marqueur — pause après un point',
                    'scoreboard players remove @s mg.tnt 1', 'execute if score @s mg.tnt matches 1.. run return 0',
                    'execute if entity @s[tag=mg.tndone] run return run function mg:tennis/court_end',
                    'function mg:tennis/point_setup'])

# ---------------------------------------------------------------- balle
w('tennis/toss', ['# @s : serveur (joueur ou robot, à sa position) — lance la balle en l\'air ; frappe auto au sommet',
                  f'kill {BALLS}', 'scoreboard players operation $tnside mg.st = @s mg.tns',
                  'summon minecraft:item_display ^ ^1.2 ^0.6 {Tags:["mg.tent","mg.npc","mg.tnball","mg.tnnew"],item:' + BALL_ITEM +
                  ',billboard:"center",teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],'
                  'translation:[0f,0f,0f],scale:[0.45f,0.45f,0.45f]}}',
                  'execute as @e[type=minecraft:item_display,tag=mg.tnnew] run function mg:tennis/toss_ball',
                  f'scoreboard players set {MARK} mg.tnph 1',
                  f'playsound minecraft:entity.snowball.throw master {NEAR} ~ ~ ~ 0.6 1.4'])
w('tennis/toss_ball', ['# @s : nouvelle balle (lancer du service)', 'tag @s remove mg.tnnew',
                       'scoreboard players operation @s mg.tnc = $tnk mg.st', 'tag @s add mg.tnk', 'tag @s add mg.tntoss',
                       'function mg:tennis/sync_in',
                       'scoreboard players set @s mg.tnvx 0', 'scoreboard players set @s mg.tnvz 0', f'scoreboard players set @s mg.tnvy {TOSS_VY}',
                       'scoreboard players operation @s mg.tnl = $tnside mg.st', 'scoreboard players set @s mg.tnb 0'])
w('tennis/sync_in', ['# @s : position réelle → coordonnées relatives au court (×1000)',
                     'execute store result score @s mg.tnx run data get entity @s Pos[0] 1000',
                     'scoreboard players operation @s mg.tnx -= $tncx mg.st',
                     'execute store result score @s mg.tny run data get entity @s Pos[1] 1000',
                     'execute store result score @s mg.tnz run data get entity @s Pos[2] 1000',
                     f'scoreboard players remove @s mg.tnz {ZO}'])

w('tennis/ball', ['# @s : balle (chaque tick) — gravité, déplacement, filet, rebond, sortie, frappe auto du service',
                  f'scoreboard players remove @s mg.tnvy {G}',
                  'scoreboard players set $tns0 mg.st 1', 'execute if score @s mg.tnz matches 0.. run scoreboard players set $tns0 mg.st 2',
                  'scoreboard players operation @s mg.tnx += @s mg.tnvx', 'scoreboard players operation @s mg.tny += @s mg.tnvy',
                  'scoreboard players operation @s mg.tnz += @s mg.tnvz',
                  'scoreboard players set $tns1 mg.st 1', 'execute if score @s mg.tnz matches 0.. run scoreboard players set $tns1 mg.st 2',
                  f'execute if entity @s[tag=mg.tnlive] unless score $tns0 mg.st = $tns1 mg.st if score @s mg.tny matches ..{NET_TOP} if score @s mg.tnx matches -7500..7500 run function mg:tennis/net',
                  f'execute if score @s mg.tny matches ..{GROUND} if score @s mg.tnvy matches ..-1 run function mg:tennis/bounce',
                  'execute if entity @s[tag=mg.tnlive] unless score @s mg.tnx matches -13000..13000 run function mg:tennis/dead',
                  'execute if entity @s[tag=mg.tnlive] unless score @s mg.tnz matches -19500..19500 run function mg:tennis/dead',
                  'execute if entity @s[tag=mg.tntoss] if score @s mg.tnvy matches ..0 run function mg:tennis/serve_hit',
                  # écriture de la position
                  'scoreboard players operation $tnq mg.st = @s mg.tnx', 'scoreboard players operation $tnq mg.st += $tncx mg.st',
                  'execute store result entity @s Pos[0] double 0.001 run scoreboard players get $tnq mg.st',
                  'execute store result entity @s Pos[1] double 0.001 run scoreboard players get @s mg.tny',
                  f'scoreboard players operation $tnq mg.st = @s mg.tnz', f'scoreboard players add $tnq mg.st {ZO}',
                  'execute store result entity @s Pos[2] double 0.001 run scoreboard players get $tnq mg.st',
                  'execute at @s run particle minecraft:dust{color:[0.85,1.0,0.25],scale:0.7} ~ ~ ~ 0 0 0 0 1'])

w('tennis/bounce', ['# @s : balle — rebond au sol (amorti) ; arbitrage si l\'échange est en cours',
                    f'scoreboard players set @s mg.tny {GROUND}',
                    'execute if score @s mg.tnvy matches ..-60 at @s run particle minecraft:dust{color:[0.75,0.55,0.35],scale:1.2} ~ ~-0.1 ~ 0.15 0 0.15 0 5',
                    f'execute if score @s mg.tnvy matches ..-60 at @s run playsound minecraft:entity.slime.jump_small master {NEAR} ~ ~ ~ 0.7 1.7',
                    'scoreboard players operation @s mg.tnvy *= #tnm7 mg.st', 'scoreboard players operation @s mg.tnvy /= #tn10 mg.st',
                    'execute if score @s mg.tnvy matches ..40 run scoreboard players set @s mg.tnvy 0',
                    'scoreboard players operation @s mg.tnvx *= #tn3 mg.st', 'scoreboard players operation @s mg.tnvx /= #tn4 mg.st',
                    'scoreboard players operation @s mg.tnvz *= #tn3 mg.st', 'scoreboard players operation @s mg.tnvz /= #tn4 mg.st',
                    'execute if entity @s[tag=mg.tnlive] run function mg:tennis/judge'])

w('tennis/judge', ['# @s : balle en jeu qui touche le sol — mg.tnl = frappeur, mg.tnb = rebonds chez le receveur',
                   'scoreboard players set $tnbs mg.st 1', 'execute if score @s mg.tnz matches 0.. run scoreboard players set $tnbs mg.st 2',
                   'scoreboard players set $tnin mg.st 0',
                   f'execute if score @s mg.tnx matches -{HW}..{HW} if score @s mg.tnz matches -{HL}..{HL} run scoreboard players set $tnin mg.st 1',
                   # rebond dans son propre camp : faute du frappeur
                   'execute if score $tnbs mg.st = @s mg.tnl run scoreboard players set $tnwhy mg.st 4',
                   'execute if score $tnbs mg.st = @s mg.tnl run return run function mg:tennis/pt_recv',
                   # second rebond chez le receveur : point au frappeur
                   'execute if score @s mg.tnb matches 1.. run scoreboard players set $tnwhy mg.st 3',
                   'execute if score @s mg.tnb matches 1.. run return run function mg:tennis/pt_hitter',
                   # premier rebond dehors : faute
                   'execute if score $tnin mg.st matches 0 run scoreboard players set $tnwhy mg.st 2',
                   'execute if score $tnin mg.st matches 0 run return run function mg:tennis/pt_recv',
                   'scoreboard players set @s mg.tnb 1'])
w('tennis/net', ['# @s : balle — dans le filet : arrêtée, point au receveur',
                 'scoreboard players set @s mg.tnz -300', 'execute if score @s mg.tnl matches 2 run scoreboard players set @s mg.tnz 300',
                 'scoreboard players set @s mg.tnvx 0', 'scoreboard players set @s mg.tnvz 0',
                 'execute if score @s mg.tnvy matches 1.. run scoreboard players set @s mg.tnvy 0',
                 f'execute at @s run playsound minecraft:block.wool.hit master {NEAR} ~ ~ ~ 1 0.8',
                 'scoreboard players set $tnwhy mg.st 1', 'function mg:tennis/pt_recv'])
w('tennis/dead', ['# @s : balle sortie de la zone sans être reprise (rebond valable avant : point au frappeur, sinon faute)',
                  'execute if score @s mg.tnb matches 1.. run scoreboard players set $tnwhy mg.st 5',
                  'execute if score @s mg.tnb matches 1.. run return run function mg:tennis/pt_hitter',
                  'scoreboard players set $tnwhy mg.st 2', 'function mg:tennis/pt_recv'])
w('tennis/pt_hitter', ['# @s : balle — point au frappeur', 'scoreboard players operation $tnw mg.st = @s mg.tnl',
                       f'execute as {MARK} run function mg:tennis/point'])
w('tennis/pt_recv', ['# @s : balle — point au receveur', 'scoreboard players set $tnw mg.st 3',
                     'scoreboard players operation $tnw mg.st -= @s mg.tnl', f'execute as {MARK} run function mg:tennis/point'])

# ---------------------------------------------------------------- frappes
w('tennis/lz', ['# $tnlz = profondeur $tndepth dans le camp adverse de $tnside (côté 1 joue vers +z)',
                'scoreboard players operation $tnlz mg.st = $tndepth mg.st',
                'execute if score $tnside mg.st matches 2 run scoreboard players operation $tnlz mg.st *= #tnm1 mg.st'])
w('tennis/aim_target', ['# @s : joueur — point d\'impact selon son regard horizontal (balle en $tnbx/$tnbz, profondeur $tndepth)',
                        f'execute rotated as @s rotated ~ 0 positioned 0.0 64 {CZ}.0 run tp {DIR} ^ ^ ^1',
                        f'execute store result score $tnax mg.st run data get entity {DIR} Pos[0] 1000',
                        f'execute store result score $tnaz mg.st run data get entity {DIR} Pos[2] 1000',
                        f'scoreboard players remove $tnaz mg.st {CZ * 1000}',
                        'execute if score $tnside mg.st matches 2 run scoreboard players operation $tnaz mg.st *= #tnm1 mg.st',
                        # direction limitée vers le camp adverse (±53° environ)
                        'execute if score $tnaz mg.st matches ..599 run scoreboard players set $tnaz mg.st 600',
                        'execute if score $tnax mg.st matches ..-801 run scoreboard players set $tnax mg.st -800',
                        'execute if score $tnax mg.st matches 801.. run scoreboard players set $tnax mg.st 800',
                        'function mg:tennis/lz',
                        'scoreboard players operation $tnd mg.st = $tnlz mg.st', 'scoreboard players operation $tnd mg.st -= $tnbz mg.st',
                        'execute if score $tnside mg.st matches 2 run scoreboard players operation $tnd mg.st *= #tnm1 mg.st',
                        'scoreboard players operation $tnlx mg.st = $tnax mg.st', 'scoreboard players operation $tnlx mg.st *= $tnd mg.st',
                        # visée adoucie (écart latéral divisé par 2) : il faut viser franchement de côté pour sortir
                        'scoreboard players operation $tnlx mg.st /= $tnaz mg.st', 'scoreboard players operation $tnlx mg.st /= #tn2 mg.st',
                        'scoreboard players operation $tnlx mg.st += $tnbx mg.st',
                        'execute if score $tnlx mg.st matches ..-7501 run scoreboard players set $tnlx mg.st -7500',
                        'execute if score $tnlx mg.st matches 7501.. run scoreboard players set $tnlx mg.st 7500'])
w('tennis/shoot', ['# @s : balle — frappe par le côté $tnside vers ($tnlx, $tnlz) en $tnT ticks',
                   'scoreboard players operation @s mg.tnvx = $tnlx mg.st', 'scoreboard players operation @s mg.tnvx -= @s mg.tnx',
                   'scoreboard players operation @s mg.tnvx /= $tnT mg.st',
                   'scoreboard players operation @s mg.tnvz = $tnlz mg.st', 'scoreboard players operation @s mg.tnvz -= @s mg.tnz',
                   'scoreboard players operation @s mg.tnvz /= $tnT mg.st',
                   f'scoreboard players set @s mg.tnvy {GROUND}', 'scoreboard players operation @s mg.tnvy -= @s mg.tny',
                   'scoreboard players operation @s mg.tnvy /= $tnT mg.st',
                   'scoreboard players operation $tnq mg.st = $tnT mg.st', 'scoreboard players operation $tnq mg.st *= #tng mg.st',
                   'scoreboard players operation $tnq mg.st /= #tn2 mg.st', 'scoreboard players operation @s mg.tnvy += $tnq mg.st',
                   'scoreboard players set @s mg.tnb 0', 'scoreboard players operation @s mg.tnl = $tnside mg.st',
                   'tag @s remove mg.tntoss', 'tag @s add mg.tnlive',
                   f'execute at @s run playsound minecraft:entity.player.attack.strong master {NEAR} ~ ~ ~ 1 1.6',
                   'execute at @s run particle minecraft:crit ~ ~ ~ 0.1 0.1 0.1 0.2 6',
                   # le robot adverse vise l'endroit où la balle arrivera
                   'scoreboard players operation $tnvx mg.st = @s mg.tnvx', 'scoreboard players operation $tnvz mg.st = @s mg.tnvz',
                   f'execute as {ROB} unless score @s mg.tns = $tnside mg.st run function mg:tennis/robot_aim',
                   # le robot qui vient de frapper revient vers le centre, celui d'en face poursuit la balle
                   f'tag {ROB} remove mg.tnchase', f'execute as {ROB} unless score @s mg.tns = $tnside mg.st run tag @s add mg.tnchase'])

SW = ['# @s : joueur qui fait un clic droit (warped_fungus_on_a_stick) — service ou renvoi',
      'scoreboard players reset @s mg.qs',
      'execute unless items entity @s weapon.* *[minecraft:custom_data~{mg_racket:1b}] run return 0',
      'execute if score @s mg.tnt matches 1.. run return 0', 'scoreboard players set @s mg.tnt 8',
      f'playsound minecraft:entity.player.attack.sweep master {NEAR} ~ ~ ~ 0.5 1.5',
      'scoreboard players operation $tnk mg.st = @s mg.tnc', 'function mg:tennis/tagk',
      'scoreboard players operation $tnside mg.st = @s mg.tns',
      # service : c'est à moi de servir et la balle n'est pas encore lancée
      'scoreboard players set $tnq mg.st 0',
      f'execute as {MARK} if score @s mg.tnph matches 0 if score @s mg.tnl = $tnside mg.st run scoreboard players set $tnq mg.st 1',
      'execute if score $tnq mg.st matches 1 run return run function mg:tennis/toss',
      # renvoi : balle en jeu, à portée, pas frappée en dernier par mon camp
      'tag @e[tag=mg.tnhit] remove mg.tnhit',
      f'execute positioned ~ ~1 ~ as @e[type=minecraft:item_display,tag=mg.tnball,tag=mg.tnk,tag=mg.tnlive,distance=..{REACH},limit=1,sort=nearest] '
      'unless score @s mg.tnl = $tnside mg.st run tag @s add mg.tnhit',
      'execute unless entity @e[tag=mg.tnhit] run return 0',
      # timing : balle encore loin = frappe tôt = coup fort ; tout près = frappe tardive, courte
      f'scoreboard players set $tnT mg.st {SHOTS["normal"][0]}', f'scoreboard players set $tndepth mg.st {SHOTS["normal"][1]}',
      'scoreboard players set $tnshot mg.st 1',
      f'execute positioned ~ ~1 ~ if entity @e[tag=mg.tnhit,distance=1.8..] run scoreboard players set $tnshot mg.st 2',
      f'execute positioned ~ ~1 ~ if entity @e[tag=mg.tnhit,distance=..1.0] run scoreboard players set $tnshot mg.st 0',
      f'execute if predicate {PRED_SNEAK} run scoreboard players set $tnshot mg.st 3']
for n, key in ((2, 'fort'), (0, 'tard'), (3, 'lob')):
    SW += [f'execute if score $tnshot mg.st matches {n} run scoreboard players set $tnT mg.st {SHOTS[key][0]}',
           f'execute if score $tnshot mg.st matches {n} run scoreboard players set $tndepth mg.st {SHOTS[key][1]}']
SW += ['execute as @e[tag=mg.tnhit] run scoreboard players operation $tnbx mg.st = @s mg.tnx',
       'execute as @e[tag=mg.tnhit] run scoreboard players operation $tnbz mg.st = @s mg.tnz',
       'function mg:tennis/aim_target', 'execute as @e[tag=mg.tnhit] run function mg:tennis/shoot',
       'tag @e[tag=mg.tnhit] remove mg.tnhit',
       'execute if score $tnshot mg.st matches 2 run title @s actionbar {"text":"💥 Coup puissant !","color":"gold"}',
       'execute if score $tnshot mg.st matches 1 run title @s actionbar {"text":"✔ Bien joué","color":"green"}',
       'execute if score $tnshot mg.st matches 0 run title @s actionbar {"text":"Frappe tardive…","color":"gray"}',
       'execute if score $tnshot mg.st matches 3 run title @s actionbar {"text":"⤴ Lob !","color":"aqua"}']
w('tennis/swing', SW)

w('tennis/serve_hit', ['# @s : balle lancée au sommet de sa course — frappe automatique du service (visée du serveur)',
                       'scoreboard players operation $tnside mg.st = @s mg.tnl',
                       'scoreboard players operation $tnbx mg.st = @s mg.tnx', 'scoreboard players operation $tnbz mg.st = @s mg.tnz',
                       f'scoreboard players set $tnT mg.st {SHOTS["service"][0]}', f'scoreboard players set $tndepth mg.st {SHOTS["service"][1]}',
                       'scoreboard players operation $tnlx mg.st = $tnbx mg.st', 'function mg:tennis/lz',
                       'execute as @a[tag=mg.tnk] if score @s mg.tns = $tnside mg.st run function mg:tennis/aim_target',
                       f'execute as {ROB} if score @s mg.tns = $tnside mg.st run function mg:tennis/robot_pick',
                       'function mg:tennis/shoot', f'scoreboard players set {MARK} mg.tnph 2'])

# ---------------------------------------------------------------- robot
w('tennis/robot', ['# @s : robot (à sa position) — se déplace vers la balle attendue (ou le centre de sa ligne de fond) et renvoie',
                   'execute store result score $tnrx mg.st run data get entity @s Pos[0] 1000',
                   'scoreboard players operation $tnrx mg.st -= $tncx mg.st',
                   'execute store result score $tnrz mg.st run data get entity @s Pos[2] 1000',
                   f'scoreboard players remove $tnrz mg.st {ZO}',
                   'scoreboard players set $tntx mg.st 0', 'scoreboard players set $tntz mg.st -14000',
                   'execute if score @s mg.tns matches 2 run scoreboard players set $tntz mg.st 14000',
                   'execute if entity @s[tag=mg.tnchase] run scoreboard players operation $tntx mg.st = @s mg.tnx',
                   'execute if entity @s[tag=mg.tnchase] run scoreboard players operation $tntz mg.st = @s mg.tnz',
                   # pas plus de ROBOT_SPEED par axe
                   'scoreboard players operation $tntx mg.st -= $tnrx mg.st', 'scoreboard players operation $tntz mg.st -= $tnrz mg.st',
                   f'execute if score $tntx mg.st matches {ROBOT_SPEED + 1}.. run scoreboard players set $tntx mg.st {ROBOT_SPEED}',
                   f'execute if score $tntx mg.st matches ..-{ROBOT_SPEED + 1} run scoreboard players set $tntx mg.st -{ROBOT_SPEED}',
                   f'execute if score $tntz mg.st matches {ROBOT_SPEED + 1}.. run scoreboard players set $tntz mg.st {ROBOT_SPEED}',
                   f'execute if score $tntz mg.st matches ..-{ROBOT_SPEED + 1} run scoreboard players set $tntz mg.st -{ROBOT_SPEED}',
                   'scoreboard players operation $tnrx mg.st += $tntx mg.st', 'scoreboard players operation $tnrz mg.st += $tntz mg.st',
                   f'execute if entity {BALL} run tp @s ~ ~ ~ facing entity {BALL}',
                   'scoreboard players operation $tnrx mg.st += $tncx mg.st', f'scoreboard players add $tnrz mg.st {ZO}',
                   'execute store result entity @s Pos[0] double 0.001 run scoreboard players get $tnrx mg.st',
                   'execute store result entity @s Pos[2] double 0.001 run scoreboard players get $tnrz mg.st',
                   # renvoi après un rebond chez lui
                   'scoreboard players operation $tnside mg.st = @s mg.tns', 'tag @e[tag=mg.tnhit] remove mg.tnhit',
                   f'execute if score @s mg.tnt matches 0 unless entity @s[tag=mg.tnmiss] positioned ~ ~1 ~ as @e[type=minecraft:item_display,tag=mg.tnball,tag=mg.tnk,tag=mg.tnlive,scores={{mg.tnb=1}},distance=..{ROBOT_REACH},limit=1] '
                   'unless score @s mg.tnl = $tnside mg.st run tag @s add mg.tnhit',
                   'execute if entity @e[tag=mg.tnhit] run function mg:tennis/robot_hit'])
w('tennis/robot_pick', ['# @s : robot — coup imprécis : impact au hasard (parfois dehors), parfois un lob',
                        'execute store result score $tnlx mg.st run random value -6300..6300',
                        'execute store result score $tndepth mg.st run random value 5000..11800',
                        'execute store result score $tnT mg.st run random value 26..36',
                        'execute store result score $tnq mg.st run random value 1..8',
                        f'execute if score $tnq mg.st matches 1 run scoreboard players set $tnT mg.st {SHOTS["lob"][0]}',
                        'scoreboard players operation $tnside mg.st = @s mg.tns', 'function mg:tennis/lz'])
w('tennis/robot_hit', ['# @s : robot — renvoie la balle tagguée mg.tnhit', 'scoreboard players set @s mg.tnt 10',
                       'function mg:tennis/robot_pick',
                       'execute as @e[tag=mg.tnhit] run function mg:tennis/shoot', 'tag @e[tag=mg.tnhit] remove mg.tnhit'])
w('tennis/robot_aim', ['# @s : robot — la balle arrive ($tnlx/$tnlz impact, $tnvx/$tnvz vitesse) : il vise un peu après le rebond',
                       'scoreboard players operation $tnq mg.st = $tnvx mg.st', 'scoreboard players operation $tnq mg.st *= #tn3 mg.st',
                       'scoreboard players operation @s mg.tnx = $tnq mg.st', 'scoreboard players operation @s mg.tnx *= #tn2 mg.st',
                       'scoreboard players operation @s mg.tnx += $tnlx mg.st',
                       'scoreboard players operation $tnq mg.st = $tnvz mg.st', 'scoreboard players operation $tnq mg.st *= #tn3 mg.st',
                       'scoreboard players operation @s mg.tnz = $tnq mg.st', 'scoreboard players operation @s mg.tnz *= #tn2 mg.st',
                       'scoreboard players operation @s mg.tnz += $tnlz mg.st',
                       'execute store result score $tnq mg.st run random value -1000..1000', 'scoreboard players operation @s mg.tnx += $tnq mg.st',
                       'execute if score @s mg.tnx matches ..-9001 run scoreboard players set @s mg.tnx -9000',
                       'execute if score @s mg.tnx matches 9001.. run scoreboard players set @s mg.tnx 9000',
                       'execute if score @s mg.tns matches 2 if score @s mg.tnz matches ..3999 run scoreboard players set @s mg.tnz 4000',
                       'execute if score @s mg.tns matches 2 if score @s mg.tnz matches 17501.. run scoreboard players set @s mg.tnz 17500',
                       'execute if score @s mg.tns matches 1 if score @s mg.tnz matches -3999.. run scoreboard players set @s mg.tnz -4000',
                       'execute if score @s mg.tns matches 1 if score @s mg.tnz matches ..-17501 run scoreboard players set @s mg.tnz -17500',
                       'tag @s remove mg.tnmiss', 'execute store result score $tnq mg.st run random value 1..100',
                       f'execute if score $tnq mg.st matches ..{ROBOT_MISS} run tag @s add mg.tnmiss'])

# ---------------------------------------------------------------- score
WHY = {1: 'Filet !', 2: 'Faute : balle dehors', 3: 'Double rebond', 4: 'Faute : rebond dans son camp', 5: 'Balle non rattrapée'}
PT = ['# @s : marqueur — point pour le côté $tnw ($tnwhy = raison)',
      f'tag {BALLS} remove mg.tnlive', f'tag {BALLS} remove mg.tntoss',
      'execute if score $tnw mg.st matches 1 run scoreboard players add @s mg.tnp1 1',
      'execute if score $tnw mg.st matches 2 run scoreboard players add @s mg.tnp2 1',
      'scoreboard players set @s mg.tnph 3', 'scoreboard players set @s mg.tnt 50',
      f'tag {ROB} remove mg.tnchase', 'title @a[tag=mg.tnk] times 3 25 8']
for r, t in WHY.items():
    PT.append(f'execute if score $tnwhy mg.st matches {r} run title @a[tag=mg.tnk] subtitle {js({"text": t, "color": "gray"})}')
for s in (1, 2):
    PT.append(f'execute if score $tnw mg.st matches {s} run title @a[tag=mg.tnk] title {js([{"text": "Point ", "color": "white"}, SIDE_TXT[s]])}')
PT += ['execute as @a[tag=mg.tnk] at @s if score @s mg.tns = $tnw mg.st run playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 0.8 1.2',
       'execute as @a[tag=mg.tnk] at @s unless score @s mg.tns = $tnw mg.st run playsound minecraft:block.note_block.bass master @s ~ ~ ~ 0.8 0.7',
       'scoreboard players operation $tnq mg.st = @s mg.tnp1', 'scoreboard players operation $tnq mg.st -= @s mg.tnp2',
       f'execute if score @s mg.tnp1 matches {POINTS}.. if score $tnq mg.st matches 2.. run function mg:tennis/game_won1',
       f'execute if score @s mg.tnp2 matches {POINTS}.. if score $tnq mg.st matches ..-2 run function mg:tennis/game_won2',
       'function mg:tennis/labels']
w('tennis/point', PT)

for s in (1, 2):
    w(f'tennis/game_won{s}', [f'# @s : marqueur — jeu gagné par le côté {s} ; le service change de camp',
                              f'scoreboard players add @s mg.tng{s} 1', 'scoreboard players set @s mg.tnp1 0', 'scoreboard players set @s mg.tnp2 0',
                              'scoreboard players set $tnq mg.st 3', 'scoreboard players operation $tnq mg.st -= @s mg.tnl',
                              'scoreboard players operation @s mg.tnl = $tnq mg.st',
                              f'scoreboard players operation $tnq mg.st = @s mg.tng{s}',
                              f'execute as @a[tag=mg.tnk,scores={{mg.tns={s}}}] run scoreboard players operation @s mg.tngw = $tnq mg.st',
                              f'execute if entity @e[type=minecraft:mannequin,tag=mg.tnrob,tag=mg.tnk,scores={{mg.tns={s}}}] run scoreboard players operation Robot mg.tngw = $tnq mg.st',
                              f'title @a[tag=mg.tnk] title {js([{"text": "Jeu ", "color": "gold"}, SIDE_TXT[s]])}',
                              'tellraw @a[tag=mg.tnk] ' + js([{'text': '🎾 Jeu pour ', 'color': 'gold'},
                                                              {'selector': f'@e[tag=mg.tnk,scores={{mg.tns={s}}}]', 'color': SIDE_TXT[s]['color']},
                                                              {'text': ' — jeux ', 'color': 'gray'}, {'score': {'name': '@s', 'objective': 'mg.tng1'}, 'color': 'aqua'},
                                                              {'text': '-', 'color': 'gray'}, {'score': {'name': '@s', 'objective': 'mg.tng2'}, 'color': 'red'}]),
                              f'execute as @a[tag=mg.tnk] at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.6 1.3',
                              f'scoreboard players set $tnw mg.st {s}',
                              f'execute if score @s mg.tng{s} matches {GAMES}.. run function mg:tennis/court_win'])

w('tennis/court_win', ['# @s : marqueur — le côté $tnw remporte le match de ce court (fin après la pause)',
                       'tag @s add mg.tndone', 'scoreboard players operation @s mg.tnb = $tnw mg.st',
                       'execute as @a[tag=mg.tnk] if score @s mg.tns = $tnw mg.st run tag @s add mg.tnwin',
                       'tag @e[tag=mg.tnws] remove mg.tnws', 'tag @e[tag=mg.tnls] remove mg.tnls',
                       'execute as @e[tag=mg.tnk,scores={mg.tns=1..2}] if score @s mg.tns = $tnw mg.st run tag @s add mg.tnws',
                       'execute as @e[tag=mg.tnk,scores={mg.tns=1..2}] unless score @s mg.tns = $tnw mg.st run tag @s add mg.tnls',
                       'tellraw @a ' + js([{'text': '🎾 Court ', 'color': 'gold'}, {'score': {'name': '@s', 'objective': 'mg.tnc'}, 'color': 'gold'},
                                           {'text': ' : ', 'color': 'gold'}, {'selector': '@e[tag=mg.tnws]', 'color': 'yellow', 'bold': True},
                                           {'text': ' bat ', 'color': 'gray'}, {'selector': '@e[tag=mg.tnls]', 'color': 'gray'},
                                           {'text': ' (', 'color': 'gray'}, {'score': {'name': '@s', 'objective': 'mg.tng1'}, 'color': 'aqua'},
                                           {'text': '-', 'color': 'gray'}, {'score': {'name': '@s', 'objective': 'mg.tng2'}, 'color': 'red'},
                                           {'text': ')', 'color': 'gray'}]),
                       'title @a[tag=mg.tnk,tag=mg.tnws] title {"text":"Jeu, set et match !","color":"gold","bold":true}',
                       'title @a[tag=mg.tnk,tag=mg.tnls] title {"text":"Match perdu","color":"gray"}',
                       'execute as @a[tag=mg.tnk,tag=mg.tnws] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.8 1.2',
                       'tag @e[tag=mg.tnws] remove mg.tnws', 'tag @e[tag=mg.tnls] remove mg.tnls'])
w('tennis/forfeit', ['# @s : marqueur — un côté est vide (joueur parti) : l\'autre gagne le court',
                     'function mg:tennis/court_win', 'function mg:tennis/court_end'])
w('tennis/court_end', ['# @s : marqueur — court terminé', f'kill {BALLS}', 'scoreboard players set @s mg.tnph 4',
                       f'tag {ROB} remove mg.tnchase',
                       'execute if entity @e[type=minecraft:marker,tag=mg.tncm,scores={mg.tnph=0..3}] run title @a[tag=mg.tnk] actionbar {"text":"🎾 Match terminé — attente des autres courts…","color":"gray"}'])

LB = ['# @s : marqueur — libellés du score (data.a / data.b, jeux data.ga / data.gb) et tableau du court']
if POINTS == 4:
    for s, key in ((1, 'a'), (2, 'b')):
        LB += [f'data modify entity @s data.{key} set value "0"'] + [
            f'execute if score @s mg.tnp{s} matches {n}{".." if n == 3 else ""} run data modify entity @s data.{key} set value "{lab}"'
            for n, lab in ((1, '15'), (2, '30'), (3, '40'))]
    LB += ['execute if score @s mg.tnp1 matches 3.. if score @s mg.tnp2 matches 3.. if score @s mg.tnp1 > @s mg.tnp2 run data modify entity @s data.a set value "AV"',
           'execute if score @s mg.tnp1 matches 3.. if score @s mg.tnp2 matches 3.. if score @s mg.tnp2 > @s mg.tnp1 run data modify entity @s data.b set value "AV"']
else:
    LB += ['execute store result entity @s data.a int 1 run scoreboard players get @s mg.tnp1',
           'execute store result entity @s data.b int 1 run scoreboard players get @s mg.tnp2']
LB += ['execute store result entity @s data.ga int 1 run scoreboard players get @s mg.tng1',
       'execute store result entity @s data.gb int 1 run scoreboard players get @s mg.tng2',
       f'execute as @e[type=minecraft:text_display,tag=mg.tntd,tag=mg.tnk] run function mg:tennis/board_set with entity {MARK} data']
w('tennis/labels', LB)
w('tennis/board_set', ['# @s : tableau du court (macro : k, a, b, ga, gb)',
                       '$data modify entity @s text set value [{"text":"🎾 COURT $(k)\\n","color":"gold","bold":true},'
                       '{"text":"BLEU  ","color":"aqua","bold":true},{"text":"$(a)","color":"white","bold":true},{"text":"  —  ","color":"gray"},'
                       '{"text":"$(b)","color":"white","bold":true},{"text":"  ROUGE","color":"red","bold":true},'
                       '{"text":"\\nJeux  ","color":"yellow","bold":false},{"text":"$(ga)","color":"aqua","bold":true},'
                       '{"text":" - ","color":"gray","bold":false},{"text":"$(gb)","color":"red","bold":true}]'])

# ---------------------------------------------------------------- fin
w('tennis/timeout', ['# Temps écoulé : sur chaque court en cours, le meilleur (jeux puis points) gagne ; égalité = personne',
                     'execute as @e[type=minecraft:marker,tag=mg.tncm,scores={mg.tnph=0..3}] run function mg:tennis/timeout_court',
                     'function mg:tennis/finish'])
w('tennis/timeout_court', ['# @s : marqueur d\'un court pas fini', 'scoreboard players operation $tnk mg.st = @s mg.tnc', 'function mg:tennis/tagk',
                           'scoreboard players set $tnw mg.st 0',
                           'execute if score @s mg.tnp1 > @s mg.tnp2 run scoreboard players set $tnw mg.st 1',
                           'execute if score @s mg.tnp2 > @s mg.tnp1 run scoreboard players set $tnw mg.st 2',
                           'execute if score @s mg.tng1 > @s mg.tng2 run scoreboard players set $tnw mg.st 1',
                           'execute if score @s mg.tng2 > @s mg.tng1 run scoreboard players set $tnw mg.st 2',
                           'execute if score $tnw mg.st matches 1..2 run function mg:tennis/court_win',
                           'function mg:tennis/court_end'])
w('tennis/finish', ['# Tous les courts sont finis : vainqueur(s) = gagnants humains de chaque court',
                    'execute unless score $state mg.st matches 2 run return 0',
                    'execute store result score $tnq mg.st if entity @a[tag=mg.tnwin,tag=mg.play]',
                    'execute if score $tnq mg.st matches 0 run return run function mg:core/draw',
                    'execute if score $tnq mg.st matches 1 as @a[tag=mg.tnwin,tag=mg.play,limit=1] run return run function mg:core/win_player',
                    'function mg:tennis/win_multi'])
w('tennis/win_multi', ['# Victoire de plusieurs joueurs (un par court), même format que core/win_red',
                       'tag @a[tag=mg.tnwin,tag=mg.play] add mg.win',
                       'scoreboard players add @a[tag=mg.tnwin,tag=mg.play] mg.wins 1',
                       'scoreboard players set $state mg.st 3',
                       'scoreboard players set $timer mg.st 120',
                       'title @a[tag=!mg.surv] subtitle [{"selector":"@a[tag=mg.tnwin,tag=mg.play]","color":"yellow"}]',
                       'title @a[tag=!mg.surv] title [{"text":"🎾 Vainqueurs des courts","color":"gold","bold":true}]',
                       'tellraw @a [{"text":"★ Victoire au tennis : ","color":"gold"},{"selector":"@a[tag=mg.tnwin,tag=mg.play]","color":"yellow","bold":true},{"text":" !","color":"gold"}]',
                       'execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1'])

OBJ = ['mg.tnc', 'mg.tns', 'mg.tnx', 'mg.tny', 'mg.tnz', 'mg.tnvx', 'mg.tnvy', 'mg.tnvz', 'mg.tnb', 'mg.tnl', 'mg.tnph', 'mg.tnt',
       'mg.tnp1', 'mg.tnp2', 'mg.tng1', 'mg.tng2']
w('tennis/cleanup', ['# Fin : balles, robot, marqueurs, tableaux, raquettes', 'kill @e[tag=mg.tent]',
                     'clear @a *[minecraft:custom_data~{mg_racket:1b}]',
                     'title @a[tag=mg.play] reset', 'tag @a remove mg.tnk', 'tag @a remove mg.tnwin', 'tag @a remove mg.tnsrv'] +
  [f'scoreboard players reset * {o}' for o in OBJ + ['mg.tngw']])

C.register([GID], 'tennis', [C.announce(GID, '', '🎾 TENNIS', 'yellow', f'1 contre 1, chacun son court : premier à {GAMES} jeux !')])
C.objectives([(o, 'dummy') for o in OBJ] + [('mg.tngw', 'dummy {"text":"🎾 Jeux gagnés","color":"yellow"}')])
C.forceload([f'# Tennis (z {CZ})', f'forceload add -80 {CZ - 25} 79 {CZ + 25}'])
print('Tennis OK')
