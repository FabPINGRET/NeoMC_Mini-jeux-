# arme palier 2
execute unless score @s mg.ollv matches 3.. run return run tellraw @s {"text":"⚒ « Reviens au niveau 3. »","color":"red"}
execute unless score @s mg.olm1 matches 6.. run return run tellraw @s {"text":"⚒ « Il me faut 6 × peau de bête et 120 💰. »","color":"red"}
execute unless score @s mg.olg matches 120.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 120
scoreboard players remove @s mg.olm1 6
scoreboard players set @s mg.olwt 2
function mg:ombre/kit
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 1
execute at @s run particle minecraft:lava ~ ~1 ~ 0.4 0.4 0.4 0 12
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ Arme d'acier ","color":"green","bold":true},{"text":"(-120 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
