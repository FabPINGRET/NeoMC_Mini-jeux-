# Premier passage : Mine abandonnée
scoreboard players operation @s mg.trdg += #p2 mg.st
function mg:terra/rpg/xp {n:500}
title @s subtitle {"text":"Donjon terminé : Mine abandonnée (+500 XP)","color":"yellow"}
tellraw @a[tag=mg.tvw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a terminé le donjon « Mine abandonnée » !","color":"gold"}]
