# Tableau de droite hors mini-jeu : automatique (défaut) ou masqué ($sbo)
execute if score $sbo mg.st matches 1 run tellraw @s [{"text":"📊 Tableau de droite automatique : celui du spawn, de GTA, de Terra Nova ou de la survie selon où sont la plupart des joueurs (re-clique pour masquer).","color":"gold"}]
execute if score $sbo mg.st matches 1 run scoreboard players set $sbm mg.st -1
execute if score $sbo mg.st matches 1 run return run scoreboard players set $sbo mg.st 0
scoreboard players set $sbo mg.st 1
tellraw @s [{"text":"📊 Tableau de droite masqué hors mini-jeu.","color":"gray"}]
