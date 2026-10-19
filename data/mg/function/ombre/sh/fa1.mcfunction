# armure palier 1
execute unless score @s mg.ollv matches 2.. run return run tellraw @s {"text":"⚒ « Reviens au niveau 2. »","color":"red"}
execute unless score @s mg.olm1 matches 4.. run return run tellraw @s {"text":"⚒ « Il me faut 4 × peau de bête et 80 💰. »","color":"red"}
execute unless score @s mg.olg matches 80.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 80
scoreboard players remove @s mg.olm1 4
scoreboard players set @s mg.olat 1
function mg:ombre/kit
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 0.8
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ Cuir renforcé ","color":"green","bold":true},{"text":"(-80 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
