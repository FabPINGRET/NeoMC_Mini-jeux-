# Premier passage : Cœur de l'Arbre-Mère
scoreboard players operation @s mg.trdg += #p0 mg.st
function mg:terra/rpg/xp {n:500}
title @s subtitle {"text":"Donjon terminé : Cœur de l'Arbre-Mère (+500 XP)","color":"yellow"}
tellraw @a[tag=mg.tvw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a terminé le donjon « Cœur de l'Arbre-Mère » !","color":"gold"}]
