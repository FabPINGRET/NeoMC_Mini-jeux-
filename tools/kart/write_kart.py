"""Écrit le moteur de kart (fonctions écrites à la main) : python write_kart.py <racine du dépôt>."""
import json, os, sys

R = sys.argv[1]
DATA = os.path.join(R, 'data')
K = os.path.join(DATA, 'mg', 'function', 'kart')
os.makedirs(K, exist_ok=True)

def wr(path, txt):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8', newline='\n').write(txt)
def fn(name, txt): wr(os.path.join(K, name + '.mcfunction'), txt)

# ------------------------------------------------------------------ prédicats (touches) et tags de blocs
for key, inp in (('f', 'forward'), ('b', 'backward'), ('l', 'left'), ('r', 'right'), ('j', 'jump')):
    wr(os.path.join(DATA, f'mg/predicate/kart_{key}.json'), json.dumps(
        {"condition": "minecraft:entity_properties", "entity": "this",
         "predicate": {"minecraft:type_specific/player": {"input": {inp: True}}}}, indent=2) + '\n')
wr(os.path.join(DATA, 'mg/tags/block/kart_pass.json'), json.dumps({"values": [
    "minecraft:air", "minecraft:cave_air", "minecraft:void_air", "minecraft:water", "minecraft:short_grass", "minecraft:tall_grass",
    "minecraft:fern", "#minecraft:small_flowers", "minecraft:light", "minecraft:snow", "#minecraft:wool_carpets"]}, indent=2) + '\n')
wr(os.path.join(DATA, 'mg/tags/block/kart_road.json'), json.dumps({"values": [
    "minecraft:gray_concrete", "minecraft:white_concrete", "minecraft:red_concrete", "minecraft:black_concrete",
    "minecraft:orange_glazed_terracotta", "minecraft:lime_concrete", "minecraft:stone_bricks"]}, indent=2) + '\n')

COLORS = ['red', 'blue', 'lime', 'yellow', 'purple', 'orange', 'cyan', 'pink']
T0 = 'left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]'
KS = 0.75   # taille du kart (1 = modèle d'origine)
def ks(v): return round(v * KS, 3)
def part(block, tr, sc):
    return ('{id:"minecraft:block_display",Tags:["mg.kpart","mg.fx"],teleport_duration:1,block_state:{Name:"minecraft:%s"},'
            'transformation:{translation:[%sf,%sf,%sf],%s,scale:[%sf,%sf,%sf]}}' % (block, *map(ks, tr), T0, *map(ks, sc)))
PASSENGERS = ','.join([
    part('black_concrete', (-0.78, 0.0, 0.45), (1.56, 0.42, 0.42)),     # roues avant
    part('black_concrete', (-0.78, 0.0, -0.85), (1.56, 0.42, 0.42)),    # roues arrière
    part('gray_concrete', (-0.4, 0.5, -0.75), (0.8, 0.5, 0.2)),         # dossier
    part('light_gray_concrete', (-0.08, 0.5, 0.45), (0.16, 0.35, 0.16)),  # colonne de direction
])

# ------------------------------------------------------------------ préparation, départ, fin
fn('prepare', '''# Kart : préparation pendant le compte à rebours (zone chargée, pilotes sur la grille, karts posés 2 s après)
function mg:kart/const
function mg:kart/fl_add
scoreboard players set #km1 mg.st -1
scoreboard players set #k3 mg.st 3
scoreboard players set #k4 mg.st 4
scoreboard players set #k5 mg.st 5
scoreboard players set #k72 mg.st 72
scoreboard players set #k100 mg.st 100
scoreboard players set #k8 mg.st 8
scoreboard players set #k20 mg.st 20
scoreboard players set #k1000 mg.st 1000
scoreboard players set $px mg.st 0
scoreboard players set $py mg.st 110
scoreboard players set $pz mg.st 16500
scoreboard players set $ktime mg.st 0
scoreboard players set $kfo mg.st 0
scoreboard players set $kend mg.st 0
scoreboard players set $kph mg.st 0
scoreboard players set $gi mg.st 0
kill @e[tag=mg.ib]
kill @e[tag=mg.kpart]
gamemode adventure @a[tag=mg.play]
clear @a[tag=mg.play]
tag @a remove mg.kfin
scoreboard players set @a[tag=mg.play] mg.ksp 0
scoreboard players set @a[tag=mg.play] mg.kdr 0
scoreboard players set @a[tag=mg.play] mg.kbo 0
scoreboard players set @a[tag=mg.play] mg.khi 0
scoreboard players set @a[tag=mg.play] mg.kst 0
scoreboard players set @a[tag=mg.play] mg.kit 0
scoreboard players set @a[tag=mg.play] mg.kcp 0
scoreboard players set @a[tag=mg.play] mg.klp 0
scoreboard players set @a[tag=mg.play] mg.kvy 0
scoreboard players set @a[tag=mg.play] mg.kfp 0
scoreboard players set @a[tag=mg.play] mg.kps 0
scoreboard players reset @a mg.qs
execute as @a[tag=mg.play] run function mg:kart/place_one
scoreboard objectives setdisplay sidebar mg.kps
schedule function mg:kart/place_all 40t
''')
fn('place_one', '''# Pilote @s : n° de grille, téléporté à sa place
scoreboard players add $gi mg.st 1
scoreboard players operation @s mg.ri = $gi mg.st
function mg:kart/grid_tp
''')
fn('place_all', '''# Dès que la zone est chargée (vérifié toutes les 0,5 s) : portillon, boîtes à objets, un kart sous chaque pilote
execute unless score $game mg.st matches 61 run return 0
execute unless score $state mg.st matches 1..2 run return 0
execute unless function mg:kart/loaded_all run return run schedule function mg:kart/place_all 10t
function mg:kart/gate_on
function mg:kart/boxes
execute as @a[tag=mg.play] at @s run function mg:kart/kart_new
''')
fn('kart_new', '''# Nouveau kart pour @s (pilote), à sa position et dans sa direction, puis le pilote monte dedans
summon minecraft:block_display ~ ~ ~ {Tags:["mg.ib","mg.kart","mg.mine"],teleport_duration:1,block_state:{Name:"minecraft:red_concrete"},transformation:{translation:[%sf,%sf,%sf],%s,scale:[%sf,%sf,%sf]},Passengers:[%s]}
execute as @e[type=minecraft:block_display,tag=mg.mine] at @s rotated as @a[tag=mg.play,limit=1,sort=nearest] run tp @s ~ ~ ~ ~ 0
execute as @e[type=minecraft:block_display,tag=mg.mine] at @s on passengers run rotate @s ~ 0
scoreboard players operation @e[type=minecraft:block_display,tag=mg.mine] mg.ri = @s mg.ri
scoreboard players operation $kc mg.st = @s mg.ri
scoreboard players operation $kc mg.st %%= #k8 mg.st
%s
ride @s mount @e[type=minecraft:block_display,tag=mg.mine,limit=1]
tag @e[tag=mg.mine] remove mg.mine
''' % (ks(-0.6), ks(0.12), ks(-0.95), T0, ks(1.2), ks(0.38), ks(1.9), PASSENGERS, '\n'.join(
    f'execute if score $kc mg.st matches {k} run data modify entity @e[type=minecraft:block_display,tag=mg.mine,limit=1] block_state.Name set value "minecraft:{c}_concrete"'
    for k, c in enumerate(COLORS))))
