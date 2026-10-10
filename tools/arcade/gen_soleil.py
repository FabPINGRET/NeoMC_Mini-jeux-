"""🔴 1, 2, 3… Soleil ! (façon Squid Game) — id 220. Terrain de sable 41×80 en z 37000, poupée géante au bout.

    python tools/arcade/gen_soleil.py .

Règles :
- Tout le monde part de la ligne de départ (sud) et doit franchir la ligne rouge (z +80) avant la fin du temps (1 min 30).
- Feu vert : la poupée tourne le dos (« 1, 2, 3… »), on avance. Feu rouge : elle se retourne (« SOLEIL ! ») :
  qui bouge (plus de 0,08 bloc, saut compris) après 0,5 s de grâce est éliminé (tir).
- Les feux verts raccourcissent avec le temps. Collisions et coups désactivés (équipe mg_sq) : personne ne peut pousser.
- Temps écoulé : tous ceux qui ne sont pas arrivés sont éliminés. Vainqueur = le premier arrivé (les suivants sont classés).
- Seul : entraînement (fin à l'arrivée ou au temps, match nul).
"""
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
GID = 220
Z = C.param('Z', 37000)
X1, X2 = -20, 20                 # intérieur du terrain
ZS, ZF, ZE = Z + 2, Z + 80, Z + 96   # ligne de départ, ligne d'arrivée, fond (poupée en Z+90)
DOLL = (0, 66, Z + 90)
LIMIT = 1800                     # 1 min 30
TF = 'transformation:{{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[{tx}f,{ty}f,{tz}f],scale:[{sx}f,{sy}f,{sz}f]}}'

# ------------------------------------------------------------------ construction
B = [f'# 🔴 1, 2, 3 Soleil — terrain 41×80 (z {Z}), poupée en {DOLL}']
B += [f'fill {X1 - 2} {y} {Z - 3} {X2 + 2} {y} {ZE + 2} minecraft:air' for y in range(62, 84)]
B += [f'fill {X1} 63 {Z} {X2} 63 {ZE} minecraft:sandstone', f'fill {X1} 64 {Z} {X2} 64 {ZE} minecraft:sand',
      # lignes de départ (blanche) et d'arrivée (rouge)
      f'fill {X1} 64 {ZS - 1} {X2} 64 {ZS - 1} minecraft:white_concrete', f'fill {X1} 64 {ZF} {X2} 64 {ZF} minecraft:red_concrete',
      f'fill {X1} 64 {ZF + 1} {X2} 64 {ZE} minecraft:smooth_sandstone',
      # murs « ciel peint » (bas sable, haut bleu ciel avec nuages), plafond invisible
      f'fill {X1 - 1} 63 {Z - 1} {X1 - 1} 80 {ZE + 1} minecraft:light_blue_concrete', f'fill {X2 + 1} 63 {Z - 1} {X2 + 1} 80 {ZE + 1} minecraft:light_blue_concrete',
      f'fill {X1 - 1} 63 {Z - 1} {X2 + 1} 80 {Z - 1} minecraft:light_blue_concrete', f'fill {X1 - 1} 63 {ZE + 1} {X2 + 1} 80 {ZE + 1} minecraft:light_blue_concrete',
      f'fill {X1 - 1} 63 {Z - 1} {X1 - 1} 67 {ZE + 1} minecraft:smooth_sandstone', f'fill {X2 + 1} 63 {Z - 1} {X2 + 1} 67 {ZE + 1} minecraft:smooth_sandstone',
      f'fill {X1 - 1} 63 {Z - 1} {X2 + 1} 67 {Z - 1} minecraft:smooth_sandstone', f'fill {X1 - 1} 63 {ZE + 1} {X2 + 1} 67 {ZE + 1} minecraft:smooth_sandstone',
      f'fill {X1 - 1} 81 {Z - 1} {X2 + 1} 81 {ZE + 1} minecraft:barrier']
CLOUDS = [(-1, 74, 10, 6, 2), (1, 76, 40, 8, 2), (-1, 72, 62, 5, 2), (1, 75, 22, 4, 1), (-1, 77, 85, 7, 2), (1, 73, 70, 6, 2)]
for side, y, dz, ln, h in CLOUDS:
    x = X1 - 1 if side < 0 else X2 + 1
    B.append(f'fill {x} {y} {Z + dz} {x} {y + h - 1} {Z + dz + ln} minecraft:white_concrete')
for (x, y, ln) in ((-14, 75, 7), (6, 77, 9), (-2, 72, 5)):
    B.append(f'fill {x} {y} {ZE + 1} {x + ln} {y + 1} {ZE + 1} minecraft:white_concrete')
