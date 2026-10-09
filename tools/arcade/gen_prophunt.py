"""🎭 Prop Hunt (id 96). Manoir de 6 pièces meublées en z 23600.

    python tools/arcade/gen_prophunt.py .

Cacheurs : invisibles et rapetissés, ils prennent l'apparence d'un objet (block_display qui les suit). Regarder un objet
du manoir et s'accroupir = se transformer en cet objet. Immobile 2 s = l'objet se cale sur la grille (verrouillé).
Toutes les 20 s, chaque cacheur fait un bruit ; il peut aussi en faire quand il veut avec sa corne (clic droit). Cacheurs : 5 cœurs (2 coups d'épée). Chercheurs : enfermés et aveugles pendant 30 s, puis 3 min 30 de chasse.
Frapper un objet suspect touche le cacheur (interaction autour de l'objet). Cacheur tué = devient chercheur.
Il reste un cacheur à la fin → les cacheurs gagnent ; plus aucun → les chercheurs gagnent.
Seul : mode entraînement (pas de victoire, fin au chrono ou menu → Arrêter).
"""
import random
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
Z = 23600
HIDE, HUNT = 600, 4200
PROPS = ['barrel', 'crafting_table', 'bookshelf', 'hay_block', 'pumpkin', 'carved_pumpkin', 'melon', 'composter', 'cauldron', 'lantern',
         'anvil', 'furnace', 'smoker', 'loom', 'fletching_table', 'smithing_table', 'cartography_table', 'beehive', 'jukebox', 'note_block',
         'cake', 'brewing_stand', 'grindstone', 'stonecutter', 'potted_red_tulip', 'oak_leaves', 'cobweb', 'target', 'lectern', 'blast_furnace']
PID = {p: i + 1 for i, p in enumerate(PROPS)}
ROOMS = [  # (x1, x2, z1, z2, sol, objets)
    (-19, -8, Z - 14, Z - 1, 'spruce_planks', ['furnace', 'smoker', 'cauldron', 'barrel', 'crafting_table', 'cake', 'blast_furnace', 'potted_red_tulip']),
    (-6, 6, Z - 14, Z - 1, 'oak_planks', ['bookshelf', 'lectern', 'lantern', 'potted_red_tulip', 'cartography_table', 'jukebox']),
    (8, 19, Z - 14, Z - 1, 'stone_bricks', ['anvil', 'grindstone', 'smithing_table', 'fletching_table', 'stonecutter', 'loom', 'barrel']),
    (-19, -8, Z + 1, Z + 14, 'dark_oak_planks', ['hay_block', 'pumpkin', 'carved_pumpkin', 'melon', 'composter', 'barrel', 'cobweb']),
    (-6, 6, Z + 1, Z + 14, 'birch_planks', ['jukebox', 'note_block', 'lantern', 'cake', 'potted_red_tulip', 'bookshelf', 'target']),
    (8, 19, Z + 1, Z + 14, 'moss_block', ['beehive', 'oak_leaves', 'potted_red_tulip', 'composter', 'target', 'pumpkin', 'hay_block']),
]

# ------------------------------------------------------------------ manoir
rnd = random.Random(96)
L = ['# 🎭 Manoir du Prop Hunt — x −20..20, z 23585..23615, sol y 80, toit y 87 ; cage des chercheurs sur le toit']
L += [f'fill -23 {y} {Z - 18} 23 {y} {Z + 18} minecraft:air' for y in range(78, 96)]
L += [f'fill -20 79 {Z - 15} 20 79 {Z + 15} minecraft:stone']
for (x1, x2, z1, z2, fl, _) in ROOMS:
    L.append(f'fill {x1 - 1} 80 {z1 - 1} {x2 + 1} 80 {z2 + 1} minecraft:{fl}')
