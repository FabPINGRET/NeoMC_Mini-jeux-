# Chute : en dessous du point le plus bas du tronçon → retour au dernier checkpoint (@s = coureur)
execute store result score $y mg.st run data get entity @s Pos[1]
execute if score @s mg.ppc matches 0 if score $y mg.st matches ..58 run return run function mg:parkour/fall
execute if score @s mg.ppc matches 1 if score $y mg.st matches ..58 run return run function mg:parkour/fall
execute if score @s mg.ppc matches 2 if score $y mg.st matches ..62 run return run function mg:parkour/fall
execute if score @s mg.ppc matches 3 if score $y mg.st matches ..62 run return run function mg:parkour/fall
