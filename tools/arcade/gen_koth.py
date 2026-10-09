"""👑 King of the Hill — solo (id 86) et en équipes rouge/bleu (id 87). Arène 51×51 en z 20400.

    python tools/arcade/gen_koth.py .

Une colline en gradins au centre, sommet 5×5 en or. Chaque seconde passée SEUL (ou seulement ton équipe) sur le
sommet = +1 point. Solo : 60 points, équipes : 90 points, ou le plus de points au bout de 5 min. Réapparition illimitée.
"""
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
Z = C.param('Z', 20400)
# thème de la carte (cartes supplémentaires : tools/arcade/gen_maps.py)
GROUND = C.param('ground', ['dirt', 'grass_block'])
TIERS = C.param('tiers', ['stone_bricks', 'mossy_stone_bricks', 'stone_bricks', 'polished_andesite', 'smooth_stone'])
STAIRS = C.param('stairs', 'stone_brick_stairs')
COVER = C.param('cover', 'cobblestone')
LIGHT = C.param('light', 'lantern')
TITLE = C.param('title', 'colline en gradins, sommet en or')
WIN_SOLO, WIN_TEAM, LIMIT = 60, 90, 6000

L = [f'# 👑 King of the Hill — arène 51×51 (centre 0 80 {Z}), {TITLE}']
L += [f'fill -27 {y} {Z - 27} 27 {y} {Z + 27} minecraft:air' for y in range(79, 101)]
L += [f'fill -25 79 {Z - 25} 25 79 {Z + 25} minecraft:{GROUND[0]}', f'fill -25 80 {Z - 25} 25 80 {Z + 25} minecraft:{GROUND[1]}']
for i, (h, mat) in enumerate(zip((11, 9, 7, 5, 3), TIERS)):
    y = 81 + i
    L.append(f'fill -{h} {y} {Z - h} {h} {y} {Z + h} minecraft:{mat}')
L += [f'fill -2 85 {Z - 2} 2 85 {Z + 2} minecraft:gold_block', f'setblock 0 85 {Z} minecraft:beacon',
      f'fill -1 84 {Z - 1} 1 84 {Z + 1} minecraft:iron_block']
# escaliers d'accès sur les 4 faces
for i in range(5):
    y = 81 + i
    d = 12 - 2 * i
    L += [f'fill -1 {y} {Z - d} 1 {y} {Z - d + 1} minecraft:{STAIRS}[facing=south]',
          f'fill -1 {y} {Z + d - 1} 1 {y} {Z + d} minecraft:{STAIRS}[facing=north]',
          f'fill -{d} {y} {Z - 1} -{d - 1} {y} {Z + 1} minecraft:{STAIRS}[facing=east]',
          f'fill {d - 1} {y} {Z - 1} {d} {y} {Z + 1} minecraft:{STAIRS}[facing=west]']
# couvertures autour
for (x, z) in [(-18, -18), (18, -18), (-18, 18), (18, 18), (-20, 0), (20, 0), (0, -20), (0, 20)]:
    L += [f'fill {x - 1} 81 {Z + z - 1} {x + 1} 82 {Z + z + 1} minecraft:{COVER}', f'setblock {x} 83 {Z + z} minecraft:{LIGHT}']
L += [f'fill -26 79 {Z - 26} 26 99 {Z - 26} minecraft:barrier', f'fill -26 79 {Z + 26} 26 99 {Z + 26} minecraft:barrier',
      f'fill -26 79 {Z - 25} -26 99 {Z + 25} minecraft:barrier', f'fill 26 79 {Z - 25} 26 99 {Z + 25} minecraft:barrier',
      f'fill -26 100 {Z - 26} 26 100 {Z + 26} minecraft:barrier', f'fill -2 86 {Z - 2} 2 86 {Z + 2} minecraft:air']
w('koth/build', L)

w('koth/prepare', ['# 👑 King of the Hill — préparation ($khm : 0 solo, 1 équipes)',
                   'scoreboard players set $khm mg.st 0', 'execute if score $game mg.st matches 87 run scoreboard players set $khm mg.st 1',
                   'function mg:koth/build', f'kill @e[type=minecraft:item,x=-30,y=60,z={Z - 30},dx=60,dy=50,dz=60]',
                   'scoreboard players set $px mg.st 0', 'scoreboard players set $py mg.st 100', f'scoreboard players set $pz mg.st {Z}',
                   'gamemode adventure @a[tag=mg.play]', 'clear @a[tag=mg.play]',
                   'scoreboard players set @a[tag=mg.play] mg.kh 0', 'scoreboard players reset Rouge mg.kh', 'scoreboard players reset Bleu mg.kh',
                   'execute if score $khm mg.st matches 1 run scoreboard players set $nt mg.st 2',
                   'execute if score $khm mg.st matches 1 run function mg:core/assign_teams',
                   'execute as @a[tag=mg.play] run function mg:koth/spawn'])
