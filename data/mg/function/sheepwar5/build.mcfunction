# Sheep War 5 « Pyramides inversées » (centre 0 ~ 3000) — deux pyramides pointe en bas, surface plate 29x29 :
# plus les tirs creusent, plus le terrain se rétrécit vers le vide.

# Nettoyage
fill -46 70 2980 -23 100 3000 minecraft:air
fill -46 70 3001 -23 100 3020 minecraft:air
fill -22 70 2980 0 100 3020 minecraft:air
fill 1 70 2980 23 100 3020 minecraft:air
fill 24 70 2980 46 100 3020 minecraft:air
# --- Pyramide RED (pointe vers le bas) ---
fill -38 90 2986 -10 90 3014 minecraft:red_concrete
fill -37 89 2987 -11 89 3013 minecraft:white_concrete
fill -36 88 2988 -12 88 3012 minecraft:white_concrete
fill -35 87 2989 -13 87 3011 minecraft:white_concrete
fill -34 86 2990 -14 86 3010 minecraft:red_terracotta
fill -33 85 2991 -15 85 3009 minecraft:light_gray_concrete
fill -32 84 2992 -16 84 3008 minecraft:light_gray_concrete
fill -31 83 2993 -17 83 3007 minecraft:light_gray_concrete
fill -30 82 2994 -18 82 3006 minecraft:red_terracotta
fill -29 81 2995 -19 81 3005 minecraft:light_gray_concrete
fill -28 80 2996 -20 80 3004 minecraft:light_gray_concrete
fill -27 79 2997 -21 79 3003 minecraft:light_gray_concrete
fill -26 78 2998 -22 78 3002 minecraft:red_terracotta
fill -25 77 2999 -23 77 3001 minecraft:light_gray_concrete
fill -24 76 3000 -24 76 3000 minecraft:light_gray_concrete
# --- Pyramide BLUE (pointe vers le bas) ---
fill 10 90 2986 38 90 3014 minecraft:blue_concrete
fill 11 89 2987 37 89 3013 minecraft:white_concrete
fill 12 88 2988 36 88 3012 minecraft:white_concrete
fill 13 87 2989 35 87 3011 minecraft:white_concrete
fill 14 86 2990 34 86 3010 minecraft:blue_terracotta
fill 15 85 2991 33 85 3009 minecraft:light_gray_concrete
fill 16 84 2992 32 84 3008 minecraft:light_gray_concrete
fill 17 83 2993 31 83 3007 minecraft:light_gray_concrete
fill 18 82 2994 30 82 3006 minecraft:blue_terracotta
fill 19 81 2995 29 81 3005 minecraft:light_gray_concrete
fill 20 80 2996 28 80 3004 minecraft:light_gray_concrete
fill 21 79 2997 27 79 3003 minecraft:light_gray_concrete
fill 22 78 2998 26 78 3002 minecraft:blue_terracotta
fill 23 77 2999 25 77 3001 minecraft:light_gray_concrete
fill 24 76 3000 24 76 3000 minecraft:light_gray_concrete
# Murs invisibles tout autour (anti-moutons perdus)
data modify storage mg:wl w set value {x:48,z0:2978,z1:3022}
function mg:sheepwar/walls with storage mg:wl w
