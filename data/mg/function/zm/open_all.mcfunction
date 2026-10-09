# Infection : toutes les portes ouvertes, pas d'achats
fill -1 81 23189 1 83 23189 minecraft:air
fill 11 81 23199 11 83 23201 minecraft:air
fill 11 81 23177 11 83 23179 minecraft:air
fill 21 81 23189 23 83 23189 minecraft:air
kill @e[tag=mg.zbuy]
kill @e[type=minecraft:text_display,tag=mg.zent]
kill @e[type=minecraft:item_display,tag=mg.zent]
tag @e[tag=mg.zsp] add mg.zon
