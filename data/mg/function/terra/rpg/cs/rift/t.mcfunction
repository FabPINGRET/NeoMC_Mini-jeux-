# Cinématique « rift » : un tick (pose de la caméra par blocs de 20 ticks, textes aux images clés)
execute if score @s mg.trct matches 1 run function mg:terra/rpg/cs/rift/k0
execute if score @s mg.trct matches 56 run function mg:terra/rpg/cs/rift/k1
execute if score @s mg.trct matches 111 run function mg:terra/rpg/cs/rift/k2
execute if score @s mg.trct matches 1..20 run function mg:terra/rpg/cs/rift/p0
execute if score @s mg.trct matches 21..40 run function mg:terra/rpg/cs/rift/p1
execute if score @s mg.trct matches 41..60 run function mg:terra/rpg/cs/rift/p2
execute if score @s mg.trct matches 61..80 run function mg:terra/rpg/cs/rift/p3
execute if score @s mg.trct matches 81..100 run function mg:terra/rpg/cs/rift/p4
execute if score @s mg.trct matches 101..120 run function mg:terra/rpg/cs/rift/p5
execute if score @s mg.trct matches 121..140 run function mg:terra/rpg/cs/rift/p6
execute if score @s mg.trct matches 141..160 run function mg:terra/rpg/cs/rift/p7
execute if score @s mg.trct matches 161..180 run function mg:terra/rpg/cs/rift/p8
execute if score @s mg.trct matches 162.. run function mg:terra/rpg/cs/end_spawn
