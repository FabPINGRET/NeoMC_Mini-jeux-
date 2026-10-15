# 🎃 Halloween : pose le décor du spawn (généré par tools/lobby/gen_themes.py ; inverse : lobby/theme/off)
function mg:lobby/theme/sync
execute if score $theme mg.st matches 1 run return run tellraw @s {"text":"Ce décor est déjà en place.","color":"gray"}
# $thsw : l'autre thème est retiré pour laisser la place, sans le message « décor retiré »
scoreboard players set $thsw mg.st 1
execute if score $theme mg.st matches 1.. run function mg:lobby/theme/off
scoreboard players set $thsw mg.st 0
scoreboard players set $theme mg.st 1
data modify storage mg:lobby theme set value 1
function mg:lobby/theme/halloween/place
tellraw @a [{"text":"🎃 ","color":"gold"},{"text":"Le spawn se pare de ses habits d'Halloween… Bouh !","color":"gold","bold":true}]
execute as @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] at @s run playsound minecraft:entity.witch.celebrate master @s ~ ~ ~ 1 0.8
