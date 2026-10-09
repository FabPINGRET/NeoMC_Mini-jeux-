# Voiture PNJ arrivée au carrefour 25 (20, 42) : nouvelle direction au hasard (tout droit, gauche, droite ; demi-tour en cul-de-sac)
execute if score @s mg.gth matches 0 run return run function mg:gta/traffic/n25_0
execute if score @s mg.gth matches 1 run return run function mg:gta/traffic/n25_1
execute if score @s mg.gth matches 2 run return run function mg:gta/traffic/n25_2
execute if score @s mg.gth matches 3 run return run function mg:gta/traffic/n25_3
