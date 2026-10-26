# Infection : toutes les portes ouvertes, pas d'achats
fill -8 83 42118 -8 85 42120 minecraft:air
fill -16 83 42111 -14 85 42111 minecraft:air
fill -16 84 42089 -14 86 42089 minecraft:air
fill -8 84 42078 -8 86 42080 minecraft:air
fill 8 83 42078 8 85 42080 minecraft:air
fill 14 83 42089 16 85 42089 minecraft:air
fill 14 84 42111 16 86 42111 minecraft:air
fill 8 84 42118 8 86 42120 minecraft:air
fill -1 81 42113 1 83 42113 minecraft:air
fill -1 81 42085 1 83 42085 minecraft:air
kill @e[tag=mg.zbuy]
kill @e[type=minecraft:text_display,tag=mg.zent]
kill @e[type=minecraft:item_display,tag=mg.zent]
kill @e[tag=mg.zwin]
summon minecraft:interaction 0.5 81 42079.5 {Tags:["mg.zent","mg.zlock"],width:1.1f,height:1.1f}
tag @e[tag=mg.zsp] add mg.zon
