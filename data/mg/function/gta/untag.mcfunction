# @s : plus joueur du GTA (tags, sons, titres, étoiles)
tag @s remove mg.gtg
tag @s remove mg.gdrv
tag @s remove mg.gscope
tag @s remove mg.grd
tag @s remove mg.gro
stopsound @s record
title @s clear
title @s reset
scoreboard players reset @s mg.gwl
scoreboard players reset @s mg.gwt
function mg:gun/reset
team leave @s