# estrade de la poupée et arbre derrière
dx_, dy_, dz_ = DOLL
B += [f'fill -4 64 {dz_ - 3} 4 65 {dz_ + 3} minecraft:smooth_sandstone', f'fill -5 64 {dz_ - 4} 5 64 {dz_ + 4} minecraft:cut_sandstone',
      f'fill -1 65 {dz_ + 5} 0 74 {dz_ + 5} minecraft:oak_log', f'fill -5 72 {dz_ + 3} 4 76 {dz_ + 6} minecraft:oak_leaves[persistent=true]',
      f'fill -3 77 {dz_ + 4} 2 77 {dz_ + 5} minecraft:oak_leaves[persistent=true]', f'fill -1 72 {dz_ + 5} 0 74 {dz_ + 5} minecraft:oak_log',
      # barrière basse devant la poupée (on ne la touche pas)
      f'fill {X1} 65 {ZF + 6} {X2} 65 {ZF + 6} minecraft:barrier']
w('soleil/build', B)

# poupée : parties en block_display au même point (la rotation de l'entité les fait tourner ensemble) ; face = +z local
PARTS = [  # bloc, (x, y, z) coin, (sx, sy, sz), tags en plus
    ('white_wool', (-1.6, 0, -0.5), (1.2, 0.8, 1.0)), ('white_wool', (0.4, 0, -0.5), (1.2, 0.8, 1.0)),
    ('white_terracotta', (-1.4, 0.8, -0.4), (0.9, 2.6, 0.8)), ('white_terracotta', (0.5, 0.8, -0.4), (0.9, 2.6, 0.8)),
    ('orange_concrete', (-2.4, 3.2, -1.3), (4.8, 3.4, 2.6)), ('orange_concrete', (-2.0, 6.4, -1.1), (4.0, 0.6, 2.2)),
    ('yellow_concrete', (-1.6, 6.9, -0.9), (3.2, 2.0, 1.8)),
    ('yellow_concrete', (-2.5, 7.6, -0.6), (0.9, 1.3, 1.2)), ('yellow_concrete', (1.6, 7.6, -0.6), (0.9, 1.3, 1.2)),
    ('white_terracotta', (-2.45, 4.9, -0.5), (0.8, 2.7, 1.0)), ('white_terracotta', (1.65, 4.9, -0.5), (0.8, 2.7, 1.0)),
    ('white_terracotta', (-0.5, 8.9, -0.5), (1.0, 0.4, 1.0)),
    ('white_terracotta', (-1.6, 9.2, -1.5), (3.2, 3.2, 3.0)),
    ('black_concrete', (-1.75, 12.3, -1.65), (3.5, 0.6, 3.3)), ('black_concrete', (-1.75, 9.6, -1.75), (3.5, 2.8, 0.3)),
    ('black_concrete', (-1.85, 10.2, -1.6), (0.3, 2.2, 2.0)), ('black_concrete', (1.55, 10.2, -1.6), (0.3, 2.2, 2.0)),
    ('black_concrete', (-2.7, 10.6, -1.0), (0.9, 1.6, 0.9)), ('black_concrete', (1.8, 10.6, -1.0), (0.9, 1.6, 0.9)),
    ('black_concrete', (-1.3, 12.0, 1.45), (2.6, 0.4, 0.1)),
    ('pink_concrete', (-1.4, 9.85, 1.48), (0.5, 0.3, 0.05)), ('pink_concrete', (0.9, 9.85, 1.48), (0.5, 0.3, 0.05)),
    ('red_concrete', (-0.35, 9.55, 1.49), (0.7, 0.15, 0.05)),
]
EYES = [(-1.0, 10.6, 1.5), (0.5, 10.6, 1.5)]
D = ['kill @e[tag=mg.sqd]']
for blk, (tx, ty, tz), (sx, sy, sz) in PARTS:
    D.append(f'summon minecraft:block_display {dx_} {dy_} {dz_} {{Tags:["mg.sqd","mg.fx"],Rotation:[0f,0f],teleport_duration:6,view_range:4f,'
             f'block_state:{{Name:"minecraft:{blk}"}},' + TF.format(tx=tx, ty=ty, tz=tz, sx=sx, sy=sy, sz=sz) + '}')
for (tx, ty, tz) in EYES:
    D.append(f'summon minecraft:block_display {dx_} {dy_} {dz_} {{Tags:["mg.sqd","mg.sqeye","mg.fx"],Rotation:[0f,0f],teleport_duration:6,view_range:4f,'
             'brightness:{sky:15,block:15},block_state:{Name:"minecraft:black_concrete"},' + TF.format(tx=tx, ty=ty, tz=tz, sx=0.5, sy=0.5, sz=0.06) + '}')
