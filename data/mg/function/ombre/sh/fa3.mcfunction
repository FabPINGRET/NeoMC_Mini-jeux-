# armure palier 3
execute unless score @s mg.ollv matches 8.. run return run tellraw @s {"text":"⚒ « Reviens au niveau 8. »","color":"red"}
execute unless score @s mg.olm2 matches 10.. run return run tellraw @s {"text":"⚒ « Il me faut 10 × soie d'araignée et 450 💰. »","color":"red"}
execute unless score @s mg.olg matches 450.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 450
scoreboard players remove @s mg.olm2 10
scoreboard players set @s mg.olat 3
function mg:ombre/kit
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 0.8
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ Armure d'acier ","color":"green","bold":true},{"text":"(-450 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
