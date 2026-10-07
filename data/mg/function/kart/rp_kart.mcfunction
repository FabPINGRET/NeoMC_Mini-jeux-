# Kart 3D du pack : modèle du type choisi (mg.kty), teinté à la couleur choisie (mg.kcol), monté sur le kart (bloc invisible)
summon minecraft:item_display ~ ~ ~ {Tags:["mg.k3d","mg.k3dn","mg.kpart","mg.fx","mg.rps"],teleport_duration:2,item:{id:"minecraft:leather_horse_armor",components:{"minecraft:item_model":"mg:kart","minecraft:dyed_color":15022389}},transformation:{translation:[0f,0.425f,-0.133f],left_rotation:[0f,1f,0f,0f],right_rotation:[0f,0f,0f,1f],scale:[0.85f,0.85f,0.85f]}}
execute if score @s mg.kty matches 2 run data modify entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] item.components."minecraft:item_model" set value "mg:kart_bolide"
execute if score @s mg.kty matches 2 run data merge entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] {transformation:{translation:[0.0f,0.425f,-0.133f],left_rotation:[0f,1f,0f,0f],right_rotation:[0f,0f,0f,1f],scale:[0.85f,0.85f,0.85f]}}
execute if score @s mg.kty matches 3 run data modify entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] item.components."minecraft:item_model" set value "mg:kart_mini"
execute if score @s mg.kty matches 3 run data merge entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] {transformation:{translation:[0.0f,0.357f,-0.112f],left_rotation:[0f,1f,0f,0f],right_rotation:[0f,0f,0f,1f],scale:[0.714f,0.714f,0.714f]}}
execute if score @s mg.kty matches 4 run data modify entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] item.components."minecraft:item_model" set value "mg:kart_costaud"
execute if score @s mg.kty matches 4 run data merge entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] {transformation:{translation:[0.0f,0.476f,-0.149f],left_rotation:[0f,1f,0f,0f],right_rotation:[0f,0f,0f,1f],scale:[0.952f,0.952f,0.952f]}}
execute if score @s mg.kcol matches 1 run data modify entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] item.components."minecraft:dyed_color" set value 15022389
execute if score @s mg.kcol matches 2 run data modify entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] item.components."minecraft:dyed_color" set value 2712319
execute if score @s mg.kcol matches 3 run data modify entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] item.components."minecraft:dyed_color" set value 6610199
execute if score @s mg.kcol matches 4 run data modify entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] item.components."minecraft:dyed_color" set value 16766464
execute if score @s mg.kcol matches 5 run data modify entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] item.components."minecraft:dyed_color" set value 9315498
execute if score @s mg.kcol matches 6 run data modify entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] item.components."minecraft:dyed_color" set value 16739584
execute if score @s mg.kcol matches 7 run data modify entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] item.components."minecraft:dyed_color" set value 47316
execute if score @s mg.kcol matches 8 run data modify entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] item.components."minecraft:dyed_color" set value 16728193
data modify entity @s block_state.Name set value "minecraft:air"
ride @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] mount @s
rotate @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] ~ 0
tag @e[tag=mg.k3dn] remove mg.k3dn
