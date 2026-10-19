scoreboard players operation @s mg.oldg += #p2 mg.st
function mg:ombre/xp {n:1500}
tellraw @a[tag=mg.olw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a terminé le donjon « Grotte de givre » !","color":"gold"}]
