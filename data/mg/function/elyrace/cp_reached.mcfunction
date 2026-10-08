# @s = joueur qui valide un anneau qui est aussi un point de reprise
scoreboard players operation @s mg.xc = @s mg.xa
title @s actionbar [{"text":"⚑ Point de reprise enregistré","color":"green","bold":true}]
execute at @s run playsound minecraft:block.beacon.activate master @s ~ ~ ~ 1 1.5
