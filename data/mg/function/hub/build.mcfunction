# Hub des portails : huit petits portails au spawn nord (ex-portail des plots), reconstruit par mg:hub/tick si son témoin disparaît
kill @e[tag=mg.hubp]
kill @e[tag=mg.gtap]
kill @e[tag=mg.tvport]
kill @e[tag=mg.olport]
kill @e[type=minecraft:text_display,x=-10,y=63,z=-56,dx=20,dy=19,dz=14]
fill -10 64 -56 10 82 -42 minecraft:air
fill -10 63 -56 10 63 -42 minecraft:smooth_stone
setblock 0 63 -49 minecraft:mossy_stone_bricks
execute unless data storage mg:hub floaty run data modify storage mg:hub floaty set value 0b
execute unless data storage mg:hub oldclean run function mg:hub/old_clean
# portail gta : plan x=-9, ouverture z -53..-52
fill -9 64 -55 -9 70 -50 minecraft:polished_deepslate
fill -9 64 -53 -9 67 -52 minecraft:air
fill -9 64 -55 -9 70 -55 minecraft:gold_block
fill -9 64 -50 -9 70 -50 minecraft:gold_block
fill -9 71 -55 -9 71 -50 minecraft:gold_block
fill -10 63 -54 -8 63 -51 minecraft:yellow_concrete
summon minecraft:text_display -8.5 73.2 -52.5 {Tags:["mg.hubp"],billboard:"center",background:-1442840576,text:'{"text": "🚓 NEO GTA", "color": "gold", "bold": true}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.2f,2.2f,2.2f]}}
summon minecraft:text_display -8.5 72.5 -52.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:'{"text": "Monde GTA libre : armes, voitures, hélicos, police", "color": "gray"}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:text_display -8.5 66.2 -52.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:'{"text": "▶ entre dans le portail", "color": "yellow"}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
setblock -9 63 -52 minecraft:chiseled_polished_blackstone
# portail terra : plan x=-3, ouverture z -53..-52
fill -3 64 -55 -3 70 -50 minecraft:polished_deepslate
fill -3 64 -53 -3 67 -52 minecraft:air
fill -3 64 -55 -3 70 -55 minecraft:moss_block
fill -3 64 -50 -3 70 -50 minecraft:moss_block
fill -3 71 -55 -3 71 -50 minecraft:moss_block
fill -4 63 -54 -2 63 -51 minecraft:mossy_stone_bricks
summon minecraft:text_display -2.5 73.2 -52.5 {Tags:["mg.hubp"],billboard:"center",background:-1442840576,text:'{"text": "🦖 TERRA NOVA", "color": "green", "bold": true}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.2f,2.2f,2.2f]}}
summon minecraft:text_display -2.5 72.5 -52.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:'{"text": "Colonie préhistorique : missions, jungle, dinosaures", "color": "gray"}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:text_display -2.5 66.2 -52.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:'{"text": "▶ entre dans le portail", "color": "yellow"}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
setblock -3 63 -52 minecraft:chiseled_tuff_bricks
# portail ombre : plan x=3, ouverture z -53..-52
fill 3 64 -55 3 70 -50 minecraft:polished_deepslate
fill 3 64 -53 3 67 -52 minecraft:air
fill 3 64 -55 3 70 -55 minecraft:amethyst_block
fill 3 64 -50 3 70 -50 minecraft:amethyst_block
fill 3 71 -55 3 71 -50 minecraft:amethyst_block
fill 2 63 -54 4 63 -51 minecraft:deepslate_tiles
summon minecraft:text_display 3.5 73.2 -52.5 {Tags:["mg.hubp"],billboard:"center",background:-1442840576,text:'{"text": "🌙 OMBRELUNE", "color": "light_purple", "bold": true}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.2f,2.2f,2.2f]}}
summon minecraft:text_display 3.5 72.5 -52.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:'{"text": "RPG médiéval-fantastique : 8 régions, dragons, donjons", "color": "gray"}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:text_display 3.5 66.2 -52.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:'{"text": "▶ entre dans le portail", "color": "yellow"}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
setblock 3 63 -52 minecraft:chiseled_polished_blackstone
# portail pvp : plan x=9, ouverture z -53..-52
fill 9 64 -55 9 70 -50 minecraft:polished_deepslate
fill 9 64 -53 9 67 -52 minecraft:air
fill 9 64 -55 9 70 -55 minecraft:red_nether_bricks
fill 9 64 -50 9 70 -50 minecraft:red_nether_bricks
fill 9 71 -55 9 71 -50 minecraft:red_nether_bricks
fill 8 63 -54 10 63 -51 minecraft:blackstone
summon minecraft:text_display 9.5 73.2 -52.5 {Tags:["mg.hubp"],billboard:"center",background:-1442840576,text:'{"text": "⚔ ARÈNE PVP", "color": "red", "bold": true}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.2f,2.2f,2.2f]}}
summon minecraft:text_display 9.5 72.5 -52.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:'{"text": "Trou souterrain : classes, points, mini-lobby", "color": "gray"}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:text_display 9.5 66.2 -52.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:'{"text": "▶ entre dans le portail", "color": "yellow"}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
# portail survie : plan x=-9, ouverture z -46..-45
fill -9 64 -48 -9 70 -43 minecraft:polished_deepslate
fill -9 64 -46 -9 67 -45 minecraft:air
fill -9 64 -48 -9 70 -48 minecraft:oak_log
fill -9 64 -43 -9 70 -43 minecraft:oak_log
fill -9 71 -48 -9 71 -43 minecraft:oak_log
fill -10 63 -47 -8 63 -44 minecraft:grass_block
summon minecraft:text_display -8.5 73.2 -45.5 {Tags:["mg.hubp"],billboard:"center",background:-1442840576,text:'{"text": "🌲 SURVIE", "color": "dark_green", "bold": true}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.2f,2.2f,2.2f]}}
summon minecraft:text_display -8.5 72.5 -45.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:'{"text": "Monde libre : inventaire gardé, structures", "color": "gray"}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:text_display -8.5 66.2 -45.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:'{"text": "▶ entre dans le portail", "color": "yellow"}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
# portail filon : plan x=-3, ouverture z -46..-45
fill -3 64 -48 -3 70 -43 minecraft:polished_deepslate
fill -3 64 -46 -3 67 -45 minecraft:air
fill -3 64 -48 -3 70 -48 minecraft:iron_block
fill -3 64 -43 -3 70 -43 minecraft:iron_block
fill -3 71 -48 -3 71 -43 minecraft:iron_block
fill -4 63 -47 -2 63 -44 minecraft:sandstone
summon minecraft:text_display -2.5 73.2 -45.5 {Tags:["mg.hubp"],billboard:"center",background:-1442840576,text:'{"text": "⛏ FILON", "color": "yellow", "bold": true}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.2f,2.2f,2.2f]}}
summon minecraft:text_display -2.5 72.5 -45.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:'{"text": "Mode long par saisons : mine, comptoir, classement", "color": "gray"}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:text_display -2.5 66.2 -45.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:'{"text": "▶ entre dans le portail", "color": "yellow"}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
# portail floaty : plan x=3, ouverture z -46..-45
fill 3 64 -48 3 70 -43 minecraft:polished_deepslate
fill 3 64 -46 3 67 -45 minecraft:air
fill 3 64 -48 3 70 -48 minecraft:prismarine_bricks
fill 3 64 -43 3 70 -43 minecraft:prismarine_bricks
fill 3 71 -48 3 71 -43 minecraft:prismarine_bricks
fill 2 63 -47 4 63 -44 minecraft:prismarine
summon minecraft:text_display 3.5 73.2 -45.5 {Tags:["mg.hubp"],billboard:"center",background:-1442840576,text:'{"text": "🏝 SCOURGE OF THE FLOATY ISLES", "color": "aqua", "bold": true}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.2f,2.2f,2.2f]}}
summon minecraft:text_display 3.5 72.5 -45.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:'{"text": "Carte d aventure partagée", "color": "gray"}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:text_display 3.5 66.2 -45.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:'{"text": "▶ entre dans le portail", "color": "yellow"}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
# portail foot : plan x=9, ouverture z -46..-45
fill 9 64 -48 9 70 -43 minecraft:polished_deepslate
fill 9 64 -46 9 67 -45 minecraft:air
fill 9 64 -48 9 70 -48 minecraft:green_terracotta
fill 9 64 -43 9 70 -43 minecraft:green_terracotta
fill 9 71 -48 9 71 -43 minecraft:green_terracotta
fill 8 63 -47 10 63 -44 minecraft:green_terracotta
summon minecraft:text_display 9.5 73.2 -45.5 {Tags:["mg.hubp"],billboard:"center",background:-1442840576,text:'{"text": "⚽ TERRAIN DE FOOT", "color": "dark_green", "bold": true}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.2f,2.2f,2.2f]}}
summon minecraft:text_display 9.5 72.5 -45.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:'{"text": "Vestiaire souterrain, équipes, buts", "color": "gray"}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:text_display 9.5 66.2 -45.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:'{"text": "▶ entre dans le portail", "color": "yellow"}',transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
