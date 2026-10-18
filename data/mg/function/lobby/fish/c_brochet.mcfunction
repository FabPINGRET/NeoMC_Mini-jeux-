# Prise : un brochet (rare, poids 60 sur 1000) ; @s = joueur, effets au marqueur mg.lfx
scoreboard players add $catch mg.lfn 1
execute store result score #lfs mg.st run random value 40..80
title @s subtitle [{"text":"un brochet","color":"aqua","bold":true},{"text":" de ","color":"gray"},{"score":{"name":"#lfs","objective":"mg.st"},"color":"yellow"},{"text":" cm","color":"gray"}]
title @s title {"text":"⭐ Belle prise !","color":"gold","bold":true}
tellraw @a[distance=..24] [{"selector":"@s","color":"yellow"},{"text":" a sorti ","color":"gray"},{"text":"un brochet","color":"aqua","bold":true},{"text":" de ","color":"gray"},{"score":{"name":"#lfs","objective":"mg.st"},"color":"yellow"},{"text":" cm","color":"gray"},{"text":" !","color":"gray"}]
execute at @e[type=minecraft:marker,tag=mg.lfx,limit=1] run playsound minecraft:entity.player.levelup player @a[distance=..16] ~ ~ ~ 1 1.4
execute at @e[type=minecraft:marker,tag=mg.lfx,limit=1] run particle minecraft:happy_villager ~ ~0.3 ~ 0.4 0.3 0.4 0 14 normal @a[distance=..16]
function mg:lobby/fish/pb
