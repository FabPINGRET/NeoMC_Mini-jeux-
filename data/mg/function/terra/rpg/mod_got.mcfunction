# @s récupère le module $k : embuscade dans le marais
scoreboard players set @s mg.trpk 0
scoreboard players operation @s mg.trqp += $kb mg.st
function mg:terra/rpg/xp {n:50}
title @s actionbar {"text":"💾 Module récupéré !","color":"aqua","bold":true}
execute at @s run playsound minecraft:block.beacon.activate player @s ~ ~ ~ 0.7 1.6
tellraw @s {"text":"⚠ Le signal du module attire des dilophosaures !","color":"red"}
execute at @s positioned ~6 ~ ~6 run function mg:terra/dino/dilo
tag @e[tag=mg.tvlast] add mg.trr
execute at @s positioned ~-6 ~ ~-4 run function mg:terra/dino/compy
tag @e[tag=mg.tvlast] add mg.trr
execute at @s positioned ~-6 ~ ~-5 run function mg:terra/dino/compy
tag @e[tag=mg.tvlast] add mg.trr
execute if score @s mg.trqp matches 7.. run function mg:terra/rpg/ch {n:35}
