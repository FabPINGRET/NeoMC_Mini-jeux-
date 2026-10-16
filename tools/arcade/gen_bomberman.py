"""💣 Bomberman — id 239 (chacun pour soi) et 240 (2 équipes). Arène en grille en z 40700, 2 à 8 joueurs.

    python tools/arcade/gen_bomberman.py .

- Arène 21 × 19 cases (1 case = 1 bloc), piliers indestructibles une case sur deux, briques cassables au hasard (70 %),
  zones dégagées autour des départs. Murs de 2 blocs : on ne saute pas par-dessus.
- Objet « 💣 Bombe » : clic droit = pose une bombe sur sa case (2,5 s). Elle devient un bloc solide (TNT) dès qu'on la quitte.
  Explosion en croix (portée en cases) : arrêtée par les piliers, casse la première brique, fait sauter les autres bombes
  (réaction en chaîne). Flammes 0,5 s : tout joueur dedans est éliminé (ses propres bombes comprises).
- Bonus dans les briques (30 %) : 💣 +1 bombe (8 max), 🔥 +1 portée (8 max), ⚡ vitesse (4 niveaux).
- 2 min 30 : mort subite, il pleut des bombes. 4 min max : match nul (équipes : la plus nombreuse gagne).
- Solo : dernier debout gagne. Équipes : rouges contre bleus (4 max par équipe). Seul : entraînement (touché = renvoyé au départ).
Préfixe des objectifs et tags : mg.y*. Fonctions : mg:bman/*.
"""
import sys
import common as C

C.init(sys.argv[1] if len(sys.argv) > 1 else '.')
w, js = C.w, C.js
GIDS, GIDT = 239, 240
Z = 40700
W, H = 21, 19                       # cases (x : −10..10, z : Z−9..Z+9)
X0, Z0 = -10, Z - 9
FY = 65                             # niveau des pieds (sol en y 64)
HARD, SOFT = 'stone_bricks', 'bricks'
FUSE, RAIN_T, SUDDEN, LIMIT = 50, 40, 3000, 4800
SP_SOLO = [(0, 0), (20, 18), (20, 0), (0, 18), (10, 0), (10, 18), (0, 10), (20, 8)]
SP_RED = [(0, 0), (0, 18), (0, 8), (4, 0)]
SP_BLUE = [(20, 18), (20, 0), (20, 10), (16, 18)]
PL = '@a[tag=mg.play]'
AREA = f'x={X0 - 2},y=60,z={Z0 - 2},dx={W + 3},dy=15,dz={H + 3}'


def cx(i):
    return X0 + i


def cz(j):
    return Z0 + j


safe = set()
for (i, j) in SP_SOLO + SP_RED + SP_BLUE:
    for d in range(-2, 3):
        safe.add((i + d, j))
        safe.add((i, j + d))

# ------------------------------------------------------------------ arène
B = [f'# 💣 Bomberman — arène {W}×{H} (x {cx(0)}..{cx(W - 1)}, z {cz(0)}..{cz(H - 1)}, sol y 64)',
     f'kill @e[type=!minecraft:player,{AREA}]',
     f'fill {X0 - 2} 63 {Z0 - 2} {X0 + W + 1} 72 {Z0 + H + 1} minecraft:air',
     f'fill {X0 - 1} 63 {Z0 - 1} {X0 + W} 63 {Z0 + H} minecraft:stone',
     f'fill {X0 - 1} 64 {Z0 - 1} {X0 + W} 64 {Z0 + H} minecraft:green_concrete']
B += [f'fill {X0} 64 {cz(j)} {X0 + W - 1} 64 {cz(j)} minecraft:lime_concrete' for j in range(0, H, 2)]
B += [f'fill {X0 - 1} {FY} {Z0 - 1} {X0 + W} {FY + 2} {Z0 - 1} minecraft:{HARD}', f'fill {X0 - 1} {FY} {Z0 + H} {X0 + W} {FY + 2} {Z0 + H} minecraft:{HARD}',
      f'fill {X0 - 1} {FY} {Z0} {X0 - 1} {FY + 2} {Z0 + H - 1} minecraft:{HARD}', f'fill {X0 + W} {FY} {Z0} {X0 + W} {FY + 2} {Z0 + H - 1} minecraft:{HARD}']
