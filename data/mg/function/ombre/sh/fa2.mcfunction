# armure palier 2
execute unless score @s mg.ollv matches 5.. run return run tellraw @s {"text":"⚒ « Reviens au niveau 5. »","color":"red"}
execute unless score @s mg.olm1 matches 8.. run return run tellraw @s {"text":"⚒ « Il me faut 8 × peau de bête et 220 💰. »","color":"red"}
execute unless score @s mg.olg matches 220.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 220
scoreboard players remove @s mg.olm1 8
scoreboard players set @s mg.olat 2
function mg:ombre/kit
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 0.8
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ Cotte de mailles ","color":"green","bold":true},{"text":"(-220 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
