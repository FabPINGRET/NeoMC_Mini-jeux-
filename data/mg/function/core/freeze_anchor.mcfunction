# @s : point de gel = position actuelle (centièmes de bloc)
execute store result score @s mg.fx run data get entity @s Pos[0] 100
execute store result score @s mg.fy run data get entity @s Pos[1] 100
execute store result score @s mg.fz run data get entity @s Pos[2] 100
