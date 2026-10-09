# Wagonnet arrivé : le passager redescend au guichet
execute on passengers run tag @s add mg.csx
ride @a[tag=mg.csx,limit=1] dismount
tp @a[tag=mg.csx] -45.5 64 44.5 0 0
tag @a[tag=mg.csx] remove mg.csx
kill @s
