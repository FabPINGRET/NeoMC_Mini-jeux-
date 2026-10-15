# 🎄 Noël : pose le décor du spawn (généré par tools/lobby/gen_themes.py ; inverse : lobby/theme/off)
function mg:lobby/theme/sync
execute if score $theme mg.st matches 2 run return run tellraw @s {"text":"Ce décor est déjà en place.","color":"gray"}
# $thsw : l'autre thème est retiré pour laisser la place, sans le message « décor retiré »
scoreboard players set $thsw mg.st 1
execute if score $theme mg.st matches 1.. run function mg:lobby/theme/off
scoreboard players set $thsw mg.st 0
scoreboard players set $theme mg.st 2
data modify storage mg:lobby theme set value 2
# chute de particules : démarre tout de suite, avec fondu d'entrée (voir theme_fall.py)
scoreboard players set $thw mg.st 1
execute store result score $thd mg.st run random value 60..240
scoreboard players set $thi mg.st 0
function mg:lobby/theme/noel/place
tellraw @a [{"text":"🎄 ","color":"red"},{"text":"Il neige sur le spawn… Joyeuses fêtes !","color":"green","bold":true}]
execute as @a[x=-80,y=30,z=-80,dx=160,dy=120,dz=160,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 1 0.8
