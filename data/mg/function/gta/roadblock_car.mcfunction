# @s : voiture de barrage (immobile, en travers)
data merge entity @s {NoAI:1b}
tag @s add mg.grbc
execute at @s run tp @s ~ ~ ~ 90 0
