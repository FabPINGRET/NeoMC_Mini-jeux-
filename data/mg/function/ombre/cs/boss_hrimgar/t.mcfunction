# Cinématique « boss_hrimgar » : un tick
execute if score @s mg.olctk matches 1 run function mg:ombre/cs/boss_hrimgar/k0
execute if score @s mg.olctk matches 51 run function mg:ombre/cs/boss_hrimgar/k1
execute if score @s mg.olctk matches 1..20 run function mg:ombre/cs/boss_hrimgar/p0
execute if score @s mg.olctk matches 21..40 run function mg:ombre/cs/boss_hrimgar/p1
execute if score @s mg.olctk matches 41..60 run function mg:ombre/cs/boss_hrimgar/p2
execute if score @s mg.olctk matches 61..80 run function mg:ombre/cs/boss_hrimgar/p3
execute if score @s mg.olctk matches 81..100 run function mg:ombre/cs/boss_hrimgar/p4
execute if score @s mg.olctk matches 101..120 run function mg:ombre/cs/boss_hrimgar/p5
execute if score @s mg.olctk matches 117.. run function mg:ombre/cs/end_back
