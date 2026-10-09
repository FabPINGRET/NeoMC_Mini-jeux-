"""🧟 Zombies façon Call of Duty (id 97) et 🧪 Infection (id 98). Même carte : bunker de 4 salles en z 23200.

    python tools/arcade/gen_zombies.py .

Zombies (97) : coop contre des manches de zombies de plus en plus nombreux et résistants. Armes réelles (tools/arcade/guns.py),
points (+10 par balle qui touche, +60 par kill), portes à acheter, armes au mur, boîte mystère, Juggernog, Speed Cola.
Mort → spectateur jusqu'à la fin de la manche (réanimé avec pistolet). 10 manches = victoire, tout le monde mort = défaite.
Infection (98) : un ou plusieurs joueurs commencent zombies ; un survivant tué devient zombie. Survivants armés,
zombies au corps à corps (plus rapides et plus forts), réapparition infinie. 3 min : les survivants restants gagnent.
Seul : mode entraînement (pas de victoire, fin au chrono ou menu → Arrêter).
"""
import json
import os
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
import guns as G

w, js = C.w, C.js
Z = C.param('Z', 23200)
THEME = C.param('blocks', {})     # carte supplémentaire : remplacement des blocs du décor (tools/arcade/gen_maps.py)
NAME = C.param('name', 'Bunker')
ROUNDS = 10
G.build()

ROOMS = {'a': (-10, 10, Z - 10, Z + 10), 'b': (-10, 10, Z - 32, Z - 12), 'c': (12, 32, Z - 10, Z + 10), 'd': (12, 32, Z - 32, Z - 12)}
# portes : id → (nom, coût, (x1,z1,x2,z2) du barrage, position interaction, salle ouverte)
DOORS = {1: ('A → B', 750, (-1, Z - 11, 1, Z - 11), (0.5, Z - 10.5), 'b'),
         2: ('A → C', 750, (11, Z - 1, 11, Z + 1), (11.5, Z + 0.5), 'c'),
         3: ('B → D', 1000, (11, Z - 23, 11, Z - 21), (11.5, Z - 21.5), 'd'),
         4: ('C → D', 1000, (21, Z - 11, 23, Z - 11), (22.5, Z - 10.5), 'd')}
# fenêtres (salle, x, z, normale vers l'extérieur)
WIN = [('a', -11, Z + 4, -1, 0), ('a', 0, Z + 11, 0, 1), ('b', -11, Z - 22, -1, 0), ('b', 0, Z - 33, 0, -1),
       ('c', 33, Z + 4, 1, 0), ('c', 22, Z + 11, 0, 1), ('d', 33, Z - 22, 1, 0), ('d', 22, Z - 33, 0, -1)]
# achats au mur : tag, nom, coût, position interaction (x, z), arme (0 = autre), position (arme collée à la face du mur, côté salle ; suppose un modèle plat handheld/generated) et orientation de l'affichage
WALL = [('zb11', 'Fusil M14', 500, (-9.5, Z + 6.5), 4, (-9.95, Z + 6.5), 90),
        ('zb12', 'Fusil à pompe', 500, (10.5, Z + 6.5), 3, (10.95, Z + 6.5), -90),
        ('zb13', 'Mitraillette', 1000, (-9.5, Z - 15.5), 2, (-9.95, Z - 15.5), 90)]

# ------------------------------------------------------------------ carte
L = ['# 🧟 Bunker (Zombies / Infection) — 4 salles 21×21, x −11..33, z 23167..23211, sol y 80, toit y 86']
L += [f'fill -17 {y} {Z - 39} 39 {y} {Z + 17} minecraft:air' for y in range(78, 92)]
L += [f'fill -11 79 {Z - 33} 33 79 {Z + 11} minecraft:stone']
for r, (x1, x2, z1, z2) in ROOMS.items():
    L.append(f'fill {x1} 80 {z1} {x2} 80 {z2} minecraft:{ {"a": "polished_andesite", "b": "stone_bricks", "c": "polished_deepslate", "d": "mossy_stone_bricks"}[r] }')
L += [f'fill -11 80 {Z - 33} 33 85 {Z - 33} minecraft:stone_bricks', f'fill -11 80 {Z + 11} 33 85 {Z + 11} minecraft:stone_bricks',
      f'fill -11 80 {Z - 32} -11 85 {Z + 10} minecraft:stone_bricks', f'fill 33 80 {Z - 32} 33 85 {Z + 10} minecraft:stone_bricks',
      f'fill 11 80 {Z - 32} 11 85 {Z + 10} minecraft:stone_bricks', f'fill -10 80 {Z - 11} 32 85 {Z - 11} minecraft:stone_bricks',
      f'fill -11 86 {Z - 33} 33 86 {Z + 11} minecraft:smooth_stone',
      f'fill -11 81 {Z - 33} 33 81 {Z + 11} minecraft:cracked_stone_bricks replace minecraft:stone_bricks']
L += [f'setblock {x} 86 {z} minecraft:sea_lantern' for x in range(-6, 33, 6) for z in range(Z - 30, Z + 11, 6)]
# portes : ouverture 3×3 + barricade en planches
for d, (nm, cost, (x1, z1, x2, z2), _, _) in DOORS.items():
    L.append(f'fill {x1} 81 {z1} {x2} 83 {z2} minecraft:dark_oak_planks')
# fenêtres + enclos d'apparition
for (r, x, z, nx, nz) in WIN:
    px, pz = (0, 1) if nx else (1, 0)          # axe perpendiculaire
    def P(d, p):
        return x + nx * d + px * p, z + nz * d + pz * p
    ax, az = P(1, -2); bx, bz = P(4, 2)
    L.append(f'fill {min(ax, bx)} 80 {min(az, bz)} {max(ax, bx)} 84 {max(az, bz)} minecraft:stone_bricks')
    ax, az = P(1, -1); bx, bz = P(3, 1)
    L.append(f'fill {min(ax, bx)} 81 {min(az, bz)} {max(ax, bx)} 83 {max(az, bz)} minecraft:air')
    L.append(f'fill {x} 81 {z} {x} 82 {z} minecraft:air')
    L.append(f'fill {x - px} 83 {z - pz} {x + px} 83 {z + pz} minecraft:iron_bars')
