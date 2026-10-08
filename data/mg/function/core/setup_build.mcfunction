# Construction du lobby et de toutes les arènes (chunks déjà forceloadés)

function mg:lobby/build
schedule function mg:lobby/food_build 20s
schedule function mg:elytra/build 22s
function mg:lobby/armory_build
function mg:parkour/build
function mg:plot/build
function mg:party/build
data remove storage mg:kart built2
data remove storage mg:dropadv v3
schedule function mg:dropadv/build 30s
data remove storage mg:elyrace v1
schedule function mg:elyrace/build 45s
schedule function mg:sky/build 40s
data remove storage mg:kart built3
function mg:kart/build
function mg:dust/build
function mg:mirage/build
function mg:nuketown/build
function mg:spleef/build
function mg:splegg/build
function mg:splegg/build_xxl
function mg:sumo/build
function mg:oitc/build
function mg:oitc/build_1
function mg:oitc/build_2
function mg:tnttag/build
function mg:blockparty/build
function mg:anvil/build
function mg:turf/build
function mg:turf/columns
function mg:quake/build
function mg:quake/build_1
function mg:quake/build_2
function mg:quake/build_3
function mg:quake/build_4
function mg:paintball/build
function mg:paintball/build_1
function mg:paintball/build_2
function mg:icerace/build
function mg:bb/build
function mg:mobarena/cathedral/build
function mg:mobarena/lab/build
function mg:mobarena/temple/build
function mg:mobarena/forge/build
function mg:mobarena/ship/build
function mg:dropper/build
execute positioned 120 58 5197 run function mg:dropper/shell_s
function mg:tntrun/build
function mg:pvp/build
function mg:bedwars/build
function mg:sheepwar/build
function mg:sheepwar2/build
function mg:sheepwar3/build
function mg:sheepwar4/build
function mg:sheepwar5/build
function mg:sheepwar6/build
function mg:sheepwar7/build
function mg:sheepwar8/build
function mg:mobarena/build

setworldspawn 0 64 0
scoreboard players set $setup mg.st 1

# Ré-initialise tous les joueurs (tp lobby + objet menu)
tag @a remove mg.init

tellraw @a [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Installation terminée !","color":"green"}]
tellraw @a[tag=mg.admin] [{"text":"Admin : clic droit sur ","color":"gray"},{"text":"≡ MENU","color":"gold"},{"text":" (ou ","color":"gray"},{"text":"/trigger mg.menu","color":"yellow"},{"text":") pour lancer un jeu.","color":"gray"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1
