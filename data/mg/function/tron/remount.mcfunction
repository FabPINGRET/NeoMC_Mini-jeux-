# @s est descendu : on le remet sur sa moto (Maj ne sert à rien)
execute as @e[tag=mg.trh] if score @s mg.trc = $tid mg.st run tag @s add mg.trmt
ride @s mount @e[tag=mg.trmt,limit=1]
tag @e remove mg.trmt
