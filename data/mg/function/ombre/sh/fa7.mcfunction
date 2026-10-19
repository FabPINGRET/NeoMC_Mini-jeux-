# armure palier 7
execute unless score @s mg.ollv matches 23.. run return run tellraw @s {"text":"⚒ « Reviens au niveau 23. »","color":"red"}
execute unless score @s mg.olm6 matches 18.. run return run tellraw @s {"text":"⚒ « Il me faut 18 × écaille de drake et 2800 💰. »","color":"red"}
execute unless score @s mg.olg matches 2800.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 2800
scoreboard players remove @s mg.olm6 18
scoreboard players set @s mg.olat 7
function mg:ombre/kit
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 0.8
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ Armure d'écailles ","color":"green","bold":true},{"text":"(-2800 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
