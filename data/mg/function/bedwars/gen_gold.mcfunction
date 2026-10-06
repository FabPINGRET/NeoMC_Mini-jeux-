# Générateur d'or (8 s)
scoreboard players set $gg mg.st 160
execute if entity @a[team=mg_red,tag=mg.play] run summon minecraft:item -27.5 64.5 1200.5 {Item:{id:"minecraft:gold_ingot",count:1},PickupDelay:10s}
execute if entity @a[team=mg_blue,tag=mg.play] run summon minecraft:item 28.5 64.5 1200.5 {Item:{id:"minecraft:gold_ingot",count:1},PickupDelay:10s}
execute if entity @a[team=mg_green,tag=mg.play] run summon minecraft:item 0.5 64.5 1172.5 {Item:{id:"minecraft:gold_ingot",count:1},PickupDelay:10s}
execute if entity @a[team=mg_yellow,tag=mg.play] run summon minecraft:item 0.5 64.5 1228.5 {Item:{id:"minecraft:gold_ingot",count:1},PickupDelay:10s}
