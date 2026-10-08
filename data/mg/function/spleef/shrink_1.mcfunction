# Spleef — rétrécissement, étape 1 : retire l'anneau extérieur de chaque étage (taille mini 9x9)
fill -14 80 286 14 80 286 minecraft:air replace minecraft:snow_block
fill -14 80 314 14 80 314 minecraft:air replace minecraft:snow_block
fill -14 80 287 -14 80 313 minecraft:air replace minecraft:snow_block
fill 14 80 287 14 80 313 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -12 76 288 12 76 288 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -12 76 312 12 76 312 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill -12 76 289 -12 76 311 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 2.. run fill 12 76 289 12 76 311 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -10 72 290 10 72 290 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -10 72 310 10 72 310 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill -10 72 291 -10 72 309 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 3.. run fill 10 72 291 10 72 309 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -8 68 292 8 68 292 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -8 68 308 8 68 308 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill -8 68 293 -8 68 307 minecraft:air replace minecraft:snow_block
execute if score $nf mg.st matches 4.. run fill 8 68 293 8 68 307 minecraft:air replace minecraft:snow_block
