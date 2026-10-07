scoreboard players set @s mg.kbill 100
scoreboard players set @s mg.kdr 0
execute at @e[type=minecraft:block_display,tag=mg.kk,limit=1] run summon minecraft:block_display ~ ~ ~ {Tags:["mg.kbillm","mg.kbilln","mg.kpart","mg.fx"],teleport_duration:2,block_state:{Name:"minecraft:coal_block"},transformation:{translation:[-0.75f,0.1f,-1.3f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.3f,2.6f]}}
ride @e[type=minecraft:block_display,tag=mg.kbilln,limit=1] mount @e[type=minecraft:block_display,tag=mg.kk,limit=1]
execute as @e[type=minecraft:block_display,tag=mg.kk,limit=1] at @s on passengers run rotate @s ~ 0
tag @e[tag=mg.kbilln] remove mg.kbilln
title @s actionbar [{"text":"🚀 BILL BALLE !","color":"dark_red","bold":true}]
execute at @s run playsound minecraft:entity.firework_rocket.large_blast master @a[tag=mg.play,distance=..30] ~ ~ ~ 1 0.6
