# Victime d'une flèche explosive (@s = victime) : le kill est crédité au tireur
execute if entity @a[tag=mg.osh] run return run damage @s 1000 minecraft:arrow by @a[tag=mg.osh,limit=1]
damage @s 1000 minecraft:arrow
