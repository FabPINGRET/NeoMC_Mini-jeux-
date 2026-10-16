# @s marche sur une case piégée (marqueur le plus proche)
execute if entity @e[type=minecraft:marker,tag=mg.jtr,tag=mg.jt1,distance=..1] run function mg:maze/trap_slow
execute if entity @e[type=minecraft:marker,tag=mg.jtr,tag=mg.jt2,distance=..1] run function mg:maze/trap_back
