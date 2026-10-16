# Cinématique « boss_rex » : un tick (pose de la caméra par blocs de 20 ticks, textes aux images clés)
execute if score @s mg.trct matches 1 run function mg:terra/rpg/cs/boss_rex/k0
execute if score @s mg.trct matches 51 run function mg:terra/rpg/cs/boss_rex/k1
execute if score @s mg.trct matches 101 run function mg:terra/rpg/cs/boss_rex/k2
execute if score @s mg.trct matches 1..20 run function mg:terra/rpg/cs/boss_rex/p0
execute if score @s mg.trct matches 21..40 run function mg:terra/rpg/cs/boss_rex/p1
execute if score @s mg.trct matches 41..60 run function mg:terra/rpg/cs/boss_rex/p2
execute if score @s mg.trct matches 61..80 run function mg:terra/rpg/cs/boss_rex/p3
execute if score @s mg.trct matches 81..100 run function mg:terra/rpg/cs/boss_rex/p4
execute if score @s mg.trct matches 101..120 run function mg:terra/rpg/cs/boss_rex/p5
execute if score @s mg.trct matches 121..140 run function mg:terra/rpg/cs/boss_rex/p6
execute if score @s mg.trct matches 141..160 run function mg:terra/rpg/cs/boss_rex/p7
execute if score @s mg.trct matches 142.. run function mg:terra/rpg/cs/end_back