# décor : caisses, tables, éclairage
for (x, z) in [(-6, Z - 6), (5, Z + 4), (-5, Z - 26), (6, Z - 19), (17, Z - 5), (27, Z + 2), (16, Z - 29), (27, Z - 20)]:
    L += [f'fill {x} 81 {z} {x + 1} 81 {z + 1} minecraft:barrel[facing=up]', f'setblock {x} 82 {z} minecraft:barrel[facing=up]']
for (x, z) in [(3, Z - 3), (-3, Z - 20), (20, Z + 3), (24, Z - 24)]:
    L += [f'fill {x} 81 {z} {x + 2} 81 {z} minecraft:spruce_slab[type=top]', f'setblock {x + 1} 82 {z} minecraft:lantern']
# machines : Juggernog (rouge), Speed Cola (vert), boîte mystère
L += [f'setblock 32 81 {Z + 6} minecraft:red_glazed_terracotta', f'setblock 32 82 {Z + 6} minecraft:red_stained_glass',
      f'setblock 32 83 {Z + 6} minecraft:redstone_lamp[lit=true]',
      f'setblock 32 81 {Z - 15} minecraft:lime_glazed_terracotta', f'setblock 32 82 {Z - 15} minecraft:lime_stained_glass',
      f'setblock 32 83 {Z - 15} minecraft:redstone_lamp[lit=true]',
      f'setblock 22 81 {Z - 27} minecraft:chest[facing=south]', f'setblock 21 81 {Z - 27} minecraft:spruce_planks',
      f'setblock 23 81 {Z - 27} minecraft:spruce_planks', f'setblock 22 85 {Z - 27} minecraft:soul_lantern[hanging=true]']
import re
L = [re.sub(r'minecraft:([a-z_]+)', lambda m: 'minecraft:' + THEME.get(m.group(1), m.group(1)), l) for l in L]
L[0] = L[0].replace('Bunker', NAME)
w('zm/build', L)

# entités : portes, achats, apparitions
E = ['# Entités du bunker (portes, achats, apparitions) — tag mg.zent', 'kill @e[tag=mg.zent]']
for (r, x, z, nx, nz) in WIN:
    E.append(f'summon minecraft:marker {x + nx * 2 + .5} 81 {z + nz * 2 + .5} {{Tags:["mg.zent","mg.zsp","mg.zr_{r}"]}}')
for d, (nm, cost, (x1, z1, x2, z2), (ix, iz), room) in DOORS.items():
    ox, oz = (0, 1.5) if z1 == z2 else (1.5, 0)    # une étiquette sur chaque face du mur (décalage perpendiculaire au mur)
    txt = f'[{{"text":"🚪 Porte {nm}","color":"gold","bold":true}},{{"text":"\\nclic droit — {cost} pts","color":"yellow"}}]'
    E += [f'summon minecraft:interaction {ix} 81 {iz} {{Tags:["mg.zent","mg.zbuy","mg.zb{d}","mg.zd{d}"],width:3.4f,height:3f,response:1b}}',
          *[f'summon minecraft:text_display {ix + s * ox} 84.3 {iz + s * oz} {{Tags:["mg.zent","mg.zd{d}"],billboard:"center",text:{txt}}}' for s in (-1, 1)]]
for tag, nm, cost, (ix, iz), gn, (dx, dz), rot in WALL:
    E += [f'summon minecraft:interaction {ix} 81 {iz} {{Tags:["mg.zent","mg.zbuy","mg.{tag}"],width:1.3f,height:2.4f,response:1b}}',
          f'summon minecraft:text_display {round(dx + (0.95 if rot == 90 else -0.95), 2)} 83.3 {dz} {{Tags:["mg.zent"],billboard:"center",text:[{{"text":"🔫 {nm}","color":"aqua","bold":true}},{{"text":"\\n{cost} pts","color":"yellow"}}]}}',
          f'execute if score $rp mg.st matches 1 run summon minecraft:item_display {dx} 82.4 {dz} {{Tags:["mg.zent"],Rotation:[{rot}f,0f],item:{{id:"minecraft:warped_fungus_on_a_stick",count:1,components:{{"minecraft:item_model":"mg:gun_{G.GUNS[gn][1]}"}}}},transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}}}',
          f'execute unless score $rp mg.st matches 1 run summon minecraft:item_display {dx} 82.4 {dz} {{Tags:["mg.zent"],Rotation:[{rot}f,0f],item:{{id:"minecraft:crossbow",count:1}},transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}}}']
E += [f'summon minecraft:interaction 31.5 81 {Z + 6.5} {{Tags:["mg.zent","mg.zbuy","mg.zb21"],width:1.3f,height:2.4f,response:1b}}',
      f'summon minecraft:text_display 31.0 84.4 {Z + 6.5} {{Tags:["mg.zent"],billboard:"center",text:[{{"text":"❤ Juggernog","color":"red","bold":true}},{{"text":"\\n2× plus de vie — 2500 pts","color":"yellow"}}]}}',
      f'summon minecraft:interaction 31.5 81 {Z - 14.5} {{Tags:["mg.zent","mg.zbuy","mg.zb22"],width:1.3f,height:2.4f,response:1b}}',
      f'summon minecraft:text_display 31.0 84.4 {Z - 14.5} {{Tags:["mg.zent"],billboard:"center",text:[{{"text":"⚡ Speed Cola","color":"green","bold":true}},{{"text":"\\nrecharge 2× plus vite — 3000 pts","color":"yellow"}}]}}',
      f'summon minecraft:interaction 22.5 81 {Z - 26.5} {{Tags:["mg.zent","mg.zbuy","mg.zb20"],width:1.6f,height:1.6f,response:1b}}',
      f'summon minecraft:text_display 22.5 83.4 {Z - 26.5} {{Tags:["mg.zent"],billboard:"center",text:[{{"text":"❓ Boîte mystère","color":"light_purple","bold":true}},{{"text":"\\narme au hasard — 950 pts","color":"yellow"}}]}}',
      'tag @e[tag=mg.zr_a] add mg.zon']
w('zm/entities', E)
w('zm/open_all', ['# Infection : toutes les portes ouvertes, pas d\'achats'] +
  [f'fill {x1} 81 {z1} {x2} 83 {z2} minecraft:air' for d, (_, _, (x1, z1, x2, z2), _, _) in DOORS.items()] +
  ['kill @e[tag=mg.zbuy]', 'kill @e[type=minecraft:text_display,tag=mg.zent]', 'kill @e[type=minecraft:item_display,tag=mg.zent]',
   'tag @e[tag=mg.zsp] add mg.zon'])
