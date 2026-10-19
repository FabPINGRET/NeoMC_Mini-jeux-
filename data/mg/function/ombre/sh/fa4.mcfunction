# armure palier 4
execute unless score @s mg.ollv matches 11.. run return run tellraw @s {"text":"⚒ « Reviens au niveau 11. »","color":"red"}
execute unless score @s mg.olm3 matches 12.. run return run tellraw @s {"text":"⚒ « Il me faut 12 × éclat de givre et 800 💰. »","color":"red"}
execute unless score @s mg.olg matches 800.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 800
scoreboard players remove @s mg.olm3 12
scoreboard players set @s mg.olat 4
function mg:ombre/kit
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 0.8
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ Armure de givre ","color":"green","bold":true},{"text":"(-800 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
