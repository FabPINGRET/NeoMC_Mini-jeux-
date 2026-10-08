# Spleef — rétrécissement, étape 5 : retire l'anneau extérieur de chaque étage (taille mini 9x9)
fill -10 80 290 10 80 290 minecraft:air replace minecraft:snow_block
fill -10 80 310 10 80 310 minecraft:air replace minecraft:snow_block
fill -10 80 291 -10 80 309 minecraft:air replace minecraft:snow_block
fill 10 80 291 10 80 309 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -8 76 292 8 76 292 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -8 76 308 8 76 308 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -8 76 293 -8 76 307 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill 8 76 293 8 76 307 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -6 72 294 6 72 294 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -6 72 306 6 72 306 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -6 72 295 -6 72 305 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill 6 72 295 6 72 305 minecraft:air replace minecraft:snow_block