w('soleil/doll', ['# Poupée (de dos au départ : regarde vers le sud, loin des joueurs)'] + D)
w('soleil/turn', ['# $(yaw) : 0 = de dos (feu vert), 180 = face aux joueurs (feu rouge)',
                  f'$execute as @e[tag=mg.sqd] run tp @s {dx_} {dy_} {dz_} $(yaw) 0'])

# ------------------------------------------------------------------ partie
PL = '@a[tag=mg.play]'
AL = '@a[tag=mg.play,tag=!mg.sqf]'            # encore en course
w('soleil/prepare', ['# 🔴 1, 2, 3 Soleil — préparation', 'function mg:soleil/build', 'function mg:soleil/doll',
                     'kill @e[tag=mg.sqs]'] +
  [f'summon minecraft:marker {x}.5 65 {ZS}.5 {{Tags:["mg.sqs","mg.fx"],Rotation:[0f,0f]}}' for x in range(X1 + 2, X2 - 1, 2)] +
  ['scoreboard players set $px mg.st 0', 'scoreboard players set $py mg.st 86', f'scoreboard players set $pz mg.st {Z + 45}',
   f'clear {PL}', f'effect clear {PL}', f'gamemode adventure {PL}', f'team join mg_sq {PL}',
   f'tag {PL} remove mg.sqf', 'tag @e remove mg.squ',
   f'execute as {PL} run function mg:soleil/place',
   'scoreboard players set $sqn mg.st 0', 'scoreboard players set $sqe mg.st 0'])
w('soleil/place', ['# @s : une place libre sur la ligne de départ (toutes prises : on recommence)',
                   'execute unless entity @e[type=minecraft:marker,tag=mg.sqs,tag=!mg.squ] run tag @e[tag=mg.sqs] remove mg.squ',
                   'tag @e[type=minecraft:marker,tag=mg.sqs,tag=!mg.squ,sort=random,limit=1] add mg.sqp',
                   'tp @s @e[type=minecraft:marker,tag=mg.sqp,limit=1]', 'execute at @s run spawnpoint @s ~ ~ ~',
                   'tag @e[tag=mg.sqp] add mg.squ', 'tag @e[tag=mg.sqp] remove mg.sqp'])
w('soleil/go', ['# Départ', 'scoreboard players set $sqt mg.st 0', 'scoreboard players set $sqc mg.st 0',
                f'bossbar add mg:soleil {js({"text": "🔴 1, 2, 3 Soleil", "color": "red"})}', 'bossbar set mg:soleil color red',
                f'bossbar set mg:soleil max {LIMIT}', f'bossbar set mg:soleil players {PL}',
                'function mg:soleil/green',
                f'tellraw {PL} ' + js([{'text': '🔴 1, 2, 3… SOLEIL ! ', 'color': 'red', 'bold': True},
                                        {'text': 'Avance quand la poupée a le dos tourné. Quand elle se retourne (« SOLEIL ! »), ne bouge plus : '
                                                 'le moindre mouvement, même un saut, et tu es éliminé. Franchis la ligne rouge avant la fin (1 min 30) !',
                                         'color': 'gray'}])])
w('soleil/green', ['# Feu vert : la poupée tourne le dos ; durée au hasard (plus courte avec le temps)',
                   'scoreboard players set $sqp mg.st 0', 'function mg:soleil/turn {yaw:0}',
                   'execute as @e[tag=mg.sqeye] run data merge entity @s {block_state:{Name:"minecraft:black_concrete"}}',
                   'execute store result score $sqt mg.st run random value 35..90',
                   'execute if score $sqc mg.st matches 600.. store result score $sqt mg.st run random value 25..65',
                   'execute if score $sqc mg.st matches 1200.. store result score $sqt mg.st run random value 15..45',
                   f'title {PL} times 0 30 5', f'title {PL} title {{"text":"1, 2, 3…","color":"green","bold":true}}',
                   f'title {PL} subtitle {{"text":"avance !","color":"gray"}}',
                   f'execute as {PL} at @s run playsound minecraft:block.note_block.chime master @s ~ ~ ~ 0.8 0.8'])
w('soleil/red', ['# Feu rouge : la poupée se retourne, 0,5 s de grâce', 'scoreboard players set $sqp mg.st 1', 'scoreboard players set $sqt mg.st 10',
                 'function mg:soleil/turn {yaw:180}',
                 f'title {PL} times 0 25 5', f'title {PL} title {{"text":"SOLEIL !","color":"red","bold":true}}',
                 f'title {PL} subtitle {{"text":"ne bouge plus","color":"gray"}}',
                 f'execute as {PL} at @s run playsound minecraft:entity.elder_guardian.curse master @s ~ ~ ~ 0.4 1.6'])
