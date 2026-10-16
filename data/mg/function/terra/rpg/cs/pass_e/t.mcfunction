# Cinématique « pass_e » : un tick (pose de la caméra par blocs de 20 ticks, textes aux images clés)
execute if score @s mg.trct matches 1 run function mg:terra/rpg/cs/pass_e/k0
execute if score @s mg.trct matches 1..20 run function mg:terra/rpg/cs/pass_e/p0
execute if score @s mg.trct matches 21..40 run function mg:terra/rpg/cs/pass_e/p1
execute if score @s mg.trct matches 41..60 run function mg:terra/rpg/cs/pass_e/p2
execute if score @s mg.trct matches 61..80 run function mg:terra/rpg/cs/pass_e/p3
execute if score @s mg.trct matches 81..100 run function mg:terra/rpg/cs/pass_e/p4
execute if score @s mg.trct matches 101..120 run function mg:terra/rpg/cs/pass_e/p5
execute if score @s mg.trct matches 121..140 run function mg:terra/rpg/cs/pass_e/p6
execute if score @s mg.trct matches 132.. run function mg:terra/rpg/cs/end_back