for i in range(W):
    for j in range(H):
        if i % 2 == 1 and j % 2 == 1:
            B.append(f'fill {cx(i)} {FY} {cz(j)} {cx(i)} {FY + 1} {cz(j)} minecraft:{HARD}')
        elif (i, j) not in safe:
            B.append(f'execute if predicate {{condition:"minecraft:random_chance",chance:0.7f}} run fill {cx(i)} {FY} {cz(j)} {cx(i)} {FY + 1} {cz(j)} minecraft:{SOFT}')
B += [f'fill {X0} {FY + 4} {Z0} {X0 + W - 1} {FY + 4} {Z0 + H - 1} minecraft:light[level=15]']
w('bman/build', B)

# ------------------------------------------------------------------ préparation
BOMB = ('minecraft:warped_fungus_on_a_stick[custom_data={ybomb:1b},item_model="minecraft:tnt",unbreakable={},custom_name='
        + js({'text': '💣 Bombe', 'color': 'red', 'bold': True, 'italic': False}) + ',lore=['
        + js({'text': 'Clic droit : poser une bombe sur ta case', 'color': 'gray', 'italic': False}) + ']]')
w('bman/prepare', [
    '# 💣 Bomberman — préparation ($ym : 0 chacun pour soi, 1 équipes)',
    'scoreboard players set $ym mg.st 0', f'execute if score $game mg.st matches {GIDT} run scoreboard players set $ym mg.st 1',
    'function mg:bman/build',
    'scoreboard players set $px mg.st 0', 'scoreboard players set $py mg.st 76', f'scoreboard players set $pz mg.st {Z}',
    f'clear {PL}', f'effect clear {PL}', f'gamemode adventure {PL}',
    f'scoreboard players set {PL} mg.yn 1', f'scoreboard players set {PL} mg.yr 2', f'scoreboard players set {PL} mg.yv 0',
    f'scoreboard players set {PL} mg.yu 0', f'scoreboard players set {PL} mg.yh 0',
    'execute if score $ym mg.st matches 1 run scoreboard players set $nt mg.st 2',
    'execute if score $ym mg.st matches 1 run function mg:core/assign_teams',
    f'execute if score $ym mg.st matches 0 run team join mg_sq {PL}',
    'scoreboard players set $yk mg.st 0', 'scoreboard players set $ykx mg.st 0', 'scoreboard players set $ykr mg.st 0', 'scoreboard players set $ykb mg.st 0',
    f'execute as {PL} run function mg:bman/spawn',
    f'execute as {PL} run function mg:bman/give',
    'tellraw @a[tag=mg.play] ' + js([{'text': '💣 BOMBERMAN : ', 'color': 'red', 'bold': True},
                                    {'text': 'clic droit avec la bombe pour la poser. L\'explosion part en croix et casse les briques ; les flammes éliminent. '
                                             'Ramasse les bonus : 💣 +1 bombe, 🔥 +1 portée, ⚡ vitesse. Attention à tes propres bombes !', 'color': 'gray'}])])


def tp_list(lst, score, fn):
    L = [f'# @s : départ n° {score}']
    for k, (i, j) in enumerate(lst):
        L.append(f'execute if score ${score} mg.st matches {k} run tp @s {cx(i) + 0.5} {FY} {cz(j) + 0.5}')
    L += [f'execute if score ${score} mg.st matches {len(lst)}.. run return run function mg:bman/extra',
          'execute at @s run spawnpoint @s ~ ~ ~', f'scoreboard players add ${score} mg.st 1']
    w(fn, L)


w('bman/spawn', ['# @s : numéro (mg.yid) et case de départ',
                 'scoreboard players add $yk mg.st 1', 'scoreboard players operation @s mg.yid = $yk mg.st',
                 'execute if score $ym mg.st matches 0 run return run function mg:bman/sp_solo',
                 'execute if entity @s[team=mg_red] run return run function mg:bman/sp_red',
                 'function mg:bman/sp_blue'])
tp_list(SP_SOLO, 'ykx', 'bman/sp_solo')
tp_list(SP_RED, 'ykr', 'bman/sp_red')
tp_list(SP_BLUE, 'ykb', 'bman/sp_blue')
w('bman/extra', ['# @s : plus de place dans l\'arène → spectateur', 'tag @s remove mg.play', 'tag @s add mg.out', 'gamemode spectator @s',
                 f'tp @s 0 76 {Z}', 'tellraw @s {"text":"💣 Arène pleine (8 joueurs, 4 par équipe) : tu regardes cette partie.","color":"gray"}'])