L += [f'fill -20 80 {Z - 15} 20 86 {Z - 15} minecraft:stripped_oak_log', f'fill -20 80 {Z + 15} 20 86 {Z + 15} minecraft:stripped_oak_log',
      f'fill -20 80 {Z - 14} -20 86 {Z + 14} minecraft:stripped_oak_log', f'fill 20 80 {Z - 14} 20 86 {Z + 14} minecraft:stripped_oak_log',
      f'fill -7 81 {Z - 14} -7 86 {Z + 14} minecraft:white_terracotta', f'fill 7 81 {Z - 14} 7 86 {Z + 14} minecraft:white_terracotta',
      f'fill -19 81 {Z} 19 86 {Z} minecraft:white_terracotta',
      f'fill -20 87 {Z - 15} 20 87 {Z + 15} minecraft:dark_oak_planks']
# portes de 2 de large
L += [f'fill -7 81 {Z - 8} -7 83 {Z - 7} minecraft:air', f'fill -7 81 {Z + 7} -7 83 {Z + 8} minecraft:air',
      f'fill 7 81 {Z - 8} 7 83 {Z - 7} minecraft:air', f'fill 7 81 {Z + 7} 7 83 {Z + 8} minecraft:air',
      f'fill -14 81 {Z} -13 83 {Z} minecraft:air', f'fill -1 81 {Z} 0 83 {Z} minecraft:air', f'fill 13 81 {Z} 14 83 {Z} minecraft:air']
# fenêtres et éclairage
for x in range(-17, 18, 6):
    L += [f'fill {x} 82 {Z - 15} {x + 1} 84 {Z - 15} minecraft:glass_pane', f'fill {x} 82 {Z + 15} {x + 1} 84 {Z + 15} minecraft:glass_pane']
L += [f'setblock {x} 87 {z} minecraft:glowstone' for x in range(-17, 18, 5) for z in range(Z - 12, Z + 13, 5)]
# mobilier (~25 objets par pièce, parfois empilés)
door_cells = {(-8, Z - 8), (-8, Z - 7), (-6, Z - 8), (-6, Z - 7), (-8, Z + 7), (-8, Z + 8), (-6, Z + 7), (-6, Z + 8),
              (6, Z - 8), (6, Z - 7), (8, Z - 8), (8, Z - 7), (6, Z + 7), (6, Z + 8), (8, Z + 7), (8, Z + 8),
              (-14, Z - 1), (-13, Z - 1), (-14, Z + 1), (-13, Z + 1), (-1, Z - 1), (0, Z - 1), (-1, Z + 1), (0, Z + 1),
              (13, Z - 1), (14, Z - 1), (13, Z + 1), (14, Z + 1)}
used = set()
for (x1, x2, z1, z2, fl, pal) in ROOMS:
    n = 0
    tries = 0
    while n < 26 and tries < 400:
        tries += 1
        x, z = rnd.randint(x1, x2), rnd.randint(z1, z2)
        if (x, z) in door_cells or (x, z) in used or any((x + dx, z + dz) in used for dx in (-1, 0, 1) for dz in (-1, 0, 1) if rnd.random() < 0.35):
            continue
        used.add((x, z))
        p = rnd.choice(pal)
        blk = 'oak_leaves[persistent=true]' if p == 'oak_leaves' else p
        L.append(f'setblock {x} 81 {z} minecraft:{blk}')
        if p in ('barrel', 'hay_block', 'bookshelf', 'melon') and rnd.random() < 0.4:
            L.append(f'setblock {x} 82 {z} minecraft:{blk}')
        n += 1
# cage des chercheurs (sur le toit)
L += [f'fill -3 88 {Z - 3} 3 92 {Z + 3} minecraft:black_stained_glass', f'fill -2 89 {Z - 2} 2 91 {Z + 2} minecraft:air',
      f'fill -2 88 {Z - 2} 2 88 {Z + 2} minecraft:black_concrete']
w('ph/build', L)

