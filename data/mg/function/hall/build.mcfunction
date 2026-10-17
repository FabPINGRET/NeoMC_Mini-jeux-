# Allée des champions (Hall des scores v18, à ciel ouvert, sud-ouest de la place) : construction + top 3 (généré par tools/hall/gen_hall.py)
# Chunks pas encore chargés (démarrage du serveur) : on réessaie dans 1 s, 60 fois au plus
execute store success score #hl mg.st unless block -58 300 23 minecraft:bedrock
execute if score #hl mg.st matches 1 store success score #hl mg.st unless block -14 300 28 minecraft:bedrock
execute if score #hl mg.st matches 0 run scoreboard players add #hlr mg.st 1
execute if score #hl mg.st matches 0 if score #hlr mg.st matches 60.. run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Hall des scores : chunks pas chargés, construction abandonnée (relance /function mg:hall/build).","color":"red"}]
execute if score #hl mg.st matches 0 if score #hlr mg.st matches 60.. run return run scoreboard players set #hlr mg.st 0
execute if score #hl mg.st matches 0 run return run schedule function mg:hall/build 20t
scoreboard players set #hlr mg.st 0
kill @e[tag=mg.hall]
execute unless data storage mg:hall v15 run function mg:hall/clear_old

# terrain des versions précédentes rendu à la pelouse, puis l'allée et ses deux rangées de stands
fill -60 64 15 -6 84 36 minecraft:air
fill -60 62 15 -6 62 36 minecraft:dirt
fill -60 63 15 -6 63 36 minecraft:grass_block
fill -59 63 24 -6 63 27 minecraft:dirt_path
fill -13 63 20 -6 63 31 minecraft:polished_andesite
fill -60 64 20 -12 64 20 minecraft:moss_block
fill -60 64 31 -12 64 31 minecraft:moss_block
fill -60 64 20 -60 64 31 minecraft:moss_block
fill -12 64 20 -12 64 31 minecraft:moss_block
fill -12 64 24 -12 64 27 minecraft:air
setblock -60 65 20 minecraft:lantern
setblock -60 65 31 minecraft:lantern
setblock -54 65 20 minecraft:lantern
setblock -54 65 31 minecraft:lantern
setblock -48 65 20 minecraft:lantern
setblock -48 65 31 minecraft:lantern
setblock -42 65 20 minecraft:lantern
setblock -42 65 31 minecraft:lantern
setblock -36 65 20 minecraft:lantern
setblock -36 65 31 minecraft:lantern
setblock -30 65 20 minecraft:lantern
setblock -30 65 31 minecraft:lantern
setblock -24 65 20 minecraft:lantern
setblock -24 65 31 minecraft:lantern
setblock -18 65 20 minecraft:lantern
setblock -18 65 31 minecraft:lantern
setblock -12 65 20 minecraft:lantern
setblock -12 65 31 minecraft:lantern
fill -59 63 21 -58 63 23 minecraft:light_blue_concrete
fill -59 64 21 -58 64 21 minecraft:polished_andesite
setblock -59 65 21 minecraft:gold_block
setblock -58 65 21 minecraft:iron_block
setblock -59 64 22 minecraft:copper_block
fill -57 63 21 -56 63 23 minecraft:red_concrete
fill -57 64 21 -56 64 21 minecraft:polished_andesite
setblock -57 65 21 minecraft:gold_block
setblock -56 65 21 minecraft:iron_block
setblock -57 64 22 minecraft:copper_block
fill -55 63 21 -54 63 23 minecraft:yellow_concrete
fill -55 64 21 -54 64 21 minecraft:polished_andesite
setblock -55 65 21 minecraft:gold_block
setblock -54 65 21 minecraft:iron_block
setblock -55 64 22 minecraft:copper_block
fill -53 63 21 -52 63 23 minecraft:red_concrete
fill -53 64 21 -52 64 21 minecraft:polished_andesite
setblock -53 65 21 minecraft:gold_block
setblock -52 65 21 minecraft:iron_block
setblock -53 64 22 minecraft:copper_block
fill -51 63 21 -50 63 23 minecraft:white_concrete
fill -51 64 21 -50 64 21 minecraft:polished_andesite
setblock -51 65 21 minecraft:gold_block
setblock -50 65 21 minecraft:iron_block
setblock -51 64 22 minecraft:copper_block
fill -49 63 21 -48 63 23 minecraft:green_concrete
fill -49 64 21 -48 64 21 minecraft:polished_andesite
setblock -49 65 21 minecraft:gold_block
setblock -48 65 21 minecraft:iron_block
setblock -49 64 22 minecraft:copper_block
fill -47 63 21 -46 63 23 minecraft:yellow_concrete
fill -47 64 21 -46 64 21 minecraft:polished_andesite
setblock -47 65 21 minecraft:gold_block
setblock -46 65 21 minecraft:iron_block
setblock -47 64 22 minecraft:copper_block
fill -45 63 21 -44 63 23 minecraft:yellow_concrete
fill -45 64 21 -44 64 21 minecraft:polished_andesite
setblock -45 65 21 minecraft:gold_block
setblock -44 65 21 minecraft:iron_block
setblock -45 64 22 minecraft:copper_block
fill -43 63 21 -42 63 23 minecraft:light_blue_concrete
fill -43 64 21 -42 64 21 minecraft:polished_andesite
setblock -43 65 21 minecraft:gold_block
setblock -42 65 21 minecraft:iron_block
setblock -43 64 22 minecraft:copper_block
fill -41 63 21 -40 63 23 minecraft:yellow_concrete
fill -41 64 21 -40 64 21 minecraft:polished_andesite
setblock -41 65 21 minecraft:gold_block
setblock -40 65 21 minecraft:iron_block
setblock -41 64 22 minecraft:copper_block
fill -39 63 21 -38 63 23 minecraft:red_concrete
fill -39 64 21 -38 64 21 minecraft:polished_andesite
setblock -39 65 21 minecraft:gold_block
setblock -38 65 21 minecraft:iron_block
setblock -39 64 22 minecraft:copper_block
fill -37 63 21 -36 63 23 minecraft:magenta_concrete
fill -37 64 21 -36 64 21 minecraft:polished_andesite
setblock -37 65 21 minecraft:gold_block
setblock -36 65 21 minecraft:iron_block
setblock -37 64 22 minecraft:copper_block
fill -35 63 21 -34 63 23 minecraft:gray_concrete
fill -35 64 21 -34 64 21 minecraft:polished_andesite
setblock -35 65 21 minecraft:gold_block
setblock -34 65 21 minecraft:iron_block
setblock -35 64 22 minecraft:copper_block
fill -33 63 21 -32 63 23 minecraft:yellow_concrete
fill -33 64 21 -32 64 21 minecraft:polished_andesite
setblock -33 65 21 minecraft:gold_block
setblock -32 65 21 minecraft:iron_block
setblock -33 64 22 minecraft:copper_block
fill -31 63 21 -30 63 23 minecraft:light_blue_concrete
fill -31 64 21 -30 64 21 minecraft:polished_andesite
setblock -31 65 21 minecraft:gold_block
setblock -30 65 21 minecraft:iron_block
setblock -31 64 22 minecraft:copper_block
fill -29 63 21 -28 63 23 minecraft:yellow_concrete
fill -29 64 21 -28 64 21 minecraft:polished_andesite
setblock -29 65 21 minecraft:gold_block
setblock -28 65 21 minecraft:iron_block
setblock -29 64 22 minecraft:copper_block
fill -27 63 21 -26 63 23 minecraft:light_blue_concrete
fill -27 64 21 -26 64 21 minecraft:polished_andesite
setblock -27 65 21 minecraft:gold_block
setblock -26 65 21 minecraft:iron_block
setblock -27 64 22 minecraft:copper_block
fill -25 63 21 -24 63 23 minecraft:lime_concrete
fill -25 64 21 -24 64 21 minecraft:polished_andesite
setblock -25 65 21 minecraft:gold_block
setblock -24 65 21 minecraft:iron_block
setblock -25 64 22 minecraft:copper_block
fill -23 63 21 -22 63 23 minecraft:yellow_concrete
fill -23 64 21 -22 64 21 minecraft:polished_andesite
setblock -23 65 21 minecraft:gold_block
setblock -22 65 21 minecraft:iron_block
setblock -23 64 22 minecraft:copper_block
fill -21 63 21 -20 63 23 minecraft:red_concrete
fill -21 64 21 -20 64 21 minecraft:polished_andesite
setblock -21 65 21 minecraft:gold_block
setblock -20 65 21 minecraft:iron_block
setblock -21 64 22 minecraft:copper_block
fill -19 63 21 -18 63 23 minecraft:light_blue_concrete
fill -19 64 21 -18 64 21 minecraft:polished_andesite
setblock -19 65 21 minecraft:gold_block
setblock -18 65 21 minecraft:iron_block
setblock -19 64 22 minecraft:copper_block
fill -17 63 21 -16 63 23 minecraft:light_blue_concrete
fill -17 64 21 -16 64 21 minecraft:polished_andesite
setblock -17 65 21 minecraft:gold_block
setblock -16 65 21 minecraft:iron_block
setblock -17 64 22 minecraft:copper_block
fill -59 63 28 -58 63 30 minecraft:yellow_concrete
fill -59 64 30 -58 64 30 minecraft:polished_andesite
setblock -59 65 30 minecraft:gold_block
setblock -58 65 30 minecraft:iron_block
setblock -59 64 29 minecraft:copper_block
fill -57 63 28 -56 63 30 minecraft:light_blue_concrete
fill -57 64 30 -56 64 30 minecraft:polished_andesite
setblock -57 65 30 minecraft:gold_block
setblock -56 65 30 minecraft:iron_block
setblock -57 64 29 minecraft:copper_block
fill -55 63 28 -54 63 30 minecraft:yellow_concrete
fill -55 64 30 -54 64 30 minecraft:polished_andesite
setblock -55 65 30 minecraft:gold_block
setblock -54 65 30 minecraft:iron_block
setblock -55 64 29 minecraft:copper_block
fill -53 63 28 -52 63 30 minecraft:yellow_concrete
fill -53 64 30 -52 64 30 minecraft:polished_andesite
setblock -53 65 30 minecraft:gold_block
setblock -52 65 30 minecraft:iron_block
setblock -53 64 29 minecraft:copper_block
fill -51 63 28 -50 63 30 minecraft:yellow_concrete
fill -51 64 30 -50 64 30 minecraft:polished_andesite
setblock -51 65 30 minecraft:gold_block
setblock -50 65 30 minecraft:iron_block
setblock -51 64 29 minecraft:copper_block
fill -49 63 28 -48 63 30 minecraft:red_concrete
fill -49 64 30 -48 64 30 minecraft:polished_andesite
setblock -49 65 30 minecraft:gold_block
setblock -48 65 30 minecraft:iron_block
setblock -49 64 29 minecraft:copper_block
fill -47 63 28 -46 63 30 minecraft:yellow_concrete
fill -47 64 30 -46 64 30 minecraft:polished_andesite
setblock -47 65 30 minecraft:gold_block
setblock -46 65 30 minecraft:iron_block
setblock -47 64 29 minecraft:copper_block
fill -45 63 28 -44 63 30 minecraft:yellow_concrete
fill -45 64 30 -44 64 30 minecraft:polished_andesite
setblock -45 65 30 minecraft:gold_block
setblock -44 65 30 minecraft:iron_block
setblock -45 64 29 minecraft:copper_block
fill -43 63 28 -42 63 30 minecraft:yellow_concrete
fill -43 64 30 -42 64 30 minecraft:polished_andesite
setblock -43 65 30 minecraft:gold_block
setblock -42 65 30 minecraft:iron_block
setblock -43 64 29 minecraft:copper_block
fill -41 63 28 -40 63 30 minecraft:green_concrete
fill -41 64 30 -40 64 30 minecraft:polished_andesite
setblock -41 65 30 minecraft:gold_block
setblock -40 65 30 minecraft:iron_block
setblock -41 64 29 minecraft:copper_block
fill -39 63 28 -38 63 30 minecraft:lime_concrete
fill -39 64 30 -38 64 30 minecraft:polished_andesite
setblock -39 65 30 minecraft:gold_block
setblock -38 65 30 minecraft:iron_block
setblock -39 64 29 minecraft:copper_block
fill -37 63 28 -36 63 30 minecraft:red_concrete
fill -37 64 30 -36 64 30 minecraft:polished_andesite
setblock -37 65 30 minecraft:gold_block
setblock -36 65 30 minecraft:iron_block
setblock -37 64 29 minecraft:copper_block
fill -35 63 28 -34 63 30 minecraft:lime_concrete
fill -35 64 30 -34 64 30 minecraft:polished_andesite
setblock -35 65 30 minecraft:gold_block
setblock -34 65 30 minecraft:iron_block
setblock -35 64 29 minecraft:copper_block
fill -33 63 28 -32 63 30 minecraft:light_blue_concrete
fill -33 64 30 -32 64 30 minecraft:polished_andesite
setblock -33 65 30 minecraft:gold_block
setblock -32 65 30 minecraft:iron_block
setblock -33 64 29 minecraft:copper_block
fill -31 63 28 -30 63 30 minecraft:red_concrete
fill -31 64 30 -30 64 30 minecraft:polished_andesite
setblock -31 65 30 minecraft:gold_block
setblock -30 65 30 minecraft:iron_block
setblock -31 64 29 minecraft:copper_block
fill -29 63 28 -28 63 30 minecraft:light_blue_concrete
fill -29 64 30 -28 64 30 minecraft:polished_andesite
setblock -29 65 30 minecraft:gold_block
setblock -28 65 30 minecraft:iron_block
setblock -29 64 29 minecraft:copper_block
fill -27 63 28 -26 63 30 minecraft:lime_concrete
fill -27 64 30 -26 64 30 minecraft:polished_andesite
setblock -27 65 30 minecraft:gold_block
setblock -26 65 30 minecraft:iron_block
setblock -27 64 29 minecraft:copper_block
fill -25 63 28 -24 63 30 minecraft:magenta_concrete
fill -25 64 30 -24 64 30 minecraft:polished_andesite
setblock -25 65 30 minecraft:gold_block
setblock -24 65 30 minecraft:iron_block
setblock -25 64 29 minecraft:copper_block
fill -23 63 28 -22 63 30 minecraft:yellow_concrete
fill -23 64 30 -22 64 30 minecraft:polished_andesite
setblock -23 65 30 minecraft:gold_block
setblock -22 65 30 minecraft:iron_block
setblock -23 64 29 minecraft:copper_block
fill -21 63 28 -20 63 30 minecraft:red_concrete
fill -21 64 30 -20 64 30 minecraft:polished_andesite
setblock -21 65 30 minecraft:gold_block
setblock -20 65 30 minecraft:iron_block
setblock -21 64 29 minecraft:copper_block
fill -19 63 28 -18 63 30 minecraft:red_concrete
fill -19 64 30 -18 64 30 minecraft:polished_andesite
setblock -19 65 30 minecraft:gold_block
setblock -18 65 30 minecraft:iron_block
setblock -19 64 29 minecraft:copper_block
fill -17 63 28 -16 63 30 minecraft:magenta_concrete
fill -17 64 30 -16 64 30 minecraft:polished_andesite
setblock -17 65 30 minecraft:gold_block
setblock -16 65 30 minecraft:iron_block
setblock -17 64 29 minecraft:copper_block

