# Kart 3D du pack : un seul modèle teinté à la couleur du pilote, monté sur le kart (le bloc devient invisible)
summon minecraft:item_display ~ ~ ~ {Tags:["mg.k3d","mg.k3dn","mg.kpart","mg.fx","mg.rps"],teleport_duration:2,item:{id:"minecraft:leather_horse_armor",components:{"minecraft:item_model":"mg:kart","minecraft:dyed_color":15022389}},transformation:{translation:[0f,0.425f,-0.133f],left_rotation:[0f,1f,0f,0f],right_rotation:[0f,0f,0f,1f],scale:[0.85f,0.85f,0.85f]}}
execute if data entity @s {block_state:{Name:"minecraft:red_concrete"}} run data modify entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] item.components."minecraft:dyed_color" set value 15022389
execute if data entity @s {block_state:{Name:"minecraft:blue_concrete"}} run data modify entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] item.components."minecraft:dyed_color" set value 2712319
execute if data entity @s {block_state:{Name:"minecraft:lime_concrete"}} run data modify entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] item.components."minecraft:dyed_color" set value 6610199
execute if data entity @s {block_state:{Name:"minecraft:yellow_concrete"}} run data modify entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] item.components."minecraft:dyed_color" set value 16766464
execute if data entity @s {block_state:{Name:"minecraft:purple_concrete"}} run data modify entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] item.components."minecraft:dyed_color" set value 9315498
execute if data entity @s {block_state:{Name:"minecraft:orange_concrete"}} run data modify entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] item.components."minecraft:dyed_color" set value 16739584
execute if data entity @s {block_state:{Name:"minecraft:cyan_concrete"}} run data modify entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] item.components."minecraft:dyed_color" set value 47316
execute if data entity @s {block_state:{Name:"minecraft:pink_concrete"}} run data modify entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] item.components."minecraft:dyed_color" set value 16728193
data modify entity @s block_state.Name set value "minecraft:air"
ride @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] mount @s
rotate @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] ~ 0
tag @e[tag=mg.k3dn] remove mg.k3dn