fn('go', '''# Départ : portillon ouvert
function mg:kart/gate_off
scoreboard players set $ktime mg.st 0
scoreboard players set @a[tag=mg.play] mg.ksp 0
tellraw @a[tag=mg.play] [{"text":"🏎 ","color":"gold"},{"text":"KART","color":"gold","bold":true},{"text":" : Z avancer, S freiner / reculer, Q / D tourner, ","color":"gray"},{"text":"ESPACE en tournant = dérapage","color":"yellow"},{"text":" (relâche après les étincelles pour un mini-turbo). Boîtes ? = objets, clic droit pour les utiliser. 3 tours !","color":"gray"}]
''')
fn('cleanup', '''# Fin de course (appelé par core/return_lobby)
kill @e[tag=mg.kpart]
kill @e[type=minecraft:item_display,tag=mg.kbox]
function mg:kart/fl_remove
''')

# ------------------------------------------------------------------ tick de course
fn('tick', '''# Kart (état 2, jeu 61)
scoreboard players add $ktime mg.st 1
execute as @a[tag=mg.play] run function mg:kart/drive
execute as @a[tag=mg.play,tag=!mg.kfin] run function mg:kart/cp_check
execute as @a[tag=mg.play,scores={mg.qs=1..}] run function mg:kart/use_item
scoreboard players reset @a mg.qs

# Boîtes à objets, carapaces, bananes
execute as @e[type=minecraft:item_display,tag=mg.kbox,tag=!mg.kboff] at @s if entity @a[tag=mg.play,distance=..2.3] run function mg:kart/box_hit
execute as @e[type=minecraft:item_display,tag=mg.kboff] run function mg:kart/box_wait
execute as @e[type=minecraft:item_display,tag=mg.kshell] at @s run function mg:kart/shell_tick
execute as @e[type=minecraft:item_display,tag=mg.kban] at @s run function mg:kart/banana_tick

# Rotation des boîtes, classement et affichage (tous les 4 ticks)
scoreboard players add $kph mg.st 1
execute if score $kph mg.st matches 4.. run function mg:kart/every4

# Fin de course
execute store result score $kn mg.st if entity @a[tag=mg.play]
execute store result score $kfn mg.st if entity @a[tag=mg.play,tag=mg.kfin]
execute if score $kn mg.st matches 1.. if score $kfn mg.st = $kn mg.st run return run function mg:kart/end
execute if score $kend mg.st matches 1.. if score $ktime mg.st >= $kend mg.st run return run function mg:kart/end
execute if score $ktime mg.st matches 8400.. run return run function mg:kart/end
execute unless entity @a[tag=mg.play] run function mg:core/draw
''')
fn('every4', '''scoreboard players set $kph mg.st 0
scoreboard players add $kbr mg.st 1
execute if score $kbr mg.st matches 4.. run scoreboard players set $kbr mg.st 0
execute if score $kbr mg.st matches 0 as @e[type=minecraft:item_display,tag=mg.kbox] run data merge entity @s {start_interpolation:0,interpolation_duration:4,transformation:{left_rotation:{angle:0f,axis:[0f,1f,0f]}}}
execute if score $kbr mg.st matches 1 as @e[type=minecraft:item_display,tag=mg.kbox] run data merge entity @s {start_interpolation:0,interpolation_duration:4,transformation:{left_rotation:{angle:1.5708f,axis:[0f,1f,0f]}}}
execute if score $kbr mg.st matches 2 as @e[type=minecraft:item_display,tag=mg.kbox] run data merge entity @s {start_interpolation:0,interpolation_duration:4,transformation:{left_rotation:{angle:3.1416f,axis:[0f,1f,0f]}}}
execute if score $kbr mg.st matches 3 as @e[type=minecraft:item_display,tag=mg.kbox] run data merge entity @s {start_interpolation:0,interpolation_duration:4,transformation:{left_rotation:{angle:4.7124f,axis:[0f,1f,0f]}}}
execute as @a[tag=mg.play] run function mg:kart/progress
execute as @a[tag=mg.play] run function mg:kart/rank_one
execute as @a[tag=mg.play] run function mg:kart/hud
''')

