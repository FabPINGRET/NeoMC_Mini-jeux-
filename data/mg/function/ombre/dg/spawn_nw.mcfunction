# Vague de donjon (nw) : $g monstres
execute store result score $r mg.st run random value 0..4
execute if score $r mg.st matches 0 run function mg:ombre/m/araignee
execute if score $r mg.st matches 1 run function mg:ombre/m/tisseuse
execute if score $r mg.st matches 2 run function mg:ombre/m/follet
execute if score $r mg.st matches 3 run function mg:ombre/m/elfe
execute if score $r mg.st matches 4 run function mg:ombre/m/garou
tag @e[tag=mg.ollast] add mg.oldgn
scoreboard players remove $g mg.st 1
execute if score $g mg.st matches 1.. positioned ~1 ~ ~0.5 run function mg:ombre/dg/spawn_nw
