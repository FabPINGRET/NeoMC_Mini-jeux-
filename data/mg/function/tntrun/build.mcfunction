# TNT Run — construction / remise à neuf (centre 0 ~ 600) : 3 étages
fill -14 84 586 14 84 614 minecraft:white_wool
fill -12 74 588 12 74 612 minecraft:white_wool
fill -10 64 590 10 64 610 minecraft:white_wool

# Murs invisibles (barrières) tout autour et sur toute la hauteur : on ne tombe plus « n'importe où »,
# une chute par le bord se fait dans le puits central (puis élimination)
fill -15 50 585 15 95 585 minecraft:barrier
fill -15 50 615 15 95 615 minecraft:barrier
fill -15 50 586 -15 95 614 minecraft:barrier
fill 15 50 586 15 95 614 minecraft:barrier
