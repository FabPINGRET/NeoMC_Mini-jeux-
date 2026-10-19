# arme palier 6
execute unless score @s mg.ollv matches 18.. run return run tellraw @s {"text":"⚒ « Reviens au niveau 18. »","color":"red"}
execute unless score @s mg.olm5 matches 14.. run return run tellraw @s {"text":"⚒ « Il me faut 14 × ambre solaire et 1600 💰. »","color":"red"}
execute unless score @s mg.olg matches 1600.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 1600
scoreboard players remove @s mg.olm5 14
scoreboard players set @s mg.olwt 6
function mg:ombre/kit
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 1
execute at @s run particle minecraft:lava ~ ~1 ~ 0.4 0.4 0.4 0 12
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ Arme solaire ","color":"green","bold":true},{"text":"(-1600 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
