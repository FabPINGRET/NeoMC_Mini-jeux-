# Parkour du spawn (généré par tools/lobby/gen_lobby.py) : jardin suspendu puis la Tour céleste en spirale
kill @e[type=minecraft:marker,tag=mg.pkm]
kill @e[type=minecraft:text_display,tag=mg.pkd]
setblock 71 63 0 minecraft:moss_block strict
setblock 74 63 2 minecraft:oak_leaves[persistent=true] strict
setblock 77 64 1 minecraft:moss_block strict
setblock 80 64 -1 minecraft:flowering_azalea_leaves[persistent=true] strict
setblock 83 65 -2 minecraft:mossy_cobblestone strict
setblock 86 65 -1 minecraft:oak_log[axis=x] strict
setblock 89 66 1 minecraft:moss_block strict
setblock 92 66 2 minecraft:mossy_stone_bricks strict
setblock 98 67 0 minecraft:moss_block strict
fill 101 67 -1 103 67 1 minecraft:lapis_block strict
setblock 106 67 1 minecraft:snow_block strict
setblock 109 68 -1 minecraft:packed_ice strict
setblock 112 68 0 minecraft:packed_ice strict
setblock 113 68 3 minecraft:lantern[hanging=true] strict
setblock 113 69 3 minecraft:snow_block strict
setblock 114 69 6 minecraft:blue_ice strict
setblock 115 70 8 minecraft:packed_ice strict
setblock 120 70 11 minecraft:lantern[hanging=true] strict
setblock 117 71 10 minecraft:ice strict
setblock 120 71 11 minecraft:snow_block strict
setblock 123 72 12 minecraft:snow_block strict
setblock 126 73 12 minecraft:packed_ice strict
setblock 129 73 11 minecraft:snow_block strict
setblock 131 73 9 minecraft:lantern[hanging=true] strict
setblock 131 74 9 minecraft:blue_ice strict
setblock 133 75 7 minecraft:packed_ice strict
setblock 135 75 4 minecraft:ice strict
setblock 136 76 -2 minecraft:lantern[hanging=true] strict
setblock 136 76 1 minecraft:snow_block strict
fill 134 77 -6 136 77 -4 minecraft:lapis_block strict
setblock 136 77 -2 minecraft:snow_block strict
setblock 128 78 -11 minecraft:soul_lantern[hanging=true] strict
setblock 133 78 -7 minecraft:glowstone strict
setblock 128 79 -11 minecraft:red_nether_bricks strict
setblock 131 79 -9 minecraft:crimson_nylium strict
setblock 125 80 -12 minecraft:warped_nylium strict
setblock 117 81 -9 minecraft:soul_lantern[hanging=true] strict
setblock 122 81 -12 minecraft:shroomlight strict
setblock 117 82 -9 minecraft:blackstone strict
setblock 113 83 -4 minecraft:glowstone strict
setblock 115 83 -7 minecraft:crying_obsidian strict
setblock 112 84 -1 minecraft:crimson_nylium strict
setblock 112 84 2 minecraft:soul_lantern[hanging=true] strict
setblock 112 85 2 minecraft:red_nether_bricks strict
setblock 113 85 5 minecraft:warped_nylium strict
setblock 120 85 11 minecraft:lantern[hanging=true] strict
setblock 115 86 7 minecraft:shroomlight strict
fill 116 86 9 118 86 11 minecraft:lapis_block strict
setblock 120 86 11 minecraft:light_blue_stained_glass strict
setblock 123 87 12 minecraft:end_stone strict
setblock 126 88 11 minecraft:amethyst_block strict
setblock 129 88 10 minecraft:end_stone_bricks strict
setblock 131 88 8 minecraft:lantern[hanging=true] strict
setblock 131 89 8 minecraft:purpur_block strict
setblock 133 90 6 minecraft:white_stained_glass strict
setblock 134 90 3 minecraft:quartz_block strict
setblock 133 91 -3 minecraft:lantern[hanging=true] strict
setblock 134 91 0 minecraft:purpur_pillar strict
setblock 131 92 -6 minecraft:end_stone strict
setblock 133 92 -3 minecraft:light_blue_stained_glass strict
setblock 123 93 -8 minecraft:lantern[hanging=true] strict
setblock 129 93 -8 minecraft:amethyst_block strict
setblock 123 94 -8 minecraft:purpur_block strict
setblock 126 94 -9 minecraft:end_stone_bricks strict
setblock 95 66 1 minecraft:oak_fence
setblock 119 81 -11 minecraft:nether_brick_fence
setblock 123 93 -1 minecraft:iron_block
setblock 123 93 0 minecraft:iron_block
setblock 123 93 1 minecraft:iron_block
setblock 124 93 -1 minecraft:iron_block
setblock 124 93 0 minecraft:iron_block
setblock 124 93 1 minecraft:iron_block
setblock 125 93 -1 minecraft:iron_block
setblock 125 93 0 minecraft:iron_block
setblock 125 93 1 minecraft:iron_block
setblock 124 94 0 minecraft:beacon
setblock 124 95 0 minecraft:lime_stained_glass
summon minecraft:marker 67.5 64 0.5 {Tags:["mg.pkc","mg.pks","mg.pkm","mg.pkn"],Rotation:[-90.0f,0f]}
scoreboard players set @e[type=minecraft:marker,tag=mg.pkn,limit=1] mg.t 0
tag @e[type=minecraft:marker,tag=mg.pkn] remove mg.pkn
summon minecraft:marker 102.5 68 0.5 {Tags:["mg.pkc","mg.pkm","mg.pkn"],Rotation:[-76.0f,0f]}
scoreboard players set @e[type=minecraft:marker,tag=mg.pkn,limit=1] mg.t 1
tag @e[type=minecraft:marker,tag=mg.pkn] remove mg.pkn
summon minecraft:marker 135.5 78 -4.5 {Tags:["mg.pkc","mg.pkm","mg.pkn"],Rotation:[135.0f,0f]}
scoreboard players set @e[type=minecraft:marker,tag=mg.pkn,limit=1] mg.t 2
tag @e[type=minecraft:marker,tag=mg.pkn] remove mg.pkn
summon minecraft:marker 117.5 87 10.5 {Tags:["mg.pkc","mg.pkm","mg.pkn"],Rotation:[-71.6f,0f]}
scoreboard players set @e[type=minecraft:marker,tag=mg.pkn,limit=1] mg.t 3
tag @e[type=minecraft:marker,tag=mg.pkn] remove mg.pkn
summon minecraft:marker 124.5 96 0.5 {Tags:["mg.pkf","mg.pkm","mg.pkn"]}
scoreboard players set @e[type=minecraft:marker,tag=mg.pkn,limit=1] mg.t 4
tag @e[type=minecraft:marker,tag=mg.pkn] remove mg.pkn
summon minecraft:text_display 67.5 66.9 0.5 {Tags:["mg.pkd","mg.pkboard"],billboard:"center",text:[{"text":"3 checkpoints : grimpe au sommet de la Tour céleste !","color":"gray"}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1f,1f,1f]}}
summon minecraft:text_display 67.5 67.4 0.5 {Tags:["mg.pkd"],billboard:"center",text:[{"text":"Pose-toi sur l'émeraude pour démarrer le chrono","color":"green"}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
summon minecraft:text_display 102.5 69.6 0.5 {Tags:["mg.pkd"],billboard:"center",text:[{"text":"✔ Checkpoint 1/3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.2f,1.2f,1.2f]}}
summon minecraft:text_display 135.5 79.6 -4.5 {Tags:["mg.pkd"],billboard:"center",text:[{"text":"✔ Checkpoint 2/3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.2f,1.2f,1.2f]}}
summon minecraft:text_display 117.5 88.6 10.5 {Tags:["mg.pkd"],billboard:"center",text:[{"text":"✔ Checkpoint 3/3","color":"aqua","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.2f,1.2f,1.2f]}}
execute if score $pkrec mg.st matches 1.. run function mg:parkour/board_refresh
