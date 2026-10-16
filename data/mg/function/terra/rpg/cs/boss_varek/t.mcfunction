# Cinématique « boss_varek » : un tick (pose de la caméra par blocs de 20 ticks, textes aux images clés)
execute if score @s mg.trct matches 1 run function mg:terra/rpg/cs/boss_varek/k0
execute if score @s mg.trct matches 51 run function mg:terra/rpg/cs/boss_varek/k1
execute if score @s mg.trct matches 1..20 run function mg:terra/rpg/cs/boss_varek/p0
execute if score @s mg.trct matches 21..40 run function mg:terra/rpg/cs/boss_varek/p1
execute if score @s mg.trct matches 41..60 run function mg:terra/rpg/cs/boss_varek/p2
execute if score @s mg.trct matches 61..80 run function mg:terra/rpg/cs/boss_varek/p3
execute if score @s mg.trct matches 81..100 run function mg:terra/rpg/cs/boss_varek/p4
execute if score @s mg.trct matches 92.. run function mg:terra/rpg/cs/end_back
