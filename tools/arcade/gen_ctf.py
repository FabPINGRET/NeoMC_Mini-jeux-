"""🚩 Capture the Flag — Rouge contre Bleu (id 93). Arène 85×45 en z 21600.

    python tools/arcade/gen_ctf.py .

Prends le drapeau adverse dans sa base et ramène-le sur ton socle pendant que TON drapeau y est encore.
3 captures pour gagner (ou le plus de captures au bout de 10 min). Le porteur brille et a le drapeau sur la tête ;
s'il meurt, le drapeau tombe : un adversaire peut le reprendre, un défenseur le renvoie chez lui en le touchant,
sinon il rentre seul au bout de 30 s. Réapparition illimitée dans sa base.
Seul : mode entraînement (pas de victoire, fin au chrono ou menu → Arrêter).
"""
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
Z = 21600
WIN, LIMIT, DROP = 3, 12000, 600
T = {  # équipe : (nom, couleur texte, couleur blocs, x du socle, signe, rgb, adverse)
    'red': ('ROUGE', 'red', 'red', -35, -1, 16711680, 'blue'),
    'blue': ('BLEU', 'blue', 'blue', 35, 1, 255, 'red'),
}
ST = {'red': '$cfr', 'blue': '$cfb'}       # état du drapeau : 0 au socle, 1 porté, 2 tombé
CAR = {'red': 'mg.cfcr', 'blue': 'mg.cfcb'}  # tag du porteur de ce drapeau
POS = {'red': 'mg.cfpr', 'blue': 'mg.cfpb'}  # marqueur qui suit le porteur
DRP = {'red': 'mg.cfdr', 'blue': 'mg.cfdb'}  # drapeau tombé (item_display)
TIM = {'red': '$cfrt', 'blue': '$cfbt'}

# ---------- arène
L = ['# 🚩 Capture the Flag — prairie x −42..42, z 21578..21622 ; bases aux deux bouts']
L += [f'fill -44 {y} {Z - 24} 44 {y} {Z + 24} minecraft:air' for y in range(78, 101)]
L += [f'fill -42 78 {Z - 22} 42 79 {Z + 22} minecraft:dirt', f'fill -42 80 {Z - 22} 42 80 {Z + 22} minecraft:grass_block']
for t, (nm, col, blk, x, s, rgb, oth) in T.items():
    bx0, bx1 = x - 7, x + 7
    L += [f'fill {bx0} 80 {Z - 8} {bx1} 80 {Z + 8} minecraft:{blk}_terracotta',
          f'fill {bx0} 81 {Z - 8} {bx1} 83 {Z + 8} minecraft:stone_bricks hollow',
          f'fill {bx0 + 1} 81 {Z - 7} {bx1 - 1} 83 {Z + 7} minecraft:air',
          f'fill {bx0} 84 {Z - 8} {bx1} 84 {Z + 8} minecraft:stone_brick_wall',
          f'fill {bx0 + 1} 84 {Z - 7} {bx1 - 1} 84 {Z + 7} minecraft:air',
          # trois entrées (avant, côtés)
          f'fill {x - 7 * s} 81 {Z - 1} {x - 7 * s} 82 {Z + 1} minecraft:air',
          f'fill {x - 1} 81 {Z - 8} {x + 1} 82 {Z - 8} minecraft:air', f'fill {x - 1} 81 {Z + 8} {x + 1} 82 {Z + 8} minecraft:air',
          f'setblock {x} 81 {Z} minecraft:{blk}_glazed_terracotta', f'fill {x - 1} 80 {Z - 1} {x + 1} 80 {Z + 1} minecraft:gold_block',
          f'setblock {x + 5 * s} 81 {Z - 5} minecraft:lantern', f'setblock {x + 5 * s} 81 {Z + 5} minecraft:lantern']
