# Mob Arena — construction (centre 0 ~ 1800), arène fermée
fill -15 63 1785 15 63 1815 minecraft:deepslate_tiles
fill -3 63 1797 3 63 1803 minecraft:polished_deepslate

# Murs (hauteur 5)
fill -15 64 1785 15 68 1785 minecraft:deepslate_bricks
fill -15 64 1815 15 68 1815 minecraft:deepslate_bricks
fill -15 64 1786 -15 68 1814 minecraft:deepslate_bricks
fill 15 64 1786 15 68 1814 minecraft:deepslate_bricks

# Rebord anti-escalade (vers l'intérieur, en haut du mur)
fill -14 68 1786 14 68 1786 minecraft:deepslate_bricks
fill -14 68 1814 14 68 1814 minecraft:deepslate_bricks
fill -14 68 1787 -14 68 1813 minecraft:deepslate_bricks
fill 14 68 1787 14 68 1813 minecraft:deepslate_bricks

# Éclairage
setblock 0 63 1800 minecraft:glowstone
setblock -10 63 1790 minecraft:glowstone
setblock 10 63 1790 minecraft:glowstone
setblock -10 63 1810 minecraft:glowstone
setblock 10 63 1810 minecraft:glowstone
setblock -14 67 1786 minecraft:soul_lantern[hanging=true]
setblock 14 67 1786 minecraft:soul_lantern[hanging=true]
setblock -14 67 1814 minecraft:soul_lantern[hanging=true]
setblock 14 67 1814 minecraft:soul_lantern[hanging=true]
