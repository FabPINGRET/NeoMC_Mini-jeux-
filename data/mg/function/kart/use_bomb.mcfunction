execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s rotated ~ 0 positioned ^ ^1 ^1.8 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.kbomb","mg.knew","mg.fx"],teleport_duration:1,item:{id:"minecraft:black_concrete"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.6f,0.6f,0.6f]}}
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s rotated ~ 0 positioned ^ ^1 ^1.8 as @e[type=minecraft:item_display,tag=mg.knew] run tp @s ~ ~ ~ ~ 0
scoreboard players set @e[type=minecraft:item_display,tag=mg.knew] mg.t 60
scoreboard players set @e[type=minecraft:item_display,tag=mg.knew] mg.kvy 5
tag @e[type=minecraft:item_display,tag=mg.knew] remove mg.knew
execute at @s run playsound minecraft:entity.snowball.throw master @a[tag=mg.play,distance=..16] ~ ~ ~ 1 0.5
