# Voiture PNJ arrivée au carrefour 0 (-76, -78) : nouvelle direction au hasard (tout droit, gauche, droite ; demi-tour en cul-de-sac)
execute if score @s mg.gth matches 0 run return run function mg:gta/traffic/n0_0
execute if score @s mg.gth matches 1 run return run function mg:gta/traffic/n0_1
execute if score @s mg.gth matches 2 run return run function mg:gta/traffic/n0_2
execute if score @s mg.gth matches 3 run return run function mg:gta/traffic/n0_3
