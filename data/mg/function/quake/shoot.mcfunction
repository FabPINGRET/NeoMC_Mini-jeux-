# Tir de railgun (@s = joueur qui a fait un clic droit)
scoreboard players reset @s mg.qs
execute if score @s mg.cd matches 1.. run return 0
scoreboard players operation @s mg.cd = $qcd mg.st
tag @s add mg.qsh
scoreboard players set $rs mg.st 140
# cartes sniper : portée 120 blocs
execute if score $ar mg.st matches 0 if score $qm mg.st matches 8..9 run scoreboard players set $rs mg.st 240
execute at @s anchored eyes positioned ^ ^ ^0.5 run function mg:quake/ray
tag @s remove mg.qsh
execute at @s run playsound minecraft:entity.firework_rocket.blast master @a ~ ~ ~ 1 1.8
