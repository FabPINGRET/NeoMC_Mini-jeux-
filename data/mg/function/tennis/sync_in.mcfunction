# @s : position réelle → coordonnées relatives au court (×1000)
execute store result score @s mg.tnx run data get entity @s Pos[0] 1000
scoreboard players operation @s mg.tnx -= $tncx mg.st
execute store result score @s mg.tny run data get entity @s Pos[1] 1000
execute store result score @s mg.tnz run data get entity @s Pos[2] 1000
scoreboard players remove @s mg.tnz 35400500
