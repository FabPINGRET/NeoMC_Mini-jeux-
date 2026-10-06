# Quakecraft — arène 31x31 (centre 0 ~ 7300) : sol en quartz, pyramide centrale, piliers et murets de couvert, murs et plafond invisibles
fill -17 81 7283 17 98 7317 minecraft:air
fill -15 80 7285 15 80 7315 minecraft:smooth_quartz
# Bordure et croix lumineuses
fill -15 80 7285 15 80 7285 minecraft:cyan_concrete
fill -15 80 7315 15 80 7315 minecraft:cyan_concrete
fill -15 80 7285 -15 80 7315 minecraft:cyan_concrete
fill 15 80 7285 15 80 7315 minecraft:cyan_concrete
fill -14 80 7300 14 80 7300 minecraft:light_blue_concrete
fill 0 80 7286 0 80 7314 minecraft:light_blue_concrete
# Pyramide centrale (marches de 1 bloc)
fill -5 81 7295 5 81 7305 minecraft:quartz_block
fill -3 82 7297 3 82 7303 minecraft:quartz_bricks
fill -1 83 7299 1 83 7301 minecraft:prismarine_bricks
setblock 0 84 7300 minecraft:sea_lantern
# Piliers d'angle (2 de haut) + marche d'accès
fill 8 81 7291 10 82 7293 minecraft:prismarine_bricks
fill -10 81 7291 -8 82 7293 minecraft:prismarine_bricks
fill 8 81 7307 10 82 7309 minecraft:prismarine_bricks
fill -10 81 7307 -8 82 7309 minecraft:prismarine_bricks
fill 7 81 7292 7 81 7292 minecraft:prismarine_bricks
fill -7 81 7292 -7 81 7292 minecraft:prismarine_bricks
fill 7 81 7308 7 81 7308 minecraft:prismarine_bricks
fill -7 81 7308 -7 81 7308 minecraft:prismarine_bricks
# Murets de couvert (2 de haut)
fill 11 81 7297 11 82 7303 minecraft:dark_prismarine
fill -11 81 7297 -11 82 7303 minecraft:dark_prismarine
fill -3 81 7289 3 82 7289 minecraft:dark_prismarine
fill -3 81 7311 3 82 7311 minecraft:dark_prismarine
# Petits blocs de couvert isolés
fill 5 81 7294 5 82 7294 minecraft:quartz_pillar
fill -5 81 7294 -5 82 7294 minecraft:quartz_pillar
fill 5 81 7306 5 82 7306 minecraft:quartz_pillar
fill -5 81 7306 -5 82 7306 minecraft:quartz_pillar
# Murs et plafond invisibles (le laser s'arrête dessus)
fill -16 81 7284 16 94 7284 minecraft:barrier
fill -16 81 7316 16 94 7316 minecraft:barrier
fill -16 81 7285 -16 94 7315 minecraft:barrier
fill 16 81 7285 16 94 7315 minecraft:barrier
fill -15 94 7285 15 94 7315 minecraft:barrier
