# Spleef — rétrécissement, étape 4 : retire l'anneau extérieur de chaque étage (taille mini 9x9)
fill -11 80 289 11 80 289 minecraft:air replace minecraft:snow_block
fill -11 80 311 11 80 311 minecraft:air replace minecraft:snow_block
fill -11 80 290 -11 80 310 minecraft:air replace minecraft:snow_block
fill 11 80 290 11 80 310 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -9 73 291 9 73 291 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -9 73 309 9 73 309 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -9 73 292 -9 73 308 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill 9 73 292 9 73 308 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -7 66 293 7 66 293 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -7 66 307 7 66 307 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -7 66 294 -7 66 306 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill 7 66 294 7 66 306 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -5 59 295 5 59 295 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -5 59 305 5 59 305 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -5 59 296 -5 59 304 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill 5 59 296 5 59 304 minecraft:air replace minecraft:snow_block
