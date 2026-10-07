scoreboard players operation $ktg mg.st = @s mg.kdd
tag @e[tag=mg.ktgt] remove mg.ktgt
execute as @e[type=minecraft:block_display,tag=mg.kart] if score @s mg.ri = $ktg mg.st run tag @s add mg.ktgt
execute facing entity @e[tag=mg.ktgt,limit=1] feet rotated ~ 0 run tp @s ~ ~ ~ ~ 0
tag @e[tag=mg.ktgt] remove mg.ktgt
