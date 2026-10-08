# Spleef — rétrécissement, étape 4 : retire l'anneau extérieur de chaque étage (taille mini 9x9)
fill -11 80 289 11 80 289 minecraft:air replace minecraft:snow_block
fill -11 80 311 11 80 311 minecraft:air replace minecraft:snow_block
fill -11 80 290 -11 80 310 minecraft:air replace minecraft:snow_block
fill 11 80 290 11 80 310 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -9 76 291 9 76 291 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -9 76 309 9 76 309 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -9 76 292 -9 76 308 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill 9 76 292 9 76 308 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -7 72 293 7 72 293 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -7 72 307 7 72 307 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -7 72 294 -7 72 306 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill 7 72 294 7 72 306 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -5 68 295 5 68 295 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -5 68 305 5 68 305 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -5 68 296 -5 68 304 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill 5 68 296 5 68 304 minecraft:air replace minecraft:snow_block