# milieu : murets, meules de foin, une butte centrale et deux couloirs
L += [f'fill -3 81 {Z - 3} 3 81 {Z + 3} minecraft:moss_block', f'fill -2 82 {Z - 2} 2 82 {Z + 2} minecraft:moss_block',
      f'fill -1 83 {Z - 1} 1 83 {Z + 1} minecraft:mossy_cobblestone']
for (x, z) in [(-18, -12), (18, 12), (-18, 12), (18, -12), (-10, 0), (10, 0), (0, -15), (0, 15)]:
    L.append(f'fill {x - 2} 81 {Z + z} {x + 2} 82 {Z + z} minecraft:cobblestone_wall')
for (x, z) in [(-22, 3), (22, -3), (-6, -9), (6, 9), (-26, -16), (26, 16)]:
    L.append(f'fill {x} 81 {Z + z} {x + 1} 82 {Z + z + 1} minecraft:hay_block')
for (x, z) in [(-14, -19), (14, 19), (-30, 18), (30, -18)]:
    L += [f'fill {x} 81 {Z + z} {x} 85 {Z + z} minecraft:oak_log', f'fill {x - 2} 85 {Z + z - 2} {x + 2} 87 {Z + z + 2} minecraft:oak_leaves[persistent=true] replace minecraft:air']
L += [f'fill -43 78 {Z - 23} 43 100 {Z - 23} minecraft:barrier', f'fill -43 78 {Z + 23} 43 100 {Z + 23} minecraft:barrier',
      f'fill -43 78 {Z - 22} -43 100 {Z + 22} minecraft:barrier', f'fill 43 78 {Z - 22} 43 100 {Z + 22} minecraft:barrier',
      f'fill -42 100 {Z - 22} 42 100 {Z + 22} minecraft:barrier']
w('ctf/build', L)


def banner(t):
    return f'minecraft:{T[t][2]}_banner'


# ---------- préparation / départ
w('ctf/prepare', ['# 🚩 Capture the Flag — préparation', 'function mg:ctf/build', 'function mg:ctf/kill_all',
                  'scoreboard players set $px mg.st 0', 'scoreboard players set $py mg.st 95', f'scoreboard players set $pz mg.st {Z}',
                  'clear @a[tag=mg.play]', 'gamemode adventure @a[tag=mg.play]',
                  'scoreboard players set $nt mg.st 2', 'function mg:core/assign_teams',
                  'scoreboard players reset Rouge mg.cf', 'scoreboard players reset Bleu mg.cf',
                  'function mg:ctf/home_red', 'function mg:ctf/home_blue',
                  'execute as @a[tag=mg.play] run function mg:ctf/spawn'])
w('ctf/kill_all', ['kill @e[tag=mg.cfd]', 'kill @e[tag=mg.cfp]',
                   f'kill @e[type=minecraft:item,x=-45,y=60,z={Z - 25},dx=90,dy=50,dz=50]',
                   f'kill @e[type=minecraft:arrow,x=-45,y=60,z={Z - 25},dx=90,dy=50,dz=50]'])
w('ctf/spawn', ['# @s : dans sa base, derrière son drapeau',
                f'execute if entity @s[team=mg_red] run spawnpoint @s -39 81 {Z}',
                f'execute if entity @s[team=mg_blue] run spawnpoint @s 39 81 {Z}',
                f'execute if entity @s[team=mg_red] run spreadplayers -39 {Z} 1 3 under 83 false @s',
                f'execute if entity @s[team=mg_blue] run spreadplayers 39 {Z} 1 3 under 83 false @s',
                f'execute at @s run tp @s ~ ~ ~ facing 0 81 {Z}'])