w('bman/give', ['# @s : la bombe (barre 1)', f'item replace entity @s hotbar.0 with {BOMB}'])
w('bman/go', ['# Départ', 'scoreboard players set $yc mg.st 0', 'scoreboard players reset @a mg.qs'])

# ------------------------------------------------------------------ jeu
w('bman/tick', [
    '# 💣 Bomberman — tick', 'scoreboard players add $yc mg.st 1',
    f'execute as @a[tag=mg.play,scores={{mg.qs=1..}}] if items entity @s weapon.mainhand *[custom_data~{{ybomb:1b}}] at @s align xz positioned ~0.5 {FY} ~0.5 run function mg:bman/place',
    'scoreboard players reset @a[scores={mg.qs=1..}] mg.qs',
    'scoreboard players remove @a[scores={mg.yh=1..}] mg.yh 1',
    'execute as @e[type=minecraft:marker,tag=mg.yb] at @s run function mg:bman/bomb_tick',
    'execute as @e[type=minecraft:marker,tag=mg.yf] at @s run function mg:bman/flame_tick',
    'execute as @e[type=minecraft:item_display,tag=mg.yp] at @s run function mg:bman/pu_tick',
    'scoreboard players operation $yq mg.st = $yc mg.st', 'scoreboard players set #20 mg.st 20', 'scoreboard players operation $yq mg.st %= #20 mg.st',
    'execute if score $yq mg.st matches 0 run function mg:bman/second',
    f'execute if score $yc mg.st matches {SUDDEN} run function mg:bman/sudden',
    f'execute if score $yc mg.st matches {SUDDEN}.. run scoreboard players operation $yq mg.st = $yc mg.st',
    'scoreboard players set #12 mg.st 12', f'execute if score $yc mg.st matches {SUDDEN}.. run scoreboard players operation $yq mg.st %= #12 mg.st',
    f'execute if score $yc mg.st matches {SUDDEN}.. if score $yq mg.st matches 0 run function mg:bman/rain',
    'execute if score $state mg.st matches 2 run function mg:bman/check',
    f'execute if score $state mg.st matches 2 if score $yc mg.st matches {LIMIT}.. run function mg:bman/time_up'])
w('bman/place', ['# @s pose une bombe (position : centre de sa case, au niveau des pieds)',
                 'execute unless block ~ ~ ~ minecraft:air run return 0',
                 'execute if entity @e[type=minecraft:marker,tag=mg.yb,distance=..0.5] run return 0',
                 'execute if score @s mg.yu >= @s mg.yn run return run title @s actionbar [{"text":"💣 Toutes tes bombes sont posées (","color":"gray"},{"score":{"name":"@s","objective":"mg.yn"},"color":"yellow"},{"text":" max)","color":"gray"}]',
                 'scoreboard players add @s mg.yu 1',
                 'summon minecraft:marker ~ ~ ~ {Tags:["mg.yb","mg.ynw"]}',
                 'scoreboard players operation @e[type=minecraft:marker,tag=mg.ynw] mg.yo = @s mg.yid',
                 'scoreboard players operation @e[type=minecraft:marker,tag=mg.ynw] mg.yr = @s mg.yr',
                 f'scoreboard players set @e[type=minecraft:marker,tag=mg.ynw] mg.yt {FUSE}',
                 'tag @e[tag=mg.ynw] remove mg.ynw', 'function mg:bman/bomb_show',
                 'playsound minecraft:entity.tnt.primed master @a ~ ~ ~ 0.8 1.2'])
w('bman/bomb_show', ['summon minecraft:item_display ~ ~0.45 ~ {Tags:["mg.yd"],item:{id:"minecraft:tnt",count:1},'
                     'transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.85f,0.85f,0.85f]}}'])
w('bman/bomb_tick', ['# @s : bombe (mg.yt = ticks avant l\'explosion) ; devient un bloc solide dès que sa case est libre',
                     'scoreboard players remove @s mg.yt 1',
                     'execute if entity @s[tag=!mg.ys] positioned ~-0.5 ~ ~-0.5 unless entity @a[gamemode=!spectator,dx=0,dy=1,dz=0] positioned ~0.5 ~ ~0.5 run function mg:bman/solid',
                     'execute if score @s mg.yt matches ..0 run return run function mg:bman/boom',
                     'scoreboard players operation $yq2 mg.st = @s mg.yt', 'scoreboard players set #5 mg.st 5', 'scoreboard players operation $yq2 mg.st %= #5 mg.st',
                     'execute if score $yq2 mg.st matches 0 run particle minecraft:smoke ~ ~1.1 ~ 0.05 0.05 0.05 0.01 2'])
