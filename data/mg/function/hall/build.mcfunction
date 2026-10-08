# Hall des scores (sud-ouest de la place) : construction + restauration des meneurs
# Chunks du hall pas encore chargés (démarrage du serveur) : on réessaie dans 1 s, 60 fois au plus (motif de mg:dropadv/loaded_all :
# « unless block … bedrock » ne réussit que si le chunk est chargé, il n'y a jamais de bedrock à y 300). #hl = 1 : les 2 chunks sont chargés
execute store success score #hl mg.st unless block -18 300 25 minecraft:bedrock
execute if score #hl mg.st matches 1 store success score #hl mg.st unless block -14 300 25 minecraft:bedrock
execute if score #hl mg.st matches 0 run scoreboard players add #hlr mg.st 1
execute if score #hl mg.st matches 0 if score #hlr mg.st matches 60.. run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] Hall des scores : chunks pas chargés, construction abandonnée (relance /function mg:hall/build).","color":"red"}]
execute if score #hl mg.st matches 0 if score #hlr mg.st matches 60.. run return run scoreboard players set #hlr mg.st 0
execute if score #hl mg.st matches 0 run return run schedule function mg:hall/build 20t
scoreboard players set #hlr mg.st 0
kill @e[tag=mg.hall]

fill -20 63 22 -12 63 28 minecraft:smooth_quartz
fill -20 64 22 -12 70 27 minecraft:air
fill -20 64 28 -12 69 28 minecraft:polished_blackstone_bricks
fill -20 70 28 -12 70 28 minecraft:gold_block
fill -20 64 22 -20 68 22 minecraft:quartz_pillar
fill -12 64 22 -12 68 22 minecraft:quartz_pillar
setblock -20 69 22 minecraft:lantern
setblock -12 69 22 minecraft:lantern
fill -20 64 27 -20 66 27 minecraft:quartz_pillar
fill -12 64 27 -12 66 27 minecraft:quartz_pillar
fill -16 63 22 -16 63 24 minecraft:red_wool
setblock -19 64 25 minecraft:emerald_block
setblock -16 64 25 minecraft:gold_block
setblock -13 64 25 minecraft:lapis_block

