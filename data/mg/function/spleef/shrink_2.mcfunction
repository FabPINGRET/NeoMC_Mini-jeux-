# Spleef — rétrécissement, étape 2 : retire l'anneau extérieur de chaque étage (taille mini 9x9)
fill -13 80 287 13 80 287 minecraft:air replace minecraft:snow_block
fill -13 80 313 13 80 313 minecraft:air replace minecraft:snow_block
fill -13 80 288 -13 80 312 minecraft:air replace minecraft:snow_block
fill 13 80 288 13 80 312 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -11 76 289 11 76 289 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -11 76 311 11 76 311 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -11 76 290 -11 76 310 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill 11 76 290 11 76 310 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -9 72 291 9 72 291 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -9 72 309 9 72 309 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -9 72 292 -9 72 308 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill 9 72 292 9 72 308 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -7 68 293 7 68 293 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -7 68 307 7 68 307 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -7 68 294 -7 68 306 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill 7 68 294 7 68 306 minecraft:air replace minecraft:snow_block
