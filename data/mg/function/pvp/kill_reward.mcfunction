# Récompense de KILL (@s = le tueur)
scoreboard players reset @s mg.pk
effect give @s minecraft:instant_health 1 1 true
effect give @s minecraft:saturation 3 0 true
title @s actionbar [{"text":"☠ KILL ! ","color":"red","bold":true},{"text":"+4 cœurs","color":"green"}]
execute at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.8 1.5