# ------------------------------------------------------------------ fonctions
w('ph/prepare', ['# 🎭 Prop Hunt — préparation', 'function mg:ph/build', 'function mg:ph/kill_all',
                 'scoreboard players set $px mg.st 0', 'scoreboard players set $py mg.st 95', f'scoreboard players set $pz mg.st {Z}',
                 'clear @a[tag=mg.play]', 'gamemode adventure @a[tag=mg.play]', 'tag @a[tag=mg.play] add mg.phx',
                 # rôles : 1 chercheur pour 4 joueurs (au moins 1)
                 'execute store result score $phn mg.st if entity @a[tag=mg.play]', 'scoreboard players set #4 mg.st 4',
                 'scoreboard players operation $phn mg.st /= #4 mg.st', 'execute if score $phn mg.st matches ..0 run scoreboard players set $phn mg.st 1',
                 'execute if score $n0 mg.st matches 2.. run function mg:ph/pick', 'execute as @a[tag=mg.play,tag=!mg.phs] run tag @s add mg.phh',
                 'team join mg_red @a[tag=mg.phs]', 'team join mg_ph @a[tag=mg.phh]',
                 f'tp @a[tag=mg.phs] 0.5 89 {Z}.5', 'execute as @a[tag=mg.phs] at @s run spawnpoint @s ~ ~ ~',
                 f'spreadplayers 0 {Z} 2 13 under 85 false @a[tag=mg.phh]', 'execute as @a[tag=mg.phh] at @s run spawnpoint @s ~ ~ ~'])
w('ph/pick', ['execute as @a[tag=mg.play,tag=!mg.phs,sort=random,limit=1] run tag @s add mg.phs',
              'scoreboard players remove $phn mg.st 1', 'execute if score $phn mg.st matches 1.. run function mg:ph/pick'])
w('ph/kill_all', ['kill @e[tag=mg.phd]', 'kill @e[tag=mg.phi]'])
w('ph/go', ['# Départ : 30 s pour se cacher', 'scoreboard players set $pht mg.st 0', 'scoreboard players set $phc mg.st 0', 'scoreboard players set @a mg.deaths 0',
            'execute as @a[tag=mg.phh] run function mg:ph/become_prop', 'execute as @a[tag=mg.phs] run function mg:ph/seeker_kit',
            'effect give @a[tag=mg.phs] minecraft:blindness 31 0 true',
            'tellraw @a[tag=mg.phh] ' + js([{'text': '🎭 PROP HUNT — tu te caches ! ', 'color': 'gold', 'bold': True},
                                            {'text': 'Regarde un objet du manoir et ACCROUPIS-TOI pour en prendre l\'apparence. Reste immobile 2 s pour te caler sur la grille. Les chercheurs arrivent dans 30 s ; toutes les 20 s tu fais un petit bruit, et ta corne (clic droit) en fait un quand tu veux. Attention : 5 cœurs seulement !', 'color': 'gray'}]),
            # seul : entraînement, pas de victoire
            'execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] ' + js([{'text': "🎭 Mode entraînement (seul) : tu es cacheur, essaie les déguisements (accroupi devant un objet) et le calage sur la grille. Pas de victoire ; il faut au moins 2 joueurs pour une vraie partie.", 'color': 'yellow'}]),
            'tellraw @a[tag=mg.phs] ' + js([{'text': '🎭 PROP HUNT — tu cherches ! ', 'color': 'red', 'bold': True},
                                            {'text': 'Les cacheurs se transforment en objets du manoir. Tu es libéré dans 30 s : frappe les objets suspects, écoute les bruits !', 'color': 'gray'}])])
