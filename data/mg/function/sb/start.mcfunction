# Tableau de droite pendant les jeux qui n'en avaient pas (appelé par core/begin) : $sbon = 1 si ce jeu l'utilise
scoreboard players set $sbon mg.st 0
scoreboard players reset * mg.sbg
scoreboard objectives modify mg.sbg numberformat blank
execute if score $game mg.st matches 1 run scoreboard players set $sbon mg.st 1
execute if score $game mg.st matches 1 run scoreboard objectives modify mg.sbg displayname [{"text":"❄ SPLEEF","color":"aqua","bold":true}]
execute if score $game mg.st matches 2 run scoreboard players set $sbon mg.st 1
execute if score $game mg.st matches 2 run scoreboard objectives modify mg.sbg displayname [{"text":"✷ TNT RUN","color":"red","bold":true}]
execute if score $game mg.st matches 3 run scoreboard players set $sbon mg.st 1
execute if score $game mg.st matches 3 run scoreboard objectives modify mg.sbg displayname [{"text":"⚔ ARÈNE PVP","color":"gold","bold":true}]
execute if score $game mg.st matches 20 run scoreboard players set $sbon mg.st 1
execute if score $game mg.st matches 20 run scoreboard objectives modify mg.sbg displayname [{"text":"❍ SPLEGG","color":"yellow","bold":true}]
execute if score $game mg.st matches 22 run scoreboard players set $sbon mg.st 1
execute if score $game mg.st matches 22 run scoreboard objectives modify mg.sbg displayname [{"text":"✊ SUMO — vies","color":"gold","bold":true}]
execute if score $game mg.st matches 23 run scoreboard players set $sbon mg.st 1
execute if score $game mg.st matches 23 run scoreboard objectives modify mg.sbg displayname [{"text":"⬇ THE DROPPER — manches","color":"aqua","bold":true}]
execute if score $game mg.st matches 27 run scoreboard players set $sbon mg.st 1
execute if score $game mg.st matches 27 run scoreboard objectives modify mg.sbg displayname [{"text":"✹ TNT TAG","color":"red","bold":true}]
execute if score $game mg.st matches 28 run scoreboard players set $sbon mg.st 1
execute if score $game mg.st matches 28 run scoreboard objectives modify mg.sbg displayname [{"text":"▦ BLOCK PARTY","color":"light_purple","bold":true}]
execute if score $game mg.st matches 29 run scoreboard players set $sbon mg.st 1
execute if score $game mg.st matches 29 run scoreboard objectives modify mg.sbg displayname [{"text":"⚓ PLUIE D'ENCLUMES","color":"gray","bold":true}]
execute if score $game mg.st matches 4 run scoreboard players set $sbon mg.st 1
execute if score $game mg.st matches 4 run scoreboard objectives modify mg.sbg displayname [{"text":"🛏 BEDWARS","color":"light_purple","bold":true}]
execute if score $game mg.st matches 5 run scoreboard players set $sbon mg.st 1
execute if score $game mg.st matches 5 run scoreboard objectives modify mg.sbg displayname [{"text":"🐑 SHEEP WAR","color":"white","bold":true}]
execute if score $game mg.st matches 7 run scoreboard players set $sbon mg.st 1
execute if score $game mg.st matches 7 run scoreboard objectives modify mg.sbg displayname [{"text":"🐑 SHEEP WAR","color":"white","bold":true}]
execute if score $mp mg.st matches 1 run scoreboard players set $sbon mg.st 0
execute if score $sbon mg.st matches 1 run scoreboard objectives setdisplay sidebar mg.sbg
scoreboard players set $sbt mg.st 0
