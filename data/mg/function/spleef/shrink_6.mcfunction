# Spleef — rétrécissement, étape 6 : retire l'anneau extérieur de chaque étage (taille mini 9x9)
fill -9 80 291 9 80 291 minecraft:air replace minecraft:snow_block
fill -9 80 309 9 80 309 minecraft:air replace minecraft:snow_block
fill -9 80 292 -9 80 308 minecraft:air replace minecraft:snow_block
fill 9 80 292 9 80 308 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -7 76 293 7 76 293 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -7 76 307 7 76 307 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -7 76 294 -7 76 306 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill 7 76 294 7 76 306 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -5 72 295 5 72 295 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -5 72 305 5 72 305 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -5 72 296 -5 72 304 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill 5 72 296 5 72 304 minecraft:air replace minecraft:snow_block
