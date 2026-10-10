# @s : une place libre sur la ligne de départ (toutes prises : on recommence)
execute unless entity @e[type=minecraft:marker,tag=mg.sqs,tag=!mg.squ] run tag @e[tag=mg.sqs] remove mg.squ
tag @e[type=minecraft:marker,tag=mg.sqs,tag=!mg.squ,sort=random,limit=1] add mg.sqp
tp @s @e[type=minecraft:marker,tag=mg.sqp,limit=1]
execute at @s run spawnpoint @s ~ ~ ~
tag @e[tag=mg.sqp] add mg.squ
tag @e[tag=mg.sqp] remove mg.sqp
