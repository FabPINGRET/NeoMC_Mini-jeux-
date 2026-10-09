# Portail de Neo GTA au lobby (avenue nord, côté est), reconstruit par mg:gta/lobby_tick s'il disparaît
kill @e[tag=mg.gtap]
fill 5 64 -37 13 73 -29 minecraft:air
fill 5 63 -37 13 63 -29 minecraft:grass_block
fill 5 64 -23 13 73 -15 minecraft:air
fill 5 63 -23 13 63 -15 minecraft:polished_blackstone_bricks
fill 6 63 -22 12 63 -16 minecraft:black_concrete
fill 5 63 -19 8 63 -19 minecraft:yellow_concrete
setblock 5 63 -23 minecraft:yellow_concrete
setblock 5 63 -15 minecraft:yellow_concrete
setblock 5 63 -23 minecraft:yellow_concrete
setblock 13 63 -23 minecraft:yellow_concrete
setblock 7 63 -23 minecraft:yellow_concrete
setblock 7 63 -15 minecraft:yellow_concrete
setblock 5 63 -21 minecraft:yellow_concrete
setblock 13 63 -21 minecraft:yellow_concrete
setblock 9 63 -23 minecraft:yellow_concrete
setblock 9 63 -15 minecraft:yellow_concrete
setblock 5 63 -19 minecraft:yellow_concrete
setblock 13 63 -19 minecraft:yellow_concrete
setblock 11 63 -23 minecraft:yellow_concrete
setblock 11 63 -15 minecraft:yellow_concrete
setblock 5 63 -17 minecraft:yellow_concrete
setblock 13 63 -17 minecraft:yellow_concrete
setblock 13 63 -23 minecraft:yellow_concrete
setblock 13 63 -15 minecraft:yellow_concrete
setblock 5 63 -15 minecraft:yellow_concrete
setblock 13 63 -15 minecraft:yellow_concrete
fill 9 64 -21 9 69 -21 minecraft:black_concrete
fill 9 64 -17 9 69 -17 minecraft:black_concrete
fill 9 70 -21 9 70 -17 minecraft:black_concrete
fill 9 64 -22 9 70 -22 minecraft:yellow_concrete
fill 9 64 -16 9 70 -16 minecraft:yellow_concrete
fill 9 71 -22 9 71 -16 minecraft:yellow_concrete
setblock 9 72 -22 minecraft:redstone_lamp[lit=true]
setblock 9 72 -16 minecraft:redstone_lamp[lit=true]
setblock 8 71 -22 minecraft:end_rod[facing=west]
setblock 8 71 -16 minecraft:end_rod[facing=west]
setblock 9 63 -19 minecraft:chiseled_polished_blackstone
fill 4 64 -20 8 66 -18 minecraft:air
fill 4 63 -20 4 63 -18 minecraft:stone_bricks
setblock 6 64 -23 minecraft:iron_bars
setblock 6 65 -23 minecraft:iron_bars
setblock 6 66 -23 minecraft:lantern
setblock 6 64 -15 minecraft:iron_bars
setblock 6 65 -15 minecraft:iron_bars
setblock 6 66 -15 minecraft:lantern
summon minecraft:text_display 8.4 72.6 -18.5 {Tags:["mg.gtap"],Rotation:[90f,0f],text:{"text":"🚓 NEO GTA","color":"gold","bold":true},background:-1442840576,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.6f,2.6f,2.6f]}}
summon minecraft:text_display 8.4 72.15 -18.5 {Tags:["mg.gtap"],Rotation:[90f,0f],text:{"text":"Monde GTA libre : armes, voitures, hélicos, police","color":"gray"},background:0,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.9f,0.9f,0.9f]}}
summon minecraft:text_display 8.4 64.4 -18.5 {Tags:["mg.gtap"],Rotation:[90f,0f],text:{"text":"▶ entre dans le portail","color":"yellow"},background:0,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:block_display 11.5 64 -18.5 {Tags:["mg.gtap"],block_state:{Name:"minecraft:yellow_concrete"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.95f,0.05f,-1.7f],scale:[1.9f,0.75f,3.4f]}}
summon minecraft:block_display 11.5 64 -18.5 {Tags:["mg.gtap"],block_state:{Name:"minecraft:black_concrete"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.8f,0.8f,-0.9f],scale:[1.6f,0.65f,1.7f]}}
summon minecraft:block_display 11.5 64 -18.5 {Tags:["mg.gtap"],block_state:{Name:"minecraft:yellow_concrete"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.3f,1.45f,-0.3f],scale:[0.6f,0.2f,0.6f]}}
summon minecraft:block_display 11.5 64 -18.5 {Tags:["mg.gtap"],block_state:{Name:"minecraft:black_concrete"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-1.0f,0.0f,-1.25f],scale:[0.25f,0.45f,0.6f]}}
summon minecraft:block_display 11.5 64 -18.5 {Tags:["mg.gtap"],block_state:{Name:"minecraft:black_concrete"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0.75f,0.0f,-1.25f],scale:[0.25f,0.45f,0.6f]}}
summon minecraft:block_display 11.5 64 -18.5 {Tags:["mg.gtap"],block_state:{Name:"minecraft:black_concrete"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-1.0f,0.0f,0.85f],scale:[0.25f,0.45f,0.6f]}}
summon minecraft:block_display 11.5 64 -18.5 {Tags:["mg.gtap"],block_state:{Name:"minecraft:black_concrete"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0.75f,0.0f,0.85f],scale:[0.25f,0.45f,0.6f]}}
