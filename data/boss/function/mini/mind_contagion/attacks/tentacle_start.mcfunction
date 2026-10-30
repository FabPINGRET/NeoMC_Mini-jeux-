summon armor_stand -11760 169 -196 {NoGravity:1b,Silent:1b,Invulnerable:1b,Tags:["mind_boss_tentacle_pivot_1","mind_boss_tentacle_face"],DisabledSlots:4144959,Rotation:[0F,90F]}
summon armor_stand -11760 169 -196 {NoGravity:1b,Silent:1b,Invulnerable:1b,Tags:["mind_boss_tentacle_pivot_2","mind_boss_tentacle_face"],DisabledSlots:4144959,Rotation:[0F,90F]}
summon armor_stand -11760 169 -196 {NoGravity:1b,Silent:1b,Invulnerable:1b,Tags:["mind_boss_tentacle_pivot_3","mind_boss_tentacle_face"],DisabledSlots:4144959,Rotation:[0F,90F]}

summon block_display -11760 170.4 -196 {NoGravity:1b,Silent:1b,Rotation:[0F,0F],Tags:["mind_boss_tentacle","1"],brightness:{sky:15,block:15},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2f,5f,2f]},block_state:{Name:"minecraft:sculk_sensor",Properties:{sculk_sensor_phase:"active"}}}
summon block_display -11760 170.4 -196 {NoGravity:1b,Silent:1b,Rotation:[0F,0F],Tags:["mind_boss_tentacle","2"],brightness:{sky:15,block:15},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2f,5f,2f]},block_state:{Name:"minecraft:sculk_sensor",Properties:{sculk_sensor_phase:"active"}}}

scoreboard players set mind_boss_tentacle_angle Value 900
particle dust_color_transition{from_color:[0.000,0.271,0.290],to_color:[0.000,0.933,1.000],scale:2} -11760 174 -196 1.5 1 1.5 0 200

setblock -11747 147 -177 redstone_block

execute if score mind_contagion_health Value matches 0..90 run setblock -11749 147 -177 minecraft:redstone_block
