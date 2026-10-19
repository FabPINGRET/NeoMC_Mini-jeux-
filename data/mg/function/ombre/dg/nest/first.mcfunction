scoreboard players operation @s mg.oldg += #p1 mg.st
function mg:ombre/xp {n:1000}
tellraw @a[tag=mg.olw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a terminé le donjon « Nid des tisseuses » !","color":"gold"}]