w('bman/solid', ['setblock ~ ~ ~ minecraft:tnt', 'setblock ~ ~1 ~ minecraft:barrier', 'kill @e[type=minecraft:item_display,tag=mg.yd,distance=..0.6]', 'tag @s add mg.ys'])
DIRS = [('px', '~1 ~ ~'), ('nx', '~-1 ~ ~'), ('pz', '~ ~ ~1'), ('nz', '~ ~ ~-1')]
BOOM = ['# @s (bombe) explose : croix de flammes de portée mg.yr', 'tag @s add mg.yx',
        'setblock ~ ~ ~ minecraft:air', 'setblock ~ ~1 ~ minecraft:air', 'kill @e[type=minecraft:item_display,tag=mg.yd,distance=..0.6]',
        'scoreboard players operation $yo mg.st = @s mg.yo',
        'execute as @a if score @s mg.yid = $yo mg.st if score @s mg.yu matches 1.. run scoreboard players remove @s mg.yu 1',
        'playsound minecraft:entity.generic.explode master @a ~ ~ ~ 1 1.1', 'function mg:bman/flame']
for d, off in DIRS:
    BOOM += ['scoreboard players operation $yk mg.st = @s mg.yr', f'execute positioned {off} run function mg:bman/ray_{d}']
BOOM += ['kill @s']
w('bman/boom', BOOM)
for d, off in DIRS:
    w(f'bman/ray_{d}', ['# Un pas de l\'explosion',
                        f'execute if block ~ ~ ~ minecraft:{HARD} run return 0',
                        f'execute if block ~ ~ ~ minecraft:{SOFT} run return run function mg:bman/brk',
                        'execute if entity @e[type=minecraft:marker,tag=mg.yb,tag=!mg.yx,distance=..0.5] run return run function mg:bman/chain',
                        'function mg:bman/flame', 'scoreboard players remove $yk mg.st 1',
                        f'execute if score $yk mg.st matches 1.. positioned {off} run function mg:bman/ray_{d}'])
w('bman/chain', ['# Une autre bombe est touchée : elle explose au tick suivant',
                 'scoreboard players set @e[type=minecraft:marker,tag=mg.yb,tag=!mg.yx,distance=..0.5] mg.yt 1'])
w('bman/brk', ['# Brique cassée (30 % : un bonus)', 'fill ~ ~ ~ ~ ~1 ~ minecraft:air',
               f'particle minecraft:block{{block_state:"minecraft:{SOFT}"}} ~ ~0.8 ~ 0.3 0.4 0.3 0 25 force',
               'execute if predicate {condition:"minecraft:random_chance",chance:0.3f} run function mg:bman/pu_spawn'])
w('bman/flame', ['# Flamme dans cette case (0,5 s)', 'summon minecraft:marker ~ ~ ~ {Tags:["mg.yf","mg.yfn"]}',
                 'scoreboard players set @e[type=minecraft:marker,tag=mg.yfn] mg.yt 10', 'tag @e[tag=mg.yfn] remove mg.yfn',
                 'particle minecraft:explosion ~ ~0.6 ~ 0 0 0 0 1 force', 'particle minecraft:flame ~ ~0.6 ~ 0.3 0.4 0.3 0.03 10 force',
                 'kill @e[type=minecraft:item_display,tag=mg.yp,distance=..0.6]',
                 'execute positioned ~-0.5 ~ ~-0.5 as @a[tag=mg.play,gamemode=adventure,dx=0,dy=1,dz=0] run function mg:bman/hit'])
w('bman/flame_tick', ['scoreboard players remove @s mg.yt 1',
                      'execute positioned ~-0.5 ~ ~-0.5 as @a[tag=mg.play,gamemode=adventure,dx=0,dy=1,dz=0] run function mg:bman/hit',
                      'execute if score @s mg.yt matches 5 run particle minecraft:flame ~ ~0.5 ~ 0.3 0.3 0.3 0.02 6 force',
                      'execute if score @s mg.yt matches ..0 run kill @s'])
w('bman/hit', ['# @s est dans les flammes',
               'execute unless score $n0 mg.st matches 2.. run return run function mg:bman/train_hit',
               'execute at @s run particle minecraft:large_smoke ~ ~1 ~ 0.3 0.5 0.3 0.05 20 force',
               'function mg:core/eliminate'])
