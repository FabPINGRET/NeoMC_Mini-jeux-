# @s : plus joueur du GTA (tags, sons, titres, étoiles, mission)
function mg:gta/mis_clean
tag @s remove mg.gtg
tag @s remove mg.gclub
tag @s remove mg.gdrv
tag @s remove mg.gscope
tag @s remove mg.grd
tag @s remove mg.gro
tag @s remove mg.gslot
tag @s remove mg.gcas_slot
tag @s remove mg.gcas_roulette
tag @s remove mg.gcas_dice
stopsound @s record
title @s clear
title @s reset
scoreboard players reset @s mg.gwl
scoreboard players reset @s mg.gwt
function mg:gun/reset
team leave @s