# ------------------------------------------------------------------ pilotage
fn('drive', '''# Pilotage du kart de @s (chaque tick)
scoreboard players set $rd mg.st 0
execute on vehicle run scoreboard players set $rd mg.st 1
execute if score $rd mg.st matches 0 run function mg:kart/remount
execute on vehicle at @s run function mg:kart/probe
execute if score $kwa mg.st matches 1 run return run function mg:kart/rescue
execute if score $kyy mg.st matches ..6000 run return run function mg:kart/rescue

# Touches (plus de commandes une fois la course finie)
scoreboard players set $kf mg.st 0
scoreboard players set $kb mg.st 0
scoreboard players set $kl mg.st 0
scoreboard players set $kr mg.st 0
scoreboard players set $kj mg.st 0
execute unless entity @s[tag=mg.kfin] run function mg:kart/inputs

scoreboard players remove @s[scores={mg.kbo=1..}] mg.kbo 1
scoreboard players remove @s[scores={mg.kst=1..}] mg.kst 1
function mg:kart/speed
function mg:kart/steer
function mg:kart/vertical
execute if score $kbp mg.st matches 1 if score $kg mg.st matches 1 run function mg:kart/boost_pad
execute if score @s mg.kst matches 1.. run function mg:kart/star_touch

# Déplacement
execute store result storage mg:kart m.d double 0.01 run scoreboard players get @s mg.ksp
scoreboard players operation $kc mg.st = @s mg.ksp
execute if score @s mg.ksp matches 0.. run scoreboard players add $kc mg.st 75
execute if score @s mg.ksp matches ..-1 run scoreboard players remove $kc mg.st 75
execute store result storage mg:kart m.c double 0.01 run scoreboard players get $kc mg.st
execute store result storage mg:kart m.t int 1 run scoreboard players get $kt mg.st
execute store result storage mg:kart m.v double 0.01 run scoreboard players get $kv mg.st
execute on vehicle run function mg:kart/move with storage mg:kart m
function mg:kart/fx
''')
fn('inputs', '''execute if predicate mg:kart_f run scoreboard players set $kf mg.st 1
execute if predicate mg:kart_b run scoreboard players set $kb mg.st 1
execute if predicate mg:kart_l run scoreboard players set $kl mg.st 1
execute if predicate mg:kart_r run scoreboard players set $kr mg.st 1
execute if predicate mg:kart_j run scoreboard players set $kj mg.st 1
''')
fn('probe', '''# Capteurs du kart (@s = kart, à sa position)
scoreboard players set $kg mg.st 0
execute unless block ~ ~-0.2 ~ #mg:kart_pass run scoreboard players set $kg mg.st 1
scoreboard players set $kro mg.st 0
execute if block ~ ~-0.5 ~ #mg:kart_road run scoreboard players set $kro mg.st 1
scoreboard players set $kju mg.st 0
execute if block ~ ~-0.5 ~ minecraft:lime_concrete run scoreboard players set $kju mg.st 1
scoreboard players set $kbp mg.st 0
execute if block ~ ~-0.5 ~ minecraft:orange_glazed_terracotta run scoreboard players set $kbp mg.st 1
scoreboard players set $kwa mg.st 0
execute if block ~ ~0.3 ~ minecraft:water run scoreboard players set $kwa mg.st 1
execute store result score $kyy mg.st run data get entity @s Pos[1] 100
''')
fn('speed', '''# Vitesse (centièmes de bloc par tick) : 80 sur la route, 38 dans l'herbe, 105 en étoile, 125 en boost
scoreboard players set $kmx mg.st 80
execute if score $kro mg.st matches 0 if score $kg mg.st matches 1 run scoreboard players set $kmx mg.st 38
execute if score @s mg.kst matches 1.. run scoreboard players set $kmx mg.st 105
execute if score @s mg.kbo matches 1.. run scoreboard players set $kmx mg.st 125
execute if score @s mg.khi matches 1.. run return run function mg:kart/speed_hit

execute if score $kf mg.st matches 1 if score $kb mg.st matches 0 run scoreboard players add @s mg.ksp 4
execute if score $kb mg.st matches 1 if score $kf mg.st matches 0 if score @s mg.ksp matches 1.. run scoreboard players remove @s mg.ksp 9
execute if score $kb mg.st matches 1 if score $kf mg.st matches 0 if score @s mg.ksp matches ..0 run scoreboard players remove @s mg.ksp 3
execute if score $kf mg.st matches 0 if score $kb mg.st matches 0 if score @s mg.ksp matches 3.. run scoreboard players remove @s mg.ksp 2
execute if score $kf mg.st matches 0 if score $kb mg.st matches 0 if score @s mg.ksp matches ..-3 run scoreboard players add @s mg.ksp 2
execute if score $kf mg.st matches 0 if score $kb mg.st matches 0 if score @s mg.ksp matches -2..2 run scoreboard players set @s mg.ksp 0
execute if score @s mg.kbo matches 1.. if score @s mg.ksp < $kmx mg.st run scoreboard players operation @s mg.ksp = $kmx mg.st
execute if score @s mg.ksp > $kmx mg.st run scoreboard players remove @s mg.ksp 5
execute if score @s mg.ksp matches ..-31 run scoreboard players set @s mg.ksp -30
''')
fn('speed_hit', '''# Touché : le kart freine fort (x0,8 par tick)
scoreboard players operation @s mg.ksp *= #k4 mg.st
scoreboard players operation @s mg.ksp /= #k5 mg.st
''')
fn('steer', '''# Direction : virage plus serré à basse vitesse, inversé en marche arrière, tête-à-queue si touché
scoreboard players set $kt mg.st 0
execute if score @s mg.khi matches 1.. run scoreboard players set $kt mg.st 36
execute if score @s mg.khi matches 1.. run return run scoreboard players remove @s mg.khi 1
scoreboard players operation $ka mg.st = @s mg.ksp
execute if score $ka mg.st matches ..-1 run scoreboard players operation $ka mg.st *= #km1 mg.st
scoreboard players set $kT mg.st 0
execute if score $ka mg.st matches 4..24 run scoreboard players set $kT mg.st 6
execute if score $ka mg.st matches 25..59 run scoreboard players set $kT mg.st 5
execute if score $ka mg.st matches 60.. run scoreboard players set $kT mg.st 4
execute if score $kl mg.st matches 1 run scoreboard players operation $kt mg.st -= $kT mg.st
execute if score $kr mg.st matches 1 run scoreboard players operation $kt mg.st += $kT mg.st
execute if score @s mg.ksp matches ..-1 run scoreboard players operation $kt mg.st *= #km1 mg.st
function mg:kart/drift
''')
fn('drift', '''# Dérapage : ESPACE + virage à plus de 45 ; étincelles bleues (25 ticks) puis orange (55) ; mini-turbo au relâchement
execute if score @s mg.kdr matches 0 if score $kj mg.st matches 1 if score $kg mg.st matches 1 if score @s mg.ksp matches 45.. if score $kl mg.st matches 1 run function mg:kart/drift_start {d:-1}
execute if score @s mg.kdr matches 0 if score $kj mg.st matches 1 if score $kg mg.st matches 1 if score @s mg.ksp matches 45.. if score $kr mg.st matches 1 run function mg:kart/drift_start {d:1}
execute if score @s mg.kdr matches 1.. if score $kj mg.st matches 1 if score @s mg.ksp matches 30.. run return run function mg:kart/drift_hold
execute if score @s mg.kdr matches 1.. run function mg:kart/drift_end
''')
fn('drift_start', '''$scoreboard players set @s mg.kdd $(d)
scoreboard players set @s mg.kdr 1
scoreboard players set @s mg.kvy 18
execute at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 0.6 0.8
''')
fn('drift_hold', '''# Virage forcé dans le sens du dérapage, la direction le resserre ou l'élargit
scoreboard players add @s mg.kdr 1
scoreboard players operation $kt mg.st = @s mg.kdd
scoreboard players operation $kt mg.st *= #k5 mg.st
execute if score @s mg.kdd matches -1 if score $kl mg.st matches 1 run scoreboard players remove $kt mg.st 2
execute if score @s mg.kdd matches -1 if score $kr mg.st matches 1 run scoreboard players add $kt mg.st 3
execute if score @s mg.kdd matches 1 if score $kr mg.st matches 1 run scoreboard players add $kt mg.st 2
execute if score @s mg.kdd matches 1 if score $kl mg.st matches 1 run scoreboard players remove $kt mg.st 3
execute if score @s mg.kdr matches 25 at @s run playsound minecraft:block.amethyst_block.chime master @s ~ ~ ~ 1 1.2
execute if score @s mg.kdr matches 55 at @s run playsound minecraft:block.amethyst_block.chime master @s ~ ~ ~ 1 1.8
''')
fn('drift_end', '''execute if score @s mg.kdr matches 55.. if score @s mg.kbo matches ..27 run scoreboard players set @s mg.kbo 28
execute if score @s mg.kdr matches 25..54 if score @s mg.kbo matches ..13 run scoreboard players set @s mg.kbo 14
execute if score @s mg.kdr matches 25.. at @s run playsound minecraft:entity.firework_rocket.launch master @a[tag=mg.play,distance=..20] ~ ~ ~ 0.8 1.4
scoreboard players set @s mg.kdr 0
''')
fn('vertical', '''# Tremplin, petit saut du dérapage, gravité
scoreboard players set $kv mg.st 0
execute if score $kju mg.st matches 1 if score $kg mg.st matches 1 if score @s mg.kvy matches ..0 run scoreboard players set @s mg.kvy 48
execute if score $kg mg.st matches 1 if score @s mg.kvy matches ..0 run scoreboard players set @s mg.kvy 0
execute if score $kg mg.st matches 0 run scoreboard players remove @s mg.kvy 6
execute if score @s mg.kvy matches ..-90 run scoreboard players set @s mg.kvy -90
scoreboard players operation $kv mg.st = @s mg.kvy
''')
fn('boost_pad', '''execute if score @s mg.kbo matches ..15 at @s run playsound minecraft:entity.firework_rocket.launch master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 1.2
execute if score @s mg.kbo matches ..21 run scoreboard players set @s mg.kbo 22
''')
fn('move', '''# @s = kart : remis sur la route s'il s'y est enfoncé, tourné, puis avancé (sauf mur devant : rebond)
execute at @s unless block ~ ~ ~ #mg:kart_pass align y run tp @s ~ ~1 ~
$execute at @s run tp @s ~ ~ ~ ~$(t) 0
$execute on passengers if entity @s[type=minecraft:block_display] run rotate @s ~$(t) ~
$execute at @s rotated ~ 0 positioned ^ ^0.5 ^$(c) unless block ~ ~ ~ #mg:kart_pass run return run function mg:kart/bump {v:$(v)}
$execute at @s rotated ~ 0 run tp @s ^ ^$(v) ^$(d)
''')
fn('bump', '''# Mur devant : le kart ne passe pas, rebondit un peu en arrière (@s = kart)
$execute at @s run tp @s ~ ~$(v) ~
execute on passengers if entity @s[type=minecraft:player] run function mg:kart/bumped
''')
fn('bumped', '''scoreboard players operation @s mg.ksp *= #km1 mg.st
scoreboard players operation @s mg.ksp /= #k3 mg.st
scoreboard players set @s mg.kdr 0
execute at @s run playsound minecraft:block.wood.hit master @s ~ ~ ~ 1 0.6
''')
fn('remount', '''# Pilote sorti de son kart (touche Maj) : il y remonte, ou un kart neuf est créé au dernier point de passage
scoreboard players operation $me mg.st = @s mg.ri
tag @e[tag=mg.mine] remove mg.mine
execute as @e[type=minecraft:block_display,tag=mg.kart] if score @s mg.ri = $me mg.st run tag @s add mg.mine
execute if entity @e[type=minecraft:block_display,tag=mg.mine] run ride @s mount @e[type=minecraft:block_display,tag=mg.mine,limit=1]
tag @e[tag=mg.mine] remove mg.mine
scoreboard players set $rd mg.st 0
execute on vehicle run scoreboard players set $rd mg.st 1
execute if score $rd mg.st matches 0 at @s run function mg:kart/kart_new
''')
fn('rescue', '''# Tombé à l'eau ou dans le vide : remis au point de passage précédent (@s = pilote)
scoreboard players operation $ki mg.st = @s mg.kcp
scoreboard players remove $ki mg.st 1
execute if score $ki mg.st matches ..-1 run scoreboard players operation $ki mg.st = $kK mg.st
execute if score $ki mg.st = $kK mg.st run scoreboard players remove $ki mg.st 1
execute on vehicle run function mg:kart/cp_tp
execute on vehicle at @s on passengers run rotate @s ~ 0
scoreboard players set @s mg.ksp 0
scoreboard players set @s mg.kvy 0
scoreboard players set @s mg.kdr 0
scoreboard players set @s mg.khi 0
title @s actionbar [{"text":"☁ Remis en piste !","color":"aqua"}]
execute at @s run playsound minecraft:entity.chicken.egg master @s ~ ~ ~ 1 1
''')
fn('fx', '''# Effets : fumée, étincelles de dérapage, flammes de boost, étoile
execute if score @s mg.ksp matches 20.. on vehicle at @s rotated ~ 0 positioned ^ ^0.4 ^-1.1 run particle minecraft:smoke ~ ~ ~ 0.1 0.05 0.1 0.01 1
execute if score @s mg.kdr matches 25..54 on vehicle at @s rotated ~ 0 positioned ^0.7 ^0.2 ^-0.9 run particle minecraft:soul_fire_flame ~ ~ ~ 0.05 0.05 0.05 0.02 2
execute if score @s mg.kdr matches 25..54 on vehicle at @s rotated ~ 0 positioned ^-0.7 ^0.2 ^-0.9 run particle minecraft:soul_fire_flame ~ ~ ~ 0.05 0.05 0.05 0.02 2
execute if score @s mg.kdr matches 55.. on vehicle at @s rotated ~ 0 positioned ^0.7 ^0.2 ^-0.9 run particle minecraft:flame ~ ~ ~ 0.05 0.05 0.05 0.02 3
execute if score @s mg.kdr matches 55.. on vehicle at @s rotated ~ 0 positioned ^-0.7 ^0.2 ^-0.9 run particle minecraft:flame ~ ~ ~ 0.05 0.05 0.05 0.02 3
execute if score @s mg.kbo matches 1.. on vehicle at @s rotated ~ 0 positioned ^ ^0.4 ^-1.2 run particle minecraft:flame ~ ~ ~ 0.15 0.1 0.15 0.03 4
execute if score @s mg.kst matches 1.. on vehicle at @s run particle minecraft:end_rod ~ ~0.8 ~ 0.6 0.5 0.6 0.05 4
''')
fn('star_touch', '''# En étoile : les karts touchés partent en tête-à-queue
tag @s add mg.kme
execute at @s as @a[tag=mg.play,tag=!mg.kme,distance=..1.8] run function mg:kart/hit
tag @s remove mg.kme
''')
fn('hit', '''# @s touché (carapace, banane, éclair, étoile) : tête-à-queue, sauf en étoile
execute if score @s mg.kst matches 1.. run return 0
scoreboard players set @s mg.khi 24
scoreboard players set @s mg.kbo 0
scoreboard players set @s mg.kdr 0
title @s actionbar [{"text":"💥 Touché !","color":"red","bold":true}]
execute at @s run playsound minecraft:entity.generic.explode master @a[tag=mg.play,distance=..24] ~ ~ ~ 0.4 1.6
execute at @s run particle minecraft:explosion ~ ~0.5 ~ 0.3 0.3 0.3 0 2
''')

