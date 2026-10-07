# Ballons du kart de @s (autant que mg.kbl), à sa couleur
scoreboard players operation $me mg.st = @s mg.ri
execute as @e[type=minecraft:item_display,tag=mg.kbal] if score @s mg.ri = $me mg.st run kill @s
function mg:kart/kk
execute unless entity @e[tag=mg.kk] run return 0
data modify storage mg:kart bal.m set value "minecraft:red_wool"
execute if score $rp mg.st matches 1 run data modify storage mg:kart bal.m set value "mg:balloon"
data modify storage mg:kart bal.c set value 15022389
execute if score @e[type=minecraft:block_display,tag=mg.kk,limit=1] mg.kcol matches 1 run data modify storage mg:kart bal.c set value 15022389
execute if score @e[type=minecraft:block_display,tag=mg.kk,limit=1] mg.kcol matches 2 run data modify storage mg:kart bal.c set value 2712319
execute if score @e[type=minecraft:block_display,tag=mg.kk,limit=1] mg.kcol matches 3 run data modify storage mg:kart bal.c set value 6610199
execute if score @e[type=minecraft:block_display,tag=mg.kk,limit=1] mg.kcol matches 4 run data modify storage mg:kart bal.c set value 16766464
execute if score @e[type=minecraft:block_display,tag=mg.kk,limit=1] mg.kcol matches 5 run data modify storage mg:kart bal.c set value 9315498
execute if score @e[type=minecraft:block_display,tag=mg.kk,limit=1] mg.kcol matches 6 run data modify storage mg:kart bal.c set value 16739584
execute if score @e[type=minecraft:block_display,tag=mg.kk,limit=1] mg.kcol matches 7 run data modify storage mg:kart bal.c set value 47316
execute if score @e[type=minecraft:block_display,tag=mg.kk,limit=1] mg.kcol matches 8 run data modify storage mg:kart bal.c set value 16728193
data modify storage mg:kart bal.s set value 1
data modify storage mg:kart bal.x set value -0.45f
data modify storage mg:kart bal.y set value 1.35f
data modify storage mg:kart bal.z set value -0.7f
execute if score @s mg.kbl matches 1.. at @e[type=minecraft:block_display,tag=mg.kk,limit=1] run function mg:kart/bat_bal with storage mg:kart bal
data modify storage mg:kart bal.s set value 2
data modify storage mg:kart bal.x set value 0.0f
data modify storage mg:kart bal.y set value 1.62f
data modify storage mg:kart bal.z set value -0.85f
execute if score @s mg.kbl matches 2.. at @e[type=minecraft:block_display,tag=mg.kk,limit=1] run function mg:kart/bat_bal with storage mg:kart bal
data modify storage mg:kart bal.s set value 3
data modify storage mg:kart bal.x set value 0.45f
data modify storage mg:kart bal.y set value 1.35f
data modify storage mg:kart bal.z set value -0.7f
execute if score @s mg.kbl matches 3.. at @e[type=minecraft:block_display,tag=mg.kk,limit=1] run function mg:kart/bat_bal with storage mg:kart bal
scoreboard players operation @e[type=minecraft:item_display,tag=mg.kbaln] mg.ri = @s mg.ri
execute as @e[type=minecraft:item_display,tag=mg.kbaln] run ride @s mount @e[type=minecraft:block_display,tag=mg.kk,limit=1]
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s on passengers run rotate @s ~ 0
tag @e[tag=mg.kbaln] remove mg.kbaln
