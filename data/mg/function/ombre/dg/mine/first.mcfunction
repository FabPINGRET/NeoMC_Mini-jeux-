scoreboard players operation @s mg.oldg += #p6 mg.st
function mg:ombre/xp {n:3500}
tellraw @a[tag=mg.olw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a terminé le donjon « Mines profondes » !","color":"gold"}]
