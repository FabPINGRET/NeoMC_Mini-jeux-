# Tableau de droite pendant le kart : classement en direct (remplace l'ancienne minimap)
scoreboard players reset * mg.sbg
scoreboard objectives modify mg.sbg numberformat blank
execute if score $kbat mg.st matches 1 run scoreboard objectives modify mg.sbg displayname [{"text":"🎈 Bataille — ballons","color":"red","bold":true}]
execute unless score $kbat mg.st matches 1 run scoreboard objectives modify mg.sbg displayname [{"text":"🏁 Classement","color":"gold","bold":true}]
scoreboard objectives setdisplay sidebar mg.sbg
