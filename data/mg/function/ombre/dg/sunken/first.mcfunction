scoreboard players operation @s mg.oldg += #p3 mg.st
function mg:ombre/xp {n:2000}
tellraw @a[tag=mg.olw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a terminé le donjon « Temple englouti » !","color":"gold"}]