w('ph/become_prop', ['# @s devient cacheur : invisible, petit, un objet au hasard',
                     'clear @s', 'scoreboard players add $phc mg.st 1', 'scoreboard players operation @s mg.pid = $phc mg.st',
                     'effect give @s minecraft:invisibility infinite 0 true', 'effect give @s minecraft:saturation infinite 0 true',
                     'attribute @s minecraft:scale base set 0.5',
                     '# Cacheur fragile : 5 cœurs (2 coups d\'épée de chercheur)',
                     'attribute @s minecraft:max_health base set 10', 'effect give @s minecraft:instant_health 1 0 true',
                     'item replace entity @s hotbar.0 with minecraft:goat_horn[instrument="minecraft:ponder_goat_horn",custom_name={"text":"📯 Faire du bruit","color":"gold","italic":false},lore=[{"text":"Clic droit : un bruit pour narguer les chercheurs","color":"gray","italic":false}]]',
                     'execute store result score @s mg.php run random value 1..' + str(len(PROPS)),
                     'execute at @s run summon minecraft:block_display ~ ~ ~ {Tags:["mg.phd","mg.phnew"],teleport_duration:1,block_state:{Name:"minecraft:barrel"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.5f,0f,-0.5f],scale:[1f,1f,1f]}}',
                     'execute at @s run summon minecraft:interaction ~ ~ ~ {Tags:["mg.phi","mg.phnew"],width:1.02f,height:1.02f}',
                     'scoreboard players operation @e[tag=mg.phnew] mg.pid = @s mg.pid', 'tag @e[tag=mg.phnew] remove mg.phnew',
                     'function mg:ph/apply'])
A = ['# @s (cacheur) : met l\'apparence de son objet ($php) sur son block_display',
     'scoreboard players operation $pid mg.st = @s mg.pid', 'scoreboard players operation $pp mg.st = @s mg.php']
for p, i in PID.items():
    st = '{Name:"minecraft:oak_leaves",Properties:{persistent:"true"}}' if p == 'oak_leaves' else f'{{Name:"minecraft:{p}"}}'
    A.append(f'execute if score $pp mg.st matches {i} as @e[type=minecraft:block_display,tag=mg.phd] if score @s mg.pid = $pid mg.st run data modify entity @s block_state set value {st}')
for p, i in PID.items():
    A.append(f'execute if score $pp mg.st matches {i} run title @s actionbar [{{"text":"🎭 Tu es : ","color":"gold"}},{{"translate":"block.minecraft.{p}","color":"yellow","bold":true}}]')
w('ph/apply', A)
w('ph/srevive', ['# @s (entraînement, seul) : cacheur réapparu après sa mort → retrouve son déguisement', 'scoreboard players set @s mg.deaths 0',
                 'effect give @s minecraft:invisibility infinite 0 true', 'effect give @s minecraft:saturation infinite 0 true',
                 'attribute @s minecraft:scale base set 0.5', 'attribute @s minecraft:max_health base set 10', 'function mg:ph/apply'])
w('ph/copy', ['# @s (cacheur) s\'accroupit : copie l\'objet qu\'il regarde (5 blocs max)', 'scoreboard players set $phf mg.st 0',
              'scoreboard players set $phr mg.st 25', 'execute at @s anchored eyes positioned ^ ^ ^0.2 run function mg:ph/copy_ray',
              'execute if score $phf mg.st matches 0 run title @s actionbar {"text":"Regarde un objet du manoir (tonneau, citrouille, enclume…)","color":"gray"}',
              'execute if score $phf mg.st matches 1 run function mg:ph/apply',
              'execute if score $phf mg.st matches 1 at @s run playsound minecraft:entity.illusioner.mirror_move player @s ~ ~ ~ 0.6 1.4',
              'execute if score $phf mg.st matches 1 at @s run particle minecraft:poof ~ ~0.5 ~ 0.3 0.3 0.3 0.02 8'])
CR = ['# Un pas (0,2 bloc) du regard du cacheur', 'execute if block ~ ~ ~ #mg:ray_pass run scoreboard players remove $phr mg.st 1',
      'execute if block ~ ~ ~ #mg:ray_pass if score $phr mg.st matches 1.. positioned ^ ^ ^0.2 run return run function mg:ph/copy_ray']
for p, i in PID.items():
    CR.append(f'execute if block ~ ~ ~ minecraft:{p} run return run function mg:ph/got {{p:{i}}}')
