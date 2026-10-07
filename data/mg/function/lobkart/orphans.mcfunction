# Karts du spawn dont le pilote est parti (déconnexion) : rangés
tag @e[type=minecraft:block_display,tag=mg.lkart] add mg.lko
execute as @e[type=minecraft:item_display,tag=mg.kcam] if score @s mg.ri matches 100.. run tag @s add mg.lko
execute as @a[tag=mg.lk] run function mg:lobkart/claim
execute as @e[type=minecraft:block_display,tag=mg.lko] on passengers run kill @s
kill @e[tag=mg.lko]
