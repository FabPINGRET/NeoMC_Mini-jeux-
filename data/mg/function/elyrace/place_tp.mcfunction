# @s = joueur : le met à sa place de départ (mg.ri) sur son parcours
execute if score $xc mg.st matches 1 run function mg:elyrace/c1/place_tp
execute if score $xc mg.st matches 2 run function mg:elyrace/c2/place_tp
