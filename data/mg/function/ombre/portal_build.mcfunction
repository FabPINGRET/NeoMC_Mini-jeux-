# Portail d'Ombrelune au lobby (avenue nord, côté ouest, au nord de Terra Nova), reconstruit s'il disparaît
kill @e[tag=mg.olport]
execute unless data storage mg:lobby olsite if block 40 63 -9 minecraft:chiseled_polished_blackstone run function mg:ombre/old_site
fill -18 64 -33 -5 80 -25 minecraft:air
fill -13 63 -33 -5 63 -25 minecraft:polished_deepslate
fill -12 63 -32 -6 63 -26 minecraft:deepslate_tiles
fill -8 63 -29 -5 63 -29 minecraft:polished_blackstone_bricks
fill -9 64 -31 -9 70 -31 minecraft:polished_blackstone_bricks
fill -9 64 -27 -9 70 -27 minecraft:polished_blackstone_bricks
fill -9 64 -32 -9 69 -32 minecraft:crying_obsidian
fill -9 64 -26 -9 69 -26 minecraft:crying_obsidian
fill -9 71 -32 -9 71 -26 minecraft:polished_blackstone_brick_slab
fill -9 70 -30 -9 70 -28 minecraft:chiseled_polished_blackstone
setblock -9 72 -29 minecraft:amethyst_block
setblock -9 73 -29 minecraft:amethyst_cluster[facing=up]
setblock -9 70 -32 minecraft:soul_lantern
setblock -9 70 -26 minecraft:soul_lantern
setblock -9 63 -29 minecraft:chiseled_polished_blackstone
fill -4 64 -30 -8 66 -28 minecraft:air
fill -4 63 -30 -4 63 -28 minecraft:stone_bricks
fill -6 64 -33 -6 65 -33 minecraft:polished_blackstone_wall
setblock -6 66 -33 minecraft:soul_lantern
setblock -11 64 -32 minecraft:amethyst_cluster[facing=up]
fill -6 64 -25 -6 65 -25 minecraft:polished_blackstone_wall
setblock -6 66 -25 minecraft:soul_lantern
setblock -11 64 -26 minecraft:amethyst_cluster[facing=up]
summon minecraft:text_display -8.4 75.4 -28.5 {Tags:["mg.olport"],Rotation:[-90f,0f],text:{"text":"🌙 OMBRELUNE","color":"light_purple","bold":true},background:-1442840576,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.6f,2.6f,2.6f]}}
summon minecraft:text_display -8.4 74.95 -28.5 {Tags:["mg.olport"],Rotation:[-90f,0f],text:{"text":"RPG médiéval-fantastique : 8 régions, dragons, donjons","color":"gray"},background:0,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.9f,0.9f,0.9f]}}
summon minecraft:text_display -8.4 64.4 -28.5 {Tags:["mg.olport"],Rotation:[-90f,0f],text:{"text":"▶ entre dans le portail","color":"yellow"},background:0,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
function mg:ombre/spawn_clean
