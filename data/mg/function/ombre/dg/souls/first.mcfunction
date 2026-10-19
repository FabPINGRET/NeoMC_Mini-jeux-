scoreboard players operation @s mg.oldg += #p7 mg.st
function mg:ombre/xp {n:4000}
tellraw @a[tag=mg.olw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a terminé le donjon « Puits des âmes » !","color":"gold"}]
