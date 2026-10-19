scoreboard players operation @s mg.oldg += #p4 mg.st
function mg:ombre/xp {n:2500}
tellraw @a[tag=mg.olw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a terminé le donjon « Tombeaux d'Azhar » !","color":"gold"}]
