# Voiture PNJ arrivée au carrefour 18 (-12, 18) : nouvelle direction au hasard (tout droit, gauche, droite ; demi-tour en cul-de-sac)
execute if score @s mg.gth matches 0 run return run function mg:gta/traffic/n18_0
execute if score @s mg.gth matches 1 run return run function mg:gta/traffic/n18_1
execute if score @s mg.gth matches 2 run return run function mg:gta/traffic/n18_2
execute if score @s mg.gth matches 3 run return run function mg:gta/traffic/n18_3
