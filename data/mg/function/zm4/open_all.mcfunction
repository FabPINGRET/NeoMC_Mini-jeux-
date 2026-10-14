# Infection : toutes les portes ouvertes, pas d'achats
fill -1 81 39091 1 83 39091 minecraft:air
fill -9 81 39099 -9 83 39101 minecraft:air
fill 9 81 39099 9 83 39101 minecraft:air
fill -1 81 39069 1 83 39069 minecraft:air
fill -23 81 39087 -21 83 39087 minecraft:air
fill 23 81 39085 25 83 39085 minecraft:air
fill 15 81 39058 15 83 39060 minecraft:air
fill -13 81 39065 -13 83 39067 minecraft:air
kill @e[tag=mg.zbuy]
kill @e[type=minecraft:text_display,tag=mg.zent]
kill @e[type=minecraft:item_display,tag=mg.zent]
kill @e[tag=mg.zwin]
summon minecraft:interaction 1.5 81 39058.5 {Tags:["mg.zent","mg.zlock"],width:1.1f,height:1.1f}
tag @e[tag=mg.zsp] add mg.zon
