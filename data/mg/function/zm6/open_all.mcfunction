# Infection : toutes les portes ouvertes, pas d'achats
fill 9 81 39799 9 83 39801 minecraft:air
fill 31 81 39799 31 83 39801 minecraft:air
fill -9 81 39799 -9 83 39801 minecraft:air
fill -9 87 39792 -9 89 39794 minecraft:air
fill -17 87 39792 -17 89 39794 minecraft:air
fill 9 87 39799 9 89 39801 minecraft:air
fill 31 87 39799 31 89 39801 minecraft:air
fill 19 81 39796 21 83 39796 minecraft:air
kill @e[tag=mg.zbuy]
kill @e[type=minecraft:text_display,tag=mg.zent]
kill @e[type=minecraft:item_display,tag=mg.zent]
kill @e[tag=mg.zwin]
summon minecraft:interaction 20.5 81 39786.5 {Tags:["mg.zent","mg.zlock"],width:1.1f,height:1.1f}
tag @e[tag=mg.zsp] add mg.zon