w('ph/copy_ray', CR)
w('ph/got', ['$scoreboard players set @s mg.php $(p)', 'scoreboard players set $phf mg.st 1'])
w('ph/follow', ['# @s (cacheur) : son objet le suit ; immobile 2 s → calé sur la grille',
                'scoreboard players operation $pid mg.st = @s mg.pid',
                'execute store result score @s mg.tx run data get entity @s Pos[0] 20', 'execute store result score @s mg.tz run data get entity @s Pos[2] 20',
                'execute if score @s mg.tx = @s mg.phx if score @s mg.tz = @s mg.phz run scoreboard players add @s mg.phs 1',
                'execute unless score @s mg.tx = @s mg.phx run scoreboard players set @s mg.phs 0',
                'execute unless score @s mg.tz = @s mg.phz run scoreboard players set @s mg.phs 0',
                'scoreboard players operation @s mg.phx = @s mg.tx', 'scoreboard players operation @s mg.phz = @s mg.tz',
                'execute if score @s mg.phs matches ..39 as @e[tag=mg.phd] if score @s mg.pid = $pid mg.st run tp @s ~ ~ ~ 0 0',
                'execute if score @s mg.phs matches ..39 as @e[tag=mg.phi] if score @s mg.pid = $pid mg.st run tp @s ~ ~-0.01 ~',
                'execute if score @s mg.phs matches 40 align xyz positioned ~0.5 ~ ~0.5 as @e[tag=mg.phd] if score @s mg.pid = $pid mg.st run tp @s ~ ~ ~ 0 0',
                'execute if score @s mg.phs matches 40 align xyz positioned ~0.5 ~ ~0.5 as @e[tag=mg.phi] if score @s mg.pid = $pid mg.st run tp @s ~ ~-0.01 ~',
                'execute if score @s mg.phs matches 40 run title @s actionbar {"text":"🔒 Verrouillé sur la grille","color":"green"}',
                'execute if score @s mg.phs matches 41.. run scoreboard players set @s mg.phs 41'])
w('ph/hit_prop', ['# @s = interaction frappée : le cacheur lié prend un coup (si c\'est un chercheur)',
                  'execute on attacker if entity @s[tag=mg.phs] run tag @s add mg.phatk', 'data remove entity @s attack',
                  'scoreboard players operation $pid mg.st = @s mg.pid',
                  'execute if entity @a[tag=mg.phatk] as @a[tag=mg.phh] if score @s mg.pid = $pid mg.st run damage @s 5 minecraft:player_attack by @a[tag=mg.phatk,limit=1]',
                  'tag @a remove mg.phatk'])
w('ph/seeker_kit', ['# @s : chercheur', 'clear @s', 'effect clear @s minecraft:invisibility', 'attribute @s minecraft:scale base set 1',
                    'attribute @s minecraft:max_health base set 20', 'effect give @s minecraft:instant_health 1 4 true',
                    'item replace entity @s hotbar.0 with minecraft:iron_sword[unbreakable={}]',
                    'item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=16711680,unbreakable={}]',
                    'item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=16711680,unbreakable={}]',
                    'effect give @s minecraft:saturation infinite 0 true', 'effect give @s minecraft:speed infinite 0 true'])
w('ph/release', ['# Fin de la cachette : les chercheurs entrent', 'effect clear @a[tag=mg.phs] minecraft:blindness',
                 f'spreadplayers 0 {Z} 1 4 under 85 false @a[tag=mg.phs]', 'execute as @a[tag=mg.phs] at @s run spawnpoint @s ~ ~ ~',
                 'title @a[tag=mg.play] title {"text":"Les chercheurs arrivent !","color":"red","bold":true}',
                 'execute as @a[tag=mg.play] at @s run playsound minecraft:entity.wolf.howl master @s ~ ~ ~ 0.7 1'])
w('ph/taunt', ['# Toutes les 20 s : chaque cacheur fait un petit bruit',
               'execute as @a[tag=mg.phh] at @s run function mg:ph/taunt_one'])
w('ph/taunt_one', ['execute store result score $phq mg.st run random value 0..3',
                   'execute if score $phq mg.st matches 0 run playsound minecraft:entity.cat.ambient player @a ~ ~ ~ 1.2 1.2',
                   'execute if score $phq mg.st matches 1 run playsound minecraft:entity.chicken.ambient player @a ~ ~ ~ 1.2 1',
                   'execute if score $phq mg.st matches 2 run playsound minecraft:entity.villager.ambient player @a ~ ~ ~ 1.2 1.3',
                   'execute if score $phq mg.st matches 3 run playsound minecraft:block.note_block.bell player @a ~ ~ ~ 1.2 1.8',
                   'particle minecraft:note ~ ~1 ~ 0.2 0.2 0.2 1 2'])
