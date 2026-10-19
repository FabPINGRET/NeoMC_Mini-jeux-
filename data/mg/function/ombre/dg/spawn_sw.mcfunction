# Vague de donjon (sw) : $g monstres
execute store result score $r mg.st run random value 0..4
execute if score $r mg.st matches 0 run function mg:ombre/m/chevnoir
execute if score $r mg.st matches 1 run function mg:ombre/m/necro
execute if score $r mg.st matches 2 run function mg:ombre/m/spectre
execute if score $r mg.st matches 3 run function mg:ombre/m/errant
execute if score $r mg.st matches 4 run function mg:ombre/m/cultiste
tag @e[tag=mg.ollast] add mg.oldgn
scoreboard players remove $g mg.st 1
execute if score $g mg.st matches 1.. positioned ~1 ~ ~0.5 run function mg:ombre/dg/spawn_sw
