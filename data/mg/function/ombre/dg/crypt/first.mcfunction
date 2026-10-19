scoreboard players operation @s mg.oldg += #p0 mg.st
function mg:ombre/xp {n:500}
tellraw @a[tag=mg.olw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a terminé le donjon « Cryptes de Valdor » !","color":"gold"}]
