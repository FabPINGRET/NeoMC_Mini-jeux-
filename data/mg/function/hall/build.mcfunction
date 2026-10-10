# Hall des scores (sud-ouest de la place) : construction + restauration des meneurs
# Chunks du hall pas encore chargés (démarrage du serveur) : on réessaie dans 1 s, 60 fois au plus (motif de mg:dropadv/loaded_all :
# « unless block … bedrock » ne réussit que si le chunk est chargé, il n'y a jamais de bedrock à y 300). #hl = 1 : les 2 chunks sont chargés
execute store success score #hl mg.st unless block -22 300 14 minecraft:bedrock
execute if score #hl mg.st matches 1 store success score #hl mg.st unless block -8 300 14 minecraft:bedrock
execute if score #hl mg.st matches 0 run scoreboard players add #hlr mg.st 1
execute if score #hl mg.st matches 0 if score #hlr mg.st matches 60.. run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Hall des scores : chunks pas chargés, construction abandonnée (relance /function mg:hall/build).","color":"red"}]
execute if score #hl mg.st matches 0 if score #hlr mg.st matches 60.. run return run scoreboard players set #hlr mg.st 0
execute if score #hl mg.st matches 0 run return run schedule function mg:hall/build 20t
scoreboard players set #hlr mg.st 0
kill @e[tag=mg.hall]
execute unless data storage mg:hall v9 run function mg:hall/clear_old

fill -24 63 11 -6 63 25 minecraft:smooth_quartz
fill -24 64 11 -6 79 25 minecraft:air
fill -24 64 25 -6 74 25 minecraft:stone_bricks
setblock -24 66 25 minecraft:mossy_stone_bricks
setblock -24 72 25 minecraft:cracked_stone_bricks
setblock -23 67 25 minecraft:mossy_stone_bricks
setblock -23 73 25 minecraft:cracked_stone_bricks
setblock -22 64 25 minecraft:cracked_stone_bricks
setblock -22 68 25 minecraft:mossy_stone_bricks
setblock -22 74 25 minecraft:cracked_stone_bricks
setblock -21 65 25 minecraft:cracked_stone_bricks
setblock -21 69 25 minecraft:mossy_stone_bricks
setblock -20 66 25 minecraft:cracked_stone_bricks
setblock -20 70 25 minecraft:mossy_stone_bricks
setblock -19 67 25 minecraft:cracked_stone_bricks
setblock -19 71 25 minecraft:mossy_stone_bricks
setblock -18 68 25 minecraft:cracked_stone_bricks
setblock -18 72 25 minecraft:mossy_stone_bricks
setblock -17 69 25 minecraft:cracked_stone_bricks
setblock -17 73 25 minecraft:mossy_stone_bricks
setblock -16 64 25 minecraft:mossy_stone_bricks
setblock -16 70 25 minecraft:cracked_stone_bricks
setblock -16 74 25 minecraft:mossy_stone_bricks
setblock -15 65 25 minecraft:mossy_stone_bricks
setblock -15 71 25 minecraft:cracked_stone_bricks
setblock -14 66 25 minecraft:mossy_stone_bricks
setblock -14 72 25 minecraft:cracked_stone_bricks
setblock -13 67 25 minecraft:mossy_stone_bricks
setblock -13 73 25 minecraft:cracked_stone_bricks
setblock -12 64 25 minecraft:cracked_stone_bricks
setblock -12 68 25 minecraft:mossy_stone_bricks
setblock -12 74 25 minecraft:cracked_stone_bricks
setblock -11 65 25 minecraft:cracked_stone_bricks
setblock -11 69 25 minecraft:mossy_stone_bricks
setblock -10 66 25 minecraft:cracked_stone_bricks
setblock -10 70 25 minecraft:mossy_stone_bricks
setblock -9 67 25 minecraft:cracked_stone_bricks
setblock -9 71 25 minecraft:mossy_stone_bricks
setblock -8 68 25 minecraft:cracked_stone_bricks
setblock -8 72 25 minecraft:mossy_stone_bricks
setblock -7 69 25 minecraft:cracked_stone_bricks
setblock -7 73 25 minecraft:mossy_stone_bricks
setblock -6 64 25 minecraft:mossy_stone_bricks
setblock -6 70 25 minecraft:cracked_stone_bricks
setblock -6 74 25 minecraft:mossy_stone_bricks
fill -24 64 25 -6 64 25 minecraft:mossy_stone_bricks
fill -24 75 25 -6 75 25 minecraft:stone_brick_slab[type=bottom]
fill -16 63 11 -15 63 24 minecraft:red_wool
fill -20 64 5 -11 74 10 minecraft:air replace #minecraft:logs
fill -20 64 5 -11 74 10 minecraft:air replace #minecraft:leaves
fill -22 64 18 -20 64 18 minecraft:dark_oak_stairs[facing=south]
fill -10 64 18 -8 64 18 minecraft:dark_oak_stairs[facing=south]
fill -22 64 15 -20 64 15 minecraft:dark_oak_stairs[facing=south]
fill -10 64 15 -8 64 15 minecraft:dark_oak_stairs[facing=south]
fill -23 63 12 -23 63 24 minecraft:gold_block
fill -7 63 12 -7 63 24 minecraft:gold_block
setblock -19 64 15 minecraft:emerald_block
setblock -16 64 15 minecraft:gold_block
setblock -13 64 15 minecraft:lapis_block

