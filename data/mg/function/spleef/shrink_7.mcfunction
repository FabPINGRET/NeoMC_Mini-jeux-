# Spleef — rétrécissement, étape 7 : retire l'anneau extérieur de chaque étage (taille mini 9x9)
fill -8 80 292 8 80 292 minecraft:air replace minecraft:snow_block
fill -8 80 308 8 80 308 minecraft:air replace minecraft:snow_block
fill -8 80 293 -8 80 307 minecraft:air replace minecraft:snow_block
fill 8 80 293 8 80 307 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -6 73 294 6 73 294 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -6 73 306 6 73 306 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -6 73 295 -6 73 305 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill 6 73 295 6 73 305 minecraft:air replace minecraft:snow_block
