"""🟩 Slime Jump — course de parkour sur blocs de slime (id 224), le premier arrivé gagne. Parcours en z 37800.

    python tools/arcade/gen_slimejump.py .

Parcours fixe d'environ 150 blocs qui descend en dénivelé (départ y 110) : on tombe sur le slime pour prendre de l'élan
et rebondir vers la corniche suivante, descente en slalom de pad en pad, petits pads 1×1, grands plongeons de 8 à 10 blocs.
4 points de passage (blocs d'émeraude) : une chute ramène au dernier. Pas de dégâts de chute.
Premier sur la plateforme d'arrivée (diamant) = victoire. 4 min max : sinon le plus avancé gagne (égalité = nul).
Seul : entraînement (chrono, match nul à l'arrivée).
"""
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
GID = 224
Z = C.param('Z', 37800)
Y0 = 110
LIMIT = 4800

# pads : (dx, dy, dz) depuis le centre du pad précédent, taille (1 ou 3), type (s = slime, p = pierre, c = point de passage)
SEQ = [
    # 1. chutes et rebonds : on tombe sur le slime pour remonter plus loin sur la corniche
    (0, -5, 6, 3, 's'), (0, 3, 6, 3, 'p'), (3, -6, 6, 3, 's'), (0, 4, 6, 3, 'p'), (-3, -5, 6, 3, 's'), (0, 3, 6, 3, 'p'),
    (0, 0, 5, 3, 'c'),
    # 2. descente en slalom : pads de slime de plus en plus bas, on garde l'élan de rebond en rebond
    (3, -3, 5, 3, 's'), (3, -3, 5, 3, 's'), (-4, -3, 5, 3, 's'), (-4, -3, 5, 3, 's'), (0, 2, 6, 3, 'p'),
    (0, 0, 5, 3, 'c'),
    # 3. petits pads 1×1 qui montent et descendent
    (0, -4, 5, 1, 's'), (-2, 2, 4, 1, 's'), (2, -3, 4, 1, 's'), (0, 2, 5, 3, 'p'),
    (0, 0, 5, 3, 'c'),
    # 4. grands plongeons : 10 et 8 blocs de chute, rebond très haut vers la corniche suivante
    (0, -10, 7, 3, 's'), (4, 7, 7, 3, 'p'), (-4, -8, 6, 3, 's'), (0, 6, 7, 3, 'p'),
    (0, 0, 5, 3, 'c'),
    # 5. final : deux rebonds en chaîne puis saut vers l'arrivée
    (3, -4, 5, 3, 's'), (-3, -2, 5, 3, 's'), (0, 4, 7, 3, 'f'),
]
pads = [(0, Y0, Z, 7, 'start')]
cx, cy, cz = 0, Y0, Z - 1
for (dx, dy, dz, size, typ) in SEQ:
    cx, cy, cz = cx + dx, cy + dy, cz + dz
    pads.append((cx, cy, cz, size, typ))
ZEND = pads[-1][2]
YMIN = min(p[1] for p in pads)
CPS = [p for p in pads if p[4] == 'c']
FIN = pads[-1]

BLK = {'s': 'slime_block', 'p': 'stone_bricks', 'c': 'emerald_block', 'f': 'diamond_block', 'start': 'polished_andesite'}
B = [f'# 🟩 Slime Jump — parcours de {len(pads)} plateformes, z {Z}..{ZEND}']
B += [f'fill -14 {y} {Z - 6} 14 {y} {ZEND + 16} minecraft:air' for y in range(min(YMIN - 4, 62), Y0 + 30)]
for (x, y, z, size, typ) in pads:
    h = size // 2
    if typ == 'start':
        B += [f'fill {x - 3} {y} {z - 4} {x + 3} {y} {z + 1} minecraft:{BLK[typ]}',
              f'fill {x - 3} {y + 1} {z - 4} {x + 3} {y + 3} {z - 4} minecraft:barrier',
              f'fill {x - 3} {y + 1} {z - 4} {x - 3} {y + 3} {z + 1} minecraft:barrier', f'fill {x + 3} {y + 1} {z - 4} {x + 3} {y + 3} {z + 1} minecraft:barrier',
              f'fill {x - 3} {y + 1} {z + 1} {x + 3} {y + 1} {z + 1} minecraft:lime_stained_glass']
        continue
    B.append(f'fill {x - h} {y} {z - h} {x + h} {y} {z + h} minecraft:{BLK[typ]}')
    if size == 3 and typ in ('s',):
        B.append(f'setblock {x} {y - 1} {z} minecraft:sea_lantern')       # dessous éclairé (repère dans le vide)
    if typ == 'f':
        B += [f'fill {x - 2} {y} {z - 2} {x + 2} {y} {z + 2} minecraft:gold_block', f'fill {x - 1} {y} {z - 1} {x + 1} {y} {z + 1} minecraft:diamond_block',
              f'setblock {x} {y - 1} {z} minecraft:beacon', f'fill {x - 1} {y - 2} {z - 1} {x + 1} {y - 2} {z + 1} minecraft:iron_block']