w('bman/train_hit', ['# Entraînement : renvoyé au départ', 'execute if score @s mg.yh matches 1.. run return 0', 'scoreboard players set @s mg.yh 30',
                     'scoreboard players add @s mg.ym 1', f'tp @s {cx(0) + 0.5} {FY} {cz(0) + 0.5}',
                     'title @s actionbar {"text":"💥 Touché ! (entraînement : retour au départ)","color":"red"}',
                     'playsound minecraft:entity.player.hurt master @s ~ ~ ~ 1 0.8'])
# bonus
PU = {1: ('tnt', '💣 +1 bombe', 'red'), 2: ('blaze_powder', '🔥 +1 portée', 'gold'), 3: ('sugar', '⚡ Vitesse', 'aqua')}
w('bman/pu_spawn', ['# Bonus au hasard dans cette case', 'execute store result score $yq3 mg.st run random value 1..3'] +
  [f'execute if score $yq3 mg.st matches {n} run summon minecraft:item_display ~ ~0.5 ~ {{Tags:["mg.yp","mg.yp{n}"],Glowing:1b,billboard:"vertical",item:{{id:"minecraft:{it}",count:1}},'
   'transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.6f,0.6f,0.6f]}}' for n, (it, _, _) in PU.items()])
w('bman/pu_tick', ['# @s : bonus au sol (ramassé en entrant dans sa case)', 'tag @s add mg.ypt',
                   'execute positioned ~-0.5 ~-0.5 ~-0.5 as @a[tag=mg.play,gamemode=adventure,dx=0,dy=1,dz=0,limit=1] run function mg:bman/pu_take',
                   'tag @s remove mg.ypt'])
w('bman/pu_take', ['# @s ramasse le bonus mg.ypt',
                   'execute if entity @e[tag=mg.ypt,tag=mg.yp1] if score @s mg.yn matches ..7 run scoreboard players add @s mg.yn 1',
                   'execute if entity @e[tag=mg.ypt,tag=mg.yp2] if score @s mg.yr matches ..7 run scoreboard players add @s mg.yr 1',
                   'execute if entity @e[tag=mg.ypt,tag=mg.yp3] if score @s mg.yv matches ..3 run function mg:bman/speed_up'] +
  [f'execute if entity @e[tag=mg.ypt,tag=mg.yp{n}] run title @s actionbar {js({"text": nm, "color": col, "bold": True})}' for n, (_, nm, col) in PU.items()] +
  ['playsound minecraft:entity.experience_orb.pickup master @s ~ ~ ~ 1 1.4', 'kill @e[tag=mg.ypt]'])
w('bman/speed_up', ['scoreboard players add @s mg.yv 1'] +
  [f'execute if score @s mg.yv matches {n} run effect give @s minecraft:speed infinite {n - 1} true' for n in range(1, 5)])
