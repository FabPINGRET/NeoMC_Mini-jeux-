# ⚔ Arène PvP souterraine : mini-lobby des classes + arène (généré par tools/lobby/gen_pvpcave.py)
kill @e[tag=mg.pvpcd]
kill @e[type=minecraft:item,tag=mg.pvpcoin]
fill 0 41 0 26 52 24 minecraft:deepslate_bricks
fill 1 43 1 25 51 23 minecraft:air
fill 1 42 1 25 42 23 minecraft:polished_andesite
fill 2 42 2 24 42 22 minecraft:stone_bricks
fill 4 42 4 22 42 20 minecraft:smooth_stone
fill 11 42 10 15 42 14 minecraft:polished_deepslate
fill 12 42 11 14 42 13 minecraft:chiseled_stone_bricks
fill 1 43 1 25 43 1 minecraft:mossy_stone_bricks
fill 1 43 23 25 43 23 minecraft:mossy_stone_bricks
fill 1 43 1 1 43 23 minecraft:mossy_stone_bricks
fill 25 43 1 25 43 23 minecraft:mossy_stone_bricks
fill 2 43 2 24 43 22 minecraft:air
fill 6 43 6 7 51 7 minecraft:stone_bricks
fill 6 43 6 7 43 7 minecraft:chiseled_stone_bricks
setblock 6 51 5 minecraft:lantern[hanging=true]
fill 19 43 6 20 51 7 minecraft:stone_bricks
fill 19 43 6 20 43 7 minecraft:chiseled_stone_bricks
setblock 19 51 5 minecraft:lantern[hanging=true]
fill 6 43 17 7 51 18 minecraft:stone_bricks
fill 6 43 17 7 43 18 minecraft:chiseled_stone_bricks
setblock 6 51 16 minecraft:lantern[hanging=true]
fill 19 43 17 20 51 18 minecraft:stone_bricks
fill 19 43 17 20 43 18 minecraft:chiseled_stone_bricks
setblock 19 51 16 minecraft:lantern[hanging=true]
fill 11 43 5 15 43 5 minecraft:mossy_stone_bricks
fill 11 43 19 15 43 19 minecraft:mossy_stone_bricks
fill 4 43 10 4 43 14 minecraft:mossy_stone_bricks
fill 22 43 10 22 43 14 minecraft:mossy_stone_bricks
fill 12 43 11 14 43 13 minecraft:smooth_stone_slab[type=bottom]
setblock 13 43 12 minecraft:chiseled_stone_bricks
fill 9 43 21 9 43 22 minecraft:cobblestone_wall
fill 17 43 2 17 43 3 minecraft:cobblestone_wall
setblock 3 42 7 minecraft:slime_block
setblock 23 42 17 minecraft:slime_block
setblock 4 52 4 minecraft:sea_lantern
setblock 4 52 10 minecraft:sea_lantern
setblock 4 52 16 minecraft:sea_lantern
setblock 4 52 22 minecraft:sea_lantern
setblock 10 52 4 minecraft:sea_lantern
setblock 10 52 10 minecraft:sea_lantern
setblock 10 52 16 minecraft:sea_lantern
setblock 10 52 22 minecraft:sea_lantern
setblock 16 52 4 minecraft:sea_lantern
setblock 16 52 10 minecraft:sea_lantern
setblock 16 52 16 minecraft:sea_lantern
setblock 16 52 22 minecraft:sea_lantern
setblock 22 52 4 minecraft:sea_lantern
setblock 22 52 10 minecraft:sea_lantern
setblock 22 52 16 minecraft:sea_lantern
setblock 22 52 22 minecraft:sea_lantern
setblock 0 46 7 minecraft:glowstone
setblock 0 46 17 minecraft:glowstone
setblock 26 46 7 minecraft:glowstone
setblock 26 46 17 minecraft:glowstone
setblock 8 46 0 minecraft:glowstone
setblock 18 46 0 minecraft:glowstone
setblock 8 46 24 minecraft:glowstone
setblock 18 46 24 minecraft:glowstone
fill 6 53 5 20 59 19 minecraft:deepslate_bricks
fill 7 55 6 19 58 18 minecraft:air
fill 7 54 6 19 54 18 minecraft:deepslate_tiles
fill 8 54 7 18 54 17 minecraft:polished_deepslate
fill 7 59 6 19 59 18 minecraft:polished_deepslate
setblock 13 53 5 minecraft:lodestone
setblock 9 59 8 minecraft:shroomlight
setblock 9 59 16 minecraft:shroomlight
setblock 13 59 8 minecraft:shroomlight
setblock 13 59 16 minecraft:shroomlight
setblock 17 59 8 minecraft:shroomlight
setblock 17 59 16 minecraft:shroomlight
fill 13 59 12 14 63 13 minecraft:air
fill 13 54 12 14 54 13 minecraft:hay_block
fill 12 64 11 15 66 14 minecraft:air
fill 12 63 11 15 63 14 minecraft:polished_blackstone_bricks
fill 13 63 12 14 63 13 minecraft:air
fill 12 59 11 15 62 14 minecraft:deepslate_bricks
fill 13 59 12 14 62 13 minecraft:air
setblock 12 64 11 minecraft:polished_blackstone_wall
setblock 12 65 11 minecraft:lantern
setblock 15 64 11 minecraft:polished_blackstone_wall
setblock 15 65 11 minecraft:lantern
setblock 12 64 14 minecraft:polished_blackstone_wall
setblock 12 65 14 minecraft:lantern
setblock 15 64 14 minecraft:polished_blackstone_wall
setblock 15 65 14 minecraft:lantern
summon minecraft:text_display 14 66.6 13 {Tags:["mg.pvpcd","mg.lby"],billboard:"center",background:0,text:[{"text":"⚔ Arène PvP","color":"red","bold":true},{"text":"\nsaute dans le trou ↓","color":"gray"}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.4f,1.4f,1.4f]}}
fill 8 54 7 10 54 9 minecraft:iron_block
summon minecraft:text_display 9.5 56.6 8.5 {Tags:["mg.pvpcd"],billboard:"center",background:1342177280,text:[{"text":"Guerrier","color":"white","bold":true},{"text":"\nÉpée en fer, bouclier, armure en fer","color":"gray"}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.8f,0.8f,0.8f]}}
fill 16 54 7 18 54 9 minecraft:emerald_block
summon minecraft:text_display 17.5 56.6 8.5 {Tags:["mg.pvpcd"],billboard:"center",background:1342177280,text:[{"text":"Archer","color":"green","bold":true},{"text":"\nArc Puissance II, 48 flèches, armure en mailles","color":"gray"}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.8f,0.8f,0.8f]}}
fill 8 54 15 10 54 17 minecraft:diamond_block
summon minecraft:text_display 9.5 56.6 16.5 {Tags:["mg.pvpcd"],billboard:"center",background:1342177280,text:[{"text":"Tank","color":"aqua","bold":true},{"text":"\nHache, bouclier, armure lourde, +4 cœurs, lent","color":"gray"}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.8f,0.8f,0.8f]}}
fill 16 54 15 18 54 17 minecraft:coal_block
summon minecraft:text_display 17.5 56.6 16.5 {Tags:["mg.pvpcd"],billboard:"center",background:1342177280,text:[{"text":"Assassin","color":"dark_gray","bold":true},{"text":"\nÉpée en fer Tranchant II, rapide, 2 perles","color":"gray"}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.8f,0.8f,0.8f]}}
fill 12 54 16 14 54 18 minecraft:gold_block
summon minecraft:text_display 13.5 56.6 17.5 {Tags:["mg.pvpcd"],billboard:"center",background:1342177280,text:[{"text":"🏠 Retour au spawn","color":"yellow","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:text_display 13.5 57.2 6.1 {Tags:["mg.pvpcd"],billboard:"fixed",Rotation:[0f,0f],background:1342177280,line_width:260,text:[{"text":"⚔ ARÈNE PVP","color":"red","bold":true},{"text":"\nMarche sur un socle pour choisir ta classe et descendre dans l'arène.","color":"white"},{"text":"\n💰 +10 pièces par kill, bonus de série à 3, 5 et 10 kills, pièces à ramasser dans l'arène.","color":"gold"},{"text":"\nÉmeraude = boutique · Boussole = retour au spawn (5 s sans prendre de coup).","color":"gray"}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.75f,0.75f,0.75f]}}
summon minecraft:marker 3.5 43 3.5 {Tags:["mg.pvpcd","mg.pvpsp"]}
summon minecraft:marker 23.5 43 3.5 {Tags:["mg.pvpcd","mg.pvpsp"]}
summon minecraft:marker 3.5 43 21.5 {Tags:["mg.pvpcd","mg.pvpsp"]}
summon minecraft:marker 23.5 43 21.5 {Tags:["mg.pvpcd","mg.pvpsp"]}
summon minecraft:marker 13.5 43 3.5 {Tags:["mg.pvpcd","mg.pvpsp"]}
summon minecraft:marker 13.5 43 21.5 {Tags:["mg.pvpcd","mg.pvpsp"]}
summon minecraft:marker 3.5 43 12.5 {Tags:["mg.pvpcd","mg.pvpsp"]}
summon minecraft:marker 23.5 43 12.5 {Tags:["mg.pvpcd","mg.pvpsp"]}
data modify storage mg:lobby pvpc1 set value 1b
