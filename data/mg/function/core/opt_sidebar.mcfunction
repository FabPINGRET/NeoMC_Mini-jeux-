# Bascule l'affichage du classement des victoires
execute if score $sb mg.st matches 0 run scoreboard objectives setdisplay sidebar mg.wins
execute if score $sb mg.st matches 0 run tellraw @s [{"text":"Classement affiché à droite (re-clique pour masquer).","color":"gold"}]
execute if score $sb mg.st matches 0 run return run scoreboard players set $sb mg.st 1
scoreboard objectives setdisplay sidebar
scoreboard players set $sb mg.st 0
tellraw @s [{"text":"Classement masqué.","color":"gray"}]