# ------------------------------------------------------------------ course : points de passage, tours, arrivée
fn('cp_pass', '''# Point de passage validé (@s = pilote) ; repasser la ligne (point 0 → 1) = nouveau tour
scoreboard players add @s mg.kcp 1
execute if score @s mg.kcp >= $kK mg.st run scoreboard players set @s mg.kcp 0
execute if score @s mg.kcp matches 1 run function mg:kart/lap
''')
fn('lap', '''scoreboard players add @s mg.klp 1
execute if score @s mg.klp > $kLaps mg.st run return run function mg:kart/finish
execute if score @s mg.klp matches 2.. if score @s mg.klp < $kLaps mg.st run title @s actionbar [{"text":"🏁 Tour ","color":"gold"},{"score":{"name":"@s","objective":"mg.klp"},"color":"yellow","bold":true},{"text":" / 3","color":"gold"}]
execute if score @s mg.klp = $kLaps mg.st run title @s title [{"text":"TOUR FINAL !","color":"gold","bold":true}]
execute if score @s mg.klp = $kLaps mg.st at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.8 1.6
''')
fn('finish', '''# Ligne d'arrivée franchie au dernier tour (@s)
tag @s add mg.kfin
scoreboard players add $kfo mg.st 1
scoreboard players operation @s mg.kfp = $kfo mg.st
scoreboard players set @s mg.kps 100
execute if score $kfo mg.st matches 1 run scoreboard players operation $kend mg.st = $ktime mg.st
execute if score $kfo mg.st matches 1 run scoreboard players add $kend mg.st 600
scoreboard players operation $ksec mg.st = $ktime mg.st
scoreboard players operation $ksec mg.st /= #k20 mg.st
title @s title [{"score":{"name":"@s","objective":"mg.kfp"},"color":"gold","bold":true},{"text":"ᵉ","color":"gold"}]
title @s subtitle [{"text":"🏁 Arrivée en ","color":"yellow"},{"score":{"name":"$ksec","objective":"mg.st"},"color":"white"},{"text":" s","color":"yellow"}]
tellraw @a[tag=!mg.surv] [{"text":"🏁 ","color":"gold"},{"selector":"@s","color":"yellow","bold":true},{"text":" franchit la ligne en position ","color":"gray"},{"score":{"name":"@s","objective":"mg.kfp"},"color":"gold","bold":true},{"text":" (","color":"gray"},{"score":{"name":"$ksec","objective":"mg.st"},"color":"white"},{"text":" s)","color":"gray"}]
execute if score $kfo mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":"⏱ 30 secondes pour finir la course !","color":"gold"}]
execute at @s run playsound minecraft:entity.firework_rocket.twinkle master @a[tag=mg.play] ~ ~ ~ 1 1
''')
fn('progress', '''# Avancement : tours x 1000 + point de passage (arrivé : selon l'ordre d'arrivée) ; tableau en %
scoreboard players operation @s mg.kpg = @s mg.klp
scoreboard players operation @s mg.kpg *= #k1000 mg.st
scoreboard players operation @s mg.kpg += @s mg.kcp
execute if entity @s[tag=mg.kfin] run scoreboard players set @s mg.kpg 900000
execute if entity @s[tag=mg.kfin] run scoreboard players operation @s mg.kpg -= @s mg.kfp
execute if entity @s[tag=mg.kfin] run return 0
scoreboard players operation $kp mg.st = @s mg.klp
scoreboard players remove $kp mg.st 1
execute if score $kp mg.st matches ..-1 run scoreboard players set $kp mg.st 0
scoreboard players operation $kp mg.st *= $kK mg.st
scoreboard players operation $kp mg.st += @s mg.kcp
scoreboard players operation $kp mg.st *= #k100 mg.st
scoreboard players operation $kq mg.st = $kK mg.st
scoreboard players operation $kq mg.st *= $kLaps mg.st
scoreboard players operation $kp mg.st /= $kq mg.st
scoreboard players operation @s mg.kps = $kp mg.st
''')
fn('rank_one', '''# Position de @s = 1 + nombre de pilotes plus avancés
scoreboard players set @s mg.krk 1
scoreboard players operation $me mg.st = @s mg.kpg
tag @s add mg.kme
execute as @a[tag=mg.play] if score @s mg.kpg > $me mg.st run scoreboard players add @a[tag=mg.kme,limit=1] mg.krk 1
tag @s remove mg.kme
''')
ITEMS = {1: ('🍌 Banane', 'yellow'), 2: ('🟢 Carapace verte', 'green'), 3: ('🔴 Carapace rouge', 'red'),
         4: ('🍄 Champignon', 'gold'), 5: ('⭐ Étoile', 'yellow'), 6: ('⚡ Éclair', 'aqua')}
