# armure palier 8
execute unless score @s mg.ollv matches 27.. run return run tellraw @s {"text":"⚒ « Reviens au niveau 27. »","color":"red"}
execute unless score @s mg.olm7 matches 20.. run return run tellraw @s {"text":"⚒ « Il me faut 20 × minerai de runite et 4200 💰. »","color":"red"}
execute unless score @s mg.olg matches 4200.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 4200
scoreboard players remove @s mg.olm7 20
scoreboard players set @s mg.olat 8
function mg:ombre/kit
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 0.8
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ Armure runique ","color":"green","bold":true},{"text":"(-4200 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
