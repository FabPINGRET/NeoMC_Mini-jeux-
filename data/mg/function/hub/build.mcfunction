# Hub des portails : huit petits portails au spawn nord (ex-portail des plots), reconstruit par mg:hub/tick si son témoin disparaît
kill @e[tag=mg.hubp]
kill @e[tag=mg.gtap]
kill @e[tag=mg.tvport]
kill @e[tag=mg.olport]
kill @e[type=minecraft:text_display,x=-10,y=63,z=-61,dx=20,dy=19,dz=19]
kill @e[type=minecraft:item_display,tag=mg.lby,x=-10,y=63,z=-61,dx=20,dy=19,dz=19]
fill -10 64 -61 10 82 -42 minecraft:air
fill -10 63 -61 10 63 -42 minecraft:smooth_stone
setblock 0 63 -52 minecraft:mossy_stone_bricks
execute unless data storage mg:hub floaty run data modify storage mg:hub floaty set value 0b
execute unless data storage mg:hub oldclean run function mg:hub/old_clean
schedule function mg:hub/decofix_start 20s
# portail gta : plan x=-9, ouverture z -55..-54, trois blocs de haut
fill -9 64 -56 -9 65 -53 minecraft:polished_deepslate
fill -9 64 -55 -9 65 -54 minecraft:air
fill -9 64 -56 -9 65 -56 minecraft:gold_block
fill -9 64 -53 -9 65 -53 minecraft:gold_block
fill -9 66 -56 -9 66 -53 minecraft:gold_block
fill -9 63 -56 -9 63 -53 minecraft:yellow_concrete
summon minecraft:text_display -8.5 68.4 -54.5 {Tags:["mg.hubp"],billboard:"center",background:-1442840576,text:{"text": "🚓 NEO GTA", "color": "gold", "bold": true},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.2f,2.2f,2.2f]}}
summon minecraft:text_display -8.5 67.8 -54.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:{"text": "Monde GTA libre : armes, voitures, hélicos, police", "color": "gray"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:text_display -8.5 67.2 -54.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:{"text": "▶ entre dans le portail", "color": "yellow"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
setblock -9 63 -54 minecraft:chiseled_polished_blackstone
# portail terra : plan x=-6, ouverture z -59..-58, trois blocs de haut
fill -6 64 -60 -6 65 -57 minecraft:polished_deepslate
fill -6 64 -59 -6 65 -58 minecraft:air
fill -6 64 -60 -6 65 -60 minecraft:moss_block
fill -6 64 -57 -6 65 -57 minecraft:moss_block
fill -6 66 -60 -6 66 -57 minecraft:moss_block
fill -6 63 -60 -6 63 -57 minecraft:mossy_stone_bricks
summon minecraft:text_display -5.5 68.4 -58.5 {Tags:["mg.hubp"],billboard:"center",background:-1442840576,text:{"text": "🦖 TERRA NOVA", "color": "green", "bold": true},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.2f,2.2f,2.2f]}}
summon minecraft:text_display -5.5 67.8 -58.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:{"text": "Colonie préhistorique : missions, jungle, dinosaures", "color": "gray"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:text_display -5.5 67.2 -58.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:{"text": "▶ entre dans le portail", "color": "yellow"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
setblock -6 63 -58 minecraft:chiseled_tuff_bricks
# portail ombre : plan x=6, ouverture z -59..-58, trois blocs de haut
fill 6 64 -60 6 65 -57 minecraft:polished_deepslate
fill 6 64 -59 6 65 -58 minecraft:air
fill 6 64 -60 6 65 -60 minecraft:amethyst_block
fill 6 64 -57 6 65 -57 minecraft:amethyst_block
fill 6 66 -60 6 66 -57 minecraft:amethyst_block
fill 6 63 -60 6 63 -57 minecraft:deepslate_tiles
summon minecraft:text_display 6.5 68.4 -58.5 {Tags:["mg.hubp"],billboard:"center",background:-1442840576,text:{"text": "🌙 OMBRELUNE", "color": "light_purple", "bold": true},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.2f,2.2f,2.2f]}}
summon minecraft:text_display 6.5 67.8 -58.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:{"text": "RPG médiéval-fantastique : 8 régions, dragons, donjons", "color": "gray"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:text_display 6.5 67.2 -58.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:{"text": "▶ entre dans le portail", "color": "yellow"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
setblock 6 63 -58 minecraft:chiseled_polished_blackstone
# portail pvp : plan x=9, ouverture z -55..-54, trois blocs de haut
fill 9 64 -56 9 65 -53 minecraft:polished_deepslate
fill 9 64 -55 9 65 -54 minecraft:air
fill 9 64 -56 9 65 -56 minecraft:red_nether_bricks
fill 9 64 -53 9 65 -53 minecraft:red_nether_bricks
fill 9 66 -56 9 66 -53 minecraft:red_nether_bricks
fill 9 63 -56 9 63 -53 minecraft:blackstone
summon minecraft:text_display 9.5 68.4 -54.5 {Tags:["mg.hubp"],billboard:"center",background:-1442840576,text:{"text": "⚔ ARÈNE PVP", "color": "red", "bold": true},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.2f,2.2f,2.2f]}}
summon minecraft:text_display 9.5 67.8 -54.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:{"text": "Trou souterrain : classes, points, mini-lobby", "color": "gray"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:text_display 9.5 67.2 -54.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:{"text": "▶ entre dans le portail", "color": "yellow"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
# portail survie : plan x=-9, ouverture z -45..-44, trois blocs de haut
fill -9 64 -46 -9 65 -43 minecraft:polished_deepslate
fill -9 64 -45 -9 65 -44 minecraft:air
fill -9 64 -46 -9 65 -46 minecraft:oak_log
fill -9 64 -43 -9 65 -43 minecraft:oak_log
fill -9 66 -46 -9 66 -43 minecraft:oak_log
fill -9 63 -46 -9 63 -43 minecraft:grass_block
summon minecraft:text_display -8.5 68.4 -44.5 {Tags:["mg.hubp"],billboard:"center",background:-1442840576,text:{"text": "🌲 SURVIE", "color": "dark_green", "bold": true},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.2f,2.2f,2.2f]}}
summon minecraft:text_display -8.5 67.8 -44.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:{"text": "Monde libre : inventaire gardé, structures", "color": "gray"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:text_display -8.5 67.2 -44.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:{"text": "▶ entre dans le portail", "color": "yellow"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
# portail filon : plan x=-9, ouverture z -50..-49, trois blocs de haut
fill -9 64 -51 -9 65 -48 minecraft:polished_deepslate
fill -9 64 -50 -9 65 -49 minecraft:air
fill -9 64 -51 -9 65 -51 minecraft:iron_block
fill -9 64 -48 -9 65 -48 minecraft:iron_block
fill -9 66 -51 -9 66 -48 minecraft:iron_block
fill -9 63 -51 -9 63 -48 minecraft:sandstone
summon minecraft:text_display -8.5 68.4 -49.5 {Tags:["mg.hubp"],billboard:"center",background:-1442840576,text:{"text": "⛏ FILON", "color": "yellow", "bold": true},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.2f,2.2f,2.2f]}}
summon minecraft:text_display -8.5 67.8 -49.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:{"text": "Mode long par saisons : mine, comptoir, classement", "color": "gray"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:text_display -8.5 67.2 -49.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:{"text": "▶ entre dans le portail", "color": "yellow"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
# portail floaty : plan x=9, ouverture z -50..-49, trois blocs de haut
fill 9 64 -51 9 65 -48 minecraft:polished_deepslate
fill 9 64 -50 9 65 -49 minecraft:air
fill 9 64 -51 9 65 -51 minecraft:prismarine_bricks
fill 9 64 -48 9 65 -48 minecraft:prismarine_bricks
fill 9 66 -51 9 66 -48 minecraft:prismarine_bricks
fill 9 63 -51 9 63 -48 minecraft:prismarine
summon minecraft:text_display 9.5 68.4 -49.5 {Tags:["mg.hubp"],billboard:"center",background:-1442840576,text:{"text": "🏝 SCOURGE OF THE FLOATY ISLES", "color": "aqua", "bold": true},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.2f,2.2f,2.2f]}}
summon minecraft:text_display 9.5 67.8 -49.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:{"text": "Carte d aventure partagée", "color": "gray"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:text_display 9.5 67.2 -49.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:{"text": "▶ entre dans le portail", "color": "yellow"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
# portail foot : plan x=9, ouverture z -45..-44, trois blocs de haut
fill 9 64 -46 9 65 -43 minecraft:polished_deepslate
fill 9 64 -45 9 65 -44 minecraft:air
fill 9 64 -46 9 65 -46 minecraft:green_terracotta
fill 9 64 -43 9 65 -43 minecraft:green_terracotta
fill 9 66 -46 9 66 -43 minecraft:green_terracotta
fill 9 63 -46 9 63 -43 minecraft:green_terracotta
summon minecraft:text_display 9.5 68.4 -44.5 {Tags:["mg.hubp"],billboard:"center",background:-1442840576,text:{"text": "⚽ TERRAIN DE FOOT", "color": "dark_green", "bold": true},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[2.2f,2.2f,2.2f]}}
summon minecraft:text_display 9.5 67.8 -44.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:{"text": "Vestiaire souterrain, équipes, buts", "color": "gray"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:text_display 9.5 67.2 -44.5 {Tags:["mg.hubp"],billboard:"center",background:0,text:{"text": "▶ entre dans le portail", "color": "yellow"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.7f,0.7f,0.7f]}}
