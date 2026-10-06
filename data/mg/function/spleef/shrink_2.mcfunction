# Spleef — rétrécissement, étape 2 : retire l'anneau extérieur de chaque étage (taille mini 9x9)
fill -13 80 287 13 80 287 minecraft:air replace minecraft:snow_block
fill -13 80 313 13 80 313 minecraft:air replace minecraft:snow_block
fill -13 80 288 -13 80 312 minecraft:air replace minecraft:snow_block
fill 13 80 288 13 80 312 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -11 73 289 11 73 289 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -11 73 311 11 73 311 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -11 73 290 -11 73 310 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill 11 73 290 11 73 310 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -9 66 291 9 66 291 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -9 66 309 9 66 309 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -9 66 292 -9 66 308 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill 9 66 292 9 66 308 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -7 59 293 7 59 293 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -7 59 307 7 59 307 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -7 59 294 -7 59 306 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill 7 59 294 7 59 306 minecraft:air replace minecraft:snow_block
