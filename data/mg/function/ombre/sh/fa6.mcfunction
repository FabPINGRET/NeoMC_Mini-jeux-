# armure palier 6
execute unless score @s mg.ollv matches 19.. run return run tellraw @s {"text":"⚒ « Reviens au niveau 19. »","color":"red"}
execute unless score @s mg.olm5 matches 16.. run return run tellraw @s {"text":"⚒ « Il me faut 16 × ambre solaire et 1800 💰. »","color":"red"}
execute unless score @s mg.olg matches 1800.. run return run function mg:ombre/sh/poor
scoreboard players remove @s mg.olg 1800
scoreboard players remove @s mg.olm5 16
scoreboard players set @s mg.olat 6
function mg:ombre/kit
execute at @s run playsound minecraft:block.anvil.use player @a ~ ~ ~ 0.8 0.8
scoreboard players set @s mg.olal 40
title @s actionbar [{"text":"✔ Armure solaire ","color":"green","bold":true},{"text":"(-1800 💰)","color":"gold"}]
execute at @s run playsound minecraft:entity.villager.yes player @s ~ ~ ~ 0.8 1.1
