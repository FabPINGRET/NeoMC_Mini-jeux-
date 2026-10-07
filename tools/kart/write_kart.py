"""Écrit le moteur de kart (fonctions écrites à la main) : python write_kart.py <racine du dépôt>.

Le kart est un block_display piloté par le datapack (touches lues par prédicats). Deux vues :
  - 3e personne (par défaut) : le joueur est spectateur d'une caméra qui suit le kart, sa tête est posée sur le siège ;
  - 1re personne : le joueur est assis dans le kart.
Tout ce qui dépend d'une position (boîtes, carapaces, points de passage) se mesure sur le KART (tag mg.kk pendant le tour du pilote).
"""
import json, os, sys

R = sys.argv[1]
DATA = os.path.join(R, 'data')
K = os.path.join(DATA, 'mg', 'function', 'kart')
os.makedirs(K, exist_ok=True)

def wr(path, txt):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8', newline='\n').write(txt)
def fn(name, txt): wr(os.path.join(K, name + '.mcfunction'), txt)

KK = '@e[type=minecraft:block_display,tag=mg.kk,limit=1]'
KART = '@e[type=minecraft:block_display,tag=mg.kart'

# ------------------------------------------------------------------ prédicats (touches) et tags de blocs
for key, inp in (('f', 'forward'), ('b', 'backward'), ('l', 'left'), ('r', 'right'), ('j', 'jump'), ('s', 'sprint')):
    wr(os.path.join(DATA, f'mg/predicate/kart_{key}.json'), json.dumps(
        {"condition": "minecraft:entity_properties", "entity": "this",
         "predicate": {"minecraft:type_specific/player": {"input": {inp: True}}}}, indent=2) + '\n')
wr(os.path.join(DATA, 'mg/tags/block/kart_pass.json'), json.dumps({"values": [
    "minecraft:air", "minecraft:cave_air", "minecraft:void_air", "minecraft:water", "minecraft:short_grass", "minecraft:tall_grass",
    "minecraft:fern", "#minecraft:small_flowers", "minecraft:light", "minecraft:snow", "#minecraft:wool_carpets"]}, indent=2) + '\n')
wr(os.path.join(DATA, 'mg/tags/block/kart_road.json'), json.dumps({"values": [
    "minecraft:gray_concrete", "minecraft:white_concrete", "minecraft:red_concrete", "minecraft:black_concrete",
    "minecraft:orange_glazed_terracotta", "minecraft:lime_concrete", "minecraft:stone_bricks"]}, indent=2) + '\n')

# ------------------------------------------------------------------ modèle du kart
COLORS = ['red', 'blue', 'lime', 'yellow', 'purple', 'orange', 'cyan', 'pink']
TEXTC = ['red', 'blue', 'green', 'yellow', 'dark_purple', 'gold', 'aqua', 'light_purple']
T0 = 'left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f]'
KS = 0.75   # taille du kart (1 = modèle d'origine)
def ks(v): return round(v * KS, 3)
def part(block, tr, sc, tag):
    return ('{id:"minecraft:block_display",Tags:["mg.kpart","mg.fx","%s"],teleport_duration:2,block_state:{Name:"minecraft:%s"},'
            'transformation:{translation:[%sf,%sf,%sf],%s,scale:[%sf,%sf,%sf]}}' % (tag, block, *map(ks, tr), T0, *map(ks, sc)))
# pièces du kart (bloc, translation, échelle, marqueur) ; le corps est le kart lui-même (ROOT)
ROOT = ((-0.6, 0.12, -0.95), (1.2, 0.38, 1.9))
PARTS = [('black_concrete', (-0.78, 0.0, 0.45), (1.56, 0.42, 0.42), 'mg.kp1'),
         ('black_concrete', (-0.78, 0.0, -0.85), (1.56, 0.42, 0.42), 'mg.kp2'),
         ('gray_concrete', (-0.4, 0.5, -0.75), (0.8, 0.5, 0.2), 'mg.kp3'),
         ('light_gray_concrete', (-0.08, 0.5, 0.45), (0.16, 0.35, 0.16), 'mg.kp4')]
PASSENGERS = ','.join(part(*p) for p in PARTS)

