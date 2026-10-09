# @s : objets de sa mission retirés
scoreboard players operation $gb mg.st = @s mg.bid
tag @e remove mg.gmine
execute as @e[tag=mg.gmo] if score @s mg.bid = $gb mg.st run tag @s add mg.gmine
kill @e[tag=mg.gmine]
scoreboard players set @s mg.gmt 0
scoreboard players set @s mg.gms 0
