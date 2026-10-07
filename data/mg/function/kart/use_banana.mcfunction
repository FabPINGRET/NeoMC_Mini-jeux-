execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s rotated ~ 0 positioned ^ ^0.15 ^-2.4 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.kban","mg.kbnew","mg.fx"],item:{id:"minecraft:yellow_dye"},billboard:"center",transformation:{translation:[0f,0.3f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.3f,1.3f,1.3f]}}
scoreboard players set @e[type=minecraft:item_display,tag=mg.kbnew] mg.t 10
tag @e[tag=mg.kbnew] remove mg.kbnew
execute at @s run playsound minecraft:entity.item.pickup master @a[tag=mg.play,distance=..16] ~ ~ ~ 1 0.6
