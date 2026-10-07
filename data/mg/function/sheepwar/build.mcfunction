# Sheep War — construction / remise à neuf (centre 0 ~ 1500)
# Grandes plateformes 3 couches (26 x 41) + murs d'obsidienne à l'arrière, écart de 15 blocs

# Nettoyage de la zone (cratères, ancienne géométrie) — 4 quarts pour rester sous la limite de fill
fill -46 77 1470 0 90 1500 minecraft:air
fill 1 77 1470 46 90 1500 minecraft:air
fill -46 77 1501 0 90 1530 minecraft:air
fill 1 77 1501 46 90 1530 minecraft:air

# --- Plateforme ROUGE (3 couches de laine) ---
fill -34 79 1480 -8 79 1520 minecraft:red_wool
fill -34 78 1480 -8 78 1520 minecraft:white_wool
fill -34 77 1480 -8 77 1520 minecraft:light_gray_wool

# --- Plateforme BLEUE (3 couches de laine) ---
fill 8 79 1480 34 79 1520 minecraft:blue_wool
fill 8 78 1480 34 78 1520 minecraft:white_wool
fill 8 77 1480 34 77 1520 minecraft:light_gray_wool

# --- Murs d'obsidienne à l'arrière (indestructibles) ---
fill -35 77 1479 -35 84 1521 minecraft:obsidian
fill 35 77 1479 35 84 1521 minecraft:obsidian
# Murs invisibles tout autour (anti-moutons perdus)
data modify storage mg:wl w set value {x:48,z0:1468,z1:1532}
function mg:sheepwar/walls with storage mg:wl w
