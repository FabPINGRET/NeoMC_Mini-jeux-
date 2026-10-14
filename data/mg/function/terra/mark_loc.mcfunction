# @s (entité) : sa position dans storage mg:terra h
execute store result storage mg:terra h.x int 1 run data get entity @s Pos[0]
execute store result storage mg:terra h.y int 1 run data get entity @s Pos[1]
execute store result storage mg:terra h.z int 1 run data get entity @s Pos[2]