w('soleil/watch', ['# La poupée regarde : positions notées, toute la durée du feu rouge', 'scoreboard players set $sqp mg.st 2',
                   'execute store result score $sqt mg.st run random value 40..80',
                   'execute as @e[tag=mg.sqeye] run data merge entity @s {block_state:{Name:"minecraft:redstone_block"}}',
                   f'execute as {AL} run function mg:soleil/mark'])
w('soleil/mark', ['execute store result score @s mg.sqx run data get entity @s Pos[0] 100',
                  'execute store result score @s mg.sqy run data get entity @s Pos[1] 100',
                  'execute store result score @s mg.sqz run data get entity @s Pos[2] 100'])
w('soleil/check', ['# @s pendant le feu rouge : bougé de plus de 0,08 bloc (ou sauté) → éliminé',
                   'execute store result score $a mg.st run data get entity @s Pos[0] 100', 'scoreboard players operation $a mg.st -= @s mg.sqx',
                   'execute unless score $a mg.st matches -8..8 run return run function mg:soleil/shot',
                   'execute store result score $a mg.st run data get entity @s Pos[2] 100', 'scoreboard players operation $a mg.st -= @s mg.sqz',
                   'execute unless score $a mg.st matches -8..8 run return run function mg:soleil/shot',
                   'execute store result score $a mg.st run data get entity @s Pos[1] 100', 'scoreboard players operation $a mg.st -= @s mg.sqy',
                   'execute unless score $a mg.st matches -15..15 run return run function mg:soleil/shot'])
w('soleil/shot', ['# @s a bougé : tir', 'execute at @s run particle minecraft:dust{color:[0.8,0.0,0.0],scale:2.0} ~ ~1 ~ 0.3 0.6 0.3 0 40 force',
                  'execute at @s run particle minecraft:explosion ~ ~1 ~ 0 0 0 0 1 force',
                  f'execute as @a[tag=!mg.surv] at @s if entity @s[x=-30,y=40,z={Z - 10},dx=60,dy=60,dz=120] run playsound minecraft:entity.firework_rocket.blast master @s ~ ~ ~ 1 0.5',
                  'tellraw @a[tag=!mg.surv] [{"text":"💥 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" a bougé !","color":"red"}]',
                  'scoreboard players add $sqe mg.st 1',
                  'execute if score $n0 mg.st matches 2.. run return run function mg:core/eliminate',
                  # seul : retour au départ
                  'function mg:soleil/place', 'function mg:soleil/mark', 'title @s actionbar {"text":"💥 Tu as bougé : retour au départ (entraînement)","color":"red"}'])
w('soleil/finish', ['# @s franchit la ligne rouge', 'tag @s add mg.sqf', 'scoreboard players add $sqn mg.st 1',
                    'execute if score $sqn mg.st matches 1 run tag @s add mg.sq1',
                    'scoreboard players operation $s mg.st = $sqc mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $s mg.st /= #20 mg.st',
                    'tellraw @a[tag=!mg.surv] [{"text":"🏁 #","color":"green"},{"score":{"name":"$sqn","objective":"mg.st"},"color":"green","bold":true},'
                    '{"text":" ","color":"green"},{"selector":"@s","color":"yellow"},{"text":" franchit la ligne en ","color":"gray"},'
                    '{"score":{"name":"$s","objective":"mg.st"},"color":"yellow"},{"text":" s","color":"gray"}]',
                    'effect give @s minecraft:resistance infinite 4 true', 'execute at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.7 1.2'])