w('zm/kill_all', ['kill @e[tag=mg.zz]', 'kill @e[tag=mg.zent]',
                  f'kill @e[type=minecraft:item,x=-17,y=70,z={Z - 39},dx=56,dy=25,dz=56]',
                  f'kill @e[type=minecraft:experience_orb,x=-17,y=70,z={Z - 39},dx=56,dy=25,dz=56]'])

# ------------------------------------------------------------------ commun (dispatch 97 / 98)
w('zmode/prepare', ['execute if score $game mg.st matches 97 run function mg:zm/prepare', 'execute if score $game mg.st matches 98 run function mg:inf/prepare'])
w('zmode/go', ['execute if score $game mg.st matches 97 run function mg:zm/go', 'execute if score $game mg.st matches 98 run function mg:inf/go'])
w('zmode/tick', ['function mg:gun/tick', 'execute if score $game mg.st matches 97 run function mg:zm/tick', 'execute if score $game mg.st matches 98 run function mg:inf/tick'])
w('zmode/cleanup', ['scoreboard players set $zpts mg.st 0', 'function mg:zm/kill_all', 'execute as @a[tag=mg.zjug] run attribute @s minecraft:max_health base set 20',
                    'tag @a remove mg.zjug', 'tag @a remove mg.zsc', 'tag @a remove mg.zdead', 'tag @a remove mg.inf', 'tag @a remove mg.gtg',
                    'execute as @a run function mg:gun/reset', 'team leave @a[team=mg_green]',
                    'effect clear @a[tag=mg.play] minecraft:speed', 'effect clear @a[tag=mg.play] minecraft:strength',
                    'scoreboard players reset * mg.zpt'])

# ------------------------------------------------------------------ ZOMBIES
w('zm/prepare', ['# 🧟 Zombies — préparation', 'function mg:zm/build', 'function mg:zm/kill_all', 'function mg:zm/entities',
                 'scoreboard players set $px mg.st 0', 'scoreboard players set $py mg.st 84', f'scoreboard players set $pz mg.st {Z}',
                 'clear @a[tag=mg.play]', 'gamemode adventure @a[tag=mg.play]', 'team join mg_blue @a[tag=mg.play]',
                 f'spreadplayers 0 {Z} 2 6 under 84 false @a[tag=mg.play]', 'execute as @a[tag=mg.play] at @s run spawnpoint @s ~ ~ ~'])
w('zm/kit', ['# @s : couteau + pistolet', 'clear @s', 'function mg:gun/reset',
             'item replace entity @s hotbar.0 with minecraft:iron_sword[unbreakable={},custom_name=[{"text":"🔪 Couteau","color":"gray","italic":false}]]',
             G.give(1, 'hotbar.1'), 'item replace entity @s hotbar.8 with minecraft:cooked_beef 8',
             'effect give @s minecraft:saturation infinite 0 true'])
w('zm/go', ['# Départ', 'scoreboard players set $zpts mg.st 1', 'scoreboard players set $zr mg.st 0', 'scoreboard players set $zph mg.st 0', 'scoreboard players set $zb mg.st 100',
            'scoreboard players set #2 mg.st 2', 'scoreboard players set @a[tag=mg.play] mg.zpt 500', 'scoreboard players reset @a mg.zk',
            'scoreboard objectives setdisplay sidebar mg.zpt', 'scoreboard players set @a mg.deaths 0',
            'execute as @a[tag=mg.play] run function mg:zm/kit',
            'tellraw @a[tag=mg.play] ' + js([{'text': '🧟 ZOMBIES : ', 'color': 'dark_green', 'bold': True},
                                             {'text': f'survivez à {ROUNDS} manches ! Clic droit = tirer, accroupi = recharger. Chaque balle qui touche = 10 pts, chaque kill = 60 pts. Clic droit sur les portes, armes au mur, boîte mystère et boissons pour les acheter. Un joueur mort revient à la manche suivante.', 'color': 'gray'}])])
w('zm/tick', ['# 🧟 Zombies — tick',
              'execute as @a[tag=mg.play,tag=!mg.zdead,scores={mg.deaths=1..}] run function mg:zm/die',
              'execute as @a[tag=mg.play,scores={mg.zk=1..}] run function mg:zm/kill_points',
              'execute as @e[type=minecraft:interaction,tag=mg.zbuy] if data entity @s interaction run function mg:zm/buy',
              'execute if score $zph mg.st matches 0 run function mg:zm/break_tick',
              'execute if score $zph mg.st matches 1 run function mg:zm/round_tick',
              'scoreboard players add $zt mg.st 1', 'scoreboard players operation $zq mg.st = $zt mg.st', 'scoreboard players set #20 mg.st 20',
              'scoreboard players operation $zq mg.st %= #20 mg.st', 'execute if score $zq mg.st matches 0 run function mg:zm/second',
              'execute if score $state mg.st matches 2 unless entity @a[tag=mg.play,tag=!mg.zdead] run function mg:zm/defeat'])
w('zm/kill_points', ['scoreboard players operation $zk mg.st = @s mg.zk', 'scoreboard players set #60 mg.st 60',
                     'scoreboard players operation $zk mg.st *= #60 mg.st', 'scoreboard players operation @s mg.zpt += $zk mg.st',
                     'scoreboard players reset @s mg.zk'])
