# @s est tombé : retour au dernier point de passage
scoreboard players operation $c mg.st = @s mg.sjp
execute as @e[type=minecraft:marker,tag=mg.sjc] if score @s mg.t = $c mg.st run tag @s add mg.sjx
tp @s @e[type=minecraft:marker,tag=mg.sjx,limit=1]
tag @e[tag=mg.sjx] remove mg.sjx
execute at @s run playsound minecraft:entity.slime.squish master @s ~ ~ ~ 1 0.7
title @s actionbar {"text":"💧 Plouf ! Retour au dernier point","color":"aqua"}
