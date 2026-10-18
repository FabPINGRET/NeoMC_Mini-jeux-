# Prise : une truite (common, poids 160 sur 1000) ; @s = joueur, effets au marqueur mg.lfx
scoreboard players add $catch mg.lfn 1
execute store result score #lfs mg.st run random value 10..40
title @s actionbar [{"text":"🎣 ","color":"aqua"},{"text":"Une truite","color":"green","bold":true},{"text":" de ","color":"gray"},{"score":{"name":"#lfs","objective":"mg.st"},"color":"yellow"},{"text":" cm","color":"gray"}]
execute at @e[type=minecraft:marker,tag=mg.lfx,limit=1] run playsound minecraft:entity.fishing_bobber.splash player @a[distance=..16] ~ ~ ~ 1 1.2
execute at @e[type=minecraft:marker,tag=mg.lfx,limit=1] run particle minecraft:splash ~ ~0.3 ~ 0.3 0.1 0.3 0.1 12 normal @a[distance=..16]
function mg:lobby/fish/pb
