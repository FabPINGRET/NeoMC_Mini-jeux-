# @s : boule près des quilles → tests de contact avec les quilles debout de sa piste
scoreboard players operation #bx mg.st = @s mg.bx
scoreboard players operation #bz mg.st = @s mg.bz
scoreboard players operation #bvx mg.st = @s mg.bvx
scoreboard players operation #bvz mg.st = @s mg.bvz
execute as @e[type=minecraft:block_display,tag=mg.bpin,tag=!mg.bpdn] if score @s mg.bln = #ln mg.st run function mg:bowl/ball_test
scoreboard players operation @s mg.bvx = #bvx mg.st
scoreboard players operation @s mg.bvz = #bvz mg.st