w('slimejump/build', B)

D = ['kill @e[tag=mg.sjd]']
for i, (x, y, z, size, typ) in enumerate(CPS, 1):
    D += [f'summon minecraft:marker {x}.5 {y + 1} {z}.5 {{Tags:["mg.sjd","mg.sjc","mg.fx"],Rotation:[0f,0f]}}',
          f'scoreboard players set @e[type=minecraft:marker,tag=mg.sjc,x={x}.5,y={y + 1},z={z}.5,distance=..0.5] mg.t {i}',
          f'summon minecraft:text_display {x}.5 {y + 2.6} {z}.5 {{Tags:["mg.sjd","mg.fx"],billboard:"center",background:0,'
          f'text:{{"text":"✔ {i}/{len(CPS)}","color":"green","bold":true}},transformation:{{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}}}']
fx, fy, fz = FIN[0], FIN[1], FIN[2]
D += [f'summon minecraft:text_display {fx}.5 {fy + 3.5} {fz}.5 {{Tags:["mg.sjd","mg.fx"],billboard:"center",background:0,'
      'text:{"text":"🏁 ARRIVÉE","color":"aqua","bold":true},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}',
      f'summon minecraft:marker 0.5 {Y0 + 1} {Z - 1}.5 {{Tags:["mg.sjd","mg.sjc","mg.sjs","mg.fx"],Rotation:[0f,0f]}}',
      f'scoreboard players set @e[type=minecraft:marker,tag=mg.sjs] mg.t 0']
w('slimejump/deco', D)

PL = '@a[tag=mg.play]'
w('slimejump/prepare', ['# 🟩 Slime Jump — préparation', 'function mg:slimejump/build', 'function mg:slimejump/deco',
                        'scoreboard players set $px mg.st 0', f'scoreboard players set $py mg.st {Y0 + 12}', f'scoreboard players set $pz mg.st {Z + 60}',
                        f'clear {PL}', f'effect clear {PL}', f'gamemode adventure {PL}', f'team join mg_sq {PL}',
                        f'scoreboard players set {PL} mg.sjp 0', 'scoreboard players set $sjt mg.st 0',
                        f'spreadplayers 0 {Z - 1} 1 2 under {Y0 + 3} false {PL}',
                        f'execute as {PL} at @s run tp @s ~ ~ ~ 0 0', f'execute as {PL} at @s run spawnpoint @s ~ ~ ~'])
w('slimejump/go', ['# Départ', 'scoreboard players set $sjt mg.st 0',
                   f'fill -2 {Y0 + 1} {Z + 1} 2 {Y0 + 1} {Z + 1} minecraft:air',
                   f'bossbar add mg:slimejump {js({"text": "🟩 Slime Jump", "color": "green"})}', 'bossbar set mg:slimejump color green',
                   f'bossbar set mg:slimejump max {LIMIT}', f'bossbar set mg:slimejump players {PL}',
                   f'tellraw {PL} ' + js([{'text': '🟩 SLIME JUMP : ', 'color': 'green', 'bold': True},
                                           {'text': f'saute de slime en slime jusqu\'à l\'arrivée (diamant) ! Rebondis plusieurs fois pour monter aux corniches. '
                                                    f'{len(CPS)} points de passage en émeraude : une chute ramène au dernier. Le premier arrivé gagne.', 'color': 'gray'}])])
w('slimejump/cp', ['# @s touche un point de passage (mg.t du marqueur le plus proche)',
                   'execute store result score $c mg.st run scoreboard players get @e[type=minecraft:marker,tag=mg.sjc,sort=nearest,limit=1] mg.t',
                   'execute unless score $c mg.st > @s mg.sjp run return 0',
                   'scoreboard players operation @s mg.sjp = $c mg.st',
                   'execute at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 1.6',
                   f'tellraw @a[tag=mg.play] [{{"text":"✔ ","color":"green"}},{{"selector":"@s","color":"yellow"}},{{"text":" passe le point ","color":"gray"}},'
                   f'{{"score":{{"name":"$c","objective":"mg.st"}},"color":"green","bold":true}},{{"text":"/{len(CPS)}","color":"green"}}]'])
