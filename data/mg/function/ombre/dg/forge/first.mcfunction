scoreboard players operation @s mg.oldg += #p5 mg.st
function mg:ombre/xp {n:3000}
tellraw @a[tag=mg.olw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a terminé le donjon « Forge écarlate » !","color":"gold"}]
