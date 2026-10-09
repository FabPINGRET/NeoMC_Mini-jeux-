# @s : un autre joueur de Neo GTA, ajouté (point bleu) à la carte de celui qui la regarde
execute store result score $goi mg.st run data get entity @s Pos[0]
execute store result score $goj mg.st run data get entity @s Pos[2]
scoreboard players add $goi mg.st 88
scoreboard players remove $goj mg.st 32312
scoreboard players operation $goi mg.st *= #30 mg.st
scoreboard players operation $goi mg.st /= #177 mg.st
scoreboard players operation $goj mg.st *= #30 mg.st
scoreboard players operation $goj mg.st /= #177 mg.st
execute if score $goi mg.st matches ..-1 run scoreboard players set $goi mg.st 0
execute if score $goi mg.st matches 30.. run scoreboard players set $goi mg.st 29
execute if score $goj mg.st matches ..-1 run scoreboard players set $goj mg.st 0
execute if score $goj mg.st matches 30.. run scoreboard players set $goj mg.st 29
scoreboard players operation $goj mg.st *= #30 mg.st
scoreboard players operation $goj mg.st += $goi mg.st
execute store result storage mg:gta mi.o int 1 run scoreboard players get $goj mg.st
function mg:gta/map_pick_o with storage mg:gta mi
function mg:gta/map_add_o with storage mg:gta mi