w('zm/break_tick', ['scoreboard players remove $zb mg.st 1', 'execute if score $zb mg.st matches ..0 run function mg:zm/round_start'])
w('zm/round_start', ['# Nouvelle manche : nombre, vie et vitesse des zombies', 'scoreboard players add $zr mg.st 1',
                     'scoreboard players set $zph mg.st 1', 'scoreboard players set $zsc mg.st 0',
                     # nombre = (4 + 3r) × (n + 1) / 2, max 60
                     'scoreboard players operation $zleft mg.st = $zr mg.st', 'scoreboard players set #3 mg.st 3',
                     'scoreboard players operation $zleft mg.st *= #3 mg.st', 'scoreboard players add $zleft mg.st 4',
                     'execute store result score $zn mg.st if entity @a[tag=mg.play]', 'scoreboard players add $zn mg.st 1',
                     'scoreboard players operation $zleft mg.st *= $zn mg.st', 'scoreboard players operation $zleft mg.st /= #2 mg.st',
                     'execute if score $zleft mg.st matches 61.. run scoreboard players set $zleft mg.st 60',
                     # vie = 16 + 8 (r − 1), max 150 ; vitesse 0,23 / 0,27 / 0,32 ; cadence d'apparition 22 − 2r (min 8)
                     'scoreboard players operation $zhp mg.st = $zr mg.st', 'scoreboard players set #8 mg.st 8',
                     'scoreboard players operation $zhp mg.st *= #8 mg.st', 'scoreboard players add $zhp mg.st 8',
                     'execute if score $zhp mg.st matches 151.. run scoreboard players set $zhp mg.st 150',
                     'scoreboard players set $zsp mg.st 23', 'execute if score $zr mg.st matches 4.. run scoreboard players set $zsp mg.st 27',
                     'execute if score $zr mg.st matches 7.. run scoreboard players set $zsp mg.st 32',
                     'scoreboard players operation $zsi mg.st = $zr mg.st', 'scoreboard players operation $zsi mg.st *= #2 mg.st',
                     'scoreboard players set $zsj mg.st 22', 'scoreboard players operation $zsj mg.st -= $zsi mg.st',
                     'execute if score $zsj mg.st matches ..7 run scoreboard players set $zsj mg.st 8',
                     'execute store result storage mg:zm hp int 1 run scoreboard players get $zhp mg.st',
                     'execute store result storage mg:zm sp double 0.01 run scoreboard players get $zsp mg.st',
                     'title @a[tag=mg.play] title [{"text":"Manche ","color":"dark_red","bold":true},{"score":{"name":"$zr","objective":"mg.st"},"color":"red","bold":true}]',
                     'title @a[tag=mg.play] subtitle [{"score":{"name":"$zleft","objective":"mg.st"},"color":"yellow"},{"text":" zombies","color":"gray"}]',
                     'execute as @a[tag=mg.play] at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.3 0.6'])
w('zm/round_tick', ['# Manche en cours : apparitions, fin de manche',
                    'scoreboard players add $zsc mg.st 1',
                    'execute store result score $zal mg.st if entity @e[type=minecraft:zombie,tag=mg.zz]',
                    'execute if score $zsc mg.st >= $zsj mg.st if score $zleft mg.st matches 1.. if score $zal mg.st matches ..23 run function mg:zm/spawn',
                    'execute if score $zleft mg.st matches ..0 if score $zal mg.st matches 0 run function mg:zm/round_end'])
w('zm/spawn', ['scoreboard players set $zsc mg.st 0', 'scoreboard players remove $zleft mg.st 1',
               'execute as @e[type=minecraft:marker,tag=mg.zsp,tag=mg.zon,sort=random,limit=1] at @s run function mg:zm/spawn_one with storage mg:zm'])
w('zm/spawn_one', ['# Un zombie (macro : $(hp) vie, $(sp) vitesse)',
                   '$summon minecraft:zombie ~ ~ ~ {Tags:["mg.zz","mg.gtg","mg.mob"],PersistenceRequired:1b,CanPickUpLoot:0b,IsBaby:0b,CanBreakDoors:0b,DeathLootTable:"minecraft:empty",Health:$(hp)f,attributes:[{id:"minecraft:max_health",base:$(hp)d},{id:"minecraft:follow_range",base:64d},{id:"minecraft:movement_speed",base:$(sp)d},{id:"minecraft:spawn_reinforcements",base:0d}]}',
                   'particle minecraft:large_smoke ~ ~1 ~ 0.3 0.5 0.3 0.02 10'])
w('zm/round_end', [f'# Manche terminée', f'execute if score $zr mg.st matches {ROUNDS}.. run return run function mg:zm/victory',
                   'scoreboard players set $zph mg.st 0', 'scoreboard players set $zb mg.st 200',
                   'tellraw @a[tag=mg.play] [{"text":"🧟 Manche ","color":"dark_green"},{"score":{"name":"$zr","objective":"mg.st"},"color":"green","bold":true},{"text":" terminée ! Prochaine dans 10 s.","color":"gray"}]',
                   'execute as @a[tag=mg.play,tag=mg.zdead] run function mg:zm/revive',
                   'execute as @a[tag=mg.play] at @s run playsound minecraft:block.bell.use master @s ~ ~ ~ 1 0.8'])
w('zm/die', ['# @s est tombé : spectateur jusqu\'à la fin de la manche, perd ses boissons', 'scoreboard players set @s mg.deaths 0',
             'tag @s add mg.zdead', 'gamemode spectator @s', f'tp @s 0 84 {Z}',
             'execute if entity @s[tag=mg.zjug] run attribute @s minecraft:max_health base set 20', 'tag @s remove mg.zjug', 'tag @s remove mg.zsc',
             'tellraw @a[tag=mg.play] [{"text":"☠ ","color":"red"},{"selector":"@s","color":"red"},{"text":" est tombé ! Il reviendra à la fin de la manche.","color":"gray"}]'])
w('zm/revive', ['# @s revient (pistolet + couteau)', 'tag @s remove mg.zdead', 'gamemode adventure @s',
                f'spreadplayers 0 {Z} 1 4 under 84 false @s', 'function mg:zm/kit', 'effect give @s minecraft:instant_health 1 4 true'])
w('zm/second', ['# Chaque seconde : zombies tombés hors de la carte ou perdus',
                'execute as @e[type=minecraft:zombie,tag=mg.zz] at @s if entity @s[y=-64,dy=139] run function mg:zm/lost',
                'execute as @e[type=minecraft:zombie,tag=mg.zz] at @s unless entity @a[tag=mg.play,tag=!mg.zdead,distance=..48] run function mg:zm/lost',
                'execute if score $zph mg.st matches 1 run title @a[tag=mg.play] actionbar [{"text":"🧟 Manche ","color":"dark_green"},{"score":{"name":"$zr","objective":"mg.st"},"color":"green","bold":true},{"text":" — restants : ","color":"gray"},{"score":{"name":"$zal","objective":"mg.st"},"color":"yellow"},{"text":" + ","color":"gray"},{"score":{"name":"$zleft","objective":"mg.st"},"color":"yellow"}]'])
w('zm/lost', ['# @s (zombie) perdu : réapparaît dans un enclos ouvert',
              'execute at @e[type=minecraft:marker,tag=mg.zsp,tag=mg.zon,sort=random,limit=1] run tp @s ~ ~ ~'])
