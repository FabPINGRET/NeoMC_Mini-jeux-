# @s est descendu : on le remet sur sa moto (Maj ne sert à rien)
execute as @e[tag=mg.trh] if score @s mg.trc = $tid mg.st run tag @s add mg.thm
ride @s mount @e[tag=mg.thm,limit=1]
tag @e remove mg.thm
