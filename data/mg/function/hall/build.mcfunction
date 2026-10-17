# Jardin des champions (Hall des scores v16, à ciel ouvert, sud-ouest de la place) : construction + top 3 (généré par tools/hall/gen_hall.py)
# Chunks pas encore chargés (démarrage du serveur) : on réessaie dans 1 s, 60 fois au plus
execute store success score #hl mg.st unless block -58 300 18 minecraft:bedrock
execute if score #hl mg.st matches 1 store success score #hl mg.st unless block -14 300 33 minecraft:bedrock
execute if score #hl mg.st matches 0 run scoreboard players add #hlr mg.st 1
execute if score #hl mg.st matches 0 if score #hlr mg.st matches 60.. run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Hall des scores : chunks pas chargés, construction abandonnée (relance /function mg:hall/build).","color":"red"}]
execute if score #hl mg.st matches 0 if score #hlr mg.st matches 60.. run return run scoreboard players set #hlr mg.st 0
execute if score #hl mg.st matches 0 run return run schedule function mg:hall/build 20t
scoreboard players set #hlr mg.st 0
kill @e[tag=mg.hall]
execute unless data storage mg:hall v15 run function mg:hall/clear_old

# terrain dégagé (arbres, ancienne fontaine, bâtiment v15), sol, haies basses
fill -60 64 15 -6 84 36 minecraft:air
fill -60 62 15 -12 62 36 minecraft:dirt
fill -60 63 15 -12 63 36 minecraft:grass_block
fill -59 63 20 -6 63 22 minecraft:dirt_path
fill -59 63 32 -6 63 34 minecraft:dirt_path
fill -13 63 20 -6 63 34 minecraft:polished_andesite
fill -60 64 15 -12 64 15 minecraft:moss_block
fill -60 64 36 -12 64 36 minecraft:moss_block
fill -60 64 15 -60 64 36 minecraft:moss_block
fill -12 64 15 -12 64 36 minecraft:moss_block
fill -12 64 20 -12 64 34 minecraft:air
fill -60 64 27 -14 64 27 minecraft:moss_block
fill -60 64 35 -12 64 35 minecraft:moss_carpet
fill -57 64 16 -57 64 19 minecraft:moss_block
setblock -57 65 16 minecraft:lantern
fill -54 64 16 -54 64 19 minecraft:moss_block
setblock -54 65 16 minecraft:lantern
fill -51 64 16 -51 64 19 minecraft:moss_block
setblock -51 65 16 minecraft:lantern
fill -48 64 16 -48 64 19 minecraft:moss_block
setblock -48 65 16 minecraft:lantern
fill -45 64 16 -45 64 19 minecraft:moss_block
setblock -45 65 16 minecraft:lantern
fill -42 64 16 -42 64 19 minecraft:moss_block
setblock -42 65 16 minecraft:lantern
fill -39 64 16 -39 64 19 minecraft:moss_block
setblock -39 65 16 minecraft:lantern
fill -36 64 16 -36 64 19 minecraft:moss_block
setblock -36 65 16 minecraft:lantern
fill -33 64 16 -33 64 19 minecraft:moss_block
setblock -33 65 16 minecraft:lantern
fill -30 64 16 -30 64 19 minecraft:moss_block
setblock -30 65 16 minecraft:lantern
fill -27 64 16 -27 64 19 minecraft:moss_block
setblock -27 65 16 minecraft:lantern
fill -24 64 16 -24 64 19 minecraft:moss_block
setblock -24 65 16 minecraft:lantern
fill -21 64 16 -21 64 19 minecraft:moss_block
setblock -21 65 16 minecraft:lantern
fill -18 64 16 -18 64 19 minecraft:moss_block
setblock -18 65 16 minecraft:lantern
fill -15 64 16 -15 64 19 minecraft:moss_block
setblock -15 65 16 minecraft:lantern
fill -57 64 23 -57 64 26 minecraft:moss_block
setblock -57 65 26 minecraft:lantern
fill -54 64 23 -54 64 26 minecraft:moss_block
setblock -54 65 26 minecraft:lantern
fill -51 64 23 -51 64 26 minecraft:moss_block
setblock -51 65 26 minecraft:lantern
fill -48 64 23 -48 64 26 minecraft:moss_block
setblock -48 65 26 minecraft:lantern
fill -45 64 23 -45 64 26 minecraft:moss_block
setblock -45 65 26 minecraft:lantern
fill -42 64 23 -42 64 26 minecraft:moss_block
setblock -42 65 26 minecraft:lantern
fill -39 64 23 -39 64 26 minecraft:moss_block
setblock -39 65 26 minecraft:lantern
fill -36 64 23 -36 64 26 minecraft:moss_block
setblock -36 65 26 minecraft:lantern
fill -33 64 23 -33 64 26 minecraft:moss_block
setblock -33 65 26 minecraft:lantern
fill -30 64 23 -30 64 26 minecraft:moss_block
setblock -30 65 26 minecraft:lantern
fill -27 64 23 -27 64 26 minecraft:moss_block
setblock -27 65 26 minecraft:lantern
fill -24 64 23 -24 64 26 minecraft:moss_block
setblock -24 65 26 minecraft:lantern
fill -21 64 23 -21 64 26 minecraft:moss_block
setblock -21 65 26 minecraft:lantern
fill -18 64 23 -18 64 26 minecraft:moss_block
setblock -18 65 26 minecraft:lantern
fill -15 64 23 -15 64 26 minecraft:moss_block
setblock -15 65 26 minecraft:lantern
fill -57 64 28 -57 64 31 minecraft:moss_block
setblock -57 65 28 minecraft:lantern
fill -54 64 28 -54 64 31 minecraft:moss_block
setblock -54 65 28 minecraft:lantern
fill -51 64 28 -51 64 31 minecraft:moss_block
setblock -51 65 28 minecraft:lantern
fill -48 64 28 -48 64 31 minecraft:moss_block
setblock -48 65 28 minecraft:lantern
fill -45 64 28 -45 64 31 minecraft:moss_block
setblock -45 65 28 minecraft:lantern
fill -42 64 28 -42 64 31 minecraft:moss_block
setblock -42 65 28 minecraft:lantern
fill -39 64 28 -39 64 31 minecraft:moss_block
setblock -39 65 28 minecraft:lantern
fill -36 64 28 -36 64 31 minecraft:moss_block
setblock -36 65 28 minecraft:lantern
fill -33 64 28 -33 64 31 minecraft:moss_block
setblock -33 65 28 minecraft:lantern
fill -30 64 28 -30 64 31 minecraft:moss_block
setblock -30 65 28 minecraft:lantern
fill -27 64 28 -27 64 31 minecraft:moss_block
setblock -27 65 28 minecraft:lantern
fill -24 64 28 -24 64 31 minecraft:moss_block
setblock -24 65 28 minecraft:lantern
fill -21 64 28 -21 64 31 minecraft:moss_block
setblock -21 65 28 minecraft:lantern
fill -18 64 28 -18 64 31 minecraft:moss_block
setblock -18 65 28 minecraft:lantern
fill -15 64 28 -15 64 31 minecraft:moss_block
setblock -15 65 28 minecraft:lantern
fill -59 63 16 -58 63 19 minecraft:light_blue_concrete
fill -59 64 16 -58 64 16 minecraft:polished_andesite
setblock -59 65 16 minecraft:gold_block
setblock -58 65 16 minecraft:iron_block
setblock -59 64 17 minecraft:copper_block
fill -56 63 16 -55 63 19 minecraft:red_concrete
fill -56 64 16 -55 64 16 minecraft:polished_andesite
setblock -56 65 16 minecraft:gold_block
setblock -55 65 16 minecraft:iron_block
setblock -56 64 17 minecraft:copper_block
fill -53 63 16 -52 63 19 minecraft:yellow_concrete
fill -53 64 16 -52 64 16 minecraft:polished_andesite
setblock -53 65 16 minecraft:gold_block
setblock -52 65 16 minecraft:iron_block
setblock -53 64 17 minecraft:copper_block
fill -50 63 16 -49 63 19 minecraft:red_concrete
fill -50 64 16 -49 64 16 minecraft:polished_andesite
setblock -50 65 16 minecraft:gold_block
setblock -49 65 16 minecraft:iron_block
setblock -50 64 17 minecraft:copper_block
fill -47 63 16 -46 63 19 minecraft:white_concrete
fill -47 64 16 -46 64 16 minecraft:polished_andesite
setblock -47 65 16 minecraft:gold_block
setblock -46 65 16 minecraft:iron_block
setblock -47 64 17 minecraft:copper_block
fill -44 63 16 -43 63 19 minecraft:green_concrete
fill -44 64 16 -43 64 16 minecraft:polished_andesite
setblock -44 65 16 minecraft:gold_block
setblock -43 65 16 minecraft:iron_block
setblock -44 64 17 minecraft:copper_block
fill -41 63 16 -40 63 19 minecraft:yellow_concrete
fill -41 64 16 -40 64 16 minecraft:polished_andesite
setblock -41 65 16 minecraft:gold_block
setblock -40 65 16 minecraft:iron_block
setblock -41 64 17 minecraft:copper_block
fill -38 63 16 -37 63 19 minecraft:yellow_concrete
fill -38 64 16 -37 64 16 minecraft:polished_andesite
setblock -38 65 16 minecraft:gold_block
setblock -37 65 16 minecraft:iron_block
setblock -38 64 17 minecraft:copper_block
fill -35 63 16 -34 63 19 minecraft:light_blue_concrete
fill -35 64 16 -34 64 16 minecraft:polished_andesite
setblock -35 65 16 minecraft:gold_block
setblock -34 65 16 minecraft:iron_block
setblock -35 64 17 minecraft:copper_block
fill -32 63 16 -31 63 19 minecraft:yellow_concrete
fill -32 64 16 -31 64 16 minecraft:polished_andesite
setblock -32 65 16 minecraft:gold_block
setblock -31 65 16 minecraft:iron_block
setblock -32 64 17 minecraft:copper_block
fill -29 63 16 -28 63 19 minecraft:red_concrete
fill -29 64 16 -28 64 16 minecraft:polished_andesite
setblock -29 65 16 minecraft:gold_block
setblock -28 65 16 minecraft:iron_block
setblock -29 64 17 minecraft:copper_block
fill -26 63 16 -25 63 19 minecraft:magenta_concrete
fill -26 64 16 -25 64 16 minecraft:polished_andesite
setblock -26 65 16 minecraft:gold_block
setblock -25 65 16 minecraft:iron_block
setblock -26 64 17 minecraft:copper_block
fill -23 63 16 -22 63 19 minecraft:gray_concrete
fill -23 64 16 -22 64 16 minecraft:polished_andesite
setblock -23 65 16 minecraft:gold_block
setblock -22 65 16 minecraft:iron_block
setblock -23 64 17 minecraft:copper_block
fill -20 63 16 -19 63 19 minecraft:yellow_concrete
fill -20 64 16 -19 64 16 minecraft:polished_andesite
setblock -20 65 16 minecraft:gold_block
setblock -19 65 16 minecraft:iron_block
setblock -20 64 17 minecraft:copper_block
fill -17 63 16 -16 63 19 minecraft:light_blue_concrete
fill -17 64 16 -16 64 16 minecraft:polished_andesite
setblock -17 65 16 minecraft:gold_block
setblock -16 65 16 minecraft:iron_block
setblock -17 64 17 minecraft:copper_block
fill -59 63 23 -58 63 26 minecraft:yellow_concrete
fill -59 64 26 -58 64 26 minecraft:polished_andesite
setblock -59 65 26 minecraft:gold_block
setblock -58 65 26 minecraft:iron_block
setblock -59 64 25 minecraft:copper_block
fill -56 63 23 -55 63 26 minecraft:light_blue_concrete
fill -56 64 26 -55 64 26 minecraft:polished_andesite
setblock -56 65 26 minecraft:gold_block
setblock -55 65 26 minecraft:iron_block
setblock -56 64 25 minecraft:copper_block
fill -53 63 23 -52 63 26 minecraft:lime_concrete
fill -53 64 26 -52 64 26 minecraft:polished_andesite
setblock -53 65 26 minecraft:gold_block
setblock -52 65 26 minecraft:iron_block
setblock -53 64 25 minecraft:copper_block
fill -50 63 23 -49 63 26 minecraft:yellow_concrete
fill -50 64 26 -49 64 26 minecraft:polished_andesite
setblock -50 65 26 minecraft:gold_block
setblock -49 65 26 minecraft:iron_block
setblock -50 64 25 minecraft:copper_block
fill -47 63 23 -46 63 26 minecraft:red_concrete
fill -47 64 26 -46 64 26 minecraft:polished_andesite
setblock -47 65 26 minecraft:gold_block
setblock -46 65 26 minecraft:iron_block
setblock -47 64 25 minecraft:copper_block
fill -44 63 23 -43 63 26 minecraft:light_blue_concrete
fill -44 64 26 -43 64 26 minecraft:polished_andesite
setblock -44 65 26 minecraft:gold_block
setblock -43 65 26 minecraft:iron_block
setblock -44 64 25 minecraft:copper_block
fill -41 63 23 -40 63 26 minecraft:light_blue_concrete
fill -41 64 26 -40 64 26 minecraft:polished_andesite
setblock -41 65 26 minecraft:gold_block
setblock -40 65 26 minecraft:iron_block
setblock -41 64 25 minecraft:copper_block
fill -38 63 23 -37 63 26 minecraft:yellow_concrete
fill -38 64 26 -37 64 26 minecraft:polished_andesite
setblock -38 65 26 minecraft:gold_block
setblock -37 65 26 minecraft:iron_block
setblock -38 64 25 minecraft:copper_block
fill -35 63 23 -34 63 26 minecraft:light_blue_concrete
fill -35 64 26 -34 64 26 minecraft:polished_andesite
setblock -35 65 26 minecraft:gold_block
setblock -34 65 26 minecraft:iron_block
setblock -35 64 25 minecraft:copper_block
fill -32 63 23 -31 63 26 minecraft:yellow_concrete
fill -32 64 26 -31 64 26 minecraft:polished_andesite
setblock -32 65 26 minecraft:gold_block
setblock -31 65 26 minecraft:iron_block
setblock -32 64 25 minecraft:copper_block
fill -29 63 23 -28 63 26 minecraft:yellow_concrete
fill -29 64 26 -28 64 26 minecraft:polished_andesite
setblock -29 65 26 minecraft:gold_block
setblock -28 65 26 minecraft:iron_block
setblock -29 64 25 minecraft:copper_block
fill -26 63 23 -25 63 26 minecraft:yellow_concrete
fill -26 64 26 -25 64 26 minecraft:polished_andesite
setblock -26 65 26 minecraft:gold_block
setblock -25 65 26 minecraft:iron_block
setblock -26 64 25 minecraft:copper_block
fill -23 63 23 -22 63 26 minecraft:red_concrete
fill -23 64 26 -22 64 26 minecraft:polished_andesite
setblock -23 65 26 minecraft:gold_block
setblock -22 65 26 minecraft:iron_block
setblock -23 64 25 minecraft:copper_block
fill -20 63 23 -19 63 26 minecraft:yellow_concrete
fill -20 64 26 -19 64 26 minecraft:polished_andesite
setblock -20 65 26 minecraft:gold_block
setblock -19 65 26 minecraft:iron_block
setblock -20 64 25 minecraft:copper_block
fill -17 63 23 -16 63 26 minecraft:yellow_concrete
fill -17 64 26 -16 64 26 minecraft:polished_andesite
setblock -17 65 26 minecraft:gold_block
setblock -16 65 26 minecraft:iron_block
setblock -17 64 25 minecraft:copper_block
fill -59 63 28 -58 63 31 minecraft:yellow_concrete
fill -59 64 28 -58 64 28 minecraft:polished_andesite
setblock -59 65 28 minecraft:gold_block
setblock -58 65 28 minecraft:iron_block
setblock -59 64 29 minecraft:copper_block
fill -56 63 28 -55 63 31 minecraft:green_concrete
fill -56 64 28 -55 64 28 minecraft:polished_andesite
setblock -56 65 28 minecraft:gold_block
setblock -55 65 28 minecraft:iron_block
setblock -56 64 29 minecraft:copper_block
fill -53 63 28 -52 63 31 minecraft:lime_concrete
fill -53 64 28 -52 64 28 minecraft:polished_andesite
setblock -53 65 28 minecraft:gold_block
setblock -52 65 28 minecraft:iron_block
setblock -53 64 29 minecraft:copper_block
fill -50 63 28 -49 63 31 minecraft:red_concrete
fill -50 64 28 -49 64 28 minecraft:polished_andesite
setblock -50 65 28 minecraft:gold_block
setblock -49 65 28 minecraft:iron_block
setblock -50 64 29 minecraft:copper_block
fill -47 63 28 -46 63 31 minecraft:lime_concrete
fill -47 64 28 -46 64 28 minecraft:polished_andesite
setblock -47 65 28 minecraft:gold_block
setblock -46 65 28 minecraft:iron_block
setblock -47 64 29 minecraft:copper_block
fill -44 63 28 -43 63 31 minecraft:light_blue_concrete
fill -44 64 28 -43 64 28 minecraft:polished_andesite
setblock -44 65 28 minecraft:gold_block
setblock -43 65 28 minecraft:iron_block
setblock -44 64 29 minecraft:copper_block
fill -41 63 28 -40 63 31 minecraft:red_concrete
fill -41 64 28 -40 64 28 minecraft:polished_andesite
setblock -41 65 28 minecraft:gold_block
setblock -40 65 28 minecraft:iron_block
setblock -41 64 29 minecraft:copper_block
fill -38 63 28 -37 63 31 minecraft:light_blue_concrete
fill -38 64 28 -37 64 28 minecraft:polished_andesite
setblock -38 65 28 minecraft:gold_block
setblock -37 65 28 minecraft:iron_block
setblock -38 64 29 minecraft:copper_block
fill -35 63 28 -34 63 31 minecraft:lime_concrete
fill -35 64 28 -34 64 28 minecraft:polished_andesite
setblock -35 65 28 minecraft:gold_block
setblock -34 65 28 minecraft:iron_block
setblock -35 64 29 minecraft:copper_block
fill -32 63 28 -31 63 31 minecraft:magenta_concrete
fill -32 64 28 -31 64 28 minecraft:polished_andesite
setblock -32 65 28 minecraft:gold_block
setblock -31 65 28 minecraft:iron_block
setblock -32 64 29 minecraft:copper_block
fill -29 63 28 -28 63 31 minecraft:yellow_concrete
fill -29 64 28 -28 64 28 minecraft:polished_andesite
setblock -29 65 28 minecraft:gold_block
setblock -28 65 28 minecraft:iron_block
setblock -29 64 29 minecraft:copper_block
fill -26 63 28 -25 63 31 minecraft:red_concrete
fill -26 64 28 -25 64 28 minecraft:polished_andesite
setblock -26 65 28 minecraft:gold_block
setblock -25 65 28 minecraft:iron_block
setblock -26 64 29 minecraft:copper_block
fill -23 63 28 -22 63 31 minecraft:red_concrete
fill -23 64 28 -22 64 28 minecraft:polished_andesite
setblock -23 65 28 minecraft:gold_block
setblock -22 65 28 minecraft:iron_block
setblock -23 64 29 minecraft:copper_block
fill -20 63 28 -19 63 31 minecraft:magenta_concrete
fill -20 64 28 -19 64 28 minecraft:polished_andesite
setblock -20 65 28 minecraft:gold_block
setblock -19 65 28 minecraft:iron_block
setblock -20 64 29 minecraft:copper_block

