# Spleef — rétrécissement, étape 3 : retire l'anneau extérieur de chaque étage (taille mini 9x9)
fill -12 80 288 12 80 288 minecraft:air replace minecraft:snow_block
fill -12 80 312 12 80 312 minecraft:air replace minecraft:snow_block
fill -12 80 289 -12 80 311 minecraft:air replace minecraft:snow_block
fill 12 80 289 12 80 311 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -10 76 290 10 76 290 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -10 76 310 10 76 310 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -10 76 291 -10 76 309 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill 10 76 291 10 76 309 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -8 72 292 8 72 292 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -8 72 308 8 72 308 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -8 72 293 -8 72 307 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill 8 72 293 8 72 307 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -6 68 294 6 68 294 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -6 68 306 6 68 306 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -6 68 295 -6 68 305 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill 6 68 295 6 68 305 minecraft:air replace minecraft:snow_block
