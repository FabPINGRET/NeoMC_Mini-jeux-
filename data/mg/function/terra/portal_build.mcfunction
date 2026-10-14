# Portail de Terra Nova au lobby (avenue nord, côté ouest, en face de Neo GTA), reconstruit par mg:terra/lobby_tick s'il disparaît
kill @e[tag=mg.tvport]
fill -13 64 -23 -5 73 -15 minecraft:air
fill -13 63 -23 -5 63 -15 minecraft:mossy_stone_bricks
fill -12 63 -22 -6 63 -16 minecraft:moss_block
fill -8 63 -19 -5 63 -19 minecraft:coarse_dirt
fill -9 64 -21 -9 69 -21 minecraft:jungle_log
fill -9 64 -17 -9 69 -17 minecraft:jungle_log
fill -9 70 -21 -9 70 -17 minecraft:stripped_jungle_log[axis=z]
fill -9 64 -22 -9 70 -22 minecraft:mossy_cobblestone
fill -9 64 -16 -9 70 -16 minecraft:mossy_cobblestone
fill -9 71 -22 -9 71 -16 minecraft:moss_block
fill -10 72 -22 -8 72 -16 minecraft:jungle_leaves[persistent=true]
setblock -9 73 -19 minecraft:jungle_leaves[persistent=true]
setblock -9 63 -19 minecraft:chiseled_tuff_bricks
fill -4 64 -20 -8 66 -18 minecraft:air
fill -4 63 -20 -4 63 -18 minecraft:stone_bricks
setblock -6 64 -23 minecraft:bamboo_fence
setblock -6 65 -23 minecraft:bamboo_fence
setblock -6 66 -23 minecraft:lantern
setblock -6 64 -15 minecraft:bamboo_fence
setblock -6 65 -15 minecraft:bamboo_fence
setblock -6 66 -15 minecraft:lantern
setblock -11 64 -22 minecraft:large_fern[half=lower]
setblock -11 65 -22 minecraft:large_fern[half=upper]
setblock -11 64 -16 minecraft:large_fern[half=lower]
setblock -11 65 -16 minecraft:large_fern[half=upper]
setblock -8 65 -22 minecraft:vine[west=true]
setblock -8 65 -16 minecraft:vine[west=true]
setblock -8 66 -22 minecraft:vine[west=true]
setblock -8 66 -16 minecraft:vine[west=true]
setblock -8 67 -22 minecraft:vine[west=true]
setblock -8 67 -16 minecraft:vine[west=true]
setblock -8 68 -22 minecraft:vine[west=true]
setblock -8 68 -16 minecraft:vine[west=true]
setblock -8 69 -22 minecraft:vine[west=true]
setblock -8 69 -16 minecraft:vine[west=true]
setblock -8 70 -22 minecraft:vine[west=true]
setblock -8 70 -16 minecraft:vine[west=true]
summon minecraft:text_display -8.4 72.6 -18.5 {Tags:["mg.tvport"],Rotation:[-90f,0f],text:{"text":"🦖 TERRA NOVA","color":"green","bold":true},background:-1442840576,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.6f,2.6f,2.6f]}}
summon minecraft:text_display -8.4 72.15 -18.5 {Tags:["mg.tvport"],Rotation:[-90f,0f],text:{"text":"Colonie préhistorique : missions, jungle, dinosaures","color":"gray"},background:0,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.9f,0.9f,0.9f]}}
summon minecraft:text_display -8.4 64.4 -18.5 {Tags:["mg.tvport"],Rotation:[-90f,0f],text:{"text":"▶ entre dans le portail","color":"yellow"},background:0,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:block_display -11.3 64 -18.5 {Tags:["mg.tvport"],block_state:{Name:"minecraft:green_terracotta"},teleport_duration:2,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.28f,0.75f,-0.55f],scale:[0.56f,0.5f,1.05f]},Rotation:[-60f,0f]}
summon minecraft:block_display -11.3 64 -18.5 {Tags:["mg.tvport"],block_state:{Name:"minecraft:green_terracotta"},teleport_duration:2,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.14f,1.05f,0.35f],scale:[0.28f,0.45f,0.3f]},Rotation:[-60f,0f]}
summon minecraft:block_display -11.3 64 -18.5 {Tags:["mg.tvport"],block_state:{Name:"minecraft:green_terracotta"},teleport_duration:2,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.2f,1.38f,0.4f],scale:[0.4f,0.32f,0.6f]},Rotation:[-60f,0f]}
summon minecraft:block_display -11.3 64 -18.5 {Tags:["mg.tvport"],block_state:{Name:"minecraft:lime_terracotta"},teleport_duration:2,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.15f,1.3f,0.98f],scale:[0.3f,0.16f,0.2f]},Rotation:[-60f,0f]}
summon minecraft:block_display -11.3 64 -18.5 {Tags:["mg.tvport"],block_state:{Name:"minecraft:yellow_concrete"},teleport_duration:2,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.21f,1.55f,0.74f],scale:[0.42f,0.06f,0.08f]},Rotation:[-60f,0f]}
summon minecraft:block_display -11.3 64 -18.5 {Tags:["mg.tvport"],block_state:{Name:"minecraft:white_concrete"},teleport_duration:2,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.13f,1.28f,1.0f],scale:[0.26f,0.04f,0.16f]},Rotation:[-60f,0f]}
summon minecraft:block_display -11.3 64 -18.5 {Tags:["mg.tvport"],block_state:{Name:"minecraft:green_terracotta"},teleport_duration:2,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.12f,0.88f,-1.45f],scale:[0.24f,0.24f,0.92f]},Rotation:[-60f,0f]}
summon minecraft:block_display -11.3 64 -18.5 {Tags:["mg.tvport"],block_state:{Name:"minecraft:black_terracotta"},teleport_duration:2,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.07f,0.92f,-1.85f],scale:[0.14f,0.14f,0.42f]},Rotation:[-60f,0f]}
summon minecraft:block_display -11.3 64 -18.5 {Tags:["mg.tvport"],block_state:{Name:"minecraft:black_terracotta"},teleport_duration:2,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.29f,1.0f,-0.3f],scale:[0.58f,0.1f,0.12f]},Rotation:[-60f,0f]}
summon minecraft:block_display -11.3 64 -18.5 {Tags:["mg.tvport"],block_state:{Name:"minecraft:black_terracotta"},teleport_duration:2,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.29f,1.0f,0.1f],scale:[0.58f,0.1f,0.12f]},Rotation:[-60f,0f]}
summon minecraft:block_display -11.3 64 -18.5 {Tags:["mg.tvport"],block_state:{Name:"minecraft:brown_terracotta"},teleport_duration:2,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.26f,0.0f,-0.15f],scale:[0.13f,0.78f,0.2f]},Rotation:[-60f,0f]}
summon minecraft:block_display -11.3 64 -18.5 {Tags:["mg.tvport"],block_state:{Name:"minecraft:brown_terracotta"},teleport_duration:2,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0.13f,0.0f,-0.15f],scale:[0.13f,0.78f,0.2f]},Rotation:[-60f,0f]}
summon minecraft:block_display -11.3 64 -18.5 {Tags:["mg.tvport"],block_state:{Name:"minecraft:brown_terracotta"},teleport_duration:2,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.24f,0.85f,0.42f],scale:[0.08f,0.25f,0.08f]},Rotation:[-60f,0f]}
summon minecraft:block_display -11.3 64 -18.5 {Tags:["mg.tvport"],block_state:{Name:"minecraft:brown_terracotta"},teleport_duration:2,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0.16f,0.85f,0.42f],scale:[0.08f,0.25f,0.08f]},Rotation:[-60f,0f]}
function mg:terra/spawn_clean
