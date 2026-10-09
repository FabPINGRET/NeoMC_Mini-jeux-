# Infection : toutes les portes ouvertes, pas d'achats
fill -1 81 35789 1 83 35789 minecraft:air
fill 11 81 35799 11 83 35801 minecraft:air
fill 11 81 35777 11 83 35779 minecraft:air
fill 21 81 35789 23 83 35789 minecraft:air
kill @e[tag=mg.zbuy]
kill @e[type=minecraft:text_display,tag=mg.zent]
kill @e[type=minecraft:item_display,tag=mg.zent]
tag @e[tag=mg.zsp] add mg.zon
