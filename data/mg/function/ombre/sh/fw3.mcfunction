# arme palier 3
execute unless score @s mg.ollv matches 6.. run return run tellraw @s {"text":"⚒ « Reviens au niveau 6. »","color":"red"}
execute unless score @s mg.olm2 matches 8.. run return run tellraw @s {"text":"⚒ « Il me faut 8 × soie d'araignée et 300 💰. »","color":"red"}
execute unless score @s mg.olg matches 300.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 300
scoreboard players remove @s mg.olm2 8
scoreboard players set @s mg.olwt 3
function mg:ombre/kit
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 1
execute at @s run particle minecraft:lava ~ ~1 ~ 0.4 0.4 0.4 0 12
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ Arme sylvestre ","color":"green","bold":true},{"text":"(-300 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
