# armure palier 5
execute unless score @s mg.ollv matches 15.. run return run tellraw @s {"text":"⚒ « Reviens au niveau 15. »","color":"red"}
execute unless score @s mg.olm4 matches 14.. run return run tellraw @s {"text":"⚒ « Il me faut 14 × fiole de venin et 1200 💰. »","color":"red"}
execute unless score @s mg.olg matches 1200.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 1200
scoreboard players remove @s mg.olm4 14
scoreboard players set @s mg.olat 5
function mg:ombre/kit
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 0.8
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ Armure de diamant ","color":"green","bold":true},{"text":"(-1200 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
