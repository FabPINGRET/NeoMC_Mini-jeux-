# @s : position au début du délai (après la petite grâce)
execute store result score @s mg.msx run data get entity @s Pos[0] 100
execute store result score @s mg.msz run data get entity @s Pos[2] 100