# Place d'entrée (est) : piédestaux d'honneur
setblock -9 64 21 minecraft:emerald_block
setblock -9 64 25 minecraft:gold_block
setblock -9 64 30 minecraft:lapis_block

# Tampon de résolution des noms (invisible)
summon minecraft:item_display -8.5 64.5 25.5 {Tags:["mg.hall","mg.hallbuf"],item:{id:"minecraft:paper"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.001f,0.001f,0.001f]}}
summon minecraft:text_display -8.5 70.8 25.5 {Tags:["mg.hall"],billboard:"vertical",background:0,text:[{"text":"🏆 Allée des champions","color":"gold","bold":true},{"text":"\n🥇 🥈 🥉 le top 3 de chaque jeu, de chaque côté de l'allée","color":"gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.6f,1.6f,1.6f]}}

# Piédestaux : objet qui tourne + plaque
summon minecraft:item_display -8.5 65.8 21.5 {Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:clock"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:item_display -8.5 65.8 25.5 {Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:totem_of_undying"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:item_display -8.5 65.8 30.5 {Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:elytra"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.8f,0.8f,0.8f]}}

# Plaques d'honneur : texte par défaut, puis meneur enregistré s'il existe
summon minecraft:text_display -8.5 66.7 21.5 {Tags:["mg.hall","mg.h_stp"],billboard:"vertical",line_width:115,text:[{"text":"▶ Le plus assidu","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute if data storage mg:hall e.stp run data modify entity @e[type=minecraft:text_display,tag=mg.h_stp,limit=1] text set from storage mg:hall e.stp
summon minecraft:text_display -8.5 66.7 25.5 {Tags:["mg.hall","mg.h_wins"],billboard:"vertical",line_width:115,text:[{"text":"👑 Champion des mini-jeux","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute if data storage mg:hall e.wins run data modify entity @e[type=minecraft:text_display,tag=mg.h_wins,limit=1] text set from storage mg:hall e.wins
summon minecraft:text_display -8.5 66.7 30.5 {Tags:["mg.hall","mg.h_ely"],billboard:"vertical",line_width:115,text:[{"text":"🪽 Record petit parcours d'élytra","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute if data storage mg:hall e.ely run data modify entity @e[type=minecraft:text_display,tag=mg.h_ely,limit=1] text set from storage mg:hall e.ely
summon minecraft:text_display -8.5 68.1 30.5 {Tags:["mg.hall","mg.h_ely2"],billboard:"vertical",line_width:115,text:[{"text":"🪽 Record grand parcours d'élytra","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute if data storage mg:hall e.ely2 run data modify entity @e[type=minecraft:text_display,tag=mg.h_ely2,limit=1] text set from storage mg:hall e.ely2
summon minecraft:text_display -8.5 69.5 30.5 {Tags:["mg.hall","mg.h_elyg"],billboard:"vertical",line_width:115,text:[{"text":"🪽 Record Élytra : course","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute if data storage mg:hall e.elyg run data modify entity @e[type=minecraft:text_display,tag=mg.h_elyg,limit=1] text set from storage mg:hall e.elyg
summon minecraft:text_display -8.5 68.6 25.5 {Tags:["mg.hall","mg.h_gen"],billboard:"vertical",line_width:200,text:[{"text":"🏅 Meilleur niveau général","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.1f,1.1f,1.1f]}}
execute if data storage mg:hall e.gen run data modify entity @e[type=minecraft:text_display,tag=mg.h_gen,limit=1] text set from storage mg:hall e.gen

# Stands : top 3 de chaque jeu (texte par défaut, puis top 3 enregistré) ; un panneau sur deux plus haut, pour qu'ils ne se touchent pas
summon minecraft:text_display -58.0 66.3 21.5 {Tags:["mg.hall","mg.h3_spleef"],billboard:"vertical",line_width:130,text:[{"text":"❄ Spleef","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.spleef run data modify entity @e[type=minecraft:text_display,tag=mg.h3_spleef,limit=1] text set from storage mg:hall t3x.spleef
summon minecraft:text_display -56.0 67.5 21.5 {Tags:["mg.hall","mg.h3_tntrun"],billboard:"vertical",line_width:130,text:[{"text":"✷ TNT Run","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.tntrun run data modify entity @e[type=minecraft:text_display,tag=mg.h3_tntrun,limit=1] text set from storage mg:hall t3x.tntrun
summon minecraft:text_display -54.0 66.3 21.5 {Tags:["mg.hall","mg.h3_pvp"],billboard:"vertical",line_width:130,text:[{"text":"⚔ PvP","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.pvp run data modify entity @e[type=minecraft:text_display,tag=mg.h3_pvp,limit=1] text set from storage mg:hall t3x.pvp
summon minecraft:text_display -52.0 67.5 21.5 {Tags:["mg.hall","mg.h3_bedwars"],billboard:"vertical",line_width:130,text:[{"text":"🛏 Bedwars","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.bedwars run data modify entity @e[type=minecraft:text_display,tag=mg.h3_bedwars,limit=1] text set from storage mg:hall t3x.bedwars
summon minecraft:text_display -50.0 66.3 21.5 {Tags:["mg.hall","mg.h3_sheepwar"],billboard:"vertical",line_width:130,text:[{"text":"🐑 Sheep War","color":"white","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.sheepwar run data modify entity @e[type=minecraft:text_display,tag=mg.h3_sheepwar,limit=1] text set from storage mg:hall t3x.sheepwar
summon minecraft:text_display -48.0 67.5 21.5 {Tags:["mg.hall","mg.h3_mobarena"],billboard:"vertical",line_width:130,text:[{"text":"☠ Mob Arena","color":"dark_green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.mobarena run data modify entity @e[type=minecraft:text_display,tag=mg.h3_mobarena,limit=1] text set from storage mg:hall t3x.mobarena
summon minecraft:text_display -46.0 66.3 21.5 {Tags:["mg.hall","mg.h3_splegg"],billboard:"vertical",line_width:130,text:[{"text":"❍ Splegg","color":"yellow","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.splegg run data modify entity @e[type=minecraft:text_display,tag=mg.h3_splegg,limit=1] text set from storage mg:hall t3x.splegg
summon minecraft:text_display -44.0 67.5 21.5 {Tags:["mg.hall","mg.h3_sumo"],billboard:"vertical",line_width:130,text:[{"text":"✊ Sumo","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.sumo run data modify entity @e[type=minecraft:text_display,tag=mg.h3_sumo,limit=1] text set from storage mg:hall t3x.sumo
summon minecraft:text_display -42.0 66.3 21.5 {Tags:["mg.hall","mg.h3_dropper"],billboard:"vertical",line_width:130,text:[{"text":"⬇ Dropper","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.dropper run data modify entity @e[type=minecraft:text_display,tag=mg.h3_dropper,limit=1] text set from storage mg:hall t3x.dropper
summon minecraft:text_display -40.0 67.5 21.5 {Tags:["mg.hall","mg.h3_oitc"],billboard:"vertical",line_width:130,text:[{"text":"➶ One in the Chamber","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.oitc run data modify entity @e[type=minecraft:text_display,tag=mg.h3_oitc,limit=1] text set from storage mg:hall t3x.oitc
summon minecraft:text_display -38.0 66.3 21.5 {Tags:["mg.hall","mg.h3_tnttag"],billboard:"vertical",line_width:130,text:[{"text":"✹ TNT Tag","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.tnttag run data modify entity @e[type=minecraft:text_display,tag=mg.h3_tnttag,limit=1] text set from storage mg:hall t3x.tnttag
summon minecraft:text_display -36.0 67.5 21.5 {Tags:["mg.hall","mg.h3_blockparty"],billboard:"vertical",line_width:130,text:[{"text":"▦ Block Party","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.blockparty run data modify entity @e[type=minecraft:text_display,tag=mg.h3_blockparty,limit=1] text set from storage mg:hall t3x.blockparty
summon minecraft:text_display -34.0 66.3 21.5 {Tags:["mg.hall","mg.h3_anvil"],billboard:"vertical",line_width:130,text:[{"text":"⚓ Pluie d'enclumes","color":"gray","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.anvil run data modify entity @e[type=minecraft:text_display,tag=mg.h3_anvil,limit=1] text set from storage mg:hall t3x.anvil
summon minecraft:text_display -32.0 67.5 21.5 {Tags:["mg.hall","mg.h3_turf"],billboard:"vertical",line_width:130,text:[{"text":"▮ Turf Wars","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.turf run data modify entity @e[type=minecraft:text_display,tag=mg.h3_turf,limit=1] text set from storage mg:hall t3x.turf
summon minecraft:text_display -30.0 66.3 21.5 {Tags:["mg.hall","mg.h3_quake"],billboard:"vertical",line_width:130,text:[{"text":"⚡ Quakecraft","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.quake run data modify entity @e[type=minecraft:text_display,tag=mg.h3_quake,limit=1] text set from storage mg:hall t3x.quake
summon minecraft:text_display -28.0 67.5 21.5 {Tags:["mg.hall","mg.h3_paintball"],billboard:"vertical",line_width:130,text:[{"text":"▓ Paintball","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.paintball run data modify entity @e[type=minecraft:text_display,tag=mg.h3_paintball,limit=1] text set from storage mg:hall t3x.paintball
summon minecraft:text_display -26.0 66.3 21.5 {Tags:["mg.hall","mg.h3_icerace"],billboard:"vertical",line_width:130,text:[{"text":"⛵ Course de bateaux","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.icerace run data modify entity @e[type=minecraft:text_display,tag=mg.h3_icerace,limit=1] text set from storage mg:hall t3x.icerace
summon minecraft:text_display -24.0 67.5 21.5 {Tags:["mg.hall","mg.h3_bb"],billboard:"vertical",line_width:130,text:[{"text":"✎ Build Battle","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.bb run data modify entity @e[type=minecraft:text_display,tag=mg.h3_bb,limit=1] text set from storage mg:hall t3x.bb
summon minecraft:text_display -22.0 66.3 21.5 {Tags:["mg.hall","mg.h3_party"],billboard:"vertical",line_width:130,text:[{"text":"★ Mini Party","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.party run data modify entity @e[type=minecraft:text_display,tag=mg.h3_party,limit=1] text set from storage mg:hall t3x.party
summon minecraft:text_display -20.0 67.5 21.5 {Tags:["mg.hall","mg.h3_kart"],billboard:"vertical",line_width:130,text:[{"text":"🏎 Kart","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.kart run data modify entity @e[type=minecraft:text_display,tag=mg.h3_kart,limit=1] text set from storage mg:hall t3x.kart
summon minecraft:text_display -18.0 66.3 21.5 {Tags:["mg.hall","mg.h3_elyrace"],billboard:"vertical",line_width:130,text:[{"text":"🪽 Course d'élytres","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.elyrace run data modify entity @e[type=minecraft:text_display,tag=mg.h3_elyrace,limit=1] text set from storage mg:hall t3x.elyrace
summon minecraft:text_display -16.0 67.5 21.5 {Tags:["mg.hall","mg.h3_elytra"],billboard:"vertical",line_width:130,text:[{"text":"🪽 Élytra (3 modes)","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.elytra run data modify entity @e[type=minecraft:text_display,tag=mg.h3_elytra,limit=1] text set from storage mg:hall t3x.elytra
summon minecraft:text_display -58.0 66.3 30.5 {Tags:["mg.hall","mg.h3_telephone"],billboard:"vertical",line_width:130,text:[{"text":"📞 Téléphone","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.telephone run data modify entity @e[type=minecraft:text_display,tag=mg.h3_telephone,limit=1] text set from storage mg:hall t3x.telephone
summon minecraft:text_display -56.0 67.5 30.5 {Tags:["mg.hall","mg.h3_tron"],billboard:"vertical",line_width:130,text:[{"text":"⚡ Tron","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.tron run data modify entity @e[type=minecraft:text_display,tag=mg.h3_tron,limit=1] text set from storage mg:hall t3x.tron
summon minecraft:text_display -54.0 66.3 30.5 {Tags:["mg.hall","mg.h3_koth"],billboard:"vertical",line_width:130,text:[{"text":"👑 King of the Hill","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.koth run data modify entity @e[type=minecraft:text_display,tag=mg.h3_koth,limit=1] text set from storage mg:hall t3x.koth
summon minecraft:text_display -52.0 67.5 30.5 {Tags:["mg.hall","mg.h3_tower"],billboard:"vertical",line_width:130,text:[{"text":"🏰 The Towers","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.tower run data modify entity @e[type=minecraft:text_display,tag=mg.h3_tower,limit=1] text set from storage mg:hall t3x.tower
summon minecraft:text_display -50.0 66.3 30.5 {Tags:["mg.hall","mg.h3_convoy"],billboard:"vertical",line_width:130,text:[{"text":"🚚 Convoi","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.convoy run data modify entity @e[type=minecraft:text_display,tag=mg.h3_convoy,limit=1] text set from storage mg:hall t3x.convoy
summon minecraft:text_display -48.0 67.5 30.5 {Tags:["mg.hall","mg.h3_ctf"],billboard:"vertical",line_width:130,text:[{"text":"🚩 Capture the Flag","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.ctf run data modify entity @e[type=minecraft:text_display,tag=mg.h3_ctf,limit=1] text set from storage mg:hall t3x.ctf
summon minecraft:text_display -46.0 66.3 30.5 {Tags:["mg.hall","mg.h3_uhc"],billboard:"vertical",line_width:130,text:[{"text":"⛏ Mini UHC Run","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.uhc run data modify entity @e[type=minecraft:text_display,tag=mg.h3_uhc,limit=1] text set from storage mg:hall t3x.uhc
summon minecraft:text_display -44.0 67.5 30.5 {Tags:["mg.hall","mg.h3_hg"],billboard:"vertical",line_width:130,text:[{"text":"🏹 Mini Hunger Games","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.hg run data modify entity @e[type=minecraft:text_display,tag=mg.h3_hg,limit=1] text set from storage mg:hall t3x.hg
summon minecraft:text_display -42.0 66.3 30.5 {Tags:["mg.hall","mg.h3_prophunt"],billboard:"vertical",line_width:130,text:[{"text":"🎭 Prop Hunt","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.prophunt run data modify entity @e[type=minecraft:text_display,tag=mg.h3_prophunt,limit=1] text set from storage mg:hall t3x.prophunt
summon minecraft:text_display -40.0 67.5 30.5 {Tags:["mg.hall","mg.h3_zombies"],billboard:"vertical",line_width:130,text:[{"text":"🧟 Zombies","color":"dark_green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.zombies run data modify entity @e[type=minecraft:text_display,tag=mg.h3_zombies,limit=1] text set from storage mg:hall t3x.zombies
summon minecraft:text_display -38.0 66.3 30.5 {Tags:["mg.hall","mg.h3_infection"],billboard:"vertical",line_width:130,text:[{"text":"🧪 Infection","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.infection run data modify entity @e[type=minecraft:text_display,tag=mg.h3_infection,limit=1] text set from storage mg:hall t3x.infection
summon minecraft:text_display -36.0 67.5 30.5 {Tags:["mg.hall","mg.h3_bomber"],billboard:"vertical",line_width:130,text:[{"text":"💣 Bombardier","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.bomber run data modify entity @e[type=minecraft:text_display,tag=mg.h3_bomber,limit=1] text set from storage mg:hall t3x.bomber
summon minecraft:text_display -34.0 66.3 30.5 {Tags:["mg.hall","mg.h3_chameleon"],billboard:"vertical",line_width:130,text:[{"text":"🦎 Meccha Chameleon","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.chameleon run data modify entity @e[type=minecraft:text_display,tag=mg.h3_chameleon,limit=1] text set from storage mg:hall t3x.chameleon
summon minecraft:text_display -32.0 67.5 30.5 {Tags:["mg.hall","mg.h3_wii"],billboard:"vertical",line_width:130,text:[{"text":"🎾 Wii Sports","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.wii run data modify entity @e[type=minecraft:text_display,tag=mg.h3_wii,limit=1] text set from storage mg:hall t3x.wii
summon minecraft:text_display -30.0 66.3 30.5 {Tags:["mg.hall","mg.h3_soleil"],billboard:"vertical",line_width:130,text:[{"text":"🔴 1, 2, 3 Soleil","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.soleil run data modify entity @e[type=minecraft:text_display,tag=mg.h3_soleil,limit=1] text set from storage mg:hall t3x.soleil
summon minecraft:text_display -28.0 67.5 30.5 {Tags:["mg.hall","mg.h3_autotamp"],billboard:"vertical",line_width:130,text:[{"text":"🚗 Autos tamponneuses","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.autotamp run data modify entity @e[type=minecraft:text_display,tag=mg.h3_autotamp,limit=1] text set from storage mg:hall t3x.autotamp
summon minecraft:text_display -26.0 66.3 30.5 {Tags:["mg.hall","mg.h3_slimejump"],billboard:"vertical",line_width:130,text:[{"text":"🟩 Slime Jump","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.slimejump run data modify entity @e[type=minecraft:text_display,tag=mg.h3_slimejump,limit=1] text set from storage mg:hall t3x.slimejump
summon minecraft:text_display -24.0 67.5 30.5 {Tags:["mg.hall","mg.h3_lab"],billboard:"vertical",line_width:130,text:[{"text":"🙈 Labyrinthe aveugle","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.lab run data modify entity @e[type=minecraft:text_display,tag=mg.h3_lab,limit=1] text set from storage mg:hall t3x.lab
summon minecraft:text_display -22.0 66.3 30.5 {Tags:["mg.hall","mg.h3_master"],billboard:"vertical",line_width:130,text:[{"text":"👑 Master dit","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.master run data modify entity @e[type=minecraft:text_display,tag=mg.h3_master,limit=1] text set from storage mg:hall t3x.master
summon minecraft:text_display -20.0 67.5 30.5 {Tags:["mg.hall","mg.h3_murder"],billboard:"vertical",line_width:130,text:[{"text":"🔪 Murder Mystery","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.murder run data modify entity @e[type=minecraft:text_display,tag=mg.h3_murder,limit=1] text set from storage mg:hall t3x.murder
summon minecraft:text_display -18.0 66.3 30.5 {Tags:["mg.hall","mg.h3_bman"],billboard:"vertical",line_width:130,text:[{"text":"💣 Bomberman","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.bman run data modify entity @e[type=minecraft:text_display,tag=mg.h3_bman,limit=1] text set from storage mg:hall t3x.bman
summon minecraft:text_display -16.0 67.5 30.5 {Tags:["mg.hall","mg.h3_maze"],billboard:"vertical",line_width:130,text:[{"text":"🌀 Labyrinthe géant","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.maze run data modify entity @e[type=minecraft:text_display,tag=mg.h3_maze,limit=1] text set from storage mg:hall t3x.maze
data modify storage mg:hall v2 set value 1b
data modify storage mg:hall v3 set value 1b
data modify storage mg:hall v4 set value 1b
data modify storage mg:hall v5 set value 1b
data modify storage mg:hall v6 set value 1b
data modify storage mg:hall v7 set value 1b
data modify storage mg:hall v8 set value 1b
data modify storage mg:hall v9 set value 1b
data modify storage mg:hall v10 set value 1b
data modify storage mg:hall v11 set value 1b
data modify storage mg:hall v12 set value 1b
data modify storage mg:hall v13 set value 1b
data modify storage mg:hall v14 set value 1b
data modify storage mg:hall v15 set value 1b
data modify storage mg:hall v16 set value 1b
data modify storage mg:hall v17 set value 1b
data modify storage mg:hall v18 set value 1b
