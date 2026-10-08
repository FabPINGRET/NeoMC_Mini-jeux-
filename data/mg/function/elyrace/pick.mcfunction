# Parcours au hasard parmi les parcours construits (appelé par prepare quand $xc vaut 0) ; $xc reste à 0 si aucun n'est construit
scoreboard players set #n mg.st 0
execute if data storage mg:elyrace v1 run scoreboard players add #n mg.st 1
execute if data storage mg:elyrace c2v1 run scoreboard players add #n mg.st 1
execute if score #n mg.st matches 0 run return 0
# #r = rang tiré (0..#n-1) : le tirage couvre un multiple commun de 1..2 pour rester équitable
execute store result score #r mg.st run random value 0..1
scoreboard players operation #r mg.st %= #n mg.st
execute if data storage mg:elyrace v1 if score #r mg.st matches 0 run scoreboard players set $xc mg.st 1
execute if data storage mg:elyrace v1 run scoreboard players remove #r mg.st 1
execute if data storage mg:elyrace c2v1 if score #r mg.st matches 0 run scoreboard players set $xc mg.st 2
execute if data storage mg:elyrace c2v1 run scoreboard players remove #r mg.st 1
