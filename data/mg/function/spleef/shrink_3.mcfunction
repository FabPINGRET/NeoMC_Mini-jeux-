# Spleef — rétrécissement, étape 3 : retire l'anneau extérieur de chaque étage (taille mini 9x9)
fill -12 80 288 12 80 288 minecraft:air replace minecraft:snow_block
fill -12 80 312 12 80 312 minecraft:air replace minecraft:snow_block
fill -12 80 289 -12 80 311 minecraft:air replace minecraft:snow_block
fill 12 80 289 12 80 311 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -10 73 290 10 73 290 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -10 73 310 10 73 310 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -10 73 291 -10 73 309 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill 10 73 291 10 73 309 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -8 66 292 8 66 292 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -8 66 308 8 66 308 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -8 66 293 -8 66 307 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill 8 66 293 8 66 307 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -6 59 294 6 59 294 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -6 59 306 6 59 306 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -6 59 295 -6 59 305 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill 6 59 295 6 59 305 minecraft:air replace minecraft:snow_block