# chaque seconde
w('bman/second', ['# Chaque seconde : barre d\'action, bombe rendue si jetée, objets au sol supprimés',
                  f'kill @e[type=minecraft:item,{AREA}]',
                  f'execute as {PL} unless items entity @s container.* *[custom_data~{{ybomb:1b}}] run function mg:bman/give',
                  'scoreboard players set $ys mg.st ' + str(LIMIT // 20), 'scoreboard players operation $yq mg.st = $yc mg.st',
                  'scoreboard players operation $yq mg.st /= #20 mg.st', 'scoreboard players operation $ys mg.st -= $yq mg.st',
                  f'execute as {PL} run title @s actionbar [{{"text":"💣 ","color":"red"}},{{"score":{{"name":"@s","objective":"mg.yn"}},"color":"white","bold":true}},'
                  '{"text":"   🔥 ","color":"gold"},{"score":{"name":"@s","objective":"mg.yr"},"color":"white","bold":true},'
                  '{"text":"   ⚡ ","color":"aqua"},{"score":{"name":"@s","objective":"mg.yv"},"color":"white","bold":true},'
                  '{"text":"     ⏱ ","color":"gray"},{"score":{"name":"$ys","objective":"mg.st"},"color":"yellow"},{"text":" s","color":"gray"}]'])
w('bman/sudden', ['title @a[tag=!mg.surv] title {"text":"☠ Mort subite","color":"dark_red","bold":true}',
                  'title @a[tag=!mg.surv] subtitle {"text":"il pleut des bombes !","color":"red"}',
                  'execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.4 1.2'])
w('bman/rain', ['# Mort subite : une bombe tombe sur une case libre au hasard',
                f'execute store result storage mg:ym r.i int 1 run random value 0..{W - 1}',
                f'execute store result storage mg:ym r.j int 1 run random value 0..{H - 1}',
                'function mg:bman/rain_m with storage mg:ym r'])
w('bman/rain_m', [f'$execute positioned {cx(0) + 0.5} {FY} {cz(0) + 0.5} positioned ~$(i) ~ ~$(j) if block ~ ~ ~ minecraft:air '
                  'unless entity @e[type=minecraft:marker,tag=mg.yb,distance=..0.5] run function mg:bman/drop'])
w('bman/drop', ['summon minecraft:marker ~ ~ ~ {Tags:["mg.yb","mg.ynw"]}', 'scoreboard players set @e[type=minecraft:marker,tag=mg.ynw] mg.yo 0',
                'scoreboard players set @e[type=minecraft:marker,tag=mg.ynw] mg.yr 3',
                f'scoreboard players set @e[type=minecraft:marker,tag=mg.ynw] mg.yt {RAIN_T}', 'tag @e[tag=mg.ynw] remove mg.ynw',
                'function mg:bman/bomb_show', 'particle minecraft:cloud ~ ~3 ~ 0.2 0.2 0.2 0.02 8 force',
                'playsound minecraft:entity.tnt.primed master @a ~ ~ ~ 0.6 1.6'])
# fin
w('bman/check', ['# Fin de partie ?', 'execute unless score $n0 mg.st matches 2.. run return 0',
                 'execute if score $ym mg.st matches 1 run return run function mg:bman/check_t',
                 f'execute store result score $ya mg.st if entity {PL}',
                 f'execute if score $ya mg.st matches 1 as {PL} run return run function mg:core/win_player',
                 'execute if score $ya mg.st matches 0 run function mg:core/draw'])
w('bman/check_t', ['execute store result score $yar mg.st if entity @a[tag=mg.play,team=mg_red]',
                   'execute store result score $yab mg.st if entity @a[tag=mg.play,team=mg_blue]',
                   'execute if score $yar mg.st matches 0 if score $yab mg.st matches 0 run return run function mg:core/draw',
                   'execute if score $yar mg.st matches 0 run return run function mg:core/win_blue',
                   'execute if score $yab mg.st matches 0 run return run function mg:core/win_red'])
w('bman/time_up', ['# Temps écoulé', 'execute unless score $ym mg.st matches 1 run return run function mg:core/draw',
                   'execute if score $yar mg.st > $yab mg.st run return run function mg:core/win_red',
                   'execute if score $yab mg.st > $yar mg.st run return run function mg:core/win_blue',
                   'function mg:core/draw'])
w('bman/cleanup', ['# Fin de partie Bomberman', f'kill @e[type=!minecraft:player,{AREA}]',
                   'clear @a *[custom_data~{ybomb:1b}]', 'effect clear @a[scores={mg.yv=1..}] minecraft:speed',
                   'scoreboard players reset * mg.yid', 'scoreboard players reset * mg.yn', 'scoreboard players reset * mg.yr',
                   'scoreboard players reset * mg.yv', 'scoreboard players reset * mg.yu', 'scoreboard players reset * mg.yh',
                   'scoreboard players reset * mg.ym', 'team leave @a[team=mg_sq]', 'data remove storage mg:ym r'])

C.register([GIDS, GIDT], 'bman', [
    C.announce(GIDS, '', '💣 BOMBERMAN', 'red', 'pose des bombes, casse les briques, dernier debout gagne !'),
    C.announce(GIDT, '', '💣 BOMBERMAN — ÉQUIPES', 'red', 'rouges contre bleus, la dernière équipe debout gagne !')])
C.objectives([('mg.yid', 'dummy'), ('mg.yn', 'dummy'), ('mg.yr', 'dummy'), ('mg.yv', 'dummy'), ('mg.yu', 'dummy'),
              ('mg.yh', 'dummy'), ('mg.ym', 'dummy'), ('mg.yo', 'dummy'), ('mg.yt', 'dummy')])
C.forceload([f'# Bomberman (z {Z})', f'forceload add {X0 - 2} {Z0 - 2} {X0 + W + 1} {Z0 + H + 1}'])
print('Bomberman OK')