w('zm/victory', ['# 10 manches !', 'kill @e[tag=mg.zz]', 'tag @a[tag=mg.play] add mg.win', 'scoreboard players add @a[tag=mg.play] mg.wins 1',
                 'scoreboard players set $state mg.st 3', 'scoreboard players set $timer mg.st 140',
                 'title @a[tag=!mg.surv] title {"text":"VICTOIRE !","color":"gold","bold":true}',
                 f'title @a[tag=!mg.surv] subtitle {{"text":"{ROUNDS} manches de zombies repoussées","color":"yellow"}}',
                 'tellraw @a {"text":"★ Le bunker a tenu — bravo aux survivants !","color":"gold"}',
                 'execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1'])
w('zm/defeat', ['# Tout le monde est tombé', 'kill @e[tag=mg.zz]', 'scoreboard players set $state mg.st 3', 'scoreboard players set $timer mg.st 80',
                'title @a[tag=!mg.surv] title {"text":"GAME OVER","color":"dark_red","bold":true}',
                'title @a[tag=!mg.surv] subtitle [{"text":"Tombés à la manche ","color":"gray"},{"score":{"name":"$zr","objective":"mg.st"},"color":"red","bold":true}]',
                'tellraw @a [{"text":"☠ Les zombies ont envahi le bunker à la manche ","color":"gray"},{"score":{"name":"$zr","objective":"mg.st"},"color":"red","bold":true}]',
                'execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.wither.death master @s ~ ~ ~ 0.5 0.8'])

# achats
B = ['# @s = interaction cliquée', 'execute on target run tag @s add mg.zbuyer', 'data remove entity @s interaction',
     'execute unless entity @a[tag=mg.zbuyer,tag=mg.play,tag=!mg.zdead] run return run tag @a remove mg.zbuyer']
for d, (nm, cost, *_ ) in DOORS.items():
    B.append(f'execute if entity @s[tag=mg.zb{d}] run scoreboard players set $zc mg.st {cost}')
    B.append(f'execute if entity @s[tag=mg.zb{d}] if function mg:zm/pay run function mg:zm/door_{d}')
for tag, nm, cost, _, gn, _, _ in WALL:
    B.append(f'execute if entity @s[tag=mg.{tag}] run scoreboard players set $zc mg.st {cost}')
    B.append(f'execute if entity @s[tag=mg.{tag}] if function mg:zm/pay run function mg:zm/buy_gun {{n:{gn}}}')
B += ['execute if entity @s[tag=mg.zb20] run scoreboard players set $zc mg.st 950',
      'execute if entity @s[tag=mg.zb20] if function mg:zm/pay run function mg:zm/box',
      'execute if entity @s[tag=mg.zb21] if entity @a[tag=mg.zbuyer,tag=mg.zjug] run return run function mg:zm/already',
      'execute if entity @s[tag=mg.zb21] run scoreboard players set $zc mg.st 2500',
      'execute if entity @s[tag=mg.zb21] if function mg:zm/pay as @a[tag=mg.zbuyer] run function mg:zm/jug',
      'execute if entity @s[tag=mg.zb22] if entity @a[tag=mg.zbuyer,tag=mg.zsc] run return run function mg:zm/already',
      'execute if entity @s[tag=mg.zb22] run scoreboard players set $zc mg.st 3000',
      'execute if entity @s[tag=mg.zb22] if function mg:zm/pay as @a[tag=mg.zbuyer] run function mg:zm/cola',
      'tag @a remove mg.zbuyer']
w('zm/buy', B)
w('zm/already', ['tellraw @a[tag=mg.zbuyer] {"text":"Tu as déjà cette boisson.","color":"gray"}', 'tag @a remove mg.zbuyer'])
w('zm/pay', ['# Paie $zc points (acheteur : mg.zbuyer) ; échoue si pas assez',
             'scoreboard players operation $zh mg.st = @a[tag=mg.zbuyer,limit=1] mg.zpt',
             'execute if score $zh mg.st < $zc mg.st run tellraw @a[tag=mg.zbuyer] [{"text":"Pas assez de points (","color":"red"},{"score":{"name":"$zc","objective":"mg.st"},"color":"yellow"},{"text":" requis).","color":"red"}]',
             'execute if score $zh mg.st < $zc mg.st as @a[tag=mg.zbuyer] at @s run playsound minecraft:block.note_block.bass player @s ~ ~ ~ 1 0.6',
             'execute if score $zh mg.st < $zc mg.st run return fail',
             'scoreboard players operation @a[tag=mg.zbuyer] mg.zpt -= $zc mg.st',
             'execute as @a[tag=mg.zbuyer] at @s run playsound minecraft:entity.experience_orb.pickup player @s ~ ~ ~ 1 0.8',
             'return 1'])
for d, (nm, cost, (x1, z1, x2, z2), _, room) in DOORS.items():
    w(f'zm/door_{d}', [f'# Porte {nm} ouverte', f'fill {x1} 81 {z1} {x2} 83 {z2} minecraft:air', f'kill @e[tag=mg.zd{d}]',
                       f'tag @e[tag=mg.zr_{room}] add mg.zon',
                       f'particle minecraft:poof {(x1 + x2) / 2 + .5} 82 {(z1 + z2) / 2 + .5} 1 1 1 0.05 40',
                       f'playsound minecraft:block.wooden_door.open master @a {(x1 + x2) / 2} 82 {(z1 + z2) / 2} 1 0.6',
                       'tellraw @a[tag=mg.play] [{"text":"🚪 ","color":"gold"},{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a ouvert la porte ' + nm + '.","color":"gray"}]'])
w('zm/buy_gun', ['# Macro $(n) : arme achetée (déjà possédée → chargeur rempli)', '$scoreboard players set $zgn mg.st $(n)',
                 'execute as @a[tag=mg.zbuyer] run function mg:zm/give_gun'])
GG = ['# @s reçoit l\'arme $zgn : recharge si déjà possédée, sinon 2e emplacement, sinon remplace l\'arme en main']
for n, g in G.GUNS.items():
    GG.append(f'execute if score $zgn mg.st matches {n} if items entity @s container.* *[custom_data~{{gun:{n}}}] run return run scoreboard players set @s mg.g{n} {g[4]}')
GG += ['execute unless items entity @s hotbar.2 * run return run function mg:zm/put {slot:"hotbar.2"}',
       'execute if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] run return run function mg:zm/put {slot:"weapon.mainhand"}',
       'function mg:zm/put {slot:"hotbar.2"}']
