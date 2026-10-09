# Case de l'objectif de la mission (@e[tag=mg.gmine])
execute store result score $gti mg.st run data get entity @e[tag=mg.gmine,limit=1] Pos[0]
execute store result score $gtj mg.st run data get entity @e[tag=mg.gmine,limit=1] Pos[2]
scoreboard players add $gti mg.st 88
scoreboard players remove $gtj mg.st 32312
scoreboard players operation $gti mg.st *= #30 mg.st
scoreboard players operation $gti mg.st /= #177 mg.st
scoreboard players operation $gtj mg.st *= #30 mg.st
scoreboard players operation $gtj mg.st /= #177 mg.st
execute if score $gti mg.st matches ..-1 run scoreboard players set $gti mg.st 0
execute if score $gti mg.st matches 30.. run scoreboard players set $gti mg.st 29
execute if score $gtj mg.st matches ..-1 run scoreboard players set $gtj mg.st 0
execute if score $gtj mg.st matches 30.. run scoreboard players set $gtj mg.st 29
scoreboard players operation $gtj mg.st *= #30 mg.st
scoreboard players operation $gtj mg.st += $gti mg.st
execute store result storage mg:gta mi.t int 1 run scoreboard players get $gtj mg.st
function mg:gta/map_pick_t with storage mg:gta mi
