# @s = joueur : le met à sa place de départ (mg.ri) sur son parcours (mg.xcr)
execute if score @s mg.xcr matches 1 run function mg:elyrace/c1/place_tp
execute if score @s mg.xcr matches 2 run function mg:elyrace/c2/place_tp
