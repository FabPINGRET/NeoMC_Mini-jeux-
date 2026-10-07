# Décor du spawn : rotation (mg.lspin) et flottement (mg.lbob), interpolés sur 2 s
scoreboard players add $lph mg.st 1
execute if score $lph mg.st matches 4.. run scoreboard players set $lph mg.st 0
execute as @e[type=minecraft:item_display,tag=mg.lby] run data merge entity @s {start_interpolation:0,interpolation_duration:40}
execute if score $lph mg.st matches 0 as @e[type=minecraft:item_display,tag=mg.lspin] run data modify entity @s transformation.left_rotation set value [0f,0.7071f,0f,0.7071f]
execute if score $lph mg.st matches 1 as @e[type=minecraft:item_display,tag=mg.lspin] run data modify entity @s transformation.left_rotation set value [0f,1f,0f,0f]
execute if score $lph mg.st matches 2 as @e[type=minecraft:item_display,tag=mg.lspin] run data modify entity @s transformation.left_rotation set value [0f,0.7071f,0f,-0.7071f]
execute if score $lph mg.st matches 3 as @e[type=minecraft:item_display,tag=mg.lspin] run data modify entity @s transformation.left_rotation set value [0f,0f,0f,1f]
execute if score $lph mg.st matches 0..3 as @e[type=minecraft:item_display,tag=mg.lbob] run data modify entity @s transformation.translation set value [0f,0f,0f]
execute if score $lph mg.st matches 0 as @e[type=minecraft:item_display,tag=mg.lbob] run data modify entity @s transformation.translation set value [0f,0.35f,0f]
execute if score $lph mg.st matches 2 as @e[type=minecraft:item_display,tag=mg.lbob] run data modify entity @s transformation.translation set value [0f,0.35f,0f]
