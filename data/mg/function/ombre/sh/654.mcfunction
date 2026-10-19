execute unless score @s mg.olm7 matches 2.. run return run tellraw @s {"text":"Il faut 2 × minerai de runite.","color":"red"}
execute unless score @s mg.olg matches 120.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 120
scoreboard players remove @s mg.olm7 2
effect give @s minecraft:resistance 180 0
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ Élixir de pierre ","color":"green","bold":true},{"text":"(-120 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
