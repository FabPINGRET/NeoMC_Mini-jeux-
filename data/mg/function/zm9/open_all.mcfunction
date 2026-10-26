# Infection : toutes les portes ouvertes, pas d'achats
fill -7 82 42515 -7 84 42517 minecraft:air
fill -15 84 42503 -13 86 42503 minecraft:air
fill -7 84 42484 -7 86 42486 minecraft:air
fill 7 83 42484 7 85 42486 minecraft:air
fill 13 83 42503 15 85 42503 minecraft:air
fill 7 82 42515 7 84 42517 minecraft:air
fill -1 81 42511 1 83 42511 minecraft:air
fill -1 81 42489 1 83 42489 minecraft:air
kill @e[tag=mg.zbuy]
kill @e[type=minecraft:text_display,tag=mg.zent]
kill @e[type=minecraft:item_display,tag=mg.zent]
kill @e[tag=mg.zwin]
summon minecraft:interaction -13.5 84 42485.5 {Tags:["mg.zent","mg.zlock"],width:1.1f,height:1.1f}
tag @e[tag=mg.zsp] add mg.zon
