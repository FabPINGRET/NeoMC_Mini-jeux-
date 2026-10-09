# Hall des scores (sud-ouest de la place) : construction + restauration des meneurs
# Chunks du hall pas encore chargés (démarrage du serveur) : on réessaie dans 1 s, 60 fois au plus (motif de mg:dropadv/loaded_all :
# « unless block … bedrock » ne réussit que si le chunk est chargé, il n'y a jamais de bedrock à y 300). #hl = 1 : les 2 chunks sont chargés
execute store success score #hl mg.st unless block -22 300 24 minecraft:bedrock
execute if score #hl mg.st matches 1 store success score #hl mg.st unless block -8 300 24 minecraft:bedrock
execute if score #hl mg.st matches 0 run scoreboard players add #hlr mg.st 1
execute if score #hl mg.st matches 0 if score #hlr mg.st matches 60.. run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Hall des scores : chunks pas chargés, construction abandonnée (relance /function mg:hall/build).","color":"red"}]
execute if score #hl mg.st matches 0 if score #hlr mg.st matches 60.. run return run scoreboard players set #hlr mg.st 0
execute if score #hl mg.st matches 0 run return run schedule function mg:hall/build 20t
scoreboard players set #hlr mg.st 0
kill @e[tag=mg.hall]

fill -24 63 21 -6 63 35 minecraft:smooth_quartz
fill -24 64 21 -6 74 35 minecraft:air
fill -24 64 35 -6 69 35 minecraft:stone_bricks
setblock -24 66 35 minecraft:mossy_stone_bricks
setblock -23 67 35 minecraft:mossy_stone_bricks
setblock -22 64 35 minecraft:cracked_stone_bricks
setblock -22 68 35 minecraft:mossy_stone_bricks
setblock -21 65 35 minecraft:cracked_stone_bricks
setblock -21 69 35 minecraft:mossy_stone_bricks
setblock -20 66 35 minecraft:cracked_stone_bricks
setblock -19 67 35 minecraft:cracked_stone_bricks
setblock -18 68 35 minecraft:cracked_stone_bricks
setblock -17 69 35 minecraft:cracked_stone_bricks
setblock -16 64 35 minecraft:mossy_stone_bricks
setblock -15 65 35 minecraft:mossy_stone_bricks
setblock -14 66 35 minecraft:mossy_stone_bricks
setblock -13 67 35 minecraft:mossy_stone_bricks
setblock -12 64 35 minecraft:cracked_stone_bricks
setblock -12 68 35 minecraft:mossy_stone_bricks
setblock -11 65 35 minecraft:cracked_stone_bricks
setblock -11 69 35 minecraft:mossy_stone_bricks
setblock -10 66 35 minecraft:cracked_stone_bricks
setblock -9 67 35 minecraft:cracked_stone_bricks
setblock -8 68 35 minecraft:cracked_stone_bricks
setblock -7 69 35 minecraft:cracked_stone_bricks
setblock -6 64 35 minecraft:mossy_stone_bricks
fill -24 64 35 -6 64 35 minecraft:mossy_stone_bricks
fill -24 70 35 -6 70 35 minecraft:stone_brick_slab[type=bottom]
fill -16 63 21 -15 63 34 minecraft:red_wool
fill -20 64 15 -11 74 20 minecraft:air replace #minecraft:logs
fill -20 64 15 -11 74 20 minecraft:air replace #minecraft:leaves
fill -22 64 28 -20 64 28 minecraft:dark_oak_stairs[facing=south]
fill -10 64 28 -8 64 28 minecraft:dark_oak_stairs[facing=south]
fill -22 64 25 -20 64 25 minecraft:dark_oak_stairs[facing=south]
fill -10 64 25 -8 64 25 minecraft:dark_oak_stairs[facing=south]
fill -23 63 22 -23 63 34 minecraft:gold_block
fill -7 63 22 -7 63 34 minecraft:gold_block
setblock -19 64 25 minecraft:emerald_block
setblock -16 64 25 minecraft:gold_block
setblock -13 64 25 minecraft:lapis_block