w('zm/give_gun', GG)
w('zm/put', ['# Macro $(slot)'] + [f'$execute if score $zgn mg.st matches {n} run function mg:gun/put_{n} {{slot:"$(slot)"}}' for n in G.GUNS])
w('zm/box', ['# Boîte mystère : 1 Ray Gun, 2 Sniper, 2 Mitraillette, 2 Fusil à pompe, 1 Fusil (sur 8)',
             'execute store result score $zx mg.st run random value 1..8',
             'scoreboard players set $zgn mg.st 4', 'execute if score $zx mg.st matches 1 run scoreboard players set $zgn mg.st 6',
             'execute if score $zx mg.st matches 2..3 run scoreboard players set $zgn mg.st 5',
             'execute if score $zx mg.st matches 4..5 run scoreboard players set $zgn mg.st 2',
             'execute if score $zx mg.st matches 6..7 run scoreboard players set $zgn mg.st 3',
             'execute as @a[tag=mg.zbuyer] run function mg:zm/give_gun',
             f'particle minecraft:witch 22.5 82.5 {Z - 26.5} 0.4 0.4 0.4 0.1 30',
             f'playsound minecraft:block.chest.open master @a 22.5 82 {Z - 26.5} 1 0.8',
             f'playsound minecraft:entity.player.levelup master @a 22.5 82 {Z - 26.5} 0.6 1.6'] +
  [f'execute if score $zgn mg.st matches {n} run title @a[tag=mg.zbuyer] actionbar ' + js([{'text': '❓ Boîte mystère : ', 'color': 'light_purple'}, {'text': g[0], 'color': g[8], 'bold': True}])
   for n, g in G.GUNS.items()] +
  ['execute if score $zgn mg.st matches 6 run tellraw @a[tag=mg.play] [{"selector":"@a[tag=mg.zbuyer]","color":"yellow"},{"text":" a tiré le RAY GUN !","color":"green","bold":true}]'])
w('zm/jug', ['# @s boit la Juggernog', 'tag @s add mg.zjug', 'attribute @s minecraft:max_health base set 40',
             'effect give @s minecraft:instant_health 1 9 true', 'title @s actionbar {"text":"❤ Juggernog : 20 cœurs !","color":"red","bold":true}',
             'playsound minecraft:entity.generic.drink player @s ~ ~ ~ 1 0.8'])
w('zm/cola', ['# @s boit la Speed Cola', 'tag @s add mg.zsc', 'title @s actionbar {"text":"⚡ Speed Cola : rechargement 2× plus rapide","color":"green","bold":true}',
              'playsound minecraft:entity.generic.drink player @s ~ ~ ~ 1 1.3'])

# ------------------------------------------------------------------ INFECTION
LIMIT = 3600
w('inf/prepare', ['# 🧪 Infection — préparation', 'function mg:zm/build', 'function mg:zm/kill_all', 'function mg:zm/entities', 'function mg:zm/open_all',
                  'scoreboard players set $px mg.st 11', 'scoreboard players set $py mg.st 84', f'scoreboard players set $pz mg.st {Z - 11}',
                  'clear @a[tag=mg.play]', 'gamemode adventure @a[tag=mg.play]', 'team join mg_blue @a[tag=mg.play]',
                  f'spreadplayers 11 {Z - 11} 4 18 under 84 false @a[tag=mg.play]', 'execute as @a[tag=mg.play] at @s run spawnpoint @s ~ ~ ~',
                  'tag @a remove mg.zhit', 'advancement revoke @a only mg:infhit'])
w('inf/kit', ['# @s : survivant (couteau, pistolet, une arme au hasard)', 'clear @s', 'function mg:gun/reset',
              'item replace entity @s hotbar.0 with minecraft:iron_sword[unbreakable={},custom_name=[{"text":"🔪 Couteau","color":"gray","italic":false}]]',
              G.give(1, 'hotbar.1'), 'execute store result score $zx mg.st run random value 2..4',
              'execute if score $zx mg.st matches 2 run ' + G.give(2, 'hotbar.2'), 'execute if score $zx mg.st matches 3 run ' + G.give(3, 'hotbar.2'),
              'execute if score $zx mg.st matches 4 run ' + G.give(4, 'hotbar.2'),
              'item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=3361970,unbreakable={}]',
              'effect give @s minecraft:saturation infinite 0 true'])
w('inf/go', ['# Départ : 1 zombie pour 5 joueurs (au moins 1)', f'scoreboard players set $ift mg.st 0', 'scoreboard players set @a mg.deaths 0',
             'execute as @a[tag=mg.play] run function mg:inf/kit',
             'execute store result score $inn mg.st if entity @a[tag=mg.play]', 'scoreboard players set #5 mg.st 5',
             'scoreboard players operation $inn mg.st /= #5 mg.st', 'execute if score $inn mg.st matches ..0 run scoreboard players set $inn mg.st 1',
             'execute if score $n0 mg.st matches 2.. unless score $infm mg.st matches 1 run function mg:inf/pick',
             # mode joueurs contre mobs : tout le monde survivant, les zombies sont des mobs
             'execute if score $infm mg.st matches 1 run function mg:inf/mstart',
             'tellraw @a[tag=mg.play] ' + js([{'text': '🧪 INFECTION : ', 'color': 'dark_green', 'bold': True},
                                              {'text': 'les zombies infectent les survivants qu\'ils tuent. Survivants : tenez 3 minutes (clic droit = tirer, accroupi = recharger) ! Zombies : contaminez tout le monde.', 'color': 'gray'}]),
             # seul : entraînement, pas de zombie ni de victoire
             'execute unless score $n0 mg.st matches 2.. unless score $infm mg.st matches 1 run tellraw @a[tag=mg.play] ' + js([{'text': "🧪 Mode entraînement (seul) : pas de zombie, essaie les armes (clic droit = tirer, accroupi = recharger). Pas de victoire ; il faut au moins 2 joueurs pour une vraie partie.", 'color': 'yellow'}])])
w('inf/pick', ['execute as @a[tag=mg.play,tag=!mg.inf,sort=random,limit=1] run function mg:inf/make_zombie',
               'scoreboard players remove $inn mg.st 1', 'execute if score $inn mg.st matches 1.. run function mg:inf/pick'])
