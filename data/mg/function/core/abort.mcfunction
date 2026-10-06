# Arrêt manuel de la partie (@s = joueur qui arrête)
tellraw @a [{"selector":"@s","color":"yellow"},{"text":" a arrêté la partie.","color":"red"}]
scoreboard players set $state mg.st 3
scoreboard players set $timer mg.st 20
