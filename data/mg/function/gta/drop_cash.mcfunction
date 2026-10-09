# @s vient de mourir : les dollars perdus ($gl) tombent en liasse là où il est mort
data modify storage mg:gta d set value {x:0,y:0,z:0}
execute store result storage mg:gta d.x int 1 run data get entity @s LastDeathLocation.pos[0]
execute store result storage mg:gta d.y int 1 run data get entity @s LastDeathLocation.pos[1]
execute store result storage mg:gta d.z int 1 run data get entity @s LastDeathLocation.pos[2]
scoreboard players operation $gcv mg.st = $gl mg.st
function mg:gta/drop_cash_at with storage mg:gta d
