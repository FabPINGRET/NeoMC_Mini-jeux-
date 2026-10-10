# @s : une place libre sur le cercle de départ
execute unless entity @e[type=minecraft:marker,tag=mg.ats,tag=!mg.atu] run tag @e[tag=mg.ats] remove mg.atu
tag @e[type=minecraft:marker,tag=mg.ats,tag=!mg.atu,sort=random,limit=1] add mg.atq
tp @s @e[type=minecraft:marker,tag=mg.atq,limit=1]
execute at @s run spawnpoint @s ~ ~ ~
tag @e[tag=mg.atq] add mg.atu
tag @e[tag=mg.atq] remove mg.atq
