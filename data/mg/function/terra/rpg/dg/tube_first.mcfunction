# Premier passage : Tube de lave
scoreboard players operation @s mg.trdg += #p3 mg.st
function mg:terra/rpg/xp {n:500}
title @s subtitle {"text":"Donjon terminé : Tube de lave (+500 XP)","color":"yellow"}
tellraw @a[tag=mg.tvw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a terminé le donjon « Tube de lave » !","color":"gold"}]