w('inf/make_zombie', ['# @s devient zombie', 'tag @s remove mg.zhit', 'tag @s add mg.inf', 'tag @s add mg.gtg', 'team join mg_green @s', 'clear @s', 'function mg:gun/reset',
                      'scoreboard players set @s mg.deaths 0',
                      'item replace entity @s armor.head with minecraft:zombie_head',
                      'item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=4227072,unbreakable={}]',
                      'item replace entity @s armor.legs with minecraft:leather_leggings[dyed_color=2116640,unbreakable={}]',
                      'item replace entity @s armor.feet with minecraft:leather_boots[dyed_color=2116640,unbreakable={}]',
                      'effect give @s minecraft:speed infinite 0 true', 'effect give @s minecraft:strength infinite 1 true',
                      'effect give @s minecraft:saturation infinite 0 true', 'function mg:inf/zspawn',
                      'title @s title {"text":"🧟 Tu es INFECTÉ","color":"dark_green","bold":true}',
                      'title @s subtitle {"text":"tue les survivants pour les contaminer","color":"gray"}',
                      'tellraw @a[tag=mg.play] [{"text":"🧪 ","color":"dark_green"},{"selector":"@s","color":"green"},{"text":" a été infecté !","color":"gray"}]',
                      'execute as @a[tag=mg.play] at @s run playsound minecraft:entity.zombie_villager.converted master @s ~ ~ ~ 0.8 1'])
w('inf/zspawn', ['# @s (zombie) : dans un enclos au hasard, 2 s de protection',
                 'execute at @e[type=minecraft:marker,tag=mg.zsp,sort=random,limit=1] run tp @s ~ ~ ~',
                 'execute at @s run spawnpoint @s ~ ~ ~', 'effect give @s minecraft:resistance 2 4 true', 'effect give @s minecraft:instant_health 1 4 true'])
w('inf/tick', ['# 🧪 Infection — tick', 'scoreboard players add $ift mg.st 1',
               'execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]',
               'execute as @a[tag=mg.play,tag=!mg.inf,scores={mg.t=..74}] run scoreboard players set @s mg.deaths 1',
               'execute if score $n0 mg.st matches 2.. as @a[tag=mg.play,tag=!mg.inf,scores={mg.deaths=1..}] run function mg:inf/make_zombie',
               # seul : pas de zombie, un survivant tombé ou tué revient au bunker
               # joueurs contre mobs : touché par un zombie (mob ou joueur) ou mort → infecté, même seul ; vagues de mobs
               'execute if score $infm mg.st matches 1 as @a[tag=mg.play,tag=!mg.inf,tag=mg.zhit] run function mg:inf/make_zombie',
               'execute if score $infm mg.st matches 1 unless score $n0 mg.st matches 2.. as @a[tag=mg.play,tag=!mg.inf,scores={mg.deaths=1..}] run function mg:inf/make_zombie',
               'execute if score $infm mg.st matches 1 run function mg:inf/mtick',
               'execute unless score $n0 mg.st matches 2.. unless score $infm mg.st matches 1 as @e[type=minecraft:player,tag=mg.play,tag=!mg.inf,scores={mg.deaths=1..}] run function mg:inf/srespawn',
               'execute as @a[tag=mg.play,tag=mg.inf,scores={mg.t=..74}] run scoreboard players set @s mg.deaths 1',
               'execute as @a[tag=mg.play,tag=mg.inf,scores={mg.deaths=1..}] run function mg:inf/zdie',
               'execute store result score $ins mg.st if entity @a[tag=mg.play,tag=!mg.inf]',
               'scoreboard players operation $inq mg.st = $ift mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $inq mg.st %= #20 mg.st',
               'execute if score $inq mg.st matches 0 run function mg:inf/second',
               'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $ins mg.st matches 0 run return run function mg:inf/zombies_win',
               'execute if score $state mg.st matches 2 if score $infm mg.st matches 1 if score $ins mg.st matches 0 run return run function mg:inf/zombies_win',
               f'execute if score $state mg.st matches 2 if score $ift mg.st matches {LIMIT}.. run function mg:inf/survivors_win'])
w('inf/srespawn', ['# @s (entraînement, seul) : mort ou chute → retour au bunker, kit rendu', 'scoreboard players set @s mg.deaths 0',
                   f'spreadplayers 11 {Z - 11} 4 18 under 84 false @s', 'execute at @s run spawnpoint @s ~ ~ ~', 'function mg:inf/kit',
                   'effect give @s minecraft:resistance 2 4 true', 'effect give @s minecraft:instant_health 1 4 true',
                   'tellraw @s {"text":"🧪 Entraînement : retour au bunker.","color":"yellow"}'])
w('inf/zdie', ['# @s (zombie) tué : réapparaît', 'scoreboard players set @s mg.deaths 0', 'function mg:inf/zspawn',
               'effect give @s minecraft:speed infinite 0 true', 'effect give @s minecraft:strength infinite 1 true',
               'effect give @s minecraft:saturation infinite 0 true'])
