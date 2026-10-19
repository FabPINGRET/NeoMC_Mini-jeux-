# Portail d'Ombrelune au lobby (avenue est, côté nord), reconstruit s'il disparaît
kill @e[tag=mg.olport]
fill 36 64 -13 44 75 -8 minecraft:air
fill 36 63 -13 44 63 -8 minecraft:polished_deepslate
fill 37 63 -12 43 63 -9 minecraft:deepslate_tiles
fill 39 63 -8 41 63 -4 minecraft:stone_bricks
fill 39 64 -8 41 66 -4 minecraft:air
fill 38 64 -9 38 70 -9 minecraft:polished_blackstone_bricks
fill 42 64 -9 42 70 -9 minecraft:polished_blackstone_bricks
fill 37 64 -9 37 69 -9 minecraft:crying_obsidian
fill 43 64 -9 43 69 -9 minecraft:crying_obsidian
fill 37 71 -9 43 71 -9 minecraft:polished_blackstone_brick_slab
fill 39 70 -9 41 70 -9 minecraft:chiseled_polished_blackstone
setblock 40 72 -9 minecraft:amethyst_block
setblock 40 73 -9 minecraft:amethyst_cluster[facing=up]
setblock 37 70 -9 minecraft:soul_lantern
setblock 43 70 -9 minecraft:soul_lantern
setblock 40 63 -9 minecraft:chiseled_polished_blackstone
summon minecraft:text_display 40.5 75.4 -8.4 {Tags:["mg.olport"],text:{"text":"🌙 OMBRELUNE","color":"light_purple","bold":true},background:-1442840576,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.6f,2.6f,2.6f]}}
summon minecraft:text_display 40.5 74.95 -8.4 {Tags:["mg.olport"],text:{"text":"RPG médiéval-fantastique : 8 régions, dragons, donjons","color":"gray"},background:0,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.9f,0.9f,0.9f]}}
summon minecraft:text_display 40.5 64.4 -7.8 {Tags:["mg.olport"],text:{"text":"▶ entre dans le portail","color":"yellow"},background:0,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
function mg:ombre/spawn_clean
