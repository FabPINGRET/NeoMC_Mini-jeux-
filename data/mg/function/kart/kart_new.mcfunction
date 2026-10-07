# Nouveau kart pour @s, à sa position et dans sa direction
tag @s add mg.kself
summon minecraft:block_display ~ ~ ~ {Tags:["mg.ib","mg.kart","mg.mine"],teleport_duration:2,block_state:{Name:"minecraft:red_concrete"},transformation:{translation:[-0.45f,0.09f,-0.712f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.285f,1.425f]},Passengers:[{id:"minecraft:block_display",Tags:["mg.kpart","mg.fx","mg.kp1"],teleport_duration:2,block_state:{Name:"minecraft:black_concrete"},transformation:{translation:[-0.585f,0.0f,0.338f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.17f,0.315f,0.315f]}},{id:"minecraft:block_display",Tags:["mg.kpart","mg.fx","mg.kp2"],teleport_duration:2,block_state:{Name:"minecraft:black_concrete"},transformation:{translation:[-0.585f,0.0f,-0.637f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.17f,0.315f,0.315f]}},{id:"minecraft:block_display",Tags:["mg.kpart","mg.fx","mg.kp3"],teleport_duration:2,block_state:{Name:"minecraft:gray_concrete"},transformation:{translation:[-0.3f,0.375f,-0.562f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.6f,0.375f,0.15f]}},{id:"minecraft:block_display",Tags:["mg.kpart","mg.fx","mg.kp4"],teleport_duration:2,block_state:{Name:"minecraft:light_gray_concrete"},transformation:{translation:[-0.06f,0.375f,0.338f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.12f,0.262f,0.12f]}}]}
execute as @e[type=minecraft:block_display,tag=mg.mine] at @s rotated as @a[tag=mg.kself,limit=1] run tp @s ~ ~ ~ ~ 0
execute as @e[type=minecraft:block_display,tag=mg.mine] at @s on passengers run rotate @s ~ 0
scoreboard players operation @e[type=minecraft:block_display,tag=mg.mine] mg.ri = @s mg.ri
scoreboard players operation $kc mg.st = @s mg.ri
scoreboard players operation $kc mg.st %= #k8 mg.st
execute if score $kc mg.st matches 0 run data modify entity @e[type=minecraft:block_display,tag=mg.mine,limit=1] block_state.Name set value "minecraft:red_concrete"
execute if score $kc mg.st matches 1 run data modify entity @e[type=minecraft:block_display,tag=mg.mine,limit=1] block_state.Name set value "minecraft:blue_concrete"
execute if score $kc mg.st matches 2 run data modify entity @e[type=minecraft:block_display,tag=mg.mine,limit=1] block_state.Name set value "minecraft:lime_concrete"
execute if score $kc mg.st matches 3 run data modify entity @e[type=minecraft:block_display,tag=mg.mine,limit=1] block_state.Name set value "minecraft:yellow_concrete"
execute if score $kc mg.st matches 4 run data modify entity @e[type=minecraft:block_display,tag=mg.mine,limit=1] block_state.Name set value "minecraft:purple_concrete"
execute if score $kc mg.st matches 5 run data modify entity @e[type=minecraft:block_display,tag=mg.mine,limit=1] block_state.Name set value "minecraft:orange_concrete"
execute if score $kc mg.st matches 6 run data modify entity @e[type=minecraft:block_display,tag=mg.mine,limit=1] block_state.Name set value "minecraft:cyan_concrete"
execute if score $kc mg.st matches 7 run data modify entity @e[type=minecraft:block_display,tag=mg.mine,limit=1] block_state.Name set value "minecraft:pink_concrete"
tag @e[tag=mg.mine] remove mg.mine
tag @s remove mg.kself
scoreboard players set @s mg.kdr 0
scoreboard players set @s mg.krc 0