w('inf/second', ['scoreboard players set $inl mg.st ' + str(LIMIT // 20), 'scoreboard players operation $ins2 mg.st = $ift mg.st',
                 'scoreboard players operation $ins2 mg.st /= #20 mg.st', 'scoreboard players operation $inl mg.st -= $ins2 mg.st',
                 'title @a[tag=mg.play,tag=mg.inf] actionbar [{"text":"🧟 Survivants : ","color":"dark_green"},{"score":{"name":"$ins","objective":"mg.st"},"color":"yellow","bold":true},{"text":" — ","color":"gray"},{"score":{"name":"$inl","objective":"mg.st"},"color":"yellow"},{"text":" s","color":"gray"}]',
                 # seul : chrono restant
                 'execute if score $infm mg.st matches 1 run title @a[tag=mg.play,tag=!mg.inf] actionbar [{"text":"🧟 Zombies : ","color":"dark_green"},{"score":{"name":"$imz","objective":"mg.st"},"color":"red","bold":true},{"text":" — survivants : ","color":"gray"},{"score":{"name":"$ins","objective":"mg.st"},"color":"yellow"},{"text":" — ","color":"gray"},{"score":{"name":"$inl","objective":"mg.st"},"color":"yellow"},{"text":" s","color":"gray"}]',
                 'execute unless score $n0 mg.st matches 2.. unless score $infm mg.st matches 1 run title @a[tag=mg.play] actionbar [{"text":"🧪 Entraînement : ","color":"yellow"},{"score":{"name":"$inl","objective":"mg.st"},"color":"yellow","bold":true},{"text":" s","color":"gray"}]',
                 'execute if score $inl mg.st matches 60 run tellraw @a[tag=mg.play] {"text":"🧪 Plus qu\'une minute !","color":"gold"}',
                 'execute if score $inl mg.st matches 60 as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 0.8'])
# --- mode joueurs contre mobs ($infm = 1, ids 217..219)
w('inf/mstart', ['# Joueurs contre mobs : réglages des zombies et première vague',
                 'data modify storage mg:zm hp set value 24', 'data modify storage mg:zm sp set value 0.25d',
                 'scoreboard players set $imc mg.st 0', 'scoreboard players set $imz mg.st 0',
                 'execute store result score $imw mg.st if entity @a[tag=mg.play]', 'scoreboard players add $imw mg.st 2',
                 'function mg:inf/mwave',
                 'tellraw @a[tag=mg.play] ' + js([{'text': '🧟 JOUEURS CONTRE MOBS : ', 'color': 'red', 'bold': True},
                                                  {'text': "des zombies envahissent le bunker. Un seul coup d'un zombie et tu es infecté : tu chasses alors les survivants (ton coup les infecte aussi). Tenez 3 minutes !", 'color': 'gray'}])])
w('inf/mwave', ['execute as @e[type=minecraft:marker,tag=mg.zsp,sort=random,limit=1] at @s run function mg:zm/spawn_one with storage mg:zm',
                'scoreboard players remove $imw mg.st 1', 'execute if score $imw mg.st matches 1.. run function mg:inf/mwave'])
w('inf/mtick', ['# Toutes les 2 s : un zombie de plus tant qu\'on est sous le plafond (6 + 3 par survivant, 30 max) ; plus rapide après 90 s',
                'scoreboard players add $imc mg.st 1', 'execute store result score $imz mg.st if entity @e[type=minecraft:zombie,tag=mg.zz]',
                'scoreboard players operation $imx mg.st = $ins mg.st', 'scoreboard players operation $imx mg.st *= #3 mg.st',
                'scoreboard players add $imx mg.st 6', 'execute if score $imx mg.st matches 31.. run scoreboard players set $imx mg.st 30',
                'execute if score $ift mg.st matches 1800.. if score $imc mg.st matches 20.. if score $imz mg.st < $imx mg.st run function mg:inf/mspawn',
                'execute if score $imc mg.st matches 40.. if score $imz mg.st < $imx mg.st run function mg:inf/mspawn',
                'execute if score $imc mg.st matches 40.. run scoreboard players set $imc mg.st 0'])
w('inf/mspawn', ['scoreboard players set $imc mg.st 0',
                 'execute as @e[type=minecraft:marker,tag=mg.zsp,sort=random,limit=1] at @s unless entity @a[tag=mg.play,tag=!mg.inf,distance=..5] run function mg:zm/spawn_one with storage mg:zm'])
w('inf/survivors_win', ['# Temps écoulé : les survivants gagnent',
                        'execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] ' + js([{'text': "🧪 Fin de l'entraînement.", 'color': 'yellow'}]),
                        'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
                        'tellraw @a {"text":"🧪 Les survivants ont tenu 3 minutes !","color":"aqua","bold":true}',
                        'function mg:core/win_blue'])
w('inf/zombies_win', ['# Plus de survivants', 'tellraw @a {"text":"🧟 Tout le monde est infecté !","color":"dark_green","bold":true}',
                      'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
                      'function mg:core/win_green'])

C.w('infhit/hit', ['# Avancement mg:infhit : @s touché par un zombie (mob) ou un joueur infecté (équipe verte)',
                   'advancement revoke @s only mg:infhit',
                   'execute if score $state mg.st matches 2 if score $infm mg.st matches 1 if entity @s[tag=mg.play,tag=!mg.inf] run tag @s add mg.zhit'])
_adv = os.path.join(C.D, 'advancement', 'infhit.json')
os.makedirs(os.path.dirname(_adv), exist_ok=True)
with open(_adv, 'w', encoding='utf-8', newline='\n') as _f:
    json.dump({'criteria': {
        'mob': {'trigger': 'minecraft:entity_hurt_player', 'conditions': {'damage': {'type': {'source_entity': {'minecraft:entity_type': 'minecraft:zombie'}}}}},
        'joueur': {'trigger': 'minecraft:entity_hurt_player', 'conditions': {'damage': {'type': {'source_entity': {'minecraft:entity_type': 'minecraft:player', 'team': 'mg_green'}}}}}},
        'requirements': [['mob', 'joueur']], 'rewards': {'function': 'mg:infhit/hit'}}, _f, ensure_ascii=False, indent=2)
    _f.write('\n')
if not C.MAP:
    # 217/218/219 : Infection « joueurs contre mobs » sur Bunker / Laboratoire / Manoir → jeu 98/211/213 + $infm = 1
    C.patch('core/request', 'execute if score $game mg.st matches 91..92 run scoreboard players set $game mg.st 28', [
        '# Infection : 217 Bunker, 218 Laboratoire, 219 Manoir = joueurs contre mobs → jeu 98 / 211 / 213 + $infm 1',
        'scoreboard players set $infm mg.st 0',
        'execute if score $game mg.st matches 217..219 run scoreboard players set $infm mg.st 1',
        'execute if score $game mg.st matches 217 run scoreboard players set $game mg.st 98',
        'execute if score $game mg.st matches 218 run scoreboard players set $game mg.st 211',
        'execute if score $game mg.st matches 219 run scoreboard players set $game mg.st 213'])
    C.go_range(219)
C.register([97, 98], 'zmode', [
    C.announce(97, '', '🧟 ZOMBIES', 'dark_green', f'survivez à {ROUNDS} manches dans le bunker !'),
    C.announce(98, '', '🧪 INFECTION', 'dark_green', 'survivants armés contre zombies contagieux, 3 min !')])
C.objectives([('mg.zpt', 'dummy {"text":"🧟 Points","color":"dark_green"}'), ('mg.zk', 'minecraft.killed:minecraft.zombie')])
C.patch('core/load', 'scoreboard objectives add mg.bw trigger', ['scoreboard players set #2 mg.st 2', 'scoreboard players set #3 mg.st 3',
                                                                 'scoreboard players set #5 mg.st 5', 'scoreboard players set #8 mg.st 8',
                                                                 'scoreboard players set #60 mg.st 60'])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw', ['data remove storage mg:zm hp'])
C.forceload([f'# Bunker Zombies / Infection (z {Z})', f'forceload add -17 {Z - 39} 39 {Z + 17}'])
print('Zombies/Infection OK')
