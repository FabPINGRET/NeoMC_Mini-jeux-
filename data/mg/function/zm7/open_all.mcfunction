# Infection : toutes les portes ouvertes, pas d'achats
fill 9 81 40199 9 83 40201 minecraft:air
fill -9 81 40196 -9 83 40198 minecraft:air
fill 29 81 40199 29 83 40201 minecraft:air
fill 29 87 40199 29 89 40201 minecraft:air
fill -14 87 40215 -12 89 40215 minecraft:air
fill 38 87 40189 40 89 40189 minecraft:air
kill @e[tag=mg.zbuy]
kill @e[type=minecraft:text_display,tag=mg.zent]
kill @e[type=minecraft:item_display,tag=mg.zent]
kill @e[tag=mg.zwin]
summon minecraft:interaction 36.5 87 40194.5 {Tags:["mg.zent","mg.zlock"],width:1.1f,height:1.1f}
tag @e[tag=mg.zsp] add mg.zon
