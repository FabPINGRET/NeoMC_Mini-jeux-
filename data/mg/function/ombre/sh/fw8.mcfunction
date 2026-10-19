# arme palier 8
execute unless score @s mg.ollv matches 26.. run return run tellraw @s {"text":"⚒ « Reviens au niveau 26. »","color":"red"}
execute unless score @s mg.olm7 matches 18.. run return run tellraw @s {"text":"⚒ « Il me faut 18 × minerai de runite et 3800 💰. »","color":"red"}
execute unless score @s mg.olg matches 3800.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 3800
scoreboard players remove @s mg.olm7 18
scoreboard players set @s mg.olwt 8
function mg:ombre/kit
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 1
execute at @s run particle minecraft:lava ~ ~1 ~ 0.4 0.4 0.4 0 12
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ Arme runique ","color":"green","bold":true},{"text":"(-3800 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
