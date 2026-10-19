# @s marche sur le socle or : quitte son équipe, perd ses buts libres et remonte à la surface (avenue nord, devant le tapis d'entrée)
function mg:foot/cleanup
tag @s remove mg.ftin
scoreboard players reset @s mg.ft
tag @s remove mg.ftlt
tp @s -2.5 64 -38.5 facing 0.5 64 0.5
title @s actionbar {"text":"🏠 Remonter au spawn","color":"yellow"}
