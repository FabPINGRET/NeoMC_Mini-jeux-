execute unless score @s mg.olm4 matches 2.. run return run tellraw @s {"text":"Il faut 2 × fiole de venin.","color":"red"}
execute unless score @s mg.olg matches 80.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 80
scoreboard players remove @s mg.olm4 2
effect give @s minecraft:strength 180 0
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ Élixir de force ","color":"green","bold":true},{"text":"(-80 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