# Tampon de résolution des noms (invisible)
summon minecraft:item_display -15.5 64.5 25.5 {Tags:["mg.hall","mg.hallbuf"],item:{id:"minecraft:paper"},transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.001f,0.001f,0.001f]}}
summon minecraft:text_display -15.5 71.0 27.5 {Tags:["mg.hall"],billboard:"center",background:0,text:[{"text":"🏆 Hall des scores","color":"gold","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1.4f,1.4f,1.4f]}}

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
summon minecraft:text_display -19.3 68.3 27.2 {Tags:["mg.hall","mg.h_spleef"],billboard:"vertical",text:[{"text":"❄ Spleef","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.spleef run data modify entity @e[type=minecraft:text_display,tag=mg.h_spleef,limit=1] text set from storage mg:hall e.spleef
summon minecraft:text_display -17.4 68.3 27.2 {Tags:["mg.hall","mg.h_tntrun"],billboard:"vertical",text:[{"text":"✷ TNT Run","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.tntrun run data modify entity @e[type=minecraft:text_display,tag=mg.h_tntrun,limit=1] text set from storage mg:hall e.tntrun
summon minecraft:text_display -15.5 68.3 27.2 {Tags:["mg.hall","mg.h_pvp"],billboard:"vertical",text:[{"text":"⚔ PvP","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.pvp run data modify entity @e[type=minecraft:text_display,tag=mg.h_pvp,limit=1] text set from storage mg:hall e.pvp
summon minecraft:text_display -13.6 68.3 27.2 {Tags:["mg.hall","mg.h_bedwars"],billboard:"vertical",text:[{"text":"🛏 Bedwars","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.bedwars run data modify entity @e[type=minecraft:text_display,tag=mg.h_bedwars,limit=1] text set from storage mg:hall e.bedwars
summon minecraft:text_display -11.7 68.3 27.2 {Tags:["mg.hall","mg.h_sheepwar"],billboard:"vertical",text:[{"text":"🐑 Sheep War","color":"white","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.sheepwar run data modify entity @e[type=minecraft:text_display,tag=mg.h_sheepwar,limit=1] text set from storage mg:hall e.sheepwar
summon minecraft:text_display -19.3 67.1 27.2 {Tags:["mg.hall","mg.h_mobarena"],billboard:"vertical",text:[{"text":"☠ Mob Arena","color":"dark_green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.mobarena run data modify entity @e[type=minecraft:text_display,tag=mg.h_mobarena,limit=1] text set from storage mg:hall e.mobarena
summon minecraft:text_display -17.4 67.1 27.2 {Tags:["mg.hall","mg.h_splegg"],billboard:"vertical",text:[{"text":"❍ Splegg","color":"yellow","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.splegg run data modify entity @e[type=minecraft:text_display,tag=mg.h_splegg,limit=1] text set from storage mg:hall e.splegg
summon minecraft:text_display -15.5 67.1 27.2 {Tags:["mg.hall","mg.h_sumo"],billboard:"vertical",text:[{"text":"✊ Sumo","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.sumo run data modify entity @e[type=minecraft:text_display,tag=mg.h_sumo,limit=1] text set from storage mg:hall e.sumo
summon minecraft:text_display -13.6 67.1 27.2 {Tags:["mg.hall","mg.h_dropper"],billboard:"vertical",text:[{"text":"⬇ Dropper","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.dropper run data modify entity @e[type=minecraft:text_display,tag=mg.h_dropper,limit=1] text set from storage mg:hall e.dropper
summon minecraft:text_display -11.7 67.1 27.2 {Tags:["mg.hall","mg.h_oitc"],billboard:"vertical",text:[{"text":"➶ One in the Chamber","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.oitc run data modify entity @e[type=minecraft:text_display,tag=mg.h_oitc,limit=1] text set from storage mg:hall e.oitc
summon minecraft:text_display -19.3 65.9 27.2 {Tags:["mg.hall","mg.h_tnttag"],billboard:"vertical",text:[{"text":"✹ TNT Tag","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.tnttag run data modify entity @e[type=minecraft:text_display,tag=mg.h_tnttag,limit=1] text set from storage mg:hall e.tnttag
summon minecraft:text_display -17.4 65.9 27.2 {Tags:["mg.hall","mg.h_blockparty"],billboard:"vertical",text:[{"text":"▦ Block Party","color":"light_purple","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.blockparty run data modify entity @e[type=minecraft:text_display,tag=mg.h_blockparty,limit=1] text set from storage mg:hall e.blockparty
summon minecraft:text_display -15.5 65.9 27.2 {Tags:["mg.hall","mg.h_anvil"],billboard:"vertical",text:[{"text":"⚓ Pluie d'enclumes","color":"gray","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.anvil run data modify entity @e[type=minecraft:text_display,tag=mg.h_anvil,limit=1] text set from storage mg:hall e.anvil
summon minecraft:text_display -13.6 65.9 27.2 {Tags:["mg.hall","mg.h_turf"],billboard:"vertical",text:[{"text":"▮ Turf Wars","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.turf run data modify entity @e[type=minecraft:text_display,tag=mg.h_turf,limit=1] text set from storage mg:hall e.turf
summon minecraft:text_display -11.7 65.9 27.2 {Tags:["mg.hall","mg.h_quake"],billboard:"vertical",text:[{"text":"⚡ Quakecraft","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.quake run data modify entity @e[type=minecraft:text_display,tag=mg.h_quake,limit=1] text set from storage mg:hall e.quake
summon minecraft:text_display -19.3 64.7 27.2 {Tags:["mg.hall","mg.h_paintball"],billboard:"vertical",text:[{"text":"▓ Paintball","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.paintball run data modify entity @e[type=minecraft:text_display,tag=mg.h_paintball,limit=1] text set from storage mg:hall e.paintball
summon minecraft:text_display -17.4 64.7 27.2 {Tags:["mg.hall","mg.h_icerace"],billboard:"vertical",text:[{"text":"⛵ Course de bateaux","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.icerace run data modify entity @e[type=minecraft:text_display,tag=mg.h_icerace,limit=1] text set from storage mg:hall e.icerace
summon minecraft:text_display -15.5 64.7 27.2 {Tags:["mg.hall","mg.h_bb"],billboard:"vertical",text:[{"text":"✎ Build Battle","color":"green","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.bb run data modify entity @e[type=minecraft:text_display,tag=mg.h_bb,limit=1] text set from storage mg:hall e.bb
summon minecraft:text_display -13.6 64.7 27.2 {Tags:["mg.hall","mg.h_party"],billboard:"vertical",text:[{"text":"★ Mini Party","color":"gold","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.party run data modify entity @e[type=minecraft:text_display,tag=mg.h_party,limit=1] text set from storage mg:hall e.party
summon minecraft:text_display -11.7 64.7 27.2 {Tags:["mg.hall","mg.h_kart"],billboard:"vertical",text:[{"text":"🏎 Kart","color":"red","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.kart run data modify entity @e[type=minecraft:text_display,tag=mg.h_kart,limit=1] text set from storage mg:hall e.kart
summon minecraft:text_display -19.3 69.5 27.2 {Tags:["mg.hall","mg.h_elyrace"],billboard:"vertical",text:[{"text":"🪽 Course d'élytres","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.elyrace run data modify entity @e[type=minecraft:text_display,tag=mg.h_elyrace,limit=1] text set from storage mg:hall e.elyrace
summon minecraft:text_display -17.4 69.5 27.2 {Tags:["mg.hall","mg.h_elytra"],billboard:"vertical",text:[{"text":"🪽 Élytra (3 modes)","color":"aqua","bold":true},{"text":"\n— personne —","color":"dark_gray","bold":false}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.42f,0.42f,0.42f]}}
execute if data storage mg:hall e.elytra run data modify entity @e[type=minecraft:text_display,tag=mg.h_elytra,limit=1] text set from storage mg:hall e.elytra
data modify storage mg:hall v2 set value 1b
data modify storage mg:hall v3 set value 1b