w('ph/found', ['# @s (cacheur) trouvé : devient chercheur', 'scoreboard players set @s mg.deaths 0',
               'scoreboard players operation $pid mg.st = @s mg.pid',
               'execute as @e[tag=mg.phd] if score @s mg.pid = $pid mg.st run kill @s',
               'execute as @e[tag=mg.phi] if score @s mg.pid = $pid mg.st run kill @s',
               'tag @s remove mg.phh', 'tag @s add mg.phs', 'team join mg_red @s', 'function mg:ph/seeker_kit',
               f'spreadplayers 0 {Z} 1 4 under 85 false @s',
               'tellraw @a[tag=mg.play] [{"text":"🎭 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a été trouvé et rejoint les chercheurs !","color":"gray"}]',
               'execute as @a[tag=mg.play] at @s run playsound minecraft:entity.item.break master @s ~ ~ ~ 0.8 0.7'])
w('ph/tick', ['# 🎭 Prop Hunt — tick', 'scoreboard players add $pht mg.st 1',
              f'execute if score $pht mg.st matches ..{HIDE - 1} run tp @a[tag=mg.phs] 0.5 89 {Z}.5',
              f'execute if score $pht mg.st matches {HIDE} run function mg:ph/release',
              # copie d'objet (accroupi), suivi, coups sur les objets
              'execute as @a[tag=mg.phh,scores={mg.gsn=1..},tag=!mg.phsn] run function mg:ph/copy',
              'tag @a[tag=mg.phh,scores={mg.gsn=1..}] add mg.phsn', 'tag @a[tag=mg.phsn,scores={mg.gsn=0}] remove mg.phsn',
              'tag @a[tag=mg.phsn] remove mg.phsn' if False else 'execute as @a[tag=mg.phsn] unless score @s mg.gsn matches 1.. run tag @s remove mg.phsn',
              'scoreboard players set @a[tag=mg.phx] mg.gsn 0',
              'execute as @a[tag=mg.phh] at @s run function mg:ph/follow',
              'execute as @a[tag=mg.phh,scores={mg.phn=1..}] at @s run function mg:ph/taunt_one',
              'scoreboard players reset @a[scores={mg.phn=1..}] mg.phn',
              'execute as @e[type=minecraft:interaction,tag=mg.phi] if data entity @s attack run function mg:ph/hit_prop',
              'execute if score $n0 mg.st matches 2.. as @a[tag=mg.phh,scores={mg.deaths=1..}] run function mg:ph/found',
              # seul : le cacheur reste cacheur
              'execute unless score $n0 mg.st matches 2.. as @e[type=minecraft:player,tag=mg.phh,scores={mg.deaths=1..}] run function mg:ph/srevive',
              'execute as @a[tag=mg.phs,scores={mg.deaths=1..}] run scoreboard players set @s mg.deaths 0',
              'scoreboard players operation $phq mg.st = $pht mg.st', 'scoreboard players set #400 mg.st 400', 'scoreboard players operation $phq mg.st %= #400 mg.st',
              f'execute if score $pht mg.st matches {HIDE + 1}.. if score $phq mg.st matches 0 run function mg:ph/taunt',
              'scoreboard players operation $phq mg.st = $pht mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $phq mg.st %= #20 mg.st',
              'execute if score $phq mg.st matches 0 run function mg:ph/second',
              'execute store result score $phh mg.st if entity @a[tag=mg.play,tag=mg.phh]',
              'execute store result score $phk mg.st if entity @a[tag=mg.play,tag=mg.phs]',
              'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $phh mg.st matches 0 run return run function mg:ph/seekers_win',
              'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $phk mg.st matches 0 run return run function mg:ph/hiders_win',
              f'execute if score $state mg.st matches 2 if score $pht mg.st matches {HIDE + HUNT}.. run function mg:ph/hiders_win'])
