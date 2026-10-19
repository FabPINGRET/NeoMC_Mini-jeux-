scoreboard players operation @s mg.olbk += #p5 mg.st
scoreboard players add @s mg.olsp 2
tellraw @a[tag=mg.olw] [{"text":"👑 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a vaincu ","color":"gray"},{"text":"Ignarok, dragon de feu","color":"gold","bold":true},{"text":" ! (+2 points de caractéristique)","color":"gray"}]
