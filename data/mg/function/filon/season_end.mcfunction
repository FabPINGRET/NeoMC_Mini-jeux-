# Fin de saison : classement gardé dans mg.fnl, tout le monde repart de zéro à sa prochaine visite
tellraw @a {"text":"⛏ Fin de la saison du Filon ! Le classement repart à zéro (l'ancien reste visible : /scoreboard objectives setdisplay sidebar mg.fnl).","color":"gold","bold":true}
execute as @a[tag=mg.fnw] in minecraft:overworld run function mg:filon/leave
scoreboard players reset * mg.fnl
scoreboard players operation * mg.fnl = * mg.fns
scoreboard players reset * mg.fns
scoreboard players add $fnsea mg.st 1
scoreboard players set $fnsc mg.st 0