w('ctf/kit', ['# @s : kit', 'clear @s', 'give @s minecraft:stone_sword[unbreakable={}]', 'give @s minecraft:bow[unbreakable={}]',
              'give @s minecraft:arrow 16', 'give @s minecraft:cooked_beef 16',
              'execute if entity @s[team=mg_red] run item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=16711680,unbreakable={}]',
              'execute if entity @s[team=mg_blue] run item replace entity @s armor.chest with minecraft:leather_chestplate[dyed_color=255,unbreakable={}]',
              'execute if entity @s[team=mg_red] run item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=16711680,unbreakable={}]',
              'execute if entity @s[team=mg_blue] run item replace entity @s armor.head with minecraft:leather_helmet[dyed_color=255,unbreakable={}]',
              'item replace entity @s armor.legs with minecraft:leather_leggings[unbreakable={}]',
              'item replace entity @s armor.feet with minecraft:leather_boots[unbreakable={}]'])
w('ctf/go', ['# Départ', 'scoreboard players set $cft mg.st 0', 'execute as @a[tag=mg.play] run function mg:ctf/kit',
             'scoreboard players set @a mg.deaths 0', 'scoreboard players set Rouge mg.cf 0', 'scoreboard players set Bleu mg.cf 0',
             'scoreboard objectives setdisplay sidebar mg.cf',
             'execute if score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] ' + js([{'text': '🚩 CAPTURE THE FLAG : ', 'color': 'gold', 'bold': True},
                                              {'text': f'va chercher le drapeau adverse (au fond de sa base) et ramène-le sur ton socle doré, pendant que TON drapeau y est. {WIN} captures pour gagner, 10 min max.', 'color': 'gray'}]),
             # seul : mêmes consignes sans la condition de victoire
             'execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] ' + js([{'text': '🚩 CAPTURE THE FLAG : ', 'color': 'gold', 'bold': True},
                                              {'text': 'va chercher le drapeau adverse (au fond de sa base) et ramène-le sur ton socle doré, pendant que TON drapeau y est. 10 min max.', 'color': 'gray'}]),
             # seul : entraînement, pas de victoire
             'execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] ' + js([{'text': "🚩 Mode entraînement (seul) : le drapeau bleu n'est pas défendu, entraîne-toi aux captures. Pas de victoire ; il faut au moins 2 joueurs pour une vraie partie.", 'color': 'yellow'}])])

# ---------- tick
TK = ['# 🚩 Capture the Flag — tick', 'scoreboard players add $cft mg.st 1',
      'execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:ctf/respawn',
      'execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]',
      'execute as @a[tag=mg.play,scores={mg.t=..72}] run function mg:ctf/respawn']
for t, (nm, col, blk, x, s, rgb, oth) in T.items():
    me, en = f'mg_{t}', f'mg_{oth}'
    TK += [f'# drapeau {nm}',
           # le marqueur suit le porteur (sa dernière position sert si le porteur meurt)
           f'execute as @e[type=minecraft:marker,tag={POS[t]}] at @a[tag={CAR[t]},limit=1] run tp @s ~ ~ ~',
           # prise au socle / ramassage par terre (adversaire) ; renvoi par un défenseur
           f'execute if score {ST[t]} mg.st matches 0 positioned {x} 82 {Z} as @a[tag=mg.play,team={en},distance=..2,limit=1,sort=nearest] run function mg:ctf/take_{t}',
           f'execute if score {ST[t]} mg.st matches 2 as @e[tag={DRP[t]}] at @s as @a[tag=mg.play,team={en},distance=..1.6,limit=1,sort=nearest] run function mg:ctf/take_{t}',
           f'execute if score {ST[t]} mg.st matches 2 as @e[tag={DRP[t]}] at @s if entity @a[tag=mg.play,team={me},distance=..1.6] run function mg:ctf/return_{t}',
           f'execute if score {ST[t]} mg.st matches 2 run scoreboard players remove {TIM[t]} mg.st 1',
           f'execute if score {ST[t]} mg.st matches 2 if score {TIM[t]} mg.st matches ..0 run function mg:ctf/return_{t}',
           # porteur : brille, particules
           f'execute as @a[tag={CAR[t]}] at @s run particle minecraft:dust{{color:[{(rgb >> 16) / 255:.1f},0.0,{(rgb & 255) / 255:.1f}],scale:1.5}} ~ ~2.3 ~ 0.2 0.2 0.2 0 2',
           f'execute as @e[tag={DRP[t]}] at @s run particle minecraft:end_rod ~ ~1 ~ 0.1 0.5 0.1 0.01 1']
    # capture : le porteur du drapeau adverse arrive sur son propre socle, son drapeau étant à la maison
    TK.append(f'execute if score {ST[t]} mg.st matches 0 positioned {x} 82 {Z} as @a[tag={CAR[oth]},team={me},distance=..2.5,limit=1] run function mg:ctf/capture_{t}')
