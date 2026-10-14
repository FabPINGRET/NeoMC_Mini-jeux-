# Piège ici (propriétaire $own)
scoreboard players add $tvid mg.st 1
summon minecraft:marker ~ ~ ~ {Tags:["mg.tv","mg.tvtrap","mg.tvn"]}
summon minecraft:block_display ~ ~ ~ {Tags:["mg.tv","mg.tvtrapd","mg.tvn"],block_state:{Name:"minecraft:heavy_weighted_pressure_plate"},teleport_duration:2,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.45f,0f,-0.45f],scale:[0.9f,1.0f,0.9f]}}
summon minecraft:block_display ~ ~ ~ {Tags:["mg.tv","mg.tvtrapd","mg.tvn"],block_state:{Name:"minecraft:iron_bars"},teleport_duration:2,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.4f,0.02f,-0.38f],scale:[0.8f,0.22f,0.1f]}}
summon minecraft:block_display ~ ~ ~ {Tags:["mg.tv","mg.tvtrapd","mg.tvn"],block_state:{Name:"minecraft:iron_bars"},teleport_duration:2,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.4f,0.02f,0.28f],scale:[0.8f,0.22f,0.1f]}}
scoreboard players operation @e[tag=mg.tvn] mg.tvid = $tvid mg.st
scoreboard players operation @e[tag=mg.tvn] mg.tvo = $own mg.st
tag @e[tag=mg.tvn] remove mg.tvn
playsound minecraft:block.chain.place player @a ~ ~ ~ 0.8 0.8
