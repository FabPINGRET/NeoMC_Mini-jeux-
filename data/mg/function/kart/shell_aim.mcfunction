scoreboard players operation $ktg mg.st = @s mg.kdd
execute as @a[tag=mg.play] if score @s mg.ri = $ktg mg.st run tag @s add mg.ktgt
execute facing entity @a[tag=mg.ktgt,limit=1] feet rotated ~ 0 run tp @s ~ ~ ~ ~ 0
tag @a remove mg.ktgt