w('soleil/tick', ['# 🔴 1, 2, 3 Soleil — tick', 'scoreboard players add $sqc mg.st 1', 'scoreboard players remove $sqt mg.st 1',
                  'execute store result bossbar mg:soleil value run scoreboard players get $sqc mg.st',
                  f'execute as @a[tag=mg.play,tag=!mg.sqf,x={X1 - 1},y=55,z={ZF},dx={X2 - X1 + 2},dy=30,dz={ZE - ZF + 2}] run function mg:soleil/finish',
                  'execute if score $sqp mg.st matches 0 if score $sqt mg.st matches ..0 run function mg:soleil/red',
                  'execute if score $sqp mg.st matches 1 if score $sqt mg.st matches ..0 run function mg:soleil/watch',
                  f'execute if score $sqp mg.st matches 2 as {AL} run function mg:soleil/check',
                  'execute if score $sqp mg.st matches 2 if score $sqt mg.st matches ..0 run function mg:soleil/green',
                  # sur le terrain : chute impossible, mais un joueur hors zone revient au départ
                  f'execute as {AL} unless entity @s[x={X1 - 3},y=55,z={Z - 3},dx={X2 - X1 + 6},dy=30,dz={ZE - Z + 6}] run function mg:soleil/place',
                  'scoreboard players operation $q mg.st = $sqc mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $q mg.st %= #20 mg.st',
                  'execute if score $q mg.st matches 0 run function mg:soleil/second',
                  'execute store result score $a mg.st if entity ' + AL,
                  'execute if score $state mg.st matches 2 if score $a mg.st matches 0 run return run function mg:soleil/end',
                  f'execute if score $state mg.st matches 2 if score $sqc mg.st matches {LIMIT}.. run function mg:soleil/timeout'])
w('soleil/second', [f'scoreboard players set $l mg.st {LIMIT // 20}', 'scoreboard players operation $s mg.st = $sqc mg.st',
                    'scoreboard players operation $s mg.st /= #20 mg.st', 'scoreboard players operation $l mg.st -= $s mg.st',
                    'execute store result storage mg:sq b.l int 1 run scoreboard players get $l mg.st',
                    'execute store result storage mg:sq b.n int 1 run scoreboard players get $sqn mg.st',
                    'function mg:soleil/bar with storage mg:sq b',
                    'execute if score $l mg.st matches 10 run tellraw @a[tag=mg.play] {"text":"⏳ Plus que 10 secondes !","color":"gold","bold":true}'])
w('soleil/bar', ['$bossbar set mg:soleil name [{"text":"🔴 1, 2, 3 Soleil — ","color":"red"},{"text":"$(l) s","color":"yellow","bold":true},'
                 '{"text":" — arrivés : $(n)","color":"green"}]'])
w('soleil/timeout', ['# Temps écoulé : ceux qui ne sont pas arrivés sont éliminés',
                     f'tellraw {PL} {{"text":"⏰ Temps écoulé !","color":"red","bold":true}}', 'function mg:soleil/turn {yaw:180}',
                     f'execute if score $n0 mg.st matches 2.. as {AL} run function mg:soleil/shot',
                     'function mg:soleil/end'])
w('soleil/end', ['# Fin : le premier arrivé gagne (seul : match nul)',
                 'execute unless score $state mg.st matches 2 run return 0',
                 'execute unless score $n0 mg.st matches 2.. run tellraw @a[tag=mg.play] [{"text":"🔴 Fin de l\'entraînement : ","color":"yellow"},'
                 '{"score":{"name":"$sqn","objective":"mg.st"},"color":"yellow","bold":true},{"text":" arrivée(s).","color":"yellow"}]',
                 'execute unless score $n0 mg.st matches 2.. run return run function mg:core/draw',
                 'execute if score $sqn mg.st matches 0 run tellraw @a {"text":"🔴 Personne n\'a franchi la ligne…","color":"red"}',
                 'execute if score $sqn mg.st matches 0 run return run function mg:core/draw',
                 'execute as @a[tag=mg.sq1,limit=1] run function mg:core/win_player',
                 'execute if score $state mg.st matches 2 run function mg:core/draw'])
w('soleil/cleanup', ['bossbar remove mg:soleil', 'kill @e[tag=mg.sqd]', 'kill @e[tag=mg.sqs]', 'tag @a remove mg.sqf', 'tag @a remove mg.sq1',
                     'team leave @a[team=mg_sq]', 'effect clear @a[tag=mg.play] minecraft:resistance'])

C.register([GID], 'soleil', [C.announce(GID, '', '🔴 1, 2, 3 SOLEIL', 'red', 'avance quand la poupée a le dos tourné, ne bouge plus quand elle te regarde !')])
C.objectives([('mg.sqx', 'dummy'), ('mg.sqy', 'dummy'), ('mg.sqz', 'dummy')])
C.patch('core/load', 'scoreboard objectives add mg.bw trigger',
        ['team add mg_sq', 'team modify mg_sq friendlyFire false', 'team modify mg_sq collisionRule never', 'team modify mg_sq nametagVisibility always'])
C.patch('desinstaller', 'scoreboard objectives remove mg.bw', ['bossbar remove mg:soleil', 'team remove mg_sq', 'data remove storage mg:sq b'])
C.forceload([f'# 1, 2, 3 Soleil (z {Z})', f'forceload add {X1 - 3} {Z - 4} {X2 + 3} {ZE + 3}'])
print('1, 2, 3 Soleil OK')
