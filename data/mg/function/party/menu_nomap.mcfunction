execute if score $mp mg.st matches 1 run tellraw @s [{"text":"La carte est disponible sur le plateau.","color":"gray"}]
execute unless score $mp mg.st matches 1 run tellraw @s [{"text":"Aucune Mini Party en cours.","color":"gray"}]
scoreboard players set @s mg.dice 0
