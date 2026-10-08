# Wagonnet en gare : le passager descend sur le quai
execute on passengers run tag @s add mg.csx
ride @a[tag=mg.csx,limit=1] dismount
tp @a[tag=mg.csx] -114.5 64 -3.5 -90 0
tag @a[tag=mg.csx] remove mg.csx
kill @s
