# arme palier 5
execute unless score @s mg.ollv matches 14.. run return run tellraw @s {"text":"⚒ « Reviens au niveau 14. »","color":"red"}
execute unless score @s mg.olm4 matches 12.. run return run tellraw @s {"text":"⚒ « Il me faut 12 × fiole de venin et 1000 💰. »","color":"red"}
execute unless score @s mg.olg matches 1000.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 1000
scoreboard players remove @s mg.olm4 12
scoreboard players set @s mg.olwt 5
function mg:ombre/kit
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 1
execute at @s run particle minecraft:lava ~ ~1 ~ 0.4 0.4 0.4 0 12
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ Arme des marais ","color":"green","bold":true},{"text":"(-1000 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