# Tampon de résolution des noms (invisible)
summon minecraft:item_display -15.5 64.5 15.5 {Tags:["mg.hall","mg.hallbuf"],item:{id:"minecraft:paper"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.001f,0.001f,0.001f]}}
summon minecraft:text_display -15.5 75.6 24.6 {Tags:["mg.hall"],billboard:"center",background:0,text:[{"text":"🏆 Hall des scores","color":"gold","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[4.5f,4.5f,4.5f]}}

# Piédestaux : objet qui tourne + plaque
summon minecraft:item_display -18.5 65.8 15.5 {Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:clock"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
summon minecraft:item_display -15.5 65.8 15.5 {Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:totem_of_undying"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}
summon minecraft:item_display -12.5 65.8 15.5 {Tags:["mg.hall","mg.lspin","mg.lbob"],billboard:"fixed",item:{id:"minecraft:elytra"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.9f,0.9f,0.9f]}}

# Plaques : texte par défaut, puis meneur enregistré s'il existe
summon minecraft:text_display -18.5 66.9 15.5 {Tags:["mg.hall","mg.h_stp"],billboard:"vertical",line_width:82,text:[{"text":"▶ Le plus assidu","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.35f,1.35f,1.35f]}}
execute if data storage mg:hall e.stp run data modify entity @e[type=minecraft:text_display,tag=mg.h_stp,limit=1] text set from storage mg:hall e.stp
summon minecraft:text_display -15.5 66.9 15.5 {Tags:["mg.hall","mg.h_wins"],billboard:"vertical",line_width:82,text:[{"text":"👑 Champion des mini-jeux","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.35f,1.35f,1.35f]}}
execute if data storage mg:hall e.wins run data modify entity @e[type=minecraft:text_display,tag=mg.h_wins,limit=1] text set from storage mg:hall e.wins
summon minecraft:text_display -12.5 66.9 15.5 {Tags:["mg.hall","mg.h_ely"],billboard:"vertical",line_width:82,text:[{"text":"🪽 Record petit parcours d'élytra","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.35f,1.35f,1.35f]}}
execute if data storage mg:hall e.ely run data modify entity @e[type=minecraft:text_display,tag=mg.h_ely,limit=1] text set from storage mg:hall e.ely
summon minecraft:text_display -12.5 68.4 15.5 {Tags:["mg.hall","mg.h_ely2"],billboard:"vertical",line_width:82,text:[{"text":"🪽 Record grand parcours d'élytra","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.35f,1.35f,1.35f]}}
execute if data storage mg:hall e.ely2 run data modify entity @e[type=minecraft:text_display,tag=mg.h_ely2,limit=1] text set from storage mg:hall e.ely2
summon minecraft:text_display -12.5 69.9 15.5 {Tags:["mg.hall","mg.h_elyg"],billboard:"vertical",line_width:82,text:[{"text":"🪽 Record Élytra : course","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.35f,1.35f,1.35f]}}
execute if data storage mg:hall e.elyg run data modify entity @e[type=minecraft:text_display,tag=mg.h_elyg,limit=1] text set from storage mg:hall e.elyg
summon minecraft:text_display -15.5 73.9 24.3 {Tags:["mg.hall","mg.h_gen"],billboard:"vertical",line_width:200,text:[{"text":"🏅 Meilleur niveau général","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.5f,1.5f,1.5f]}}
execute if data storage mg:hall e.gen run data modify entity @e[type=minecraft:text_display,tag=mg.h_gen,limit=1] text set from storage mg:hall e.gen
summon minecraft:text_display -22.5 72.6 24.2 {Tags:["mg.hall","mg.h_spleef"],billboard:"vertical",line_width:99,text:[{"text":"❄ Spleef","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.spleef run data modify entity @e[type=minecraft:text_display,tag=mg.h_spleef,limit=1] text set from storage mg:hall e.spleef
summon minecraft:text_display -19.5 72.6 24.2 {Tags:["mg.hall","mg.h_tntrun"],billboard:"vertical",line_width:99,text:[{"text":"✷ TNT Run","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.tntrun run data modify entity @e[type=minecraft:text_display,tag=mg.h_tntrun,limit=1] text set from storage mg:hall e.tntrun
summon minecraft:text_display -16.5 72.6 24.2 {Tags:["mg.hall","mg.h_pvp"],billboard:"vertical",line_width:99,text:[{"text":"⚔ PvP","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.pvp run data modify entity @e[type=minecraft:text_display,tag=mg.h_pvp,limit=1] text set from storage mg:hall e.pvp
summon minecraft:text_display -13.5 72.6 24.2 {Tags:["mg.hall","mg.h_bedwars"],billboard:"vertical",line_width:99,text:[{"text":"🛏 Bedwars","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.bedwars run data modify entity @e[type=minecraft:text_display,tag=mg.h_bedwars,limit=1] text set from storage mg:hall e.bedwars
summon minecraft:text_display -10.5 72.6 24.2 {Tags:["mg.hall","mg.h_sheepwar"],billboard:"vertical",line_width:99,text:[{"text":"🐑 Sheep War","color":"white","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.sheepwar run data modify entity @e[type=minecraft:text_display,tag=mg.h_sheepwar,limit=1] text set from storage mg:hall e.sheepwar
summon minecraft:text_display -7.5 72.6 24.2 {Tags:["mg.hall","mg.h_mobarena"],billboard:"vertical",line_width:99,text:[{"text":"☠ Mob Arena","color":"dark_green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.mobarena run data modify entity @e[type=minecraft:text_display,tag=mg.h_mobarena,limit=1] text set from storage mg:hall e.mobarena
summon minecraft:text_display -22.5 71.3 24.2 {Tags:["mg.hall","mg.h_splegg"],billboard:"vertical",line_width:99,text:[{"text":"❍ Splegg","color":"yellow","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.splegg run data modify entity @e[type=minecraft:text_display,tag=mg.h_splegg,limit=1] text set from storage mg:hall e.splegg
summon minecraft:text_display -19.5 71.3 24.2 {Tags:["mg.hall","mg.h_sumo"],billboard:"vertical",line_width:99,text:[{"text":"✊ Sumo","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.sumo run data modify entity @e[type=minecraft:text_display,tag=mg.h_sumo,limit=1] text set from storage mg:hall e.sumo
summon minecraft:text_display -16.5 71.3 24.2 {Tags:["mg.hall","mg.h_dropper"],billboard:"vertical",line_width:99,text:[{"text":"⬇ Dropper","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.dropper run data modify entity @e[type=minecraft:text_display,tag=mg.h_dropper,limit=1] text set from storage mg:hall e.dropper
summon minecraft:text_display -13.5 71.3 24.2 {Tags:["mg.hall","mg.h_oitc"],billboard:"vertical",line_width:99,text:[{"text":"➶ One in the Chamber","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.oitc run data modify entity @e[type=minecraft:text_display,tag=mg.h_oitc,limit=1] text set from storage mg:hall e.oitc
summon minecraft:text_display -10.5 71.3 24.2 {Tags:["mg.hall","mg.h_tnttag"],billboard:"vertical",line_width:99,text:[{"text":"✹ TNT Tag","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.tnttag run data modify entity @e[type=minecraft:text_display,tag=mg.h_tnttag,limit=1] text set from storage mg:hall e.tnttag
summon minecraft:text_display -7.5 71.3 24.2 {Tags:["mg.hall","mg.h_blockparty"],billboard:"vertical",line_width:99,text:[{"text":"▦ Block Party","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.blockparty run data modify entity @e[type=minecraft:text_display,tag=mg.h_blockparty,limit=1] text set from storage mg:hall e.blockparty
summon minecraft:text_display -22.5 70.0 24.2 {Tags:["mg.hall","mg.h_anvil"],billboard:"vertical",line_width:99,text:[{"text":"⚓ Pluie d'enclumes","color":"gray","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.anvil run data modify entity @e[type=minecraft:text_display,tag=mg.h_anvil,limit=1] text set from storage mg:hall e.anvil
summon minecraft:text_display -19.5 70.0 24.2 {Tags:["mg.hall","mg.h_turf"],billboard:"vertical",line_width:99,text:[{"text":"▮ Turf Wars","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.turf run data modify entity @e[type=minecraft:text_display,tag=mg.h_turf,limit=1] text set from storage mg:hall e.turf
summon minecraft:text_display -16.5 70.0 24.2 {Tags:["mg.hall","mg.h_quake"],billboard:"vertical",line_width:99,text:[{"text":"⚡ Quakecraft","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.quake run data modify entity @e[type=minecraft:text_display,tag=mg.h_quake,limit=1] text set from storage mg:hall e.quake
summon minecraft:text_display -13.5 70.0 24.2 {Tags:["mg.hall","mg.h_paintball"],billboard:"vertical",line_width:99,text:[{"text":"▓ Paintball","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.paintball run data modify entity @e[type=minecraft:text_display,tag=mg.h_paintball,limit=1] text set from storage mg:hall e.paintball
summon minecraft:text_display -10.5 70.0 24.2 {Tags:["mg.hall","mg.h_icerace"],billboard:"vertical",line_width:99,text:[{"text":"⛵ Course de bateaux","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.icerace run data modify entity @e[type=minecraft:text_display,tag=mg.h_icerace,limit=1] text set from storage mg:hall e.icerace
summon minecraft:text_display -7.5 70.0 24.2 {Tags:["mg.hall","mg.h_bb"],billboard:"vertical",line_width:99,text:[{"text":"✎ Build Battle","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.bb run data modify entity @e[type=minecraft:text_display,tag=mg.h_bb,limit=1] text set from storage mg:hall e.bb
summon minecraft:text_display -22.5 68.7 24.2 {Tags:["mg.hall","mg.h_party"],billboard:"vertical",line_width:99,text:[{"text":"★ Mini Party","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.party run data modify entity @e[type=minecraft:text_display,tag=mg.h_party,limit=1] text set from storage mg:hall e.party
summon minecraft:text_display -19.5 68.7 24.2 {Tags:["mg.hall","mg.h_kart"],billboard:"vertical",line_width:99,text:[{"text":"🏎 Kart","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.kart run data modify entity @e[type=minecraft:text_display,tag=mg.h_kart,limit=1] text set from storage mg:hall e.kart
summon minecraft:text_display -16.5 68.7 24.2 {Tags:["mg.hall","mg.h_elyrace"],billboard:"vertical",line_width:99,text:[{"text":"🪽 Course d'élytres","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.elyrace run data modify entity @e[type=minecraft:text_display,tag=mg.h_elyrace,limit=1] text set from storage mg:hall e.elyrace
summon minecraft:text_display -13.5 68.7 24.2 {Tags:["mg.hall","mg.h_elytra"],billboard:"vertical",line_width:99,text:[{"text":"🪽 Élytra (3 modes)","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.elytra run data modify entity @e[type=minecraft:text_display,tag=mg.h_elytra,limit=1] text set from storage mg:hall e.elytra
summon minecraft:text_display -10.5 68.7 24.2 {Tags:["mg.hall","mg.h_telephone"],billboard:"vertical",line_width:99,text:[{"text":"📞 Téléphone","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.telephone run data modify entity @e[type=minecraft:text_display,tag=mg.h_telephone,limit=1] text set from storage mg:hall e.telephone
summon minecraft:text_display -7.5 68.7 24.2 {Tags:["mg.hall","mg.h_tron"],billboard:"vertical",line_width:99,text:[{"text":"⚡ Tron","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.tron run data modify entity @e[type=minecraft:text_display,tag=mg.h_tron,limit=1] text set from storage mg:hall e.tron
summon minecraft:text_display -22.5 67.4 24.2 {Tags:["mg.hall","mg.h_koth"],billboard:"vertical",line_width:99,text:[{"text":"👑 King of the Hill","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.koth run data modify entity @e[type=minecraft:text_display,tag=mg.h_koth,limit=1] text set from storage mg:hall e.koth
summon minecraft:text_display -19.5 67.4 24.2 {Tags:["mg.hall","mg.h_tower"],billboard:"vertical",line_width:99,text:[{"text":"🏰 The Towers","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.tower run data modify entity @e[type=minecraft:text_display,tag=mg.h_tower,limit=1] text set from storage mg:hall e.tower
summon minecraft:text_display -16.5 67.4 24.2 {Tags:["mg.hall","mg.h_convoy"],billboard:"vertical",line_width:99,text:[{"text":"🚚 Convoi","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.convoy run data modify entity @e[type=minecraft:text_display,tag=mg.h_convoy,limit=1] text set from storage mg:hall e.convoy
summon minecraft:text_display -13.5 67.4 24.2 {Tags:["mg.hall","mg.h_ctf"],billboard:"vertical",line_width:99,text:[{"text":"🚩 Capture the Flag","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.ctf run data modify entity @e[type=minecraft:text_display,tag=mg.h_ctf,limit=1] text set from storage mg:hall e.ctf
summon minecraft:text_display -10.5 67.4 24.2 {Tags:["mg.hall","mg.h_uhc"],billboard:"vertical",line_width:99,text:[{"text":"⛏ Mini UHC Run","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.uhc run data modify entity @e[type=minecraft:text_display,tag=mg.h_uhc,limit=1] text set from storage mg:hall e.uhc
summon minecraft:text_display -7.5 67.4 24.2 {Tags:["mg.hall","mg.h_hg"],billboard:"vertical",line_width:99,text:[{"text":"🏹 Mini Hunger Games","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.hg run data modify entity @e[type=minecraft:text_display,tag=mg.h_hg,limit=1] text set from storage mg:hall e.hg
summon minecraft:text_display -22.5 66.1 24.2 {Tags:["mg.hall","mg.h_prophunt"],billboard:"vertical",line_width:99,text:[{"text":"🎭 Prop Hunt","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.prophunt run data modify entity @e[type=minecraft:text_display,tag=mg.h_prophunt,limit=1] text set from storage mg:hall e.prophunt
summon minecraft:text_display -19.5 66.1 24.2 {Tags:["mg.hall","mg.h_zombies"],billboard:"vertical",line_width:99,text:[{"text":"🧟 Zombies","color":"dark_green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.zombies run data modify entity @e[type=minecraft:text_display,tag=mg.h_zombies,limit=1] text set from storage mg:hall e.zombies
summon minecraft:text_display -16.5 66.1 24.2 {Tags:["mg.hall","mg.h_infection"],billboard:"vertical",line_width:99,text:[{"text":"🧪 Infection","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.infection run data modify entity @e[type=minecraft:text_display,tag=mg.h_infection,limit=1] text set from storage mg:hall e.infection
summon minecraft:text_display -13.5 66.1 24.2 {Tags:["mg.hall","mg.h_bomber"],billboard:"vertical",line_width:99,text:[{"text":"💣 Bombardier","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.bomber run data modify entity @e[type=minecraft:text_display,tag=mg.h_bomber,limit=1] text set from storage mg:hall e.bomber
summon minecraft:text_display -10.5 66.1 24.2 {Tags:["mg.hall","mg.h_chameleon"],billboard:"vertical",line_width:99,text:[{"text":"🦎 Meccha Chameleon","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.chameleon run data modify entity @e[type=minecraft:text_display,tag=mg.h_chameleon,limit=1] text set from storage mg:hall e.chameleon
summon minecraft:text_display -7.5 66.1 24.2 {Tags:["mg.hall","mg.h_wii"],billboard:"vertical",line_width:99,text:[{"text":"🎾 Wii Sports","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.wii run data modify entity @e[type=minecraft:text_display,tag=mg.h_wii,limit=1] text set from storage mg:hall e.wii
summon minecraft:text_display -22.5 64.8 24.2 {Tags:["mg.hall","mg.h_soleil"],billboard:"vertical",line_width:99,text:[{"text":"🔴 1, 2, 3 Soleil","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.125f,1.125f,1.125f]}}
execute if data storage mg:hall e.soleil run data modify entity @e[type=minecraft:text_display,tag=mg.h_soleil,limit=1] text set from storage mg:hall e.soleil
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
