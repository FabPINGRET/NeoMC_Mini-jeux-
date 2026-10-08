# @s (cacheur) : son objet le suit ; immobile 2 s → calé sur la grille
scoreboard players operation $pid mg.st = @s mg.pid
execute store result score @s mg.tx run data get entity @s Pos[0] 20
execute store result score @s mg.tz run data get entity @s Pos[2] 20
execute if score @s mg.tx = @s mg.phx if score @s mg.tz = @s mg.phz run scoreboard players add @s mg.phs 1
execute unless score @s mg.tx = @s mg.phx run scoreboard players set @s mg.phs 0
execute unless score @s mg.tz = @s mg.phz run scoreboard players set @s mg.phs 0
scoreboard players operation @s mg.phx = @s mg.tx
scoreboard players operation @s mg.phz = @s mg.tz
execute if score @s mg.phs matches ..39 as @e[tag=mg.phd] if score @s mg.pid = $pid mg.st run tp @s ~ ~ ~ 0 0
execute if score @s mg.phs matches ..39 as @e[tag=mg.phi] if score @s mg.pid = $pid mg.st run tp @s ~ ~-0.01 ~
execute if score @s mg.phs matches 40 align xyz positioned ~0.5 ~ ~0.5 as @e[tag=mg.phd] if score @s mg.pid = $pid mg.st run tp @s ~ ~ ~ 0 0
execute if score @s mg.phs matches 40 align xyz positioned ~0.5 ~ ~0.5 as @e[tag=mg.phi] if score @s mg.pid = $pid mg.st run tp @s ~ ~-0.01 ~
execute if score @s mg.phs matches 40 run title @s actionbar {"text":"🔒 Verrouillé sur la grille","color":"green"}
execute if score @s mg.phs matches 41.. run scoreboard players set @s mg.phs 41
