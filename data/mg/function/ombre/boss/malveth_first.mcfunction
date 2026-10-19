scoreboard players operation @s mg.olbk += #p7 mg.st
scoreboard players add @s mg.olsp 2
tellraw @a[tag=mg.olw] [{"text":"👑 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a vaincu ","color":"gray"},{"text":"Malveth, l'archimage","color":"gold","bold":true},{"text":" ! (+2 points de caractéristique)","color":"gray"}]
