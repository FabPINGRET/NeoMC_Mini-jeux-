# @s : bonus de vie du niveau (2 PV tous les 2 niveaux)
attribute @s minecraft:max_health modifier remove mg:trlv
scoreboard players operation $hp mg.st = @s mg.trlv
scoreboard players remove $hp mg.st 1
scoreboard players operation $hp mg.st /= #2 mg.st
scoreboard players operation $hp mg.st *= #2 mg.st
execute store result storage mg:terra s.hp int 1 run scoreboard players get $hp mg.st
function mg:terra/rpg/stats_m with storage mg:terra s
function mg:terra/rpg/cl/passive
function mg:terra/rpg/st/apply
