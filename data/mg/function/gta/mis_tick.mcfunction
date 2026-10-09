# @s (mission en cours, toutes les 5 ticks, à sa position) : temps, étapes, faisceau sur l'objectif
scoreboard players operation $gb mg.st = @s mg.bid
tag @e remove mg.gmine
execute as @e[tag=mg.gmo] if score @s mg.bid = $gb mg.st run tag @s add mg.gmine
scoreboard players remove @s mg.gmtime 5
scoreboard players operation @s mg.gmsec = @s mg.gmtime
scoreboard players set #20 mg.st 20
scoreboard players operation @s mg.gmsec /= #20 mg.st
execute if score @s mg.gmtime matches ..0 run return run function mg:gta/mis_fail
execute at @e[tag=mg.gmine] run particle minecraft:end_rod ~ ~3 ~ 0.05 4 0.05 0 8 force @s
execute if score @s mg.gmt matches 1 if score @s mg.gms matches 1 if entity @e[tag=mg.gmine,tag=mg.gmpk,distance=..2.5] run return run function mg:gta/mis1_picked
execute if score @s mg.gmt matches 1 if score @s mg.gms matches 2 if entity @e[tag=mg.gmine,tag=mg.gmdl,distance=..3] run return run function mg:gta/mis_win
execute if score @s mg.gmt matches 2 unless entity @e[tag=mg.gmine,tag=mg.gmvip] run return run function mg:gta/mis_win
execute if score @s mg.gmt matches 3 if entity @e[tag=mg.gmine,tag=mg.gmcp,distance=..4] run return run function mg:gta/mis3_next
