# Générateur de fer (2 s) — uniquement pour les îles occupées
scoreboard players set $gi mg.st 40
execute if entity @a[team=mg_red,tag=mg.play] run summon minecraft:item -27.5 64.5 1200.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:10s}
execute if entity @a[team=mg_blue,tag=mg.play] run summon minecraft:item 28.5 64.5 1200.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:10s}
execute if entity @a[team=mg_green,tag=mg.play] run summon minecraft:item 0.5 64.5 1172.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:10s}
execute if entity @a[team=mg_yellow,tag=mg.play] run summon minecraft:item 0.5 64.5 1228.5 {Item:{id:"minecraft:iron_ingot",count:1},PickupDelay:10s}
