# fin de cinématique : retour à l'endroit de départ
scoreboard players operation $own mg.st = @s mg.tvpid
spectate
execute as @e[type=minecraft:item_display,tag=mg.trcam] if score @s mg.tvo = $own mg.st run kill @s
tag @s remove mg.trcine
scoreboard players set @s mg.trcs 0
gamemode adventure @s
title @s clear
execute store result storage mg:terra d.x int 1 run scoreboard players get @s mg.tvx
execute store result storage mg:terra d.y int 1 run scoreboard players get @s mg.tvy
execute store result storage mg:terra d.z int 1 run scoreboard players get @s mg.tvz
function mg:terra/rpg/cs/back with storage mg:terra d
