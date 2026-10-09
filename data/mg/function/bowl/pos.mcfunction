# @s (boule ou quille) : position du monde = repère de la piste (×1000)
scoreboard players operation #w mg.st = @s mg.bcx
scoreboard players operation #w mg.st += @s mg.bx
execute store result entity @s Pos[0] double 0.001 run scoreboard players get #w mg.st
scoreboard players set #w mg.st 35160000
scoreboard players operation #w mg.st += @s mg.bz
execute store result entity @s Pos[2] double 0.001 run scoreboard players get #w mg.st
