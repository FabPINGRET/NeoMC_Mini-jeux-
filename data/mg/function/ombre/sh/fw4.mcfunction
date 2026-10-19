# arme palier 4
execute unless score @s mg.ollv matches 10.. run return run tellraw @s {"text":"⚒ « Reviens au niveau 10. »","color":"red"}
execute unless score @s mg.olm3 matches 10.. run return run tellraw @s {"text":"⚒ « Il me faut 10 × éclat de givre et 600 💰. »","color":"red"}
execute unless score @s mg.olg matches 600.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 600
scoreboard players remove @s mg.olm3 10
scoreboard players set @s mg.olwt 4
function mg:ombre/kit
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 1
execute at @s run particle minecraft:lava ~ ~1 ~ 0.4 0.4 0.4 0 12
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ Arme de givre ","color":"green","bold":true},{"text":"(-600 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
