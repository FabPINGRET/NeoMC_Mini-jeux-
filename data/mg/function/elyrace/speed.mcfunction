# @s = joueur : chute de la vitesse horizontale d'un tick à l'autre (vérification de secours du choc contre un mur,
# si l'avancement ne se déclenche pas). La vitesse est mesurée par le carré de la norme (dx² + dz², en centièmes de bloc)
execute store result score #cx mg.st run data get entity @s Pos[0] 100
execute store result score #cz mg.st run data get entity @s Pos[2] 100
scoreboard players operation #dx mg.st = #cx mg.st
scoreboard players operation #dx mg.st -= @s mg.xb1
scoreboard players operation #dz mg.st = #cz mg.st
scoreboard players operation #dz mg.st -= @s mg.xb2
scoreboard players operation #vv mg.st = #dx mg.st
scoreboard players operation #vv mg.st *= #dx mg.st
scoreboard players operation #dz mg.st *= #dz mg.st
scoreboard players operation #vv mg.st += #dz mg.st
# pendant le délai (réapparition, mur déjà compté) la référence de vitesse est remise à zéro
execute if score @s mg.xk matches 1.. run scoreboard players set #vv mg.st 0
scoreboard players operation #wv mg.st = @s mg.xb3
scoreboard players operation #wv mg.st -= #vv mg.st
# seuil relatif : chute * 100 - précédent * 30 >= 0 (la chute doit représenter au moins 30 % du carré précédent)
scoreboard players operation #wq mg.st = #wv mg.st
scoreboard players operation #wq mg.st *= #k100 mg.st
scoreboard players operation #wp mg.st = @s mg.xb3
scoreboard players operation #wp mg.st *= #krel mg.st
scoreboard players operation #wq mg.st -= #wp mg.st
scoreboard players operation @s mg.xb1 = #cx mg.st
scoreboard players operation @s mg.xb2 = #cz mg.st
scoreboard players operation @s mg.xb3 = #vv mg.st
execute unless predicate mg:gliding run return 0
execute if score @s mg.xg matches 1.. run return 0
execute if score #wv mg.st matches 4000.. if score #wq mg.st matches 0.. run function mg:elyrace/wall
