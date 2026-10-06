# Nouvelle flèche (@s = flèche, à sa position) : équipe du tireur = joueur le plus proche
tag @s add mg.ar
data modify entity @s pickup set value 0b
scoreboard players set $ot mg.st 0
execute as @p[tag=mg.play] if entity @s[team=mg_red] run scoreboard players set $ot mg.st 1
execute as @p[tag=mg.play] if entity @s[team=mg_blue] run scoreboard players set $ot mg.st 2
execute if score $ot mg.st matches 1 run tag @s add mg.ar_r
execute if score $ot mg.st matches 2 run tag @s add mg.ar_b
