# @s vient de mourir : son arc tombe là où il est mort
data modify storage mg:mm d set value {x:0,y:0,z:0}
execute store result storage mg:mm d.x int 1 run data get entity @s LastDeathLocation.pos[0]
execute store result storage mg:mm d.y int 1 run data get entity @s LastDeathLocation.pos[1]
execute store result storage mg:mm d.z int 1 run data get entity @s LastDeathLocation.pos[2]
clear @s minecraft:bow
clear @s minecraft:arrow
function mg:mm/drop_at with storage mg:mm d
function mg:mm/bow_news
