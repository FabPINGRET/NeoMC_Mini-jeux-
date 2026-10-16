# Premier passage : Pic du Nid
scoreboard players operation @s mg.trdg += #p1 mg.st
function mg:terra/rpg/xp {n:500}
title @s subtitle {"text":"Donjon terminé : Pic du Nid (+500 XP)","color":"yellow"}
tellraw @a[tag=mg.tvw] [{"text":"🏆 ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" a terminé le donjon « Pic du Nid » !","color":"gold"}]
