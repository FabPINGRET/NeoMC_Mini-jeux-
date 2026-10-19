execute unless score @s mg.olm2 matches 2.. run return run tellraw @s {"text":"Il faut 2 × soie d'araignée.","color":"red"}
execute unless score @s mg.olg matches 60.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 60
scoreboard players remove @s mg.olm2 2
effect give @s minecraft:speed 180 0
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ Élixir de vent ","color":"green","bold":true},{"text":"(-60 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
