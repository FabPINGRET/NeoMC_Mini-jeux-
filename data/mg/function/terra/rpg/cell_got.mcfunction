# @s récupère la cellule d'énergie
scoreboard players set @s mg.trpk 0
function mg:terra/rpg/xp {n:150}
function mg:terra/rpg/ch {n:66}
title @s title {"text":"🔋 Cellule récupérée","color":"aqua","bold":true}
execute at @s run playsound minecraft:block.respawn_anchor.charge player @a ~ ~ ~ 1 1