TK += [f'execute if score $cft mg.st matches {LIMIT - 1200} run tellraw @a[tag=mg.play] {{"text":"🚩 Plus qu\'une minute !","color":"gold"}}',
       f'execute if score $state mg.st matches 2 if score $cft mg.st matches {LIMIT}.. run function mg:ctf/timeout',
       'execute store result score $cfn mg.st if entity @a[tag=mg.play,team=mg_red]',
       'execute store result score $cfm mg.st if entity @a[tag=mg.play,team=mg_blue]',
       'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $cfn mg.st matches 0 if score $cfm mg.st matches 1.. run return run function mg:core/win_blue',
       'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $cfm mg.st matches 0 if score $cfn mg.st matches 1.. run return run function mg:core/win_red',
       'execute if score $state mg.st matches 2 if score $cfm mg.st matches 0 if score $cfn mg.st matches 0 run function mg:core/draw']
w('ctf/tick', TK)

for t, (nm, col, blk, x, s, rgb, oth) in T.items():
    oname, ocol = T[oth][0], T[oth][1]
    head = f'minecraft:{blk}_banner'
    w(f'ctf/home_{t}', [f'# Drapeau {nm} remis sur son socle', f'scoreboard players set {ST[t]} mg.st 0',
                        f'kill @e[tag={DRP[t]}]', f'kill @e[tag={POS[t]}]', f'tag @a remove {CAR[t]}',
                        f'setblock {x} 82 {Z} minecraft:{blk}_banner[rotation={12 if s < 0 else 4}]'])
    w(f'ctf/take_{t}', [f'# @s (équipe adverse) prend le drapeau {nm}', f'scoreboard players set {ST[t]} mg.st 1',
                        f'kill @e[tag={DRP[t]}]', f'setblock {x} 82 {Z} minecraft:air', f'tag @s add {CAR[t]}',
                        f'kill @e[tag={POS[t]}]', f'execute at @s run summon minecraft:marker ~ ~ ~ {{Tags:["mg.cfp","{POS[t]}"]}}',
                        f'item replace entity @s armor.head with {head}',
                        'effect give @s minecraft:glowing infinite 0 true',
                        'tellraw @a[tag=mg.play] ' + js([{'text': '🚩 ', 'color': col}, {'selector': '@s', 'color': ocol},
                                                         {'text': f' a pris le drapeau {nm} !', 'color': col, 'bold': True}]),
                        f'execute as @a[tag=mg.play,team=mg_{t}] at @s run playsound minecraft:block.note_block.didgeridoo master @s ~ ~ ~ 1 0.6',
                        f'execute as @a[tag=mg.play,team=mg_{oth}] at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.5'])
    w(f'ctf/drop_{t}', [f'# Le porteur du drapeau {nm} est tombé : le drapeau reste là (ou rentre s\'il est tombé dans le vide)',
                        f'tag @a remove {CAR[t]}',
                        f'execute as @e[type=minecraft:marker,tag={POS[t]},limit=1] at @s unless entity @s[y=-64,dy=141] run return run function mg:ctf/drop_here_{t}',
                        f'function mg:ctf/return_{t}'])
    w(f'ctf/drop_here_{t}', [f'# (marqueur) drapeau {nm} posé au sol ici', f'scoreboard players set {ST[t]} mg.st 2',
                             f'scoreboard players set {TIM[t]} mg.st {DROP}',
                             f'summon minecraft:item_display ~ ~0.9 ~ {{Tags:["mg.cfd","{DRP[t]}"],billboard:"vertical",item:{{id:"{head}",count:1}},transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}}}',
                             'kill @s',
                             'tellraw @a[tag=mg.play] ' + js([{'text': f'🚩 Le drapeau {nm} est tombé ! ', 'color': col},
                                                              {'text': '(retour automatique dans 30 s)', 'color': 'gray'}])])
    w(f'ctf/return_{t}', [f'# Drapeau {nm} renvoyé à sa base', f'function mg:ctf/home_{t}',
                          'tellraw @a[tag=mg.play] ' + js([{'text': f'🚩 Le drapeau {nm} est rentré à sa base.', 'color': col}])])
    w(f'ctf/capture_{t}', [f'# @s ({nm}) ramène le drapeau {oname} chez lui : +1',
                           f'scoreboard players add {"Rouge" if t == "red" else "Bleu"} mg.cf 1', 'scoreboard players add @s mg.cf 1',
                           f'function mg:ctf/home_{oth}', 'effect clear @s minecraft:glowing', 'function mg:ctf/kit',
                           'tellraw @a[tag=mg.play] ' + js([{'text': '🚩 ', 'color': col}, {'selector': '@s', 'color': col},
                                                            {'text': ' CAPTURE ! ', 'color': 'gold', 'bold': True},
                                                            {'text': 'Rouge ', 'color': 'red'}, {'score': {'name': 'Rouge', 'objective': 'mg.cf'}, 'color': 'red'},
                                                            {'text': ' – ', 'color': 'gray'}, {'score': {'name': 'Bleu', 'objective': 'mg.cf'}, 'color': 'blue'},
                                                            {'text': ' Bleu', 'color': 'blue'}]),
                           f'title @a[tag=mg.play] title {{"text":"🚩 Capture {nm} !","color":"{col}","bold":true}}',
                           'execute as @a[tag=mg.play] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.8 1.2',
                           f'execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score {"Rouge" if t == "red" else "Bleu"} mg.cf matches {WIN}.. run function mg:core/win_{t}'])