# Plaza d'entrée (est) : piédestaux d'honneur
setblock -9 64 22 minecraft:emerald_block
setblock -9 64 27 minecraft:gold_block
setblock -9 64 32 minecraft:lapis_block

# Tampon de résolution des noms (invisible)
summon minecraft:item_display -8.5 64.5 27.5 {Tags:["mg.hall","mg.hallbuf"],item:{id:"minecraft:paper"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.001f,0.001f,0.001f]}}
summon minecraft:text_display -8.5 71.2 27.5 {Tags:["mg.hall"],billboard:"vertical",background:0,text:[{"text":"🏆 Jardin des champions","color":"gold","bold":true},{"text":"\n🥇 🥈 🥉 le top 3 de chaque jeu, dans les allées","color":"gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.6f,1.6f,1.6f]}}

# Piédestaux : objet qui tourne + plaque
summon minecraft:item_display -8.5 65.8 22.5 {Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:clock"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:item_display -8.5 65.8 27.5 {Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:totem_of_undying"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.8f,0.8f,0.8f]}}
summon minecraft:item_display -8.5 65.8 32.5 {Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:elytra"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.8f,0.8f,0.8f]}}

# Plaques d'honneur : texte par défaut, puis meneur enregistré s'il existe
summon minecraft:text_display -8.5 66.7 22.5 {Tags:["mg.hall","mg.h_stp"],billboard:"vertical",line_width:115,text:[{"text":"▶ Le plus assidu","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute if data storage mg:hall e.stp run data modify entity @e[type=minecraft:text_display,tag=mg.h_stp,limit=1] text set from storage mg:hall e.stp
summon minecraft:text_display -8.5 66.7 27.5 {Tags:["mg.hall","mg.h_wins"],billboard:"vertical",line_width:115,text:[{"text":"👑 Champion des mini-jeux","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute if data storage mg:hall e.wins run data modify entity @e[type=minecraft:text_display,tag=mg.h_wins,limit=1] text set from storage mg:hall e.wins
summon minecraft:text_display -8.5 66.7 32.5 {Tags:["mg.hall","mg.h_ely"],billboard:"vertical",line_width:115,text:[{"text":"🪽 Record petit parcours d'élytra","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute if data storage mg:hall e.ely run data modify entity @e[type=minecraft:text_display,tag=mg.h_ely,limit=1] text set from storage mg:hall e.ely
summon minecraft:text_display -8.5 68.1 32.5 {Tags:["mg.hall","mg.h_ely2"],billboard:"vertical",line_width:115,text:[{"text":"🪽 Record grand parcours d'élytra","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute if data storage mg:hall e.ely2 run data modify entity @e[type=minecraft:text_display,tag=mg.h_ely2,limit=1] text set from storage mg:hall e.ely2
summon minecraft:text_display -8.5 69.5 32.5 {Tags:["mg.hall","mg.h_elyg"],billboard:"vertical",line_width:115,text:[{"text":"🪽 Record Élytra : course","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
execute if data storage mg:hall e.elyg run data modify entity @e[type=minecraft:text_display,tag=mg.h_elyg,limit=1] text set from storage mg:hall e.elyg
summon minecraft:text_display -8.5 69.4 27.5 {Tags:["mg.hall","mg.h_gen"],billboard:"vertical",line_width:200,text:[{"text":"🏅 Meilleur niveau général","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.1f,1.1f,1.1f]}}
execute if data storage mg:hall e.gen run data modify entity @e[type=minecraft:text_display,tag=mg.h_gen,limit=1] text set from storage mg:hall e.gen

# Stands : top 3 de chaque jeu (texte par défaut, puis top 3 enregistré)
summon minecraft:text_display -58.0 66.4 16.5 {Tags:["mg.hall","mg.h3_spleef"],billboard:"vertical",line_width:120,text:[{"text":"❄ Spleef","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.spleef run data modify entity @e[type=minecraft:text_display,tag=mg.h3_spleef,limit=1] text set from storage mg:hall t3x.spleef
summon minecraft:text_display -55.0 66.4 16.5 {Tags:["mg.hall","mg.h3_tntrun"],billboard:"vertical",line_width:120,text:[{"text":"✷ TNT Run","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.tntrun run data modify entity @e[type=minecraft:text_display,tag=mg.h3_tntrun,limit=1] text set from storage mg:hall t3x.tntrun
summon minecraft:text_display -52.0 66.4 16.5 {Tags:["mg.hall","mg.h3_pvp"],billboard:"vertical",line_width:120,text:[{"text":"⚔ PvP","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.pvp run data modify entity @e[type=minecraft:text_display,tag=mg.h3_pvp,limit=1] text set from storage mg:hall t3x.pvp
summon minecraft:text_display -49.0 66.4 16.5 {Tags:["mg.hall","mg.h3_bedwars"],billboard:"vertical",line_width:120,text:[{"text":"🛏 Bedwars","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.bedwars run data modify entity @e[type=minecraft:text_display,tag=mg.h3_bedwars,limit=1] text set from storage mg:hall t3x.bedwars
summon minecraft:text_display -46.0 66.4 16.5 {Tags:["mg.hall","mg.h3_sheepwar"],billboard:"vertical",line_width:120,text:[{"text":"🐑 Sheep War","color":"white","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.sheepwar run data modify entity @e[type=minecraft:text_display,tag=mg.h3_sheepwar,limit=1] text set from storage mg:hall t3x.sheepwar
summon minecraft:text_display -43.0 66.4 16.5 {Tags:["mg.hall","mg.h3_mobarena"],billboard:"vertical",line_width:120,text:[{"text":"☠ Mob Arena","color":"dark_green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.mobarena run data modify entity @e[type=minecraft:text_display,tag=mg.h3_mobarena,limit=1] text set from storage mg:hall t3x.mobarena
summon minecraft:text_display -40.0 66.4 16.5 {Tags:["mg.hall","mg.h3_splegg"],billboard:"vertical",line_width:120,text:[{"text":"❍ Splegg","color":"yellow","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.splegg run data modify entity @e[type=minecraft:text_display,tag=mg.h3_splegg,limit=1] text set from storage mg:hall t3x.splegg
summon minecraft:text_display -37.0 66.4 16.5 {Tags:["mg.hall","mg.h3_sumo"],billboard:"vertical",line_width:120,text:[{"text":"✊ Sumo","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.sumo run data modify entity @e[type=minecraft:text_display,tag=mg.h3_sumo,limit=1] text set from storage mg:hall t3x.sumo
summon minecraft:text_display -34.0 66.4 16.5 {Tags:["mg.hall","mg.h3_dropper"],billboard:"vertical",line_width:120,text:[{"text":"⬇ Dropper","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.dropper run data modify entity @e[type=minecraft:text_display,tag=mg.h3_dropper,limit=1] text set from storage mg:hall t3x.dropper
summon minecraft:text_display -31.0 66.4 16.5 {Tags:["mg.hall","mg.h3_oitc"],billboard:"vertical",line_width:120,text:[{"text":"➶ One in the Chamber","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.oitc run data modify entity @e[type=minecraft:text_display,tag=mg.h3_oitc,limit=1] text set from storage mg:hall t3x.oitc
summon minecraft:text_display -28.0 66.4 16.5 {Tags:["mg.hall","mg.h3_tnttag"],billboard:"vertical",line_width:120,text:[{"text":"✹ TNT Tag","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.tnttag run data modify entity @e[type=minecraft:text_display,tag=mg.h3_tnttag,limit=1] text set from storage mg:hall t3x.tnttag
summon minecraft:text_display -25.0 66.4 16.5 {Tags:["mg.hall","mg.h3_blockparty"],billboard:"vertical",line_width:120,text:[{"text":"▦ Block Party","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.blockparty run data modify entity @e[type=minecraft:text_display,tag=mg.h3_blockparty,limit=1] text set from storage mg:hall t3x.blockparty
summon minecraft:text_display -22.0 66.4 16.5 {Tags:["mg.hall","mg.h3_anvil"],billboard:"vertical",line_width:120,text:[{"text":"⚓ Pluie d'enclumes","color":"gray","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.anvil run data modify entity @e[type=minecraft:text_display,tag=mg.h3_anvil,limit=1] text set from storage mg:hall t3x.anvil
summon minecraft:text_display -19.0 66.4 16.5 {Tags:["mg.hall","mg.h3_turf"],billboard:"vertical",line_width:120,text:[{"text":"▮ Turf Wars","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.turf run data modify entity @e[type=minecraft:text_display,tag=mg.h3_turf,limit=1] text set from storage mg:hall t3x.turf
summon minecraft:text_display -16.0 66.4 16.5 {Tags:["mg.hall","mg.h3_quake"],billboard:"vertical",line_width:120,text:[{"text":"⚡ Quakecraft","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.quake run data modify entity @e[type=minecraft:text_display,tag=mg.h3_quake,limit=1] text set from storage mg:hall t3x.quake
summon minecraft:text_display -58.0 66.4 26.5 {Tags:["mg.hall","mg.h3_paintball"],billboard:"vertical",line_width:120,text:[{"text":"▓ Paintball","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.paintball run data modify entity @e[type=minecraft:text_display,tag=mg.h3_paintball,limit=1] text set from storage mg:hall t3x.paintball
summon minecraft:text_display -55.0 66.4 26.5 {Tags:["mg.hall","mg.h3_icerace"],billboard:"vertical",line_width:120,text:[{"text":"⛵ Course de bateaux","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.icerace run data modify entity @e[type=minecraft:text_display,tag=mg.h3_icerace,limit=1] text set from storage mg:hall t3x.icerace
summon minecraft:text_display -52.0 66.4 26.5 {Tags:["mg.hall","mg.h3_bb"],billboard:"vertical",line_width:120,text:[{"text":"✎ Build Battle","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.bb run data modify entity @e[type=minecraft:text_display,tag=mg.h3_bb,limit=1] text set from storage mg:hall t3x.bb
summon minecraft:text_display -49.0 66.4 26.5 {Tags:["mg.hall","mg.h3_party"],billboard:"vertical",line_width:120,text:[{"text":"★ Mini Party","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.party run data modify entity @e[type=minecraft:text_display,tag=mg.h3_party,limit=1] text set from storage mg:hall t3x.party
summon minecraft:text_display -46.0 66.4 26.5 {Tags:["mg.hall","mg.h3_kart"],billboard:"vertical",line_width:120,text:[{"text":"🏎 Kart","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.kart run data modify entity @e[type=minecraft:text_display,tag=mg.h3_kart,limit=1] text set from storage mg:hall t3x.kart
summon minecraft:text_display -43.0 66.4 26.5 {Tags:["mg.hall","mg.h3_elyrace"],billboard:"vertical",line_width:120,text:[{"text":"🪽 Course d'élytres","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.elyrace run data modify entity @e[type=minecraft:text_display,tag=mg.h3_elyrace,limit=1] text set from storage mg:hall t3x.elyrace
summon minecraft:text_display -40.0 66.4 26.5 {Tags:["mg.hall","mg.h3_elytra"],billboard:"vertical",line_width:120,text:[{"text":"🪽 Élytra (3 modes)","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.elytra run data modify entity @e[type=minecraft:text_display,tag=mg.h3_elytra,limit=1] text set from storage mg:hall t3x.elytra
summon minecraft:text_display -37.0 66.4 26.5 {Tags:["mg.hall","mg.h3_telephone"],billboard:"vertical",line_width:120,text:[{"text":"📞 Téléphone","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.telephone run data modify entity @e[type=minecraft:text_display,tag=mg.h3_telephone,limit=1] text set from storage mg:hall t3x.telephone
summon minecraft:text_display -34.0 66.4 26.5 {Tags:["mg.hall","mg.h3_tron"],billboard:"vertical",line_width:120,text:[{"text":"⚡ Tron","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.tron run data modify entity @e[type=minecraft:text_display,tag=mg.h3_tron,limit=1] text set from storage mg:hall t3x.tron
summon minecraft:text_display -31.0 66.4 26.5 {Tags:["mg.hall","mg.h3_koth"],billboard:"vertical",line_width:120,text:[{"text":"👑 King of the Hill","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.koth run data modify entity @e[type=minecraft:text_display,tag=mg.h3_koth,limit=1] text set from storage mg:hall t3x.koth
summon minecraft:text_display -28.0 66.4 26.5 {Tags:["mg.hall","mg.h3_tower"],billboard:"vertical",line_width:120,text:[{"text":"🏰 The Towers","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.tower run data modify entity @e[type=minecraft:text_display,tag=mg.h3_tower,limit=1] text set from storage mg:hall t3x.tower
summon minecraft:text_display -25.0 66.4 26.5 {Tags:["mg.hall","mg.h3_convoy"],billboard:"vertical",line_width:120,text:[{"text":"🚚 Convoi","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.convoy run data modify entity @e[type=minecraft:text_display,tag=mg.h3_convoy,limit=1] text set from storage mg:hall t3x.convoy
summon minecraft:text_display -22.0 66.4 26.5 {Tags:["mg.hall","mg.h3_ctf"],billboard:"vertical",line_width:120,text:[{"text":"🚩 Capture the Flag","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.ctf run data modify entity @e[type=minecraft:text_display,tag=mg.h3_ctf,limit=1] text set from storage mg:hall t3x.ctf
summon minecraft:text_display -19.0 66.4 26.5 {Tags:["mg.hall","mg.h3_uhc"],billboard:"vertical",line_width:120,text:[{"text":"⛏ Mini UHC Run","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.uhc run data modify entity @e[type=minecraft:text_display,tag=mg.h3_uhc,limit=1] text set from storage mg:hall t3x.uhc
summon minecraft:text_display -16.0 66.4 26.5 {Tags:["mg.hall","mg.h3_hg"],billboard:"vertical",line_width:120,text:[{"text":"🏹 Mini Hunger Games","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.hg run data modify entity @e[type=minecraft:text_display,tag=mg.h3_hg,limit=1] text set from storage mg:hall t3x.hg
summon minecraft:text_display -58.0 66.4 28.5 {Tags:["mg.hall","mg.h3_prophunt"],billboard:"vertical",line_width:120,text:[{"text":"🎭 Prop Hunt","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.prophunt run data modify entity @e[type=minecraft:text_display,tag=mg.h3_prophunt,limit=1] text set from storage mg:hall t3x.prophunt
summon minecraft:text_display -55.0 66.4 28.5 {Tags:["mg.hall","mg.h3_zombies"],billboard:"vertical",line_width:120,text:[{"text":"🧟 Zombies","color":"dark_green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.zombies run data modify entity @e[type=minecraft:text_display,tag=mg.h3_zombies,limit=1] text set from storage mg:hall t3x.zombies
summon minecraft:text_display -52.0 66.4 28.5 {Tags:["mg.hall","mg.h3_infection"],billboard:"vertical",line_width:120,text:[{"text":"🧪 Infection","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.infection run data modify entity @e[type=minecraft:text_display,tag=mg.h3_infection,limit=1] text set from storage mg:hall t3x.infection
summon minecraft:text_display -49.0 66.4 28.5 {Tags:["mg.hall","mg.h3_bomber"],billboard:"vertical",line_width:120,text:[{"text":"💣 Bombardier","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.bomber run data modify entity @e[type=minecraft:text_display,tag=mg.h3_bomber,limit=1] text set from storage mg:hall t3x.bomber
summon minecraft:text_display -46.0 66.4 28.5 {Tags:["mg.hall","mg.h3_chameleon"],billboard:"vertical",line_width:120,text:[{"text":"🦎 Meccha Chameleon","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.chameleon run data modify entity @e[type=minecraft:text_display,tag=mg.h3_chameleon,limit=1] text set from storage mg:hall t3x.chameleon
summon minecraft:text_display -43.0 66.4 28.5 {Tags:["mg.hall","mg.h3_wii"],billboard:"vertical",line_width:120,text:[{"text":"🎾 Wii Sports","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.wii run data modify entity @e[type=minecraft:text_display,tag=mg.h3_wii,limit=1] text set from storage mg:hall t3x.wii
summon minecraft:text_display -40.0 66.4 28.5 {Tags:["mg.hall","mg.h3_soleil"],billboard:"vertical",line_width:120,text:[{"text":"🔴 1, 2, 3 Soleil","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.soleil run data modify entity @e[type=minecraft:text_display,tag=mg.h3_soleil,limit=1] text set from storage mg:hall t3x.soleil
summon minecraft:text_display -37.0 66.4 28.5 {Tags:["mg.hall","mg.h3_autotamp"],billboard:"vertical",line_width:120,text:[{"text":"🚗 Autos tamponneuses","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.autotamp run data modify entity @e[type=minecraft:text_display,tag=mg.h3_autotamp,limit=1] text set from storage mg:hall t3x.autotamp
summon minecraft:text_display -34.0 66.4 28.5 {Tags:["mg.hall","mg.h3_slimejump"],billboard:"vertical",line_width:120,text:[{"text":"🟩 Slime Jump","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.slimejump run data modify entity @e[type=minecraft:text_display,tag=mg.h3_slimejump,limit=1] text set from storage mg:hall t3x.slimejump
summon minecraft:text_display -31.0 66.4 28.5 {Tags:["mg.hall","mg.h3_lab"],billboard:"vertical",line_width:120,text:[{"text":"🙈 Labyrinthe aveugle","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.lab run data modify entity @e[type=minecraft:text_display,tag=mg.h3_lab,limit=1] text set from storage mg:hall t3x.lab
summon minecraft:text_display -28.0 66.4 28.5 {Tags:["mg.hall","mg.h3_master"],billboard:"vertical",line_width:120,text:[{"text":"👑 Master dit","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.master run data modify entity @e[type=minecraft:text_display,tag=mg.h3_master,limit=1] text set from storage mg:hall t3x.master
summon minecraft:text_display -25.0 66.4 28.5 {Tags:["mg.hall","mg.h3_murder"],billboard:"vertical",line_width:120,text:[{"text":"🔪 Murder Mystery","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.murder run data modify entity @e[type=minecraft:text_display,tag=mg.h3_murder,limit=1] text set from storage mg:hall t3x.murder
summon minecraft:text_display -22.0 66.4 28.5 {Tags:["mg.hall","mg.h3_bman"],billboard:"vertical",line_width:120,text:[{"text":"💣 Bomberman","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
execute if data storage mg:hall t3x.bman run data modify entity @e[type=minecraft:text_display,tag=mg.h3_bman,limit=1] text set from storage mg:hall t3x.bman
summon minecraft:text_display -19.0 66.4 28.5 {Tags:["mg.hall","mg.h3_maze"],billboard:"vertical",line_width:120,text:[{"text":"🌀 Labyrinthe géant","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.5f,0.5f,0.5f]}}
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