w('koth/spawn', ['# @s : point de départ (solo : n\'importe où au bord ; équipes : son camp)',
                 f'execute as @s[team=mg_red] run spawnpoint @s -20 81 {Z}', f'execute as @s[team=mg_blue] run spawnpoint @s 20 81 {Z}',
                 f'execute unless entity @s[team=mg_red] unless entity @s[team=mg_blue] run spawnpoint @s 0 81 {Z - 20}',
                 f'execute if score $khm mg.st matches 1 if entity @s[team=mg_red] run spreadplayers -20 {Z} 1 4 under 83 false @s',
                 f'execute if score $khm mg.st matches 1 if entity @s[team=mg_blue] run spreadplayers 20 {Z} 1 4 under 83 false @s',
                 f'execute if score $khm mg.st matches 0 run function mg:koth/spawn_ring',
                 f'execute at @s run tp @s ~ ~ ~ facing 0 85 {Z}'])
w('koth/spawn_ring', ['# Solo : un des 8 coins/bords, au hasard', 'execute store result score $khr mg.st run random value 0..7'] +
  [f'execute if score $khr mg.st matches {k} run spreadplayers {x} {Z + z} 1 2 under 83 false @s' for k, (x, z) in
   enumerate([(-21, -21), (21, -21), (-21, 21), (21, 21), (-22, 0), (22, 0), (0, -22), (0, 22)])])
w('koth/kit', ['# @s : kit (épée en pierre, bâton de recul, armure en cuir à la couleur de l\'équipe)',
               'clear @s', 'give @s minecraft:stone_sword[unbreakable={}]',
               'give @s minecraft:stick[enchantments={knockback:2},custom_name=[{"text":"Bâton de recul","color":"gold","italic":false}]]',
               'give @s minecraft:golden_apple 1',
               'execute if entity @s[team=mg_red] run item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=16711680,unbreakable={}]',
               'execute if entity @s[team=mg_blue] run item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=255,unbreakable={}]',
               'execute unless entity @s[team=mg_red] unless entity @s[team=mg_blue] run item replace entity @s armor.chest with minecraft:leather_chestplate[unbreakable={}]',
               'item replace entity @s armor.feet with minecraft:leather_boots[unbreakable={}]',
               'effect give @s minecraft:saturation infinite 0 true'])
w('koth/go', ['# Départ', 'scoreboard players set $kht mg.st 0', 'execute as @a[tag=mg.play] run function mg:koth/kit',
              'scoreboard players set @a mg.deaths 0',
              'execute if score $khm mg.st matches 0 run scoreboard objectives setdisplay sidebar mg.kh',
              'execute if score $khm mg.st matches 1 run scoreboard players set Rouge mg.kh 0', 'execute if score $khm mg.st matches 1 run scoreboard players set Bleu mg.kh 0',
              'execute if score $khm mg.st matches 1 run scoreboard objectives setdisplay sidebar mg.kh',
              'execute if score $khm mg.st matches 1 run scoreboard players reset @a mg.kh',
              'tellraw @a[tag=mg.play] ' + js([{'text': '👑 KING OF THE HILL : ', 'color': 'gold', 'bold': True},
                                               {'text': f'reste sur le sommet en or SANS adversaire : +1 point par seconde. Solo : {WIN_SOLO} points, équipes : {WIN_TEAM}. 5 minutes max. Réapparition illimitée.', 'color': 'gray'}])])
w('koth/tick', ['# 👑 King of the Hill — tick', 'scoreboard players add $kht mg.st 1',
                # morts / chutes → réapparition
                'execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:koth/respawn',
                'execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]',
                'execute as @a[tag=mg.play,scores={mg.t=..74}] run function mg:koth/respawn',
                # présence sur le sommet (x −2..2, z −2..2, y 86..89)
                'tag @a remove mg.khz', f'tag @a[tag=mg.play,x=-2,y=85,z={Z - 2},dx=4,dy=3,dz=4,gamemode=!spectator] add mg.khz',
                'execute store result score $khn mg.st if entity @a[tag=mg.khz]',
                'execute store result score $khr mg.st if entity @a[tag=mg.khz,team=mg_red]',
                'execute store result score $khb mg.st if entity @a[tag=mg.khz,team=mg_blue]',
                'scoreboard players operation $khq mg.st = $kht mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $khq mg.st %= #20 mg.st',
                'execute if score $khq mg.st matches 0 run function mg:koth/second',
                f'execute if score $kht mg.st matches {LIMIT - 1200} run tellraw @a[tag=mg.play] {{"text":"👑 Plus qu\'une minute !","color":"gold"}}',
                f'execute if score $state mg.st matches 2 if score $kht mg.st matches {LIMIT}.. run function mg:koth/timeout',
                'execute store result score $alive mg.st if entity @a[tag=mg.play]',
                'execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw'])
