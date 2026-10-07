# Attente au respawn (@s = joueur, mg.cd > 20) : immobilisé à la base, compte à rebours en actionbar
effect give @s minecraft:slowness 1 255 true
effect give @s minecraft:jump_boost 1 128 true
scoreboard players operation @s mg.t = @s mg.cd
scoreboard players remove @s mg.t 1
scoreboard players operation @s mg.t /= $c20 mg.st
title @s actionbar [{"text":"✖ Réapparition dans ","color":"red"},{"score":{"name":"@s","objective":"mg.t"},"color":"gold","bold":true},{"text":" s","color":"red"}]
execute if score @s mg.cd matches 21 run title @s actionbar [{"text":"▓ GO !","color":"green","bold":true}]
