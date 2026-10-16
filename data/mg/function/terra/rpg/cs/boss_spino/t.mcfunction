# Cinématique « boss_spino » : un tick (pose de la caméra par blocs de 20 ticks, textes aux images clés)
execute if score @s mg.trct matches 1 run function mg:terra/rpg/cs/boss_spino/k0
execute if score @s mg.trct matches 51 run function mg:terra/rpg/cs/boss_spino/k1
execute if score @s mg.trct matches 1..20 run function mg:terra/rpg/cs/boss_spino/p0
execute if score @s mg.trct matches 21..40 run function mg:terra/rpg/cs/boss_spino/p1
execute if score @s mg.trct matches 41..60 run function mg:terra/rpg/cs/boss_spino/p2
execute if score @s mg.trct matches 61..80 run function mg:terra/rpg/cs/boss_spino/p3
execute if score @s mg.trct matches 81..100 run function mg:terra/rpg/cs/boss_spino/p4
execute if score @s mg.trct matches 101..120 run function mg:terra/rpg/cs/boss_spino/p5
execute if score @s mg.trct matches 121..140 run function mg:terra/rpg/cs/boss_spino/p6
execute if score @s mg.trct matches 122.. run function mg:terra/rpg/cs/end_back
