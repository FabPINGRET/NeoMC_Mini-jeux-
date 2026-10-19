# Cinématique « open_s » : un tick
execute if score @s mg.olctk matches 1 run function mg:ombre/cs/open_s/k0
execute if score @s mg.olctk matches 61 run function mg:ombre/cs/open_s/k1
execute if score @s mg.olctk matches 1..20 run function mg:ombre/cs/open_s/p0
execute if score @s mg.olctk matches 21..40 run function mg:ombre/cs/open_s/p1
execute if score @s mg.olctk matches 41..60 run function mg:ombre/cs/open_s/p2
execute if score @s mg.olctk matches 61..80 run function mg:ombre/cs/open_s/p3
execute if score @s mg.olctk matches 81..100 run function mg:ombre/cs/open_s/p4
execute if score @s mg.olctk matches 101..120 run function mg:ombre/cs/open_s/p5
execute if score @s mg.olctk matches 121..140 run function mg:ombre/cs/open_s/p6
execute if score @s mg.olctk matches 141..160 run function mg:ombre/cs/open_s/p7
execute if score @s mg.olctk matches 142.. run function mg:ombre/cs/end_back
