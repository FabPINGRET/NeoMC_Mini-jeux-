# Cinématique « pass_n » : un tick (pose de la caméra par blocs de 20 ticks, textes aux images clés)
execute if score @s mg.trct matches 1 run function mg:terra/rpg/cs/pass_n/k0
execute if score @s mg.trct matches 1..20 run function mg:terra/rpg/cs/pass_n/p0
execute if score @s mg.trct matches 21..40 run function mg:terra/rpg/cs/pass_n/p1
execute if score @s mg.trct matches 41..60 run function mg:terra/rpg/cs/pass_n/p2
execute if score @s mg.trct matches 61..80 run function mg:terra/rpg/cs/pass_n/p3
execute if score @s mg.trct matches 81..100 run function mg:terra/rpg/cs/pass_n/p4
execute if score @s mg.trct matches 101..120 run function mg:terra/rpg/cs/pass_n/p5
execute if score @s mg.trct matches 121..140 run function mg:terra/rpg/cs/pass_n/p6
execute if score @s mg.trct matches 132.. run function mg:terra/rpg/cs/end_back
