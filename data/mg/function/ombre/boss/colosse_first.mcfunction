scoreboard players operation @s mg.olbk += #p6 mg.st
scoreboard players add @s mg.olsp 2
tellraw @a[tag=mg.olw] [{"text":"👑 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a vaincu ","color":"gray"},{"text":"Le Colosse de runes","color":"gold","bold":true},{"text":" ! (+2 points de caractéristique)","color":"gray"}]
