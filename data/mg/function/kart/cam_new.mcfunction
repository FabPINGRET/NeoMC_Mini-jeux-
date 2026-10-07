# Caméra de poursuite de @s + sa tête posée sur le siège du kart
execute at @e[type=minecraft:block_display,tag=mg.kk,limit=1] run summon minecraft:item_display ~ ~2 ~ {Tags:["mg.kcam","mg.kcamc","mg.fx"],teleport_duration:2}
scoreboard players operation @e[type=minecraft:item_display,tag=mg.kcamc] mg.ri = @s mg.ri
execute at @e[type=minecraft:block_display,tag=mg.kk,limit=1] run summon minecraft:item_display ~ ~ ~ {Tags:["mg.khead","mg.kheadn","mg.kpart","mg.fx"],teleport_duration:1,transformation:{translation:[0f,0.62f,-0.1f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.75f,0.75f,0.75f]}}
loot replace entity @e[type=minecraft:item_display,tag=mg.kheadn,limit=1] contents loot mg:plot_head
scoreboard players operation @e[type=minecraft:item_display,tag=mg.kheadn] mg.ri = @s mg.ri
ride @e[type=minecraft:item_display,tag=mg.kheadn,limit=1] mount @e[type=minecraft:block_display,tag=mg.kk,limit=1]
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s on passengers run rotate @s ~ 0
tag @e[tag=mg.kheadn] remove mg.kheadn
