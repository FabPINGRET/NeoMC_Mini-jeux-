# @s : clic droit avec une arme → viser / arrêter de viser
scoreboard players reset @s mg.qs
scoreboard players reset @s mg.gqs
execute if entity @s[tag=mg.gads] run return run function mg:gun/cl_unaim
tag @s add mg.gads
function mg:gun/cl_zoom
execute at @s run playsound minecraft:item.spyglass.use player @s ~ ~ ~ 0.6 1.4