# ------------------------------------------------------------------ préparation, départ, fin
fn('prepare', '''# Kart : préparation pendant le compte à rebours (zone chargée, pilotes sur la grille, karts dès que la zone est prête)
function mg:kart/const
function mg:kart/fl_add
function mg:kart/mm_base
function mg:kart/mm_init
scoreboard players set #km1 mg.st -1
scoreboard players set #k3 mg.st 3
scoreboard players set #k4 mg.st 4
scoreboard players set #k5 mg.st 5
scoreboard players set #k8 mg.st 8
scoreboard players set #k20 mg.st 20
scoreboard players set #k100 mg.st 100
scoreboard players set #k1000 mg.st 1000
scoreboard players set #k60 mg.st 60
scoreboard players set #k12 mg.st 12
scoreboard players set #k65 mg.st 65
scoreboard players set #k120 mg.st 120
scoreboard players set #kkmh mg.st 108
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
kill @e[tag=mg.kcam]
gamemode adventure @a[tag=mg.play]
clear @a[tag=mg.play]
tag @a remove mg.kfin
scoreboard players set @a[tag=mg.play] mg.ksp 0
scoreboard players set @a[tag=mg.play] mg.kdr 0
scoreboard players set @a[tag=mg.play] mg.krc 0
scoreboard players set @a[tag=mg.play] mg.kbo 0
scoreboard players set @a[tag=mg.play] mg.khi 0
scoreboard players set @a[tag=mg.play] mg.kst 0
scoreboard players set @a[tag=mg.play] mg.kit 0
scoreboard players set @a[tag=mg.play] mg.kic 0
scoreboard players set @a[tag=mg.play] mg.kgd 0
scoreboard players set @a[tag=mg.play] mg.kbill 0
scoreboard players set @a[tag=mg.play] mg.kboo 0
scoreboard players set @a[tag=mg.play] mg.kmg 0
scoreboard players set @a[tag=mg.play] mg.kcp 0
scoreboard players set @a[tag=mg.play] mg.klp 0
scoreboard players set @a[tag=mg.play] mg.kvy 0
scoreboard players set @a[tag=mg.play] mg.kfp 0
scoreboard players set @a[tag=mg.play] mg.kps 0
execute as @a[tag=mg.play] unless score @s mg.kvm matches 0..1 run scoreboard players set @s mg.kvm 0
scoreboard players reset @a mg.qs
execute as @a[tag=mg.play] run function mg:kart/place_one
scoreboard objectives setdisplay sidebar mg.kmap
schedule function mg:kart/place_all 40t
''')
fn('place_one', '''scoreboard players add $gi mg.st 1
scoreboard players operation @s mg.ri = $gi mg.st
function mg:kart/grid_tp
''')
fn('place_all', '''# Dès que la zone est chargée (vérifié toutes les 0,5 s) : portillon, boîtes, un kart par pilote, vue installée
execute unless score $game mg.st matches 61 run return 0
execute unless score $state mg.st matches 1..2 run return 0
execute unless function mg:kart/loaded_all run return run schedule function mg:kart/place_all 10t
function mg:kart/gate_on
function mg:kart/boxes
execute as @a[tag=mg.play] at @s run function mg:kart/kart_new
execute as @a[tag=mg.play] run function mg:kart/grid_face
execute as @a[tag=mg.play] run function mg:kart/place_seat
tellraw @a[tag=mg.play] [{"text":"🏎 ","color":"gold"},{"text":"Vue : 3e personne (Ctrl = objet). ","color":"gray"},{"text":"[1re personne]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.kv set 2"}},{"text":" ","color":"gray"},{"text":"[3e personne]","color":"yellow","click_event":{"action":"run_command","command":"trigger mg.kv set 1"}}]
''')
fn('grid_face', f'''# Le kart de @s est posé sur sa place de grille, dans l'axe de la piste (et pas dans le sens du regard du joueur)
function mg:kart/kk
scoreboard players operation $gi mg.st = @s mg.ri
execute as {KK} run function mg:kart/grid_tp
execute as {KK} at @s on passengers run rotate @s ~ 0
tag @e[tag=mg.kk] remove mg.kk
''')
fn('place_seat', '''function mg:kart/kk
function mg:kart/seat
tag @e[tag=mg.kk] remove mg.kk
''')
fn('kk', f'''# Marque le kart de @s (mg.kk) et sa caméra (mg.kcamc)
scoreboard players operation $me mg.st = @s mg.ri
tag @e[tag=mg.kk] remove mg.kk
tag @e[tag=mg.kcamc] remove mg.kcamc
execute as {KART}] if score @s mg.ri = $me mg.st run tag @s add mg.kk
execute as @e[type=minecraft:item_display,tag=mg.kcam] if score @s mg.ri = $me mg.st run tag @s add mg.kcamc
''')
fn('kart_new', '''# Nouveau kart pour @s, à sa position et dans sa direction
tag @s add mg.kself
summon minecraft:block_display ~ ~ ~ {Tags:["mg.ib","mg.kart","mg.mine"],teleport_duration:2,block_state:{Name:"minecraft:red_concrete"},transformation:{translation:[%sf,%sf,%sf],%s,scale:[%sf,%sf,%sf]},Passengers:[%s]}
execute as @e[type=minecraft:block_display,tag=mg.mine] at @s rotated as @a[tag=mg.kself,limit=1] run tp @s ~ ~ ~ ~ 0
execute as @e[type=minecraft:block_display,tag=mg.mine] at @s on passengers run rotate @s ~ 0
scoreboard players operation @e[type=minecraft:block_display,tag=mg.mine] mg.ri = @s mg.ri
scoreboard players operation $kc mg.st = @s mg.ri
scoreboard players operation $kc mg.st %%= #k8 mg.st
%s
tag @e[tag=mg.mine] remove mg.mine
tag @s remove mg.kself
scoreboard players set @s mg.kdr 0
scoreboard players set @s mg.krc 0
''' % (ks(-0.6), ks(0.12), ks(-0.95), T0, ks(1.2), ks(0.38), ks(1.9), PASSENGERS, '\n'.join(
    f'execute if score $kc mg.st matches {k} run data modify entity @e[type=minecraft:block_display,tag=mg.mine,limit=1] block_state.Name set value "minecraft:{c}_concrete"'
    for k, c in enumerate(COLORS))))
fn('seat', f'''# Installe le pilote selon sa vue : 1re personne assis dans le kart, 3e personne spectateur de sa caméra
execute if score @s mg.kvm matches 1 run return run function mg:kart/seat_ride
function mg:kart/seat_cam
''')
fn('seat_ride', f'''execute if entity @s[gamemode=spectator] run gamemode adventure @s
scoreboard players operation $me mg.st = @s mg.ri
execute as @e[type=minecraft:item_display,tag=mg.khead] if score @s mg.ri = $me mg.st run kill @s
scoreboard players set $rd mg.st 0
execute on vehicle run scoreboard players set $rd mg.st 1
execute if score $rd mg.st matches 0 run ride @s mount {KK}
''')
fn('seat_cam', f'''scoreboard players set $rd mg.st 0
execute on vehicle run scoreboard players set $rd mg.st 1
execute if score $rd mg.st matches 1 run ride @s dismount
execute unless entity @s[gamemode=spectator] run gamemode spectator @s
execute unless entity @e[tag=mg.kcamc] run function mg:kart/cam_new
execute at @s unless entity @e[type=minecraft:item_display,tag=mg.kcamc,distance=..2] run spectate @e[type=minecraft:item_display,tag=mg.kcamc,limit=1] @s
''')
fn('cam_new', f'''# Caméra de poursuite de @s + sa tête posée sur le siège du kart
execute at {KK} run summon minecraft:item_display ~ ~2 ~ {{Tags:["mg.kcam","mg.kcamc","mg.fx"],teleport_duration:2}}
scoreboard players operation @e[type=minecraft:item_display,tag=mg.kcamc] mg.ri = @s mg.ri
execute at {KK} run summon minecraft:item_display ~ ~ ~ {{Tags:["mg.khead","mg.kheadn","mg.kpart","mg.fx"],teleport_duration:2,transformation:{{translation:[0f,0.62f,-0.1f],{T0},scale:[0.75f,0.75f,0.75f]}}}}
loot replace entity @e[type=minecraft:item_display,tag=mg.kheadn,limit=1] contents loot mg:plot_head
scoreboard players operation @e[type=minecraft:item_display,tag=mg.kheadn] mg.ri = @s mg.ri
ride @e[type=minecraft:item_display,tag=mg.kheadn,limit=1] mount {KK}
execute as {KK} at @s on passengers run rotate @s ~ 0
tag @e[tag=mg.kheadn] remove mg.kheadn
''')
fn('view_cmd', '''# /trigger mg.kv : 1 = 3e personne, 2 = 1re personne
execute if score @s mg.kv matches 1 run scoreboard players set @s mg.kvm 0
execute if score @s mg.kv matches 2 run scoreboard players set @s mg.kvm 1
execute if score @s mg.kv matches 1 run tellraw @s [{"text":"🎥 Vue 3e personne (Ctrl = objet).","color":"aqua"}]
execute if score @s mg.kv matches 2 run tellraw @s [{"text":"🎥 Vue 1re personne (clic droit ou Ctrl = objet).","color":"aqua"}]
scoreboard players reset @s mg.kv
scoreboard players enable @s mg.kv
''')
fn('go', '''# Départ : portillon ouvert
function mg:kart/gate_off
scoreboard players set $ktime mg.st 0
scoreboard players set @a[tag=mg.play] mg.ksp 0
tellraw @a[tag=mg.play] [{"text":"🏎 ","color":"gold"},{"text":"KART","color":"gold","bold":true},{"text":" : Z avancer, S freiner / reculer, Q / D tourner, ","color":"gray"},{"text":"ESPACE en tournant = dérapage","color":"yellow"},{"text":" (relâche après les étincelles bleues, orange ou violettes pour un mini-turbo). Boîtes ? = objets, Ctrl pour les utiliser. 3 tours !","color":"gray"}]
''')
fn('cleanup', '''# Fin de course (appelé par core/return_lobby)
kill @e[tag=mg.kpart]
kill @e[tag=mg.kcam]
kill @e[type=minecraft:item_display,tag=mg.kbox]
function mg:kart/fl_remove
''')

