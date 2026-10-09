# @s : point de gel = position actuelle (x/z en centièmes)
execute store result score @s mg.fx run data get entity @s Pos[0] 100
execute store result score @s mg.fz run data get entity @s Pos[2] 100
