# Infection : toutes les portes ouvertes, pas d'achats
fill -8 81 39399 -8 83 39401 minecraft:air
fill 8 81 39399 8 83 39401 minecraft:air
fill -26 81 39399 -26 83 39401 minecraft:air
fill 26 81 39399 26 83 39401 minecraft:air
fill -37 81 39387 -35 83 39387 minecraft:air
fill 35 81 39387 37 83 39387 minecraft:air
fill -1 81 39408 1 83 39408 minecraft:air
kill @e[tag=mg.zbuy]
kill @e[type=minecraft:text_display,tag=mg.zent]
kill @e[type=minecraft:item_display,tag=mg.zent]
kill @e[tag=mg.zwin]
summon minecraft:interaction 0.5 81 39378.5 {Tags:["mg.zent","mg.zlock"],width:1.1f,height:1.1f}
tag @e[tag=mg.zsp] add mg.zon
