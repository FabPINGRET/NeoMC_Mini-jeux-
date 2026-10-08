# Spleef — rétrécissement, étape 8 : retire l'anneau extérieur de chaque étage (taille mini 9x9)
fill -7 80 293 7 80 293 minecraft:air replace minecraft:snow_block
fill -7 80 307 7 80 307 minecraft:air replace minecraft:snow_block
fill -7 80 294 -7 80 306 minecraft:air replace minecraft:snow_block
fill 7 80 294 7 80 306 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -5 76 295 5 76 295 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -5 76 305 5 76 305 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -5 76 296 -5 76 304 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill 5 76 296 5 76 304 minecraft:air replace minecraft:snow_block
