# Cinématique « open_ne » : un tick
execute if score @s mg.olctk matches 1 run function mg:ombre/cs/open_ne/k0
execute if score @s mg.olctk matches 61 run function mg:ombre/cs/open_ne/k1
execute if score @s mg.olctk matches 1..20 run function mg:ombre/cs/open_ne/p0
execute if score @s mg.olctk matches 21..40 run function mg:ombre/cs/open_ne/p1
execute if score @s mg.olctk matches 41..60 run function mg:ombre/cs/open_ne/p2
execute if score @s mg.olctk matches 61..80 run function mg:ombre/cs/open_ne/p3
execute if score @s mg.olctk matches 81..100 run function mg:ombre/cs/open_ne/p4
execute if score @s mg.olctk matches 101..120 run function mg:ombre/cs/open_ne/p5
execute if score @s mg.olctk matches 121..140 run function mg:ombre/cs/open_ne/p6
execute if score @s mg.olctk matches 141..160 run function mg:ombre/cs/open_ne/p7
execute if score @s mg.olctk matches 142.. run function mg:ombre/cs/end_back
