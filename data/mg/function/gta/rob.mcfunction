# @s (accroupi, arme en main) : banque, sinon commerce, sinon passant visé (6 blocs)
execute if entity @e[type=minecraft:marker,tag=mg.gbank,distance=..3.5,scores={mg.gpc=..0}] run return run function mg:gta/rob_bank
execute if entity @e[type=minecraft:marker,tag=mg.gshop,distance=..2.6,scores={mg.gpc=..0}] run return run function mg:gta/rob_shop
tag @e[tag=mg.grt] remove mg.grt
scoreboard players set $gar mg.st 7
tag @s add mg.gaim
execute anchored eyes positioned ^ ^ ^1 run function mg:gta/rob_ray
tag @s remove mg.gaim
execute if entity @e[tag=mg.grt] run return run function mg:gta/rob_ped
function mg:gta/rob_stop