hud = ['# Barre du bas : tour, position, objet, vitesse',
       'scoreboard players operation $kmh mg.st = @s mg.ksp',
       'scoreboard players operation $kmh mg.st *= #k72 mg.st',
       'scoreboard players operation $kmh mg.st /= #k100 mg.st',
       'execute if score $kmh mg.st matches ..-1 run scoreboard players operation $kmh mg.st *= #km1 mg.st',
       'execute store result score $kpl mg.st run scoreboard players get @s mg.klp',
       'execute if score $kpl mg.st matches ..0 run scoreboard players set $kpl mg.st 1',
       'execute if score $kpl mg.st > $kLaps mg.st run scoreboard players operation $kpl mg.st = $kLaps mg.st']
base = ('{"text":"🏁 Tour ","color":"gold"},{"score":{"name":"$kpl","objective":"mg.st"},"color":"yellow","bold":true},{"text":"/3   ","color":"gold"},'
        '{"text":"Position ","color":"gray"},{"score":{"name":"@s","objective":"mg.krk"},"color":"white","bold":true},{"text":"/","color":"gray"},{"score":{"name":"$kn","objective":"mg.st"},"color":"gray"},'
        '{"text":"   ","color":"gray"}')
tail = ',{"text":"   ","color":"gray"},{"score":{"name":"$kmh","objective":"mg.st"},"color":"aqua"},{"text":" km/h","color":"dark_aqua"}'
hud.append(f'execute unless score @s mg.khi matches 1.. if score @s mg.kit matches 0 run title @s actionbar [{base},{{"text":"(pas d\'objet)","color":"dark_gray"}}{tail}]')
for k, (name, color) in ITEMS.items():
    hud.append(f'execute unless score @s mg.khi matches 1.. if score @s mg.kit matches {k} run title @s actionbar [{base},{{"text":"{name} (clic droit)","color":"{color}","bold":true}}{tail}]')
