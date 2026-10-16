# Cinématique « finale » : un tick (pose de la caméra par blocs de 20 ticks, textes aux images clés)
execute if score @s mg.trct matches 1 run function mg:terra/rpg/cs/finale/k0
execute if score @s mg.trct matches 56 run function mg:terra/rpg/cs/finale/k1
execute if score @s mg.trct matches 111 run function mg:terra/rpg/cs/finale/k2
execute if score @s mg.trct matches 166 run function mg:terra/rpg/cs/finale/k3
execute if score @s mg.trct matches 1..20 run function mg:terra/rpg/cs/finale/p0
execute if score @s mg.trct matches 21..40 run function mg:terra/rpg/cs/finale/p1
execute if score @s mg.trct matches 41..60 run function mg:terra/rpg/cs/finale/p2
execute if score @s mg.trct matches 61..80 run function mg:terra/rpg/cs/finale/p3
execute if score @s mg.trct matches 81..100 run function mg:terra/rpg/cs/finale/p4
execute if score @s mg.trct matches 101..120 run function mg:terra/rpg/cs/finale/p5
execute if score @s mg.trct matches 121..140 run function mg:terra/rpg/cs/finale/p6
execute if score @s mg.trct matches 141..160 run function mg:terra/rpg/cs/finale/p7
execute if score @s mg.trct matches 161..180 run function mg:terra/rpg/cs/finale/p8
execute if score @s mg.trct matches 181..200 run function mg:terra/rpg/cs/finale/p9
execute if score @s mg.trct matches 201..220 run function mg:terra/rpg/cs/finale/p10
execute if score @s mg.trct matches 202.. run function mg:terra/rpg/cs/end_back