w('ph/second', [f'scoreboard players set $phl mg.st {(HIDE + HUNT) // 20}', 'scoreboard players operation $phs2 mg.st = $pht mg.st',
                'scoreboard players operation $phs2 mg.st /= #20 mg.st', 'scoreboard players operation $phl mg.st -= $phs2 mg.st',
                # seul : chrono restant
                'execute unless score $n0 mg.st matches 2.. run title @a[tag=mg.play] actionbar [{"text":"🎭 Entraînement : ","color":"yellow"},{"score":{"name":"$phl","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"gray"}]',
                f'execute if score $pht mg.st matches ..{HIDE} run title @a[tag=mg.phs] actionbar [{{"text":"🎭 Les cacheurs se cachent… ","color":"gray"}},{{"score":{{"name":"$phl","objective":"mg.st"}},"color":"yellow"}}]',
                f'execute if score $pht mg.st matches {HIDE + 1}.. run title @a[tag=mg.phs] actionbar [{{"text":"🎭 Cacheurs restants : ","color":"red"}},{{"score":{{"name":"$phh","objective":"mg.st"}},"color":"yellow","bold":true}},{{"text":" — ","color":"gray"}},{{"score":{{"name":"$phl","objective":"mg.st"}},"color":"yellow"}},{{"text":" s","color":"gray"}}]'])
w('ph/hiders_win', ['# Les cacheurs gagnent',
                    'execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] ' + js([{'text': "🎭 Fin de l'entraînement.", 'color': 'yellow'}]),
                    'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
                    'tag @a[tag=mg.play,tag=mg.phh] add mg.win', 'scoreboard players add @a[tag=mg.play,tag=mg.phh] mg.wins 1',
                    'scoreboard players set $state mg.st 3', 'scoreboard players set $timer mg.st 120',
                    'title @a[tag=!mg.surv] title {"text":"Les CACHEURS gagnent !","color":"gold","bold":true}',
                    'tellraw @a [{"text":"★ Victoire des cacheurs : ","color":"gold"},{"selector":"@a[tag=mg.play,tag=mg.phh]","color":"yellow"}]',
                    'execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1'])
w('ph/seekers_win', ['# Plus aucun cacheur', 'tellraw @a {"text":"🎭 Tous les cacheurs ont été trouvés !","color":"red","bold":true}', 'function mg:core/win_red'])
w('ph/cleanup', ['function mg:ph/kill_all', 'execute as @a[tag=mg.phx] run attribute @s minecraft:scale base set 1',
                 'execute as @a[tag=mg.phx] run attribute @s minecraft:max_health base set 20',
                 'effect clear @a[tag=mg.phx] minecraft:invisibility', 'effect clear @a[tag=mg.phx] minecraft:speed',
                 'effect clear @a[tag=mg.phx] minecraft:blindness', 'team leave @a[team=mg_ph]',
                 'tag @a remove mg.phh', 'tag @a remove mg.phs', 'tag @a remove mg.phsn', 'tag @a remove mg.phx'])

C.register([96], 'ph', [C.announce(96, '', '🎭 PROP HUNT', 'gold', 'cachez-vous en objets, les chercheurs arrivent dans 30 s !')])
C.objectives([('mg.phn', 'minecraft.used:minecraft.goat_horn'), ('mg.pid', 'dummy'), ('mg.php', 'dummy'), ('mg.phx', 'dummy'), ('mg.phz', 'dummy'), ('mg.phs', 'dummy')])
C.patch('core/load', 'scoreboard objectives add mg.bw trigger', ['team add mg_ph', 'team modify mg_ph nametagVisibility never',
                                                                 'team modify mg_ph friendlyFire false', 'team modify mg_ph collisionRule never',
                                                                 'scoreboard players set #4 mg.st 4'])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw', ['team remove mg_ph'])
C.forceload([f'# Prop Hunt (z {Z})', f'forceload add -23 {Z - 18} 23 {Z + 18}'])
print('Prop Hunt OK')
