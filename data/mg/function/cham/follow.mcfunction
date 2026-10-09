# @s (caméléon) : son corps le suit ; immobile 2 s → calé (angle droit, grille en pose « bloc »)
scoreboard players operation $cmid mg.st = @s mg.cmid
execute store result score $cmx mg.st run data get entity @s Pos[0] 20
execute store result score $cmz mg.st run data get entity @s Pos[2] 20
execute store result score $cmy mg.st run data get entity @s Pos[1] 20
execute if score $cmx mg.st = @s mg.cmlx if score $cmz mg.st = @s mg.cmlz if score $cmy mg.st = @s mg.cmly run scoreboard players add @s mg.cmst 1
execute unless score $cmx mg.st = @s mg.cmlx run scoreboard players set @s mg.cmst 0
execute unless score $cmz mg.st = @s mg.cmlz run scoreboard players set @s mg.cmst 0
execute unless score $cmy mg.st = @s mg.cmly run scoreboard players set @s mg.cmst 0
scoreboard players operation @s mg.cmlx = $cmx mg.st
scoreboard players operation @s mg.cmlz = $cmz mg.st
scoreboard players operation @s mg.cmly = $cmy mg.st
execute if score @s mg.cmst matches ..39 as @e[type=minecraft:block_display,tag=mg.cmd] if score @s mg.cmid = $cmid mg.st run tp @s ~ ~ ~ ~ 0
execute if score @s mg.cmst matches ..39 as @e[type=minecraft:interaction,tag=mg.cmi] if score @s mg.cmid = $cmid mg.st run tp @s ~ ~ ~
execute if score @s mg.cmst matches 40 run function mg:cham/snap
execute if score @s mg.cmst matches 41.. run scoreboard players set @s mg.cmst 41
