# Spleef — construction / remise à neuf (centre 0 ~ 300)
# 4 étages de plus en plus petits + murs invisibles tout autour

# Nettoyage (anciens étages, murs, trous)
fill -16 80 284 16 84 316 minecraft:air
fill -16 73 284 16 77 316 minecraft:air
fill -16 66 284 16 70 316 minecraft:air
fill -16 59 284 16 63 316 minecraft:air

# Étages de neige
fill -14 80 286 14 80 314 minecraft:snow_block
fill -12 73 288 12 73 312 minecraft:snow_block
fill -10 66 290 10 66 310 minecraft:snow_block
fill -8 59 292 8 59 308 minecraft:snow_block

# Murs invisibles (barrières) tout autour et sur toute la hauteur (y 50 → 95) : on ne tombe plus « n'importe où »,
# une chute par le bord se fait dans le puits central (puis élimination). Remplace les anciens murs d'obsidienne.
fill -15 50 285 15 95 285 minecraft:barrier
fill -15 50 315 15 95 315 minecraft:barrier
fill -15 50 286 -15 95 314 minecraft:barrier
fill 15 50 286 15 95 314 minecraft:barrier
