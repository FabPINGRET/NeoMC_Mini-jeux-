# Infection : toutes les portes ouvertes, pas d'achats
fill -1 81 36089 1 83 36089 minecraft:air
fill 11 81 36099 11 83 36101 minecraft:air
fill 11 81 36077 11 83 36079 minecraft:air
fill 21 81 36089 23 83 36089 minecraft:air
kill @e[tag=mg.zbuy]
kill @e[type=minecraft:text_display,tag=mg.zent]
kill @e[type=minecraft:item_display,tag=mg.zent]
kill @e[tag=mg.zwin]
summon minecraft:interaction 22.5 81 36073.5 {Tags:["mg.zent","mg.zlock"],width:1.1f,height:1.1f}
tag @e[tag=mg.zsp] add mg.zon