fn('hud', '\n'.join(hud) + '\n')

# ------------------------------------------------------------------ objets
fn('box_hit', '''# Boîte à objets touchée (@s = boîte) : elle disparaît 3 s, les pilotes sans objet en reçoivent un
tag @s add mg.kboff
scoreboard players set @s mg.t 60
item replace entity @s contents with minecraft:air
execute at @s run playsound minecraft:block.glass.break master @a[tag=mg.play,distance=..16] ~ ~ ~ 0.8 1.4
execute at @s run particle minecraft:wax_on ~ ~0.5 ~ 0.4 0.4 0.4 0 12
execute at @s as @e[type=minecraft:text_display,tag=mg.kboxq,distance=..1.5] run data merge entity @s {text:""}
execute at @s as @a[tag=mg.play,distance=..2.3,scores={mg.kit=0}] run function mg:kart/item_roll
''')
fn('box_wait', '''scoreboard players remove @s mg.t 1
execute if score @s mg.t matches 1.. run return 0
tag @s remove mg.kboff
item replace entity @s contents with minecraft:yellow_stained_glass
execute at @s as @e[type=minecraft:text_display,tag=mg.kboxq,distance=..1.5] run data merge entity @s {text:[{"text":"?","color":"gold","bold":true}]}
''')
fn('item_roll', '''# Tirage d'un objet selon la position (les derniers ont de meilleurs objets)
execute store result score $kr1 mg.st run random value 1..100
scoreboard players operation $kf1 mg.st = @s mg.krk
scoreboard players remove $kf1 mg.st 1
scoreboard players operation $kf1 mg.st *= #k100 mg.st
scoreboard players operation $kn1 mg.st = $kn mg.st
scoreboard players remove $kn1 mg.st 1
execute if score $kn1 mg.st matches ..0 run scoreboard players set $kf1 mg.st 50
execute if score $kn1 mg.st matches 1.. run scoreboard players operation $kf1 mg.st /= $kn1 mg.st
# tête de course
execute if score $kf1 mg.st matches ..33 run scoreboard players set $kgv mg.st 1
execute if score $kf1 mg.st matches ..33 if score $kr1 mg.st matches 41..75 run scoreboard players set $kgv mg.st 2
execute if score $kf1 mg.st matches ..33 if score $kr1 mg.st matches 76..95 run scoreboard players set $kgv mg.st 4
execute if score $kf1 mg.st matches ..33 if score $kr1 mg.st matches 96.. run scoreboard players set $kgv mg.st 3
# milieu
execute if score $kf1 mg.st matches 34..66 run scoreboard players set $kgv mg.st 1
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 16..35 run scoreboard players set $kgv mg.st 2
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 36..65 run scoreboard players set $kgv mg.st 3
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 66..95 run scoreboard players set $kgv mg.st 4
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 96.. run scoreboard players set $kgv mg.st 5
# derniers
execute if score $kf1 mg.st matches 67.. run scoreboard players set $kgv mg.st 2
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 11..35 run scoreboard players set $kgv mg.st 3
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 36..65 run scoreboard players set $kgv mg.st 4
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 66..90 run scoreboard players set $kgv mg.st 5
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 91.. run scoreboard players set $kgv mg.st 6
scoreboard players operation @s mg.kit = $kgv mg.st
function mg:kart/item_give
''')
MODEL = {1: 'minecraft:yellow_dye', 2: 'minecraft:turtle_scute', 3: 'minecraft:red_dye', 4: 'minecraft:red_mushroom', 5: 'minecraft:nether_star', 6: 'minecraft:lightning_rod'}
give = ['# Objet en main (case 1 de la barre) : bâton à champignon tordu, clic droit = utiliser']
for k, (name, color) in ITEMS.items():
    give.append(f'execute if score @s mg.kit matches {k} run item replace entity @s hotbar.0 with minecraft:warped_fungus_on_a_stick'
                f'[item_model="{MODEL[k]}",custom_name=[{{"text":"{name}","color":"{color}","bold":true,"italic":false}}],'
                f'lore=[[{{"text":"Clic droit pour l\'utiliser","color":"gray","italic":false}}]],unbreakable={{}}]')
    give.append(f'execute if score @s mg.kit matches {k} run title @s subtitle [{{"text":"{name}","color":"{color}","bold":true}}]')