w('slimejump/fall', ['# @s est tombé : retour au dernier point de passage',
                     'scoreboard players operation $c mg.st = @s mg.sjp',
                     'execute as @e[type=minecraft:marker,tag=mg.sjc] if score @s mg.t = $c mg.st run tag @s add mg.sjx',
                     'tp @s @e[type=minecraft:marker,tag=mg.sjx,limit=1]', 'tag @e[tag=mg.sjx] remove mg.sjx',
                     'execute at @s run playsound minecraft:entity.slime.squish master @s ~ ~ ~ 1 0.7',
                     'title @s actionbar {"text":"💧 Plouf ! Retour au dernier point","color":"aqua"}'])
w('slimejump/finish', ['# @s atteint l\'arrivée',
                       'scoreboard players operation $s mg.st = $sjt mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $s mg.st /= #20 mg.st',
                       'tellraw @a [{"text":"🏁 ","color":"aqua"},{"selector":"@s","color":"yellow","bold":true},{"text":" arrive en premier en ","color":"aqua"},'
                       '{"score":{"name":"$s","objective":"mg.st"},"color":"yellow"},{"text":" s !","color":"aqua"}]',
                       'execute at @s run summon minecraft:firework_rocket ~ ~1 ~ {LifeTime:20,FireworksItem:{id:"minecraft:firework_rocket",count:1,components:{"minecraft:fireworks":{explosions:[{shape:"star",colors:[I;65280,16776960]}]}}}}',
                       'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
                       'function mg:core/win_player'])
w('slimejump/tick', ['# 🟩 Slime Jump — tick', 'scoreboard players add $sjt mg.st 1',
                     'execute store result bossbar mg:slimejump value run scoreboard players get $sjt mg.st',
                     f'execute as {PL} at @s if block ~ ~-0.5 ~ minecraft:emerald_block run function mg:slimejump/cp',
                     f'execute as {PL} at @s if entity @s[y=-64,dy={YMIN - 6 + 64}] run function mg:slimejump/fall',
                     f'execute if score $state mg.st matches 2 as {PL} at @s if block ~ ~-0.5 ~ minecraft:diamond_block run return run function mg:slimejump/finish',
                     f'execute if score $state mg.st matches 2 as {PL} at @s if block ~ ~-0.5 ~ minecraft:gold_block if entity @s[x={fx - 3},y={fy},z={fz - 3},dx=6,dy=3,dz=6] run return run function mg:slimejump/finish',
                     f'execute if score $state mg.st matches 2 if score $sjt mg.st matches {LIMIT}.. run function mg:slimejump/timeout'])
w('slimejump/timeout', ['# 4 min : le plus avancé gagne (égalité = nul)',
                        'tellraw @a[tag=mg.play] {"text":"⏰ Temps écoulé !","color":"red","bold":true}',
                        'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
                        'scoreboard players set $b mg.st -1', 'scoreboard players operation $b mg.st > @a[tag=mg.play] mg.sjp',
                        'tag @a remove mg.sjw', 'execute as @a[tag=mg.play] if score @s mg.sjp = $b mg.st run tag @s add mg.sjw',
                        'execute store result score $c mg.st if entity @a[tag=mg.sjw]',
                        'execute if score $c mg.st matches 1 as @a[tag=mg.sjw,limit=1] run return run function mg:core/win_player',
                        'function mg:core/draw'])
w('slimejump/cleanup', ['bossbar remove mg:slimejump', 'kill @e[tag=mg.sjd]', 'tag @a remove mg.sjw', 'team leave @a[team=mg_sq]'])

C.register([GID], 'slimejump', [C.announce(GID, '', '🟩 SLIME JUMP', 'green', 'parkour de rebonds sur slime, le premier arrivé gagne !')])
C.objectives([('mg.sjp', 'dummy')])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw', ['bossbar remove mg:slimejump'])
C.forceload([f'# Slime Jump (z {Z})', f'forceload add -14 {Z - 6} 14 {ZEND + 16}'])
print('Slime Jump OK :', len(pads), 'plateformes, arrivée en z', ZEND, 'y', FIN[1], '— points de passage', len(CPS))
