# Spleef — rétrécissement, étape 1 : retire l'anneau extérieur de chaque étage (taille mini 9x9)
fill -14 80 286 14 80 286 minecraft:air replace minecraft:snow_block
fill -14 80 314 14 80 314 minecraft:air replace minecraft:snow_block
fill -14 80 287 -14 80 313 minecraft:air replace minecraft:snow_block
fill 14 80 287 14 80 313 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -12 73 288 12 73 288 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -12 73 312 12 73 312 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -12 73 289 -12 73 311 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill 12 73 289 12 73 311 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -10 66 290 10 66 290 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -10 66 310 10 66 310 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -10 66 291 -10 66 309 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill 10 66 291 10 66 309 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -8 59 292 8 59 292 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -8 59 308 8 59 308 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -8 59 293 -8 59 307 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill 8 59 293 8 59 307 minecraft:air replace minecraft:snow_block
