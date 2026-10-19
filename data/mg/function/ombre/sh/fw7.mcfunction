# arme palier 7
execute unless score @s mg.ollv matches 22.. run return run tellraw @s {"text":"⚒ « Reviens au niveau 22. »","color":"red"}
execute unless score @s mg.olm6 matches 16.. run return run tellraw @s {"text":"⚒ « Il me faut 16 × écaille de drake et 2500 💰. »","color":"red"}
execute unless score @s mg.olg matches 2500.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 2500
scoreboard players remove @s mg.olm6 16
scoreboard players set @s mg.olwt 7
function mg:ombre/kit
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 1
execute at @s run particle minecraft:lava ~ ~1 ~ 0.4 0.4 0.4 0 12
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ Arme draconique ","color":"green","bold":true},{"text":"(-2500 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