give.append('title @s title ""')
give.append('execute at @s run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 1 1.4')
fn('item_give', '\n'.join(give) + '\n')
fn('use_item', '''# Objet utilisé (clic droit) par @s
scoreboard players reset @s mg.qs
execute if score @s mg.kit matches 0 run return 0
scoreboard players operation $kuse mg.st = @s mg.kit
scoreboard players set @s mg.kit 0
clear @s minecraft:warped_fungus_on_a_stick
execute if score $kuse mg.st matches 1 run function mg:kart/use_banana
execute if score $kuse mg.st matches 2 run function mg:kart/use_shell {t:"mg.kgreen",c:3381555}
execute if score $kuse mg.st matches 3 run function mg:kart/use_shell {t:"mg.kred",c:13382451}
execute if score $kuse mg.st matches 4 run function mg:kart/use_mushroom
execute if score $kuse mg.st matches 5 run function mg:kart/use_star
execute if score $kuse mg.st matches 6 run function mg:kart/use_lightning
''')
fn('use_banana', '''execute on vehicle at @s rotated ~ 0 positioned ^ ^0.15 ^-2.4 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.kban","mg.fx"],item:{id:"minecraft:yellow_dye"},billboard:"center",transformation:{translation:[0f,0.3f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.3f,1.3f,1.3f]}}
execute on vehicle at @s rotated ~ 0 positioned ^ ^0.15 ^-2.4 run scoreboard players set @e[type=minecraft:item_display,tag=mg.kban,distance=..0.5] mg.t 10
execute at @s run playsound minecraft:entity.item.pickup master @a[tag=mg.play,distance=..16] ~ ~ ~ 1 0.6
''')
fn('use_shell', '''# Carapace lancée devant le kart (verte : tout droit, rebondit ; rouge : vise le pilote juste devant)
$execute on vehicle at @s rotated ~ 0 positioned ^ ^0.45 ^1.9 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.kshell","$(t)","mg.knew","mg.fx"],teleport_duration:1,item:{id:"minecraft:leather_helmet",components:{"minecraft:dyed_color":$(c)}},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute on vehicle at @s rotated ~ 0 positioned ^ ^0.45 ^1.9 as @e[type=minecraft:item_display,tag=mg.knew] run tp @s ~ ~ ~ ~ 0
scoreboard players set @e[type=minecraft:item_display,tag=mg.knew] mg.t 120
scoreboard players set @e[type=minecraft:item_display,tag=mg.knew] mg.kbo 4
scoreboard players set @e[type=minecraft:item_display,tag=mg.knew] mg.kdr 0
scoreboard players set @e[type=minecraft:item_display,tag=mg.knew] mg.kdd -1
scoreboard players operation $kme mg.st = @s mg.krk
scoreboard players remove $kme mg.st 1
execute if entity @e[type=minecraft:item_display,tag=mg.knew,tag=mg.kred] as @a[tag=mg.play,tag=!mg.kfin] if score @s mg.krk = $kme mg.st run scoreboard players operation @e[type=minecraft:item_display,tag=mg.knew] mg.kdd = @s mg.ri
tag @e[type=minecraft:item_display,tag=mg.knew] remove mg.knew
execute at @s run playsound minecraft:entity.snowball.throw master @a[tag=mg.play,distance=..16] ~ ~ ~ 1 0.7
''')
fn('use_mushroom', '''scoreboard players set @s mg.kbo 30
execute at @s run playsound minecraft:entity.firework_rocket.launch master @a[tag=mg.play,distance=..20] ~ ~ ~ 1 1
title @s actionbar [{"text":"🍄 Turbo !","color":"gold","bold":true}]
''')
fn('use_star', '''scoreboard players set @s mg.kst 160
effect give @s minecraft:glowing 8 0 true
execute at @s run playsound minecraft:entity.player.levelup master @a[tag=mg.play,distance=..24] ~ ~ ~ 1 1.6
title @s actionbar [{"text":"⭐ Invincible !","color":"yellow","bold":true}]
''')
fn('use_lightning', '''# Éclair : tous les adversaires partent en tête-à-queue
tag @s add mg.kme
execute as @a[tag=mg.play,tag=!mg.kme] run function mg:kart/hit
tag @s remove mg.kme
execute as @a[tag=mg.play] at @s run playsound minecraft:entity.lightning_bolt.thunder master @s ~ ~ ~ 0.6 1.4
tellraw @a[tag=mg.play] [{"text":"⚡ ","color":"aqua"},{"selector":"@s","color":"yellow"},{"text":" foudroie tout le monde !","color":"aqua"}]
''')
fn('shell_tick', '''# Carapace (@s, à sa position) : avance, rebondit ou éclate contre un mur, touche un kart
scoreboard players remove @s mg.t 1
execute if score @s mg.t matches ..0 run return run kill @s
scoreboard players remove @s[scores={mg.kbo=1..}] mg.kbo 1
execute if entity @s[tag=mg.kred] unless score @s mg.kdd matches -1 run function mg:kart/shell_aim
execute positioned ^ ^ ^1.3 unless block ~ ~ ~ #mg:kart_pass run return run function mg:kart/shell_wall
tp @s ^ ^ ^1.3
particle minecraft:crit ~ ~0.2 ~ 0.1 0.1 0.1 0 1
execute if score @s mg.kbo matches 1.. run return 0
tag @s add mg.kcur
execute as @a[tag=mg.play,distance=..1.7,limit=1,sort=nearest] run function mg:kart/shell_hit
tag @s remove mg.kcur
''')
fn('shell_aim', '''scoreboard players operation $ktg mg.st = @s mg.kdd
execute as @a[tag=mg.play] if score @s mg.ri = $ktg mg.st run tag @s add mg.ktgt
execute facing entity @a[tag=mg.ktgt,limit=1] feet rotated ~ 0 run tp @s ~ ~ ~ ~ 0
tag @a remove mg.ktgt
''')
fn('shell_wall', '''execute if entity @s[tag=mg.kred] run return run kill @s
execute if score @s mg.kdr matches 3.. run return run kill @s
scoreboard players add @s mg.kdr 1
tp @s ~ ~ ~ ~180 0
playsound minecraft:block.stone.hit master @a[tag=mg.play,distance=..16] ~ ~ ~ 1 1.4
''')
fn('shell_hit', '''function mg:kart/hit
kill @e[type=minecraft:item_display,tag=mg.kcur]
''')
fn('banana_tick', '''execute if score @s mg.t matches 1.. run return run scoreboard players remove @s mg.t 1
tag @s add mg.kcur
execute as @a[tag=mg.play,distance=..1.5,limit=1,sort=nearest] run function mg:kart/shell_hit
tag @s remove mg.kcur
''')

# ------------------------------------------------------------------ fin de course
fn('end', '''# Fin de course : arrivés dans l'ordre, puis les autres selon leur avancement ; victoire au premier
execute as @a[tag=mg.play] run function mg:kart/progress
execute as @a[tag=mg.play] run function mg:kart/rank_one
tellraw @a[tag=!mg.surv] [{"text":"\\n🏁 CLASSEMENT DE LA COURSE","color":"gold","bold":true}]
scoreboard players set $kr0 mg.st 1
function mg:kart/end_line
execute unless entity @a[tag=mg.play] run return run function mg:core/draw
execute as @a[tag=mg.play,scores={mg.krk=1},limit=1] run function mg:core/win_player
''')
fn('end_line', '''execute if score $kr0 mg.st > $kn mg.st run return 0
execute as @a[tag=mg.play] if score @s mg.krk = $kr0 mg.st run tellraw @a[tag=!mg.surv] [{"text":"  ","color":"gray"},{"score":{"name":"$kr0","objective":"mg.st"},"color":"gold","bold":true},{"text":". ","color":"gold"},{"selector":"@s","color":"white"}]
scoreboard players add $kr0 mg.st 1
function mg:kart/end_line
''')
print('ok')
