# @s tombé dans le vide : remis à côté de sa balle (ou au trou s'il a fini)
function mg:golf/own
execute if score @s mg.gfs matches 0..1 if entity @e[tag=mg.gfmy] run function mg:golf/place
execute if score @s mg.gfs matches 2 run tp @s @e[tag=mg.gftg,limit=1]
tag @e[tag=mg.gfmy] remove mg.gfmy