w('koth/second', ['# Une seconde : points pour le roi (seul) ou l\'équipe (seule) sur le sommet',
                  'execute if score $khm mg.st matches 0 if score $khn mg.st matches 1 run scoreboard players add @a[tag=mg.khz] mg.kh 1',
                  'execute if score $khm mg.st matches 1 if score $khr mg.st matches 1.. if score $khb mg.st matches 0 run scoreboard players add Rouge mg.kh 1',
                  'execute if score $khm mg.st matches 1 if score $khb mg.st matches 1.. if score $khr mg.st matches 0 run scoreboard players add Bleu mg.kh 1',
                  'execute if score $khm mg.st matches 0 if score $khn mg.st matches 1 run title @a[tag=mg.play] actionbar [{"text":"👑 Roi : ","color":"gold"},{"selector":"@a[tag=mg.khz]","color":"yellow"}]',
                  'execute if score $khm mg.st matches 1 if score $khr mg.st matches 1.. if score $khb mg.st matches 0 run title @a[tag=mg.play] actionbar {"text":"👑 Les ROUGES tiennent la colline","color":"red"}',
                  'execute if score $khm mg.st matches 1 if score $khb mg.st matches 1.. if score $khr mg.st matches 0 run title @a[tag=mg.play] actionbar {"text":"👑 Les BLEUS tiennent la colline","color":"blue"}',
                  'execute if score $khn mg.st matches 2.. unless score $khr mg.st matches 1.. run title @a[tag=mg.play] actionbar {"text":"⚔ Sommet contesté !","color":"gray"}',
                  'execute if score $khm mg.st matches 1 if score $khr mg.st matches 1.. if score $khb mg.st matches 1.. run title @a[tag=mg.play] actionbar {"text":"⚔ Sommet contesté !","color":"gray"}',
                  f'execute positioned 0 86 {Z} run particle minecraft:happy_villager ~ ~0.5 ~ 2 0.3 2 0 6',
                  # victoire
                  f'execute if score $state mg.st matches 2 if score $khm mg.st matches 0 as @a[tag=mg.play,scores={{mg.kh={WIN_SOLO}..}},limit=1] run return run function mg:core/win_player',
                  f'execute if score $state mg.st matches 2 if score $khm mg.st matches 1 if score Rouge mg.kh matches {WIN_TEAM}.. run return run function mg:core/win_red',
                  f'execute if score $state mg.st matches 2 if score $khm mg.st matches 1 if score Bleu mg.kh matches {WIN_TEAM}.. run return run function mg:core/win_blue'])
w('koth/respawn', ['# @s : réapparition (kit rendu, 2 s de protection)', 'scoreboard players set @s mg.deaths 0',
                   'function mg:koth/spawn', 'function mg:koth/kit', 'effect give @s minecraft:resistance 2 4 true',
                   'effect give @s minecraft:instant_health 1 4 true'])
w('koth/timeout', ['# 5 min écoulées : le plus de points gagne (égalité = match nul)',
                   'execute if score $khm mg.st matches 1 if score Rouge mg.kh > Bleu mg.kh run return run function mg:core/win_red',
                   'execute if score $khm mg.st matches 1 if score Bleu mg.kh > Rouge mg.kh run return run function mg:core/win_blue',
                   'execute if score $khm mg.st matches 1 run return run function mg:core/draw',
                   'scoreboard players set $khx mg.st 0', 'scoreboard players operation $khx mg.st > @a[tag=mg.play] mg.kh',
                   'scoreboard players set $khc mg.st 0', 'execute as @a[tag=mg.play] if score @s mg.kh = $khx mg.st run scoreboard players add $khc mg.st 1',
                   'execute if score $khx mg.st matches 0 run return run function mg:core/draw',
                   'execute if score $khc mg.st matches 2.. run return run function mg:core/draw',
                   'execute as @a[tag=mg.play] if score @s mg.kh = $khx mg.st run function mg:core/win_player'])
w('koth/cleanup', ['tag @a remove mg.khz', 'scoreboard players reset * mg.kh'])

C.register([86, 87], 'koth', [
    C.announce(86, '', '👑 KING OF THE HILL', 'gold', f'tiens le sommet seul, {WIN_SOLO} points pour gagner !'),
    C.announce(87, '', '👑 KING OF THE HILL — ÉQUIPES', 'gold', f'rouges contre bleus, {WIN_TEAM} points sur le sommet !')])
C.objectives([('mg.kh', 'dummy {"text":"👑 Colline","color":"gold"}')])
C.forceload([f'# King of the Hill (z {Z})', f'forceload add -27 {Z - 27} 27 {Z + 27}'])
print('KotH OK')