# ------------------------------------------------------------------ tick de course
fn('tick', f'''# Kart (état 2, jeu 61)
scoreboard players add $ktime mg.st 1
scoreboard players enable @a[tag=mg.play] mg.kv
execute as @a[tag=mg.play] run function mg:kart/drive
tag @e[tag=mg.kk] remove mg.kk
tag @e[tag=mg.kcamc] remove mg.kcamc

execute as @e[type=minecraft:item_display,tag=mg.kbox,tag=!mg.kboff] at @s if entity {KART},distance=..2.3] run function mg:kart/box_hit
execute as @e[type=minecraft:item_display,tag=mg.kboff] run function mg:kart/box_wait
execute as @e[type=minecraft:item_display,tag=mg.kshell] at @s run function mg:kart/shell_tick
execute as @e[type=minecraft:item_display,tag=mg.kban] at @s run function mg:kart/banana_tick
execute as @e[type=minecraft:item_display,tag=mg.kblue] at @s run function mg:kart/blue_tick

scoreboard players add $kph mg.st 1
execute if score $kph mg.st matches 4.. run function mg:kart/every4

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
function mg:kart/minimap
''')

# ------------------------------------------------------------------ pilotage
fn('drive', f'''# Pilotage du kart de @s (chaque tick)
function mg:kart/kk
execute unless entity @e[tag=mg.kk] at @s run function mg:kart/kart_new
execute unless entity @e[tag=mg.kk] run function mg:kart/kk
execute if score @s mg.kv matches 1.. run function mg:kart/view_cmd
function mg:kart/seat
execute as {KK} at @s run function mg:kart/probe
execute if score $kwa mg.st matches 1 run return run function mg:kart/rescue
execute if score $kyy mg.st matches ..6000 run return run function mg:kart/rescue

scoreboard players set $kf mg.st 0
scoreboard players set $kb mg.st 0
scoreboard players set $kl mg.st 0
scoreboard players set $kr mg.st 0
scoreboard players set $kj mg.st 0
scoreboard players set $ks mg.st 0
execute unless entity @s[tag=mg.kfin] run function mg:kart/inputs

# Objet : clic droit (1re personne) ou Ctrl
scoreboard players set $kuse mg.st 0
execute if score @s mg.qs matches 1.. run scoreboard players set $kuse mg.st 1
execute if score $ks mg.st matches 1 unless score @s mg.kspr matches 1 run scoreboard players set $kuse mg.st 1
scoreboard players operation @s mg.kspr = $ks mg.st
scoreboard players reset @s mg.qs
execute if score $kuse mg.st matches 1 run function mg:kart/use_item

scoreboard players remove @s[scores={{mg.kbo=1..}}] mg.kbo 1
scoreboard players remove @s[scores={{mg.kst=1..}}] mg.kst 1
function mg:kart/speed
function mg:kart/steer
function mg:kart/heading
function mg:kart/vertical
execute if score $kbp mg.st matches 1 if score $kg mg.st matches 1 run function mg:kart/boost_pad
execute if score @s mg.kst matches 1.. run function mg:kart/star_touch

execute store result storage mg:kart m.d double 0.01 run scoreboard players get @s mg.ksp
scoreboard players operation $kc mg.st = @s mg.ksp
execute if score @s mg.ksp matches 0.. run scoreboard players add $kc mg.st 75
execute if score @s mg.ksp matches ..-1 run scoreboard players remove $kc mg.st 75
execute store result storage mg:kart m.c double 0.01 run scoreboard players get $kc mg.st
execute store result storage mg:kart m.t double 0.1 run scoreboard players get $kt mg.st
execute store result storage mg:kart m.h double 0.1 run scoreboard players get @s mg.khd
execute store result storage mg:kart m.v double 0.01 run scoreboard players get $kv mg.st
execute as {KK} run function mg:kart/move with storage mg:kart m
function mg:kart/fx
execute unless entity @s[tag=mg.kfin] run function mg:kart/cp_check
''')
fn('inputs', '''execute if predicate mg:kart_f run scoreboard players set $kf mg.st 1
execute if predicate mg:kart_b run scoreboard players set $kb mg.st 1
execute if predicate mg:kart_l run scoreboard players set $kl mg.st 1
execute if predicate mg:kart_r run scoreboard players set $kr mg.st 1
execute if predicate mg:kart_j run scoreboard players set $kj mg.st 1
execute if predicate mg:kart_s run scoreboard players set $ks mg.st 1
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
execute store result score $kyaw mg.st run data get entity @s Rotation[0] 10
''')
fn('speed', '''# Vitesse (centièmes de bloc par tick) : 100 sur la route, 45 dans l'herbe, 125 en étoile, 150 en boost
scoreboard players set $kmx mg.st 100
execute if score $kro mg.st matches 0 if score $kg mg.st matches 1 run scoreboard players set $kmx mg.st 45
execute if score @s mg.kst matches 1.. run scoreboard players set $kmx mg.st 125
execute if score @s mg.kbo matches 1.. run scoreboard players set $kmx mg.st 150
execute if score @s mg.khi matches 1.. run return run function mg:kart/speed_hit

execute if score $kf mg.st matches 1 if score $kb mg.st matches 0 run scoreboard players add @s mg.ksp 5
execute if score $kb mg.st matches 1 if score $kf mg.st matches 0 if score @s mg.ksp matches 1.. run scoreboard players remove @s mg.ksp 10
execute if score $kb mg.st matches 1 if score $kf mg.st matches 0 if score @s mg.ksp matches ..0 run scoreboard players remove @s mg.ksp 3
execute if score $kf mg.st matches 0 if score $kb mg.st matches 0 if score @s mg.ksp matches 3.. run scoreboard players remove @s mg.ksp 2
execute if score $kf mg.st matches 0 if score $kb mg.st matches 0 if score @s mg.ksp matches ..-3 run scoreboard players add @s mg.ksp 2
execute if score $kf mg.st matches 0 if score $kb mg.st matches 0 if score @s mg.ksp matches -2..2 run scoreboard players set @s mg.ksp 0
execute if score @s mg.kbo matches 1.. if score @s mg.ksp < $kmx mg.st run scoreboard players operation @s mg.ksp = $kmx mg.st
execute if score @s mg.ksp > $kmx mg.st run scoreboard players remove @s mg.ksp 6
execute if score @s mg.ksp matches ..-36 run scoreboard players set @s mg.ksp -35
''')
fn('speed_hit', '''scoreboard players operation @s mg.ksp *= #k4 mg.st
scoreboard players operation @s mg.ksp /= #k5 mg.st
''')
fn('steer', '''# Direction en dixièmes de degré : plus serrée à basse vitesse, inversée en marche arrière, tête-à-queue si touché
scoreboard players set $kt mg.st 0
execute if score @s mg.khi matches 1.. run scoreboard players set $kt mg.st 360
execute if score @s mg.khi matches 1.. run return run scoreboard players remove @s mg.khi 1
scoreboard players operation $ka mg.st = @s mg.ksp
execute if score $ka mg.st matches ..-1 run scoreboard players operation $ka mg.st *= #km1 mg.st
scoreboard players set $kT mg.st 0
execute if score $ka mg.st matches 4..24 run scoreboard players set $kT mg.st 65
execute if score $ka mg.st matches 25..69 run scoreboard players set $kT mg.st 55
execute if score $ka mg.st matches 70.. run scoreboard players set $kT mg.st 45
execute if score $kl mg.st matches 1 run scoreboard players operation $kt mg.st -= $kT mg.st
execute if score $kr mg.st matches 1 run scoreboard players operation $kt mg.st += $kT mg.st
execute if score @s mg.ksp matches ..-1 run scoreboard players operation $kt mg.st *= #km1 mg.st
function mg:kart/drift
''')
fn('drift', '''# Dérapage : ESPACE + virage à plus de 40 ; mini-turbo bleu (20 ticks), orange (45), violet (80) au relâchement
execute if score @s mg.kdr matches 0 if score $kj mg.st matches 1 if score $kg mg.st matches 1 if score @s mg.ksp matches 40.. if score $kl mg.st matches 1 run function mg:kart/drift_start {d:-1}
execute if score @s mg.kdr matches 0 if score $kj mg.st matches 1 if score $kg mg.st matches 1 if score @s mg.ksp matches 40.. if score $kr mg.st matches 1 run function mg:kart/drift_start {d:1}
execute if score @s mg.kdr matches 1.. if score $kj mg.st matches 1 if score @s mg.ksp matches 30.. run return run function mg:kart/drift_hold
execute if score @s mg.kdr matches 1.. run function mg:kart/drift_end
''')
fn('drift_start', '''$scoreboard players set @s mg.kdd $(d)
scoreboard players set @s mg.kdr 1
scoreboard players set @s mg.kvy 18
execute at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 0.6 0.8
''')
fn('drift_hold', '''# Le nez pivote vers l'intérieur (la trajectoire suit avec retard, voir heading) ; la direction resserre ou élargit
scoreboard players add @s mg.kdr 1
scoreboard players operation $kt mg.st = @s mg.kdd
scoreboard players operation $kt mg.st *= #k60 mg.st
execute if score @s mg.kdd matches -1 if score $kl mg.st matches 1 run scoreboard players remove $kt mg.st 30
execute if score @s mg.kdd matches -1 if score $kr mg.st matches 1 run scoreboard players add $kt mg.st 35
execute if score @s mg.kdd matches 1 if score $kr mg.st matches 1 run scoreboard players add $kt mg.st 30
execute if score @s mg.kdd matches 1 if score $kl mg.st matches 1 run scoreboard players remove $kt mg.st 35
execute if score @s mg.kdr matches 20 at @s run playsound minecraft:block.amethyst_block.chime master @s ~ ~ ~ 1 1.0
execute if score @s mg.kdr matches 45 at @s run playsound minecraft:block.amethyst_block.chime master @s ~ ~ ~ 1 1.4
execute if score @s mg.kdr matches 80 at @s run playsound minecraft:block.amethyst_block.chime master @s ~ ~ ~ 1 1.9
''')
fn('drift_end', '''execute if score @s mg.kdr matches 80.. if score @s mg.kbo matches ..47 run scoreboard players set @s mg.kbo 48
execute if score @s mg.kdr matches 45..79 if score @s mg.kbo matches ..31 run scoreboard players set @s mg.kbo 32
execute if score @s mg.kdr matches 20..44 if score @s mg.kbo matches ..17 run scoreboard players set @s mg.kbo 18
execute if score @s mg.kdr matches 20.. at @s run playsound minecraft:entity.firework_rocket.launch master @a[tag=mg.play,distance=..24] ~ ~ ~ 0.8 1.4
scoreboard players set @s mg.kdr 0
scoreboard players set @s mg.krc 8
''')
fn('heading', '''# Trajectoire (mg.khd, dixièmes de degré) : suit le nez du kart, avec retard en dérapage (glisse) et juste après
execute if score @s mg.khi matches 1.. run return 0
scoreboard players operation $kyn mg.st = $kyaw mg.st
scoreboard players operation $kyn mg.st += $kt mg.st
execute unless score @s mg.kdr matches 1.. unless score @s mg.krc matches 1.. run return run scoreboard players operation @s mg.khd = $kyn mg.st
scoreboard players operation $kdf mg.st = $kyn mg.st
scoreboard players operation $kdf mg.st -= @s mg.khd
execute if score $kdf mg.st matches 1801.. run scoreboard players remove $kdf mg.st 3600
execute if score $kdf mg.st matches ..-1801 run scoreboard players add $kdf mg.st 3600
scoreboard players set $kfac mg.st 22
execute if score @s mg.kdr matches 0 run scoreboard players set $kfac mg.st 45
scoreboard players operation $kdf mg.st *= $kfac mg.st
scoreboard players operation $kdf mg.st /= #k100 mg.st
scoreboard players operation @s mg.khd += $kdf mg.st
scoreboard players remove @s[scores={mg.krc=1..}] mg.krc 1
''')
fn('vertical', '''scoreboard players set $kv mg.st 0
execute if score $kju mg.st matches 1 if score $kg mg.st matches 1 if score @s mg.kvy matches ..0 run scoreboard players set @s mg.kvy 52
execute if score $kg mg.st matches 1 if score @s mg.kvy matches ..0 run scoreboard players set @s mg.kvy 0
execute if score $kg mg.st matches 0 run scoreboard players remove @s mg.kvy 6
execute if score @s mg.kvy matches ..-90 run scoreboard players set @s mg.kvy -90
scoreboard players operation $kv mg.st = @s mg.kvy
''')
fn('boost_pad', '''execute if score @s mg.kbo matches ..15 at @s run playsound minecraft:entity.firework_rocket.launch master @a[tag=mg.play,distance=..24] ~ ~ ~ 1 1.2
execute if score @s mg.kbo matches ..21 run scoreboard players set @s mg.kbo 22
''')
CAM = '$execute at @s rotated $(h) 0 positioned ^ ^2.4 ^-5 rotated ~ 16 run tp @e[type=minecraft:item_display,tag=mg.kcamc,limit=1] ~ ~ ~ ~ ~'
fn('move', f'''# @s = kart : remis sur la route s'il s'y est enfoncé, nez tourné, avance selon la trajectoire (rebond si mur), caméra
execute at @s unless block ~ ~ ~ #mg:kart_pass align y run tp @s ~ ~1 ~
$execute at @s run tp @s ~ ~ ~ ~$(t) 0
execute at @s on passengers unless entity @s[type=minecraft:player] run rotate @s ~ 0
$execute at @s rotated $(h) 0 positioned ^ ^0.5 ^$(c) unless block ~ ~ ~ #mg:kart_pass run return run function mg:kart/bump {{v:$(v),h:$(h)}}
$execute at @s rotated $(h) 0 run tp @s ^ ^$(v) ^$(d)
{CAM}
''')
fn('bump', f'''$execute at @s run tp @s ~ ~$(v) ~
{CAM}
function mg:kart/bumped_owner
''')
fn('bumped_owner', '''scoreboard players operation $ko mg.st = @s mg.ri
execute as @a[tag=mg.play] if score @s mg.ri = $ko mg.st run function mg:kart/bumped
''')
fn('bumped', '''scoreboard players operation @s mg.ksp *= #km1 mg.st
scoreboard players operation @s mg.ksp /= #k3 mg.st
scoreboard players set @s mg.kdr 0
scoreboard players set @s mg.krc 0
execute at @s run playsound minecraft:block.wood.hit master @s ~ ~ ~ 1 0.6
''')
fn('rescue', f'''# Tombé à l'eau ou dans le vide : remis au point de passage précédent (@s = pilote)
scoreboard players operation $ki mg.st = @s mg.kcp
scoreboard players remove $ki mg.st 1
execute if score $ki mg.st matches ..-1 run scoreboard players operation $ki mg.st = $kK mg.st
execute if score $ki mg.st = $kK mg.st run scoreboard players remove $ki mg.st 1
execute as {KK} run function mg:kart/cp_tp
execute as {KK} at @s on passengers run rotate @s ~ 0
scoreboard players set @s mg.ksp 0
scoreboard players set @s mg.kvy 0
scoreboard players set @s mg.kdr 0
scoreboard players set @s mg.krc 0
scoreboard players set @s mg.khi 0
title @s actionbar [{{"text":"☁ Remis en piste !","color":"aqua"}}]
execute at @s run playsound minecraft:entity.chicken.egg master @s ~ ~ ~ 1 1
''')
fn('fx', f'''# Effets : fumée, étincelles de dérapage (bleues, orange, violettes), flammes de boost, étoile
execute if score @s mg.ksp matches 20.. as {KK} at @s rotated ~ 0 positioned ^ ^0.3 ^-0.9 run particle minecraft:smoke ~ ~ ~ 0.08 0.04 0.08 0.01 1
execute if score @s mg.kdr matches 20..44 as {KK} at @s rotated ~ 0 positioned ^0.5 ^0.15 ^-0.7 run particle minecraft:soul_fire_flame ~ ~ ~ 0.04 0.04 0.04 0.02 2
execute if score @s mg.kdr matches 20..44 as {KK} at @s rotated ~ 0 positioned ^-0.5 ^0.15 ^-0.7 run particle minecraft:soul_fire_flame ~ ~ ~ 0.04 0.04 0.04 0.02 2
execute if score @s mg.kdr matches 45..79 as {KK} at @s rotated ~ 0 positioned ^0.5 ^0.15 ^-0.7 run particle minecraft:flame ~ ~ ~ 0.04 0.04 0.04 0.02 3
execute if score @s mg.kdr matches 45..79 as {KK} at @s rotated ~ 0 positioned ^-0.5 ^0.15 ^-0.7 run particle minecraft:flame ~ ~ ~ 0.04 0.04 0.04 0.02 3
execute if score @s mg.kdr matches 80.. as {KK} at @s rotated ~ 0 positioned ^0.5 ^0.15 ^-0.7 run particle minecraft:dust{{color:[0.75f,0.25f,1.0f],scale:1.2f}} ~ ~ ~ 0.05 0.05 0.05 0 4
execute if score @s mg.kdr matches 80.. as {KK} at @s rotated ~ 0 positioned ^-0.5 ^0.15 ^-0.7 run particle minecraft:dust{{color:[0.75f,0.25f,1.0f],scale:1.2f}} ~ ~ ~ 0.05 0.05 0.05 0 4
execute if score @s mg.kbo matches 1.. as {KK} at @s rotated ~ 0 positioned ^ ^0.3 ^-1.0 run particle minecraft:flame ~ ~ ~ 0.12 0.08 0.12 0.03 4
execute if score @s mg.kst matches 1.. as {KK} at @s run particle minecraft:end_rod ~ ~0.7 ~ 0.5 0.4 0.5 0.05 4
''')
fn('star_touch', f'''# En étoile : les karts touchés partent en tête-à-queue
execute as {KK} at @s as {KART},tag=!mg.kk,distance=..1.8] run function mg:kart/owner_hit
''')
fn('owner_hit', '''# @s = kart : son pilote est touché
scoreboard players operation $ko mg.st = @s mg.ri
execute as @a[tag=mg.play] if score @s mg.ri = $ko mg.st run function mg:kart/hit
''')
fn('hit', f'''# @s touché (carapace, banane, éclair, étoile) : tête-à-queue, sauf en étoile
execute if score @s mg.kst matches 1.. run return 0
scoreboard players set @s mg.khi 20
scoreboard players set @s mg.kbo 0
scoreboard players set @s mg.kdr 0
scoreboard players set @s mg.krc 0
title @s actionbar [{{"text":"💥 Touché !","color":"red","bold":true}}]
scoreboard players operation $kh mg.st = @s mg.ri
execute as {KART}] if score @s mg.ri = $kh mg.st at @s run particle minecraft:explosion ~ ~0.5 ~ 0.3 0.3 0.3 0 2
execute as {KART}] if score @s mg.ri = $kh mg.st at @s run playsound minecraft:entity.generic.explode master @a[tag=mg.play,distance=..24] ~ ~ ~ 0.4 1.6
''')
fn('hit_big', '''function mg:kart/hit
execute if score @s mg.khi matches 1.. run scoreboard players set @s mg.khi 40
''')