# Tampon de résolution des noms (invisible)
summon minecraft:item_display -15.5 64.5 25.5 {Tags:["mg.hall","mg.hallbuf"],item:{id:"minecraft:paper"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.001f,0.001f,0.001f]}}
summon minecraft:text_display -15.5 71.4 34.6 {Tags:["mg.hall"],billboard:"center",background:0,text:[{"text":"🏆 Hall des scores","color":"gold","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2.2f,2.2f,2.2f]}}

# Piédestaux : objet qui tourne + plaque
summon minecraft:item_display -18.5 65.8 25.5 {Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:clock"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
summon minecraft:item_display -15.5 65.8 25.5 {Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:totem_of_undying"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
summon minecraft:item_display -12.5 65.8 25.5 {Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:elytra"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}

# Plaques : texte par défaut, puis meneur enregistré s'il existe
summon minecraft:text_display -18.5 66.9 25.5 {Tags:["mg.hall","mg.h_stp"],billboard:"vertical",text:[{"text":"▶ Le plus assidu","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall e.stp run data modify entity @e[type=minecraft:text_display,tag=mg.h_stp,limit=1] text set from storage mg:hall e.stp
summon minecraft:text_display -15.5 66.9 25.5 {Tags:["mg.hall","mg.h_wins"],billboard:"vertical",text:[{"text":"👑 Champion des mini-jeux","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall e.wins run data modify entity @e[type=minecraft:text_display,tag=mg.h_wins,limit=1] text set from storage mg:hall e.wins
summon minecraft:text_display -12.5 66.9 25.5 {Tags:["mg.hall","mg.h_ely"],billboard:"vertical",text:[{"text":"🪽 Record petit parcours d'élytra","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall e.ely run data modify entity @e[type=minecraft:text_display,tag=mg.h_ely,limit=1] text set from storage mg:hall e.ely
summon minecraft:text_display -12.5 67.6 25.5 {Tags:["mg.hall","mg.h_ely2"],billboard:"vertical",text:[{"text":"🪽 Record grand parcours d'élytra","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall e.ely2 run data modify entity @e[type=minecraft:text_display,tag=mg.h_ely2,limit=1] text set from storage mg:hall e.ely2
summon minecraft:text_display -12.5 68.3 25.5 {Tags:["mg.hall","mg.h_elyg"],billboard:"vertical",text:[{"text":"🪽 Record Élytra : course","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.55f,0.55f,0.55f]}}
execute if data storage mg:hall e.elyg run data modify entity @e[type=minecraft:text_display,tag=mg.h_elyg,limit=1] text set from storage mg:hall e.elyg
summon minecraft:text_display -15.5 70.15 34.3 {Tags:["mg.hall","mg.h_gen"],billboard:"vertical",text:[{"text":"🏅 Meilleur niveau général","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.62f,0.62f,0.62f]}}
execute if data storage mg:hall e.gen run data modify entity @e[type=minecraft:text_display,tag=mg.h_gen,limit=1] text set from storage mg:hall e.gen
summon minecraft:text_display -23.0 68.6 34.2 {Tags:["mg.hall","mg.h_spleef"],billboard:"vertical",text:[{"text":"❄ Spleef","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.spleef run data modify entity @e[type=minecraft:text_display,tag=mg.h_spleef,limit=1] text set from storage mg:hall e.spleef
summon minecraft:text_display -21.0 68.6 34.2 {Tags:["mg.hall","mg.h_tntrun"],billboard:"vertical",text:[{"text":"✷ TNT Run","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.tntrun run data modify entity @e[type=minecraft:text_display,tag=mg.h_tntrun,limit=1] text set from storage mg:hall e.tntrun
summon minecraft:text_display -19.0 68.6 34.2 {Tags:["mg.hall","mg.h_pvp"],billboard:"vertical",text:[{"text":"⚔ PvP","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.pvp run data modify entity @e[type=minecraft:text_display,tag=mg.h_pvp,limit=1] text set from storage mg:hall e.pvp
summon minecraft:text_display -17.0 68.6 34.2 {Tags:["mg.hall","mg.h_bedwars"],billboard:"vertical",text:[{"text":"🛏 Bedwars","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.bedwars run data modify entity @e[type=minecraft:text_display,tag=mg.h_bedwars,limit=1] text set from storage mg:hall e.bedwars
summon minecraft:text_display -15.0 68.6 34.2 {Tags:["mg.hall","mg.h_sheepwar"],billboard:"vertical",text:[{"text":"🐑 Sheep War","color":"white","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.sheepwar run data modify entity @e[type=minecraft:text_display,tag=mg.h_sheepwar,limit=1] text set from storage mg:hall e.sheepwar
summon minecraft:text_display -13.0 68.6 34.2 {Tags:["mg.hall","mg.h_mobarena"],billboard:"vertical",text:[{"text":"☠ Mob Arena","color":"dark_green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.mobarena run data modify entity @e[type=minecraft:text_display,tag=mg.h_mobarena,limit=1] text set from storage mg:hall e.mobarena
summon minecraft:text_display -11.0 68.6 34.2 {Tags:["mg.hall","mg.h_splegg"],billboard:"vertical",text:[{"text":"❍ Splegg","color":"yellow","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.splegg run data modify entity @e[type=minecraft:text_display,tag=mg.h_splegg,limit=1] text set from storage mg:hall e.splegg
summon minecraft:text_display -9.0 68.6 34.2 {Tags:["mg.hall","mg.h_sumo"],billboard:"vertical",text:[{"text":"✊ Sumo","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.sumo run data modify entity @e[type=minecraft:text_display,tag=mg.h_sumo,limit=1] text set from storage mg:hall e.sumo
summon minecraft:text_display -7.0 68.6 34.2 {Tags:["mg.hall","mg.h_dropper"],billboard:"vertical",text:[{"text":"⬇ Dropper","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.dropper run data modify entity @e[type=minecraft:text_display,tag=mg.h_dropper,limit=1] text set from storage mg:hall e.dropper
summon minecraft:text_display -23.0 67.4 34.2 {Tags:["mg.hall","mg.h_oitc"],billboard:"vertical",text:[{"text":"➶ One in the Chamber","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.oitc run data modify entity @e[type=minecraft:text_display,tag=mg.h_oitc,limit=1] text set from storage mg:hall e.oitc
summon minecraft:text_display -21.0 67.4 34.2 {Tags:["mg.hall","mg.h_tnttag"],billboard:"vertical",text:[{"text":"✹ TNT Tag","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.tnttag run data modify entity @e[type=minecraft:text_display,tag=mg.h_tnttag,limit=1] text set from storage mg:hall e.tnttag
summon minecraft:text_display -19.0 67.4 34.2 {Tags:["mg.hall","mg.h_blockparty"],billboard:"vertical",text:[{"text":"▦ Block Party","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.blockparty run data modify entity @e[type=minecraft:text_display,tag=mg.h_blockparty,limit=1] text set from storage mg:hall e.blockparty
summon minecraft:text_display -17.0 67.4 34.2 {Tags:["mg.hall","mg.h_anvil"],billboard:"vertical",text:[{"text":"⚓ Pluie d'enclumes","color":"gray","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.anvil run data modify entity @e[type=minecraft:text_display,tag=mg.h_anvil,limit=1] text set from storage mg:hall e.anvil
summon minecraft:text_display -15.0 67.4 34.2 {Tags:["mg.hall","mg.h_turf"],billboard:"vertical",text:[{"text":"▮ Turf Wars","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.turf run data modify entity @e[type=minecraft:text_display,tag=mg.h_turf,limit=1] text set from storage mg:hall e.turf
summon minecraft:text_display -13.0 67.4 34.2 {Tags:["mg.hall","mg.h_quake"],billboard:"vertical",text:[{"text":"⚡ Quakecraft","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.quake run data modify entity @e[type=minecraft:text_display,tag=mg.h_quake,limit=1] text set from storage mg:hall e.quake
summon minecraft:text_display -11.0 67.4 34.2 {Tags:["mg.hall","mg.h_paintball"],billboard:"vertical",text:[{"text":"▓ Paintball","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.paintball run data modify entity @e[type=minecraft:text_display,tag=mg.h_paintball,limit=1] text set from storage mg:hall e.paintball
summon minecraft:text_display -9.0 67.4 34.2 {Tags:["mg.hall","mg.h_icerace"],billboard:"vertical",text:[{"text":"⛵ Course de bateaux","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.icerace run data modify entity @e[type=minecraft:text_display,tag=mg.h_icerace,limit=1] text set from storage mg:hall e.icerace
summon minecraft:text_display -7.0 67.4 34.2 {Tags:["mg.hall","mg.h_bb"],billboard:"vertical",text:[{"text":"✎ Build Battle","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.bb run data modify entity @e[type=minecraft:text_display,tag=mg.h_bb,limit=1] text set from storage mg:hall e.bb
summon minecraft:text_display -23.0 66.2 34.2 {Tags:["mg.hall","mg.h_party"],billboard:"vertical",text:[{"text":"★ Mini Party","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.party run data modify entity @e[type=minecraft:text_display,tag=mg.h_party,limit=1] text set from storage mg:hall e.party
summon minecraft:text_display -21.0 66.2 34.2 {Tags:["mg.hall","mg.h_kart"],billboard:"vertical",text:[{"text":"🏎 Kart","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.kart run data modify entity @e[type=minecraft:text_display,tag=mg.h_kart,limit=1] text set from storage mg:hall e.kart
summon minecraft:text_display -19.0 66.2 34.2 {Tags:["mg.hall","mg.h_elyrace"],billboard:"vertical",text:[{"text":"🪽 Course d'élytres","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.elyrace run data modify entity @e[type=minecraft:text_display,tag=mg.h_elyrace,limit=1] text set from storage mg:hall e.elyrace
summon minecraft:text_display -17.0 66.2 34.2 {Tags:["mg.hall","mg.h_elytra"],billboard:"vertical",text:[{"text":"🪽 Élytra (3 modes)","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.elytra run data modify entity @e[type=minecraft:text_display,tag=mg.h_elytra,limit=1] text set from storage mg:hall e.elytra
summon minecraft:text_display -15.0 66.2 34.2 {Tags:["mg.hall","mg.h_telephone"],billboard:"vertical",text:[{"text":"📞 Téléphone","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.telephone run data modify entity @e[type=minecraft:text_display,tag=mg.h_telephone,limit=1] text set from storage mg:hall e.telephone
summon minecraft:text_display -13.0 66.2 34.2 {Tags:["mg.hall","mg.h_tron"],billboard:"vertical",text:[{"text":"⚡ Tron","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.tron run data modify entity @e[type=minecraft:text_display,tag=mg.h_tron,limit=1] text set from storage mg:hall e.tron
summon minecraft:text_display -11.0 66.2 34.2 {Tags:["mg.hall","mg.h_koth"],billboard:"vertical",text:[{"text":"👑 King of the Hill","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.koth run data modify entity @e[type=minecraft:text_display,tag=mg.h_koth,limit=1] text set from storage mg:hall e.koth
summon minecraft:text_display -9.0 66.2 34.2 {Tags:["mg.hall","mg.h_tower"],billboard:"vertical",text:[{"text":"🏰 The Towers","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.tower run data modify entity @e[type=minecraft:text_display,tag=mg.h_tower,limit=1] text set from storage mg:hall e.tower
summon minecraft:text_display -7.0 66.2 34.2 {Tags:["mg.hall","mg.h_convoy"],billboard:"vertical",text:[{"text":"🚚 Convoi","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.convoy run data modify entity @e[type=minecraft:text_display,tag=mg.h_convoy,limit=1] text set from storage mg:hall e.convoy
summon minecraft:text_display -23.0 65.0 34.2 {Tags:["mg.hall","mg.h_ctf"],billboard:"vertical",text:[{"text":"🚩 Capture the Flag","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.ctf run data modify entity @e[type=minecraft:text_display,tag=mg.h_ctf,limit=1] text set from storage mg:hall e.ctf
summon minecraft:text_display -21.0 65.0 34.2 {Tags:["mg.hall","mg.h_uhc"],billboard:"vertical",text:[{"text":"⛏ Mini UHC Run","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.uhc run data modify entity @e[type=minecraft:text_display,tag=mg.h_uhc,limit=1] text set from storage mg:hall e.uhc
summon minecraft:text_display -19.0 65.0 34.2 {Tags:["mg.hall","mg.h_hg"],billboard:"vertical",text:[{"text":"🏹 Mini Hunger Games","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.hg run data modify entity @e[type=minecraft:text_display,tag=mg.h_hg,limit=1] text set from storage mg:hall e.hg
summon minecraft:text_display -17.0 65.0 34.2 {Tags:["mg.hall","mg.h_prophunt"],billboard:"vertical",text:[{"text":"🎭 Prop Hunt","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.prophunt run data modify entity @e[type=minecraft:text_display,tag=mg.h_prophunt,limit=1] text set from storage mg:hall e.prophunt
summon minecraft:text_display -15.0 65.0 34.2 {Tags:["mg.hall","mg.h_zombies"],billboard:"vertical",text:[{"text":"🧟 Zombies","color":"dark_green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.zombies run data modify entity @e[type=minecraft:text_display,tag=mg.h_zombies,limit=1] text set from storage mg:hall e.zombies
summon minecraft:text_display -13.0 65.0 34.2 {Tags:["mg.hall","mg.h_infection"],billboard:"vertical",text:[{"text":"🧪 Infection","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.infection run data modify entity @e[type=minecraft:text_display,tag=mg.h_infection,limit=1] text set from storage mg:hall e.infection
summon minecraft:text_display -11.0 65.0 34.2 {Tags:["mg.hall","mg.h_bomber"],billboard:"vertical",text:[{"text":"💣 Bombardier","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.bomber run data modify entity @e[type=minecraft:text_display,tag=mg.h_bomber,limit=1] text set from storage mg:hall e.bomber
data modify storage mg:hall v2 set value 1b
data modify storage mg:hall v3 set value 1b
data modify storage mg:hall v4 set value 1b
data modify storage mg:hall v5 set value 1b
data modify storage mg:hall v6 set value 1b
data modify storage mg:hall v7 set value 1b
data modify storage mg:hall v8 set value 1b
