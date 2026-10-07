# Chute : en dessous du point le plus bas du tronçon → retour au dernier checkpoint (@s = coureur)
execute if score @s mg.ppc matches 0 at @s if entity @s[y=-1990,dy=2048] run return run function mg:parkour/fall
execute if score @s mg.ppc matches 1 at @s if entity @s[y=-1990,dy=2048] run return run function mg:parkour/fall
execute if score @s mg.ppc matches 2 at @s if entity @s[y=-1986,dy=2048] run return run function mg:parkour/fall
execute if score @s mg.ppc matches 3 at @s if entity @s[y=-1986,dy=2048] run return run function mg:parkour/fall