# ------------------------------------------------------------------ course
fn('cp_pass', '''scoreboard players add @s mg.kcp 1
execute if score @s mg.kcp >= $kK mg.st run scoreboard players set @s mg.kcp 0
execute if score @s mg.kcp matches 1 run function mg:kart/lap
''')
fn('lap', '''scoreboard players add @s mg.klp 1
execute if score @s mg.klp > $kLaps mg.st run return run function mg:kart/finish
execute if score @s mg.klp matches 2.. if score @s mg.klp < $kLaps mg.st run title @s actionbar [{"text":"🏁 Tour ","color":"gold"},{"score":{"name":"@s","objective":"mg.klp"},"color":"yellow","bold":true},{"text":" / 3","color":"gold"}]
execute if score @s mg.klp = $kLaps mg.st run title @s title [{"text":"TOUR FINAL !","color":"gold","bold":true}]
execute if score @s mg.klp = $kLaps mg.st at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 0.8 1.6
''')
fn('finish', '''tag @s add mg.kfin
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
fn('progress', '''scoreboard players operation @s mg.kpg = @s mg.klp
scoreboard players operation @s mg.kpg *= #k1000 mg.st
scoreboard players operation @s mg.kpg += @s mg.kcp
execute if entity @s[tag=mg.kfin] run scoreboard players set @s mg.kpg 900000
execute if entity @s[tag=mg.kfin] run scoreboard players operation @s mg.kpg -= @s mg.kfp
''')
fn('rank_one', '''scoreboard players set @s mg.krk 1
scoreboard players operation $me mg.st = @s mg.kpg
tag @s add mg.kme
execute as @a[tag=mg.play] if score @s mg.kpg > $me mg.st run scoreboard players add @a[tag=mg.kme,limit=1] mg.krk 1
tag @s remove mg.kme
''')
ITEMS = {1: ('🍌 Banane', 'yellow'), 2: ('🟢 Carapace verte', 'green'), 3: ('🔴 Carapace rouge', 'red'),
         4: ('🍄 Champignon', 'gold'), 5: ('⭐ Étoile', 'yellow'), 6: ('⚡ Éclair', 'aqua'), 7: ('🔵 Carapace bleue', 'blue')}
MODEL = {1: 'minecraft:yellow_dye', 2: 'minecraft:turtle_scute', 3: 'minecraft:red_dye', 4: 'minecraft:red_mushroom',
         5: 'minecraft:nether_star', 6: 'minecraft:lightning_rod', 7: 'minecraft:heart_of_the_sea'}
hud = ['# Barre du bas : tour, position, objet, vitesse',
       'scoreboard players operation $kmh mg.st = @s mg.ksp',
       'scoreboard players operation $kmh mg.st *= #kkmh mg.st',
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
    hud.append(f'execute unless score @s mg.khi matches 1.. if score @s mg.kit matches {k} run title @s actionbar [{base},{{"text":"{name} (Ctrl)","color":"{color}","bold":true}}{tail}]')
fn('hud', '\n'.join(hud) + '\n')

# ------------------------------------------------------------------ minimap (tableau de droite)
fn('minimap', '''# Minimap : carte de base, un point par pilote à la couleur de son kart, puis les 15 lignes du tableau
data modify storage mg:kart mm set from storage mg:kart base
execute as @a[tag=mg.play] run function mg:kart/mm_dot
function mg:kart/mm_show with storage mg:kart mm
''')
fn('mm_dot', f'''# Case du kart de @s sur la minimap
scoreboard players operation $me mg.st = @s mg.ri
tag @e[tag=mg.kdot] remove mg.kdot
execute as {KART}] if score @s mg.ri = $me mg.st run tag @s add mg.kdot
execute unless entity @e[tag=mg.kdot] run return 0
execute store result score $mx mg.st run data get entity @e[tag=mg.kdot,limit=1] Pos[0]
execute store result score $mz mg.st run data get entity @e[tag=mg.kdot,limit=1] Pos[2]
scoreboard players operation $mx mg.st += #kmx0 mg.st
scoreboard players operation $mx mg.st *= #kmc mg.st
scoreboard players operation $mx mg.st /= #kmw mg.st
scoreboard players operation $mz mg.st -= #kmz0 mg.st
scoreboard players operation $mz mg.st *= #kmr mg.st
scoreboard players operation $mz mg.st /= #kmh mg.st
execute if score $mx mg.st matches ..-1 run scoreboard players set $mx mg.st 0
execute if score $mz mg.st matches ..-1 run scoreboard players set $mz mg.st 0
execute if score $mx mg.st >= #kmc mg.st run scoreboard players operation $mx mg.st = #kmc mg.st
execute if score $mx mg.st >= #kmc mg.st run scoreboard players remove $mx mg.st 1
execute if score $mz mg.st >= #kmr mg.st run scoreboard players operation $mz mg.st = #kmr mg.st
execute if score $mz mg.st >= #kmr mg.st run scoreboard players remove $mz mg.st 1
execute store result storage mg:kart dot.c int 1 run scoreboard players get $mx mg.st
execute store result storage mg:kart dot.r int 1 run scoreboard players get $mz mg.st
scoreboard players operation $kc mg.st = @s mg.ri
scoreboard players operation $kc mg.st %= #k8 mg.st
''' + '\n'.join(f'execute if score $kc mg.st matches {k} run data modify storage mg:kart dot.col set value "{c}"' for k, c in enumerate(TEXTC)) + '''
function mg:kart/mm_dot_m with storage mg:kart dot
''')
fn('mm_dot_m', '$data modify storage mg:kart mm.l$(r)[$(c)] set value {text:"█",color:"$(col)"}\n')

# ------------------------------------------------------------------ objets
fn('box_hit', f'''# Boîte touchée (@s = boîte) : elle disparaît 3 s ; les pilotes sans objet dont le kart est tout près en reçoivent un
tag @s add mg.kboff
scoreboard players set @s mg.t 60
item replace entity @s contents with minecraft:air
playsound minecraft:block.glass.break master @a[tag=mg.play,distance=..16] ~ ~ ~ 0.8 1.4
particle minecraft:wax_on ~ ~0.5 ~ 0.4 0.4 0.4 0 12
execute as @e[type=minecraft:text_display,tag=mg.kboxq,distance=..1.5] run data merge entity @s {{text:""}}
execute as {KART},distance=..2.3] run function mg:kart/owner_roll
''')
fn('owner_roll', '''scoreboard players operation $ko mg.st = @s mg.ri
execute as @a[tag=mg.play,scores={mg.kit=0}] if score @s mg.ri = $ko mg.st run function mg:kart/item_roll
''')
fn('box_wait', '''scoreboard players remove @s mg.t 1
execute if score @s mg.t matches 1.. run return 0
tag @s remove mg.kboff
item replace entity @s contents with minecraft:yellow_stained_glass
execute at @s as @e[type=minecraft:text_display,tag=mg.kboxq,distance=..1.5] run data merge entity @s {text:[{"text":"?","color":"gold","bold":true}]}
''')
fn('item_roll', '''# Tirage selon la position : les derniers ont de meilleurs objets (carapace bleue réservée aux derniers)
execute store result score $kr1 mg.st run random value 1..100
scoreboard players operation $kf1 mg.st = @s mg.krk
scoreboard players remove $kf1 mg.st 1
scoreboard players operation $kf1 mg.st *= #k100 mg.st
scoreboard players operation $kn1 mg.st = $kn mg.st
scoreboard players remove $kn1 mg.st 1
execute if score $kn1 mg.st matches ..0 run scoreboard players set $kf1 mg.st 50
execute if score $kn1 mg.st matches 1.. run scoreboard players operation $kf1 mg.st /= $kn1 mg.st
execute if score $kf1 mg.st matches ..33 run scoreboard players set $kgv mg.st 1
execute if score $kf1 mg.st matches ..33 if score $kr1 mg.st matches 41..75 run scoreboard players set $kgv mg.st 2
execute if score $kf1 mg.st matches ..33 if score $kr1 mg.st matches 76..95 run scoreboard players set $kgv mg.st 4
execute if score $kf1 mg.st matches ..33 if score $kr1 mg.st matches 96.. run scoreboard players set $kgv mg.st 3
execute if score $kf1 mg.st matches 34..66 run scoreboard players set $kgv mg.st 1
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 16..35 run scoreboard players set $kgv mg.st 2
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 36..65 run scoreboard players set $kgv mg.st 3
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 66..95 run scoreboard players set $kgv mg.st 4
execute if score $kf1 mg.st matches 34..66 if score $kr1 mg.st matches 96.. run scoreboard players set $kgv mg.st 5
execute if score $kf1 mg.st matches 67.. run scoreboard players set $kgv mg.st 2
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 11..30 run scoreboard players set $kgv mg.st 3
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 31..55 run scoreboard players set $kgv mg.st 4
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 56..78 run scoreboard players set $kgv mg.st 5
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 79..90 run scoreboard players set $kgv mg.st 6
execute if score $kf1 mg.st matches 67.. if score $kr1 mg.st matches 91.. run scoreboard players set $kgv mg.st 7
scoreboard players operation @s mg.kit = $kgv mg.st
function mg:kart/item_give
''')
give = ['# Objet en main (case 1) ; clic droit en 1re personne, Ctrl dans les deux vues']
for k, (name, color) in ITEMS.items():
    give.append(f'execute if score @s mg.kit matches {k} run item replace entity @s hotbar.0 with minecraft:warped_fungus_on_a_stick'
                f'[item_model="{MODEL[k]}",custom_name=[{{"text":"{name}","color":"{color}","bold":true,"italic":false}}],'
                f'lore=[[{{"text":"Ctrl (ou clic droit) pour l\'utiliser","color":"gray","italic":false}}]],unbreakable={{}}]')
    give.append(f'execute if score @s mg.kit matches {k} run title @s subtitle [{{"text":"{name}","color":"{color}","bold":true}}]')
give.append('title @s title ""')
give.append('execute at @s run playsound minecraft:entity.item.pickup master @s ~ ~ ~ 1 1.4')
fn('item_give', '\n'.join(give) + '\n')
fn('use_item', '''# Objet utilisé par @s (son kart porte mg.kk)
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
execute if score $kuse mg.st matches 7 run function mg:kart/use_blue
''')
fn('use_banana', f'''execute as {KK} at @s rotated ~ 0 positioned ^ ^0.15 ^-2.4 run summon minecraft:item_display ~ ~ ~ {{Tags:["mg.kban","mg.kbnew","mg.fx"],item:{{id:"minecraft:yellow_dye"}},billboard:"center",transformation:{{translation:[0f,0.3f,0f],{T0},scale:[1.3f,1.3f,1.3f]}}}}
scoreboard players set @e[type=minecraft:item_display,tag=mg.kbnew] mg.t 10
tag @e[tag=mg.kbnew] remove mg.kbnew
execute at @s run playsound minecraft:entity.item.pickup master @a[tag=mg.play,distance=..16] ~ ~ ~ 1 0.6
''')
fn('use_shell', f'''# Carapace devant le kart (verte : tout droit, rebondit ; rouge : vise le pilote juste devant)
$execute as {KK} at @s rotated ~ 0 positioned ^ ^0.45 ^1.9 run summon minecraft:item_display ~ ~ ~ {{Tags:["mg.kshell","$(t)","mg.knew","mg.fx"],teleport_duration:1,item:{{id:"minecraft:leather_helmet",components:{{"minecraft:dyed_color":$(c)}}}},transformation:{{translation:[0f,0f,0f],{T0},scale:[0.9f,0.9f,0.9f]}}}}
execute as {KK} at @s rotated ~ 0 positioned ^ ^0.45 ^1.9 as @e[type=minecraft:item_display,tag=mg.knew] run tp @s ~ ~ ~ ~ 0
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
fn('use_mushroom', '''scoreboard players set @s mg.kbo 32
execute at @s run playsound minecraft:entity.firework_rocket.launch master @a[tag=mg.play,distance=..24] ~ ~ ~ 1 1
title @s actionbar [{"text":"🍄 Turbo !","color":"gold","bold":true}]
''')
fn('use_star', '''scoreboard players set @s mg.kst 160
execute at @s run playsound minecraft:entity.player.levelup master @a[tag=mg.play,distance=..24] ~ ~ ~ 1 1.6
title @s actionbar [{"text":"⭐ Invincible !","color":"yellow","bold":true}]
''')
fn('use_lightning', '''tag @s add mg.kme
execute as @a[tag=mg.play,tag=!mg.kme] run function mg:kart/hit
tag @s remove mg.kme
execute as @a[tag=mg.play] at @s run playsound minecraft:entity.lightning_bolt.thunder master @s ~ ~ ~ 0.6 1.4
tellraw @a[tag=mg.play] [{"text":"★ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" foudroie tout le monde ⚡","color":"aqua"}]
''')
fn('use_blue', f'''# Carapace bleue : s'envole et file sur le premier, explose sur lui et ses voisins
execute as {KK} at @s run summon minecraft:item_display ~ ~3 ~ {{Tags:["mg.kblue","mg.knew","mg.fx"],teleport_duration:1,Glowing:1b,glow_color_override:3364351,item:{{id:"minecraft:leather_helmet",components:{{"minecraft:dyed_color":3364351}}}},transformation:{{translation:[0f,0f,0f],{T0},scale:[1.3f,1.3f,1.3f]}}}}
scoreboard players set @e[type=minecraft:item_display,tag=mg.knew] mg.t 400
tag @e[type=minecraft:item_display,tag=mg.knew] remove mg.knew
tellraw @a[tag=mg.play] [{{"text":"★ ","color":"gold"}},{{"selector":"@s","color":"yellow"}},{{"text":" lance une ","color":"gray"}},{{"text":"carapace bleue 🔵","color":"blue","bold":true}}]
execute as @a[tag=mg.play] at @s run playsound minecraft:entity.elder_guardian.curse master @s ~ ~ ~ 0.4 1.6
''')
fn('blue_tick', f'''# Carapace bleue (@s) : vise le kart du premier (à travers tout), explose à son contact
scoreboard players remove @s mg.t 1
execute if score @s mg.t matches ..0 run return run kill @s
tag @e[tag=mg.ktgt] remove mg.ktgt
execute as @a[tag=mg.play,tag=!mg.kfin,scores={{mg.krk=1}},limit=1] run scoreboard players operation $ktg mg.st = @s mg.ri
execute as {KART}] if score @s mg.ri = $ktg mg.st run tag @s add mg.ktgt
execute unless entity @e[tag=mg.ktgt] run return run kill @s
execute if entity @e[tag=mg.ktgt,distance=..2.2] run return run function mg:kart/blue_boom
execute facing entity @e[tag=mg.ktgt,limit=1] feet run tp @s ^ ^ ^1.8
particle minecraft:electric_spark ~ ~ ~ 0.2 0.2 0.2 0 3
''')
fn('blue_boom', f'''particle minecraft:explosion_emitter ~ ~ ~ 0 0 0 0 1
playsound minecraft:entity.generic.explode master @a[tag=mg.play,distance=..40] ~ ~ ~ 1 0.8
execute as {KART},distance=..4] run function mg:kart/owner_hit_big
kill @s
''')
fn('owner_hit_big', '''scoreboard players operation $ko mg.st = @s mg.ri
execute as @a[tag=mg.play] if score @s mg.ri = $ko mg.st run function mg:kart/hit_big
''')
fn('shell_tick', f'''# Carapace (@s) : avance, rebondit ou éclate contre un mur, touche un kart
scoreboard players remove @s mg.t 1
execute if score @s mg.t matches ..0 run return run kill @s
scoreboard players remove @s[scores={{mg.kbo=1..}}] mg.kbo 1
execute if entity @s[tag=mg.kred] unless score @s mg.kdd matches -1 run function mg:kart/shell_aim
execute positioned ^ ^ ^1.4 unless block ~ ~ ~ #mg:kart_pass run return run function mg:kart/shell_wall
tp @s ^ ^ ^1.4
particle minecraft:crit ~ ~0.2 ~ 0.1 0.1 0.1 0 1
execute if score @s mg.kbo matches 1.. run return 0
tag @s add mg.kcur
execute as {KART},distance=..1.7,limit=1,sort=nearest] run function mg:kart/shell_hit
tag @s remove mg.kcur
''')
fn('shell_aim', f'''scoreboard players operation $ktg mg.st = @s mg.kdd
tag @e[tag=mg.ktgt] remove mg.ktgt
execute as {KART}] if score @s mg.ri = $ktg mg.st run tag @s add mg.ktgt
execute facing entity @e[tag=mg.ktgt,limit=1] feet rotated ~ 0 run tp @s ~ ~ ~ ~ 0
tag @e[tag=mg.ktgt] remove mg.ktgt
''')
fn('shell_wall', '''execute if entity @s[tag=mg.kred] run return run kill @s
execute if score @s mg.kdr matches 3.. run return run kill @s
scoreboard players add @s mg.kdr 1
tp @s ~ ~ ~ ~180 0
playsound minecraft:block.stone.hit master @a[tag=mg.play,distance=..16] ~ ~ ~ 1 1.4
''')
fn('shell_hit', '''# @s = kart touché par l'objet marqué mg.kcur
function mg:kart/owner_hit
kill @e[type=minecraft:item_display,tag=mg.kcur]
''')
fn('banana_tick', f'''execute if score @s mg.t matches 1.. run return run scoreboard players remove @s mg.t 1
tag @s add mg.kcur
execute as {KART},distance=..1.5,limit=1,sort=nearest] run function mg:kart/shell_hit
tag @s remove mg.kcur
''')

# ------------------------------------------------------------------ fin de course
fn('end', '''execute as @a[tag=mg.play] run function mg:kart/progress
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
# objets Mario Kart (v3) : redéfinit item_roll, item_give, use_item, hit, speed, drive, tick, every4, shell_tick, hud
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'items_part.py'), encoding='utf-8').read())

# anciennes fonctions qui n'existent plus dans cette version
for old in ('remount', 'star_touch_old', 'grid_player'):
    p = os.path.join(K, old + '.mcfunction')
    if os.path.exists(p): os.remove(p)
print('ok')
