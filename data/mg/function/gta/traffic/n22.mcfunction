# Voiture PNJ arrivée au carrefour 22 (20, -30) : nouvelle direction au hasard (tout droit, gauche, droite ; demi-tour en cul-de-sac)
execute if score @s mg.gth matches 0 run return run function mg:gta/traffic/n22_0
execute if score @s mg.gth matches 1 run return run function mg:gta/traffic/n22_1
execute if score @s mg.gth matches 2 run return run function mg:gta/traffic/n22_2
execute if score @s mg.gth matches 3 run return run function mg:gta/traffic/n22_3