w('ctf/respawn', ['# @s : mort ou chute → lâche le drapeau, réapparaît dans sa base', 'scoreboard players set @s mg.deaths 0',
                  'execute if entity @s[tag=mg.cfcr] run function mg:ctf/drop_red',
                  'execute if entity @s[tag=mg.cfcb] run function mg:ctf/drop_blue',
                  'effect clear @s minecraft:glowing', 'function mg:ctf/spawn', 'function mg:ctf/kit',
                  'effect give @s minecraft:resistance 3 4 true', 'effect give @s minecraft:instant_health 1 4 true'])
w('ctf/timeout', ['# 10 min : le plus de captures gagne',
                  'execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] ' + js([{'text': "🚩 Fin de l'entraînement.", 'color': 'yellow'}]),
                  'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
                  'execute if score Rouge mg.cf > Bleu mg.cf run return run function mg:core/win_red',
                  'execute if score Bleu mg.cf > Rouge mg.cf run return run function mg:core/win_blue',
                  'function mg:core/draw'])
w('ctf/cleanup', ['function mg:ctf/kill_all', 'tag @a remove mg.cfcr', 'tag @a remove mg.cfcb',
                  'effect clear @a[tag=mg.play] minecraft:glowing', 'scoreboard players reset * mg.cf'])

C.register([93], 'ctf', [C.announce(93, '', '🚩 CAPTURE THE FLAG', 'gold', f'rouges contre bleus, {WIN} captures pour gagner !')])
C.objectives([('mg.cf', 'dummy {"text":"🚩 Drapeaux","color":"gold"}')])
C.forceload([f'# Capture the Flag (z {Z})', f'forceload add -44 {Z - 24} 44 {Z + 24}'])
print('CTF OK')
