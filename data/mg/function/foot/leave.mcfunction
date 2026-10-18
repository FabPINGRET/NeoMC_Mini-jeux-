# @s marche sur le socle or : quitte son équipe et remonte au spawn
function mg:foot/cleanup
tag @s remove mg.ftin
tp @s 0.5 64 0.5 facing 0.5 64 8.5
title @s actionbar {"text":"🏠 Retour au spawn","color":"yellow"}
